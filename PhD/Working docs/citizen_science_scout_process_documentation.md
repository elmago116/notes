---
tags:
  - op/doc/reporte
---
# Citizen Science Keywords Scout - Process Documentation

**Date of creation:** 2025-01-27

## Overview
This document describes the step-by-step process followed to create a script that scouts and extracts citizen science related keywords from a RIS (Research Information Systems) document.

## Process Steps

### Step 1: File Analysis
- **Input:** TFM1.ris file located at `/Users/elenagomez/Library/Mobile Documents/iCloud~md~obsidian/Documents/TFM/Scimat simulation/SciMAT-v1.1.04/ScimatCursor/results/data/TFM1.ris`
- **File size:** 4,937,854 characters (approximately 82,726 lines)
- **Format:** RIS (Research Information Systems) format used for bibliographic data

### Step 2: Keyword Pattern Definition
Defined comprehensive patterns for citizen science related terms including:

#### Core Terms:
- citizen science
- crowdsourcing/crowd-sourcing
- volunteer
- participatory
- community-based
- public participation/engagement
- citizen scientist(s)

#### Related Concepts:
- community science/engagement/participation
- public science
- volunteer monitoring/science
- participatory science/research/monitoring
- collaborative science/research
- open science/research
- distributed research/science

#### Specific Domains:
- citizen journalism/reporting
- volunteer computing/thinking
- participatory sensing/mapping/GIS
- community mapping
- crowd mapping
- crowdsourced/volunteer/community data

#### Digital Platforms:
- Zooniverse, Foldit, Galaxy Zoo
- iNaturalist, eBird
- citizen observatories

### Step 3: Script Development
Created Python script `citizen_science_keywords_scout.py` with the following components:

#### Key Functions:
1. `load_ris_file()` - Loads and parses RIS file content
2. `extract_citizen_science_keywords()` - Searches for patterns across RIS fields
3. `format_keywords_output()` - Formats results into readable markdown
4. `main()` - Orchestrates the entire process

#### Search Strategy:
- Case-insensitive pattern matching using regular expressions
- Searches across multiple RIS fields: TI (Title), AB (Abstract), KW (Keywords)
- Tracks frequency of each term across different records
- Provides detailed record references for verification

### Step 4: Execution and Results
- **Execution date:** 2025-01-27
- **Processing time:** < 1 second
- **Results:** 18 unique citizen science related terms found

## Tools and Models Used

### Software Tools:
- **Python 3.x** - Programming language
- **Regular Expressions (re module)** - Pattern matching
- **Collections (defaultdict, Counter)** - Data organization
- **Pathlib** - File path handling

### Libraries Used:
- `re` - Regular expression operations
- `sys` - System-specific parameters and functions
- `collections` - Specialized container datatypes
- `pathlib` - Object-oriented filesystem paths

### Models/Methods:
- Pattern-based text extraction
- Frequency analysis
- Case-insensitive string matching
- Record-based indexing

## Results Summary

### Top 10 Most Frequent Terms:
1. **participatory** - 147 records
2. **open research** - 18 records
3. **community-based** - 17 records
4. **crowdsourcing** - 17 records
5. **volunteer** - 15 records
6. **open science** - 10 records
7. **community engagement** - 9 records
8. **collaborative research** - 8 records
9. **participatory research** - 6 records
10. **community participation** - 5 records

### Output Files Generated:
1. `citizen_science_keywords_scout.py` - The extraction script
2. `citizen_science_keywords_list.md` - Detailed results with frequencies and record references
3. `citizen_science_scout_process_documentation.md` - This process documentation

## Key Findings

### High-Frequency Terms:
- "Participatory" appears in 147 records, indicating strong presence of participatory methodologies
- "Open research" and "open science" appear in 28 combined records, showing interest in open science practices
- "Community-based" approaches are mentioned in 17 records

### Specific Citizen Science Terms:
- Direct mentions of "citizen science" found in only 2 records
- "Citizen scientist(s)" mentioned in 4 records total
- "Crowdsourcing" appears in 17 records, showing broader adoption

### Methodology Insights:
- Strong emphasis on participatory and community-based approaches
- Significant presence of collaborative and open research practices
- Limited direct use of "citizen science" terminology despite relevant concepts

## Technical Notes

### Script Features:
- Comprehensive pattern matching covering various citizen science terminology
- Case-insensitive search for broader coverage
- Detailed record tracking for verification purposes
- Clean markdown output format for easy reading
- Error handling for file operations

### Performance:
- Efficient processing of large RIS file (4.9M characters)
- Fast execution time due to optimized pattern matching
- Memory-efficient processing using generators and sets

### Step 5: Clusters CSV Analysis
- **Input:** clusters_by_period_fixed_no_article.csv file from SciMAT analysis
- **File size:** 397 rows (395 data rows + header)
- **Format:** CSV with columns: period, cluster_id, cluster_name, keyword, is_center, is_densest

#### Clusters Analysis Results:
- **Total unique citizen science terms:** 5 (vs. 18 in RIS file)
- **Total matches:** 8 (vs. 377 in RIS file)
- **Distribution by period:**
  - 2014-2019: 3 matches
  - 2020-2025: 5 matches
- **Center keywords:** 0 (none found as cluster centers)
- **Densest keywords:** 0 (none found as densest keywords)

#### Top Terms in Clusters:
1. **participatory** - 3 matches (across digital storytelling, HIV research, ethical community research)
2. **community-based** - 2 matches (ethical community research, participation clusters)
3. **community participation** - 1 match (value co-creation cluster)
4. **crowdsourcing** - 1 match (digital storytelling cluster)
5. **participatory research** - 1 match (ethical community research cluster)

#### Key Clusters Containing Citizen Science Terms:
- **Cluster 4 (ethical community research)** - 2020-2025: 3 matches
- **Cluster 11 (digital storytelling)** - 2014-2019: 2 matches
- **Cluster 3 (HIV)** - 2020-2025: 1 match
- **Cluster 5 (participation)** - 2020-2025: 1 match
- **Cluster 7 (value co-creation)** - 2014-2019: 1 match

### Step 6: Comparative Analysis
Comparing RIS file vs. Clusters CSV results:

| Metric | RIS File | Clusters CSV | Difference |
|--------|----------|--------------|------------|
| Unique terms | 18 | 5 | -72% |
| Total matches | 377 | 8 | -98% |
| Most frequent term | participatory (147) | participatory (3) | -98% |

#### Key Insights:
1. **Dramatic reduction in citizen science presence** when moving from full text to clustered keywords
2. **Cluster normalization process** significantly filtered out citizen science terminology
3. **Temporal shift** toward more recent periods (2020-2025) in clusters
4. **Focus areas** in clusters: digital storytelling, community research, participation, HIV research

## Conclusion

The comprehensive analysis reveals two distinct perspectives on citizen science research:

### RIS File Analysis (Full Text):
- **Rich presence** of citizen science concepts with 18 unique terms and 377 total matches
- **Strong participatory focus** with "participatory" appearing in 147 records
- **Broad thematic coverage** across multiple research domains
- **Limited direct "citizen science" terminology** but extensive related concepts

### Clusters Analysis (Normalized Keywords):
- **Significantly reduced presence** with only 5 unique terms and 8 total matches
- **Cluster normalization** filtered out most citizen science terminology
- **Concentrated in specific clusters** related to digital storytelling, community research, and participation
- **Temporal concentration** in more recent periods (2020-2025)

### Research Implications:
1. **Citizen science concepts** are present in the literature but may not be explicitly labeled as such
2. **Participatory methodologies** are the most prominent citizen science approach
3. **Community-based research** represents a key pathway for citizen science implementation
4. **Digital storytelling and crowdsourcing** emerge as specific application areas
5. **Recent trend** toward more explicit citizen science terminology in newer research

The generated keyword lists provide complementary perspectives for bibliometric studies, research gap analysis, and thematic exploration of citizen science trends in the dataset.

