#!/usr/bin/env python3
"""
Citizen Science Keywords in Clusters Analyzer
Date of creation: 2025-01-27

This script searches for citizen science related keywords in the clusters CSV file
from the SciMAT analysis and provides detailed analysis of their distribution
across periods, clusters, and cluster types.
"""

import csv
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

def load_clusters_csv(file_path):
    """Load and parse clusters CSV file."""
    try:
        clusters_data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clusters_data.append(row)
        return clusters_data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_citizen_science_patterns():
    """Define citizen science related patterns (same as RIS analysis)."""
    
    # Define citizen science related patterns (case-insensitive)
    citizen_science_patterns = [
        # Core citizen science terms
        r'citizen science',
        r'crowdsourcing',
        r'crowd-sourcing',
        r'crowd sourcing',
        r'volunteer',
        r'participatory',
        r'community-based',
        r'public participation',
        r'public engagement',
        r'citizen scientist',
        r'citizen scientists',
        
        # Related concepts
        r'community science',
        r'community engagement',
        r'community participation',
        r'public science',
        r'volunteer monitoring',
        r'volunteer science',
        r'participatory science',
        r'participatory research',
        r'participatory monitoring',
        r'participatory observation',
        r'collaborative science',
        r'collaborative research',
        r'open science',
        r'open research',
        r'distributed research',
        r'distributed science',
        
        # Specific domains
        r'citizen journalism',
        r'citizen reporting',
        r'volunteer computing',
        r'volunteer thinking',
        r'participatory sensing',
        r'participatory mapping',
        r'participatory gis',
        r'community mapping',
        r'crowd mapping',
        r'crowdsourced data',
        r'volunteer data',
        r'community data',
        
        # Digital platforms
        r'zooniverse',
        r'foldit',
        r'galaxy zoo',
        r'inaturalist',
        r'ebird',
        r'citizen observatory',
        r'citizen observatories',
    ]
    
    return [re.compile(pattern, re.IGNORECASE) for pattern in citizen_science_patterns]

def search_keywords_in_clusters(clusters_data, patterns):
    """Search for citizen science keywords in clusters data."""
    
    keyword_matches = defaultdict(list)
    
    for i, row in enumerate(clusters_data):
        # Search in keyword field
        keyword_text = row.get('keyword', '').lower()
        cluster_name = row.get('cluster_name', '').lower()
        
        # Combine keyword and cluster name for search
        search_text = f"{keyword_text} {cluster_name}"
        
        for pattern in patterns:
            matches = pattern.findall(search_text)
            for match in matches:
                keyword_matches[match.lower()].append({
                    'row_index': i,
                    'period': row.get('period', ''),
                    'cluster_id': row.get('cluster_id', ''),
                    'cluster_name': row.get('cluster_name', ''),
                    'keyword': row.get('keyword', ''),
                    'is_center': row.get('is_center', ''),
                    'is_densest': row.get('is_densest', ''),
                    'match_type': 'keyword' if match.lower() in keyword_text else 'cluster_name'
                })
    
    return keyword_matches

def analyze_distribution(keyword_matches):
    """Analyze the distribution of citizen science keywords."""
    
    analysis = {
        'total_unique_terms': len(keyword_matches),
        'total_matches': sum(len(matches) for matches in keyword_matches.values()),
        'by_period': defaultdict(int),
        'by_cluster_type': defaultdict(int),
        'center_keywords': 0,
        'densest_keywords': 0,
        'period_cluster_distribution': defaultdict(lambda: defaultdict(int))
    }
    
    for term, matches in keyword_matches.items():
        for match in matches:
            # Count by period
            period = match['period']
            analysis['by_period'][period] += 1
            
            # Count center and densest keywords
            if match['is_center'].lower() == 'true':
                analysis['center_keywords'] += 1
            if match['is_densest'].lower() == 'true':
                analysis['densest_keywords'] += 1
            
            # Period-cluster distribution
            analysis['period_cluster_distribution'][period][match['cluster_id']] += 1
    
    return analysis

def format_clusters_output(keyword_matches, analysis):
    """Format the results into readable markdown output."""
    
    output = []
    output.append("# Citizen Science Keywords in Clusters Analysis")
    output.append(f"Date of analysis: 2025-01-27")
    output.append(f"Total unique citizen science terms found: {analysis['total_unique_terms']}")
    output.append(f"Total keyword matches: {analysis['total_matches']}")
    output.append("")
    
    # Summary statistics
    output.append("## Summary Statistics")
    output.append("")
    output.append(f"- **Total unique terms:** {analysis['total_unique_terms']}")
    output.append(f"- **Total matches:** {analysis['total_matches']}")
    output.append(f"- **Center keywords:** {analysis['center_keywords']}")
    output.append(f"- **Densest keywords:** {analysis['densest_keywords']}")
    output.append("")
    
    # Distribution by period
    output.append("## Distribution by Period")
    output.append("")
    for period, count in sorted(analysis['by_period'].items()):
        output.append(f"- **{period}:** {count} matches")
    output.append("")
    
    # Keywords by frequency
    output.append("## Keywords by Frequency")
    output.append("")
    sorted_keywords = sorted(keyword_matches.items(), key=lambda x: len(x[1]), reverse=True)
    
    for keyword, matches in sorted_keywords:
        frequency = len(matches)
        output.append(f"### {keyword} ({frequency} matches)")
        
        # Group by period
        period_groups = defaultdict(list)
        for match in matches:
            period_groups[match['period']].append(match)
        
        for period, period_matches in period_groups.items():
            output.append(f"- **{period}:** {len(period_matches)} matches")
            for match in period_matches[:5]:  # Show first 5 matches per period
                cluster_info = f"Cluster {match['cluster_id']} ({match['cluster_name']})"
                keyword_info = f"'{match['keyword']}'"
                match_type = f"[{match['match_type']}]"
                output.append(f"  - {cluster_info}: {keyword_info} {match_type}")
            
            if len(period_matches) > 5:
                output.append(f"  - ... and {len(period_matches) - 5} more matches")
            output.append("")
    
    # Period-cluster analysis
    output.append("## Period-Cluster Distribution")
    output.append("")
    for period, clusters in analysis['period_cluster_distribution'].items():
        output.append(f"### {period}")
        output.append("")
        for cluster_id, count in sorted(clusters.items()):
            output.append(f"- **Cluster {cluster_id}:** {count} matches")
        output.append("")
    
    # Alphabetical list
    output.append("## Alphabetical List of Terms")
    output.append("")
    alphabetical_keywords = sorted(keyword_matches.keys())
    for keyword in alphabetical_keywords:
        frequency = len(keyword_matches[keyword])
        output.append(f"- {keyword} ({frequency} matches)")
    
    return "\n".join(output)

def main():
    """Main function to run the citizen science clusters analyzer."""
    
    # Path to the clusters CSV file
    clusters_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/clusters_by_period_fixed_no_article.csv"
    
    print("Citizen Science Keywords in Clusters Analyzer")
    print("=" * 50)
    print(f"Date of execution: 2025-01-27")
    print(f"Analyzing file: {clusters_file_path}")
    print()
    
    # Load clusters CSV file
    print("Loading clusters CSV file...")
    clusters_data = load_clusters_csv(clusters_file_path)
    if clusters_data is None:
        sys.exit(1)
    
    print(f"File loaded successfully. Total rows: {len(clusters_data)}")
    print()
    
    # Extract patterns and search
    print("Extracting citizen science patterns and searching...")
    patterns = extract_citizen_science_patterns()
    keyword_matches = search_keywords_in_clusters(clusters_data, patterns)
    
    if not keyword_matches:
        print("No citizen science related keywords found in the clusters data.")
        return
    
    print(f"Found {len(keyword_matches)} unique citizen science related terms")
    print()
    
    # Analyze distribution
    print("Analyzing distribution...")
    analysis = analyze_distribution(keyword_matches)
    
    # Format and save results
    formatted_output = format_clusters_output(keyword_matches, analysis)
    
    # Save results to file
    output_file = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/Drafts/citizen_science_clusters_analysis.md"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"Error saving results: {e}")
    
    # Display summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total unique citizen science terms: {analysis['total_unique_terms']}")
    print(f"Total matches: {analysis['total_matches']}")
    print(f"Center keywords: {analysis['center_keywords']}")
    print(f"Densest keywords: {analysis['densest_keywords']}")
    
    print("\nDistribution by period:")
    for period, count in sorted(analysis['by_period'].items()):
        print(f"  {period}: {count} matches")
    
    # Show top 5 most frequent terms
    sorted_keywords = sorted(keyword_matches.items(), key=lambda x: len(x[1]), reverse=True)
    print("\nTop 5 most frequent terms:")
    for i, (keyword, matches) in enumerate(sorted_keywords[:5], 1):
        print(f"{i}. {keyword} ({len(matches)} matches)")
    
    print(f"\nComplete results saved to: {output_file}")

if __name__ == "__main__":
    main()




