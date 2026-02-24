#!/usr/bin/env python3
"""
Auto-tag Clippings files based on title analysis and existing tag patterns

This script:
1. Analyzes existing tags in Clippings files to learn tag taxonomy
2. Analyzes titles of files without tags or with empty tags
3. Extracts keywords from titles and matches to existing tag patterns
4. Adds appropriate tags to YAML frontmatter

Usage:
    python3 auto_tag_from_titles.py [--dry-run] [--apply]
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, List, Tuple, Optional
import argparse

YAML_START = "---\n"
YAML_END = "---\n"

def split_yaml_and_body(content: str) -> Tuple[Optional[str], str]:
    """Split YAML frontmatter from body"""
    if content.startswith(YAML_START):
        end_idx = content.find(YAML_END, len(YAML_START))
        if end_idx != -1:
            yaml_block = content[len(YAML_START):end_idx]
            body = content[end_idx + len(YAML_END):]
            return yaml_block, body
    return None, content

def parse_yaml_block(yaml_content: str) -> Dict:
    """Parse YAML content into dictionary"""
    metadata = {}
    lines = yaml_content.split('\n')
    current_key = None
    current_list = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ':' in line and not line.startswith(' ') and not line.startswith('-'):
            if current_key and current_list:
                metadata[current_key] = current_list
                current_list = []
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip().strip('"\'')
            if value:
                metadata[key] = value
            current_key = key
        elif line.startswith('- ') or line.startswith('  - '):
            item = line.lstrip('- ').strip().strip('"\'')
            if item:
                current_list.append(item)
    
    if current_key and current_list:
        metadata[current_key] = current_list
    elif current_key and not current_list:
        metadata[current_key] = []
    
    return metadata

def format_yaml_block(metadata: Dict) -> str:
    """Format metadata dictionary as YAML block"""
    lines = ['---']
    
    # Order fields consistently
    field_order = ['title', 'authors', 'year', 'type', 'journal', 'doi', 'base', 'source', 'tags']
    remaining_keys = set(metadata.keys()) - set(field_order)
    
    for key in field_order:
        if key in metadata:
            value = metadata[key]
            if isinstance(value, list):
                if value:
                    lines.append(f'{key}:')
                    for item in sorted(value) if key == 'tags' else value:
                        lines.append(f'  - {item}')
                else:
                    lines.append(f'{key}: []')
            else:
                if ' ' in str(value) and not value.startswith('"') and not value.startswith("'"):
                    lines.append(f'{key}: "{value}"')
                else:
                    lines.append(f'{key}: {value}')
    
    for key in sorted(remaining_keys):
        value = metadata[key]
        if isinstance(value, list):
            if value:
                lines.append(f'{key}:')
                for item in value:
                    lines.append(f'  - {item}')
        else:
            if ' ' in str(value) and not value.startswith('"'):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f'{key}: {value}')
    
    lines.append('---')
    return '\n'.join(lines) + '\n'

def extract_tags_from_title(title: str, filename: str) -> List[str]:
    """Extract tags from title based on keyword matching"""
    tags = set()
    title_lower = title.lower()
    filename_lower = filename.lower()
    combined = f"{title_lower} {filename_lower}"
    
    # Knowledge Graph (most specific first)
    if any(kw in combined for kw in ['knowledge graph', 'knowledge-graph', 'kg']):
        if 'cultural heritage' in combined:
            tags.add('Tech/KG')
            tags.add('themes/heritage')
        else:
            tags.add('Tech/KG')
    
    # Neuro-symbolic AI (specific)
    if any(kw in combined for kw in ['neuro-symbolic', 'neurosymbolic', 'neural-symbolic']):
        tags.add('Tech/NeuroSymbolic')
    
    # AI/ML
    if any(kw in combined for kw in ['artificial intelligence', ' ai ', 'machine learning']):
        tags.add('Tech/AI')
    
    # Semantic Web
    if any(kw in combined for kw in ['semantic web', 'rdf', 'sparql', 'owl', 'linked data', 'lod']):
        tags.add('Tech/SemanticWeb')
    if 'ontology' in combined and 'semantic' not in combined:
        tags.add('Tech/SemanticWeb')
    
    # User-Centered Design
    if any(kw in combined for kw in ['user-centered', 'user centred', 'ucd', 'usability', 'ux']):
        tags.add('design/UCD')
    
    # Participatory Design
    if any(kw in combined for kw in ['participatory', 'co-design', 'co design', 'crowdsourcing']):
        tags.add('design/participatory')
    
    # Digital Humanities
    if any(kw in combined for kw in ['digital humanities', 'dh']):
        tags.add('themes/DH')
    
    # GLAM
    if any(kw in combined for kw in ['glam', 'museum', 'library', 'archive', 'gallery']):
        tags.add('themes/GLAM')
    
    # Gender/HerStory (be specific - not all bias is gender bias)
    if any(kw in combined for kw in ['gender bias', 'gender gap', 'women', 'feminist', 'herstory']):
        tags.add('themes/HerStory')
    if 'bias' in combined and ('gender' in combined or 'women' in combined):
        tags.add('themes/HerStory')
    
    # Algorithmic bias (more general)
    if 'algorithmic bias' in combined:
        tags.add('themes/bias')
    
    # Citizen Science
    if any(kw in combined for kw in ['citizen science', 'volunteer', 'crowd']):
        tags.add('themes/citizen_science')
    
    # Health
    if any(kw in combined for kw in ['health', 'medical', 'dementia', 'mental health']):
        tags.add('themes/health')
    
    # Bibliometrics
    if any(kw in combined for kw in ['bibliometric', 'scientometric', 'science mapping']):
        tags.add('bibliometrics')
    
    # Cultural Heritage
    if 'cultural heritage' in combined:
        tags.add('themes/heritage')
    
    # Research methods
    if any(kw in combined for kw in ['systematic review', 'scoping review', 'meta-analysis']):
        tags.add('research_method')
    
    # Tools
    if any(kw in combined for kw in ['tool', 'platform', 'system', 'software']):
        tags.add('op/tool')
    
    return sorted(tags)

def learn_from_existing_tags(clippings_path: Path) -> Dict[str, Set[str]]:
    """Learn tag patterns from files that already have tags"""
    tag_examples = defaultdict(set)
    
    md_files = list(clippings_path.rglob('*.md'))
    print(f"Learning from {len(md_files)} files...")
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
            yaml_content, body = split_yaml_and_body(content)
            
            if yaml_content:
                metadata = parse_yaml_block(yaml_content)
                title = metadata.get('title', md_file.stem)
                existing_tags = metadata.get('tags', [])
                
                if existing_tags and isinstance(existing_tags, list):
                    title_lower = title.lower()
                    words = re.findall(r'\b\w{4,}\b', title_lower)  # Words 4+ chars
                    for tag in existing_tags:
                        for word in words:
                            tag_examples[tag].add(word)
        except Exception:
            continue
    
    return tag_examples

def process_files(clippings_path: Path, dry_run: bool = True):
    """Process all Clippings files and add tags"""
    
    print("=" * 70)
    print("Auto-tagging Clippings files based on title analysis")
    print("=" * 70)
    print()
    
    md_files = list(clippings_path.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files\n")
    
    updated = 0
    skipped = 0
    
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
            yaml_content, body = split_yaml_and_body(content)
            
            if not yaml_content:
                skipped += 1
                continue
            
            metadata = parse_yaml_block(yaml_content)
            
            # Get title
            title = metadata.get('title', '')
            if not title:
                title = md_file.stem
            
            # Check existing tags
            existing_tags = metadata.get('tags', [])
            if isinstance(existing_tags, str):
                existing_tags = [existing_tags] if existing_tags else []
            elif not isinstance(existing_tags, list):
                existing_tags = []
            
            # Skip if already has tags
            if existing_tags:
                skipped += 1
                continue
            
            # Extract tags from title
            new_tags = extract_tags_from_title(title, md_file.stem)
            
            if new_tags:
                # Merge with existing (should be empty but just in case)
                all_tags = sorted(set(existing_tags) | set(new_tags))
                metadata['tags'] = all_tags
                
                # Rebuild file
                new_yaml = format_yaml_block(metadata)
                new_content = new_yaml + '\n' + body
                
                if not dry_run:
                    md_file.write_text(new_content, encoding='utf-8')
                
                print(f"{'[DRY RUN] ' if dry_run else ''}✓ {md_file.name[:60]}")
                print(f"  Tags added: {', '.join(new_tags)}")
                updated += 1
            else:
                skipped += 1
        
        except Exception as e:
            print(f"✗ Error processing {md_file.name}: {e}")
            continue
    
    print(f"\n{'='*70}")
    print(f"Summary:")
    print(f"  Files updated: {updated}")
    print(f"  Files skipped: {skipped} (already have tags or no tags found)")
    if dry_run:
        print(f"\n  This was a DRY RUN. Use --apply to make changes.")

def main():
    parser = argparse.ArgumentParser(description='Auto-tag Clippings files from titles')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default is dry-run)')
    parser.add_argument('--root', type=str, default='Clippings', help='Root directory (default: Clippings)')
    args = parser.parse_args()
    
    clippings_path = Path(args.root)
    if not clippings_path.exists():
        print(f"Error: Directory not found: {clippings_path}")
        sys.exit(1)
    
    process_files(clippings_path, dry_run=not args.apply)

if __name__ == "__main__":
    main()

