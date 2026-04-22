#!/usr/bin/env python3
"""
Script to normalize author names in RIS files.

This script reads RIS files and normalizes the author names (AU fields) to a consistent format:
- LastName, F. (with period after each initial)
- Handles multiple initials properly
- Preserves special characters and diacritics
- Creates backup files before modification
"""

import re
import os
import shutil
from pathlib import Path

def normalize_author_name(author_name):
    """
    Normalize author name to format: LastName, F.
    
    Args:
        author_name (str): Original author name
        
    Returns:
        str: Normalized author name
    """
    # Remove extra whitespace
    author_name = author_name.strip()
    
    # Handle empty names
    if not author_name:
        return author_name
    
    # Split by comma
    parts = [part.strip() for part in author_name.split(',')]
    
    if len(parts) == 2:
        last_name, first_part = parts
        
        # Process the first part (initials/first name)
        # Remove existing periods and spaces to start clean
        first_part = re.sub(r'[.\s]+', '', first_part)
        
        # Add periods after each character (assuming they are initials)
        if first_part:
            # Handle multiple initials
            normalized_initials = '.'.join(first_part) + '.'
            return f"{last_name}, {normalized_initials}"
        else:
            return f"{last_name},"
    
    elif len(parts) == 1:
        # Handle cases where there's no comma (shouldn't happen in RIS but just in case)
        # Try to split by space and assume last part is surname
        name_parts = author_name.split()
        if len(name_parts) >= 2:
            *first_parts, last_name = name_parts
            initials = ''.join([part[0] for part in first_parts if part])
            if initials:
                normalized_initials = '.'.join(initials) + '.'
                return f"{last_name}, {normalized_initials}"
        return author_name  # Return as-is if can't parse
    
    else:
        # More than 2 parts - join all but the last as first name, last as surname
        *first_parts, last_name = parts
        first_part = ' '.join(first_parts)
        first_part = re.sub(r'[.\s]+', '', first_part)
        if first_part:
            normalized_initials = '.'.join(first_part) + '.'
            return f"{last_name}, {normalized_initials}"
        else:
            return f"{last_name},"

def normalize_ris_file(input_file, output_file=None):
    """
    Normalize author names in a RIS file.
    
    Args:
        input_file (str): Path to input RIS file
        output_file (str): Path to output RIS file (if None, overwrites input)
    """
    if output_file is None:
        output_file = input_file
    
    # Create backup
    backup_file = input_file + '.backup'
    shutil.copy2(input_file, backup_file)
    print(f"Created backup: {backup_file}")
    
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
                    print(f"  {author_name} -> {normalized_name}")
                
                # Create new line with normalized name
                normalized_lines.append(f"AU  - {normalized_name}\n")
            else:
                normalized_lines.append(line)
        
        # Write normalized content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(normalized_lines)
        
        print(f"Processed {total_authors} authors, normalized {normalized_count} names")
        return normalized_count, total_authors
        
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        # Restore from backup if something went wrong
        if os.path.exists(backup_file):
            shutil.copy2(backup_file, input_file)
            print(f"Restored from backup due to error")
        return 0, 0

def main():
    """Main function to process all specified RIS files."""
    
    # List of files to process
    files_to_process = [
        "RIS completos/metadataScopus3_completo.ris",
        "RIS completos/metadataWoS1_completo.ris", 
        "RIS completos/metadataWoS1+_completo.ris",
        "RIS completos/metadataWoS2_completo.ris",
        "RIS completos/metadataWoS3_completo.ris"
    ]
    
    total_normalized = 0
    total_authors = 0
    
    print("Starting author name normalization...")
    print("=" * 50)
    
    for file_path in files_to_process:
        if os.path.exists(file_path):
            print(f"\nProcessing: {os.path.basename(file_path)}")
            normalized, authors = normalize_ris_file(file_path)
            total_normalized += normalized
            total_authors += authors
        else:
            print(f"File not found: {file_path}")
    
    print("=" * 50)
    print(f"Summary:")
    print(f"Total authors processed: {total_authors}")
    print(f"Total authors normalized: {total_normalized}")
    print(f"Normalization rate: {(total_normalized/total_authors)*100:.1f}%" if total_authors > 0 else "No authors found")
    print("\nBackup files (.backup) have been created for all processed files.")

if __name__ == "__main__":
    main() 