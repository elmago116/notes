#!/usr/bin/env python3
"""
Extract Articles with Citizen Science Keywords
Date of creation: 2025-01-27

This script extracts full bibliographic records for articles containing 
citizen science related keywords from a RIS document.
"""

import re
from collections import defaultdict
from pathlib import Path

def load_ris_file(file_path):
    """Load and parse RIS file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
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

def extract_citizen_science_articles(ris_content):
    """Extract articles with citizen science related keywords."""
    
    # Core citizen science keywords from the keywords list file
    citizen_science_keywords = [
        'citizen science',
        'citizen scientist',
        'citizen scientists',
        'crowdsourcing',
        'crowd-sourcing',
        'crowd sourcing',
        'volunteer',
        'participatory',
        'community-based',
        'community engagement',
        'community participation',
        'public participation',
        'public engagement',
        'open science',
        'open research',
        'collaborative research',
        'participatory research',
        'participatory observation',
        'community mapping',
    ]
    
    # Create compiled patterns for case-insensitive matching
    patterns = [re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE) 
                for keyword in citizen_science_keywords]
    
    # Split content by records (separated by ER -)
    records = re.split(r'ER\s*-\s*\n', ris_content)
    
    articles_with_keywords = []
    keyword_matches_per_article = defaultdict(list)
    
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
        
        # Search for citizen science keywords in title, abstract, and keywords
        found_keywords = set()
        search_text = ""
        if title:
            search_text += " " + title
        if abstract:
            search_text += " " + abstract
        if keywords:
            search_text += " " + " ".join(keywords)
        
        # Check each pattern
        for pattern in patterns:
            if pattern.search(search_text):
                keyword_text = pattern.pattern.replace(r'\b', '').replace('\\', '')
                found_keywords.add(keyword_text)
        
        # If any citizen science keywords found, add article
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
                'citizen_science_keywords_found': sorted(list(found_keywords))
            }
            articles_with_keywords.append(article_info)
            keyword_matches_per_article[i] = sorted(list(found_keywords))
    
    return articles_with_keywords, keyword_matches_per_article

def format_article_list(articles, output_file_path):
    """Format articles into markdown format."""
    
    output = []
    output.append("# Articles with Citizen Science Keywords")
    output.append("")
    output.append(f"**Date of extraction:** 2025-01-27")
    output.append(f"**Total articles found:** {len(articles)}")
    output.append("")
    output.append("This document lists all articles from TFM1.ris that contain citizen science related keywords in their title, abstract, or keyword fields.")
    output.append("")
    output.append("---")
    output.append("")
    
    # Group articles by keyword
    keyword_to_articles = defaultdict(list)
    for article in articles:
        for keyword in article['citizen_science_keywords_found']:
            keyword_to_articles[keyword].append(article)
    
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
    
    # Path to the RIS file
    ris_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris"
    
    print("Extracting Articles with Citizen Science Keywords")
    print("=" * 60)
    print(f"Analyzing file: {ris_file_path}")
    print()
    
    # Load RIS file
    print("Loading RIS file...")
    ris_content = load_ris_file(ris_file_path)
    if ris_content is None:
        return
    
    print(f"File loaded successfully.")
    print()
    
    # Extract articles
    print("Extracting articles with citizen science keywords...")
    articles, keyword_matches = extract_citizen_science_articles(ris_content)
    
    print(f"Found {len(articles)} articles with citizen science keywords")
    print()
    
    # Format and save results
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_articles_list.md"
    print(f"Formatting article list...")
    formatted_output = format_article_list(articles, output_file)
    
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
    print(f"Total articles found: {len(articles)}")
    print(f"\nOutput file: {output_file}")

if __name__ == "__main__":
    main()

