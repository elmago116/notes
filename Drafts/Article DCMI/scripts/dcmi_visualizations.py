#!/usr/bin/env python3
"""
DCMI Visualization Generator
Creates DCMI-specific visualizations for bibliometric analysis results

Date: January 27, 2025
Research Context: DCMI-specific visualization outputs for semantic web and GLAM research
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import networkx as nx
import json
import os
import argparse
from pathlib import Path
import numpy as np

def create_dcmi_theme_evolution_plot(temporal_results, output_dir):
    """
    Create DCMI theme evolution plot over time periods
    
    Args:
        temporal_results (dict): Temporal analysis results
        output_dir (str): Output directory for plots
    """
    
    # Prepare data for plotting
    themes = ['dublin_core', 'semantic_web', 'cultural_heritage', 'participatory_design', 'accessibility', 'metadata_standards']
    periods = list(temporal_results.keys())
    
    # Create data matrix
    data_matrix = []
    for period in periods:
        period_data = temporal_results[period]
        theme_counts = [len(period_data['themes'].get(theme, [])) for theme in themes]
        data_matrix.append(theme_counts)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    
    x = np.arange(len(themes))
    width = 0.35
    
    for i, period in enumerate(periods):
        ax.bar(x + i * width, data_matrix[i], width, label=period, alpha=0.8)
    
    ax.set_xlabel('DCMI Themes')
    ax.set_ylabel('Citation Count')
    ax.set_title('DCMI Theme Evolution Over Time Periods')
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels([theme.replace('_', ' ').title() for theme in themes], rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcmi_theme_evolution.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Created DCMI theme evolution plot: {os.path.join(output_dir, 'dcmi_theme_evolution.png')}")

def create_dcmi_impact_metrics_chart(impact_metrics, output_dir):
    """
    Create DCMI impact metrics radar chart
    
    Args:
        impact_metrics (dict): Impact metrics from analysis
        output_dir (str): Output directory for plots
    """
    
    # Prepare data for radar chart
    metrics = ['dcmi_compliance_rate', 'accessibility_score', 'metadata_completeness', 'semantic_web_integration']
    values = [impact_metrics[metric] for metric in metrics]
    
    # Convert to percentages
    values = [v * 100 for v in values]
    
    # Create radar chart
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
    values += values[:1]  # Close the loop
    angles += angles[:1]
    
    ax.plot(angles, values, 'o-', linewidth=2, label='DCMI Impact Metrics')
    ax.fill(angles, values, alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([metric.replace('_', ' ').title() for metric in metrics])
    ax.set_ylim(0, 100)
    ax.set_title('DCMI Impact Metrics Radar Chart', size=16, pad=20)
    
    # Add value labels
    for i, (angle, value) in enumerate(zip(angles[:-1], values[:-1])):
        ax.text(angle, value + 5, f'{value:.1f}%', ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcmi_impact_radar.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Created DCMI impact metrics radar chart: {os.path.join(output_dir, 'dcmi_impact_radar.png')}")

def create_dcmi_strategic_diagram(temporal_results, output_dir):
    """
    Create DCMI strategic diagram showing centrality vs density
    
    Args:
        temporal_results (dict): Temporal analysis results
        output_dir (str): Output directory for plots
    """
    
    # Collect all themes and their metrics across periods
    all_themes = {}
    
    for period_name, period_data in temporal_results.items():
        for theme_name, metrics in period_data['metrics'].items():
            if theme_name not in all_themes:
                all_themes[theme_name] = []
            all_themes[theme_name].append({
                'period': period_name,
                'centrality': metrics['centrality'],
                'density': metrics['density'],
                'count': metrics['count']
            })
    
    # Create strategic diagram for each period
    for period_name, period_data in temporal_results.items():
        fig, ax = plt.subplots(figsize=(12, 10))
        
        themes = list(period_data['metrics'].keys())
        centralities = [period_data['metrics'][theme]['centrality'] for theme in themes]
        densities = [period_data['metrics'][theme]['density'] for theme in themes]
        counts = [period_data['metrics'][theme]['count'] for theme in themes]
        
        # Create scatter plot with size based on count
        scatter = ax.scatter(centralities, densities, s=[c*50 for c in counts], 
                           alpha=0.7, c=counts, cmap='viridis')
        
        # Add theme labels
        for i, theme in enumerate(themes):
            ax.annotate(theme.replace('_', ' ').title(), 
                       (centralities[i], densities[i]),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=10, ha='left', va='bottom')
        
        # Add quadrant lines
        max_centrality = max(centralities) if centralities else 1
        max_density = max(densities) if densities else 1
        
        ax.axhline(y=max_density/2, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=max_centrality/2, color='gray', linestyle='--', alpha=0.5)
        
        # Add quadrant labels
        ax.text(max_centrality*0.75, max_density*0.75, 'Motor Themes', 
               ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(max_centrality*0.25, max_density*0.75, 'Specialized Themes', 
               ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(max_centrality*0.25, max_density*0.25, 'Emerging/Declining', 
               ha='center', va='center', fontsize=12, fontweight='bold')
        ax.text(max_centrality*0.75, max_density*0.25, 'Basic Themes', 
               ha='center', va='center', fontsize=12, fontweight='bold')
        
        ax.set_xlabel('Centrality')
        ax.set_ylabel('Density')
        ax.set_title(f'DCMI Strategic Diagram - {period_name}')
        
        # Add colorbar
        cbar = plt.colorbar(scatter)
        cbar.set_label('Citation Count')
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'dcmi_strategic_diagram_{period_name.replace(" ", "_")}.png'), 
                    bbox_inches='tight', dpi=300)
        plt.close()
        
        print(f"Created DCMI strategic diagram for {period_name}: {os.path.join(output_dir, f'dcmi_strategic_diagram_{period_name.replace(' ', '_')}.png')}")

def create_dcmi_network_visualization(citation_network, output_dir):
    """
    Create DCMI citation network visualization
    
    Args:
        citation_network (NetworkX graph): Citation network
        output_dir (str): Output directory for plots
    """
    
    if len(citation_network.nodes()) == 0:
        print("No nodes in citation network to visualize")
        return
    
    # Create network layout
    pos = nx.spring_layout(citation_network, k=1, iterations=50)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Draw nodes
    nx.draw_networkx_nodes(citation_network, pos, 
                          node_color='lightblue',
                          node_size=100,
                          alpha=0.7)
    
    # Draw edges
    nx.draw_networkx_edges(citation_network, pos, 
                          edge_color='gray',
                          alpha=0.5,
                          arrows=True,
                          arrowsize=10)
    
    # Draw labels
    nx.draw_networkx_labels(citation_network, pos, 
                           font_size=8,
                           font_family='sans-serif')
    
    ax.set_title('DCMI Citation Network')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcmi_citation_network.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Created DCMI citation network visualization: {os.path.join(output_dir, 'dcmi_citation_network.png')}")

def create_dcmi_quality_dashboard(quality_metrics, output_dir):
    """
    Create DCMI quality metrics dashboard
    
    Args:
        quality_metrics (dict): Quality assessment results
        output_dir (str): Output directory for plots
    """
    
    # Create subplots for different quality metrics
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Compliance rate pie chart
    compliant = quality_metrics['dcmi_compliant']
    non_compliant = quality_metrics['total_citations'] - compliant
    
    ax1.pie([compliant, non_compliant], 
            labels=['DCMI Compliant', 'Non-Compliant'],
            autopct='%1.1f%%',
            colors=['lightgreen', 'lightcoral'])
    ax1.set_title('DCMI Compliance Rate')
    
    # Accessibility score bar chart
    accessible = quality_metrics['accessibility_compliant']
    non_accessible = quality_metrics['total_citations'] - accessible
    
    ax2.bar(['Accessible', 'Non-Accessible'], [accessible, non_accessible],
            color=['lightblue', 'lightcoral'])
    ax2.set_title('Accessibility Compliance')
    ax2.set_ylabel('Citation Count')
    
    # Metadata completeness
    complete = quality_metrics['metadata_complete']
    incomplete = quality_metrics['total_citations'] - complete
    
    ax3.bar(['Complete', 'Incomplete'], [complete, incomplete],
            color=['lightgreen', 'lightcoral'])
    ax3.set_title('Metadata Completeness')
    ax3.set_ylabel('Citation Count')
    
    # Semantic web readiness
    semantic_ready = quality_metrics['semantic_web_ready']
    not_semantic_ready = quality_metrics['total_citations'] - semantic_ready
    
    ax4.bar(['Semantic Web Ready', 'Not Ready'], [semantic_ready, not_semantic_ready],
            color=['lightblue', 'lightcoral'])
    ax4.set_title('Semantic Web Readiness')
    ax4.set_ylabel('Citation Count')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcmi_quality_dashboard.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Created DCMI quality dashboard: {os.path.join(output_dir, 'dcmi_quality_dashboard.png')}")

def create_dcmi_temporal_trends(temporal_results, output_dir):
    """
    Create DCMI temporal trends visualization
    
    Args:
        temporal_results (dict): Temporal analysis results
        output_dir (str): Output directory for plots
    """
    
    # Prepare data for line plot
    periods = list(temporal_results.keys())
    themes = ['dublin_core', 'semantic_web', 'cultural_heritage', 'participatory_design']
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    for theme in themes:
        theme_counts = []
        for period in periods:
            count = len(temporal_results[period]['themes'].get(theme, []))
            theme_counts.append(count)
        
        ax.plot(periods, theme_counts, 'o-', linewidth=2, label=theme.replace('_', ' ').title())
    
    ax.set_xlabel('Time Period')
    ax.set_ylabel('Citation Count')
    ax.set_title('DCMI Theme Trends Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'dcmi_temporal_trends.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Created DCMI temporal trends visualization: {os.path.join(output_dir, 'dcmi_temporal_trends.png')}")

def generate_dcmi_visualization_report(output_dir):
    """
    Generate a comprehensive visualization report
    
    Args:
        output_dir (str): Output directory containing visualization files
    """
    
    report_content = """# DCMI Visualization Report

## Generated Visualizations

This report summarizes the DCMI-specific visualizations created for bibliometric analysis.

### 1. Theme Evolution Plot
- **File**: `dcmi_theme_evolution.png`
- **Purpose**: Shows how DCMI themes evolve across time periods
- **Insights**: Identifies emerging and declining themes in semantic web and GLAM research

### 2. Impact Metrics Radar Chart
- **File**: `dcmi_impact_radar.png`
- **Purpose**: Displays DCMI-specific impact metrics in radar format
- **Metrics**: Compliance rate, accessibility score, metadata completeness, semantic web integration

### 3. Strategic Diagrams
- **Files**: `dcmi_strategic_diagram_[period].png`
- **Purpose**: Shows centrality vs density for each time period
- **Quadrants**: Motor themes, specialized themes, emerging/declining themes, basic themes

### 4. Citation Network
- **File**: `dcmi_citation_network.png`
- **Purpose**: Visualizes citation relationships between DCMI publications
- **Features**: Node size based on citation count, edge direction shows citation flow

### 5. Quality Dashboard
- **File**: `dcmi_quality_dashboard.png`
- **Purpose**: Comprehensive view of DCMI quality metrics
- **Components**: Compliance rate, accessibility, metadata completeness, semantic web readiness

### 6. Temporal Trends
- **File**: `dcmi_temporal_trends.png`
- **Purpose**: Shows theme evolution trends over time
- **Features**: Line plots for each major DCMI theme

## Academic Framework Integration

These visualizations support several academic research frameworks:

### SALSA Framework Compatibility
- **Search**: Theme evolution plots help identify research gaps
- **Appraisal**: Quality dashboard provides quality assessment metrics
- **Synthesis**: Strategic diagrams support systematic review processes
- **Analysis**: Temporal trends enable longitudinal analysis

### Semantic Web Research Support
- **Dublin Core standards**: Direct visualization of metadata compliance
- **Linked data compatibility**: Network visualizations show data relationships
- **Interoperability**: Quality metrics assess cross-platform compatibility

### GLAM Sector Applications
- **Cultural heritage preservation**: Theme analysis shows preservation trends
- **Participatory design**: Quality metrics assess community engagement
- **Accessibility compliance**: Dedicated accessibility visualization

## Research Implications

### NeSy AI in GLAM Contexts
- **Neural-symbolic integration**: Network visualizations show AI-semantic web connections
- **Cultural heritage preservation**: Temporal trends identify preservation technology evolution
- **Community engagement**: Quality metrics assess participatory design effectiveness

### Metadata Evolution Studies
- **Temporal analysis**: Strategic diagrams show metadata standard evolution
- **Cross-domain interoperability**: Network analysis reveals cross-sector connections
- **User-centered design**: Quality dashboard tracks community-driven development

**Date of visualization generation**: January 27, 2025  
**Research framework**: DCMI-specific visualization for semantic web and GLAM research  
**Methodological approach**: Comprehensive visualization suite for bibliometric analysis
"""
    
    with open(os.path.join(output_dir, 'dcmi_visualization_report.md'), 'w') as f:
        f.write(report_content)
    
    print(f"Created DCMI visualization report: {os.path.join(output_dir, 'dcmi_visualization_report.md')}")

def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description='DCMI Visualization Generator')
    parser.add_argument('--input', required=True, help='Input JSON file with analysis results')
    parser.add_argument('--output', required=True, help='Output directory for visualizations')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Load analysis results
    with open(args.input, 'r') as f:
        results = json.load(f)
    
    # Generate visualizations
    if 'temporal_results' in results:
        create_dcmi_theme_evolution_plot(results['temporal_results'], args.output)
        create_dcmi_strategic_diagram(results['temporal_results'], args.output)
        create_dcmi_temporal_trends(results['temporal_results'], args.output)
    
    if 'impact_metrics' in results:
        create_dcmi_impact_metrics_chart(results['impact_metrics'], args.output)
    
    # Generate visualization report
    generate_dcmi_visualization_report(args.output)
    
    print(f"All DCMI visualizations generated in {args.output}")

if __name__ == "__main__":
    main()


