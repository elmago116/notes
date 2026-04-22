#!/usr/bin/env python3
"""
Generate Emerald Harvard-style references from clipping files
"""

import re
from pathlib import Path
from collections import OrderedDict

def parse_yaml_simple(content):
    """Simple YAML parser for frontmatter"""
    metadata = {}
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return metadata
    
    yaml_content = yaml_match.group(1)
    for line in yaml_content.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            try:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                
                # Handle lists
                if value.startswith('['):
                    # Extract list items
                    items = []
                    current_item = ""
                    in_quotes = False
                    for char in value[1:-1]:  # Remove brackets
                        if char == '"' or char == "'":
                            in_quotes = not in_quotes
                        elif char == ',' and not in_quotes:
                            if current_item.strip():
                                items.append(current_item.strip().strip('"').strip("'"))
                            current_item = ""
                        else:
                            current_item += char
                    if current_item.strip():
                        items.append(current_item.strip().strip('"').strip("'"))
                    metadata[key] = items if items else [value]
                else:
                    metadata[key] = value
            except:
                pass
    
    return metadata

def format_author_emerald(authors_list, is_et_al=False):
    """Format authors in Emerald style: Surname, Initials"""
    if not authors_list:
        return None
    
    if isinstance(authors_list, str):
        authors_list = [authors_list]
    
    formatted = []
    for author in authors_list:
        # Handle different formats
        author = str(author).strip()
        if not author:
            continue
            
        # Remove wikilink markers
        author = re.sub(r'\[\[.*?\]\]', '', author).strip()
        
        # Parse "Surname, Initials" or "Initials Surname"
        if ',' in author:
            parts = [p.strip() for p in author.split(',', 1)]
            formatted.append(f"{parts[0]}, {parts[1]}")
        else:
            # Try to parse "First Last" or "First Middle Last"
            parts = author.split()
            if len(parts) >= 2:
                surname = parts[-1]
                initials = '. '.join([p[0].upper() for p in parts[:-1]]) + '.'
                formatted.append(f"{surname}, {initials}")
            else:
                formatted.append(author)
    
    if is_et_al and len(formatted) > 2:
        return f"{formatted[0]} *et al.*"
    elif len(formatted) == 2:
        return f"{formatted[0]} and {formatted[1]}"
    elif len(formatted) == 1:
        return formatted[0]
    else:
        return ', '.join(formatted[:-1]) + f" and {formatted[-1]}"

def format_emerald_journal(authors, year, title, journal, volume=None, issue=None, pages=None, doi=None):
    """Format journal article in Emerald Harvard style"""
    author_str = authors if isinstance(authors, str) else format_author_emerald(authors)
    ref = f"{author_str} ({year}), \"{title}\""
    
    if journal:
        ref += f", *{journal}*"
    if volume:
        if issue:
            ref += f", Vol. {volume} No. {issue}"
        else:
            ref += f", Vol. {volume}"
    if pages:
        if '-' in str(pages):
            ref += f", pp.{pages}"
        else:
            ref += f", p.{pages}"
    
    if doi:
        ref += f". https://doi.org/{doi.replace('https://doi.org/', '').replace('doi:', '')}"
    
    return ref

def format_emerald_book(authors, year, title, publisher, place=None, doi=None):
    """Format book in Emerald Harvard style"""
    author_str = authors if isinstance(authors, str) else format_author_emerald(authors)
    ref = f"{author_str} ({year}), *{title}*"
    
    if publisher:
        ref += f", {publisher}"
    if place:
        ref += f", {place}"
    
    if doi:
        ref += f". https://doi.org/{doi.replace('https://doi.org/', '').replace('doi:', '')}"
    
    return ref

def format_emerald_chapter(authors, year, title, editor, book_title, publisher, place=None, pages=None, doi=None):
    """Format book chapter in Emerald Harvard style"""
    author_str = authors if isinstance(authors, str) else format_author_emerald(authors)
    ref = f"{author_str} ({year}), \"{title}\""
    
    if editor:
        editor_str = format_author_emerald([editor]) if isinstance(editor, str) else format_author_emerald(editor)
        ref += f", {editor_str} (Ed.)"
    
    if book_title:
        ref += f", *{book_title}*"
    if publisher:
        ref += f", {publisher}"
    if place:
        ref += f", {place}"
    if pages:
        ref += f", pp.{pages}"
    
    if doi:
        ref += f". https://doi.org/{doi.replace('https://doi.org/', '').replace('doi:', '')}"
    
    return ref

def format_emerald_conference(authors, year, title, editors, proceedings_title, publisher, place=None, pages=None, doi=None):
    """Format conference proceedings in Emerald Harvard style"""
    author_str = authors if isinstance(authors, str) else format_author_emerald(authors)
    ref = f"{author_str} ({year}), \"{title}\""
    
    if editors:
        if isinstance(editors, list) and len(editors) > 1:
            editor_str = ', '.join([format_author_emerald([e]) if isinstance(e, str) else format_author_emerald(e) for e in editors[:-1]])
            editor_str += f" and {format_author_emerald([editors[-1]]) if isinstance(editors[-1], str) else format_author_emerald(editors[-1])}"
            ref += f", in {editor_str} (Ed.s)"
        else:
            editor = editors[0] if isinstance(editors, list) else editors
            editor_str = format_author_emerald([editor]) if isinstance(editor, str) else format_author_emerald(editor)
            ref += f", in {editor_str} (Ed.)"
    
    if proceedings_title:
        ref += f", *{proceedings_title}*"
    if publisher:
        ref += f", {publisher}"
    if place:
        ref += f", {place}"
    if pages:
        ref += f", pp.{pages}"
    
    if doi:
        ref += f". https://doi.org/{doi.replace('https://doi.org/', '').replace('doi:', '')}"
    
    return ref

# Citation mapping - from document links to clipping files
citation_map = {
    "Almeida et al., 2024": {
        "file": "Remixing and repurposing cultural heritage archives through a collaborative and AI-generated storytelling digital platform.md",
        "search": "Remixing and repurposing"
    },
    "Calvano, 2024": {
        "file": "Design and evaluation of high-quality simbolic AI systems.md",
        "search": "Design and evaluation"
    },
    "Calvano, 2025": {
        "file": "Techniques and Methods to Evaluate Human-Centered Symbiotic AI Systems.md",
        "search": "Techniques and Methods"
    },
    "Capel and Brereton, 2023": {
        "file": "What is Human-Centered about Human-Centered AI_ A Map of the Research Landscape _ Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.md",
        "search": "What is Human-Centered"
    },
    "Cardoso et al., 2021": {
        "file": "Literature Reviews Modern Methods for Investigating Scientific and Technological Knowledge.md",
        "search": "Literature Reviews Modern Methods"
    },
    "Cobo et al., 2011": {
        "file": "Science mapping software tools_ Review, analysis, and cooperative study among tools.md",
        "search": "Science mapping software tools"
    },
    "Codina, 2023": {
        "file": "Codina-Buscadores-alternativos - perplexity.md",
        "search": "Codina-Buscadores"
    },
    "Davis and Horst, 2016": {
        "file": "Science Communication Culture, Identity and Citizenship.md",
        "search": "Science Communication Culture"
    },
    "Delgado et al., 2023": {
        "file": "The Participatory Turn in AI Design Theoretical Foundations and the Current State of Practice.md",
        "search": "Participatory Turn in AI Design"
    },
    "Escobar, 2016": {
        "file": "Autonomía y diseño - La realización de lo comunal.md",
        "search": "Autonomía y diseño"
    },
    "Farnel and Shiri, 2019": {
        "file": "Community-Driven Knowledge Organization for Cultural Heritage Digital Libraries The Case of the Inuvialuit Settlement Region.md",
        "search": "Community-Driven Knowledge Organization"
    },
    "Fox and Chandrasekar, 2021": {
        "file": "How Should One Explore the Digital Library of the Future?.md",
        "search": "How Should One Explore"
    },
    "Fricker, 2007": {
        "file": "Epistemic Injustice _ Power and the Ethics of Knowing -- Fricker, Miranda(Author) -- Repr, 2011 -- Oxford University Press, USA.md",
        "search": "Epistemic Injustice"
    },
    "García-Zarza et al., 2022": {
        "file": "Towards a Teacher Application to Support Semantic Annotations of Learning Tasks in Cultural Heritage.md",
        "search": "Towards a Teacher Application"
    },
    "Garoufallou et al., 2021": {
        "file": "Metadata and Semantic Research - Conference.md",
        "search": "Metadata and Semantic Research"
    },
    "Gómez-Ferri, 2014": {
        "file": "Ciència Ciutadana o Ciutadanies Científiques? Quatre Models de Participació en Ciència i Tecnologia.md",
        "search": "Ciència Ciutadana"
    },
    "Gardasevic and Lamba, 2024": {
        "file": "It answers questions that I didn't know I had\" PhD students' evaluation of an information sharing knowledge graph.md",
        "search": "It answers questions"
    },
    "Haklay et al., 2020": {
        "file": "ecsa_characteristics_of_citizen_science_explanation_notes_-_v1_final.md",
        "search": "ecsa_characteristics"
    },
    "Haraway, 1991": {
        "file": "Ciencia, cyborgs y mujeres - la reinvención de la naturaleza.md",
        "search": "Ciencia, cyborgs y mujeres"
    },
    "Leblanc, 2020": {
        "file": "Participatory Indexing in the Eyes of Its Potential Users- An Example of a Co-design of Participatory Services in an Academic Digital Library.md",
        "search": "Participatory Indexing"
    },
    "Liu, 2025": {
        "file": "Human_AI_Co_Creation_A_Framework_for_Collaborative_Design_in_Intelligent_Systems.md",
        "search": "Human_AI_Co_Creation"
    },
    "Lopezosa et al., 2024": {
        "file": "ChatGPT como apoyo a las systematic scoping reviews- integrando la inteligencia artificial con el framework SALSA.md",
        "search": "ChatGPT como apoyo"
    },
    "Mahdie et al., 2024": {
        "file": "Usability Testing  A Bibliometric Analysis Based on WoS Data – Journal of Scientometric Research.md",
        "search": "Usability Testing"
    },
    "Matt, 2015": {
        "file": "White Paper on Citizen Science for Europe.md",
        "search": "White Paper on Citizen Science"
    },
    "Nesterov et al., 2023": {
        "file": "A Knowledge Graph of Contentious Terminology for Inclusive Representation of Cultural Heritage.md",
        "search": "Knowledge Graph of Contentious Terminology"
    },
    "Ranjgar et al., 2024": {
        "file": "Cultural_Heritage_Information_Retrieval_Past_Present_and_Future_Trends.md",
        "search": "Cultural_Heritage_Information_Retrieval"
    },
    "Shneiderman, 2021": {
        "file": "Human-Centered AI  A New Synthesis   Human-Computer Interaction – INTERACT 2021.md",
        "search": "Human-Centered AI"
    },
    "Stappers and Sanders, 2008": {
        "file": "Co-creation and the new landscapes of design.md",
        "search": "Co-creation and the new landscapes"
    },
    "Stengers and Despret, 2014": {
        "file": "Women Who Make a Fuss  The Unfaithful Daughters of Virginia Woolf on JSTOR.md",
        "search": "Women Who Make a Fuss"
    },
    "Turnhout et al., 2020": {
        "file": "The politics of co-production participation, power, and transformation.md",
        "search": "politics of co-production"
    },
    "Vohland et al., 2021": {
        "file": "The Science of Citizen Science.md",
        "search": "Science of Citizen Science"
    },
    "Wacnik et al., 2025": {
        "file": "Participatory_design_A_systematic_review_and_insights_for_future_practice.md",
        "search": "Participatory_design_A_systematic_review"
    },
    "Waidelich et al., 2018": {
        "file": "Design Thinking Process Model Review.md",
        "search": "Design Thinking Process Model"
    },
    "Wang et al., 2024": {
        "file": "Digital Humanities & Large Language Models Practice and Research in Semantic Retrieval of Ancient Documents.md",
        "search": "Digital Humanities"
    },
}

clippings_path = Path(__file__).parent.parent.parent / "Clippings"
references = []
missing_info = []

for citation_key, info in citation_map.items():
    file_path = clippings_path / info["file"]
    
    if not file_path.exists():
        # Try to find by search term
        found = False
        for f in clippings_path.glob("*.md"):
            if info["search"].lower() in f.stem.lower():
                file_path = f
                found = True
                break
        
        if not found:
            missing_info.append((citation_key, f"File not found: {info['file']}"))
            continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = parse_yaml_simple(content)
        
        authors = metadata.get('authors', metadata.get('author', []))
        year = metadata.get('year', '').strip('"').strip("'")
        title = metadata.get('title', '').strip('"').strip("'")
        journal = metadata.get('journal', '').strip('"').strip("'")
        type_doc = metadata.get('type', metadata.get('Type', '')).strip('"').strip("'")
        publisher = metadata.get('publisher', '').strip('"').strip("'")
        volume = metadata.get('volume', '').strip('"').strip("'")
        issue = metadata.get('issue', '').strip('"').strip("'")
        pages = metadata.get('pages', '').strip('"').strip("'")
        doi = metadata.get('doi', metadata.get('DOI', '')).strip('"').strip("'")
        
        # Check if we have minimum info
        if not authors or not year or not title:
            missing_info.append((citation_key, f"Missing required fields: authors={bool(authors)}, year={bool(year)}, title={bool(title)}"))
            continue
        
        # Determine document type and format
        is_et_al = 'et al' in citation_key.lower()
        
        if 'journal' in type_doc.lower() or journal:
            ref = format_emerald_journal(authors, year, title, journal, volume, issue, pages, doi)
        elif 'book' in type_doc.lower() or (publisher and not journal):
            ref = format_emerald_book(authors, year, title, publisher, doi=doi)
        elif 'conference' in type_doc.lower() or 'proceeding' in type_doc.lower():
            # For conference, we need editor info
            editors = metadata.get('editors', [])
            ref = format_emerald_conference(authors, year, title, editors, journal or title, publisher, pages=pages, doi=doi)
        elif 'chapter' in type_doc.lower():
            editor = metadata.get('editor', '')
            book_title = metadata.get('book_title', title)
            ref = format_emerald_chapter(authors, year, title, editor, book_title, publisher, pages=pages, doi=doi)
        else:
            # Default to journal if journal field exists, else book
            if journal:
                ref = format_emerald_journal(authors, year, title, journal, volume, issue, pages, doi)
            else:
                ref = format_emerald_book(authors, year, title, publisher, doi=doi)
        
        # Extract first author surname for sorting
        first_author = authors[0] if isinstance(authors, list) else authors
        first_author = str(first_author).strip()
        if ',' in first_author:
            surname = first_author.split(',')[0].strip()
        else:
            surname = first_author.split()[-1].strip() if ' ' in first_author else first_author
        
        references.append({
            'citation_key': citation_key,
            'surname': surname,
            'year': year,
            'reference': ref,
            'metadata': metadata
        })
    
    except Exception as e:
        missing_info.append((citation_key, f"Error processing: {str(e)}"))

# Sort by surname, then year
references.sort(key=lambda x: (x['surname'].lower(), x['year']))

# Output
print("# References\n")
for ref in references:
    print(ref['reference'])

if missing_info:
    print("\n\n## Citations requiring manual review:\n")
    for key, reason in missing_info:
        print(f"- {key}: {reason}")

