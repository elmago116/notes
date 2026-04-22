#!/usr/bin/env python3
"""
RIS Missing Authors Enrichment Script
Automatically enriches RIS metadata files with missing authors using CrossRef API
"""

import requests
import time
import re
import os
from typing import Dict, List, Optional, Tuple
import argparse
from datetime import datetime

class RISRecord:
    """Represents a single RIS record"""
    def __init__(self):
        self.fields = {}
        self.raw_lines = []
        self.has_authors = False
        self.record_number = 0
        
    def add_field(self, tag: str, value: str):
        """Add a field to the record"""
        if tag in self.fields:
            if isinstance(self.fields[tag], list):
                self.fields[tag].append(value)
            else:
                self.fields[tag] = [self.fields[tag], value]
        else:
            self.fields[tag] = value
            
    def get_field(self, tag: str) -> Optional[str]:
        """Get field value, handling both single values and lists"""
        if tag not in self.fields:
            return None
        value = self.fields[tag]
        if isinstance(value, list):
            return value[0] if value else None
        return value
        
    def get_all_fields(self, tag: str) -> List[str]:
        """Get all values for a field (useful for authors)"""
        if tag not in self.fields:
            return []
        value = self.fields[tag]
        if isinstance(value, list):
            return value
        return [value] if value else []

class AuthorEnricher:
    """Main class for author enrichment"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RIS-Author-Enricher/1.0 (mailto:researcher@university.edu)',
            'Accept': 'application/json'
        })
        self.found_authors = 0
        self.processed_records = 0
        self.rate_limit_delay = 1.0  # seconds between requests
        
    def parse_ris_file(self, filename: str) -> List[RISRecord]:
        """Parse RIS file and return list of records"""
        records = []
        current_record = None
        record_count = 0
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.rstrip('\n\r')
                    
                    if line.startswith('TY  - '):
                        # Start of new record
                        if current_record:
                            current_record.record_number = record_count
                            records.append(current_record)
                        record_count += 1
                        current_record = RISRecord()
                        current_record.raw_lines.append(line)
                        current_record.add_field('TY', line[6:])
                        
                    elif line.startswith('ER  -'):
                        # End of record
                        if current_record:
                            current_record.raw_lines.append(line)
                            current_record.record_number = record_count
                            records.append(current_record)
                            current_record = None
                            
                    elif current_record and '  - ' in line:
                        # Field line
                        current_record.raw_lines.append(line)
                        tag = line[:2]
                        value = line[6:] if len(line) > 6 else ''
                        current_record.add_field(tag, value)
                        
                        # Check for author fields
                        if tag in ['AU', 'A1', 'A2', 'A3', 'A4'] and value.strip():
                            current_record.has_authors = True
                            
                    elif current_record:
                        # Continuation line or other content
                        current_record.raw_lines.append(line)
                        
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            return []
            
        print(f"Parsed {len(records)} records from {filename}")
        return records
    
    def clean_title(self, title: str) -> str:
        """Clean title for search"""
        if not title:
            return ""
        # Remove special characters and extra spaces
        title = re.sub(r'[^\w\s-]', ' ', title)
        title = re.sub(r'\s+', ' ', title)
        return title.strip()
    
    def search_crossref_authors(self, record: RISRecord) -> List[str]:
        """Search CrossRef API for authors"""
        title = record.get_field('TI')
        if not title:
            return []
            
        title = self.clean_title(title)
        year = record.get_field('PY')
        doi = record.get_field('DO')
        
        try:
            # If we have a DOI, search by DOI first (most accurate)
            if doi and doi != 'No DOI':
                return self.search_by_doi(doi)
            
            # Otherwise search by title and year
            return self.search_by_title_year(title, year)
                            
        except Exception as e:
            print(f"  ✗ CrossRef search error: {e}")
            return []
    
    def search_by_doi(self, doi: str) -> List[str]:
        """Search CrossRef by DOI"""
        url = f"https://api.crossref.org/works/{doi}"
        
        response = self.session.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if 'message' in data:
            item = data['message']
            return self.extract_authors_from_crossref_item(item)
        
        return []
    
    def search_by_title_year(self, title: str, year: str) -> List[str]:
        """Search CrossRef by title and year"""
        query_parts = [title]
        if year:
            query_parts.append(year)
            
        query = ' '.join(query_parts)
        
        url = f"https://api.crossref.org/works"
        params = {
            'query': query,
            'rows': 3,
            'sort': 'relevance'
        }
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if 'message' in data and 'items' in data['message']:
            items = data['message']['items']
            
            for item in items:
                # Check if this looks like a match
                if self.is_good_title_match(title, item, year):
                    return self.extract_authors_from_crossref_item(item)
                    
        return []
    
    def extract_authors_from_crossref_item(self, item: Dict) -> List[str]:
        """Extract authors from CrossRef item"""
        authors = []
        
        if 'author' in item:
            for author in item['author']:
                # Format: "Last, First" or "Last, F."
                family = author.get('family', '')
                given = author.get('given', '')
                
                if family:
                    if given:
                        # Try to abbreviate first name if it's long
                        if len(given.split()) > 1:
                            # Multiple names, take first letters
                            initials = '. '.join([name[0] for name in given.split() if name]) + '.'
                            author_name = f"{family}, {initials}"
                        else:
                            author_name = f"{family}, {given[0]}." if len(given) > 1 else f"{family}, {given}"
                    else:
                        author_name = family
                    authors.append(author_name)
        
        return authors
    
    def is_good_title_match(self, record_title: str, crossref_item: Dict, year: str = None) -> bool:
        """Check if CrossRef result is a good match"""
        record_title = self.clean_title(record_title).lower()
        crossref_title = ''
        
        if 'title' in crossref_item and crossref_item['title']:
            crossref_title = self.clean_title(crossref_item['title'][0]).lower()
        
        if not record_title or not crossref_title:
            return False
            
        # Simple title similarity check
        record_words = set(record_title.split())
        crossref_words = set(crossref_title.split())
        
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'proceedings', 'conference', 'international'}
        record_words -= common_words
        crossref_words -= common_words
        
        if len(record_words) == 0 or len(crossref_words) == 0:
            return False
            
        # Calculate similarity
        intersection = len(record_words.intersection(crossref_words))
        union = len(record_words.union(crossref_words))
        similarity = intersection / union if union > 0 else 0
        
        # Check year match if available
        year_match = True
        if year and 'published-print' in crossref_item:
            try:
                crossref_year = str(crossref_item['published-print']['date-parts'][0][0])
                year_match = year == crossref_year
            except:
                year_match = True  # Don't exclude if year parsing fails
        
        # Lower threshold for title similarity since conference proceedings can be tricky
        return similarity > 0.4 and year_match
    
    def enrich_record(self, record: RISRecord) -> bool:
        """Enrich a single record with authors"""
        if record.has_authors:
            return False
            
        title = record.get_field('TI')
        if not title:
            print(f"  ⚠ Skipping record without title")
            return False
            
        print(f"  📖 Searching authors for: {title[:80]}...")
        
        # Rate limiting
        time.sleep(self.rate_limit_delay)
        
        authors = self.search_crossref_authors(record)
        
        if authors:
            # Add authors to the record
            self.add_authors_to_record(record, authors)
            self.found_authors += len(authors)
            print(f"  ✓ Found {len(authors)} authors: {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''}")
            return True
        else:
            print(f"  ✗ No authors found")
            return False
    
    def add_authors_to_record(self, record: RISRecord, authors: List[str]):
        """Add author fields to RIS record"""
        # Find where to insert the author fields (typically after title or type)
        new_lines = []
        authors_added = False
        
        for line in record.raw_lines:
            new_lines.append(line)
            
            # Add authors after title field
            if line.startswith('TI  - ') and not authors_added:
                for author in authors:
                    new_lines.append(f'AU  - {author}')
                authors_added = True
                
        # If no title found, add authors after type
        if not authors_added:
            new_lines_with_authors = []
            for line in record.raw_lines:
                new_lines_with_authors.append(line)
                if line.startswith('TY  - ') and not authors_added:
                    for author in authors:
                        new_lines_with_authors.append(f'AU  - {author}')
                    authors_added = True
            new_lines = new_lines_with_authors
                
        record.raw_lines = new_lines
        record.has_authors = True
        for author in authors:
            record.add_field('AU', author)
    
    def save_enriched_file(self, records: List[RISRecord], original_filename: str):
        """Save enriched records to new file in 'RIS completos' directory"""
        # Create output directory
        output_dir = "RIS completos"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"📁 Created directory: {output_dir}")
        
        # Generate output filename
        base_name = os.path.basename(original_filename)
        name_without_ext = os.path.splitext(base_name)[0]
        output_filename = os.path.join(output_dir, f"{name_without_ext}_authors_enriched.ris")
        
        # Save enriched version
        with open(output_filename, 'w', encoding='utf-8') as f:
            for record in records:
                for line in record.raw_lines:
                    f.write(line + '\n')
                    
        print(f"💾 Enriched file saved: {output_filename}")
        return output_filename
    
    def enrich_file(self, filename: str) -> Dict:
        """Enrich a single RIS file with missing authors"""
        print(f"\n🔍 Processing: {filename}")
        
        records = self.parse_ris_file(filename)
        if not records:
            return {'error': 'Failed to parse file'}
            
        total_records = len(records)
        records_without_authors = [r for r in records if not r.has_authors]
        
        print(f"📊 Total records: {total_records}")
        print(f"📊 Records without authors: {len(records_without_authors)}")
        
        if len(records_without_authors) == 0:
            print("✅ All records already have authors!")
            return {
                'total': total_records,
                'without_authors': 0,
                'enriched': 0,
                'output_file': None
            }
        
        enriched_count = 0
        
        for i, record in enumerate(records_without_authors, 1):
            print(f"\n[{i}/{len(records_without_authors)}]")
            if self.enrich_record(record):
                enriched_count += 1
                
        # Save enriched file
        output_file = self.save_enriched_file(records, filename)
        
        return {
            'total': total_records,
            'without_authors': len(records_without_authors),
            'enriched': enriched_count,
            'output_file': output_file
        }

def main():
    parser = argparse.ArgumentParser(description='Enrich RIS files with missing authors')
    parser.add_argument('files', nargs='+', help='RIS files to process')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between API requests (seconds)')
    
    args = parser.parse_args()
    
    enricher = AuthorEnricher()
    enricher.rate_limit_delay = args.delay
    
    total_stats = {'total': 0, 'without_authors': 0, 'enriched': 0}
    output_files = []
    
    print("🚀 Starting Author enrichment process...")
    print("📁 Enriched files will be saved to 'RIS completos' directory")
    start_time = time.time()
    
    for filename in args.files:
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}")
            continue
            
        stats = enricher.enrich_file(filename)
        
        if 'error' not in stats:
            total_stats['total'] += stats['total']
            total_stats['without_authors'] += stats['without_authors']
            total_stats['enriched'] += stats['enriched']
            if stats.get('output_file'):
                output_files.append(stats['output_file'])
    
    end_time = time.time()
    
    print(f"\n🎉 Author Enrichment Complete!")
    print(f"⏰ Time taken: {end_time - start_time:.1f} seconds")
    print(f"📊 Total records processed: {total_stats['total']}")
    print(f"📊 Records without authors: {total_stats['without_authors']}")
    print(f"📊 Authors found and added: {total_stats['enriched']}")
    if total_stats['without_authors'] > 0:
        print(f"📊 Success rate: {total_stats['enriched']/total_stats['without_authors']*100:.1f}%")
    
    if output_files:
        print(f"\n📁 Enriched files created:")
        for output_file in output_files:
            print(f"   ✓ {output_file}")
        print(f"\n💡 Original files remain unchanged in current directory.")

if __name__ == "__main__":
    main() 