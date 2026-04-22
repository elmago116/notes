#!/usr/bin/env python3
"""
Replace |X Placeholders with APA Citation Labels
=================================================

Reads apa_citation field from Clippings YAML and replaces |X placeholders
in Draft links with the citation label (e.g., "Author, Year").

Usage:
    python3 replace_placeholders_with_citations.py "Draft File Name.md"

Author: AI Assistant
Date: 2025-01-XX
"""

import re
import sys
from pathlib import Path
from typing import Dict, Optional, Tuple

# Configuration
BASE_PATH = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_PATH / "Clippings"
DRAFTS_DIR = BASE_PATH / "Drafts"

# --- YAML Parsing (reuse from export script) ---

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

# --- Normalization & Matching (reuse from export script) ---

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
        if pdf_filename.startswith('PDF/'):
            pdf_filename = pdf_filename[4:]
        return match_note(pdf_basename=basename_only(pdf_filename), display_label=display, clippings_dir=clippings_dir)
    else:
        display = link_body
        if display.startswith('Clippings/'):
            display = display[10:]
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

# --- Extract Citation Label from apa_citation ---

def extract_citation_label(apa_citation: str) -> str:
    """Extract short label from full APA citation (Author, Year) format."""
    if not apa_citation:
        return ""
    
    # Remove parentheses if present: "(Author, Year)" -> "Author, Year"
    citation = apa_citation.strip()
    if citation.startswith('(') and citation.endswith(')'):
        citation = citation[1:-1].strip()
    
    # Remove page info if present: "Author, Year, p. 45" -> "Author, Year"
    citation = re.sub(r',\s*p\.\s*\d+.*$', '', citation, flags=re.IGNORECASE)
    
    return citation.strip()

# --- Main Replacement Function ---

def replace_placeholders(input_file: Path, drafts_dir: Path, clippings_dir: Path) -> None:
    """Replace |X placeholders with citation labels from apa_citation field."""
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        return
    
    # Read original content
    original = input_file.read_text(encoding='utf-8')
    content = original
    
    # Find all Obsidian links with |X or |XY placeholder (including escaped pipes in tables)
    link_pattern = r'\[\[([^\]]+)(?:\\|)\|([xX\sY]+)\]\]'
    matches = list(re.finditer(link_pattern, content))
    
    replacements = {}
    replaced = 0
    not_found = 0
    no_citation = 0
    
    print(f"Processing {len(matches)} links with |X placeholders...")
    
    for match in matches:
        full_match = match.group(0)
        link_body = match.group(1)
        placeholder = match.group(2)
        
        # Clean link body (remove sync-conflict suffixes, handle escaped pipes)
        clean_link_body = link_body.replace(' 1.sync-conflict-20250925-181434-GF7SSHV', '')
        clean_link_body = clean_link_body.replace('\\', '')
        
        # Find corresponding note
        note = find_note_for_link(clean_link_body, clippings_dir)
        
        if note is None:
            not_found += 1
            print(f"  ⚠️  Could not resolve: {link_body}")
            continue
        
        try:
            # Parse metadata
            meta = parse_yaml_frontmatter(note.read_text(encoding='utf-8'))
            
            # Check for apa_citation field
            apa_citation = meta.get('apa_citation', '')
            
            if not apa_citation:
                # Try to generate from authors/year if available
                authors = meta.get('authors', meta.get('author', []))
                year = meta.get('year', meta.get('Year', ''))
                
                # If no year, try to extract from published field
                if not year:
                    published = meta.get('published', '')
                    if published:
                        # Extract year from dates like "2020-04-01" or "2020"
                        year_match = re.search(r'(\d{4})', str(published))
                        if year_match:
                            year = year_match.group(1)
                
                if authors and year:
                    # Format authors for citation
                    if isinstance(authors, str):
                        # Remove Obsidian link syntax: [[Author]] -> Author
                        author_str = re.sub(r'\[\[([^\]]+)\]\]', r'\1', authors)
                        if 'et al' in author_str.lower() or '&' in author_str:
                            author_str = author_str.strip().strip('"\'')
                        else:
                            author_str = author_str.strip().strip('"\'')
                    elif isinstance(authors, list) and len(authors) > 0:
                        clean_authors = []
                        for a in authors:
                            if isinstance(a, str):
                                # Remove Obsidian link syntax
                                clean_a = re.sub(r'\[\[([^\]]+)\]\]', r'\1', a)
                                clean_a = clean_a.strip().strip('"\'')
                                # Remove trailing commas
                                clean_a = clean_a.rstrip(',')
                                # Skip if it's just a single word (likely a broken Obsidian link)
                                if clean_a and 'et al' not in clean_a.lower() and len(clean_a.split()) > 0:
                                    clean_authors.append(clean_a)
                        
                        if len(clean_authors) == 0:
                            no_citation += 1
                            continue
                        elif len(clean_authors) == 1:
                            author_str = clean_authors[0]
                        elif len(clean_authors) == 2:
                            # APA format: Author1 & Author2 (no comma before &)
                            author_str = f"{clean_authors[0]} & {clean_authors[1]}"
                        else:
                            author_str = f"{clean_authors[0]} et al."
                    else:
                        no_citation += 1
                        continue
                    
                    year_str = str(year).strip().strip('"\'')
                    citation_label = f"{author_str}, {year_str}"
                else:
                    no_citation += 1
                    print(f"  ⚠️  No apa_citation and missing authors/year: {note.name}")
                    continue
            else:
                # Extract label from apa_citation
                citation_label = extract_citation_label(str(apa_citation))
                if not citation_label:
                    no_citation += 1
                    continue
                
                # Fix two-author citations: ensure both authors appear (APA format)
                # Check if this is a two-author citation that incorrectly uses "et al."
                meta = parse_yaml_frontmatter(note.read_text(encoding='utf-8'))
                authors = meta.get('authors', meta.get('author', []))
                if isinstance(authors, list) and len(authors) == 2:
                    # Rebuild citation with both authors
                    clean_authors = []
                    for a in authors:
                        if isinstance(a, str):
                            clean_a = re.sub(r'\[\[([^\]]+)\]\]', r'\1', a)
                            clean_a = clean_a.strip().strip('"\'')
                            clean_a = clean_a.rstrip(',')
                            if clean_a:
                                clean_authors.append(clean_a)
                    if len(clean_authors) == 2:
                        year = meta.get('year', meta.get('Year', ''))
                        if not year:
                            published = meta.get('published', '')
                            if published:
                                year_match = re.search(r'(\d{4})', str(published))
                                if year_match:
                                    year = year_match.group(1)
                        if year:
                            citation_label = f"{clean_authors[0]} & {clean_authors[1]}, {year}"
            
            # Build new link: keep original link body, replace placeholder with citation label in parentheses
            citation_with_parens = f"({citation_label})"
            new_link = f"[[{link_body}|{citation_with_parens}]]"
            replacements[full_match] = new_link
            replaced += 1
            
        except Exception as e:
            not_found += 1
            print(f"  ⚠️  Error processing {note.name}: {e}")
            continue
    
    # Apply replacements
    for old_link, new_link in replacements.items():
        content = content.replace(old_link, new_link)
    
    # Write output (in-place update)
    if replaced > 0:
        input_file.write_text(content, encoding='utf-8')
        print(f"\n{'='*60}")
        print(f"Replacement complete!")
        print(f"{'='*60}")
        print(f"Replaced: {replaced} links")
        print(f"Not found: {not_found} links")
        print(f"No citation available: {no_citation} links")
        print(f"\nUpdated file: {input_file.name}")
    else:
        print(f"\nNo replacements made. Check that Clippings files have 'apa_citation' field or authors/year metadata.")

# --- Main ---

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 replace_placeholders_with_citations.py \"Draft File Name.md\"")
        print("\nExample:")
        print('  python3 replace_placeholders_with_citations.py "General Methodological context and theoretic framework.md"')
        sys.exit(1)
    
    input_filename = sys.argv[1]
    input_file = DRAFTS_DIR / input_filename
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        print(f"Looking in: {DRAFTS_DIR}")
        sys.exit(1)
    
    replace_placeholders(input_file, DRAFTS_DIR, CLIPPINGS_DIR)

if __name__ == '__main__':
    main()

