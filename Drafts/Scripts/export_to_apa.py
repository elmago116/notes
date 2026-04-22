#!/usr/bin/env python3
"""
Export Draft File to APA Format
================================

Converts Obsidian links in a draft file to APA 7th edition citations
and generates a complete References section.

Usage:
    python3 export_to_apa.py "Draft File Name.md"

Author: AI Assistant
Date: 2025-01-XX
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import OrderedDict

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"
DRAFTS_DIR = BASE_PATH / "Drafts"

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

# --- Normalization & Matching ---

def normalize(text: str) -> str:
    """Normalize text for matching (lowercase, remove PDF extension, collapse spaces)."""
    text = text.replace('.pdf', '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

def basename_only(path_like: str) -> str:
    """Extract basename from path-like string."""
    cleaned = path_like.strip().strip('"\'')
    cleaned = cleaned.split('/')[-1]
    return cleaned

def extract_pdf_and_label(link_body: str) -> Tuple[str, str]:
    """Extract PDF filename and display label from link body."""
    label = ''
    if '|' in link_body:
        parts = link_body.split('|')
        filename_part = parts[0]
        label = parts[-1].strip()
    else:
        filename_part = link_body
    filename = filename_part.strip('[[]]')
    if '#' in filename:
        filename = filename.split('#')[0]
    return filename, label

def find_note_for_link(link_body: str, clippings_dir: Path) -> Optional[Path]:
    """Find corresponding Clippings note for a link."""
    is_pdf = '.pdf' in link_body.lower() or 'pdf/' in link_body.lower()
    
    if is_pdf:
        pdf_filename, display = extract_pdf_and_label(link_body)
        # Remove PDF/ prefix if present
        if pdf_filename.startswith('PDF/'):
            pdf_filename = pdf_filename[4:]
        return match_note(pdf_basename=basename_only(pdf_filename), display_label=display, clippings_dir=clippings_dir)
    else:
        # MD wikilink; check if it's a Clippings/ path
        display = link_body
        if display.startswith('Clippings/'):
            display = display[10:]  # Remove 'Clippings/' prefix
        return match_note(pdf_basename='', display_label=display, clippings_dir=clippings_dir)

def match_note(pdf_basename: str, display_label: str, clippings_dir: Path) -> Optional[Path]:
    """Match link to Clippings note using multi-stage strategy."""
    md_files = list(clippings_dir.rglob('*.md'))
    norm_pdf = normalize(pdf_basename) if pdf_basename else ''
    norm_label = normalize(display_label) if display_label else ''
    
    # Remove placeholder markers like "|X" from label
    norm_label = re.sub(r'\|\s*[xX]\s*$', '', norm_label).strip()

    # 1) Exact stem match
    for md in md_files:
        stem = md.stem.lower()
        if norm_pdf and stem == norm_pdf:
            return md
        if norm_label and stem == norm_label:
            return md

    # 2) Frontmatter 'pdf' basename
    for md in md_files:
        try:
            meta = parse_yaml_frontmatter(md.read_text(encoding='utf-8'))
            pdf_field = meta.get('pdf') or meta.get('file') or meta.get('attachment')
            if pdf_field and norm_pdf:
                if basename_only(str(pdf_field)).lower() == pdf_basename.lower():
                    return md
        except Exception:
            continue

    # 3) Frontmatter 'title' match to label
    for md in md_files:
        try:
            meta = parse_yaml_frontmatter(md.read_text(encoding='utf-8'))
            title = meta.get('title')
            if title and norm_label:
                title_normalized = normalize(str(title))
                # Also check filename stem in case title doesn't match exactly
                stem_normalized = normalize(md.stem)
                if (title_normalized == norm_label or 
                    title_normalized in norm_label or 
                    norm_label in title_normalized or
                    stem_normalized == norm_label or
                    stem_normalized in norm_label or
                    norm_label in stem_normalized):
                    return md
        except Exception:
            continue

    # 4) Word overlap fallback (strict, 60% threshold)
    candidates = []
    for md in md_files:
        stem_words = set(normalize(md.stem).split())
        label_words = set(norm_label.split()) if norm_label else set()
        pdf_words = set(norm_pdf.split()) if norm_pdf else set()
        target = label_words or pdf_words
        if not target or not stem_words:
            continue
        score = len(target.intersection(stem_words)) / max(len(target), len(stem_words))
        candidates.append((score, md))
    candidates.sort(key=lambda x: x[0], reverse=True)
    if candidates and candidates[0][0] >= 0.6:
        return candidates[0][1]
    return None

# --- Page Info Extraction ---

def extract_page_info_from_link(link_body: str) -> str:
    """Extract page number from link fragment."""
    m = re.search(r'page=(\d+)', link_body)
    if m:
        return f"p. {m.group(1)}"
    # Try label page hints like 'p. 55' inside the display text
    if '|' in link_body:
        display = link_body.split('|')[-1]
        m2 = re.search(r'p\.\s*(\d+)', display)
        if m2:
            return f"p. {m2.group(1)}"
    return ''

# --- APA Citation Building ---

def format_authors_for_citation(authors) -> Optional[str]:
    """Format authors for in-text citation."""
    if not authors:
        return None
    
    # Handle string representation
    if isinstance(authors, str):
        # Check if already formatted with "et al."
        if 'et al' in authors.lower() or '&' in authors:
            # Already formatted, return as-is after cleaning
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
                # Remove Obsidian link syntax
                clean_author = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean_author)
                if clean_author and 'et al' not in clean_author.lower():
                    clean_authors.append(clean_author)
        
        if len(clean_authors) == 0:
            return None
        elif len(clean_authors) == 1:
            return clean_authors[0]
        elif len(clean_authors) == 2:
            return f"{clean_authors[0]} & {clean_authors[1]}"
        else:
            return f"{clean_authors[0]} et al."
    
    return str(authors)

def build_apa_citation(metadata: Dict, page_info: str = '') -> Optional[str]:
    """Build APA in-text citation from metadata."""
    authors = metadata.get('authors', metadata.get('author', []))
    year = metadata.get('year', metadata.get('Year', 'n.d.'))
    
    # Clean year
    if isinstance(year, str):
        year = year.strip().strip('"\'')
    
    author_str = format_authors_for_citation(authors)
    if not author_str:
        return None
    
    if page_info:
        return f"({author_str}, {year}, {page_info})"
    return f"({author_str}, {year})"

# --- References Section Building ---

def format_authors_for_reference(authors) -> str:
    """Format authors for reference entry (full format)."""
    if not authors:
        return ''
    
    # Handle string representation
    if isinstance(authors, str):
        if authors.startswith('[') and authors.endswith(']'):
            content = authors[1:-1]
            author_list = [auth.strip().strip('"\'') for auth in content.split(',')]
            authors = author_list
        else:
            return authors
    
    if isinstance(authors, list):
        clean_authors = []
        for author in authors:
            if isinstance(author, str):
                clean_author = author.strip().strip('"\'')
                # Remove Obsidian link syntax
                clean_author = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean_author)
                if clean_author:
                    clean_authors.append(clean_author)
        
        if len(clean_authors) == 0:
            return ''
        elif len(clean_authors) == 1:
            return clean_authors[0]
        elif len(clean_authors) == 2:
            return f'{clean_authors[0]} & {clean_authors[1]}'
        else:
            # Format: Last, F., Last, F., & Last, F.
            formatted = ', '.join(clean_authors[:-1])
            return f'{formatted}, & {clean_authors[-1]}'
    
    return str(authors)

def build_apa_reference(meta: Dict) -> Optional[str]:
    """Build full APA reference entry from metadata."""
    authors = meta.get('authors') or meta.get('author', [])
    year = meta.get('year') or meta.get('Year', 'n.d.')
    title = meta.get('title', '')
    journal = meta.get('journal', '') or meta.get('Published in', '')
    publisher = meta.get('publisher', '')
    volume = meta.get('volume', '')
    issue = meta.get('issue', '')
    pages = meta.get('pages', '')
    doi = meta.get('doi', '') or meta.get('DOI', '')
    url = meta.get('url', '') or meta.get('Links', '')
    doc_type = meta.get('type', '').lower()
    
    if not title:
        return None
    
    # Ensure year is a string
    year_str = str(year).strip().strip('"\'') if year else 'n.d.'
    
    author_str = format_authors_for_reference(authors)
    if not author_str:
        return None
    
    # Format title (sentence case, italicize for books)
    title_clean = str(title).strip()
    
    ref = f"{author_str} ({year_str}). "
    
    # Format based on document type
    if 'journal' in doc_type or journal:
        # Journal article
        ref += f"{title_clean}. "
        if journal:
            ref += f"*{journal.strip()}*"
            if volume:
                ref += f", {volume.strip()}"
                if issue:
                    ref += f"({issue.strip()})"
            if pages:
                ref += f", {pages.strip()}"
        ref += "."
    elif 'book' in doc_type or publisher and not journal:
        # Book
        ref += f"*{title_clean}*. {publisher.strip()}."
    elif 'conference' in doc_type or 'proceedings' in doc_type:
        # Conference paper
        ref += f"{title_clean}. "
        if journal or publisher:
            venue = journal or publisher
            ref += f"In *{venue.strip()}*"
            if pages:
                ref += f" (pp. {pages.strip()})"
        ref += "."
    else:
        # Default format
        ref += f"{title_clean}."
        if journal:
            ref += f" *{journal.strip()}*."
        elif publisher:
            ref += f" {publisher.strip()}."
    
    # Add DOI or URL
    if doi:
        doi_clean = str(doi).strip().strip('"\'')
        if 'doi.org' in doi_clean or doi_clean.startswith('http'):
            ref += f" {doi_clean}"
        else:
            ref += f" https://doi.org/{doi_clean}"
    elif url:
        url_clean = str(url).strip().strip('\'"')
        ref += f" {url_clean}"
    
    return ref

def sort_references(references: List[str]) -> List[str]:
    """Sort references alphabetically by first author."""
    def get_sort_key(ref: str) -> str:
        # Extract first author's last name (usually before comma)
        match = re.match(r'^([^,]+)', ref)
        if match:
            return match.group(1).strip().lower()
        return ref.lower()
    
    return sorted(references, key=get_sort_key)

# --- Main Export Function ---

def export_to_apa(input_file: Path, drafts_dir: Path, clippings_dir: Path) -> None:
    """Convert draft file to APA format with citations and references."""
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        return
    
    # Read original content
    original = input_file.read_text(encoding='utf-8')
    content = original
    
    # Find all Obsidian links
    link_pattern = r'\[\[([^\]]+)\]\]'
    all_links = re.findall(link_pattern, content)
    
    # Track conversions and references
    replacements = {}
    references_dict = OrderedDict()  # Use OrderedDict to preserve order and avoid duplicates
    converted = 0
    unresolved = 0
    unresolved_links = []
    
    print(f"Processing {len(all_links)} links...")
    
    for link_body in all_links:
        # Extract page info
        page_info = extract_page_info_from_link(link_body)
        
        # Find corresponding note
        note = find_note_for_link(link_body, clippings_dir)
        
        if note is None:
            unresolved += 1
            unresolved_links.append(link_body)
            continue
        
        try:
            # Parse metadata
            meta = parse_yaml_frontmatter(note.read_text(encoding='utf-8'))
            
            # Build citation
            citation = build_apa_citation(meta, page_info)
            if not citation:
                unresolved += 1
                unresolved_links.append(link_body)
                continue
            
            # Store replacement
            replacements[f"[[{link_body}]]"] = citation
            converted += 1
            
            # Build reference entry for References section
            ref_entry = build_apa_reference(meta)
            if ref_entry:
                # Use title as key to avoid duplicates
                ref_key = meta.get('title', '') or str(note.stem)
                if ref_key not in references_dict:
                    references_dict[ref_key] = ref_entry
            
        except Exception as e:
            unresolved += 1
            unresolved_links.append(link_body)
            print(f"  Warning: Error processing link '{link_body}': {e}")
            continue
    
    # Apply replacements
    for old_link, citation in replacements.items():
        content = content.replace(old_link, citation)
    
    # Build references section
    references_list = list(references_dict.values())
    references_list = sort_references(references_list)
    
    # Remove existing References section if present
    content = re.sub(r'\n## References\s*\n[\s\S]*$', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\n## Referencias\s*\n[\s\S]*$', '', content, flags=re.IGNORECASE)
    
    # Add References section
    if references_list:
        refs_text = "\n\n## References\n\n" + "\n\n".join(references_list) + "\n"
        content = content.rstrip() + refs_text
    
    # Create output filename
    output_file = input_file.parent / f"{input_file.stem} - APA Export{input_file.suffix}"
    
    # Write output
    output_file.write_text(content, encoding='utf-8')
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Export complete!")
    print(f"{'='*60}")
    print(f"Converted: {converted} links")
    print(f"Unresolved: {unresolved} links")
    print(f"References: {len(references_list)} entries")
    print(f"\nOutput file: {output_file.name}")
    
    if unresolved_links:
        print(f"\nUnresolved links (preserved as-is):")
        for link in unresolved_links[:10]:  # Show first 10
            print(f"  - [[{link}]]")
        if len(unresolved_links) > 10:
            print(f"  ... and {len(unresolved_links) - 10} more")

# --- Main ---

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 export_to_apa.py \"Draft File Name.md\"")
        print("\nExample:")
        print('  python3 export_to_apa.py "General Methodological context and theoretic framework.md"')
        sys.exit(1)
    
    input_filename = sys.argv[1]
    input_file = DRAFTS_DIR / input_filename
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        print(f"Looking in: {DRAFTS_DIR}")
        sys.exit(1)
    
    export_to_apa(input_file, DRAFTS_DIR, CLIPPINGS_DIR)

if __name__ == '__main__':
    main()

