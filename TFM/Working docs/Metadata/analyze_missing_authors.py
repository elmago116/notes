#!/usr/bin/env python3
"""
RIS Missing Authors Analysis Script
Analyzes RIS metadata files to identify records missing author information
and provides statistics about author coverage
"""

import os
import re
from typing import Dict, List, Optional, Tuple
import argparse
from collections import defaultdict

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

class MissingAuthorsAnalyzer:
    """Analyzes RIS files for missing author information"""
    
    def __init__(self):
        self.total_records = 0
        self.records_without_authors = 0
        self.files_stats = {}
        
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
                        
                        # Check for author fields (AU, A1, A2, A3, A4)
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
    
    def analyze_file(self, filename: str) -> Dict:
        """Analyze a single RIS file for missing authors"""
        print(f"\n🔍 Analyzing: {filename}")
        
        records = self.parse_ris_file(filename)
        if not records:
            return {'error': 'Failed to parse file'}
            
        total_records = len(records)
        records_without_authors = [r for r in records if not r.has_authors]
        records_with_authors = [r for r in records if r.has_authors]
        
        # Analyze types of records without authors
        types_without_authors = defaultdict(int)
        missing_author_samples = []
        
        for record in records_without_authors[:10]:  # Sample first 10
            record_type = record.get_field('TY') or 'Unknown'
            types_without_authors[record_type] += 1
            
            title = record.get_field('TI') or 'No title'
            year = record.get_field('PY') or 'No year'
            doi = record.get_field('DO') or 'No DOI'
            
            missing_author_samples.append({
                'record_num': record.record_number,
                'type': record_type,
                'title': title[:100] + '...' if len(title) > 100 else title,
                'year': year,
                'doi': doi
            })
        
        # Count total types without authors
        for record in records_without_authors:
            record_type = record.get_field('TY') or 'Unknown'
            types_without_authors[record_type] += 1
        
        stats = {
            'filename': filename,
            'total': total_records,
            'with_authors': len(records_with_authors),
            'without_authors': len(records_without_authors),
            'coverage_percentage': (len(records_with_authors) / total_records * 100) if total_records > 0 else 0,
            'types_without_authors': dict(types_without_authors),
            'samples': missing_author_samples
        }
        
        self.files_stats[filename] = stats
        self.total_records += total_records
        self.records_without_authors += len(records_without_authors)
        
        return stats
    
    def print_file_analysis(self, stats: Dict):
        """Print analysis results for a single file"""
        if 'error' in stats:
            print(f"❌ {stats['error']}")
            return
            
        print(f"📊 Total records: {stats['total']}")
        print(f"📊 Records with authors: {stats['with_authors']} ({stats['coverage_percentage']:.1f}%)")
        print(f"📊 Records without authors: {stats['without_authors']} ({100-stats['coverage_percentage']:.1f}%)")
        
        if stats['without_authors'] > 0:
            print(f"\n📋 Types of records missing authors:")
            for record_type, count in sorted(stats['types_without_authors'].items(), key=lambda x: x[1], reverse=True):
                print(f"   • {record_type}: {count} records")
            
            print(f"\n📝 Sample records without authors (first 10):")
            for i, sample in enumerate(stats['samples'], 1):
                print(f"   {i}. [{sample['record_num']}] {sample['type']} ({sample['year']})")
                print(f"      Title: {sample['title']}")
                print(f"      DOI: {sample['doi']}")
                print()
    
    def analyze_all_files(self, filenames: List[str]):
        """Analyze all specified RIS files"""
        print("🚀 Starting Missing Authors Analysis...")
        print("="*60)
        
        for filename in filenames:
            if not os.path.exists(filename):
                print(f"❌ File not found: {filename}")
                continue
                
            stats = self.analyze_file(filename)
            self.print_file_analysis(stats)
            print("-" * 60)
        
        self.print_summary()
    
    def print_summary(self):
        """Print overall summary across all files"""
        print("\n🎯 OVERALL SUMMARY")
        print("="*60)
        print(f"📊 Total files analyzed: {len(self.files_stats)}")
        print(f"📊 Total records across all files: {self.total_records}")
        print(f"📊 Total records without authors: {self.records_without_authors}")
        
        overall_coverage = ((self.total_records - self.records_without_authors) / self.total_records * 100) if self.total_records > 0 else 0
        print(f"📊 Overall author coverage: {overall_coverage:.1f}%")
        
        print(f"\n📋 Author coverage by file:")
        for filename, stats in self.files_stats.items():
            coverage = stats['coverage_percentage']
            status = "✅" if coverage >= 90 else "⚠️" if coverage >= 75 else "❌"
            print(f"   {status} {os.path.basename(filename)}: {coverage:.1f}% ({stats['without_authors']} missing)")
        
        # Find most common record types without authors
        all_types = defaultdict(int)
        for stats in self.files_stats.values():
            for record_type, count in stats['types_without_authors'].items():
                all_types[record_type] += count
        
        if all_types:
            print(f"\n📋 Most common record types missing authors (across all files):")
            for record_type, count in sorted(all_types.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"   • {record_type}: {count} records")
    
    def export_missing_authors_report(self, output_filename: str = "missing_authors_report.txt"):
        """Export detailed report of missing authors"""
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("MISSING AUTHORS ANALYSIS REPORT\n")
            f.write("="*50 + "\n\n")
            
            for filename, stats in self.files_stats.items():
                f.write(f"FILE: {filename}\n")
                f.write(f"Total records: {stats['total']}\n")
                f.write(f"Records without authors: {stats['without_authors']} ({100-stats['coverage_percentage']:.1f}%)\n\n")
                
                if stats['samples']:
                    f.write("Sample records without authors:\n")
                    for sample in stats['samples']:
                        f.write(f"  [{sample['record_num']}] {sample['type']} ({sample['year']})\n")
                        f.write(f"    Title: {sample['title']}\n")
                        f.write(f"    DOI: {sample['doi']}\n\n")
                
                f.write("-" * 40 + "\n\n")
        
        print(f"📄 Detailed report exported to: {output_filename}")

def main():
    parser = argparse.ArgumentParser(description='Analyze RIS files for missing author information')
    parser.add_argument('files', nargs='+', help='RIS files to analyze')
    parser.add_argument('--export-report', action='store_true', help='Export detailed report to file')
    
    args = parser.parse_args()
    
    analyzer = MissingAuthorsAnalyzer()
    analyzer.analyze_all_files(args.files)
    
    if args.export_report:
        analyzer.export_missing_authors_report()

if __name__ == "__main__":
    main() 