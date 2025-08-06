# RIS Processing Pipeline Knowledge Base

**Last Updated:** 2025-08-04  
**Version:** 2.1  
**Scope:** Complete RIS processing and SciMAT analysis pipeline

## Overview

This document contains comprehensive knowledge about the RIS processing pipeline and SciMAT analysis implementation, including all scripts, methodologies, and results.

## Pipeline Components

### 1. RIS Processing Pipeline ✅ COMPLETED
- **Phase 1:** File merging and initial cleaning
- **Phase 2:** Field mapping and standardization  
- **Phase 3:** Keyword extraction and normalization
- **Phase 4:** Quality assurance and validation
- **Phase 5:** Final dataset preparation

### 2. SciMAT Analysis Implementation ✅ COMPLETED
- **Step 0:** Data cleaning and normalization (TFM1.ris - 3,270 records)
- **Step 1:** Keyword extraction and preprocessing
- **Step 2:** Co-occurrence network building
- **Step 3:** Network clustering (43 clusters total)
- **Step 4:** Strategic measures calculation (centrality and density)
- **Step 5:** Cluster evolution analysis
- **Step 6:** Cluster network generation (42 networks) ✅ **COMPLETED 2025-08-04**
- **Step 7:** Strategic diagrams generation

## Recent Updates - 2025-08-04

### File Organization Correction ✅ RESOLVED
**Issue Identified:** Cluster network files were generated in incorrect location
- **Problem:** Files created in `./results/output_diagrams/cluster_networks_2025-08-04/` (scripts subfolder)
- **Expected Location:** `../results/output_diagrams/` (main results folder)
- **Resolution:** Successfully moved all 42 cluster network PNG files to correct location

### File Structure Validation
**Correct Structure:**
```
ScimatCursor/
├── scripts/                    # Python analysis scripts
│   └── results/               # ❌ WRONG LOCATION (was used)
└── results/                   # ✅ CORRECT LOCATION
    ├── data/                  # CSV data files
    ├── output_diagrams/       # Generated visualizations
    │   ├── 2025-08-04/       # Strategic diagrams
    │   └── [cluster networks] # Cluster networks (moved here)
    └── processing_results/    # Processing outputs
```

### Cluster Network Generation - COMPLETED 2025-08-04

### Implementation Details
- **Script:** `generate_all_cluster_networks.py`
- **Methodology:** Following original SciMAT procedures
- **Data Sources:** 
  - `clusters_by_period.csv` (cluster data)
  - `cooccurrence_*.csv` (co-occurrence networks)
- **Output:** 42 PNG network visualizations

### Technical Specifications
- **Layout Algorithm:** Spring layout (k=2, iterations=50)
- **Node Sizing:** Proportional to degree centrality
- **Edge Weighting:** Based on co-occurrence strength
- **Thematic Coloring:** 8 color groups with enhanced coding system
- **Image Format:** PNG, 300 DPI, 14x10 inches

### Thematic Color System
1. **🔵 Blue:** Semantic Technologies (knowledge graphs, ontologies, RDF)
2. **🔴 Red:** HerStory (cultural heritage, gender, digital humanities)
3. **🟢 Green:** Participative Design (UX, co-creation, HCI)
4. **🟣 Purple:** GLAM (museums, libraries, archives)
5. **🟠 Orange:** Identity & Culture (identity, culture, ethnic)
6. **🔶 Teal:** Health & Society (health, community research)
7. **🟤 Dark Orange:** Design & Technology (design control, politics)
8. **⚪ Gray:** Other/Unclassified (cross-thematic content)

### Generation Results
- **✅ Successfully Generated:** 42 network maps
- **⚠️ Skipped:** 1 cluster (insufficient co-occurrence data)
- **📁 Final Output Directory:** `../results/output_diagrams/` (corrected)
- **Documentation:** `README_Cluster_Networks.md` created

### Network Features
- **Visual Elements:** Nodes, edges, colors, labels
- **Statistical Information:** Network density, clustering coefficient
- **Thematic Classification:** Primary thematic group assignment
- **Cluster Information:** ID, name, period

## Strategic Diagram Corrections - 2025-08-04

### Critical Fixes Applied
1. **Density Formula:** Restored original SciMAT formula `100 × (sum_internal / cluster_size)`
2. **Axes Configuration:** Corrected to X-axis = Density, Y-axis = Centrality
3. **Quadrant Interpretation:** Fixed strategic quadrant assignments
4. **Centrality Zero Validation:** Confirmed 6/43 clusters (14%) have zero centrality - academically valid

### Strategic Quadrants (Corrected)
- **Motor (Top Right):** High Centrality + High Density
- **Basic (Top Left):** Low Centrality + High Density  
- **Specialized (Bottom Right):** High Centrality + Low Density
- **Emerging/Declining (Bottom Left):** Low Centrality + Low Density

## Data Quality Metrics

### Dataset Statistics
- **Total Records:** 3,270 (TFM1.ris)
- **Source Breakdown:** 2,657 Scopus (81.2%), 613 WoS (18.8%)
- **Keyword Coverage:** 1,919 records with keywords (58.7%)
- **Quality Score:** 100% essential fields, 99.9% valid formats

### Network Scale
- **2014-2019:** 150K edges (dramatically improved from 6K)
- **2020-2025:** 150K edges (dramatically improved from 6K)
- **Previous_2013:** 12K edges

### Clustering Results
- **Total Clusters:** 43 across all periods
- **Cluster Sizes:** 3-12 keywords per cluster
- **Algorithm:** Simple Centers Algorithm
- **Normalization:** Inclusion index

## Technical Validation

### Script Performance
- **Memory Management:** Chunked file reading for large networks
- **Processing Speed:** Optimized for 150K+ edge networks
- **Error Handling:** Comprehensive exception handling
- **Output Quality:** High-resolution PNG images

### Academic Rigor
- **Methodology:** Follows original SciMAT Java implementation
- **Validation:** Cross-referenced with original SciMAT source code
- **Documentation:** Comprehensive README files created
- **Reproducibility:** All scripts and data files preserved

## File Organization

### Current Structure (Corrected)
```
ScimatCursor/
├── scripts/                    # Python analysis scripts
├── results/                   # ✅ MAIN RESULTS FOLDER
│   ├── data/                  # CSV data files
│   ├── output_diagrams/       # Generated visualizations
│   │   ├── 2025-08-04/       # Strategic diagrams
│   │   └── [42 cluster networks] # Cluster networks (moved here)
│   ├── processing_results/    # Processing outputs
│   └── interactive_visualizations/ # Interactive outputs
└── documentation/             # Analysis documentation
```

### Key Files Generated
- **Cluster Networks:** 42 PNG files with thematic coloring (correctly located)
- **Strategic Diagrams:** 6 files (PNG + SVG) for 3 periods
- **Data Files:** CSV files with strategic measures and cluster data
- **Documentation:** README files for each output type

## Lessons Learned

### Critical Insights
1. **Density Formula:** Original SciMAT uses division by cluster size, not multiplication
2. **Axes Configuration:** Strategic diagrams require specific X/Y axis mapping
3. **Centrality Zero:** Valid academic result for isolated, specialized clusters
4. **Thematic Coloring:** Enhanced 8-color system provides better classification
5. **Network Generation:** Spring layout with proper parameters essential for readability
6. **File Organization:** Always verify output locations match expected structure

### Best Practices
1. **Validation:** Always cross-reference with original SciMAT implementation
2. **Documentation:** Create comprehensive README files for all outputs
3. **Organization:** Maintain clear folder structure for outputs
4. **Quality Control:** Validate network statistics and visual clarity
5. **Academic Standards:** Follow bibliometric methodology rigorously
6. **File Location:** Double-check output directories match project structure

## Future Enhancements

### Planned Improvements
1. **Interactive Networks:** D3.js interactive cluster network visualizations
2. **Evolution Tracking:** Side-by-side cluster evolution comparisons
3. **Export Options:** SVG format for scalable graphics
4. **Batch Processing:** Automated generation for new datasets

### Integration Possibilities
1. **Citation Networks:** Combined keyword and citation analysis
2. **Temporal Analysis:** Time-series visualization of cluster development
3. **Strategic Integration:** Combined strategic diagrams and cluster networks
4. **Thematic Evolution:** Tracking thematic changes over time

---

**Generated by:** SciMAT Analysis Pipeline  
**Date:** 2025-08-04  
**Status:** Complete cluster network generation with corrected file organization 