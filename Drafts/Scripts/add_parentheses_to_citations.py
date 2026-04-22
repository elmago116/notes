#!/usr/bin/env python3
"""
Add Parentheses to Citation Labels in Draft Links
==================================================

Updates links that have citation labels (without parentheses) to wrap them in parentheses.

Usage:
    python3 add_parentheses_to_citations.py "Draft File Name.md"

Author: AI Assistant
Date: 2025-01-XX
"""

import re
import sys
from pathlib import Path

# Configuration
DRAFTS_DIR = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts")

def add_parentheses_to_citations(input_file: Path) -> None:
    """Add parentheses to citation labels in links."""
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        return
    
    # Read original content
    original = input_file.read_text(encoding='utf-8')
    content = original
    
    # Pattern to match links with citation labels (not starting with parentheses or X)
    # Matches: [[link|Author, Year]] but not [[link|(Author, Year)]] or [[link|X]]
    link_pattern = r'\[\[([^\]]+)\|([^X\(][^\]]+)\]\]'
    
    def replace_with_parentheses(match):
        full_match = match.group(0)
        link_body = match.group(1)
        citation_label = match.group(2).strip()
        
        # Skip if already has parentheses or is just "X" or "XY"
        if citation_label.startswith('(') or citation_label.upper() in ['X', 'XY']:
            return full_match
        
        # Wrap in parentheses
        new_label = f"({citation_label})"
        return f"[[{link_body}|{new_label}]]"
    
    # Apply replacements
    content = re.sub(link_pattern, replace_with_parentheses, content)
    
    # Count changes
    if content != original:
        input_file.write_text(content, encoding='utf-8')
        changes = len(re.findall(link_pattern, original))
        print(f"Updated {changes} citation labels with parentheses")
        print(f"Updated file: {input_file.name}")
    else:
        print("No changes needed - all citations already have parentheses or are placeholders")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add_parentheses_to_citations.py \"Draft File Name.md\"")
        print("\nExample:")
        print('  python3 add_parentheses_to_citations.py "General Methodological context and theoretic framework.md"')
        sys.exit(1)
    
    input_filename = sys.argv[1]
    input_file = DRAFTS_DIR / input_filename
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    add_parentheses_to_citations(input_file)

if __name__ == '__main__':
    main()

