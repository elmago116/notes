#!/usr/bin/env python3
"""
Citizen Science Keywords Scout
Date of creation: 2025-01-27

This script extracts keywords related to citizen science from a RIS document.
It searches for citizen science related terms and compiles a comprehensive list.
"""

import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

def load_ris_file(file_path):
    """Load and parse RIS file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_citizen_science_keywords(ris_content):
    """Extract citizen science related keywords from RIS content."""
    
    # Define citizen science related patterns (case-insensitive)
    citizen_science_patterns = [
        # Core citizen science terms
        r'citizen science',
        r'crowdsourcing',
        r'crowd-sourcing',
        r'crowd sourcing',
        r'volunteer',
        r'participatory',
        r'community-based',
        r'public participation',
        r'public engagement',
        r'citizen scientist',
        r'citizen scientists',
        
        # Related concepts
        r'community science',
        r'community engagement',
        r'community participation',
        r'public science',
        r'volunteer monitoring',
        r'volunteer science',
        r'participatory science',
        r'participatory research',
        r'participatory monitoring',
        r'participatory observation',
        r'collaborative science',
        r'collaborative research',
        r'open science',
        r'open research',
        r'distributed research',
        r'distributed science',
        
        # Specific domains
        r'citizen journalism',
        r'citizen reporting',
        r'volunteer computing',
        r'volunteer thinking',
        r'participatory sensing',
        r'participatory mapping',
        r'participatory GIS',
        r'community mapping',
        r'crowd mapping',
        r'crowdsourced data',
        r'volunteer data',
        r'community data',
        
        # Digital platforms
        r'Zooniverse',
        r'Foldit',
        r'Galaxy Zoo',
        r'iNaturalist',
        r'eBird',
        r'citizen observatory',
        r'citizen observatories',
    ]
    
    # Compile patterns for case-insensitive matching
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in citizen_science_patterns]
    
    # Extract keywords from different RIS fields
    keywords_found = defaultdict(set)
    
    # Split content by records (separated by ER -)
    records = re.split(r'ER\s*-\s*\n', ris_content)
    
    for i, record in enumerate(records):
        if not record.strip():
            continue
            
        # Extract different fields
        title_match = re.search(r'TI\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        abstract_match = re.search(r'AB\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        keywords_match = re.search(r'KW\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        
        record_text = ""
        if title_match:
            record_text += " " + title_match.group(1)
        if abstract_match:
            record_text += " " + abstract_match.group(1)
        if keywords_match:
            record_text += " " + keywords_match.group(1)
        
        # Search for patterns in this record
        for pattern in compiled_patterns:
            matches = pattern.findall(record_text)
            for match in matches:
                keywords_found[match.lower()].add(i)
    
    return keywords_found

def format_keywords_output(keywords_found):
    """Format the found keywords into a readable output."""
    
    # Sort keywords by frequency (number of records containing them)
    sorted_keywords = sorted(keywords_found.items(), key=lambda x: len(x[1]), reverse=True)
    
    output = []
    output.append("# Citizen Science Keywords Found in RIS Document")
    output.append(f"Date of analysis: 2025-01-27")
    output.append(f"Total unique citizen science related terms: {len(keywords_found)}")
    output.append("")
    
    output.append("## Keywords by Frequency")
    output.append("")
    
    for keyword, record_indices in sorted_keywords:
        frequency = len(record_indices)
        output.append(f"- **{keyword}** (found in {frequency} records)")
        if frequency <= 10:  # Show record numbers for less frequent terms
            record_list = sorted(list(record_indices))
            output.append(f"  - Records: {', '.join(map(str, record_list))}")
        output.append("")
    
    output.append("## Alphabetical List")
    output.append("")
    
    # Alphabetical list
    alphabetical_keywords = sorted(keywords_found.keys())
    for keyword in alphabetical_keywords:
        frequency = len(keywords_found[keyword])
        output.append(f"- {keyword} ({frequency} occurrences)")
    
    return "\n".join(output)

def main():
    """Main function to run the citizen science keywords scout."""
    
    # Path to the RIS file
    ris_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris"
    
    print("Citizen Science Keywords Scout")
    print("=" * 40)
    print(f"Date of execution: 2025-01-27")
    print(f"Analyzing file: {ris_file_path}")
    print()
    
    # Load RIS file
    print("Loading RIS file...")
    ris_content = load_ris_file(ris_file_path)
    if ris_content is None:
        sys.exit(1)
    
    print(f"File loaded successfully. Content length: {len(ris_content)} characters")
    print()
    
    # Extract citizen science keywords
    print("Extracting citizen science related keywords...")
    keywords_found = extract_citizen_science_keywords(ris_content)
    
    if not keywords_found:
        print("No citizen science related keywords found in the document.")
        return
    
    print(f"Found {len(keywords_found)} unique citizen science related terms")
    print()
    
    # Format and display results
    formatted_output = format_keywords_output(keywords_found)
    
    # Save results to file
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_keywords_list.md"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
    
    # Display summary
    print("\n" + "=" * 40)
    print("SUMMARY")
    print("=" * 40)
    print(f"Total unique citizen science terms found: {len(keywords_found)}")
    
    # Show top 10 most frequent terms
    sorted_keywords = sorted(keywords_found.items(), key=lambda x: len(x[1]), reverse=True)
    print("\nTop 10 most frequent terms:")
    for i, (keyword, record_indices) in enumerate(sorted_keywords[:10], 1):
        print(f"{i:2d}. {keyword} ({len(record_indices)} records)")
    
    print(f"\nComplete results saved to: {output_file}")

if __name__ == "__main__":
    main()




