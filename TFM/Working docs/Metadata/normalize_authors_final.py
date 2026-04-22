#!/usr/bin/env python3
"""
Final Author Normalization Script for RIS files.

This script ensures ALL author names follow the exact format: LastName, F.
- All initials are separated by periods
- All author names end with a period after the last initial
- Handles edge cases and special characters
"""

import re
import os
import shutil

def normalize_author_name(author_name):
    """
    Normalize author name to format: LastName, F.
    Ensures ALL names end with a period after the last initial.
    """
    # Remove extra whitespace
    author_name = author_name.strip()
    
    # Handle empty names
    if not author_name:
        return author_name
    
    # Split by comma
    parts = [part.strip() for part in author_name.split(',')]
    
    if len(parts) >= 2:
        last_name = parts[0].strip()
        first_part = parts[1].strip()
        
        # Handle the initials part
        if first_part:
            # Remove all existing periods and spaces to start clean
            cleaned_initials = re.sub(r'[.\s]+', '', first_part)
            
            if cleaned_initials:
                # Add periods after each character (initial)
                normalized_initials = '.'.join(cleaned_initials) + '.'
                return f"{last_name}, {normalized_initials}"
            else:
                return f"{last_name},"
        else:
            return f"{last_name},"
    
    else:
        # Single part - try to parse as "FirstName LastName"
        name_parts = author_name.split()
        if len(name_parts) >= 2:
            *first_parts, last_name = name_parts
            initials = ''.join([part[0] for part in first_parts if part])
            if initials:
                normalized_initials = '.'.join(initials) + '.'
                return f"{last_name}, {normalized_initials}"
        
        return author_name  # Return as-is if can't parse

def normalize_single_ris_file(input_file):
    """
    Normalize author names in a single RIS file.
    """
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return 0, 0
    
    # Create backup
    backup_file = input_file + '.backup_final'
    shutil.copy2(input_file, backup_file)
    print(f"📦 Created backup: {backup_file}")
    
    normalized_count = 0
    total_authors = 0
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        normalized_lines = []
        
        for line in lines:
            if line.startswith('AU  - '):
                # Extract author name
                author_name = line[6:].strip()  # Remove 'AU  - ' prefix
                total_authors += 1
                
                # Normalize the author name
                normalized_name = normalize_author_name(author_name)
                
                # Check if normalization changed anything
                if normalized_name != author_name:
                    normalized_count += 1
                    print(f"  ✏️  {author_name} → {normalized_name}")
                else:
                    print(f"  ✅ {author_name} (already normalized)")
                
                # Create new line with normalized name
                normalized_lines.append(f"AU  - {normalized_name}\n")
            else:
                normalized_lines.append(line)
        
        # Write normalized content
        with open(input_file, 'w', encoding='utf-8') as f:
            f.writelines(normalized_lines)
        
        print(f"✅ Processed {total_authors} authors, normalized {normalized_count} names")
        return normalized_count, total_authors
        
    except Exception as e:
        print(f"❌ Error processing {input_file}: {e}")
        # Restore from backup if something went wrong
        if os.path.exists(backup_file):
            shutil.copy2(backup_file, input_file)
            print(f"🔄 Restored from backup due to error")
        return 0, 0

def main():
    """Process a single file specified as argument."""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python normalize_authors_final.py <filename>")
        print("Example: python normalize_authors_final.py 'RIS completos/metadataScopus3_completo.ris'")
        return
    
    file_path = sys.argv[1]
    
    print(f"🔄 Processing: {os.path.basename(file_path)}")
    print("=" * 60)
    
    normalized, total = normalize_single_ris_file(file_path)
    
    print("=" * 60)
    print(f"📊 Summary for {os.path.basename(file_path)}:")
    print(f"   Total authors: {total}")
    print(f"   Normalized: {normalized}")
    print(f"   Already correct: {total - normalized}")
    if total > 0:
        print(f"   Normalization rate: {(normalized/total)*100:.1f}%")
    print("\n🎉 Processing complete!")

if __name__ == "__main__":
    main() 