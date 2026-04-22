#!/usr/bin/env python3
"""
Strict Filter for Articles with Specific Citizen Science Keywords
Date: 2025-01-27

Filters to ONLY include articles with the EXACT keywords from 
TFM1_Citizen_Science_Keywords.md lines 3-11.
"""

import re

# EXACT keywords only (from TFM1_Citizen_Science_Keywords.md lines 3-11)
EXACT_TARGET_KEYWORDS = [
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
    """Normalize keyword for matching."""
    return keyword.strip().strip('`').strip()

def article_matches_exact_keywords(article_text, target_keywords):
    """Check if article contains EXACT target keywords."""
    # Search in the entire article text (title, abstract, keywords, etc.)
    article_lower = article_text.lower()
    
    matches = []
    for target_kw in target_keywords:
        # Case-insensitive exact word boundary matching
        # Handle variations with punctuation
        pattern = r'\b' + re.escape(target_kw.lower()) + r'\.?\b'
        if re.search(pattern, article_lower):
            matches.append(target_kw)
    
    return matches

def filter_articles_strict(input_file, output_file, target_keywords):
    """Filter articles to ONLY include those with exact target keywords."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content by article sections (## pattern)
    articles = re.split(r'^## \d+\.', content, flags=re.MULTILINE)
    
    filtered_articles = []
    header = articles[0] if articles else ""  # Keep the header
    
    for article in articles[1:]:  # Skip header
        if not article.strip():
            continue
        
        # Check if article contains any of the EXACT keywords
        matches = article_matches_exact_keywords(article, target_keywords)
        
        if matches:
            # Verify the matches are in the "Citizen Science Keywords Found" field
            keywords_match = re.search(r'\*\*Citizen Science Keywords Found:\*\* (.+?)(?=\n\*\*|$)', article, re.DOTALL)
            
            if keywords_match:
                keywords_text = keywords_match.group(1)
                # Extract keywords from backticks
                found_keywords = re.findall(r'`([^`]+)`', keywords_text)
                
                # Check if any found keyword matches our target keywords
                has_match = False
                for found_kw in found_keywords:
                    found_kw_normalized = normalize_keyword(found_kw)
                    for target_kw in target_keywords:
                        # Exact case-insensitive match
                        if found_kw_normalized.lower() == target_kw.lower():
                            has_match = True
                            break
                        # Also check if target is a substring (e.g., "Community-based" in "Community-based Co-design")
                        if target_kw.lower() in found_kw_normalized.lower() or found_kw_normalized.lower() in target_kw.lower():
                            # But only if it's a reasonable match
                            if target_kw.lower().replace('-', ' ') in found_kw_normalized.lower().replace('-', ' ') or \
                               found_kw_normalized.lower().replace('-', ' ') in target_kw.lower().replace('-', ' '):
                                has_match = True
                                break
                    if has_match:
                        break
                
                if has_match:
                    filtered_articles.append(article)
    
    # Build output
    output = header.split("---")[0] if "---" in header else header.split("\n\n")[0]
    output = output.replace("**Total articles found:** 244", f"**Total articles found:** {len(filtered_articles)}")
    output += "\n\nThis document lists articles from TFM1.ris that contain the following specific citizen science keywords (from TFM1_Citizen_Science_Keywords.md, lines 3-11):\n"
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
    
    print(f"Strictly filtered articles: {len(filtered_articles)}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    # We need to go back to the original unfiltered list
    # Let's use the RIS file directly to extract only articles with exact keywords
    print("Extracting articles with EXACT citizen science keywords only...")
    print("This will only include articles with:")
    for kw in EXACT_TARGET_KEYWORDS:
        print(f"  - {kw}")
    print("\nRe-running extraction with strict filtering...")
    
    # Import and modify the extraction script logic
    from extract_citizen_science_articles import load_ris_file, extract_field, extract_all_keywords, extract_citizen_science_articles
    
    ris_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris"
    
    print("Loading RIS file...")
    ris_content = load_ris_file(ris_file_path)
    
    # Split content by records
    records = re.split(r'ER\s*-\s*\n', ris_content)
    
    filtered_articles = []
    
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
        
        # Search for EXACT keywords only
        found_keywords = []
        search_text = ""
        if title:
            search_text += " " + title
        if abstract:
            search_text += " " + abstract
        if keywords:
            search_text += " " + " ".join(keywords)
        
        search_text_lower = search_text.lower()
        
        # Check each EXACT keyword
        for target_kw in EXACT_TARGET_KEYWORDS:
            # Exact match with word boundaries
            pattern = r'\b' + re.escape(target_kw.lower()) + r'\.?\b'
            if re.search(pattern, search_text_lower):
                found_keywords.append(target_kw)
        
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
    
    # Format output
    from extract_citizen_science_articles import format_article_list
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_articles_list.md"
    
    formatted_output = format_article_list(filtered_articles, output_file)
    
    # Update header to mention strict filtering
    formatted_output = formatted_output.replace(
        "This document lists all articles from TFM1.ris that contain citizen science related keywords",
        "This document lists articles from TFM1.ris that contain the following EXACT citizen science keywords (from TFM1_Citizen_Science_Keywords.md, lines 3-11)"
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_output)
    
    print(f"\nStrictly filtered articles: {len(filtered_articles)}")
    print(f"Output saved to: {output_file}")

