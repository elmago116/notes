---
title: Web Platform User Guide (EN)
source: Web Platform User Guide (EN).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---

[[PDF/Peninsula/Web Platform User Guide (EN).pdf]]

## User Guide - UBXAT

### Introduction

UBXAT is an advanced knowledge management platform designed for the exploration and analysis of historical data regarding the Spanish Civil War. The system integrates natural language processing technologies and knowledge graphs to facilitate the study of international brigaders and mass graves. This guide details the operational functionalities of the web interface.

### Main Functionalities

The UBXAT platform allows the execution of the following operations:

- **Natural language interaction**: Direct queries regarding brigader records, mass grave geolocation, and documentary sources.
- **Visual data analysis**: Exploration of an interactive graph representing entities and their relationships.
- **Technical queries (SPARQL)**: Execution of complex queries on the knowledge database.
- **Data ingestion and processing**: Tools for loading and transforming new information assets.
- **System monitoring**: Real-time supervision of the operational status of services.

### Navigation and Interface Structure

The interface is divided into two main navigation components:

1. **Sidebar**: Direct access to the system's four operational modules.
2. **Header**: Indicator of the active section and data update controls.

---

### 1. Agent Module (Intelligent Assistant)

This module constitutes the main query interface, allowing the user to obtain precise information without the need for technical database knowledge.

**Query procedure**

1. Select the Agent option in the sidebar.
2. Enter the query in the bottom text field.
3. Execute using the Enter key or the Send button.

**Assistant capabilities**

- **Confidence evaluation**: A visual indicator (green, yellow, or red) determines the degree of reliability of the generated response.
- **Information traceability**: The system displays "source chips," allowing users to verify the origin of the data.
- **Performance metrics**: Visualization of the processing time for each response.
- **History management**: Tools to copy responses to the clipboard or restart the chat session for new queries.

---

### 2. Knowledge Graph Module (Interactive Visualization)

Graphic representation of the network of historical entities and their interconnections.

**Entity classification by nodes**

- **Red Nodes**: Personnel (Brigaders).
- **Blue Nodes**: Geographical locations and historical events.
- **Green Nodes**: Documentation and reference archives.
- **Orange Nodes**: Mass grave records.

**Interaction and analysis**

- **Navigation**: Users can pan and zoom to explore the network.
- **Inspection**: When a node is selected, detailed information associated with that entity is displayed.
- **Control Panel**: Located in the bottom left margin, it provides real-time statistics on the volume of processed nodes and relationships.

---

### 3. SPARQL Module (Advanced Queries)

Section oriented toward technical users for the extraction of structured data using the SPARQL query language.

**Executing queries**

The system offers a library of predefined queries covering the most frequent use cases:

- Lists of people with birth/death metadata.
- Geolocation of mass graves with specific coordinates.
- Analysis of relationship density between entities.
- Data existence verifications (ASK queries).

**Results management**

Data is returned in JSON format, ensuring compatibility for subsequent export or external analysis. A quick copy function is included to facilitate workflow.

---

### 4. Ingestion Module (Data Administration)

Tool dedicated to expanding the knowledge base by loading new datasets.

**Ingestion workflow**

1. **File Upload**: Support for structured formats (SQL, CSV, JSON).
2. **ETL Process Configuration**: Definition of parameters such as automatic format detection and batch size to optimize performance.
3. **Execution**: The system allows monitoring the loading progress in real-time.

**Activity log**

The module maintains a record of:

- Files available on the server (name, type, size, and date).
- Process status (In progress, Completed, or Failed).

---

### Maintenance and System Status

The platform integrates self-diagnostic mechanisms visible to the user:

- **API Status**: Connection indicators with the Cognitive ETL engine.
- **Synchronization**: Alerts regarding the availability of the chat service and graph updates.

---

### Professional Use Recommendations

- For optimal results in the Agent module, the use of precise and contextualized queries is recommended.
- In case of high latency during graph loading, use zoom controls to segment the view of interest.
- For any persistent technical issues, it is suggested to refresh the session or check the status indicators in the administration section.

*Note: Possible refinements may be applied to the interface.*
