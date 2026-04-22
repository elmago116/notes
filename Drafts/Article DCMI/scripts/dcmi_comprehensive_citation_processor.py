#!/usr/bin/env python3
"""
DCMI Comprehensive Citation Processor
Processes both Obsidian-style citations and traditional academic citations in parentheses

Date: January 27, 2025
Research Context: DCMI citation standards for semantic web and GLAM research
"""

import re
import os
import sys
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DCMIComprehensiveCitationProcessor:
    """
    DCMI comprehensive citation processor for academic papers
    """
    
    def __init__(self):
        self.citations = []
        self.bibliography = []
        self.in_text_citations = []
        
        # Obsidian-specific citation patterns
        self.OBSIDIAN_PATTERNS = {
            # [[filename.pdf#page=X&selection=Y,Z,A,B|display text]]
            'obsidian_link_with_display': r'\[\[([^|]+)\|([^\]]+)\]\]',
            # [[filename.pdf#page=X&annotation=YR]] or [[filename.pdf]]
            'obsidian_link_without_display': r'\[\[([^\]|]+)\]\]',
            # Page and annotation patterns
            'page_pattern': r'#page=(\d+)',
            'annotation_pattern': r'annotation=([^&|]+)',
            'selection_pattern': r'selection=([^&|]+)'
        }
        
        # Traditional academic citation patterns (parenthetical)
        # Capture full parentheses including possible et al., ampersand, initials, and optional question mark in year
        self.ACADEMIC_PATTERNS = [
            r'\([A-Z][A-Za-z\-]+,\s*[A-Z]\.(?:,\s*&\s*[A-Z][A-Za-z\-]+,\s*[A-Z]\.)\s*\d{4}\?\)',  # (Author, X. & Author, X. 2018?)
            r'\([A-Z][A-Za-z\-]+,\s*[A-Z]\.(?:,\s*&\s*[A-Z][A-Za-z\-]+,\s*[A-Z]\.)\s*\d{4}\)',     # (Author, X. & Author, X. 2023)
            r'\([A-Z][A-Za-z\-]+\s+et\s+al\.,\s*\d{4}\?\)',                                          # (Cobo et al., 2018?)
            r'\([A-Z][A-Za-z\-]+\s+et\s+al\.,\s*\d{4}\)',                                             # (Cobo et al., 2011)
            r'\([A-Z][A-Za-z\-]+(?:\s+[A-Z][A-Za-z\-]+)*,\s*\d{4}\?\)',                               # (Surname Surname, 2018?)
            r'\([A-Z][A-Za-z\-]+(?:\s+[A-Z][A-Za-z\-]+)*,\s*\d{4}\)'                                   # (Surname, 2019)
        ]
        
        # Comprehensive academic citation database
        self.ACADEMIC_CITATIONS = {
            'fricker_epistemic_injustice': {
                'authors': 'Fricker, M.',
                'title': 'Epistemic Injustice: Power and the Ethics of Knowing',
                'year': 2011,
                'publisher': 'Oxford University Press',
                'location': 'USA',
                'isbn': '9780191519307',
                'type': 'book',
                'doi': '',
                'url': '',
                'dcmi_compliant': True,
                'obsidian_patterns': [
                    'Epistemic Injustice _ Power and the Ethics of Knowing',
                    'Fricker, Miranda',
                    '9780191519307'
                ],
                'academic_patterns': [
                    'Fricker, 2011',
                    'Fricker, M., 2011'
                ]
            },
            'capel_brereton_human_centered_ai': {
                'authors': 'Capel, T., Brereton, M.',
                'title': 'What is Human-Centered about Human-Centered AI? A Map of the Research Landscape',
                'year': 2023,
                'journal': 'Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems',
                'type': 'conference',
                'doi': '',
                'url': '',
                'dcmi_compliant': True,
                'obsidian_patterns': [
                    'What is Human-Centered about Human-Centered AI',
                    'Proceedings of the 2023 CHI Conference'
                ],
                'academic_patterns': [
                    'Capel, T., & Brereton, M. 2023',
                    'Capel & Brereton, 2023'
                ]
            },
            'cobo_2011_science_mapping': {
                'authors': 'Cobo, M.J., López-Herrera, A.G., Herrera-Viedma, E., Herrera, F.',
                'title': 'Science mapping software tools: Review, analysis, and cooperative study among tools',
                'year': 2011,
                'journal': 'Journal of the American Society for Information Science and Technology',
                'volume': '62',
                'pages': '1382-1402',
                'type': 'journal',
                'doi': '10.1002/asi.21525',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Cobo et al., 2011'
                ]
            },
            'cobo_2012_scimat': {
                'authors': 'Cobo, M.J., López-Herrera, A.G., Herrera-Viedma, E., Herrera, F.',
                'title': 'SciMAT: A new science mapping analysis software tool',
                'year': 2012,
                'journal': 'Journal of the American Society for Information Science and Technology',
                'volume': '63',
                'pages': '1609-1630',
                'type': 'journal',
                'doi': '10.1002/asi.22688',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Cobo et al, 2012'
                ]
            },
            'cobo_2018_knowledge_based': {
                'authors': 'Cobo, M.J., Martínez, M.A., Gutiérrez-Salcedo, M., Fujita, H., Herrera-Viedma, E.',
                'title': '25 years at Knowledge-Based Systems: A bibliometric analysis',
                'year': 2018,
                'journal': 'Knowledge-Based Systems',
                'volume': '80',
                'pages': '3-13',
                'type': 'journal',
                'doi': '10.1016/j.knosys.2014.12.035',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Cobo et al., 2018?'
                ]
            },
            'codina_2023_perplexity': {
                'authors': 'Codina, L.',
                'title': 'Perplexity AI: A new paradigm for academic research assistance',
                'year': 2023,
                'journal': 'Information Research',
                'volume': '28',
                'type': 'journal',
                'doi': '',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Codina, 2023'
                ]
            },
            'lopezosa_2023_ai_search': {
                'authors': 'Lópezosa, C., Codina, L., Guerrero-Solé, F.',
                'title': 'AI-powered search strategies for systematic reviews: A comparative analysis',
                'year': 2023,
                'journal': 'Journal of Documentation',
                'volume': '79',
                'type': 'journal',
                'doi': '',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Lopezosa et al., 2023'
                ]
            },
            'snyder_2019_literature_review': {
                'authors': 'Snyder, H.',
                'title': 'Literature review as a research methodology: An overview and guidelines',
                'year': 2019,
                'journal': 'Journal of Business Research',
                'volume': '104',
                'pages': '333-339',
                'type': 'journal',
                'doi': '10.1016/j.jbusres.2019.07.039',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Snyder, 2019'
                ]
            },
            'callon_1991_co_word': {
                'authors': 'Callon, M., Courtial, J.P., Laville, F.',
                'title': 'Co-word analysis as a tool for describing the network of interactions between basic and technological research: The case of polymer chemistry',
                'year': 1991,
                'journal': 'Scientometrics',
                'volume': '22',
                'pages': '155-205',
                'type': 'journal',
                'doi': '10.1007/BF02019280',
                'dcmi_compliant': True,
                'academic_patterns': [
                    'Callon et al., 1991'
                ]
            }
        }
        
        # Research project information
        self.RESEARCH_PROJECT = {
            'name': 'HerStory&NeSyAI',
            'code': 'PID2023-147673OB-I00',
            'duration': '2023-2026',
            'institution': 'Research Institution'
        }
    
    def extract_all_citations(self, abstract_text):
        all_citations = []
        
        # Obsidian citations
        obsidian_citations = self.extract_obsidian_citations(abstract_text)
        all_citations.extend(obsidian_citations)
        
        # Academic parentheses citations
        academic_citations = self.extract_academic_citations(abstract_text)
        all_citations.extend(academic_citations)
        
        return all_citations
    
    def extract_obsidian_citations(self, abstract_text):
        citations_found = []
        
        # [[file|display]]
        for file_path, display_text in re.findall(self.OBSIDIAN_PATTERNS['obsidian_link_with_display'], abstract_text):
            citation_data = self.parse_obsidian_link(file_path, display_text)
            if citation_data:
                citations_found.append(citation_data)
        
        # [[file]] and variants without display
        for file_path in re.findall(self.OBSIDIAN_PATTERNS['obsidian_link_without_display'], abstract_text):
            if not any(c.get('raw_file_path') == file_path for c in citations_found):
                citation_data = self.parse_obsidian_link(file_path, None)
                if citation_data:
                    citations_found.append(citation_data)
        
        return citations_found
    
    def extract_academic_citations(self, abstract_text):
        citations_found = []
        for pattern in self.ACADEMIC_PATTERNS:
            for m in re.finditer(pattern, abstract_text):
                full = m.group(0)  # includes parentheses
                inner = full[1:-1]
                citation_data = self.parse_academic_citation(full, inner, pattern)
                if citation_data and not any(c['raw_text'] == full for c in citations_found):
                    citations_found.append(citation_data)
        return citations_found
    
    def parse_obsidian_link(self, file_path, display_text):
        citation_data = {
            'raw_file_path': file_path,
            'display_text': display_text,
            'file_name': self.extract_filename(file_path),
            'page_info': self.extract_page_info(file_path),
            'annotation_info': self.extract_annotation_info(file_path),
            'selection_info': self.extract_selection_info(file_path),
            'matched_academic_citation': None,
            'citation_type': 'obsidian_matched_or_raw',
            'original_type': 'obsidian',
            'raw_text': f"[[{file_path}{'|' + display_text if display_text else ''}]]"
        }
        matched_citation = self.match_with_academic_database(citation_data)
        if matched_citation:
            citation_data['matched_academic_citation'] = matched_citation
        return citation_data
    
    def parse_academic_citation(self, full_parenthetical, inner_text, pattern):
        citation_data = {
            'raw_text': full_parenthetical,  # keep parentheses for direct replacement
            'inner_text': inner_text,
            'pattern_used': pattern,
            'matched_academic_citation': None,
            'citation_type': 'academic_matched_or_raw',
            'original_type': 'academic'
        }
        matched_citation = self.match_academic_with_database(inner_text)
        if matched_citation:
            citation_data['matched_academic_citation'] = matched_citation
        return citation_data
    
    def extract_filename(self, file_path):
        clean_path = re.sub(r'#.*$', '', file_path)
        return os.path.basename(clean_path)
    
    def extract_page_info(self, file_path):
        page_match = re.search(self.OBSIDIAN_PATTERNS['page_pattern'], file_path)
        if page_match:
            return {'page_number': int(page_match.group(1)), 'has_page': True}
        return {'has_page': False}
    
    def extract_annotation_info(self, file_path):
        annotation_match = re.search(self.OBSIDIAN_PATTERNS['annotation_pattern'], file_path)
        if annotation_match:
            return {'annotation_id': annotation_match.group(1), 'has_annotation': True}
        return {'has_annotation': False}
    
    def extract_selection_info(self, file_path):
        selection_match = re.search(self.OBSIDIAN_PATTERNS['selection_pattern'], file_path)
        if selection_match:
            return {'selection_coords': selection_match.group(1), 'has_selection': True}
        return {'has_selection': False}
    
    def match_with_academic_database(self, citation_data):
        file_name = citation_data['file_name'].lower()
        display_text = citation_data['display_text'].lower() if citation_data['display_text'] else ''
        
        for _, academic_citation in self.ACADEMIC_CITATIONS.items():
            for pattern in academic_citation.get('obsidian_patterns', []):
                p = pattern.lower()
                if p in file_name or p in display_text:
                    return academic_citation
        return None
    
    def match_academic_with_database(self, citation_text):
        citation_lower = citation_text.lower()
        for _, academic_citation in self.ACADEMIC_CITATIONS.items():
            for pattern in academic_citation.get('academic_patterns', []):
                if pattern.lower() in citation_lower:
                    return academic_citation
        return None
    
    def generate_dcmi_citations(self, all_citations):
        dcmi_citations = []
        citation_counter = 1
        used_keys = set()
        for citation in all_citations:
            if citation.get('matched_academic_citation'):
                ac = citation['matched_academic_citation']
                key = f"{ac.get('authors','')}__{ac.get('title','')}__{ac.get('year','')}"
                if key in used_keys:
                    continue
                used_keys.add(key)
                dcmi_citations.append(self.format_dcmi_citation(ac, citation_counter))
                citation_counter += 1
        return dcmi_citations
    
    def format_dcmi_citation(self, ac, citation_id):
        if ac['type'] == 'journal':
            authors = ac['authors']; title = ac['title']; journal = ac['journal']; year = ac['year']
            volume = ac.get('volume',''); pages = ac.get('pages',''); doi = ac.get('doi','')
            s = f"[{citation_id}] {authors}, {title}, {journal}"
            if volume:
                s += f" {volume}"
            if pages:
                s += f" ({pages})"
            s += f" {year}"
            s += f". {doi}." if doi else "."
            return s
        if ac['type'] == 'conference':
            authors = ac['authors']; title = ac['title']; conf = ac['journal']; year = ac['year']
            doi = ac.get('doi','')
            s = f"[{citation_id}] {authors}, {title}, in: {conf}, {year}"
            s += f". {doi}." if doi else "."
            return s
        if ac['type'] == 'book':
            authors = ac['authors']; title = ac['title']; pub = ac['publisher']; loc = ac.get('location',''); year = ac['year']
            isbn = ac.get('isbn','')
            s = f"[{citation_id}] {authors}, {title}, {pub}"
            if loc:
                s += f", {loc}"
            s += f", {year}"
            s += f". ISBN: {isbn}." if isbn else "."
            return s
        # general
        authors = ac.get('authors','Unknown Author'); title = ac.get('title','Untitled'); year = ac.get('year','Unknown Year')
        return f"[{citation_id}] {authors}, {title}, {year}."
    
    def replace_all_citations_in_text(self, abstract_text, all_citations):
        processed_text = abstract_text
        # stable numbering by order of first occurrence
        numbering = {}
        next_num = 1
        used_keys = {}
        for c in all_citations:
            ac = c.get('matched_academic_citation')
            if not ac:
                continue
            key = f"{ac.get('authors','')}__{ac.get('title','')}__{ac.get('year','')}"
            if key not in numbering:
                numbering[key] = next_num
                next_num += 1
            num = numbering[key]
            pattern = re.escape(c['raw_text'])
            processed_text = re.sub(pattern, f"[{num}]", processed_text)
        return processed_text
    
    def process_comprehensive_abstract(self, file_path):
        try:
            abstract_text = Path(file_path).read_text(encoding='utf-8')
            all_citations = self.extract_all_citations(abstract_text)
            dcmi_citations = self.generate_dcmi_citations(all_citations)
            processed_abstract = self.replace_all_citations_in_text(abstract_text, all_citations)
            project_entry = f"[1] {self.RESEARCH_PROJECT['name']} Research Project, {self.RESEARCH_PROJECT['code']}, {self.RESEARCH_PROJECT['duration']}. {self.RESEARCH_PROJECT['institution']}."
            all_citations_list = [project_entry] + dcmi_citations
            
            # Counts by original_type (not mutated)
            obsidian_count = sum(1 for c in all_citations if c.get('original_type') == 'obsidian')
            academic_count = sum(1 for c in all_citations if c.get('original_type') == 'academic')
            matched_count = sum(1 for c in all_citations if c.get('matched_academic_citation'))
            
            return {
                'processed_abstract': processed_abstract,
                'bibliography': all_citations_list,
                'all_citations': all_citations,
                'dcmi_citations': dcmi_citations,
                'total_citations': len(all_citations_list),
                'obsidian_citations_count': obsidian_count,
                'academic_citations_count': academic_count,
                'matched_citations': matched_count,
                'unmatched_citations': len(all_citations) - matched_count
            }
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            return None
    
    def save_comprehensive_results(self, results, output_dir):
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        abstract_file = output_path / "dcmi_comprehensive_abstract.md"
        with open(abstract_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Abstract with All Citations Processed\n\n")
            f.write(f"**Date of Processing**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Abstract with Academic Citations\n\n")
            f.write(results['processed_abstract'])
        
        bibliography_file = output_path / "dcmi_comprehensive_bibliography.md"
        with open(bibliography_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Comprehensive Bibliography\n\n")
            f.write(f"**Date of Generation**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## References\n\n")
            for entry in results['bibliography']:
                f.write(f"{entry}\n\n")
        
        analysis_file = output_path / "dcmi_comprehensive_analysis.md"
        with open(analysis_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Comprehensive Citation Analysis\n\n")
            f.write(f"**Date of Analysis**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Summary\n\n")
            total_found = results['obsidian_citations_count'] + results['academic_citations_count']
            f.write(f"- **Total Citations Found**: {total_found}\n")
            f.write(f"- **Obsidian Citations**: {results['obsidian_citations_count']}\n")
            f.write(f"- **Academic Citations (Parentheses)**: {results['academic_citations_count']}\n")
            f.write(f"- **Matched with Academic Database**: {results['matched_citations']}\n")
            f.write(f"- **Unmatched Citations**: {results['unmatched_citations']}\n")
            f.write(f"- **Total DCMI Citations Generated**: {results['total_citations']}\n")
            match_rate = (results['matched_citations']/total_found*100) if total_found else 0.0
            f.write(f"- **Match Rate**: {match_rate:.1f}%\n\n")
            
            f.write("## Citation Details\n\n")
            for i, citation in enumerate(results['all_citations'], 1):
                f.write(f"### Citation {i}\n\n")
                f.write(f"- **Type**: {citation.get('original_type')}\n")
                f.write(f"- **Raw Text**: {citation.get('raw_text')}\n")
                if citation.get('original_type') == 'obsidian':
                    f.write(f"- **File Name**: {citation.get('file_name')}\n")
                    f.write(f"- **Display Text**: {citation.get('display_text') or 'None'}\n")
                    f.write(f"- **Page Info**: {citation.get('page_info')}\n")
                    f.write(f"- **Annotation Info**: {citation.get('annotation_info')}\n")
                    f.write(f"- **Selection Info**: {citation.get('selection_info')}\n")
                if citation.get('matched_academic_citation'):
                    f.write(f"- **Matched Academic Title**: {citation['matched_academic_citation']['title']}\n")
                else:
                    f.write(f"- **Matched Academic**: No\n")
                f.write("\n")

def main():
    processor = DCMIComprehensiveCitationProcessor()
    input_file = "../Abstract DCMI.md"
    output_dir = "../results"
    print("Processing all citations in Abstract DCMI.md...")
    results = processor.process_comprehensive_abstract(input_file)
    if results:
        processor.save_comprehensive_results(results, output_dir)
        print("Processing completed successfully!")
        total_found = results['obsidian_citations_count'] + results['academic_citations_count']
        print(f"- Total citations found: {total_found}")
        print(f"- Obsidian citations: {results['obsidian_citations_count']}")
        print(f"- Academic citations (parentheses): {results['academic_citations_count']}")
        print(f"- Matched with academic database: {results['matched_citations']}")
        print(f"- Unmatched citations: {results['unmatched_citations']}")
        print(f"- Total DCMI citations generated: {results['total_citations']}")
        match_rate = (results['matched_citations']/total_found*100) if total_found else 0.0
        print(f"- Match rate: {match_rate:.1f}%")
        print(f"\nResults saved to {output_dir}/")
        print("- dcmi_comprehensive_abstract.md")
        print("- dcmi_comprehensive_bibliography.md")
        print("- dcmi_comprehensive_analysis.md")
    else:
        print("Error processing file")

if __name__ == "__main__":
    main()
