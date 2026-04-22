#!/usr/bin/env python3
"""
Convert Clippings YAML to BibTeX
=================================

Converts all Clippings .md files with YAML frontmatter to BibTeX format
for use with Quarto's native citation system.

Usage:
    python3 clippings_to_bibtex.py

Output:
    Creates bibliography.bib in project root
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"
OUTPUT_BIB = BASE_PATH / "bibliography.bib"

def parse_yaml_frontmatter(content: str) -> Dict:
    """Parse YAML frontmatter from markdown content."""
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not yaml_match:
        return {}
    
    yaml_content = yaml_match.group(1)
    metadata = {}
    lines = yaml_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()
            
            # Handle list values
            if value == '' and i + 1 < len(lines):
                items = []
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('- '):
                    items.append(lines[j].strip()[2:].strip())
                    j += 1
                if items:
                    metadata[key] = items
                    i = j
                    continue
            
            metadata[key] = value
        i += 1
    
    return metadata

def generate_bibtex_key(metadata: Dict) -> str:
    """Generate BibTeX citation key from metadata."""
    authors = metadata.get('authors', metadata.get('author', []))
    year = metadata.get('year', metadata.get('published', ''))
    
    if isinstance(authors, list) and authors:
        first_author = authors[0]
    elif isinstance(authors, str):
        first_author = authors
    else:
        first_author = "unknown"
    
    # Extract last name (before first comma if present)
    if ',' in first_author:
        last_name = first_author.split(',')[0].strip()
    else:
        # Assume "First Last" format
        parts = first_author.split()
        last_name = parts[-1] if parts else "unknown"
    
    # Clean last name
    last_name = re.sub(r'[^a-zA-Z]', '', last_name.lower())
    
    # Extract year (first 4 digits)
    year_match = re.search(r'\d{4}', str(year))
    year_str = year_match.group(0) if year_match else datetime.now().year
    
    return f"{last_name}{year_str}"

def format_author_bibtex(authors: List[str] or str) -> str:
    """Format authors for BibTeX."""
    if isinstance(authors, str):
        authors = [authors]
    
    formatted = []
    for author in authors:
        # Remove Obsidian links if present
        author = re.sub(r'\[\[([^\]]+)\]\]', r'\1', author)
        
        # Handle "Last, First" or "First Last" format
        if ',' in author:
            formatted.append(author.strip())
        else:
            # Convert "First Last" to "Last, First"
            parts = author.strip().split()
            if len(parts) >= 2:
                last = parts[-1]
                first = ' '.join(parts[:-1])
                formatted.append(f"{last}, {first}")
            else:
                formatted.append(author.strip())
    
    return " and ".join(formatted)

def determine_entry_type(metadata: Dict) -> str:
    """Determine BibTeX entry type from metadata."""
    doc_type = metadata.get('type', '').lower()
    
    type_mapping = {
        'article': 'article',
        'journal': 'article',
        'book': 'book',
        'chapter': 'incollection',
        'conference': 'inproceedings',
        'proceedings': 'inproceedings',
        'thesis': 'phdthesis',
        'phdthesis': 'phdthesis',
        'mastersthesis': 'mastersthesis',
        'report': 'techreport',
        'website': 'misc',
        'web': 'misc',
    }
    
    return type_mapping.get(doc_type, 'misc')

def format_bibtex_entry(metadata: Dict, citekey: str) -> str:
    """Format a single BibTeX entry."""
    entry_type = determine_entry_type(metadata)
    
    lines = [f"@{entry_type}{{{citekey},"]
    
    # Title
    title = metadata.get('title', '')
    if title:
        # Remove markdown formatting
        title = re.sub(r'\*\*([^\*]+)\*\*', r'\1', title)  # Bold
        title = re.sub(r'\*([^\*]+)\*', r'\1', title)      # Italic
        if entry_type in ['article', 'inproceedings']:
            lines.append(f"  title = {{{title}}},")
        else:
            lines.append(f"  title = {{{title}}},")
    
    # Authors
    authors = metadata.get('authors', metadata.get('author', []))
    if authors:
        author_str = format_author_bibtex(authors)
        lines.append(f"  author = {{{author_str}}},")
    
    # Year
    year = metadata.get('year', metadata.get('published', ''))
    if year:
        year_match = re.search(r'\d{4}', str(year))
        if year_match:
            lines.append(f"  year = {{{year_match.group(0)}}},")
    
    # Journal (for articles)
    if entry_type == 'article':
        journal = metadata.get('journal', '')
        if journal:
            lines.append(f"  journal = {{{journal}}},")
    
    # Publisher (for books)
    if entry_type in ['book', 'incollection']:
        publisher = metadata.get('publisher', '')
        if publisher:
            lines.append(f"  publisher = {{{publisher}}},")
    
    # DOI
    doi = metadata.get('doi', '')
    if doi:
        lines.append(f"  doi = {{{doi}}},")
    
    # URL
    url = metadata.get('url', '')
    if url:
        lines.append(f"  url = {{{url}}},")
    
    # Volume and Issue (for articles)
    if entry_type == 'article':
        volume = metadata.get('volume', '')
        if volume:
            lines.append(f"  volume = {{{volume}}},")
        issue = metadata.get('issue', metadata.get('number', ''))
        if issue:
            lines.append(f"  number = {{{issue}}},")
        pages = metadata.get('pages', '')
        if pages:
            lines.append(f"  pages = {{{pages}}},")
    
    # Remove trailing comma from last line
    if lines[-1].endswith(','):
        lines[-1] = lines[-1][:-1]
    
    lines.append("}")
    
    return "\n".join(lines)

def convert_clippings_to_bibtex():
    """Convert all Clippings files to BibTeX."""
    if not CLIPPINGS_DIR.exists():
        print(f"Error: Clippings directory not found: {CLIPPINGS_DIR}")
        return
    
    entries = []
    processed = 0
    skipped = 0
    
    for md_file in sorted(CLIPPINGS_DIR.glob("*.md")):
        try:
            content = md_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(content)
            
            if not metadata:
                skipped += 1
                continue
            
            # Skip if no title or authors
            if not metadata.get('title') and not metadata.get('authors') and not metadata.get('author'):
                skipped += 1
                continue
            
            citekey = generate_bibtex_key(metadata)
            entry = format_bibtex_entry(metadata, citekey)
            entries.append(entry)
            processed += 1
            
        except Exception as e:
            print(f"Warning: Error processing {md_file.name}: {e}")
            skipped += 1
    
    # Write BibTeX file
    bib_content = "\n\n".join(entries)
    OUTPUT_BIB.write_text(bib_content, encoding='utf-8')
    
    print(f"✓ Converted {processed} entries to BibTeX")
    print(f"  Skipped {skipped} files (no metadata)")
    print(f"  Output: {OUTPUT_BIB}")

if __name__ == "__main__":
    convert_clippings_to_bibtex()
