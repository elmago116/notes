#!/usr/bin/env python3
"""
Match Participatory Design articles from TFM1.ris to methodological variables
and generate markdown links for Draft_Emerald_CFP_Participatory_Design_Digital_Libraries.md
"""

import re
from pathlib import Path
from collections import defaultdict

# Participatory Design keywords from TFM1_Citizen_Science_Keywords.md
PARTICIPATORY_DESIGN_KEYWORDS = [
    'participatory design',
    'participatory design methods',
    'Co-participatory design',
    'participatory planning',
    'Participatory design approach',
    'user-centered design',
    'user-centered design methodology',
    'Iterative user-centered design',
    'user-centred design',
]

# Methodological variables for Participatory Design
METHODOLOGICAL_VARIABLES = {
    'Level of user participation (inform, consult, involve, collaborate, empower)': [
        'inform', 'consult', 'involve', 'collaborate', 'empower', 'participation level',
        'user participation', 'stakeholder participation', 'engagement level',
        'ladder of participation', 'participation spectrum'
    ],
    'Stakeholder diversity and representation': [
        'stakeholder', 'diversity', 'representation', 'marginalized', 'minority',
        'community', 'inclusive', 'equity', 'underrepresented', 'marginalised',
        'indigenous', 'vulnerable groups'
    ],
    'Design process structure and phases': [
        'design process', 'design phase', 'design stage', 'process structure',
        'iterative design', 'design methodology', 'design framework',
        'co-design process', 'collaborative design process'
    ],
    'Methods used (workshops, interviews, prototyping, etc.)': [
        'workshop', 'interview', 'prototyping', 'prototype', 'focus group',
        'design session', 'co-design session', 'participatory workshop',
        'design method', 'methodology', 'technique'
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
    
    print("Matching Participatory Design articles to methodological variables...")
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
        
        # Extract fields
        title = extract_field(record, 'TI') or extract_field(record, 'T1') or ''
        if not title:
            continue
            
        year = extract_field(record, 'PY') or ''
        keywords = extract_all_keywords(record)
        abstract = extract_field(record, 'AB') or ''
        
        # Build search text
        search_text = f"{title} {' '.join(keywords)} {abstract}"
        
        # Check for participatory design keyword matches
        matched_keywords = find_exact_keyword_matches(search_text, PARTICIPATORY_DESIGN_KEYWORDS)
        
        if matched_keywords:
            article = {
                'title': title,
                'year': year,
                'keywords': keywords,
                'matched_pd_keywords': matched_keywords,
                'abstract': abstract[:500]  # First 500 chars
            }
            
            articles.append(article)
            
            # Categorize by variable
            variables = categorize_article(title, keywords, abstract)
            for var in variables:
                variable_articles[var].append(article)
    
    print(f"\nFound {len(articles)} articles with participatory design keywords")
    
    # Generate markdown output
    output_lines = []
    
    for variable in METHODOLOGICAL_VARIABLES.keys():
        output_lines.append(f"\n**{variable}:**")
        
        articles_for_var = variable_articles.get(variable, [])
        
        if not articles_for_var:
            output_lines.append("  - *No articles found*")
        else:
            # Sort by year (newest first), remove duplicates by title
            seen_titles = set()
            unique_articles = []
            for article in articles_for_var:
                if article['title'] not in seen_titles:
                    seen_titles.add(article['title'])
                    unique_articles.append(article)
            
            unique_articles.sort(key=lambda x: int(x.get('year', '0') or '0'), reverse=True)
            
            for article in unique_articles:
                title = article['title']
                year = article['year']
                
                clipping_name, exists = find_clipping_file(title, clippings_path)
                
                # Create safe link name
                safe_title = re.sub(r'[^\w\s\-\.\(\)]', '', title)[:80]
                
                if exists:
                    link = f"[[{clipping_name.replace('.md', '')}]]"
                    if year:
                        link += f" ({year})"
                else:
                    link = f"[[Clippings/{safe_title}]]"
                    if year:
                        link += f" ({year})"
                    link += " #op/acc/download"
                
                output_lines.append(f"  - {link}")
    
    markdown_output = '\n'.join(output_lines)
    
    print("\n" + "="*70)
    print("MARKDOWN OUTPUT:")
    print("="*70)
    print(markdown_output)
    
    # Save to file
    output_file = Path("Drafts/participatory_design_methodological_links.md")
    output_file.write_text(markdown_output, encoding='utf-8')
    print(f"\nOutput saved to: {output_file}")

if __name__ == "__main__":
    main()



