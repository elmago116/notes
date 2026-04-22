#!/usr/bin/env python3
"""
Filter Articles with Specific Citizen Science Keywords
Date: 2025-01-27

Filters the citizen science articles list to only include articles with
specific keywords from TFM1_Citizen_Science_Keywords.md lines 3-11.
"""

import re

# Specific keywords to filter by (from TFM1_Citizen_Science_Keywords.md lines 3-11)
TARGET_KEYWORDS = [
    'citizen science',
    'citizen participation',
    'community-based participatory research',
    'Community-based Co-design',
    'Community-based co-design',
    'Community-based',
    'senior citizens.',
    'Senior citizen.',
    'Senior citizens'
]

def normalize_keyword(keyword):
    """Normalize keyword for case-insensitive matching."""
    # Remove backticks and normalize
    return keyword.strip().strip('`').strip()

def article_matches_keywords(keywords_text, target_keywords):
    """Check if article keywords contain any target keywords."""
    if not keywords_text:
        return False
    
    # Extract keywords from the text (they're in backticks)
    keywords_found = re.findall(r'`([^`]+)`', keywords_text)
    
    # Normalize and check
    normalized_found = [normalize_keyword(kw) for kw in keywords_found]
    
    # Case-insensitive matching
    for found_kw in normalized_found:
        for target_kw in target_keywords:
            if found_kw.lower() == target_kw.lower() or target_kw.lower() in found_kw.lower():
                return True
    
    return False

def filter_articles(input_file, output_file, target_keywords):
    """Filter articles based on target keywords."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by article sections (## pattern)
    articles = re.split(r'^## \d+\.', content, flags=re.MULTILINE)
    
    filtered_articles = []
    header = articles[0] if articles else ""  # Keep the header
    
    for article in articles[1:]:  # Skip header
        if not article.strip():
            continue
        
        # Extract the "Citizen Science Keywords Found" field
        keywords_match = re.search(r'\*\*Citizen Science Keywords Found:\*\* (.+?)(?=\n\*\*|$)', article, re.DOTALL)
        
        if keywords_match:
            keywords_text = keywords_match.group(1)
            if article_matches_keywords(keywords_text, target_keywords):
                filtered_articles.append(article)
    
    # Build output
    output = header + "\n"
    output = output.replace("**Total articles found:** 244", f"**Total articles found:** {len(filtered_articles)}")
    output += "This document lists articles from TFM1.ris that contain the following specific citizen science keywords:\n"
    output += "- citizen science\n"
    output += "- citizen participation\n"
    output += "- community-based participatory research\n"
    output += "- Community-based Co-design / Community-based co-design / Community-based\n"
    output += "- senior citizens. / Senior citizen. / Senior citizens\n"
    output += "\n---\n\n"
    
    # Add filtered articles with renumbered headers
    for idx, article in enumerate(filtered_articles, 1):
        output += f"## {idx}.{article}\n\n---\n\n"
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Filtered articles: {len(filtered_articles)}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    input_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_articles_list.md"
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_articles_list.md"
    
    print("Filtering articles with specific citizen science keywords...")
    filter_articles(input_file, output_file, TARGET_KEYWORDS)

