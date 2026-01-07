#!/usr/bin/env python3
"""
Check which references from a markdown file are in TFM1.ris
and mark them in the markdown file
"""

from pathlib import Path
import re

# Read RIS file and extract all titles
ris_file = Path('TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris')
print(f"Reading RIS file: {ris_file}")
ris_content = ris_file.read_text(encoding='utf-8', errors='ignore')

# Extract all titles from RIS - pattern is "TI  - Title" (two spaces)
ris_titles = []
for match in re.finditer(r'^TI\s{2}-\s+(.+?)(?=\n[A-Z]{2}\s{2}-|\nER|\Z)', ris_content, re.MULTILINE | re.DOTALL):
    title = match.group(1).strip()
    if title:
        ris_titles.append(title)

print(f"Extracted {len(ris_titles)} titles from RIS file\n")

# Read markdown file
md_file = Path('Clippings/The_Multiple_Faces_of_Cultural_Heritage_Towards_an_Integrated_Visualization_Platform_for_Tangible_and_Intangible_Cultural_Assets.md')
md_content = md_file.read_text(encoding='utf-8')

# Extract references section
refs_match = re.search(r'## References\n\n(.*?)$', md_content, re.DOTALL)
if not refs_match:
    print("No references section found!")
    exit(1)

refs_text = refs_match.group(1)
refs_lines = [line for line in refs_text.split('\n') if line.strip() and re.match(r'^\d+\.', line.strip())]

print(f"Found {len(refs_lines)} references in markdown file\n")

# Function to normalize title for comparison
def normalize_title(text):
    """Normalize text for comparison"""
    if not text:
        return ""
    # Remove markdown formatting
    text = re.sub(r'\*([^*]+)\*', r'\1', text)  # Remove italics
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Remove links
    # Remove special chars, normalize spaces
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to extract title from reference line
def extract_title_from_ref(ref_line):
    """Extract title from reference citation"""
    # Remove number prefix
    ref_line = re.sub(r'^\d+\.\s*', '', ref_line)
    
    # Remove authors - typically everything before first period or colon that's followed by title
    # Titles usually come after author names which end with period or comma+&
    # Try multiple patterns
    patterns = [
        r'^[^.]+\.[\s]+([^.*]+?)(?:[.*]|$)',  # Author. Title.
        r'^[^:]+:\s*([^.*]+?)(?:[.*]|$)',  # Author: Title
        r'\.\s+([A-Z][^.*]+?)[.*]',  # . Title.
    ]
    
    for pattern in patterns:
        match = re.search(pattern, ref_line)
        if match:
            title = match.group(1).strip()
            # Clean up
            title = re.sub(r'^(In|In Proceedings of|At)\s+', '', title, flags=re.I)
            return title.strip()
    
    # Fallback: take first part after removing common prefixes
    return ref_line.split('.')[0] if '.' in ref_line else ref_line

# Check each reference
matched_refs = {}
for i, ref_line in enumerate(refs_lines, 1):
    ref_title = extract_title_from_ref(ref_line)
    if ref_title:
        ref_normalized = normalize_title(ref_title)
        
        # Check against RIS titles
        for ris_title in ris_titles:
            ris_normalized = normalize_title(ris_title)
            
            if not ref_normalized or not ris_normalized:
                continue
                
            # Check for significant overlap
            ref_words = set(ref_normalized.split())
            ris_words = set(ris_normalized.split())
            
            # Filter out common words
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were'}
            ref_words = {w for w in ref_words if len(w) > 3 and w not in stop_words}
            ris_words = {w for w in ris_words if len(w) > 3 and w not in stop_words}
            
            if not ref_words:
                continue
            
            # Calculate overlap
            overlap = ref_words & ris_words
            overlap_ratio = len(overlap) / len(ref_words) if ref_words else 0
            
            # Match if at least 3 significant words overlap OR >50% overlap
            if len(overlap) >= 3 or (len(ref_words) >= 5 and overlap_ratio > 0.5):
                matched_refs[i] = ris_title
                print(f"✓ Ref {i} matched: {ref_title[:60]}...")
                print(f"  → RIS: {ris_title[:60]}...")
                break

print(f"\n\nTotal matches: {len(matched_refs)} out of {len(refs_lines)} references")

# Now update the markdown file to mark matched references
if matched_refs:
    # Rebuild references section with markers
    new_refs_lines = []
    for i, ref_line in enumerate(refs_lines, 1):
        if i in matched_refs:
            # Add marker at the end
            if not ref_line.endswith('.'):
                ref_line += '.'
            ref_line += ' ✓ *[in TFM1.ris]*'
        new_refs_lines.append(ref_line)
    
    # Reconstruct the file
    new_refs_text = '\n'.join(new_refs_lines) + '\n'
    
    # Replace references section
    new_md_content = md_content[:refs_match.start(1)] + new_refs_text + md_content[refs_match.end(1):]
    
    # Write back
    md_file.write_text(new_md_content, encoding='utf-8')
    print(f"\n✓ Updated markdown file with {len(matched_refs)} markers")
else:
    print("\nNo matches found - file not updated")



