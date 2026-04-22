#!/usr/bin/env python3
"""
Count Articles per Citizen Science Cluster
Date of creation: 2025-01-27

This script counts the actual number of articles from the RIS file that contain
the citizen science keywords found in each cluster.
"""

import re
import sys
from collections import defaultdict

def load_ris_file(file_path):
    """Load and parse RIS file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def extract_cluster_specific_keywords():
    """Define the specific citizen science keywords found in each cluster."""
    
    # Based on our clusters analysis
    cluster_keywords = {
        '2014-2019_11_digital_storytelling': [
            'participatory approach',
            'crowdsourcing'
        ],
        '2014-2019_7_value_co_creation': [
            'community participation'
        ],
        '2020-2025_3_hiv': [
            'participatory design methods'
        ],
        '2020-2025_4_ethical_community_research': [
            'community-based participatory research',
            'community-based',
            'participatory research'
        ],
        '2020-2025_5_participation': [
            'community-based tourism'
        ]
    }
    
    return cluster_keywords

def count_articles_with_cluster_keywords(ris_content, cluster_keywords):
    """Count articles containing specific cluster keywords."""
    
    # Split content by records (separated by ER -)
    records = re.split(r'ER\s*-\s*\n', ris_content)
    
    cluster_article_counts = defaultdict(set)  # Use set to avoid duplicates
    all_articles_with_citizen_science = set()
    
    for i, record in enumerate(records):
        if not record.strip():
            continue
            
        # Extract different fields
        title_match = re.search(r'TI\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        abstract_match = re.search(r'AB\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        keywords_match = re.search(r'KW\s*-\s*(.+?)(?=\n[A-Z]{2}\s*-|\nER|\Z)', record, re.DOTALL | re.IGNORECASE)
        
        record_text = ""
        if title_match:
            record_text += " " + title_match.group(1)
        if abstract_match:
            record_text += " " + abstract_match.group(1)
        if keywords_match:
            record_text += " " + keywords_match.group(1)
        
        # Convert to lowercase for case-insensitive matching
        record_text_lower = record_text.lower()
        
        # Check each cluster's keywords
        for cluster_name, keywords in cluster_keywords.items():
            for keyword in keywords:
                pattern = re.compile(re.escape(keyword.lower()), re.IGNORECASE)
                if pattern.search(record_text_lower):
                    cluster_article_counts[cluster_name].add(i)
                    all_articles_with_citizen_science.add(i)
    
    return cluster_article_counts, all_articles_with_citizen_science

def main():
    """Main function to count articles per cluster."""
    
    # Path to the RIS file
    ris_file_path = "/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris"
    
    print("Count Articles per Citizen Science Cluster")
    print("=" * 50)
    print(f"Date of execution: 2025-01-27")
    print(f"Analyzing file: {ris_file_path}")
    print()
    
    # Load RIS file
    print("Loading RIS file...")
    ris_content = load_ris_file(ris_file_path)
    if ris_content is None:
        sys.exit(1)
    
    print(f"File loaded successfully. Content length: {len(ris_content)} characters")
    print()
    
    # Get cluster-specific keywords
    cluster_keywords = extract_cluster_specific_keywords()
    
    # Count articles
    print("Counting articles with cluster-specific citizen science keywords...")
    cluster_article_counts, all_articles = count_articles_with_cluster_keywords(ris_content, cluster_keywords)
    
    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    
    print("\nArticles per Cluster:")
    print("-" * 30)
    
    total_articles = 0
    for cluster_name, articles in sorted(cluster_article_counts.items()):
        article_count = len(articles)
        total_articles += article_count
        
        # Format cluster name for display
        display_name = cluster_name.replace('_', ' ').replace(' co ', ' co-').title()
        display_name = display_name.replace('Hiv', 'HIV').replace('Ich', 'ICH')
        
        print(f"{display_name}: {article_count} articles")
    
    print(f"\nTotal unique articles with citizen science keywords: {len(all_articles)}")
    print(f"Total keyword matches across clusters: {total_articles}")
    
    # Calculate overlap
    print(f"\nNote: Some articles may appear in multiple clusters due to keyword overlap")
    
    # Show detailed breakdown
    print("\n" + "=" * 50)
    print("DETAILED BREAKDOWN")
    print("=" * 50)
    
    for cluster_name, articles in sorted(cluster_article_counts.items()):
        article_count = len(articles)
        display_name = cluster_name.replace('_', ' ').replace(' co ', ' co-').title()
        display_name = display_name.replace('Hiv', 'HIV').replace('Ich', 'ICH')
        
        print(f"\n{display_name}:")
        print(f"  - Articles: {article_count}")
        print(f"  - Keywords searched: {cluster_keywords[cluster_name]}")

if __name__ == "__main__":
    main()
