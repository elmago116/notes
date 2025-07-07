#!/usr/bin/env python3
"""
Script to analyze keyword formatting inconsistencies in RIS files.

This script identifies patterns like:
- Case inconsistencies (e.g., "Digital Humanities" vs "digital humanities")
- Hyphenation variations (e.g., "User-centered" vs "User centered")
- Punctuation differences
- Plural variations
- Abbreviation inconsistencies
"""

import re
import os
from collections import defaultdict, Counter
from pathlib import Path

def extract_keywords_from_ris(file_path):
    """Extract all KW fields from a RIS file."""
    keywords = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('KW  - '):
                    keyword = line[6:].strip()  # Remove 'KW  - ' prefix
                    if keyword:  # Only add non-empty keywords
                        keywords.append(keyword)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return keywords

def normalize_for_comparison(keyword):
    """Create a normalized version for comparison."""
    # Convert to lowercase
    normalized = keyword.lower()
    # Remove punctuation and extra spaces
    normalized = re.sub(r'[^\w\s]', ' ', normalized)
    # Normalize spaces
    normalized = ' '.join(normalized.split())
    return normalized

def find_similar_keywords(keywords):
    """Find groups of similar keywords that might need normalization."""
    # Group keywords by their normalized form
    groups = defaultdict(list)
    
    for keyword in keywords:
        normalized = normalize_for_comparison(keyword)
        groups[normalized].append(keyword)
    
    # Only return groups with multiple variations
    similar_groups = {}
    for normalized, variations in groups.items():
        if len(set(variations)) > 1:  # More than one unique variation
            similar_groups[normalized] = variations
    
    return similar_groups

def analyze_case_patterns(keywords):
    """Analyze capitalization patterns."""
    patterns = {
        'all_caps': [],
        'title_case': [],
        'sentence_case': [],
        'all_lower': [],
        'mixed_case': []
    }
    
    for keyword in keywords:
        if keyword.isupper():
            patterns['all_caps'].append(keyword)
        elif keyword.istitle():
            patterns['title_case'].append(keyword)
        elif keyword.islower():
            patterns['all_lower'].append(keyword)
        elif keyword[0].isupper() and not keyword.istitle():
            patterns['sentence_case'].append(keyword)
        else:
            patterns['mixed_case'].append(keyword)
    
    return patterns

def analyze_hyphenation_patterns(keywords):
    """Find hyphenation inconsistencies."""
    hyphen_groups = defaultdict(list)
    
    for keyword in keywords:
        # Create versions with and without hyphens for comparison
        no_hyphen = keyword.replace('-', ' ')
        base_form = normalize_for_comparison(no_hyphen)
        hyphen_groups[base_form].append(keyword)
    
    # Only return groups with both hyphenated and non-hyphenated versions
    inconsistent_hyphenation = {}
    for base, variations in hyphen_groups.items():
        unique_variations = list(set(variations))
        if len(unique_variations) > 1:
            # Check if we have both hyphenated and non-hyphenated versions
            has_hyphen = any('-' in var for var in unique_variations)
            has_no_hyphen = any('-' not in var for var in unique_variations)
            if has_hyphen and has_no_hyphen:
                inconsistent_hyphenation[base] = unique_variations
    
    return inconsistent_hyphenation

def main():
    """Analyze keyword patterns across all RIS files."""
    
    # List of files to analyze
    files_to_analyze = [
        "RIS completos/metadataScopus3_completo.ris",
        "RIS completos/metadataScopus1_authors_enriched.ris",
        "RIS completos/metadataWoS1_completo.ris", 
        "RIS completos/metadataWoS1+_completo.ris",
        "RIS completos/metadataWoS2_completo.ris",
        "RIS completos/metadataWoS3_completo.ris"
    ]
    
    all_keywords = []
    file_keyword_counts = {}
    
    print("🔍 ANALYZING KEYWORD PATTERNS IN RIS FILES")
    print("=" * 60)
    
    # Extract keywords from all files
    for file_path in files_to_analyze:
        if os.path.exists(file_path):
            keywords = extract_keywords_from_ris(file_path)
            file_keyword_counts[os.path.basename(file_path)] = len(keywords)
            all_keywords.extend(keywords)
            print(f"✅ {os.path.basename(file_path)}: {len(keywords)} keywords")
        else:
            print(f"❌ File not found: {file_path}")
    
    print(f"\n📊 TOTAL KEYWORDS EXTRACTED: {len(all_keywords)}")
    print(f"📊 UNIQUE KEYWORDS: {len(set(all_keywords))}")
    
    # Analyze patterns
    print("\n" + "="*60)
    print("🔍 CASE PATTERN ANALYSIS")
    print("="*60)
    
    case_patterns = analyze_case_patterns(all_keywords)
    for pattern, keywords in case_patterns.items():
        if keywords:
            print(f"\n{pattern.upper().replace('_', ' ')}: {len(set(keywords))} unique")
            # Show first few examples
            examples = list(set(keywords))[:5]
            for example in examples:
                print(f"  • {example}")
            if len(set(keywords)) > 5:
                print(f"  ... and {len(set(keywords)) - 5} more")
    
    print("\n" + "="*60)
    print("🔍 SIMILAR KEYWORD GROUPS (potential inconsistencies)")
    print("="*60)
    
    similar_groups = find_similar_keywords(all_keywords)
    inconsistency_count = 0
    
    for normalized, variations in similar_groups.items():
        unique_variations = list(set(variations))
        if len(unique_variations) > 1:
            inconsistency_count += 1
            print(f"\n{inconsistency_count}. Base form: '{normalized}'")
            variation_counts = Counter(variations)
            for variation, count in variation_counts.most_common():
                print(f"   → '{variation}' (appears {count} times)")
    
    print(f"\n📊 FOUND {inconsistency_count} GROUPS WITH INCONSISTENT FORMATTING")
    
    print("\n" + "="*60)
    print("🔍 HYPHENATION INCONSISTENCIES")
    print("="*60)
    
    hyphen_inconsistencies = analyze_hyphenation_patterns(all_keywords)
    hyphen_count = 0
    
    for base, variations in hyphen_inconsistencies.items():
        hyphen_count += 1
        print(f"\n{hyphen_count}. Base: '{base}'")
        for variation in set(variations):
            count = all_keywords.count(variation)
            print(f"   → '{variation}' (appears {count} times)")
    
    print(f"\n📊 FOUND {hyphen_count} GROUPS WITH HYPHENATION INCONSISTENCIES")
    
    # Most common keywords
    print("\n" + "="*60)
    print("🔍 MOST COMMON KEYWORDS")
    print("="*60)
    
    keyword_counts = Counter(all_keywords)
    for keyword, count in keyword_counts.most_common(20):
        print(f"  {count:3d}x  '{keyword}'")
    
    print("\n🎉 ANALYSIS COMPLETE!")
    print(f"💡 Consider normalizing the {inconsistency_count + hyphen_count} identified inconsistency groups")

if __name__ == "__main__":
    main() 