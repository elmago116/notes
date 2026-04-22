#!/usr/bin/env python3
"""
DCMI Bibliometric Analyzer
DCMI-specific bibliometric analysis tool for semantic web and GLAM research

Date: January 27, 2025
Research Context: Integration of DCMI citation standards with existing bibliometric workflows
"""

import re
import os
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
import argparse
import json

class DCMICitationAnalyzer:
    """
    DCMI-specific citation network analysis tool
    """
    
    def __init__(self, dcmi_data):
        self.dcmi_data = dcmi_data
        self.citation_network = nx.DiGraph()
        self.author_network = nx.Graph()
        self.keyword_network = nx.Graph()
        
        # DCMI-specific field mappings
        self.DCMI_FIELD_MAPPING = {
            'TY': 'Type of reference',
            'TI': 'Title',
            'AU': 'Author',
            'PY': 'Publication Year',
            'KW': 'Keywords',
            'ER': 'End of Record',
            'DC': 'Dublin Core metadata',
            'OR': 'ORCID identifier',
            'CC': 'Creative Commons license',
            'AF': 'Author affiliation (DCMI format)',
            'EM': 'Author email',
            'CR': 'Corresponding author mark',
            'EC': 'Equal contribution mark',
            'DO': 'DOI (enhanced for DCMI)',
            'UR': 'URL (enhanced for accessibility)',
            'AC': 'Accessibility compliance',
            'SRC': 'Source database (DCMI-specific)'
        }
    
    def extract_dcmi_metadata(self):
        """Extract DCMI-specific metadata from citations"""
        metadata = {
            'authors': [],
            'affiliations': [],
            'orcid_ids': [],
            'creative_commons': [],
            'accessibility_features': [],
            'dublin_core_elements': []
        }
        
        for citation in self.dcmi_data:
            # Extract ORCID identifiers
            orcid_pattern = r'0000-\d{4}-\d{4}-\d{4}'
            orcids = re.findall(orcid_pattern, citation)
            metadata['orcid_ids'].extend(orcids)
            
            # Extract Creative Commons licenses
            cc_pattern = r'Creative Commons License Attribution'
            if re.search(cc_pattern, citation):
                metadata['creative_commons'].append(citation)
            
            # Extract accessibility features
            if 'URL:' in citation or 'alt-text' in citation:
                metadata['accessibility_features'].append(citation)
            
            # Extract Dublin Core elements
            if 'dc:' in citation or 'Dublin Core' in citation:
                metadata['dublin_core_elements'].append(citation)
        
        return metadata
    
    def extract_authors(self, citation):
        """Extract author information from DCMI citation"""
        # DCMI author format: Initials + Last name
        author_pattern = r'([A-Z]\.[A-Z]\.\s+[A-Z][a-z]+)'
        authors = re.findall(author_pattern, citation)
        return authors
    
    def extract_references(self, citation):
        """Extract reference information from DCMI citation"""
        # Extract DOIs as references
        doi_pattern = r'doi:10\.\d+/[^\s]+'
        references = re.findall(doi_pattern, citation)
        return references
    
    def validate_dcmi_format(self, citation):
        """Validate DCMI citation format compliance"""
        validation_results = {
            'author_format': False,
            'title_format': False,
            'journal_format': False,
            'doi_present': False,
            'accessibility_compliant': False,
            'dcmi_standards': False
        }
        
        # DCMI author format validation (Initials + Last name)
        author_pattern = r'[A-Z]\.[A-Z]\.\s+[A-Z][a-z]+'
        validation_results['author_format'] = bool(re.search(author_pattern, citation))
        
        # DCMI title format validation (sentence case, no quotes)
        title_pattern = r'[A-Z][a-z].*[^"]\.'
        validation_results['title_format'] = bool(re.search(title_pattern, citation))
        
        # DOI validation (required for DCMI)
        doi_pattern = r'doi:10\.\d+/[^\s]+'
        validation_results['doi_present'] = bool(re.search(doi_pattern, citation))
        
        # Accessibility compliance check
        validation_results['accessibility_compliant'] = 'URL:' in citation
        
        # Overall DCMI standards compliance
        validation_results['dcmi_standards'] = (
            validation_results['author_format'] and
            validation_results['title_format'] and
            validation_results['doi_present']
        )
        
        return validation_results
    
    def build_dcmi_citation_network(self):
        """Build citation network with DCMI-specific features"""
        for citation in self.dcmi_data:
            # Extract author information
            authors = self.extract_authors(citation)
            
            # Extract references
            references = self.extract_references(citation)
            
            # Build network with DCMI metadata
            for author in authors:
                for ref in references:
                    self.citation_network.add_edge(author, ref, 
                                                 dcmi_metadata=self.extract_dcmi_metadata())
    
    def analyze_dcmi_impact_factors(self):
        """Calculate DCMI-specific impact metrics"""
        impact_metrics = {
            'dcmi_compliance_rate': 0,
            'accessibility_score': 0,
            'metadata_completeness': 0,
            'semantic_web_integration': 0
        }
        
        total_citations = len(self.dcmi_data)
        
        if total_citations == 0:
            return impact_metrics
        
        # Calculate DCMI compliance rate
        compliant_citations = sum(1 for c in self.dcmi_data 
                                if self.validate_dcmi_format(c)['dcmi_standards'])
        impact_metrics['dcmi_compliance_rate'] = compliant_citations / total_citations
        
        # Calculate accessibility score
        accessible_citations = sum(1 for c in self.dcmi_data 
                                 if 'URL:' in c or 'alt-text' in c)
        impact_metrics['accessibility_score'] = accessible_citations / total_citations
        
        # Calculate metadata completeness
        complete_citations = sum(1 for c in self.dcmi_data 
                               if 'doi:' in c and 'URL:' in c)
        impact_metrics['metadata_completeness'] = complete_citations / total_citations
        
        # Calculate semantic web integration
        semantic_citations = sum(1 for c in self.dcmi_data 
                               if 'dc:' in c or 'Dublin Core' in c)
        impact_metrics['semantic_web_integration'] = semantic_citations / total_citations
        
        return impact_metrics

def create_dcmi_temporal_analysis(dcmi_data, time_periods):
    """
    Create DCMI-specific temporal strategic analysis
    
    Args:
        dcmi_data (list): DCMI-formatted citation data
        time_periods (list): List of time period dictionaries
    """
    
    def extract_year(citation):
        """Extract year from citation"""
        year_pattern = r'\[(\d{4})\]'
        match = re.search(year_pattern, citation)
        if match:
            return int(match.group(1))
        return None
    
    def extract_dcmi_themes(citations):
        """Extract DCMI-specific thematic elements"""
        themes = {
            'dublin_core': [],
            'semantic_web': [],
            'cultural_heritage': [],
            'participatory_design': [],
            'accessibility': [],
            'metadata_standards': []
        }
        
        for citation in citations:
            # Dublin Core themes
            if 'Dublin Core' in citation or 'dc:' in citation:
                themes['dublin_core'].append(citation)
            
            # Semantic web themes
            if 'semantic web' in citation.lower() or 'linked data' in citation.lower():
                themes['semantic_web'].append(citation)
            
            # Cultural heritage themes
            if 'GLAM' in citation or 'cultural heritage' in citation.lower():
                themes['cultural_heritage'].append(citation)
            
            # Participatory design themes
            if 'participatory' in citation.lower() or 'user-centered' in citation.lower():
                themes['participatory_design'].append(citation)
            
            # Accessibility themes
            if 'accessibility' in citation.lower() or 'screen reader' in citation.lower():
                themes['accessibility'].append(citation)
            
            # Metadata standards themes
            if 'metadata' in citation.lower() or 'standards' in citation.lower():
                themes['metadata_standards'].append(citation)
        
        return themes
    
    def calculate_dcmi_strategic_metrics(themes, time_period):
        """Calculate DCMI-specific strategic metrics"""
        metrics = {}
        
        for theme_name, theme_citations in themes.items():
            if theme_citations:
                # Calculate centrality (external connections)
                centrality = len([c for c in theme_citations 
                               if any(other_theme in c.lower() 
                                     for other_theme in themes.keys() 
                                     if other_theme != theme_name)])
                
                # Calculate density (internal connections)
                density = len([c for c in theme_citations 
                            if any(theme_name in c.lower() 
                                  for _ in theme_citations)])
                
                metrics[theme_name] = {
                    'centrality': centrality,
                    'density': density,
                    'count': len(theme_citations)
                }
        
        return metrics
    
    # Process each time period
    temporal_results = {}
    
    for period in time_periods:
        period_citations = [c for c in dcmi_data 
                          if extract_year(c) and period['start'] <= extract_year(c) <= period['end']]
        
        themes = extract_dcmi_themes(period_citations)
        metrics = calculate_dcmi_strategic_metrics(themes, period)
        
        temporal_results[period['name']] = {
            'themes': themes,
            'metrics': metrics,
            'citation_count': len(period_citations)
        }
    
    return temporal_results

def process_dcmi_ris_for_scimat(input_file, output_file):
    """
    Process DCMI-formatted RIS files for SciMAT compatibility
    
    Args:
        input_file (str): Path to DCMI RIS file
        output_file (str): Path to processed SciMAT-compatible file
    """
    # DCMI-specific field mappings
    dcmi_to_scimat_mapping = {
        'DC': 'KW',  # Dublin Core metadata as keywords
        'OR': 'AU',  # ORCID as author identifier
        'AF': 'AU',  # Affiliation as author info
        'EM': 'UR',  # Email as URL
        'CR': '',    # Remove corresponding author marks
        'EC': '',    # Remove equal contribution marks
        'CC': 'UR',  # Creative Commons as URL
        'AC': 'KW'   # Accessibility as keyword
    }
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply DCMI-specific transformations
    for dcmi_field, scimat_field in dcmi_to_scimat_mapping.items():
        if scimat_field:
            content = re.sub(f'^{dcmi_field} -', f'{scimat_field} -', content, flags=re.MULTILINE)
        else:
            content = re.sub(f'^{dcmi_field} -.*\n', '', content, flags=re.MULTILINE)
    
    # Ensure required SciMAT fields
    required_fields = ['TY', 'TI', 'PY', 'KW', 'ER']
    for field in required_fields:
        if f'{field} -' not in content:
            print(f"Warning: Missing required field {field}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def assess_dcmi_quality(citation_data):
    """
    Assess quality of DCMI-formatted citations
    
    Args:
        citation_data (list): List of DCMI citations
        
    Returns:
        dict: Quality assessment results
    """
    quality_metrics = {
        'total_citations': len(citation_data),
        'dcmi_compliant': 0,
        'accessibility_compliant': 0,
        'metadata_complete': 0,
        'semantic_web_ready': 0,
        'issues': []
    }
    
    analyzer = DCMICitationAnalyzer(citation_data)
    
    for citation in citation_data:
        # Check DCMI compliance
        validation = analyzer.validate_dcmi_format(citation)
        if validation['dcmi_standards']:
            quality_metrics['dcmi_compliant'] += 1
        else:
            quality_metrics['issues'].append(f"DCMI format issue: {citation[:50]}...")
        
        # Check accessibility compliance
        if 'URL:' in citation or 'alt-text' in citation:
            quality_metrics['accessibility_compliant'] += 1
        
        # Check metadata completeness
        required_elements = ['doi:', 'URL:']
        if all(element in citation for element in required_elements):
            quality_metrics['metadata_complete'] += 1
        
        # Check semantic web readiness
        if 'dc:' in citation or 'Dublin Core' in citation:
            quality_metrics['semantic_web_ready'] += 1
    
    # Calculate percentages
    total = quality_metrics['total_citations']
    for key in ['dcmi_compliant', 'accessibility_compliant', 'metadata_complete', 'semantic_web_ready']:
        if total > 0:
            quality_metrics[f'{key}_percentage'] = (quality_metrics[key] / total) * 100
    
    return quality_metrics

def run_dcmi_bibliometric_analysis(input_data, output_directory):
    """
    Complete DCMI bibliometric analysis workflow
    
    Args:
        input_data (str): Path to DCMI-formatted data
        output_directory (str): Output directory for results
    """
    
    print("Starting DCMI bibliometric analysis...")
    
    # Read input data
    if input_data.endswith('.ris'):
        with open(input_data, 'r', encoding='utf-8') as f:
            content = f.read()
        # Simple parsing - in practice, you'd use a proper RIS parser
        citations = content.split('\n\n')
    else:
        with open(input_data, 'r', encoding='utf-8') as f:
            citations = f.readlines()
    
    # Step 1: Initialize DCMI analyzer
    dcmi_analyzer = DCMICitationAnalyzer(citations)
    
    # Step 2: Extract DCMI metadata
    metadata = dcmi_analyzer.extract_dcmi_metadata()
    print(f"Extracted {len(metadata['orcid_ids'])} ORCID identifiers")
    
    # Step 3: Build citation networks
    dcmi_analyzer.build_dcmi_citation_network()
    print(f"Built citation network with {dcmi_analyzer.citation_network.number_of_nodes()} nodes")
    
    # Step 4: Calculate DCMI impact factors
    impact_metrics = dcmi_analyzer.analyze_dcmi_impact_factors()
    print(f"DCMI compliance rate: {impact_metrics['dcmi_compliance_rate']:.2%}")
    
    # Step 5: Create temporal analysis
    temporal_results = create_dcmi_temporal_analysis(citations, [
        {'name': '2014-2019', 'start': 2014, 'end': 2019},
        {'name': '2020-2025', 'start': 2020, 'end': 2025}
    ])
    
    # Step 6: Generate outputs
    generate_dcmi_outputs(impact_metrics, temporal_results, output_directory)
    
    print("DCMI bibliometric analysis completed successfully!")
    
    return {
        'impact_metrics': impact_metrics,
        'temporal_results': temporal_results,
        'metadata': metadata
    }

def generate_dcmi_outputs(impact_metrics, temporal_results, output_dir):
    """Generate DCMI-specific output files"""
    
    # Create impact metrics report
    with open(os.path.join(output_dir, 'dcmi_impact_report.md'), 'w') as f:
        f.write("# DCMI Impact Metrics Report\n\n")
        f.write(f"- DCMI Compliance Rate: {impact_metrics['dcmi_compliance_rate']:.2%}\n")
        f.write(f"- Accessibility Score: {impact_metrics['accessibility_score']:.2%}\n")
        f.write(f"- Metadata Completeness: {impact_metrics['metadata_completeness']:.2%}\n")
        f.write(f"- Semantic Web Integration: {impact_metrics['semantic_web_integration']:.2%}\n")
    
    # Create temporal analysis report
    with open(os.path.join(output_dir, 'dcmi_temporal_analysis.md'), 'w') as f:
        f.write("# DCMI Temporal Analysis Report\n\n")
        for period_name, period_data in temporal_results.items():
            f.write(f"## {period_name}\n\n")
            f.write(f"- Total Citations: {period_data['citation_count']}\n")
            for theme, metrics in period_data['metrics'].items():
                f.write(f"- {theme}: Centrality={metrics['centrality']}, Density={metrics['density']}\n")
            f.write("\n")
    
    # Create JSON output for programmatic access
    with open(os.path.join(output_dir, 'dcmi_analysis_results.json'), 'w') as f:
        json.dump({
            'impact_metrics': impact_metrics,
            'temporal_results': temporal_results
        }, f, indent=2)

def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description='DCMI Bibliometric Analyzer')
    parser.add_argument('--input', required=True, help='Input DCMI data file')
    parser.add_argument('--output', required=True, help='Output directory for results')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Run analysis
    results = run_dcmi_bibliometric_analysis(args.input, args.output)
    
    print(f"Analysis complete. Results saved to {args.output}")

if __name__ == "__main__":
    main()


