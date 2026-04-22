---
tags:
  - op/doc/reporte
authors:
  - Matheus Jenevain
date: 2026-01-29
---

# Ground Truth and Structured Prompt Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Ground Truth: The Validation Framework](#ground-truth-the-validation-framework)
3. [Components of Ground Truth](#components-of-ground-truth)
4. [Structured Prompt: The Neural-Symbolic Bridge](#structured-prompt-the-neural-symbolic-bridge)
5. [How Ground Truth and Prompt Work Together](#how-ground-truth-and-prompt-work-together)
6. [Complete Structured Prompt](#complete-structured-prompt)
7. [Validation Pipeline Flow](#validation-pipeline-flow)

---

## Introduction

neoRAG implements a **neurosymbolic AI architecture** that combines neural language models (Google Gemini) with symbolic validation rules. This document explains two critical components:

1. **Ground Truth**: The comprehensive set of validation rules, ontological constraints, and data quality standards that ensure extracted information is semantically correct and consistent.
2. **Structured Prompt**: The detailed instructions given to the LLM that guide entity and relationship extraction according to the ground truth rules.

Together, these components form a **neural-symbolic bridge** where the LLM performs intelligent extraction (neural) and the ground truth rules enforce consistency and correctness (symbolic).

---

## Ground Truth: The Validation Framework

### What is Ground Truth?

**Ground Truth** in neoRAG refers to the authoritative set of rules, mappings, and constraints that define:
- **Valid entity types** and their canonical names
- **Valid properties** for each entity type
- **Valid relationships** between entity types
- **Required vs. optional** properties and relationships
- **Data transformation rules** (e.g., coordinate normalization, Wikidata mapping)
- **Validation constraints** (e.g., geographic bounds, administrative hierarchies)

The ground truth is implemented in `backend/utils/constants.py` and serves as the **single source of truth** for all validation logic.

### Why Ground Truth Matters

Without ground truth, an LLM might:
- Extract entities with inconsistent naming ("Author" vs "Autor" vs "Writer")
- Create invalid relationships (e.g., a "Municipi" located in another "Municipi" instead of a "Comarca")
- Use incorrect property names or missing required properties
- Generate data that doesn't conform to the CELIRU ontology or Wikidata standards

Ground truth ensures that **all extracted data conforms to the domain ontology** before it enters the knowledge graph.

---

## Components of Ground Truth

### 1. Canonical Node Types (`CANONICAL_NODE_TYPES`)

Defines the complete list of valid entity types in the system:

```python
CANONICAL_NODE_TYPES = [
    # Base ontology types
    'Person', 'Document', 'Entity', 'Organization', 'Location', 'Site', 'Event', 'Concept',
    
    # CELIRU-specific types
    'LibroPresentado', 'LibroPublicado', 'Autor', 'Coleccion', 'Lector', 
    'Importador', 'Editor', 'ProveedorDePapel', 'InformeDeLector', 'InformeLector',
    'SolicitudDeImportacion', 'SolicitudDePublicacion', 'SolicitudDeTraduccion', 
    'SolicitudDeCirculacion', 'ExpedienteCensura',
    'Formulario0', 'Formulario1', 'Formulario2', 'Formulario3', 'Formulario4', 'Formulario5',
    
    # Geographic types
    'Municipi', 'Comarca', 'Provincia', 'Country', 'City', 'Place', 'Region',
    'Comunitat autònoma', 'País',
    
    # Historical types
    'Brigadista', 'Brigade', 'Company', 'Division', 'Column', 'Military Unit',
    'fossa comú', 'Fossa Comuna', 'Mass Grave Site', 'Cemetery', 'Prison',
    'Historical Event', 'Political Party', 'Profession'
]
```

**Purpose**: Any entity type extracted by the LLM must either be in this list or be mapped to a canonical type via `TYPE_ALIAS_MAP`.

---

### 2. Type Alias Mapping (`TYPE_ALIAS_MAP`)

Maps common variations and aliases to canonical types:

```python
TYPE_ALIAS_MAP = {
    # Author variations
    'author': 'Autor',
    'writer': 'Autor',
    'escritor': 'Autor',
    
    # Book variations
    'book': 'LibroPublicado',
    'published_book': 'LibroPublicado',
    'libro': 'LibroPublicado',
    'presented_book': 'LibroPresentado',
    'libro_presentado': 'LibroPresentado',
    
    # Editorial roles
    'editor': 'Editor',
    'reader': 'Lector',
    'importer': 'Importador',
    
    # Documents and reports
    'reader_report': 'InformeLector',
    'informe': 'InformeLector',
    'expedient': 'ExpedienteCensura',
    'expediente': 'ExpedienteCensura',
    
    # Geographic variations
    'coordinates': 'Coordinates',
    'fossa comuna': 'Fossa Comuna',
    'fossa comú': 'Fossa Comuna',
    'comunitat autònoma': 'Comunitat autònoma',
    
    # ... (many more mappings)
}
```

**Purpose**: Normalizes entity types extracted by the LLM to canonical forms, ensuring consistency regardless of how the LLM names them.

---

### 3. Ontological Property Map (`ONTOLOGICAL_PROPERTY_MAP`)

Defines valid properties for each entity type and maps them to standardized names:

```python
ONTOLOGICAL_PROPERTY_MAP = {
    'ExpedienteCensura': {
        'idExpediente': 'file_id',
        'titulo': 'title',
        'paisDeOrigen': 'country_of_origin',
        'idColeccion': 'collection_id'
    },
    'LibroPresentado': {
        'titulo': 'title',
        'autor': 'author',
        'fechaPresentacion': 'presentation_date'
    },
    'LibroPublicado': {
        'titulo': 'title',
        'autor': 'author',
        'fechaPublicacion': 'publication_date',
        'idAutor': 'author_id',
        'idColeccion': 'collection_id'
    },
    'Autor': {
        'nombre': 'name',
        'nacionalidad': 'nationality'
    },
    # ... (many more entity types)
}
```

**Purpose**: 
- Validates that extracted properties are valid for each entity type
- Maps Spanish property names to English equivalents (or vice versa)
- Ensures property names conform to the CELIRU ontology

---

### 4. Ontological Transformation Rules (`ONTOLOGICAL_TRANSFORMATION_RULES`)

Defines how database schema elements map to ontological constructs:

```python
ONTOLOGICAL_TRANSFORMATION_RULES = {
    'PRIMARY_KEY': {
        'rule_type': 'class_identifier',
        'description': 'Primary keys are used as class identifiers',
        'properties': ['idExpediente', 'idLibroPublicado', 'idLibroPresentado', ...]
    },
    'FOREIGN_KEY': {
        'rule_type': 'object_property',
        'description': 'Foreign keys become object properties',
        'properties': ['idColeccion', 'idAutor']
    },
    'ASSOCIATIVE_TABLE': {
        'rule_type': 'inverse_object_property',
        'description': 'Foreign keys in associative tables become inverse object properties',
        'tables': ['AUTOR_LIBROS_PUBLICADOS']
    },
    'REGULAR_ATTRIBUTE': {
        'rule_type': 'datatype_property',
        'description': 'Regular attributes become datatype properties',
        'properties': ['titulo', 'paisDeOrigen']
    }
}
```

**Purpose**: Guides transformation of SQL/relational data into ontological structures (entities, properties, relationships).

---

### 5. Ontological Inference Rules (`ONTOLOGICAL_INFERENCE_RULES`)

Defines inverse relationships, functional properties, and property chains:

```python
ONTOLOGICAL_INFERENCE_RULES = {
    'INVERSE_PROPERTIES': {
        'DA_COMO_RESULTADO': {
            'inverse': 'RESULTA_DE',
            'domain': 'ExpedienteCensura',
            'range': 'LibroPublicado',
            'properties': ['fecha_resolucion', 'tipo_resolucion']
        },
        'TIENE_OBJETO_CENSURA': {
            'inverse': 'ES_CENSURADO_EN',
            'domain': 'ExpedienteCensura',
            'range': 'LibroPresentado',
            'properties': ['fecha_presentacion']
        },
        'REDACTA': {
            'inverse': 'ES_REDACTADO_POR',
            'domain': 'Lector',
            'range': 'InformeLector',
            'properties': ['fecha_redaccion', 'tipo_formulario']
        },
        # ... (many more relationships)
    },
    'FUNCTIONAL_PROPERTIES': [
        'IDENTIFIER',
        'PRIMARY_TITLE',
        'RESOLUTION_TYPE',
        'FORM_TYPE'
    ],
    'PROPERTY_CHAINS': {
        'expediente_resolucion': {
            'chain': ['DA_COMO_RESULTADO', 'resolucion'],
            'domain': 'ExpedienteCensura',
            'range': 'xsd:string'
        }
    }
}
```

**Purpose**:
- **Inverse Properties**: Automatically creates bidirectional relationships (e.g., if A `AUTHORED` B, then B `AUTHORED_BY` A)
- **Functional Properties**: Ensures properties like `IDENTIFIER` have unique values
- **Property Chains**: Enables querying across relationships (e.g., get resolution of an expediente through its relationship to a libro)

---

### 6. Relationship Rules (`RELATIONSHIP_RULES`)

Defines required, functional, and optional relationships for each entity type:

```python
RELATIONSHIP_RULES = {
    'ExpedienteCensura': {
        'required_relationships': ['TIENE_OBJETO_CENSURA'],
        'functional_relationships': ['DA_COMO_RESULTADO'],
        'optional_relationships': ['CONTIENE_INFORME']
    },
    'InformeLector': {
        'required_relationships': ['ES_REDACTADO_POR', 'ELABORADO_MEDIANTE'],
        'functional_relationships': ['FORMA_PARTE_DE'],
        'optional_relationships': []
    },
    'LibroPresentado': {
        'required_relationships': ['ES_CENSURADO_EN'],
        'functional_relationships': ['IDENTIFIER', 'PRIMARY_TITLE'],
        'optional_relationships': ['RELATED_TO']
    },
    # ... (many more entity types)
}
```

**Purpose**:
- **Required relationships**: Must exist for an entity to be valid (e.g., every `LibroPresentado` must be `ES_CENSURADO_EN` an `ExpedienteCensura`)
- **Functional relationships**: Must be unique (e.g., each `ExpedienteCensura` can only have one `DA_COMO_RESULTADO`)
- **Optional relationships**: May exist but are not required

---

### 7. Administrative Hierarchy (`ADMINISTRATIVE_HIERARCHY`)

Defines the geographic administrative hierarchy for validation:

```python
ADMINISTRATIVE_HIERARCHY = {
    'municipio': {
        'level': 0,
        'parent': 'comarca'
    },
    'comarca': {
        'level': 1,
        'parent': 'provincia'
    },
    'provincia': {
        'level': 2,
        'parent': 'comunidad_autonoma'
    },
    'comunidad_autonoma': {
        'level': 3,
        'parent': 'pais'
    },
    'pais': {
        'level': 4,
        'parent': None
    }
}
```

**Purpose**: Validates that geographic relationships respect the hierarchy (e.g., a `Municipi` can only be `LOCATED_IN` a `Comarca`, not another `Municipi`).

---

### 8. Wikidata Property Mapping

Maps Wikidata property codes (P-codes) and entity codes (Q-codes) for interoperability:

```python
# In RelationshipValidator class
self.wikidata_properties = {
    "P625": "coordinate_location",
    "P131": "located_in_administrative_territorial_entity",
    "P17": "country",
    "P1552": "has_quality",
    "P527": "has_part",
    "P1542": "has_cause",
    "P2046": "area"
}

self.controlled_values = {
    "P1552": {  # has_quality
        "Confirmada": "Q5727902",
        "Probable": "Q24574780",
        "Es desconeix": "Q24574781",
        "Existent": "Q56661804",
        "Desapareguda": "Q7240364",
        "Parcialment destruïda": "Q26884324"
    },
    # ... (more controlled vocabularies)
}
```

**Purpose**: Ensures extracted data can be exported to Wikidata format and validated against Wikidata schemas.

---

### 9. Coordinate Validation

Validates geographic coordinates are within valid bounds:

```python
# In RelationshipValidator.validate_wikidata_properties()
if "latitud" in properties and "longitud" in properties:
    lat = float(properties["latitud"])
    lon = float(properties["longitud"])
    if not (35.0 <= lat <= 44.0 and -9.0 <= lon <= 4.0):
        errors.append(f"Coordenadas fuera de rango para España: {lat}, {lon}")
```

**Purpose**: Ensures coordinates are within the Iberian Peninsula bounds (35-44°N, -9-4°W).

---

## Structured Prompt: The Neural-Symbolic Bridge

### What is the Structured Prompt?

The **Structured Prompt** (`EXTRACTION_PROMPT` in `backend/core/prompts/prompts.py`) is a comprehensive set of instructions given to Google Gemini LLM that guides it to extract entities and relationships according to the ground truth rules.

The prompt serves as a **neural-symbolic bridge** because it:
1. **Encodes ground truth rules** into natural language instructions
2. **Guides the LLM** to follow ontological constraints during extraction
3. **Specifies output format** (JSON with nodes and relationships)
4. **Handles multiple data sources** (RDF, CSV, SQL, web content)

### Key Characteristics

1. **Template-based**: Uses placeholders (`{custom_extraction_rules}`, `{custom_relationship_instructions}`, etc.) for customization
2. **Source-aware**: Provides specific instructions for different data source types (RDF/Dublin Core, CSV, SQL)
3. **Ontology-aware**: Includes detailed entity type definitions and relationship types from CELIRU
4. **Format-specific**: Specifies exact JSON output structure

---

## How Ground Truth and Prompt Work Together

### The Extraction Pipeline

```
┌─────────────────┐
│  Raw Data       │  (CSV, RDF, SQL, Web)
│  (Text Chunk)   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  STRUCTURED PROMPT                   │
│  (Neural Layer)                      │
│  - Instructs LLM to extract          │
│  - References ground truth rules     │
│  - Specifies output format           │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  LLM (Google Gemini)                │
│  - Extracts entities & relationships│
│  - Returns JSON                     │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  GROUND TRUTH VALIDATION             │
│  (Symbolic Layer)                    │
│  - Type normalization (TYPE_ALIAS)  │
│  - Property validation (PROPERTY_MAP)│
│  - Relationship validation (RULES)    │
│  - Coordinate bounds checking        │
│  - Administrative hierarchy check    │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  Validated Graph Document            │
│  (Ready for Neo4j)                  │
└─────────────────────────────────────┘
```

### Step-by-Step Flow

1. **Prompt Customization** (`get_customized_prompt()`):
   - Loads configuration from `prompt_config.json`
   - Injects ground truth rules into prompt placeholders
   - Includes canonical node types, relationship types, and extraction rules

2. **LLM Extraction**:
   - LLM receives the structured prompt + text chunk
   - LLM extracts entities and relationships following prompt instructions
   - LLM returns JSON with `nodes` and `relationships`

3. **Type Normalization** (`normalize_type_name()`):
   - Uses `TYPE_ALIAS_MAP` to convert LLM-extracted types to canonical forms
   - Example: "author" → "Autor", "book" → "LibroPublicado"

4. **Property Validation** (`validate_properties()`):
   - Uses `ONTOLOGICAL_PROPERTY_MAP` to validate and map properties
   - Removes invalid properties
   - Maps Spanish ↔ English property names

5. **Relationship Validation** (`RelationshipValidator`):
   - Validates relationship types against `RELATIONSHIP_RULES`
   - Checks domain/range constraints (e.g., `AUTHORED` can only connect `Autor` → `LibroPublicado`)
   - Validates administrative hierarchy for geographic relationships

6. **Inverse Relationship Creation** (`create_inverse_relationship()`):
   - Uses `ONTOLOGICAL_INFERENCE_RULES['INVERSE_PROPERTIES']` to create bidirectional relationships
   - Example: If A `AUTHORED` B, creates B `AUTHORED_BY` A

7. **Coordinate Validation**:
   - Checks coordinates are within Iberian Peninsula bounds (35-44°N, -9-4°W)
   - Validates administrative hierarchy for location relationships

8. **Wikidata Normalization** (`normalize_to_wikidata()`):
   - Maps properties to Wikidata P-codes
   - Maps controlled values to Wikidata Q-codes
   - Ensures interoperability with global Linked Open Data

---

## Complete Structured Prompt

The following is the complete `EXTRACTION_PROMPT` as defined in `backend/core/prompts/prompts.py`:

```python
EXTRACTION_PROMPT = """You are an expert knowledge graph builder specializing in extracting structured information from various data sources including RDF files (Dublin Core metadata), CSV files (tabular geographic/historical data), and SQL records.

Your task is to extract entities and relationships that represent the real-world semantic connections in the data.

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

1. Analyze and detect presence of Dublin Core metadata patterns (dc:title, dc:creator, dc:type, dc:subject, etc.)
2. Identify real-world entities like People, Documents, Organizations, Locations, and Concepts
3. Create meaningful relationships that represent the actual semantic connections
4. For Dublin Core records about people (like brigadistas), distinguish between:
   - The PERSON mentioned in the record (e.g., the brigadista)
   - The DOCUMENT/RECORD itself (metadata about that person)
   - The CREATOR/AUTHOR of the record
5. Preserve original identifiers and terminology for consistency
6. Create rich cross-references between related entities
7. For biographical/historical records, focus on comprehensive relationship types
8.**Geographic Data Handling**: For CSV data with coordinates and location hierarchies:
   - Create Location entities for each geographic level (Municipi, Comarca, Província, País)
   - Use coordinates (Latitud, Longitud) as location properties
   - Create LOCATED_IN relationships between location levels
   - Link main entities (fosses, sites, people) to their geographic locations

## Custom Extraction Rules
{custom_relationship_instructions}

## Entity Focus
Focus primarily on these entity types: {custom_entity_focus}

## Entity Types

- **Person**: Individual people mentioned in records (brigadistas, authors, historical figures)
  - Properties: full_name, role, date_of_birth, occupation, nationality, military_unit
- **Document**: Metadata records, publications, written works, historical records
  - Properties: title, content_type, creation_date, author, identifier, subject_area
- **Organization**: Companies, institutions, military units, political groups
  - Properties: name, type, founding_date, location, role, historical_context
- **Location**: Physical places, countries, regions, sites, coordinates
  - Properties: name, type, coordinates, latitude, longitude, country, administrative_level, historical_context
- **Site**: Specific historical sites, monuments, fosses, archaeological locations
  - Properties: name, type, status, conservation_state, municipality, coordinates, historical_period
- **Concept**: Abstract ideas, themes, historical periods, topics
  - Properties: name, description, domain, historical_period, significance
- **Event**: Historical events, battles, campaigns, political milestones
  - Properties: name, date, location, description, participants, historical_impact

## Ontological Entity Types

- **LibroPresentado**: Books presented in events or conferences
  - Properties: titulo (title), autor (author), fechaPresentacion (presentation_date)
  - Relationships: AUTHORED_BY -> Autor, PRESENTED_AT -> Event
  
- **LibroPublicado**: Published books
  - Properties: titulo (title), autor (author), fechaPublicacion (publication_date)
  - Relationships: AUTHORED_BY -> Autor, PUBLISHED_BY -> Organization
  
- **Autor**: Book authors and writers
  - Properties: nombre (name), nacionalidad (nationality)
  - Relationships: AUTHORED -> LibroPresentado/LibroPublicado, MEMBER_OF -> Organization

- **Coleccion**: Collections of published works
  - Properties: nombre (name), descripcion (description), idColeccion (collection_id)
  - Relationships: CONTAINS -> LibroPublicado, MANAGED_BY -> Editor

- **Lector**: Readers who review works
  - Properties: nombre (name), idLector (reader_id)
  - Relationships: REVIEWS -> LibroPublicado, CREATES -> InformeDeLector

- **Editor**: Publishing editors
  - Properties: nombre (name), idEditor (editor_id)
  - Relationships: PUBLISHES -> LibroPublicado, MANAGES -> Coleccion, WORKS_WITH -> ProveedorDePapel

- **Importador**: Book importers
  - Properties: nombre (name), idImportador (importer_id)
  - Relationships: IMPORTS -> LibroPublicado

- **ProveedorDePapel**: Paper suppliers
  - Properties: nombre (name), idProveedor (supplier_id)
  - Relationships: SUPPLIES -> Editor

- **InformeDeLector**: Reader reports
  - Properties: idInforme (report_id), idExpediente (file_id), fecha (date)
  - Relationships: CREATED_BY -> Lector, REFERS_TO -> LibroPublicado

- **SolicitudDeTraduccion**: Translation requests
  - Properties: idSolicitudTraduccion (request_id), tirada (print_run), extension (pages_volumes), formato (format), caracter (character), claseDeImpreso (print_class), matizPolitico (political_nuance), fechaPresentacion (presentation_date), observaciones (observations)
  - Relationships: TIENE_EDITOR_SOLICITANTE_TRADUCCION -> Editor, FORMA_PARTE_DE_EXPEDIENTE -> ExpedienteCensura

- **SolicitudDeCirculacion**: Circulation requests
  - Properties: idSolicitudCirculacion (request_id), tirada (print_run), extension (pages_volumes), formato (format), caracter (character), fechaEntrada (entry_date), fechaSalida (exit_date), fechaEdicion (edition_date), resolucion (resolution), matizPolitico (political_nuance)
  - Relationships: TIENE_EDITOR_SOLICITANTE_CIRCULACION -> Editor, FORMA_PARTE_DE_EXPEDIENTE -> ExpedienteCensura

- **Formulario0**: Pre-1939 reader evaluation forms
  - Properties: idFormulario0 (form_id), comentario (comment)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

- **Formulario1**: Post-1939 reader evaluation forms
  - Properties: idFormulario1 (form_id), valorLiterarioOArtistico (literary_artistic_value), valorDocumental (documentary_value), matizPolitico (political_nuance), otrasObservaciones (other_observations)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

- **Formulario2**: Censorship evaluation forms (Type 2)
  - Properties: idFormulario2 (form_id), atacaAlDogmaOALaMoral (attacks_dogma_or_morals), atacaALasInstitucionesDelRegimen (attacks_regime_institutions), tieneValorLiterarioODocumental (has_literary_documentary_value), razonesCircunstanciales (circumstantial_reasons)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

- **Formulario3**: Detailed censorship evaluation forms
  - Properties: idFormulario3 (form_id), atacaAlDogma (attacks_dogma), atacaALaIglesia (attacks_church), atacaASusMinistros (attacks_ministers), atacaALaMoral (attacks_morals), atacaAlRegimenYASusInstituciones (attacks_regime_institutions), atacaALasPersonasQueColaboranOHanColaboradoConElRegimen (attacks_regime_collaborators), resultando (resulting)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

- **Formulario4**: Circulation request evaluation forms
  - Properties: idFormulario4 (form_id), valorLiterario (literary_value), valorDocumental (documentary_value), matizPolitico (political_nuance), tachaduras (corrections), otrasObservaciones (other_observations)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

- **Formulario5**: Translation request evaluation forms
  - Properties: idFormulario5 (form_id), atacaAlDogmaOALaMoral (attacks_dogma_or_morals), atacaALasInstitucionesDelRegimen (attacks_regime_institutions), tieneValorLiterarioODocumental (has_literary_documentary_value), razonesCircunstanciales (circumstantial_reasons), observaciones (observations)
  - Relationships: ES_FORMULARIO_DE_INFORME -> InformeLector

## Ontological Rules

1. When processing RDF data:
   - Check for owl:Class definitions to identify entity types
   - Map owl:DatatypeProperty to appropriate node properties
   - Preserve original property names but normalize values

2. For table transformations:
   - Non-associative tables become ontological classes
   - Foreign keys become relationships
   - Non-key attributes become DatatypeProperties

3. Special handling for book-related entities:
   - LibroPresentado and LibroPublicado are distinct types
   - Maintain relationships with Autor entities
   - Track presentation and publication dates separately

4. Collection and Editorial Process:
   - Collections group published works
   - Track editorial workflow through relationships
   - Maintain paper supplier connections
   - Link reader reports to specific works

5. Relationship Rules:
   - Books must belong to at least one collection
   - Reader reports must link to both reader and book
   - Editors can manage multiple collections
   - Track all supply chain relationships

## Enhanced Relationship Types

### PRIORITIZED RELATIONSHIPS
Focus especially on these relationship types: {enabled_relationship_types}

### Geographic Relationships
- **LOCATED_IN**: A site, person, organization, or event is geographically located within a place
- **CONTAINS**: A larger geographic area contains a smaller one (País CONTAINS Província)
- **COORDINATES_AT**: An entity has specific geographic coordinates
- **BORDERS**: Two geographic areas share a border
- **ADMINISTRATIVE_DIVISION_OF**: Administrative relationship between location levels

### Document-Level Relationships
- **DOCUMENTS**: A record/document describes or documents a person's life/activities
- **AUTHORED**: A person creates, writes, or authors a document/record  
- **MENTIONS**: A document/record mentions or references a person, place, concept, or event
- **REFERENCES**: A document cites or refers to another document
- **CONTAINS_INFORMATION_ABOUT**: A document contains detailed information about a topic/person

### Personal & Social Relationships  
- **BELONGS_TO**: A person belongs to an organization, military unit, or group
- **MEMBER_OF**: A person is a member of an organization or collective
- **SERVED_IN**: A person served in a military unit or organization
- **AFFILIATED_WITH**: A person has professional or ideological affiliation

### Temporal Relationships
- **BORN_IN**: A person was born in a specific location
- **DIED_IN**: A person died in a specific location
- **ACTIVE_IN**: A person was active in a particular location or region
- **OCCURRED_IN**: An event took place in a specific location or time period

### Thematic & Conceptual Relationships
- **RELATED_TO**: General thematic relationship between concepts, topics, or entities
- **ASSOCIATED_WITH**: An entity is associated with a concept, theme, or topic
- **PARTICIPATED_IN**: A person participated in an event, campaign, or activity
- **INVOLVED_IN**: A person was involved in a historical event or movement

### Cross-Document Relationships
- **SAME_PERSON_AS**: Links the same person mentioned across different documents
- **CONTEMPORARY_OF**: People who lived or were active during the same time period
- **COLLEAGUE_OF**: People who worked together or shared professional connections

## Geographic Data Interpretation Guidelines
### Coordinate Columns (Latitud, Longitud, lat, lon, latitude, longitude):
- Create Location entities with coordinate properties
- Use coordinates for precise geographic positioning
- Link sites/entities to their coordinate locations with COORDINATES_AT

### Hierarchical Location Columns:
- **País → Comunitat autònoma → Província → Comarca → Municipi**
- Create separate Location entities for each level
- Create LOCATED_IN relationships: Municipi LOCATED_IN Comarca LOCATED_IN Província etc.
- Link main entities (sites, fosses) to their most specific location (usually Municipi)

### Site-Specific Data (Fosses Comunes example):
- Main entity: Site (fossa comú) with properties like status, conservation, type
- Geographic linking: Site LOCATED_IN Municipi
- Coordinate linking: Site COORDINATES_AT Location(coordinates)

### Column Pattern Recognition:
- **ID columns**: Use for entity identifiers
- **Title/Name columns**: Primary entity names
- **Category/Type columns**: Entity classification
- **Status/State columns**: Current condition properties
- **URL/Link columns**: External reference properties

## Dublin Core Interpretation Guidelines

When you see Dublin Core patterns like:
- dc:title = "PERSON NAME" + dc:type = "Brigadista" → Create Person entity + Document entity
- dc:creator = "AUTHOR" → Create Person entity for author + AUTHORED relationship  
- dc:subject or dc:coverage → Extract as concepts/locations with MENTIONS, ASSOCIATED_WITH relationships

## Output Format

Return a JSON object with the following structure:

```
{
    "nodes":[
         {
             "id":"unique_identifier",
             "type":"Person|Document|Organization|Location|Site|Concept|Event",
             "properties":
               {
                   "property1":"value1",
                   "property2":"value2",
                   "latitude": 41.5933, // Important: locations with coordinates
                   "longitude": 2.4003  // Important: locations with coordinates
                }
            }
            ],
      "relationships":[
         {
               "source":"source_entity_id",
               "target":"target_entity_id",
               "type":"LOCATED_IN|COORDINATES_AT|CONTAINS|DOCUMENTS|BELONGS_TO|PARTICIPATED_IN|etc",
               "properties":{
                     "context":"specific_context",
                     "confidence":"high|medium|low",
                     "source_document":"document_identifier"
                  }
         }
      ]
   }
```

## Important Guidelines

- **For Geographic Data**: Always create location hierarchies and coordinate-based relationships
- **Coordinate Handling**: When latitude/longitude columns exist, create Location entities with these coordinates
- **Administrative Hierarchies**: Create nested LOCATED_IN relationships for geographic administrative levels
- **Site Recognition**: Recognize historical sites, monuments, fosses as specific Site entities
- **Cross-Document Linking**: Use consistent IDs for same entities across different sources
- **Confidence Levels**: Add confidence and context to relationships for quality tracking

"""
```

---

## Validation Pipeline Flow

### Detailed Validation Steps

1. **Initial Extraction** (`extractGraph()` in `backend/graph/extraction.py`):
   - Receives text chunk and customized prompt
   - Calls LLM with prompt + text
   - Parses JSON response into `GraphDocument` (nodes + relationships)

2. **Type Normalization**:
   ```python
   normalized_type = normalize_type_name(node.type)
   # Uses TYPE_ALIAS_MAP to convert "author" → "Autor"
   ```

3. **Property Validation**:
   ```python
   validated_props = validate_properties(node.type, node.properties)
   # Uses ONTOLOGICAL_PROPERTY_MAP to validate and map properties
   ```

4. **ID Normalization**:
   ```python
   normalized_id = normalize_id(node.id, node.type)
   # Ensures IDs are unique and follow naming conventions
   ```

5. **Relationship Type Validation**:
   ```python
   if relationship_validator.validate_relationship_type(rel.type):
       # Relationship type is valid
   ```

6. **Domain/Range Validation**:
   ```python
   # Checks if relationship can connect source_type → target_type
   # Uses ONTOLOGICAL_INFERENCE_RULES['INVERSE_PROPERTIES']
   ```

7. **Administrative Hierarchy Validation**:
   ```python
   if relationship_validator.validate_administrative_hierarchy(source_type, target_type):
       # Geographic relationship respects hierarchy
   ```

8. **Coordinate Validation**:
   ```python
   is_valid, errors = relationship_validator.validate_wikidata_properties(properties)
   # Checks coordinates are within 35-44°N, -9-4°W
   ```

9. **Inverse Relationship Creation**:
   ```python
   inverse_rel = create_inverse_relationship(relationship)
   # Creates bidirectional relationship if defined in ONTOLOGICAL_INFERENCE_RULES
   ```

10. **Ontological Transformation** (`_apply_ontological_rules()` in `writer.py`):
    - Applies primary key rules
    - Applies foreign key rules
    - Applies coordinate combining
    - Applies Wikidata property mapping

11. **Final Validation** (`validate_ontological_relationships()`):
    - Ensures required relationships exist
    - Validates bidirectional relationships are symmetric
    - Checks functional relationship uniqueness

---

## Summary

**Ground Truth** and **Structured Prompt** work together to ensure high-quality knowledge graph extraction:

- **Ground Truth** provides the authoritative rules and constraints that define what is valid
- **Structured Prompt** encodes these rules into instructions for the LLM
- **LLM** performs intelligent extraction following the prompt
- **Validation Pipeline** enforces ground truth rules on LLM output
- **Result**: Consistent, validated, ontology-compliant knowledge graph data

This neurosymbolic approach combines the flexibility of neural language models with the precision and consistency of symbolic validation rules, ensuring that extracted data is both semantically rich and structurally correct.

