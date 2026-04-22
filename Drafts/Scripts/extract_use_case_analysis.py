#!/usr/bin/env python3
"""
Extract use-case analysis information from linked documents and build a table.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Base directories
BASE_DIR = Path("/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents")
CLIPPINGS_DIR = BASE_DIR / "Clippings"
DRAFTS_DIR = BASE_DIR / "Drafts"

# Use-case mapping: name -> list of link targets
USE_CASES = {
    "Yanyuwa Comic Project": ["Data Storytelling on Multi-modal Knowledge graph via data comics"],
    "World Literature Knowledge Graph": ["The World Literature Knowledge Graph"],
    "PhD Students' Information-Sharing Knowledge Graph": [
        "It answers questions that I didn't know I had\" PhD students' evaluation of an information sharing knowledge graph",
        "Community design of a knowledge graph to support interdisciplinary PhD Students"
    ],
    "Research Knowledge Graphs for Participatory Archives": [
        "Potentials of Research Knowledge Graphs for Interlinking Participatory Archives"
    ],
    "KnowEdu": ["KnowEdu_ A System to Construct Knowledge Graph for Education – DOAJ"],
    "Musical Meetups Knowledge Graph": [],  # #op/acc/download
    "Archive Dynamics Ontology (ArDO)": [],  # #op/acc/download
    "GTDOnto": ["GTDOnto- An Ontology for Organizing and Modeling Knowledge about Global Terrorism"],
    "IICONGRAPH": [],  # #op/acc/download
    "DigiNUMA": [],  # #op/acc/download
    "SAMPO Model Projects": ["hyvonen-2022-digital-humanities-on-the-semantic-web-sampo-model-and-portal-series"],
    "Wikibase for Cultural Heritage": [],  # #op/acc/download
    "Cultural Leaf Semantic Portal": ["Cultural Leaf - a LOD portal for exploring the cultural heritage"],
    "European Cultural Gems": ["Cultural gems linked open data- Mapping culture and intangible heritage in European cities"],
    "ARCA": ["Design, realization, and user evaluation of the ARCA system for exploring a digital library"],
    "InTaVia": [
        "The_Multiple_Faces_of_Cultural_Heritage_Towards_an_Integrated_Visualization_Platform_for_Tangible_and_Intangible_Cultural_Assets",
        "The InTaVia Knowledge Graph–European National Biographical and Cultural Heritage Object Data"
    ],
    "ATLAS": ["ATLAS- Towards a Knowledge Graph of International Scholarly Research on the Italian Digital Cultural Heritage"],
    "Neurosymbolic Narrative Generation for Cultural Heritage": ["Neurosymbolic Narrative Generation for Cultural Heritage"],
    "ArsEmotica": [],  # #op/acc/download
    "Participatory Indexing for Academic Digital Libraries": [
        "Participatory Indexing in the Eyes of Its Potential Users- An Example of a Co-design of Participatory Services in an Academic Digital Library"
    ],
    "ProvKOS": ["A conceptual model for tracking the provenance of activities in knowledge organization systems"],
    "Inuvialuit Digital Library": ["Community-Driven Knowledge Organization for Cultural Heritage Digital Libraries The Case of the Inuvialuit Settlement Region"],
    "HyperReal": [],  # #op/acc/download
    "Memes and Revolutionary Cultural Heritage (China)": [
        "Research on the construction of revolutionary cultural heritage knowledge graph and the application of digital cultural innovation"
    ],
    "Rhizomer": ["Rhizomer- Interactive semantic knowledge graphs exploration"]
}

# Methodological framework mappings
DESIGN_METHODS = [
    "participatory design workshop", "participatory design workshops",
    "co-design", "co-design session", "co-design sessions",
    "user testing", "interface evaluation", "usability testing",
    "user-centred design", "user-centered design", "user centered design",
    "hci evaluation", "human-computer interaction"
]

RESEARCH_METHODS = [
    "crowdsourcing", "annotation", "curation",
    "collective intelligence", "data collection", "analysis tasks",
    "participatory experiment", "participatory experiments"
]

DESIGN_PHASES = [
    "design", "development", "evaluation", "deployment", "monitoring"
]

RESEARCH_PHASES = [
    "research design", "information gathering", "field work", "analysis",
    "science communication", "knowledge transference", "impact evaluation"
]


def normalize_text(text: str) -> str:
    """Normalize text for matching."""
    return text.lower().strip()


def find_file_by_name(name: str, base_dir: Path) -> Optional[Path]:
    """Find a file by name (case-insensitive, handles variations)."""
    name_lower = normalize_text(name)
    # Try exact match first
    for file in base_dir.glob("*.md"):
        if normalize_text(file.stem) == name_lower:
            return file
    # Try partial match
    for file in base_dir.glob("*.md"):
        if name_lower in normalize_text(file.stem) or normalize_text(file.stem) in name_lower:
            return file
    return None


def extract_participants(content: str) -> str:
    """Extract participant information."""
    patterns = [
        r"participants?[:\s]+([^\.\n]+)",
        r"users?[:\s]+([^\.\n]+)",
        r"(\d+)\s+(?:participants?|users?)",
        r"(?:PhD\s+)?students?",
        r"researchers?",
        r"archivists?",
        r"language\s+teachers?",
        r"reader\s+communities?",
        r"experts?",
        r"community\s+members?",
        r"citizens?",
        r"professionals?",
        r"practitioners?",
        r"editors?",
        r"information\s+professionals?"
    ]
    
    content_lower = content.lower()
    found = []
    
    for pattern in patterns:
        matches = re.findall(pattern, content_lower, re.IGNORECASE)
        if matches:
            found.extend(matches)
    
    if found:
        # Return first meaningful match
        return found[0] if isinstance(found[0], str) else str(found[0])
    return "not explicit"


def extract_created_object(content: str, use_case_name: str) -> str:
    """Extract what was co-created."""
    patterns = [
        r"knowledge\s+graph",
        r"ontology",
        r"semantic\s+model",
        r"metadata",
        r"interface",
        r"visualization",
        r"platform",
        r"system",
        r"digital\s+library",
        r"indexing",
        r"narrative",
        r"storytelling"
    ]
    
    content_lower = content.lower()
    found = []
    
    for pattern in patterns:
        if re.search(pattern, content_lower, re.IGNORECASE):
            found.append(pattern.replace("\\s+", " ").replace("\\", ""))
    
    # Also check use case name
    if "knowledge graph" in use_case_name.lower():
        found.append("knowledge graph")
    if "ontology" in use_case_name.lower():
        found.append("ontology")
    if "digital library" in use_case_name.lower():
        found.append("digital library")
    
    if found:
        return ", ".join(set(found))
    return "not explicit"


def extract_general_method(content: str) -> str:
    """Determine if Design-led or Research-driven."""
    content_lower = content.lower()
    
    # Check for design indicators
    design_indicators = [
        "design", "development", "evaluation", "user-centered", "user-centred",
        "participatory design", "co-design", "hci", "usability"
    ]
    
    # Check for research indicators
    research_indicators = [
        "research", "citizen science", "field work", "data collection",
        "analysis", "science communication"
    ]
    
    design_count = sum(1 for ind in design_indicators if ind in content_lower)
    research_count = sum(1 for ind in research_indicators if ind in content_lower)
    
    if design_count > research_count:
        return "Design-led"
    elif research_count > design_count:
        return "Research-driven"
    else:
        return "not explicit"


def extract_method_name(content: str) -> str:
    """Extract method name from methodological tools."""
    content_lower = content.lower()
    
    # Check design methods
    for method in DESIGN_METHODS:
        if method in content_lower:
            return method.title()
    
    # Check research methods
    for method in RESEARCH_METHODS:
        if method in content_lower:
            return method.title()
    
    return "not explicit"


def extract_participation_phase(content: str) -> Tuple[str, str]:
    """Extract participation phase (early/late/constant) and phase name."""
    content_lower = content.lower()
    
    # Check for phase indicators
    early_indicators = ["early", "initial", "design", "requirements", "workshop"]
    late_indicators = ["late", "evaluation", "testing", "validation"]
    constant_indicators = ["ongoing", "continuous", "constant", "iterative", "throughout"]
    
    phase = "not explicit"
    phase_name = "not explicit"
    
    if any(ind in content_lower for ind in constant_indicators):
        phase = "constant"
        phase_name = "Development, Ongoing"
    elif any(ind in content_lower for ind in early_indicators):
        phase = "early"
        phase_name = "Design"
    elif any(ind in content_lower for ind in late_indicators):
        phase = "late"
        phase_name = "Evaluation"
    
    # Try to find specific phase names
    for design_phase in DESIGN_PHASES:
        if design_phase in content_lower:
            phase_name = design_phase.title()
            break
    
    for research_phase in RESEARCH_PHASES:
        if research_phase in content_lower:
            phase_name = research_phase.title()
            break
    
    return phase, phase_name


def extract_tools(content: str) -> str:
    """Extract tools used."""
    tools_patterns = [
        r"(neo4j|sparql|rdf|owl|wikibase|omeka|clef)",
        r"(workshop|interview|survey|focus\s+group)",
        r"(crowdsourcing|annotation|curation)",
        r"(usability\s+testing|user\s+testing)",
        r"(co-design|participatory\s+design)"
    ]
    
    content_lower = content.lower()
    found = []
    
    for pattern in tools_patterns:
        matches = re.findall(pattern, content_lower, re.IGNORECASE)
        if matches:
            found.extend([m if isinstance(m, str) else m[0] for m in matches])
    
    if found:
        return ", ".join(set(found))
    return "not explicit"


def read_file_content(file_path: Path) -> str:
    """Read file content, handling large files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read first 5000 lines to avoid memory issues
            lines = []
            for i, line in enumerate(f):
                if i >= 5000:
                    break
                lines.append(line)
            return "".join(lines)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def extract_use_case_info(use_case_name: str, link_targets: List[str]) -> Dict[str, str]:
    """Extract all information for a use case."""
    all_content = ""
    
    # Read all linked documents
    for link_target in link_targets:
        file_path = find_file_by_name(link_target, CLIPPINGS_DIR)
        if file_path and file_path.exists():
            content = read_file_content(file_path)
            all_content += "\n" + content
    
    # If no content found, return defaults
    if not all_content.strip():
        return {
            "participant": "not explicit",
            "created_object": "not explicit",
            "general_method": "not explicit",
            "method_name": "not explicit",
            "participation_phase": "not explicit",
            "phase_name": "not explicit",
            "tools": "not explicit"
        }
    
    # Extract information
    participant = extract_participants(all_content)
    created_object = extract_created_object(all_content, use_case_name)
    general_method = extract_general_method(all_content)
    method_name = extract_method_name(all_content)
    participation_phase, phase_name = extract_participation_phase(all_content)
    tools = extract_tools(all_content)
    
    return {
        "participant": participant,
        "created_object": created_object,
        "general_method": general_method,
        "method_name": method_name,
        "participation_phase": participation_phase,
        "phase_name": phase_name,
        "tools": tools
    }


def build_table() -> str:
    """Build the analysis table."""
    rows = []
    
    for use_case_name, link_targets in USE_CASES.items():
        info = extract_use_case_info(use_case_name, link_targets)
        
        row = [
            use_case_name,
            info["participant"],
            info["created_object"],
            info["general_method"],
            info["method_name"],
            info["participation_phase"],
            info["phase_name"],
            info["tools"]
        ]
        rows.append(row)
    
    # Build markdown table
    header = "| Use Case Name | Participant | Created Object | General Method | Method Name | Participation Phase | Phase Name | Tools |"
    separator = "|" + "|".join(["---"] * 8) + "|"
    
    table_lines = [header, separator]
    
    for row in rows:
        # Escape pipes in content
        escaped_row = [str(cell).replace("|", "\\|") for cell in row]
        table_lines.append("|" + "|".join(escaped_row) + "|")
    
    return "\n".join(table_lines)


def main():
    """Main function."""
    table = build_table()
    
    # Read the main document
    main_file = DRAFTS_DIR / "Borrador_Participatory_Design_Digital_Libraries.md"
    
    if not main_file.exists():
        print(f"Error: {main_file} not found")
        return
    
    with open(main_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove existing incomplete table if present
    content = re.sub(r'\n\| Use Case Name.*?\n\n', '\n', content, flags=re.DOTALL)
    
    # Append new table at the end
    new_content = content.rstrip() + "\n\n## Use-Case Analysis Table\n\n" + table + "\n"
    
    # Write back
    with open(main_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Table generated and appended to the document.")


if __name__ == "__main__":
    main()






