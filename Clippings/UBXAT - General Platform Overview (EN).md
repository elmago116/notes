---
title: UBXAT - General Platform Overview (EN)
source: UBXAT - General Platform Overview (EN).pdf
type: PDF extraction
---


UBXAT: PLATFORM DOCUMENTATION
Overview
UBXAT is a platform for processing historical data through Artificial Intelligence, enabling historical researchers
to work with complex data without technical expertise in databases or programming.
The Historical Problem
Traditional Historical Research
Historians face significant technical barriers:
Fragmented Data: Historical information distributed across multiple formats (Drupal SQL files, CSVs, PDF
documents)
Technical Complexity: Requires advanced knowledge of databases, SPARQL, and data processing
Limited Time: Researchers spend months on data cleaning and structuring
Loss of Context: Technical focus displaces historical analysis
Current Reality
85% of research time is dedicated to technical processing
Critical historical data remains inaccessible due to technical complexity
Specialized knowledge limits who can contribute to historical research
The Solution
Cognitive ETL Platform
UBXAT transforms the historical research paradigm through:
1. Intelligent Zero-Configuration Ingestion

Heterogeneous Files
SQL, CSV, RDF
Automatic Processing
AI + Ground Truth
Knowledge Graph
Structured Neo4j
Auto-detection: Automatically identifies data format and structure
Ground Truth: Intelligent mappings based on pre-existing historical knowledge
Adaptability: Learns and adapts to new data schemas
2. Semantic Mapping with AI
Google Gemini: Analyzes and understands the historical context of data
Wikidata Mapping: Connects local data with standardized global ontologies
Intelligent Resolution: Avoids duplicates through advanced semantic matching
3. Historical Knowledge Graph
Neo4j Aura: Graph database optimized for complex relationships
Natural Queries: Conversational interface for questions in human language
Context Preservation: Maintains historical relationships and complete metadata
Conceptual Architecture
Cognitive Pipeline

Input Sources
Heterogeneous
Dynamic Parser
Ground Truth
Gemini Analyzer
AI Context
Schema Mapper
Wikidata
Entity Resolver
No Duplicates
Cypher Generator
Optimal Queries
Neo4j Storage
Knowledge Graph
Conversational API
Natural Language
Key Components
Ground Truth as Collective Intelligence
Historical Mappings: Accumulated knowledge from previous researchers
Continuous Learning: Updates with each new processed dataset

Consistency: Ensures similar data is mapped uniformly
AI as Cognitive Accelerator
Contextual Analysis: Gemini understands the historical meaning of data
Intelligent Generation: Creates optimized queries based on semantic understanding
Adaptability: Learns historical patterns to improve future mappings
Benefits for Research
Knowledge Democratization
Universal Access: Historians without technical background can process complex data
Barrier Reduction: Eliminates dependence on IT specialists
Expanded Collaboration: Enables contributions from diverse researchers
Operational Efficiency
80% Reduction in time dedicated to technical processing
Scalability: Processes massive datasets in minutes instead of months
Reproducibility: Automated processes ensure consistency
Research Quality
Consistent Mappings: Ground truth ensures uniformity in analysis
Context Preservation: Knowledge graphs maintain complex relationships
New Discoveries: Conversational queries reveal hidden patterns
Real Use Cases
International Brigades Research
Problem: Fragmented data on brigadiers across multiple Drupal databases, inconsistent formats.
UBXAT Solution:

1. Automatic Ingestion: Processes SQL dumps without manual configuration
2. Intelligent Mapping: Connects local data with Wikidata (Q5 for persons)
3. Entity Resolution: Identifies individuals mentioned in multiple sources
4. Conversational Queries: "How many brigadiers were from the United States?"
Mass Graves Analysis
Problem: Geographic and temporal data distributed across CSVs and documents.
UBXAT Solution:
1. Multi-source Integration: Automatically combines data from different formats
2. Geographic Mapping: Connects locations with Wikidata geographic ontologies
3. Temporal Analysis: Identifies chronological patterns in discoveries
4. Visualization: Knowledge graph reveals connections between historical events
Impact on Historical Research
Methodological Transformation
Before UBXAT
Traditional Flow
Raw Data
Researcher
Months of Cleaning
Manual Analysis
Conclusions

With UBXAT
UBXAT Flow
Natural Language Question
Researcher
Immediate Answers
Advanced Hypotheses
Benefits
For Individual Researchers
Time Freed: From technical cleaning to historical analysis
Expanded Scope: Processes datasets that were previously inaccessible
Collaboration: Shares findings with global community
For Institutions
Digital Preservation: Historical archives permanently accessible
Accelerated Research: Real-time answers to historical questions
Education: Tools for teaching history with data
Underlying Technology
AI as Cognitive Partner
Gemini 2.0: Advanced contextual understanding of historical content
LangGraph: Intelligent orchestration of ETL processes
Semantic Embeddings: Intelligent matching of similar entities

Robust Infrastructure
Neo4j Aura: Cloud-native graph database
REST APIs: Programmatic interface for integration with existing tools
Dynamic Ground Truth: Evolving knowledge base
