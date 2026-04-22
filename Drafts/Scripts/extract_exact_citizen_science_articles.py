#!/usr/bin/env python3
"""
Extract Articles with EXACT Citizen Science Keywords Only
Date: 2025-01-27

Only extracts articles with the EXACT keywords from TFM1_Citizen_Science_Keywords.md lines 3-11.
"""

import re
from pathlib import Path

# EXACT keywords only (from TFM1_Citizen_Science_Keywords.md lines 3-11)
EXACT_KEYWORDS = [
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

def load_ris_file(file_path):
    """Load and parse RIS file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_field(record, field_code):
    """Extract a specific field from RIS record."""
    pattern = rf'^{field_code}\s*-\s*(.+?)(?=\n[A-Z]{{2}}\s*-|\nER|\Z)'
    match = re.search(pattern, record, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def extract_all_keywords(record):
    """Extract all KW fields from a record."""
    keywords = []
    for match in re.finditer(r'^KW\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.MULTILINE | re.DOTALL | re.IGNORECASE):
        keywords.append(match.group(1).strip())
    return keywords

def find_exact_keyword_matches(search_text, exact_keywords):
    """Find which exact keywords appear in the search text."""
    found = []
    search_text_lower = search_text.lower()
    
    for keyword in exact_keywords:
        # Create pattern for exact match (case-insensitive)
        # Handle punctuation and word boundaries
        keyword_lower = keyword.lower().rstrip('.')
        pattern = r'\b' + re.escape(keyword_lower) + r'\.?\b'
        
        if re.search(pattern, search_text_lower):
            found.append(keyword)
    
    return found

def format_article_list(articles):
    """Format articles into markdown format."""
    
    output = []
    output.append("# Articles with Citizen Science Keywords")
    output.append("")
    output.append(f"**Date of extraction:** 2025-01-27")
    output.append(f"**Total articles found:** {len(articles)}")
    output.append("")
    output.append("This document lists articles from TFM1.ris that contain the following EXACT citizen science keywords (from TFM1_Citizen_Science_Keywords.md, lines 3-11):")
    output.append("- citizen science")
    output.append("- citizen participation")
    output.append("- community-based participatory research")
    output.append("- Community-based Co-design / Community-based co-design / Community-based")
    output.append("- senior citizens. / Senior citizen. / Senior citizens")
    output.append("")
    output.append("---")
    output.append("")
    
    # List articles
    for idx, article in enumerate(articles, 1):
        output.append(f"## {idx}. {article['title']}")
        output.append("")
        
        # Authors
        if article['authors']:
            authors_str = ", ".join(article['authors'])
            output.append(f"**Authors:** {authors_str}")
        else:
            output.append("**Authors:** Not specified")
        output.append("")
        
        # Year
        output.append(f"**Year:** {article['year']}")
        output.append("")
        
        # Journal
        output.append(f"**Journal/Publication:** {article['journal']}")
        output.append("")
        
        # Volume/Issue/Pages
        if article['volume'] or article['issue'] or article['pages']:
            vol_info = []
            if article['volume']:
                vol_info.append(f"Vol. {article['volume']}")
            if article['issue']:
                vol_info.append(f"Iss. {article['issue']}")
            if article['pages']:
                vol_info.append(f"pp. {article['pages']}")
            output.append(f"**Publication Details:** {', '.join(vol_info)}")
            output.append("")
        
        # DOI
        if article['doi']:
            output.append(f"**DOI:** {article['doi']}")
            output.append("")
        
        # Citizen Science Keywords Found
        keywords_str = ", ".join([f"`{kw}`" for kw in article['citizen_science_keywords_found']])
        output.append(f"**Citizen Science Keywords Found:** {keywords_str}")
        output.append("")
        
        # Keywords
        if article['keywords']:
            all_keywords = ", ".join(article['keywords'])
            output.append(f"**Keywords:** {all_keywords}")
            output.append("")
        
        # Abstract (truncated if too long)
        if article['abstract'] and article['abstract'] != 'No abstract':
            abstract = article['abstract']
            if len(abstract) > 500:
                abstract = abstract[:500] + "..."
            output.append(f"**Abstract:** {abstract}")
            output.append("")
        
        output.append("---")
        output.append("")
    
    return "\n".join(output)

def main():
    """Main function to extract and format articles."""
    
    ris_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris"
    
    print("Extracting Articles with EXACT Citizen Science Keywords Only")
    print("=" * 60)
    print(f"Analyzing file: {ris_file_path}")
    print()
    print("Looking for these EXACT keywords only:")
    for kw in EXACT_KEYWORDS:
        print(f"  - {kw}")
    print()
    
    # Load RIS file
    print("Loading RIS file...")
    ris_content = load_ris_file(ris_file_path)
    if ris_content is None:
        return
    
    print(f"File loaded successfully.")
    print()
    
    # Split content by records
    records = re.split(r'ER\s*-\s*\n', ris_content)
    
    filtered_articles = []
    
    print("Searching for articles with exact keywords...")
    for i, record in enumerate(records):
        if not record.strip():
            continue
        
        # Extract fields
        title = extract_field(record, 'TI')
        authors = []
        for match in re.finditer(r'^AU\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.MULTILINE | re.DOTALL | re.IGNORECASE):
            authors.append(match.group(1).strip())
        year = extract_field(record, 'PY')
        journal = extract_field(record, 'JO')
        volume = extract_field(record, 'VL')
        issue = extract_field(record, 'IS')
        pages = extract_field(record, 'SP')
        pages_end = extract_field(record, 'EP')
        doi = extract_field(record, 'DO')
        abstract = extract_field(record, 'AB')
        keywords = extract_all_keywords(record)
        
        # Build search text
        search_text = ""
        if title:
            search_text += " " + title
        if abstract:
            search_text += " " + abstract
        if keywords:
            search_text += " " + " ".join(keywords)
        
        # Find exact keyword matches
        found_keywords = find_exact_keyword_matches(search_text, EXACT_KEYWORDS)
        
        # Only include if we found exact matches
        if found_keywords:
            article_info = {
                'record_number': i,
                'title': title or 'No title',
                'authors': authors,
                'year': year or 'No year',
                'journal': journal or 'No journal',
                'volume': volume,
                'issue': issue,
                'pages': f"{pages}-{pages_end}" if pages and pages_end else (pages or ''),
                'doi': doi,
                'abstract': abstract or 'No abstract',
                'keywords': keywords,
                'citizen_science_keywords_found': sorted(list(set(found_keywords)))
            }
            filtered_articles.append(article_info)
    
    print(f"Found {len(filtered_articles)} articles with exact keywords")
    print()
    
    # Format and save results
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_articles_list.md"
    print(f"Formatting article list...")
    formatted_output = format_article_list(filtered_articles)
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
        return
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total articles found: {len(filtered_articles)}")
    print(f"\nOutput file: {output_file}")

if __name__ == "__main__":
    main()

