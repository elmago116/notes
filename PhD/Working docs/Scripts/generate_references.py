#!/usr/bin/env python3
"""
Generate References Section from Citations
==========================================
Extracts citations from markdown file and generates APA 7th References section.
"""

import re
from pathlib import Path
from collections import OrderedDict

BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"

def parse_yaml_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter."""
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
            value = value.strip().strip('"\'')
            if value == '' and i + 1 < len(lines):
                items = []
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('- '):
                    items.append(lines[j].strip()[2:].strip().strip('"\'[]'))
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

def find_clipping_file(link_text: str) -> Path:
    """Find Clippings file for a link."""
    clean_link = link_text.split('#')[0].split('|')[0].strip()
    if clean_link.startswith('Clippings/'):
        clean_link = clean_link[10:]
    
    possible_names = [
        clean_link,
        clean_link + '.md',
        clean_link.replace('.pdf', '') + '.md',
    ]
    
    for name in possible_names:
        file_path = CLIPPINGS_DIR / name
        if file_path.exists():
            return file_path
    
    return None

def format_authors_for_reference(authors) -> str:
    """Format authors for reference entry."""
    if not authors:
        return ''
    
    if isinstance(authors, str):
        if 'et al' in authors.lower():
            return authors.split(',')[0].strip()
        parts = [a.strip() for a in re.split(r'[&,]| and ', authors) if a.strip()]
        authors = parts
    
    if isinstance(authors, list):
        clean_authors = [a.strip().strip('"\'[]') for a in authors if a.strip() and 'et al' not in a.lower()]
        if not clean_authors:
            return ''
        if len(clean_authors) == 1:
            return clean_authors[0]
        elif len(clean_authors) == 2:
            return f'{clean_authors[0]} & {clean_authors[1]}'
        else:
            return f'{clean_authors[0]} et al.'
    
    return str(authors)

def build_apa_reference(meta: dict) -> str:
    """Build full APA reference entry."""
    authors = meta.get('authors', [])
    year = meta.get('year', 'n.d.')
    title = meta.get('title', '')
    journal = meta.get('journal', '') or meta.get('published in', '')
    publisher = meta.get('publisher', '')
    volume = meta.get('volume', '')
    issue = meta.get('issue', '')
    pages = meta.get('pages', '')
    doi = meta.get('doi', '')
    url = meta.get('url', '')
    
    if not title:
        return None
    
    author_str = format_authors_for_reference(authors)
    if not author_str:
        return None
    
    # Format title
    if isinstance(title, list):
        title = title[0] if title else ''
    title = title.strip()
    
    # Build reference
    ref = f"{author_str} ({year}). {title}."
    
    if journal:
        ref += f" *{journal}*"
        if volume:
            ref += f", {volume}"
            if issue:
                ref += f"({issue})"
        if pages:
            ref += f", {pages}"
        ref += "."
    elif publisher:
        ref += f" {publisher}."
    
    if doi:
        if not doi.startswith('http'):
            doi = f"https://doi.org/{doi}"
        ref += f" {doi}"
    elif url:
        ref += f" {url}"
    
    return ref

def extract_citations_from_file(file_path: Path) -> list:
    """Extract all unique citations from markdown file."""
    content = file_path.read_text(encoding='utf-8')
    
    # Find all links with citations
    pattern = r'\[\[([^\]]+)\|\(([^)]+)\)\]\]'
    matches = re.findall(pattern, content)
    
    citations = []
    for link_body, citation in matches:
        citations.append((link_body, citation))
    
    return citations

def main():
    input_file = BASE_PATH / "PhD" / "Working docs" / "Maqueta Digital Libraries.md"
    
    citations = extract_citations_from_file(input_file)
    
    # Get unique citations with their link info
    unique_refs = OrderedDict()
    
    for link_body, citation in citations:
        if citation in unique_refs:
            continue
        
        # Find Clippings file
        clipping_file = find_clipping_file(link_body)
        if not clipping_file:
            continue
        
        try:
            content = clipping_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(content)
            ref_entry = build_apa_reference(metadata)
            
            if ref_entry:
                # Use citation as key to avoid duplicates
                unique_refs[citation] = ref_entry
        except Exception as e:
            print(f"Error processing {clipping_file.name}: {e}")
            continue
    
    # Sort references alphabetically by first author
    sorted_refs = sorted(unique_refs.values(), key=lambda x: x.split('(')[0].strip())
    
    # Generate References section
    refs_section = "\n## References\n\n"
    for i, ref in enumerate(sorted_refs, 1):
        refs_section += f"{ref}\n\n"
    
    # Append to file
    content = input_file.read_text(encoding='utf-8')
    
    # Remove existing References section
    content = re.sub(r'\n## References\s*\n[\s\S]*$', '', content, flags=re.IGNORECASE)
    
    # Add new References section
    content += refs_section
    
    input_file.write_text(content, encoding='utf-8')
    print(f"✅ Added {len(sorted_refs)} references to {input_file.name}")

if __name__ == "__main__":
    main()






