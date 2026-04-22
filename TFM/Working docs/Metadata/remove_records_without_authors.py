#!/usr/bin/env python3
"""
Script to remove records without authors from RIS files
Processes metadataScopus1.ris and metadataScopus2.ris only
"""

import re
import os
from datetime import datetime

def remove_records_without_authors(filename):
    """Remove records that don't have author information"""
    
    print(f"\n🔍 Processing {filename}...")
    
    # Read the file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        return False
    
    # Split into records using ER tag
    records = re.split(r'\n(ER  -.*?\n)', content)
    
    # Rebuild records with their ER tags
    full_records = []
    for i in range(0, len(records)-1, 2):
        if i+1 < len(records):
            full_records.append(records[i] + records[i+1])
        else:
            full_records.append(records[i])
    
    # Filter out records without authors
    records_with_authors = []
    removed_count = 0
    total_records = 0
    
    for record in full_records:
        if record.strip() and 'TY  -' in record:
            total_records += 1
            # Check if record has author information
            if re.search(r'^AU  -', record, re.MULTILINE):
                records_with_authors.append(record)
            else:
                removed_count += 1
                print(f"  📝 Removing record: {record.split('TI  -')[1].split('\\n')[0][:60] if 'TI  -' in record else 'No title'}...")
        elif record.strip():
            # Keep non-record content (headers, etc.)
            records_with_authors.append(record)
    
    # Create backup
    backup_name = f"{filename}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.rename(filename, backup_name)
    print(f"💾 Created backup: {backup_name}")
    
    # Write cleaned content
    cleaned_content = ''.join(records_with_authors)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"✅ Processed {filename}:")
    print(f"   📊 Total records: {total_records}")
    print(f"   ❌ Removed: {removed_count}")
    print(f"   ✅ Remaining: {total_records - removed_count}")
    
    return True

def main():
    """Main function to process the files"""
    
    print("🧹 Starting removal of records without authors...")
    print("=" * 60)
    
    files_to_process = ['metadataScopus1.ris', 'metadataScopus2.ris']
    
    total_removed = 0
    total_remaining = 0
    
    for filename in files_to_process:
        if os.path.exists(filename):
            # Count before processing
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            records = re.split(r'\nER  -.*?\n', content)
            original_count = len([r for r in records if r.strip() and 'TY  -' in r])
            
            # Process the file
            if remove_records_without_authors(filename):
                # Count after processing
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                records = re.split(r'\nER  -.*?\n', content)
                new_count = len([r for r in records if r.strip() and 'TY  -' in r])
                
                removed = original_count - new_count
                total_removed += removed
                total_remaining += new_count
        else:
            print(f"⚠️  File not found: {filename}")
    
    print("\n" + "=" * 60)
    print("📈 SUMMARY:")
    print(f"   📊 Total records removed: {total_removed}")
    print(f"   ✅ Total records remaining: {total_remaining}")
    print(f"   📁 Backup files created with timestamp")
    print("🎉 Processing complete!")

if __name__ == "__main__":
    main() 