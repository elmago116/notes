#!/usr/bin/env python3
"""
Add apa_citation Fields to Clippings Files
==========================================

Generates and adds apa_citation field to Clippings files based on their
authors and year metadata. Only adds if field doesn't already exist.

Usage:
    python3 add_apa_citation_fields.py [--dry-run] [--file "specific_file.md"]

Author: AI Assistant
Date: 2025-01-XX
"""

import re
import sys
from pathlib import Path
from typing import Dict, Optional

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"

# --- YAML Parsing ---

def parse_yaml_frontmatter(content: str) -> Dict:
    """Parse YAML frontmatter from markdown content (list-aware)."""
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not yaml_match:
        return {}
    yaml_content = yaml_match.group(1)
    metadata: Dict = {}
    lines = yaml_content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()
            if value == '' and i + 1 < len(lines):
                items = []
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('- '):
                    items.append(lines[j].strip()[2:].strip())
                    j += 1
                if items:
                    metadata[key] = items
                    i = j - 1
                else:
                    metadata[key] = value
            else:
                metadata[key] = value
        i += 1
    return metadata

def format_authors_for_citation(authors) -> Optional[str]:
    """Format authors for in-text citation."""
    if not authors:
        return None
    
    # Handle string representation
    if isinstance(authors, str):
        # Check if already formatted with "et al."
        if 'et al' in authors.lower() or '&' in authors:
            clean = authors.strip().strip('"\'')
            clean = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean)
            return clean if clean else None
        
        if authors.startswith('[') and authors.endswith(']'):
            content = authors[1:-1]
            author_list = [auth.strip().strip('"\'') for auth in content.split(',')]
            authors = author_list
        else:
            authors = [authors]
    
    if isinstance(authors, list):
        clean_authors = []
        for author in authors:
            if isinstance(author, str):
                clean_author = author.strip().strip('"\'')
                # Remove trailing commas
                clean_author = clean_author.rstrip(',')
                # Remove Obsidian link syntax
                clean_author = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean_author)
                # Remove numeric suffixes like "1,2" or "Bonhoure1,2"
                clean_author = re.sub(r'\d+[,;]\d+', '', clean_author)
                clean_author = re.sub(r'\d+$', '', clean_author)
                if clean_author and 'et al' not in clean_author.lower():
                    clean_authors.append(clean_author)
        
        if len(clean_authors) == 0:
            return None
        elif len(clean_authors) == 1:
            return clean_authors[0]
        elif len(clean_authors) == 2:
            # APA format: Author1 & Author2 (no comma before &)
            return f"{clean_authors[0]} & {clean_authors[1]}"
        else:
            return f"{clean_authors[0]} et al."
    
    return str(authors)

def build_apa_citation_label(metadata: Dict) -> Optional[str]:
    """Build APA citation label (Author, Year) from metadata."""
    authors = metadata.get('authors', metadata.get('author', []))
    year = metadata.get('year', metadata.get('Year', ''))
    
    # Clean year
    if isinstance(year, str):
        year = year.strip().strip('"\'')
    
    author_str = format_authors_for_citation(authors)
    if not author_str:
        return None
    
    if year:
        return f"{author_str}, {year}"
    return None

def add_apa_citation_field(file_path: Path, dry_run: bool = False) -> bool:
    """Add apa_citation field to a Clippings file if missing."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ⚠️  Error reading {file_path.name}: {e}")
        return False
    
    # Check if apa_citation already exists
    if 'apa_citation:' in content.lower():
        return False
    
    # Parse metadata
    meta = parse_yaml_frontmatter(content)
    
    # Build citation label
    citation_label = build_apa_citation_label(meta)
    
    if not citation_label:
        return False
    
    # Find YAML frontmatter end
    yaml_match = re.match(r'^(---\s*\n.*?\n---\s*\n)', content, re.DOTALL)
    if not yaml_match:
        return False
    
    yaml_block = yaml_match.group(1)
    rest_of_content = content[len(yaml_block):]
    
    # Add apa_citation field before closing ---
    yaml_lines = yaml_block.split('\n')
    # Find the last --- line
    last_dash_idx = -1
    for i in range(len(yaml_lines) - 1, -1, -1):
        if yaml_lines[i].strip() == '---':
            last_dash_idx = i
            break
    
    if last_dash_idx == -1:
        return False
    
    # Insert apa_citation before the closing ---
    citation_line = f"apa_citation: {citation_label}"
    yaml_lines.insert(last_dash_idx, citation_line)
    
    new_yaml_block = '\n'.join(yaml_lines)
    new_content = new_yaml_block + rest_of_content
    
    if not dry_run:
        file_path.write_text(new_content, encoding='utf-8')
    
    return True

def main():
    dry_run = '--dry-run' in sys.argv
    specific_file = None
    
    if '--file' in sys.argv:
        idx = sys.argv.index('--file')
        if idx + 1 < len(sys.argv):
            specific_file = sys.argv[idx + 1]
    
    if specific_file:
        file_path = CLIPPINGS_DIR / specific_file
        if file_path.exists():
            if add_apa_citation_field(file_path, dry_run):
                print(f"{'[DRY RUN] Would add' if dry_run else 'Added'} apa_citation to: {file_path.name}")
            else:
                print(f"No changes needed for: {file_path.name}")
        else:
            print(f"File not found: {file_path}")
    else:
        # Process all Clippings files
        md_files = list(CLIPPINGS_DIR.rglob('*.md'))
        added = 0
        skipped = 0
        
        print(f"Processing {len(md_files)} Clippings files...")
        
        for md_file in md_files:
            if add_apa_citation_field(md_file, dry_run):
                added += 1
                if not dry_run:
                    print(f"  ✓ Added to: {md_file.name}")
            else:
                skipped += 1
        
        print(f"\n{'='*60}")
        print(f"Summary:")
        print(f"{'='*60}")
        print(f"{'Would add' if dry_run else 'Added'}: {added} files")
        print(f"Skipped: {skipped} files (already have apa_citation or missing authors/year)")

if __name__ == '__main__':
    main()

