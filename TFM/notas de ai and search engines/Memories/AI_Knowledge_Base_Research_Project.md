# AI Knowledge Base: Cultural Heritage & Technology Research Project
## SciMAT Bibliometric Analysis - TFM Research

**Date of Creation:** 2024-07-30  
**Project Type:** Master's Thesis (TFM)  
**Research Domain:** Cultural Heritage & Technology  
**Methodology:** Bibliometric Analysis, Strategic Diagram Visualization  

---

## Project Overview

### Research Context
This project analyzes the evolution of research themes in Cultural Heritage and Technology using SciMAT bibliometric analysis. The research examines three distinct time periods to understand how research focus areas have evolved over time.

### Time Periods Analyzed
1. **2014-2019**: Growth and specialization period (20 clusters)  
2. **2020-2025**: Current research landscape (20 clusters)

### Academic Framework
- **Discipline**: Digital Humanities, Information Science
- **Methodology**: Bibliometric Analysis, Science Mapping
- **Tools**: SciMAT, D3.js, Python, pandas
- **Output**: Interactive Strategic Diagrams

### Analysis Framework
- Follow the "SciMAT-v1.1.04 Original" Folder
- **Unit of analysis:** Words (authorRole=true, sourceRole=true)
- **Kind of network:** Co-occurrence 
- **Normalization measure:** Inclusion index
- **Cluster algorithm:** Centers simples
- **Max cluster size:** 12
- **Min cluster size:** 3
- Treshold: 0.5
- Analyze Cluster Evolution - Inclusion Index for overlap between clusters across periods 
- **Evolution measure:** Inclusion index
- **Overlapping measure:** Inclusion index  

---

## Technical Infrastructure

### Development Environment
- **Operating System**: macOS 23.4.0
- **Python Version**: 3.13
- **Virtual Environment**: venv (with pandas 2.3.1)
- **Web Server**: Python HTTP Server (port 8000)

### Key Files and Directories
```
TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor
├── strategic_measures.csv (43 records)
├── generate_d3_data.py (D3.js data generator)
├── d3_visualizations/ (Interactive HTML files)
│   ├── interactive_strategic_map_2014_2019.html
│   ├── interactive_strategic_map_2020_2025.html
│   ├── interactive_strategic_map_Previous_2013.html
│   └── *.json (Data files)
└── D3_Visualization_Process_Documentation.md
```

### Data Structure
- **Input**: CSV files with strategic measures
- **Processing**: Python scripts for data transformation
- **Output**: Interactive D3.js visualizations
- **Format**: JSON data + HTML templates

---

## Research Methodology

### SciMAT Analysis Process
1. **Data Collection**: Bibliographic records from multiple sources
2. **Preprocessing**: Deduplication, cleaning, standardization
3. **Co-occurrence Analysis**: Keyword network construction
4. **Strategic Diagram Generation**: Centrality vs Density mapping
5. **Interactive Visualization**: D3.js web-based exploration
- Document with rules: [[Scimat_Analysis_Master_Plan]]

### Strategic Quadrants
- **Motor**: Core research themes
- **Specialized**: Emerging specialized areas
- **Basic**: Fundamental research
- **Emerging/Declining**: Peripheral or declining themes
- Document with rules: [[Strategic_Diagrams_Rules]]

### Key Metrics
- **Centrality**: Measure of cluster importance in the network
- **Density**: Measure of internal cohesion within clusters
- **Size**: Number of keywords in each cluster
- **Evolution**: Temporal changes in research themes
- Document with rules: [[Strategic_Diagrams_Rules]]

---

## Interactive Visualization Features

### D3.js Implementation
- **Interactive Bubble Charts**: Hover for detailed information
- **Color-coded Quadrants**: Strategic positioning visualization
- **Real-time Statistics**: Dynamic summary cards
- **Responsive Design**: Academic presentation ready

### User Interaction
- **Hover Tooltips**: Cluster details, keywords, metrics
- **Period Comparison**: Side-by-side temporal analysis
- **Statistical Summary**: Total clusters, keywords, averages
- **Strategic Positioning**: Visual quadrant mapping

---

## Academic Applications

### Research Communication
1. **Conference Presentations**: Dynamic displays for academic conferences
2. **Publication Enhancement**: Supplementary materials for research papers
3. **Teaching Tools**: Educational resources for bibliometric methods
4. **Collaborative Analysis**: Shared exploration of research trends

### Methodological Contributions
- **Interactive Bibliometrics**: Moving beyond static diagrams
- **Temporal Analysis**: Understanding research evolution
- **Visual Learning**: Enhanced comprehension of strategic positioning
- **Open Science**: Reproducible visualization workflows

---

## Technical Commands and Workflows

### Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install pandas --break-system-packages

# Run D3.js data generation
python3 generate_d3_data.py
```

### Web Server Access
```bash
# Start local server
cd d3_visualizations && python3 -m http.server 8000

# Access visualizations
http://localhost:8000/interactive_strategic_map_2014_2019.html
http://localhost:8000/interactive_strategic_map_2020_2025.html
http://localhost:8000/interactive_strategic_map_Previous_2013.html
```

### File Management
```bash
# Check generated files
ls -la d3_visualizations/

# View JSON data structure
cat d3_visualizations/strategic_map_2014_2019.json
```

---

## Research Insights and Findings

### Temporal Evolution
- **Previous_2013**: Limited research activity (3 clusters)
- **2014-2019**: Significant growth and diversification (20 clusters)
- **2020-2025**: Continued expansion with new specializations (20 clusters)

### Strategic Positioning
- **Motor Themes**: Core research areas with high centrality and density
- **Specialized Areas**: Emerging specialized research domains
- **Basic Research**: Fundamental concepts and methodologies
- **Emerging/Declining**: Peripheral or transitioning research themes

### Academic Impact
- **Digital Humanities**: Contribution to interactive visualization methods
- **Cultural Heritage**: Understanding research evolution in the field
- **Bibliometrics**: Advancement of science mapping techniques
- **Open Science**: Reproducible research workflows

---

## Future Development Opportunities

### Technical Enhancements
1. **Export Functionality**: PDF/SVG export capabilities
2. **Comparative Analysis**: Side-by-side period comparison
3. **Advanced Filtering**: Keyword-based cluster filtering
4. **Mobile Optimization**: Responsive design improvements

### Research Extensions
1. **Citation Analysis**: Integration with citation networks
2. **Author Analysis**: Researcher collaboration patterns
3. **Institution Mapping**: Geographic and institutional patterns
4. **Funding Analysis**: Research funding trends

### Academic Applications
1. **Teaching Resources**: Educational materials for bibliometric courses
2. **Research Planning**: Evidence-based research strategy development
3. **Policy Support**: Data-driven research policy recommendations
4. **Collaboration Networks**: Identifying potential research partnerships

---

## Key References and Citations

### Core Methodologies
1. Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2011). SciMAT: A new science mapping analysis software tool. *Journal of the American Society for Information Science and Technology*, 63(8), 1609-1630.

2. Bostock, M., Ogievetsky, V., & Heer, J. (2011). D3: Data-driven documents. *IEEE Transactions on Visualization and Computer Graphics*, 17(12), 2301-2309.

### Academic Context
3. McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 51-56.

4. Digital Humanities Quarterly. (2023). Interactive visualizations in humanities research. *Digital Humanities Quarterly*, 17(2). #research_method 

---

## AI Interaction Guidelines

### When Working with This Project
1. **Always reference the academic framework** of Cultural Heritage and Technology research
2. **Consider the temporal evolution** across three distinct periods
3. **Emphasize interactive visualization** benefits for research communication
4. **Include methodological contributions** to bibliometric analysis
5. **Reference the strategic quadrant** classification system
6. **Consider the digital humanities** perspective in all recommendations

### Technical Support
- **Environment**: Always activate virtual environment first
- **Dependencies**: Use `--break-system-packages` flag for pip installations
- **Web Server**: Use localhost:8000 for interactive visualizations
- **Data Files**: JSON files contain structured strategic measures data

### Academic Standards
- **Citations**: Always include relevant academic references
- **Methodology**: Explain processes step-by-step for learning
- **Documentation**: Create comprehensive process documentation
- **Reproducibility**: Ensure all workflows are reproducible

---

**Knowledge Base Version:** 1.0  
**Last Updated:** 2024-07-30  
**Next Review:** 2024-08-30  
**Maintained By:** AI Assistant 