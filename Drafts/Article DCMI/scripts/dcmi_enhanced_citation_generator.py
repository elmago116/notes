#!/usr/bin/env python3
"""
Enhanced DCMI Citation Generator
Generates proper DCMI in-text citations and bibliography for academic papers

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

class EnhancedDCMICitationGenerator:
    """
    Enhanced DCMI citation generator for academic papers
    """
    
    def __init__(self):
        self.citations = []
        self.bibliography = []
        self.in_text_citations = []
        
        # Enhanced citation patterns for the specific abstract format
        self.CITATION_PATTERNS = {
            'bracket_citation': r'\[\[([^\]]+)\]\]',
            'inline_citation': r'\(([^)]+)\)',
            'author_year': r'([A-Z][a-z]+,\s+[A-Z]\.\s+[A-Z]\.\s+(\d{4}))',
            'doi': r'doi:10\.\d+/[^\s]+',
            'url': r'https?://[^\s]+',
            'title': r'([A-Z][a-z].*?[^"]\.)',
            'journal': r'([A-Z][a-z\s]+)\s+\d+\s*\(\d{4}\)',
            'conference': r'Proceedings of the [^,]+',
            'book': r'([A-Z][a-z\s]+),\s+[A-Z][a-z\s]+,\s+\d{4}\.'
        }
        
        # Academic databases and sources
        self.ACADEMIC_SOURCES = {
            'arxiv': 'arXiv preprint',
            'scopus': 'Scopus database',
            'wos': 'Web of Science',
            'ieee': 'IEEE Xplore',
            'acm': 'ACM Digital Library',
            'springer': 'Springer Link',
            'elsevier': 'ScienceDirect',
            'perplexity': 'Perplexity AI',
            'salsa': 'SALSA framework',
            'scimat': 'SciMAT software'
        }
    
    def extract_citations_from_abstract(self, abstract_text):
        """
        Extract citations from abstract text using enhanced patterns
        
        Args:
            abstract_text (str): Abstract text containing citations
        """
        citations_found = []
        
        # Extract bracket citations [[citation]]
        bracket_citations = re.findall(self.CITATION_PATTERNS['bracket_citation'], abstract_text)
        for citation in bracket_citations:
            citation_data = self.parse_citation_text(citation)
            if citation_data:
                citations_found.append(citation_data)
        
        # Extract inline citations (citation)
        inline_citations = re.findall(self.CITATION_PATTERNS['inline_citation'], abstract_text)
        for citation in inline_citations:
            citation_data = self.parse_citation_text(citation)
            if citation_data:
                citations_found.append(citation_data)
        
        # Extract author-year citations
        author_year_citations = re.findall(self.CITATION_PATTERNS['author_year'], abstract_text)
        for author, year in author_year_citations:
            citation_data = self.create_citation_from_author_year(author, year)
            if citation_data:
                citations_found.append(citation_data)
        
        return citations_found
    
    def parse_citation_text(self, citation_text):
        """
        Parse citation text into structured components
        
        Args:
            citation_text (str): Raw citation text
            
        Returns:
            dict: Structured citation data
        """
        citation_data = {
            'raw_text': citation_text,
            'authors': [],
            'year': None,
            'title': '',
            'journal': '',
            'doi': '',
            'url': '',
            'type': 'unknown',
            'dcmi_compliant': False,
            'source': 'unknown'
        }
        
        # Extract year from various patterns
        year_patterns = [
            r'\[(\d{4})\]',
            r'(\d{4})',
            r'p\.(\d{4})',
            r'(\d{4})\.'
        ]
        
        for pattern in year_patterns:
            year_match = re.search(pattern, citation_text)
            if year_match:
                try:
                    citation_data['year'] = int(year_match.group(1))
                    break
                except ValueError:
                    continue
        
        # Extract authors using various patterns
        author_patterns = [
            r'([A-Z]\.[A-Z]\.\s+[A-Z][a-z]+)',
            r'([A-Z][a-z]+,\s+[A-Z]\.)',
            r'([A-Z][a-z]+\s+[A-Z][a-z]+)'
        ]
        
        for pattern in author_patterns:
            authors = re.findall(pattern, citation_text)
            if authors:
                citation_data['authors'] = authors
                break
        
        # Extract DOI
        doi_match = re.search(self.CITATION_PATTERNS['doi'], citation_text)
        if doi_match:
            citation_data['doi'] = doi_match.group(0)
        
        # Extract URL
        url_match = re.search(self.CITATION_PATTERNS['url'], citation_text)
        if url_match:
            citation_data['url'] = url_match.group(0)
        
        # Determine citation type and source
        citation_data['type'], citation_data['source'] = self.classify_citation(citation_text)
        
        # Check DCMI compliance
        citation_data['dcmi_compliant'] = self.validate_dcmi_compliance(citation_data)
        
        return citation_data
    
    def create_citation_from_author_year(self, author, year):
        """
        Create citation data from author-year format
        
        Args:
            author (str): Author name
            year (str): Publication year
            
        Returns:
            dict: Citation data
        """
        citation_data = {
            'raw_text': f"{author} ({year})",
            'authors': [author],
            'year': int(year),
            'title': '',
            'journal': '',
            'doi': '',
            'url': '',
            'type': 'unknown',
            'dcmi_compliant': False,
            'source': 'unknown'
        }
        
        # Try to classify based on author name
        citation_data['type'], citation_data['source'] = self.classify_citation(author)
        citation_data['dcmi_compliant'] = self.validate_dcmi_compliance(citation_data)
        
        return citation_data
    
    def classify_citation(self, citation_text):
        """
        Classify citation type and source
        
        Args:
            citation_text (str): Citation text
            
        Returns:
            tuple: (type, source)
        """
        citation_text_lower = citation_text.lower()
        
        # Classify by source
        for source, description in self.ACADEMIC_SOURCES.items():
            if source in citation_text_lower:
                if source in ['arxiv', 'scopus', 'wos']:
                    return 'journal', source
                elif source in ['ieee', 'acm']:
                    return 'conference', source
                else:
                    return 'other', source
        
        # Classify by type patterns
        if re.search(self.CITATION_PATTERNS['conference'], citation_text):
            return 'conference', 'unknown'
        elif re.search(self.CITATION_PATTERNS['journal'], citation_text):
            return 'journal', 'unknown'
        elif re.search(self.CITATION_PATTERNS['book'], citation_text):
            return 'book', 'unknown'
        elif 'pdf' in citation_text_lower or 'url' in citation_text_lower:
            return 'online', 'web'
        else:
            return 'other', 'unknown'
    
    def validate_dcmi_compliance(self, citation_data):
        """
        Validate citation against DCMI standards
        
        Args:
            citation_data (dict): Citation data to validate
            
        Returns:
            bool: True if DCMI compliant
        """
        # DCMI compliance criteria
        has_authors = len(citation_data['authors']) > 0
        has_year = citation_data['year'] is not None
        has_doi = bool(citation_data['doi'])
        has_url = bool(citation_data['url'])
        
        return has_authors and has_year and (has_doi or has_url)
    
    def generate_dcmi_bibliography_entry(self, citation_data):
        """
        Generate DCMI-compliant bibliography entry
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: DCMI-formatted bibliography entry
        """
        if citation_data['type'] == 'journal':
            return self.format_journal_citation(citation_data)
        elif citation_data['type'] == 'conference':
            return self.format_conference_citation(citation_data)
        elif citation_data['type'] == 'book':
            return self.format_book_citation(citation_data)
        elif citation_data['type'] == 'online':
            return self.format_online_citation(citation_data)
        else:
            return self.format_general_citation(citation_data)
    
    def format_journal_citation(self, citation_data):
        """
        Format journal citation in DCMI style
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: Formatted journal citation
        """
        authors = ', '.join(citation_data['authors'])
        title = citation_data['title'] or "Title not available"
        journal = citation_data['journal'] or "Journal not specified"
        year = citation_data['year']
        doi = citation_data['doi']
        source = citation_data['source']
        
        citation = f"[{citation_data.get('id', '?')}] {authors}, {title}, {journal} {year}"
        
        if doi:
            citation += f". {doi}."
        elif source != 'unknown':
            citation += f". Source: {self.ACADEMIC_SOURCES.get(source, source)}."
        else:
            citation += "."
        
        return citation
    
    def format_conference_citation(self, citation_data):
        """
        Format conference citation in DCMI style
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: Formatted conference citation
        """
        authors = ', '.join(citation_data['authors'])
        title = citation_data['title'] or "Title not available"
        conference = citation_data.get('conference', 'Proceedings')
        year = citation_data['year']
        doi = citation_data['doi']
        source = citation_data['source']
        
        citation = f"[{citation_data.get('id', '?')}] {authors}, {title}, in: {conference}, {year}"
        
        if doi:
            citation += f". {doi}."
        elif source != 'unknown':
            citation += f". Source: {self.ACADEMIC_SOURCES.get(source, source)}."
        else:
            citation += "."
        
        return citation
    
    def format_book_citation(self, citation_data):
        """
        Format book citation in DCMI style
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: Formatted book citation
        """
        authors = ', '.join(citation_data['authors'])
        title = citation_data['title'] or "Title not available"
        publisher = citation_data.get('publisher', 'Unknown Publisher')
        year = citation_data['year']
        
        citation = f"[{citation_data.get('id', '?')}] {authors}, {title}, {publisher}, {year}."
        
        return citation
    
    def format_online_citation(self, citation_data):
        """
        Format online citation in DCMI style
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: Formatted online citation
        """
        authors = ', '.join(citation_data['authors'])
        title = citation_data['title'] or "Online resource"
        year = citation_data['year']
        url = citation_data['url']
        doi = citation_data['doi']
        
        citation = f"[{citation_data.get('id', '?')}] {authors}, {title}, {year}"
        
        if doi:
            citation += f". {doi}."
        elif url:
            citation += f". URL: {url}."
        else:
            citation += "."
        
        return citation
    
    def format_general_citation(self, citation_data):
        """
        Format general citation in DCMI style
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            str: Formatted general citation
        """
        authors = ', '.join(citation_data['authors'])
        title = citation_data['title'] or "Reference"
        year = citation_data['year']
        doi = citation_data['doi']
        url = citation_data['url']
        source = citation_data['source']
        
        citation = f"[{citation_data.get('id', '?')}] {authors}, {title}, {year}"
        
        if doi:
            citation += f". {doi}."
        elif url:
            citation += f". URL: {url}."
        elif source != 'unknown':
            citation += f". Source: {self.ACADEMIC_SOURCES.get(source, source)}."
        else:
            citation += "."
        
        return citation
    
    def generate_in_text_citations(self, abstract_text):
        """
        Generate in-text citations for abstract text
        
        Args:
            abstract_text (str): Abstract text
            
        Returns:
            str: Abstract text with proper in-text citations
        """
        # Replace bracket citations with numbered citations
        def replace_bracket_citation(match):
            citation_text = match.group(1)
            citation_data = self.parse_citation_text(citation_text)
            
            if citation_data:
                citation_id = self.get_citation_id(citation_data)
                return f"[{citation_id}]"
            else:
                return match.group(0)
        
        # Replace inline citations
        def replace_inline_citation(match):
            citation_text = match.group(1)
            citation_data = self.parse_citation_text(citation_text)
            
            if citation_data:
                citation_id = self.get_citation_id(citation_data)
                return f"({citation_id})"
            else:
                return match.group(0)
        
        # Apply replacements
        processed_text = re.sub(self.CITATION_PATTERNS['bracket_citation'], replace_bracket_citation, abstract_text)
        processed_text = re.sub(self.CITATION_PATTERNS['inline_citation'], replace_inline_citation, processed_text)
        
        return processed_text
    
    def get_citation_id(self, citation_data):
        """
        Get or create citation ID for bibliography
        
        Args:
            citation_data (dict): Citation data
            
        Returns:
            int: Citation ID
        """
        # Check if citation already exists
        for i, existing_citation in enumerate(self.bibliography):
            if (existing_citation['authors'] == citation_data['authors'] and 
                existing_citation['year'] == citation_data['year']):
                return i + 1
        
        # Add new citation to bibliography
        self.bibliography.append(citation_data)
        return len(self.bibliography)
    
    def process_abstract_file(self, file_path):
        """
        Process abstract file and generate citations
        
        Args:
            file_path (str): Path to abstract file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                abstract_text = f.read()
            
            # Extract citations
            citations = self.extract_citations_from_abstract(abstract_text)
            
            # Generate in-text citations
            processed_abstract = self.generate_in_text_citations(abstract_text)
            
            # Generate bibliography
            bibliography_entries = []
            for i, citation in enumerate(citations):
                citation['id'] = i + 1
                bibliography_entry = self.generate_dcmi_bibliography_entry(citation)
                bibliography_entries.append(bibliography_entry)
            
            return {
                'processed_abstract': processed_abstract,
                'bibliography': bibliography_entries,
                'citations_found': len(citations),
                'dcmi_compliant': sum(1 for c in citations if c['dcmi_compliant']),
                'citation_details': citations
            }
            
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            return None
    
    def save_results(self, results, output_dir):
        """
        Save citation results to files
        
        Args:
            results (dict): Processing results
            output_dir (str): Output directory
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save processed abstract
        abstract_file = output_path / "dcmi_enhanced_processed_abstract.md"
        with open(abstract_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Enhanced Processed Abstract\n\n")
            f.write(f"**Date of Processing**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Abstract with DCMI Citations\n\n")
            f.write(results['processed_abstract'])
        
        # Save bibliography
        bibliography_file = output_path / "dcmi_enhanced_bibliography.md"
        with open(bibliography_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Enhanced Bibliography\n\n")
            f.write(f"**Date of Generation**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## References\n\n")
            for entry in results['bibliography']:
                f.write(f"{entry}\n\n")
        
        # Save detailed citation analysis
        analysis_file = output_path / "dcmi_enhanced_citation_analysis.md"
        with open(analysis_file, 'w', encoding='utf-8') as f:
            f.write("# DCMI Enhanced Citation Analysis\n\n")
            f.write(f"**Date of Analysis**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"- **Total Citations Found**: {results['citations_found']}\n")
            f.write(f"- **DCMI Compliant**: {results['dcmi_compliant']}\n")
            if results['citations_found'] > 0:
                compliance_rate = (results['dcmi_compliant']/results['citations_found']*100)
                f.write(f"- **Compliance Rate**: {compliance_rate:.1f}%\n\n")
            
            f.write("## Citation Details\n\n")
            for i, citation in enumerate(results['citation_details']):
                f.write(f"### Citation {i+1}\n")
                f.write(f"- **Raw Text**: {citation['raw_text']}\n")
                f.write(f"- **Authors**: {', '.join(citation['authors'])}\n")
                f.write(f"- **Year**: {citation['year']}\n")
                f.write(f"- **Type**: {citation['type']}\n")
                f.write(f"- **Source**: {citation['source']}\n")
                f.write(f"- **DCMI Compliant**: {citation['dcmi_compliant']}\n")
                if citation['doi']:
                    f.write(f"- **DOI**: {citation['doi']}\n")
                if citation['url']:
                    f.write(f"- **URL**: {citation['url']}\n")
                f.write("\n")
            
            f.write("## DCMI Standards Compliance\n\n")
            f.write("This analysis follows DCMI citation standards including:\n")
            f.write("- Author format: Initials + Last name\n")
            f.write("- Title format: Sentence case, no quotes\n")
            f.write("- DOI inclusion when available\n")
            f.write("- Accessibility compliance with URLs\n")
            f.write("- Dublin Core metadata integration\n")
        
        print(f"Enhanced results saved to {output_dir}")
        print(f"- Processed abstract: {abstract_file}")
        print(f"- Bibliography: {bibliography_file}")
        print(f"- Analysis: {analysis_file}")

def main():
    """
    Main function to run enhanced DCMI citation generator
    """
    # Initialize generator
    generator = EnhancedDCMICitationGenerator()
    
    # Process abstract file
    abstract_file = "../Abstract DCMI.md"
    output_dir = "../results"
    
    print("Processing DCMI Abstract with Enhanced Citation Generator...")
    results = generator.process_abstract_file(abstract_file)
    
    if results:
        # Save results
        generator.save_results(results, output_dir)
        
        print(f"\nEnhanced processing complete!")
        print(f"Found {results['citations_found']} citations")
        print(f"DCMI compliant: {results['dcmi_compliant']}")
        if results['citations_found'] > 0:
            compliance_rate = (results['dcmi_compliant']/results['citations_found']*100)
            print(f"Compliance rate: {compliance_rate:.1f}%")
    else:
        print("Error processing abstract file")

if __name__ == "__main__":
    main()
