#!/usr/bin/env python3
"""
RIS DOI Enrichment Script
Automatically enriches RIS metadata files with missing DOIs using CrossRef API
"""

import requests
import time
import re
import sys
import os
from typing import Dict, List, Optional, Tuple
import json
from urllib.parse import quote
import argparse
from datetime import datetime

class RISRecord:
    """Represents a single RIS record"""
    def __init__(self):
        self.fields = {}
        self.raw_lines = []
        self.has_doi = False
        
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

class DOIEnricher:
    """Main class for DOI enrichment"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RIS-DOI-Enricher/1.0 (mailto:researcher@university.edu)',
            'Accept': 'application/json'
        })
        self.found_dois = 0
        self.processed_records = 0
        self.rate_limit_delay = 1.0  # seconds between requests
        
    def parse_ris_file(self, filename: str) -> List[RISRecord]:
        """Parse RIS file and return list of records"""
        records = []
        current_record = None
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.rstrip('\n\r')
                    
                    if line.startswith('TY  - '):
                        # Start of new record
                        if current_record:
                            records.append(current_record)
                        current_record = RISRecord()
                        current_record.raw_lines.append(line)
                        current_record.add_field('TY', line[6:])
                        
                    elif line.startswith('ER  -'):
                        # End of record
                        if current_record:
                            current_record.raw_lines.append(line)
                            records.append(current_record)
                            current_record = None
                            
                    elif current_record and '  - ' in line:
                        # Field line
                        current_record.raw_lines.append(line)
                        tag = line[:2]
                        value = line[6:] if len(line) > 6 else ''
                        current_record.add_field(tag, value)
                        
                        if tag == 'DO':
                            current_record.has_doi = True
                            
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
    
    def search_crossref_doi(self, record: RISRecord) -> Optional[str]:
        """Search CrossRef API for DOI"""
        title = record.get_field('TI')
        if not title:
            return None
            
        title = self.clean_title(title)
        authors = record.get_all_fields('AU')
        year = record.get_field('PY')
        
        # Build search query
        query_parts = [title]
        
        if authors and len(authors) > 0:
            # Add first author's last name
            first_author = authors[0]
            if ',' in first_author:
                last_name = first_author.split(',')[0].strip()
                query_parts.append(last_name)
        
        if year:
            query_parts.append(year)
            
        query = ' '.join(query_parts)
        
        try:
            # Search CrossRef
            url = f"https://api.crossref.org/works"
            params = {
                'query': query,
                'rows': 5,
                'sort': 'relevance'
            }
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if 'message' in data and 'items' in data['message']:
                items = data['message']['items']
                
                for item in items:
                    # Check if this looks like a match
                    if self.is_good_match(record, item):
                        doi = item.get('DOI')
                        if doi:
                            print(f"  ✓ Found DOI: {doi}")
                            return doi
                            
        except Exception as e:
            print(f"  ✗ CrossRef search error: {e}")
            
        return None
    
    def is_good_match(self, record: RISRecord, crossref_item: Dict) -> bool:
        """Check if CrossRef result is a good match"""
        record_title = self.clean_title(record.get_field('TI') or '').lower()
        crossref_title = ''
        
        if 'title' in crossref_item and crossref_item['title']:
            crossref_title = self.clean_title(crossref_item['title'][0]).lower()
        
        if not record_title or not crossref_title:
            return False
            
        # Simple title similarity check
        record_words = set(record_title.split())
        crossref_words = set(crossref_title.split())
        
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were'}
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
        record_year = record.get_field('PY')
        if record_year and 'published-print' in crossref_item:
            crossref_year = str(crossref_item['published-print']['date-parts'][0][0])
            year_match = record_year == crossref_year
        
        # Require high similarity and year match
        return similarity > 0.6 and year_match
    
    def enrich_record(self, record: RISRecord) -> bool:
        """Enrich a single record with DOI"""
        if record.has_doi:
            return False
            
        title = record.get_field('TI')
        if not title:
            print(f"  ⚠ Skipping record without title")
            return False
            
        print(f"  📖 Searching: {title[:80]}...")
        
        # Rate limiting
        time.sleep(self.rate_limit_delay)
        
        doi = self.search_crossref_doi(record)
        
        if doi:
            # Add DOI to the record
            self.add_doi_to_record(record, doi)
            self.found_dois += 1
            return True
        else:
            print(f"  ✗ No DOI found")
            return False
    
    def add_doi_to_record(self, record: RISRecord, doi: str):
        """Add DOI field to RIS record"""
        # Find where to insert the DOI field (typically after title)
        new_lines = []
        doi_added = False
        
        for line in record.raw_lines:
            new_lines.append(line)
            
            # Add DOI after title field
            if line.startswith('TI  - ') and not doi_added:
                new_lines.append(f'DO  - {doi}')
                doi_added = True
                
        # If no title found, add DOI before ER
        if not doi_added:
            # Insert before ER line
            if new_lines and new_lines[-1].startswith('ER  -'):
                new_lines.insert(-1, f'DO  - {doi}')
            else:
                new_lines.append(f'DO  - {doi}')
                
        record.raw_lines = new_lines
        record.has_doi = True
        record.add_field('DO', doi)
    
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
        output_filename = os.path.join(output_dir, f"{name_without_ext}_completo.ris")
        
        # Save enriched version
        with open(output_filename, 'w', encoding='utf-8') as f:
            for record in records:
                for line in record.raw_lines:
                    f.write(line + '\n')
                    
        print(f"💾 Enriched file saved: {output_filename}")
        return output_filename
    
    def enrich_file(self, filename: str) -> Dict:
        """Enrich a single RIS file"""
        print(f"\n🔍 Processing: {filename}")
        
        records = self.parse_ris_file(filename)
        if not records:
            return {'error': 'Failed to parse file'}
            
        records_without_doi = [r for r in records if not r.has_doi]
        
        print(f"📊 Total records: {len(records)}")
        print(f"📊 Records without DOI: {len(records_without_doi)}")
        
        if len(records_without_doi) == 0:
            print("✅ All records already have DOIs!")
            return {'total': len(records), 'without_doi': 0, 'enriched': 0}
        
        enriched_count = 0
        output_file = None
        
        for i, record in enumerate(records_without_doi, 1):
            print(f"\n[{i}/{len(records_without_doi)}]")
            if self.enrich_record(record):
                enriched_count += 1
                
        # Always save the file (even if no DOIs were found, for completeness)
        output_file = self.save_enriched_file(records, filename)
            
        return {
            'total': len(records),
            'without_doi': len(records_without_doi),
            'enriched': enriched_count,
            'output_file': output_file
        }

def main():
    parser = argparse.ArgumentParser(description='Enrich RIS files with missing DOIs')
    parser.add_argument('files', nargs='+', help='RIS files to process')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between API requests (seconds)')
    
    args = parser.parse_args()
    
    enricher = DOIEnricher()
    enricher.rate_limit_delay = args.delay
    
    total_stats = {'total': 0, 'without_doi': 0, 'enriched': 0}
    output_files = []
    
    print("🚀 Starting DOI enrichment process...")
    print("📁 Enriched files will be saved to 'RIS completos' directory")
    start_time = time.time()
    
    for filename in args.files:
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}")
            continue
            
        stats = enricher.enrich_file(filename)
        
        if 'error' not in stats:
            total_stats['total'] += stats['total']
            total_stats['without_doi'] += stats['without_doi']
            total_stats['enriched'] += stats['enriched']
            if stats.get('output_file'):
                output_files.append(stats['output_file'])
    
    end_time = time.time()
    
    print(f"\n🎉 Enrichment Complete!")
    print(f"⏰ Time taken: {end_time - start_time:.1f} seconds")
    print(f"📊 Total records processed: {total_stats['total']}")
    print(f"📊 Records without DOI: {total_stats['without_doi']}")
    print(f"📊 DOIs found and added: {total_stats['enriched']}")
    print(f"📊 Success rate: {total_stats['enriched']/total_stats['without_doi']*100:.1f}%" if total_stats['without_doi'] > 0 else "N/A")
    
    if output_files:
        print(f"\n📁 Enriched files created:")
        for output_file in output_files:
            print(f"   ✓ {output_file}")
        print(f"\n💡 Original files remain unchanged in current directory.")

if __name__ == "__main__":
    main()
