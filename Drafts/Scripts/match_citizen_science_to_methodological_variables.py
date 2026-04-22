#!/usr/bin/env python3
"""
Match Citizen Science articles from TFM1.ris to methodological variables
and generate markdown links for Draft_Emerald_CFP_Participatory_Design_Digital_Libraries.md
"""

import re
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Tuple

# Citizen science keywords from TFM1_Citizen_Science_Keywords.md
CITIZEN_SCIENCE_KEYWORDS = [
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

# Methodological variables for Citizen Science
METHODOLOGICAL_VARIABLES = {
    'Crowdsourcing mechanisms': [
        'crowdsourcing', 'crowd-sourcing', 'crowd sourcing', 'crowd science',
        'volunteer computing', 'distributed computing', 'mass participation'
    ],
    'Community contribution models': [
        'community-based', 'community participation', 'community engagement',
        'community contribution', 'public participation', 'citizen participation',
        'participatory research', 'collaborative research'
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

def normalize_title_for_filename(title: str) -> str:
    """Normalize title to match possible filename patterns"""
    # Remove special chars, keep basic punctuation
    normalized = re.sub(r'[^\w\s\-\.\(\)]', '', title)
    # Replace multiple spaces with single space
    normalized = re.sub(r'\s+', ' ', normalized)
    return normalized.strip()

def find_clipping_file(title: str, clippings_path: Path) -> Tuple[str, bool]:
    """
    Try to find matching clipping file by title.
    Returns: (filename if found, exists_in_clippings)
    """
    normalized_title = normalize_title_for_filename(title)
    title_lower = title.lower().strip()
    
    # Try exact match first
    for md_file in clippings_path.rglob('*.md'):
        stem = md_file.stem
        if stem.lower() == title_lower or stem == normalized_title:
            return md_file.name, True
        
        # Try partial match (first 50 chars)
        if len(title) > 50:
            title_short = title[:50].lower()
            if stem.lower().startswith(title_short):
                return md_file.name, True
    
    # Not found - return filename that would be created
    safe_filename = re.sub(r'[^\w\s\-\.\(\)]', '', title)
    safe_filename = re.sub(r'\s+', ' ', safe_filename)
    safe_filename = safe_filename[:100] + '.md'  # Limit length
    return safe_filename, False

def extract_ris_record_fields(record: str) -> Dict[str, str]:
    """Extract fields from RIS record"""
    fields = {}
    
    # Extract title - handle multiple T1 lines
    titles = []
    for match in re.finditer(r'^T1\s+-\s+(.+?)(?=\n[A-Z]{2}\s+-|\n$|\nER)', record, re.MULTILINE | re.DOTALL):
        titles.append(match.group(1).strip())
    if titles:
        fields['title'] = ' '.join(titles)
    
    # Extract year
    year_match = re.search(r'^PY\s+-\s+(\d{4})', record, re.MULTILINE)
    if year_match:
        fields['year'] = year_match.group(1).strip()
    
    # Extract authors
    authors = []
    for match in re.finditer(r'^AU\s+-\s+(.+?)(?=\n[A-Z]{2}\s+-|\n$|\nER)', record, re.MULTILINE | re.DOTALL):
        authors.append(match.group(1).strip())
    if authors:
        fields['authors'] = authors  # Keep as list
    
    # Extract keywords - each KW line is one keyword
    keywords = []
    for match in re.finditer(r'^KW\s+-\s+(.+?)(?=\n[A-Z]{2}\s+-|\n$|\nER)', record, re.MULTILINE | re.DOTALL):
        kw_text = match.group(1).strip()
        # Remove quotes if present
        kw_text = kw_text.strip('"\'')
        keywords.append(kw_text)
    fields['keywords'] = keywords
    
    # Extract abstract
    abstracts = []
    for match in re.finditer(r'^AB\s+-\s+(.+?)(?=\n[A-Z]{2}\s+-|\n$|\nER)', record, re.MULTILINE | re.DOTALL):
        abstracts.append(match.group(1).strip())
    if abstracts:
        fields['abstract'] = ' '.join(abstracts)
    
    # Extract DOI
    doi_match = re.search(r'^DO\s+-\s+(.+?)(?=\n[A-Z]{2}\s+-|\n$|\nER)', record, re.MULTILINE | re.DOTALL)
    if doi_match:
        fields['doi'] = doi_match.group(1).strip()
    
    return fields

def matches_citizen_science_keywords(keywords: List[str]) -> Tuple[bool, List[str]]:
    """Check if keywords match any citizen science keywords. Returns (matches, matched_keywords)"""
    keywords_str = ' '.join([kw.lower() for kw in keywords])
    matched = []
    
    for cs_kw in CITIZEN_SCIENCE_KEYWORDS:
        # Normalize for comparison (remove trailing periods, case-insensitive)
        cs_kw_normalized = cs_kw.lower().rstrip('.')
        # Check exact matches and word boundaries
        pattern = r'\b' + re.escape(cs_kw_normalized) + r'\.?\b'
        if re.search(pattern, keywords_str, re.IGNORECASE):
            matched.append(cs_kw)
    
    return len(matched) > 0, matched

def categorize_by_methodological_variable(title: str, keywords: List[str], abstract: str = '') -> List[str]:
    """Categorize article by methodological variables based on title, keywords, and abstract"""
    text = f"{title} {' '.join(keywords)} {abstract}".lower()
    matched_variables = []
    
    for variable, search_terms in METHODOLOGICAL_VARIABLES.items():
        for term in search_terms:
            if term.lower() in text:
                matched_variables.append(variable)
                break
    
    return matched_variables

def parse_ris_file(ris_path: Path) -> List[Dict]:
    """Parse RIS file and extract articles with citizen science keywords"""
    print(f"Reading RIS file: {ris_path}")
    
    with open(ris_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into records
    records = re.split(r'\nER\s+-\s*\n', content)
    print(f"Found {len(records)} records")
    
    articles = []
    for record in records:
        if not record.strip():
            continue
        
        fields = extract_ris_record_fields(record)
        
        if not fields.get('title'):
            continue
        
        keywords = fields.get('keywords', [])
        
        # Check if matches citizen science keywords
        matches, matched_keywords = matches_citizen_science_keywords(keywords)
        if matches:
            fields['matched_cs_keywords'] = matched_keywords
            articles.append(fields)
    
    print(f"Found {len(articles)} articles with citizen science keywords")
    return articles

def generate_markdown_links(articles: List[Dict], clippings_path: Path) -> str:
    """Generate markdown with links organized by methodological variable"""
    
    # Organize articles by variable
    variable_articles = defaultdict(list)
    
    for article in articles:
        title = article.get('title', '')
        keywords = article.get('keywords', [])
        
        # Categorize article
        variables = categorize_by_methodological_variable(title, keywords)
        
        if not variables:
            # If no specific match, assign to all (broad match)
            variables = list(METHODOLOGICAL_VARIABLES.keys())
        
        for var in variables:
            variable_articles[var].append(article)
    
    # Generate markdown
    output = []
    
    for variable in METHODOLOGICAL_VARIABLES.keys():
        output.append(f"\n**{variable}:**")
        
        articles_for_var = variable_articles.get(variable, [])
        
        if not articles_for_var:
            output.append("- *No articles found*")
        else:
            # Sort by year (newest first)
            articles_for_var.sort(key=lambda x: int(x.get('year', '0')), reverse=True)
            
            for article in articles_for_var:
                title = article.get('title', '')
                year = article.get('year', '')
                
                # Find clipping file
                clipping_name, exists = find_clipping_file(title, clippings_path)
                
                # Create link
                if exists:
                    link_text = f"[[{clipping_name.replace('.md', '')}]]"
                    if year:
                        link_text += f" ({year})"
                else:
                    # Create link that will be created later
                    safe_title = title[:80]
                    link_text = f"[[Clippings/{safe_title}]]"
                    if year:
                        link_text += f" ({year})"
                    link_text += " #op/acc/download"
                
                output.append(f"- {link_text}")
    
    return '\n'.join(output)

def main():
    ris_file = Path("TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris")
    clippings_path = Path("Clippings")
    
    if not ris_file.exists():
        print(f"ERROR: RIS file not found: {ris_file}")
        return
    
    # Parse RIS file
    articles = parse_ris_file(ris_file)
    
    if not articles:
        print("No articles found with citizen science keywords")
        return
    
    # Generate markdown
    markdown_output = generate_markdown_links(articles, clippings_path)
    
    print("\n" + "="*70)
    print("MARKDOWN OUTPUT FOR CITIZEN SCIENCE VARIABLES:")
    print("="*70)
    print(markdown_output)
    
    # Save to file for review
    output_file = Path("Drafts/citizen_science_methodological_links.md")
    output_file.write_text(markdown_output, encoding='utf-8')
    print(f"\nOutput saved to: {output_file}")

if __name__ == "__main__":
    main()

