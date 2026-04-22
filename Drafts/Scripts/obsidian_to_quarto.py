#!/usr/bin/env python3
"""
Convert Obsidian Draft to Quarto Format
========================================

Converts Obsidian-style links to Quarto citation syntax (@citekey)
and generates a .qmd file ready for Quarto rendering.

Usage:
    python3 obsidian_to_quarto.py "Draft File.md" [--bibliography bibliography.bib]

Output:
    Creates [Draft File].qmd in same directory
"""

import re
import sys
import argparse
from pathlib import Path
from typing import Dict, Optional

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"
DRAFTS_DIR = BASE_PATH / "Drafts"

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
    """Generate BibTeX citation key from metadata (same as clippings_to_bibtex.py)."""
    authors = metadata.get('authors', metadata.get('author', []))
    year = metadata.get('year', metadata.get('published', ''))
    
    if isinstance(authors, list) and authors:
        first_author = authors[0]
    elif isinstance(authors, str):
        first_author = authors
    else:
        first_author = "unknown"
    
    if ',' in first_author:
        last_name = first_author.split(',')[0].strip()
    else:
        parts = first_author.split()
        last_name = parts[-1] if parts else "unknown"
    
    last_name = re.sub(r'[^a-zA-Z]', '', last_name.lower())
    
    year_match = re.search(r'\d{4}', str(year))
    year_str = year_match.group(0) if year_match else "2025"
    
    return f"{last_name}{year_str}"

def find_clipping_by_link(link_text: str) -> Optional[Dict]:
    """Find Clipping file by link text (filename, title, or display text)."""
    # Try exact filename match
    possible_names = [
        link_text,
        link_text.replace(' ', '_'),
        link_text.replace('_', ' '),
    ]
    
    for name in possible_names:
        # Try with .md extension
        md_file = CLIPPINGS_DIR / f"{name}.md"
        if md_file.exists():
            content = md_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(content)
            if metadata:
                return metadata
        
        # Try without extension
        md_file = CLIPPINGS_DIR / f"{name}"
        if md_file.exists() and md_file.suffix == '.md':
            content = md_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(content)
            if metadata:
                return metadata
    
    # Try title matching
    for md_file in CLIPPINGS_DIR.glob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(content)
            title = metadata.get('title', '').lower()
            if title and link_text.lower() in title:
                return metadata
        except:
            continue
    
    return None

def convert_obsidian_link_to_quarto(match: re.Match) -> str:
    """Convert a single Obsidian link to Quarto citation."""
    full_match = match.group(0)
    link_path = match.group(1) or match.group(2) or ""
    display_text = match.group(3) or ""
    
    # Extract page number if present
    page_match = re.search(r'#page=(\d+)', link_path)
    page_num = page_match.group(1) if page_match else None
    
    # Clean link path
    link_path = re.sub(r'#page=\d+', '', link_path)
    link_path = link_path.replace('Clippings/', '').replace('.md', '').replace('.pdf', '')
    
    # Try to find citation key
    citekey = None
    
    # If display text looks like a citation (Author, Year), try to extract
    citation_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*(?:et\s+al\.?|&\s*[A-Z])?[,\s]+(\d{4})', display_text)
    if citation_match:
        # Try to find by author/year
        author_part = citation_match.group(1)
        year_part = citation_match.group(2)
        
        for md_file in CLIPPINGS_DIR.glob("*.md"):
            try:
                content = md_file.read_text(encoding='utf-8')
                metadata = parse_yaml_frontmatter(content)
                authors = metadata.get('authors', metadata.get('author', []))
                year = str(metadata.get('year', metadata.get('published', '')))
                
                if year_part in year:
                    if isinstance(authors, list):
                        first_author = authors[0] if authors else ""
                    else:
                        first_author = str(authors)
                    
                    if author_part.lower() in first_author.lower():
                        citekey = generate_bibtex_key(metadata)
                        break
            except:
                continue
    
    # Fallback: find by link path
    if not citekey:
        metadata = find_clipping_by_link(link_path)
        if metadata:
            citekey = generate_bibtex_key(metadata)
    
    # If still no citekey, use placeholder
    if not citekey:
        citekey = "TODO"
    
    # Build Quarto citation
    citation = f"@{citekey}"
    if page_num:
        citation += f" [p. {page_num}]"
    
    return citation

def convert_draft_to_quarto(md_file: Path, bibliography: Optional[Path] = None) -> str:
    """Convert Obsidian markdown to Quarto format."""
    content = md_file.read_text(encoding='utf-8')
    
    # Parse existing YAML frontmatter if present
    yaml_match = re.match(r'^(---\s*\n.*?\n---\s*\n)', content, re.DOTALL)
    yaml_header = yaml_match.group(1) if yaml_match else ""
    body = content[yaml_match.end() if yaml_match else 0:]
    
    # Add bibliography to YAML if specified
    if bibliography and bibliography.exists():
        if 'bibliography:' not in yaml_header:
            # Add bibliography line
            if yaml_header:
                yaml_header = yaml_header.rstrip() + f"\nbibliography: {bibliography.name}\n"
            else:
                yaml_header = f"---\nbibliography: {bibliography.name}\n---\n"
    
    # Convert Obsidian links to Quarto citations
    # Pattern: [[path|display]] or [[path]]
    link_pattern = r'\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]'
    
    def replace_link(match):
        return convert_obsidian_link_to_quarto(match)
    
    body = re.sub(link_pattern, replace_link, body)
    
    return yaml_header + body

def main():
    parser = argparse.ArgumentParser(description='Convert Obsidian draft to Quarto format')
    parser.add_argument('draft_file', help='Path to draft .md file')
    parser.add_argument('--bibliography', '-b', help='Path to bibliography.bib file', 
                       default='bibliography.bib')
    
    args = parser.parse_args()
    
    # Resolve file paths
    draft_path = Path(args.draft_file)
    if not draft_path.is_absolute():
        draft_path = DRAFTS_DIR / draft_path
    
    if not draft_path.exists():
        print(f"Error: File not found: {draft_path}")
        sys.exit(1)
    
    # Resolve bibliography path
    bib_path = None
    if args.bibliography:
        bib_path = Path(args.bibliography)
        if not bib_path.is_absolute():
            bib_path = BASE_PATH / bib_path
    
    # Convert
    quarto_content = convert_draft_to_quarto(draft_path, bib_path)
    
    # Write .qmd file
    qmd_path = draft_path.with_suffix('.qmd')
    qmd_path.write_text(quarto_content, encoding='utf-8')
    
    print(f"✓ Converted {draft_path.name} to {qmd_path.name}")
    print(f"  Output: {qmd_path}")
    print(f"\n  Next step: quarto render \"{qmd_path.name}\"")

if __name__ == "__main__":
    main()
