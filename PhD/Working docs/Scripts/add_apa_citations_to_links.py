#!/usr/bin/env python3
"""
Add APA Citations to Obsidian Links
====================================

Adds APA 7th edition citations as display text to Obsidian links in a markdown file,
while preserving the original links. Reports any metadata issues.

Usage:
    python3 add_apa_citations_to_links.py "Maqueta Digital Libraries.md"
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"
WORKING_DOCS_DIR = BASE_PATH / "PhD" / "Working docs"

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

def normalize(text: str) -> str:
    """Normalize text for matching."""
    text = text.replace('.pdf', '').replace('.md', '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

def find_clipping_file(link_text: str, clippings_dir: Path) -> Optional[Path]:
    """Find corresponding Clippings file for a link."""
    # Remove fragments and query params
    clean_link = link_text.split('#')[0].split('?')[0].strip()
    
    # Remove Clippings/ prefix if present
    if clean_link.startswith('Clippings/'):
        clean_link = clean_link[10:]
    
    # Try exact match first
    possible_names = [
        clean_link,
        clean_link + '.md',
        clean_link.replace('.pdf', '') + '.md',
        clean_link.replace('.pdf', ''),
    ]
    
    for name in possible_names:
        file_path = clippings_dir / name
        if file_path.exists():
            return file_path
    
    # Try normalized matching
    clean_normalized = normalize(clean_link)
    for file_path in clippings_dir.glob('*.md'):
        if normalize(file_path.stem) == clean_normalized:
            return file_path
    
    return None

def format_apa_citation(metadata: Dict) -> Optional[str]:
    """Format APA 7th edition in-text citation from metadata."""
    authors = metadata.get('authors', [])
    year = metadata.get('year', '')
    apa_citation = metadata.get('apa_citation', '')
    
    # If apa_citation exists, use it
    if apa_citation:
        return apa_citation
    
    # Otherwise, build from authors and year
    if not authors or not year:
        return None
    
    # Handle different author formats
    if isinstance(authors, str):
        # Parse string format
        if 'et al.' in authors.lower():
            # Extract first author
            first_author = authors.split(',')[0].strip()
            return f"{first_author} et al., {year}"
        elif '&' in authors or ' and ' in authors.lower():
            # Two authors
            parts = re.split(r'[&,]| and ', authors)
            authors_list = [a.strip() for a in parts if a.strip()]
            if len(authors_list) >= 2:
                return f"{authors_list[0]} & {authors_list[1]}, {year}"
            else:
                return f"{authors_list[0]}, {year}"
        else:
            # Single author or comma-separated
            parts = [a.strip() for a in authors.split(',') if a.strip()]
            if len(parts) == 1:
                return f"{parts[0]}, {year}"
            elif len(parts) == 2:
                return f"{parts[0]} & {parts[1]}, {year}"
            else:
                return f"{parts[0]} et al., {year}"
    
    elif isinstance(authors, list):
        if len(authors) == 0:
            return None
        elif len(authors) == 1:
            return f"{authors[0]}, {year}"
        elif len(authors) == 2:
            return f"{authors[0]} & {authors[1]}, {year}"
        else:
            return f"{authors[0]} et al., {year}"
    
    return None

def check_metadata_issues(metadata: Dict, file_path: Path) -> List[str]:
    """Check for metadata issues that prevent proper APA citation."""
    issues = []
    
    authors = metadata.get('authors', [])
    year = metadata.get('year', '')
    apa_citation = metadata.get('apa_citation', '')
    
    if not apa_citation:
        if not authors:
            issues.append(f"Missing 'authors' field")
        elif isinstance(authors, str):
            # Check for malformed author strings
            if '[' in authors or ']' in authors:
                issues.append(f"Malformed 'authors' field (contains brackets): {authors}")
            if '", "' in authors or '",' in authors:
                issues.append(f"Malformed 'authors' field (contains quotes/commas): {authors}")
        if not year:
            issues.append(f"Missing 'year' field")
    
    return issues

def process_file(input_file: Path) -> Tuple[str, List[str]]:
    """Process markdown file and add APA citations to links."""
    content = input_file.read_text(encoding='utf-8')
    issues = []
    
    # Pattern to match Obsidian links: [[link|display]] or [[link]]
    link_pattern = r'\[\[([^\]]+)\]\]'
    
    def replace_link(match):
        link_body = match.group(1)
        
        # Skip if already has display text with citation-like format
        if '|' in link_body:
            parts = link_body.split('|')
            display = parts[-1].strip()
            # Check if display looks like a citation (contains year in parentheses)
            if re.search(r'\([0-9]{4}\)', display):
                return match.group(0)  # Already has citation, skip
        
        # Extract the actual link target
        link_target = link_body.split('|')[0].strip()
        
        # Skip special links
        if link_target.startswith('#') or link_target.startswith('http'):
            return match.group(0)
        
        # Find corresponding Clippings file
        clipping_file = find_clipping_file(link_target, CLIPPINGS_DIR)
        
        if not clipping_file:
            issues.append(f"Link '{link_target}' - No corresponding Clippings file found")
            return match.group(0)
        
        # Read and parse metadata
        try:
            clipping_content = clipping_file.read_text(encoding='utf-8')
            metadata = parse_yaml_frontmatter(clipping_content)
            
            # Check for issues
            file_issues = check_metadata_issues(metadata, clipping_file)
            if file_issues:
                issues.append(f"Link '{link_target}' ({clipping_file.name}): " + "; ".join(file_issues))
            
            # Generate citation
            citation = format_apa_citation(metadata)
            
            if citation:
                # Add citation as display text
                return f"[[{link_target}|{citation}]]"
            else:
                issues.append(f"Link '{link_target}' ({clipping_file.name}): Cannot generate citation (missing authors or year)")
                return match.group(0)
        
        except Exception as e:
            issues.append(f"Link '{link_target}' ({clipping_file.name}): Error reading file - {str(e)}")
            return match.group(0)
    
    # Replace all links
    new_content = re.sub(link_pattern, replace_link, content)
    
    return new_content, issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 add_apa_citations_to_links.py <filename.md>")
        sys.exit(1)
    
    filename = sys.argv[1]
    input_file = WORKING_DOCS_DIR / filename
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    print(f"Processing: {input_file}")
    new_content, issues = process_file(input_file)
    
    # Write output
    output_file = input_file.parent / f"{input_file.stem}_with_citations.md"
    output_file.write_text(new_content, encoding='utf-8')
    
    print(f"\nOutput written to: {output_file}")
    
    # Report issues
    if issues:
        print(f"\n⚠️  Found {len(issues)} metadata issue(s):\n")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ No metadata issues found!")
    
    print(f"\n✅ Processing complete!")

if __name__ == "__main__":
    main()

