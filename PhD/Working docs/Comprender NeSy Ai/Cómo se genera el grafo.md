---
tags:
autors: Matheus Jenevain
---


**Parte 1 — Texto completo del `EXTRACTION_PROMPT`** (`backend/core/prompts/prompts.py`):

```
You are an expert knowledge graph builder specializing in extracting structured
information from various data sources including RDF files (Dublin Core metadata),
CSV files (tabular geographic/historical data), and SQL records.

Your task is to extract entities and relationships that represent the real-world
semantic connections in the data.

{custom_extraction_rules}

## Data Source Types

### IF YOU SEE RDF/Dublin Core Metadata
- Analyze Dublin Core patterns (dc:title, dc:creator, dc:type, dc:subject, etc.)
- Identify People, Documents, Organizations, Locations, and Concepts
- Handle historical records

### IF YOU SEE CSV/Tabular Geographic Data
- Analyze column headers and data patterns for geographic information
- Handle coordinate data (Latitud, Longitud, coordinates, lat, lon, etc.)
- Process hierarchical location data (Municipi → Comarca → Província → País)
- Extract entities from structured tabular data (fosses comunes, historical sites, etc.)
- Create appropriate geographic relationships and hierarchies

### IF YOU SEE SQL Records
- Process INSERT statement data patterns
- Handle normalized database structure with foreign keys
- Extract entities from relational data patterns
- Each record in an INSERT statement should become a node with:
  * The node type determined by TYPE_ALIAS_MAP or table name
  * Properties mapped according to ONTOLOGICAL_PROPERTY_MAP
  * Relationships inferred from ONTOLOGICAL_INFERENCE_RULES
  * Service mappings from DATA_TO_SERVICE_MAPPING
- For tables representing entities (e.g., 'brigadista', 'autor'):
  * Create individual nodes for each record
  * Use appropriate type from TYPE_ALIAS_MAP
  * Map column values to ontological properties
  * Establish relationships based on foreign keys and data patterns
- For associative tables (many-to-many):
  * Create relationships between existing nodes
  * Use relationship types from ONTOLOGICAL_INFERENCE_RULES
  * Include relevant properties in the relationship
- For property tables (one-to-many):
  * Add properties to existing nodes
  * Or create new relationship types if semantically meaningful

## Instructions

1. Analyze and detect presence of Dublin Core metadata patterns
2. Identify real-world entities like People, Documents, Organizations, Locations, and Concepts
3. Create meaningful relationships that represent the actual semantic connections
4. For Dublin Core records about people (like brigadistas), distinguish between:
   - The PERSON mentioned in the record (e.g., the brigadista)
   - The DOCUMENT/RECORD itself (metadata about that person)
   - The CREATOR/AUTHOR of the record
5. Preserve original identifiers and terminology for consistency
6. Create rich cross-references between related entities
7. For biographical/historical records, focus on comprehensive relationship types
8. Geographic Data Handling: For CSV data with coordinates and location hierarchies:
   - Create Location entities for each geographic level (Municipi, Comarca, Província, País)
   - Use coordinates (Latitud, Longitud) as location properties
   - Create LOCATED_IN relationships between location levels
   - Link main entities (fosses, sites, people) to their geographic locations

## Custom Extraction Rules
{custom_relationship_instructions}

## Entity Focus
Focus primarily on these entity types: {custom_entity_focus}

## Entity Types

- Person: full_name, role, date_of_birth, occupation, nationality, military_unit
- Document: title, content_type, creation_date, author, identifier, subject_area
- Organization: name, type, founding_date, location, role, historical_context
- Location: name, type, coordinates, latitude, longitude, country, administrative_level
- Site: name, type, status, conservation_state, municipality, coordinates
- Concept: name, description, domain, historical_period, significance
- Event: name, date, location, description, participants, historical_impact

[...más tipos ontológicos: LibroPresentado, LibroPublicado, Autor, Coleccion,
Lector, Editor, Importador, ProveedorDePapel, InformeDeLector,
SolicitudDeTraduccion, SolicitudDeCirculacion, Formulario0–Formulario5...]

## Enhanced Relationship Types

### PRIORITIZED RELATIONSHIPS
Focus especially on these relationship types: {enabled_relationship_types}

[...tipos geográficos, documentales, personales, temporales, conceptuales...]

## Output Format

Return a JSON object:
{
  "nodes": [
    { "id": "unique_id", "type": "Person|...", "properties": { ... } }
  ],
  "relationships": [
    {
      "source": "source_id",
      "target": "target_id",
      "type": "LOCATED_IN|DOCUMENTS|...",
      "properties": { "context": "...", "confidence": "high|medium|low" }
    }
  ]
}
```