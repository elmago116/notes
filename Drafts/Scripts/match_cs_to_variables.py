#!/usr/bin/env python3
"""
Match Citizen Science articles to methodological variables and generate markdown links
Reuses extraction logic from extract_exact_citizen_science_articles.py
"""

import re
from pathlib import Path
from collections import defaultdict

# Reuse the exact keywords from the existing script
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

METHODOLOGICAL_VARIABLES = {
    'Crowdsourcing mechanisms': [
        'crowdsourcing', 'crowd-sourcing', 'crowd sourcing', 'crowd science',
        'volunteer computing', 'distributed computing', 'mass participation',
        'citizen science'  # Add this as it's a key term
    ],
    'Community contribution models': [
        'community-based', 'community participation', 'community engagement',
        'community contribution', 'public participation', 'citizen participation',
        'participatory research', 'collaborative research', 'community-based participatory research'
    ],
    'Quality control and validation processes': [
        'quality control', 'validation', 'verification', 'peer review',
        'data quality', 'accuracy', 'reliability', 'expert review'
    ],
    'Recognition and motivation strategies - engagement': [
        'motivation', 'engagement', 'recognition', 'incentives', 'gamification',
        'rewards', 'acknowledgment', 'credit', 'participation'
    ]
}

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
        keywords.append(match.group(1).strip().strip('"\''))
    return keywords

def find_exact_keyword_matches(search_text, exact_keywords):
    """Find which exact keywords appear in the search text."""
    found = []
    search_text_lower = search_text.lower()
    
    for keyword in exact_keywords:
        keyword_lower = keyword.lower().rstrip('.')
        pattern = r'\b' + re.escape(keyword_lower) + r'\.?\b'
        if re.search(pattern, search_text_lower):
            found.append(keyword)
    
    return found

def find_clipping_file(title: str, clippings_path: Path) -> tuple:
    """Find matching clipping file. Returns (filename, exists)"""
    title_lower = title.lower().strip()
    
    for md_file in clippings_path.rglob('*.md'):
        stem = md_file.stem.lower()
        # Try various matching strategies
        if stem == title_lower:
            return md_file.name, True
        # Partial match
        if len(title) > 30:
            title_short = title[:50].lower()
            if stem.startswith(title_short) or title_short in stem:
                return md_file.name, True
    
    # Not found - create safe filename
    safe = re.sub(r'[^\w\s\-\.\(\)]', '', title)[:80] + '.md'
    return safe, False

def categorize_article(title: str, keywords: list, abstract: str = '') -> list:
    """Categorize article by methodological variables"""
    text = f"{title} {' '.join(keywords)} {abstract}".lower()
    matched = []
    
    for variable, search_terms in METHODOLOGICAL_VARIABLES.items():
        for term in search_terms:
            if term.lower() in text:
                matched.append(variable)
                break
    
    return matched if matched else list(METHODOLOGICAL_VARIABLES.keys())  # Default to all if no match

def main():
    ris_file_path = Path("TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris")
    clippings_path = Path("Clippings")
    
    print("Matching Citizen Science articles to methodological variables...")
    print("=" * 70)
    
    ris_content = load_ris_file(ris_file_path)
    if ris_content is None:
        return
    
    records = re.split(r'ER\s*-\s*\n', ris_content)
    print(f"Found {len(records)} records in RIS file")
    
    articles = []
    variable_articles = defaultdict(list)
    
    for record in records:
        if not record.strip():
            continue
        
        keywords = extract_all_keywords(record)
        keywords_text = ' '.join(keywords)
        
        # Check for exact keyword matches
        matched_keywords = find_exact_keyword_matches(keywords_text, EXACT_KEYWORDS)
        
        if matched_keywords:
            title = extract_field(record, 'T1') or extract_field(record, 'TI') or 'No title'
            year = extract_field(record, 'PY') or ''
            authors = []
            for au_match in re.finditer(r'^AU\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.MULTILINE | re.DOTALL | re.IGNORECASE):
                authors.append(au_match.group(1).strip())
            abstract = extract_field(record, 'AB') or ''
            
            article = {
                'title': title,
                'year': year,
                'authors': authors[:3],
                'keywords': keywords,
                'matched_cs_keywords': matched_keywords,
                'abstract': abstract
            }
            
            articles.append(article)
            
            # Categorize by variable
            variables = categorize_article(title, keywords, abstract)
            for var in variables:
                variable_articles[var].append(article)
    
    print(f"\nFound {len(articles)} articles with citizen science keywords")
    
    # Generate markdown output
    output_lines = []
    
    for variable in METHODOLOGICAL_VARIABLES.keys():
        output_lines.append(f"\n**{variable}:**")
        
        articles_for_var = variable_articles.get(variable, [])
        
        if not articles_for_var:
            output_lines.append("- *No articles found*")
        else:
            # Sort by year (newest first)
            articles_for_var.sort(key=lambda x: int(x.get('year', '0') or '0'), reverse=True)
            
            for article in articles_for_var:
                title = article['title']
                year = article['year']
                
                clipping_name, exists = find_clipping_file(title, clippings_path)
                
                if exists:
                    link = f"[[{clipping_name.replace('.md', '')}]]"
                    if year:
                        link += f" ({year})"
                else:
                    safe_title = re.sub(r'[^\w\s\-\.\(\)]', '', title)[:80]
                    link = f"[[Clippings/{safe_title}]]"
                    if year:
                        link += f" ({year})"
                    link += " #op/acc/download"
                
                output_lines.append(f"- {link}")
    
    markdown_output = '\n'.join(output_lines)
    
    print("\n" + "="*70)
    print("MARKDOWN OUTPUT:")
    print("="*70)
    print(markdown_output)
    
    # Save to file
    output_file = Path("Drafts/citizen_science_methodological_links.md")
    output_file.write_text(markdown_output, encoding='utf-8')
    print(f"\nOutput saved to: {output_file}")

if __name__ == "__main__":
    main()



