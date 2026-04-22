#!/usr/bin/env python3
"""
Normalize clipping and PDF filenames based on extraction_matches.md and add extraction sections.
"""

import re
from pathlib import Path
from typing import Optional, List, Tuple

root = Path('/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents')
matches_file = root / 'Drafts/Scripts/extraction_matches.md'
clippings_dir = root / 'Clippings'
pdf_dir = root / 'PDF'
extracted_dir = clippings_dir / 'Extracted'

EXCLUDED_TAGS = ['#op/projects/peninsula', '#op/projects/UBXAT', '#op/projects/WikiData', '#op/doc', '#op/activity']
SECTION_TITLE = "## PDF text extraction"


def parse_matches() -> List[Tuple[str, str, Optional[str]]]:
    """Parse matches file: (extracted_stem, clipping_name, pdf_name)"""
    content = matches_file.read_text(encoding='utf-8')
    matches = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('- ') and not line.startswith('    -'):
            extracted_stem = line[2:].strip()
            clipping_name = None
            pdf_name = None
            
            j = i + 1
            while j < len(lines) and (lines[j].startswith('    -') or lines[j].strip() == ''):
                subline = lines[j].strip()
                if 'clipping:' in subline.lower():
                    # Check if it says "(missing)" - still extract the link if present
                    if '(missing)' in subline.lower():
                        m = re.search(r'\[\[([^\]]+)\]\]', subline)
                        if m:
                            link = m.group(1)
                            if '|' in link:
                                clipping_name = link.split('|')[0].strip()
                            else:
                                clipping_name = link.strip()
                            # Remove .pdf extension if present
                            if clipping_name.endswith('.pdf'):
                                clipping_name = clipping_name[:-4]
                        else:
                            clipping_name = None
                    else:
                        # Normal link extraction
                        m = re.search(r'\[\[([^\]]+)\]\]', subline)
                        if m:
                            link = m.group(1)
                            if '|' in link:
                                clipping_name = link.split('|')[0].strip()
                            else:
                                clipping_name = link.strip()
                        else:
                            clipping_name = None
                    
                    if clipping_name:
                        if clipping_name.startswith('Clippings/'):
                            clipping_name = clipping_name[10:]
                        if clipping_name.startswith('['):
                            clipping_name = clipping_name[1:]
                        if clipping_name.endswith(']'):
                            clipping_name = clipping_name[:-1]
                elif 'pdf:' in subline.lower() and 'no PDF found' not in subline:
                    m = re.search(r'\[\[([^\]]+)\]\]', subline)
                    if m:
                        pdf_name = m.group(1).strip()
                        if pdf_name.endswith('.pdf'):
                            pdf_name = pdf_name[:-4]
                
                j += 1
            
            # Include if we have a clipping name (even if it was marked as missing, we extracted a link)
            if clipping_name:
                matches.append((extracted_stem, clipping_name, pdf_name))
            
            i = j
        else:
            i += 1
    
    return matches


def normalize_filename(name: str) -> str:
    """Normalize filename: replace colons, remove special chars"""
    name = name.replace(':', '-')
    name = name.replace('/', '-')
    return name


def find_clipping_file(name: str) -> Optional[Path]:
    """Find clipping file by name (handles aliases, case-insensitive, partial matches)"""
    name_clean = name.replace('Clippings/', '').strip()
    # Remove .pdf extension if present
    if name_clean.endswith('.pdf'):
        name_clean = name_clean[:-4]
    candidates = list(clippings_dir.rglob('*.md'))
    name_lower = name_clean.lower()
    
    # Try exact match first
    for md in candidates:
        if md.parent == extracted_dir:
            continue
        if md.stem.lower() == name_lower:
            return md
    
    # Try normalized match
    for md in candidates:
        if md.parent == extracted_dir:
            continue
        if normalize_filename(md.stem).lower() == normalize_filename(name_clean).lower():
            return md
    
    # Try partial match (name contains stem or vice versa)
    for md in candidates:
        if md.parent == extracted_dir:
            continue
        md_stem_lower = md.stem.lower()
        # Check if one contains the other (for manual connections)
        if name_lower in md_stem_lower or md_stem_lower in name_lower:
            # Prefer longer match
            if len(md_stem_lower) > len(name_lower) * 0.8:  # At least 80% match
                return md
    
    return None


def find_pdf_file(name: str) -> Optional[Path]:
    """Find PDF file by name"""
    if not name:
        return None
    name_clean = name.replace('PDF/', '').replace('.pdf', '').strip()
    candidates = list(pdf_dir.rglob('*.pdf'))
    
    for pdf in candidates:
        if 'Scripts' in pdf.parts:
            continue
        if pdf.stem == name_clean or normalize_filename(pdf.stem) == normalize_filename(name_clean):
            return pdf
        if pdf.stem.lower() == name_clean.lower():
            return pdf
    
    return None


def has_excluded_tags(md_path: Path) -> bool:
    """Check if file has excluded tags"""
    try:
        content = md_path.read_text(encoding='utf-8')
        for tag in EXCLUDED_TAGS:
            if tag in content:
                return True
    except:
        pass
    return False


def has_extraction_section(md_path: Path) -> bool:
    """Check if file already has extraction section"""
    try:
        content = md_path.read_text(encoding='utf-8')
        return SECTION_TITLE.lower() in content.lower()
    except:
        return False


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter"""
    fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, flags=re.DOTALL)
    if fm:
        return text[fm.end():]
    return text


def update_links_in_file(file_path: Path, old_name: str, new_name: str) -> bool:
    """Update all links to old_name with new_name in a file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        # Pattern: [[old_name]] or [[old_name|alias]]
        pattern = r'\[\[(' + re.escape(old_name) + r')(\|[^\]]+)?\]\]'
        replacement = f'[[{new_name}\\2]]'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            file_path.write_text(new_content, encoding='utf-8')
            return True
    except Exception as e:
        print(f"    Error updating {file_path.name}: {e}")
    return False


def update_all_links(old_name: str, new_name: str) -> int:
    """Update links in all markdown files"""
    updated_count = 0
    for md in root.rglob('*.md'):
        if md.parent == extracted_dir:
            continue
        if update_links_in_file(md, old_name, new_name):
            updated_count += 1
    return updated_count


def rename_clipping(old_path: Path, new_stem: str) -> Path:
    """Rename clipping file to match extracted stem"""
    if old_path.stem == new_stem:
        return old_path
    
    new_path = old_path.parent / f"{new_stem}.md"
    if new_path.exists() and new_path != old_path:
        print(f"    Warning: {new_path.name} already exists, skipping rename")
        return old_path
    
    old_name = old_path.stem
    old_path.rename(new_path)
    print(f"    Renamed clipping: {old_name} -> {new_stem}")
    
    link_updates = update_all_links(old_name, new_stem)
    if link_updates > 0:
        print(f"      Updated {link_updates} links")
    
    return new_path


def rename_pdf(old_path: Path, new_stem: str) -> Path:
    """Rename PDF file to match extracted stem"""
    if old_path.stem == new_stem:
        return old_path
    
    new_path = old_path.parent / f"{new_stem}.pdf"
    if new_path.exists() and new_path != old_path:
        print(f"    Warning: {new_path.name} already exists, skipping rename")
        return old_path
    
    old_name = old_path.stem
    old_path.rename(new_path)
    print(f"    Renamed PDF: {old_name} -> {new_stem}")
    return new_path


def add_extraction_section(clipping_path: Path, extracted_path: Path):
    """Add extraction section to clipping if not present and not excluded"""
    if has_excluded_tags(clipping_path):
        print(f"    Skipped extraction (excluded tags): {clipping_path.name}")
        return False
    
    if has_extraction_section(clipping_path):
        print(f"    Skipped extraction (section exists): {clipping_path.name}")
        return False
    
    try:
        extracted_text = extracted_path.read_text(encoding='utf-8')
        body = strip_frontmatter(extracted_text).strip()
        if not body:
            print(f"    Skipped extraction (empty): {clipping_path.name}")
            return False
        
        content = clipping_path.read_text(encoding='utf-8')
        updated = content.rstrip() + "\n\n" + SECTION_TITLE + "\n\n" + body + "\n"
        clipping_path.write_text(updated, encoding='utf-8')
        print(f"    Added extraction section: {clipping_path.name}")
        return True
    except Exception as e:
        print(f"    Error adding section to {clipping_path.name}: {e}")
        return False


def main():
    matches = parse_matches()
    print(f"Found {len(matches)} matches\n")
    
    renamed_clippings = 0
    renamed_pdfs = 0
    added_sections = 0
    
    for extracted_stem, clipping_name, pdf_name in matches:
        print(f"\nProcessing: {extracted_stem}")
        
        # Find and rename clipping
        clipping_file = find_clipping_file(clipping_name)
        if clipping_file:
            new_clipping = rename_clipping(clipping_file, extracted_stem)
            if new_clipping != clipping_file:
                renamed_clippings += 1
            clipping_file = new_clipping
        else:
            print(f"    Clipping not found: {clipping_name}")
            continue
        
        # Find and rename PDF
        if pdf_name and pdf_name != '(no PDF found)':
            pdf_file = find_pdf_file(pdf_name)
            if pdf_file:
                new_pdf = rename_pdf(pdf_file, extracted_stem)
                if new_pdf != pdf_file:
                    renamed_pdfs += 1
            else:
                print(f"    PDF not found: {pdf_name}")
        
        # Add extraction section
        extracted_file = extracted_dir / f"{extracted_stem}.md"
        if extracted_file.exists():
            if add_extraction_section(clipping_file, extracted_file):
                added_sections += 1
    
    print(f"\n\nSummary:")
    print(f"  Renamed clippings: {renamed_clippings}")
    print(f"  Renamed PDFs: {renamed_pdfs}")
    print(f"  Added extraction sections: {added_sections}")


if __name__ == "__main__":
    main()

