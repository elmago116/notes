---
tags:
  - op/doc/reporte
authors:
  - Matheus Jenevain
date: 2026-01-29
---

# 🧠 neoRAG Ontology Architecture Guide

## How CELIRU, Wikidata, and Knowledge Graphs Work Together

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Neurosymbolic AI Architecture](#neurosymbolic-ai-architecture)
3. [The Role of Prompts](#the-role-of-prompts)
4. [How Answers Are Generated](#how-answers-are-generated)
5. [The Three Ontology Layers](#the-three-ontology-layers)
6. [CELIRU Ontology](#celiru-ontology)
7. [Wikidata Integration](#wikidata-integration)
8. [Knowledge Graph Structure](#knowledge-graph-structure)
9. [Data Flow](#data-flow)
10. [Validation Pipeline](#validation-pipeline)
11. [Code Reference](#code-reference)

---

## Overview

> **Summary:** neoRAG is a neurosymbolic knowledge management system that processes heterogeneous historical data (CSV, RDF, SQL, web sources), extracts structured information using Large Language Models, validates it against domain-specific ontological rules, and stores it in a graph database. Users can query the system using natural language and receive accurate, source-referenced answers. The architecture combines neural language understanding with symbolic rule-based validation to ensure both flexibility in data processing and consistency in data quality.

neoRAG uses a **multi-layered ontology architecture** that combines:

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER DATA INPUT                             │
│              (CSV, RDF, SQL?, Web Scraping ?)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   NEURAL PROCESSING                             │
│                   (Google Gemini Flash LLM)                     │
│         Extracts entities & relationships from text             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│               SYMBOLIC VALIDATION LAYER                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   CELIRU    │  │  Wikidata   │  │  Domain     │              │
│  │  Ontology   │  │  Standards  │  │   Rules     │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE GRAPH                              │
│                       (Neo4j)                                   │
│            Nodes + Relationships + Properties                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Neurosymbolic AI Architecture

> **Summary:** Neurosymbolic AI represents the core architectural principle of neoRAG, integrating a neural component (Google Gemini LLM) for natural language understanding with a symbolic component (CELIRU ontology and validation rules) for logical consistency enforcement. The neural layer processes unstructured text and extracts candidate entities and relationships. The symbolic layer then validates these extractions against domain rules, checking type validity, required properties, and relationship constraints. This hybrid approach addresses the limitations of each paradigm individually: pure neural systems lack consistency guarantees and may generate unfounded assertions, while pure symbolic systems require perfectly structured input and cannot handle linguistic variation.

### What is Neurosymbolic AI?

**Neurosymbolic AI** combines two complementary approaches:

| Component | What it does | Technology in neoRAG |
|-----------|--------------|---------------------|
| **Neural** | "Understands" natural language, extracts meaning from unstructured text | Google Gemini LLM |
| **Symbolic** | Applies rules, validates structure, ensures logical consistency | CELIRU ontology + validation rules |

### Why Both?

```
┌─────────────────────────────────────────────────────────────────┐
│                     NEURAL ALONE (LLM)                          │
│  ✓ Great at understanding text                                  │
│  ✓ Can extract entities from messy data                         │
│  ✗ May hallucinate (invent) facts                               │
│  ✗ No consistency guarantees                                    │
│  ✗ Can't enforce domain rules                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   SYMBOLIC ALONE (Rules)                        │
│  ✓ Perfect consistency                                          │
│  ✓ Enforces all domain rules                                    │
│  ✗ Can't understand natural language                            │
│  ✗ Requires perfectly structured input                          │
│  ✗ Brittle - breaks with unexpected data                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   NEUROSYMBOLIC (Both)                          │
│  ✓ Understands messy, natural language data                     │
│  ✓ Extracts entities intelligently                              │
│  ✓ Validates against domain rules                               │
│  ✓ Ensures logical consistency                                  │
│  ✓ Prevents hallucinations through validation                   │
│  ✓ Flexible input, reliable output                              │
└─────────────────────────────────────────────────────────────────┘
```

### How neoRAG Implements Neurosymbolic AI

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  INPUT DATA (CSV, RDF, SQL, Web)                                │
│                                                                 │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              NEURAL LAYER (Gemini LLM)                  │    │
│  │  ─────────────────────────────────────────────────────  │    │
│  │  • Receives structured EXTRACTION_PROMPT                │    │
│  │  • "Reads" and understands the data                     │    │
│  │  • Extracts entities: "This is a book by Cela"          │    │
│  │  • Identifies relationships: "Written by this author"   │    │ #op/acc/question 
│  │  • Outputs JSON with nodes + relationships              │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         │  (Raw extraction - may have errors)                   │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │             SYMBOLIC LAYER (Rules Engine)               │    │
│  │  ─────────────────────────────────────────────────────  │    │
│  │                                                         │    │
│  │  Step 1: TYPE NORMALIZATION                             │    │
│  │  ├─ "writer" → "Autor" (TYPE_ALIAS_MAP)                │    │
│  │  └─ Validate against CANONICAL_NODE_TYPES              │    │
│  │                                                         │    │
│  │  Step 2: PROPERTY VALIDATION                            │    │
│  │  ├─ Check required properties exist                     │    │
│  │  └─ Normalize names (ONTOLOGICAL_PROPERTY_MAP)         │    │
│  │                                                         │    │
│  │  Step 3: ID NORMALIZATION                               │    │
│  │  └─ Generate consistent IDs: autor_cela_spanish        │    │
│  │                                                         │    │
│  │  Step 4: RELATIONSHIP VALIDATION                        │    │
│  │  ├─ Check domain/range (Autor → LibroPublicado)        │    │
│  │  ├─ Validate required relationships exist               │    │
│  │  └─ Create inverse relationships automatically          │    │
│  │                                                         │    │
│  │  Step 5: WIKIDATA NORMALIZATION                         │    │
│  │  ├─ Coordinates → P625 format                           │    │
│  │  └─ Values → Q-codes                                    │    │
│  │                                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         │  (Validated, normalized data)                         │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  KNOWLEDGE GRAPH (Neo4j)                │    │
│  │  ─────────────────────────────────────────────────────  │    │
│  │  • Clean, consistent entities                           │    │
│  │  • Bidirectional relationships                          │    │
│  │  • Embeddings for semantic search                       │    │
│  │  • Ready for RAG queries                                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Key Files for Neurosymbolic Processing 

#op/acc/question 

| File            | Neural/Symbolic   | Role                                    |
| --------------- | ----------------- | --------------------------------------- |
| `extraction.py` | Neural → Symbolic | Calls LLM, then applies validation      |
| `prompts.py`    | Neural            | Structured prompt for entity extraction |
| `constants.py`  | Symbolic          | All rules and mappings                  |
| `relations.py`  | Symbolic          | Relationship validation logic           |
| `writer.py`     | Symbolic          | Final validation before Neo4j           |

---

## The Role of Prompts

> **Summary:** Prompts serve as structured instruction sets that guide the LLM's behavior in specific contexts. neoRAG employs two distinct prompts: 
(1) **EXTRACTION_PROMPT** provides comprehensive guidelines for entity and relationship extraction from ingested data, including entity type definitions, property specifications, relationship taxonomies, and output format requirements. 
(2) **QA_TEMPLATE** constrains the LLM during question answering to use only retrieved context, preventing hallucination and ensuring response traceability. The separation of concerns between extraction and retrieval allows each prompt to be optimized for its specific task while maintaining system coherence.

neoRAG uses **two distinct prompts** for different purposes:

### 1. EXTRACTION_PROMPT (prompts.py) - For Data Ingestion

**Purpose:** Guide the LLM to extract entities and relationships from raw data.

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTRACTION_PROMPT                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  "You are an expert knowledge graph builder..."                 │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  DATA SOURCE HANDLING                                   │    │
│  │  • IF RDF: analyze Dublin Core patterns                 │    │
│  │  • IF CSV: analyze columns, coordinates, hierarchies    │    │
│  │  • IF SQL: process INSERT statements, foreign keys      │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  CELIRU RULES (custom_extraction_rules)                 │    │
│  │  • Entidades: Brigadista, ExpedienteCensura, etc.       │    │
│  │  • Propiedades mínimas: nombre, nacionalidad...         │    │
│  │  • Relaciones: DA_COMO_RESULTADO, TIENE_OBJETO...       │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  ENTITY TYPES                                           │    │
│  │  • Generic: Person, Document, Location, Site, Event     │    │
│  │  • Ontological: LibroPresentado, Autor, Lector, etc.    │    │
│  │  • With properties and relationships defined            │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  RELATIONSHIP TYPES                                     │    │
│  │  • Geographic: LOCATED_IN, CONTAINS, COORDINATES_AT     │    │
│  │  • Document: DOCUMENTS, AUTHORED, MENTIONS              │    │
│  │  • Personal: BELONGS_TO, MEMBER_OF, SERVED_IN           │    │
│  │  • Temporal: BORN_IN, DIED_IN, OCCURRED_IN              │    │
│  │  • Cross-doc: SAME_PERSON_AS, CONTEMPORARY_OF           │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  OUTPUT FORMAT                                          │    │
│  │  Return JSON: { "nodes": [...], "relationships": [...]} │    │
│  │  Include: id, type, properties, confidence              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Used when:** Data is ingested (uploaded CSV, RDF, SQL files)

**Location:** `backend/core/prompts/prompts.py`

### 2. QA_TEMPLATE (graph_rag.py) - For Answering Questions

**Purpose:** Guide the LLM to answer user questions using retrieved context.

```
┌─────────────────────────────────────────────────────────────────┐
│                      QA_TEMPLATE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  "Eres un asistente experto en tareas de respuesta a           │
│   preguntas usando información contextual..."                   │
│                                                                 │
│  RULES:                                                         │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  1. Use ONLY the provided context                       │    │
│  │  2. Do NOT invent information                           │    │
│  │  3. If facts (dates, names, locations) → find them      │    │
│  │  4. If ambiguous → ask for clarification                │    │
│  │  5. Keep Catalan words in Catalan                       │    │
│  │  6. Respond in Catalan                                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  INPUT:                                                         │
│  • Pregunta: {question}     ← User's question                  │
│  • Contexto: {context}      ← Retrieved from knowledge graph   │
│                                                                 │
│  OUTPUT:                                                        │
│  • Respuesta: ← Grounded answer based on context               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Used when:** User asks a question in the chat

**Location:** `backend/rag/graph_rag.py`

### How Prompts Connect to the System

```
┌─────────────────────────────────────────────────────────────────┐
│                   DATA INGESTION FLOW                           │
│                                                                 │
│  User uploads file → loader.py → extraction.py                  │
│                                          │                      │
│                                          ▼                      │
│                              ┌───────────────────┐              │
│                              │ EXTRACTION_PROMPT │              │
│                              │  + custom rules   │  gemini? rag?            │
│                              │  + entity focus   │              │
│                              └─────────┬─────────┘              │
│                                        │                        │
│                                        ▼                        │
│                                    Gemini LLM                   │
│                                        │                        │
│                                        ▼                        │
│                              JSON (nodes, rels)                 │
│                                        │                        │
│                                        ▼                        │
│                              Symbolic Validation                │
│                                        │                        │
│                                        ▼                        │
│                                   Neo4j Graph                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   QUESTION ANSWERING FLOW                       │
│                                                                 │
│  User asks question → graph_rag.py                              │
│                              │                                  │
│                              ▼                                  │
│                   ┌───────────────────┐                         │
│                   │  Vector Search    │                         │
│                   │  (Embeddings)     │                         │
│                   └─────────┬─────────┘                         │
│                             │                                   │
│                             ▼                                   │
│                   Retrieved context                             │
│                             │                                   │
│                             ▼                                   │
│                   ┌───────────────────┐                         │
│                   │   QA_TEMPLATE     │                         │
│                   │   + question      │                         │
│                   │   + context       │                         │
│                   └─────────┬─────────┘                         │
│                             │                                   │
│                             ▼                                   │
│                        Gemini LLM                               │
│                             │                                   │
│                             ▼                                   │
│                     Answer to user                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## How Answers Are Generated

> **Summary:** Answer generation follows the Retrieval-Augmented Generation (RAG) paradigm, a 5-step process that grounds LLM responses in verified knowledge. First, the user query is converted to a vector embedding using the same model employed during data ingestion. Second, a similarity search retrieves relevant nodes from the Neo4j vector index. Third, retrieved entities are assembled into a textual context. Fourth, the QA_TEMPLATE combines the original question with this context and instructs the LLM to generate responses exclusively from the provided information. Fifth, all operations are logged to Langfuse for observability and quality assurance. This architecture ensures responses are traceable to source documents and prevents the generation of unfounded assertions.

### The RAG (Retrieval-Augmented Generation) Process

When a user asks a question, neoRAG uses a 4-step process:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  User Question: "¿Quién escribió La Colmena?"                   │
│                                                                 │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STEP 1: EMBEDDING                                      │    │
│  │  ─────────────────                                      │    │
│  │  • Convert question to vector (embedding)               │    │
│  │  • Same model used for storing data                     │    │
│  │  • Captures semantic meaning, not just keywords         │    │
│  │  • "escribió" ≈ "author" ≈ "written by"                │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STEP 2: RETRIEVAL (Vector Search)                      │    │
│  │  ────────────────────────────────                       │    │
│  │  • Search Neo4j vector index                            │    │
│  │  • Find nodes with similar embeddings                   │    │
│  │  • Return most relevant documents/entities              │    │
│  │                                                         │    │
│  │  Retrieved:                                             │    │
│  │  ├─ Node: LibroPublicado "La Colmena"                  │    │
│  │  ├─ Node: Autor "Camilo José Cela"                     │    │
│  │  └─ Relationship: AUTHORED_BY                           │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STEP 3: CONTEXT ASSEMBLY                               │    │
│  │  ────────────────────────                               │    │
│  │  • Combine retrieved nodes into text context            │    │
│  │  • Include relevant properties and relationships        │    │
│  │                                                         │    │
│  │  Context:                                               │    │
│  │  "LibroPublicado: La Colmena, publicado 1951,          │    │
│  │   AUTHORED_BY: Camilo José Cela, nacionalidad España"   │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STEP 4: GENERATION (LLM)                               │    │
│  │  ────────────────────────                               │    │
│  │  • Send QA_TEMPLATE + question + context to Gemini      │    │
│  │  • LLM generates answer ONLY from context               │    │
│  │  • Cannot hallucinate - must cite retrieved data        │    │
│  │                                                         │    │
│  │  Answer:                                                │    │
│  │  "La Colmena va ser escrita per Camilo José Cela,      │    │
│  │   autor espanyol. Va ser publicada l'any 1951."         │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  STEP 5: OBSERVABILITY (Langfuse)                       │    │
│  │  ─────────────────────────────                          │    │
│  │  • Log the question, context, and answer                │    │
│  │  • Track token usage and latency                        │    │
│  │  • Enable debugging and quality monitoring              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Code Flow: queryGraph() Function

```python
# backend/rag/graph_rag.py

def queryGraph(question: str, source_url: str = None) -> str:
    
    # 1. Get the vector store (Neo4j with embeddings)
    vector_store = getVectorRetriever()
    
    # 2. Get the RAG chain (prompt + LLM)
    chain_template, qa_llm = getRAGChain()
    
    # 3. Create retriever (with optional source filter)
    retriever = vector_store.as_retriever()
    
    # 4. Build the full chain
    full_chain = (
        {"context": retriever | format_docs,    # Retrieve & format
         "question": RunnablePassthrough()}     # Pass question through
        | chain_template                         # Apply QA_TEMPLATE
    )
    
    # 5. Invoke and get answer
    answer = full_chain.invoke(question)
    
    return answer
```

### Why This Architecture Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    ADVANTAGES OF RAG                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✓ GROUNDED ANSWERS                                             │
│    LLM can only use retrieved context, not training data        │
│    → Prevents hallucinations about your specific domain         │
│                                                                 │
│  ✓ UP-TO-DATE INFORMATION                                       │
│    Knowledge graph is updated when new data is ingested         │
│    → Answers reflect latest uploaded documents                  │
│                                                                 │
│  ✓ TRACEABLE SOURCES                                            │
│    Every answer comes from specific nodes in the graph          │
│    → Can verify and cite original sources                       │
│                                                                 │
│  ✓ DOMAIN-SPECIFIC                                              │
│    Only searches YOUR data, not general internet                │
│    → Focused, relevant answers for historical research          │
│                                                                 │
│  ✓ SEMANTIC UNDERSTANDING                                       │
│    Embeddings capture meaning, not just keywords                │
│    → "author" matches "escribió", "written by", etc.           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Complete System Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                    HOW EVERYTHING CONNECTS                      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  DATA INGESTION                          │    │
│  │                                                         │    │
│  │  File Upload → Loader → EXTRACTION_PROMPT → Gemini      │    │
│  │       │                                        │         │    │
│  │       │                                        ▼         │    │
│  │       │                              JSON (nodes, rels)  │    │
│  │       │                                        │         │    │
│  │       │                                        ▼         │    │
│  │       │           ┌────────────────────────────────┐     │    │
│  │       │           │     SYMBOLIC VALIDATION        │     │    │
│  │       │           │  • TYPE_ALIAS_MAP              │     │    │
│  │       │           │  • ONTOLOGICAL_PROPERTY_MAP    │     │    │
│  │       │           │  • RELATIONSHIP_RULES          │     │    │
│  │       │           │  • Wikidata normalization      │     │    │
│  │       │           └────────────────────────────────┘     │    │
│  │       │                                        │         │    │
│  │       └──────────────────────┬─────────────────┘         │    │
│  │                              │                           │    │
│  │                              ▼                           │    │
│  │                    ┌─────────────────┐                   │    │
│  │                    │   NEO4J GRAPH   │                   │    │
│  │                    │  + Embeddings   │                   │    │
│  │                    └────────┬────────┘                   │    │
│  │                             │                            │    │
│  └─────────────────────────────┼────────────────────────────┘    │
│                                │                                 │
│                                │ (stored knowledge)              │
│                                │                                 │
│  ┌─────────────────────────────┼────────────────────────────┐    │
│  │                  QUESTION ANSWERING                      │    │
│  │                             │                            │    │
│  │  User Question ─────────────┼─────────────────────────┐  │    │
│  │       │                     │                         │  │    │
│  │       ▼                     ▼                         │  │    │
│  │  ┌─────────┐         ┌─────────────┐                  │  │    │
│  │  │Embedding│◀────────│Vector Search│                  │  │    │
│  │  └────┬────┘         └──────┬──────┘                  │  │    │
│  │       │                     │                         │  │    │
│  │       │              Retrieved Context                │  │    │
│  │       │                     │                         │  │    │
│  │       │                     ▼                         │  │    │
│  │       │              ┌─────────────┐                  │  │    │
│  │       └─────────────▶│ QA_TEMPLATE │                  │  │    │
│  │                      │ + question  │                  │  │    │
│  │                      │ + context   │                  │  │    │
│  │                      └──────┬──────┘                  │  │    │
│  │                             │                         │  │    │
│  │                             ▼                         │  │    │
│  │                         Gemini LLM                    │  │    │
│  │                             │                         │  │    │
│  │                             ▼                         │  │    │
│  │                      Grounded Answer                  │  │    │
│  │                                                       │  │    │
│  └───────────────────────────────────────────────────────┘  │    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Three Ontology Layers

> **Summary:** The ontology architecture comprises three complementary layers, each addressing a distinct aspect of knowledge representation. **CELIRU** (domain ontology) defines the conceptual schema for historical censorship data, specifying valid entity types, their properties, and permissible relationships. **Wikidata** (interoperability standard) provides universal identifiers (P-codes for properties, Q-codes for entities) and standardized data formats, enabling integration with the global Linked Open Data ecosystem. **Domain Rules** (validation logic) implements quality constraints including type normalization, coordinate bounds checking, administrative hierarchy validation, and relationship cardinality enforcement. Together, these layers ensure data is semantically meaningful, globally interoperable, and internally consistent.

### Layer 1: CELIRU (Domain Ontology)
**Purpose:** Define historical censorship domain entities and relationships

| What it does | Example |
|--------------|---------|
| Entity types | `ExpedienteCensura`, `LibroPublicado`, `Lector` |
| Properties per type | Autor needs `nombre`, `nacionalidad` |
| Relationships | `TIENE_OBJETO_CENSURA`, `REDACTA` |
| Business rules | Every `InformeLector` must have a `Lector` |

### Layer 2: Wikidata (Interoperability Standard)
**Purpose:** Enable data exchange with global linked data

| What it does | Example |
|--------------|---------|
| Property codes | `P625` = coordinates, `P131` = located_in |
| Entity codes | `Q5727902` = "Confirmed" status |
| Data formats | Globe-coordinate format for locations |
| Namespaces | `wd:`, `wdt:` for RDF export |

### Layer 3: Domain Rules (Validation Logic)
**Purpose:** Ensure data quality and consistency

| What it does | Example |
|--------------|---------|
| Type normalization | "writer" → "Autor" |
| Coordinate validation | Must be within Spain (35-44°N) |
| Hierarchy validation | Municipi → Comarca → Província |
| Inverse relationships | Auto-create bidirectional links |

---

## CELIRU Ontology

> **Summary:** CELIRU (Censorship of Editing in the Iberian Romance Languages) is a domain-specific ontology designed to model the Spanish Francoist censorship apparatus (1939-1975). It defines a comprehensive entity taxonomy including censorship files (ExpedienteCensura), submitted manuscripts (LibroPresentado), approved publications (LibroPublicado), censors (Lector), and six historical evaluation form types (Formulario0-5). Each entity type specifies required properties (e.g., Autor requires nombre and nacionalidad) and mandatory relationships (e.g., InformeLector requires ES_REDACTADO_POR relationship to a Lector). The TYPE_ALIAS_MAP provides lexical normalization, mapping variant terms ("writer", "author", "escritor") to canonical types ("Autor"), ensuring consistent representation regardless of source data heterogeneity.

### What is CELIRU?

**CELIRU** = Censorship of Editing in the Iberian Romance Languages

It's an ontology designed to model the **Spanish Francoist censorship system (1939-1975)**, capturing:
- Books submitted for censorship
- Censorship files and reports
- Readers (censors) who evaluated books
- Evaluation forms with specific criteria
- Resolutions (approved, denied, modified)

### CELIRU Entity Hierarchy

```
                    ┌──────────────────┐
                    │ ExpedienteCensura │ (Censorship File)
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│LibroPresentado│   │ InformeLector │   │ Solicitud...  │
│(Submitted Book)   │(Reader Report)│   │  (Requests)   │
└───────┬───────┘   └───────┬───────┘   └───────────────┘
        │                   │
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│LibroPublicado │   │  Formulario   │
│(Published Book)   │ (0,1,2,3,4,5) │
└───────────────┘   └───────────────┘
```

### CELIRU Entity Types (constants.py)

```python
CANONICAL_NODE_TYPES = [
    # Core CELIRU entities
    'ExpedienteCensura',      # Censorship file
    'LibroPresentado',        # Book submitted for review
    'LibroPublicado',         # Book approved for publication
    'Autor',                  # Author
    'Lector',                 # Reader/Censor
    'Editor',                 # Publisher
    'Importador',             # Book importer
    'InformeLector',          # Reader's report
    'Coleccion',              # Book collection
    
    # Request types
    'SolicitudDeTraduccion',  # Translation request
    'SolicitudDeCirculacion', # Circulation request
    'SolicitudDeImportacion', # Import request
    'SolicitudDePublicacion', # Publication request
    
    # Evaluation forms (historical)
    'Formulario0',  # Pre-1939 (simple comment)
    'Formulario1',  # Literary/documentary value
    'Formulario2',  # Dogma/morals/regime attacks
    'Formulario3',  # Detailed attack categories
    'Formulario4',  # Circulation evaluation
    'Formulario5',  # Translation evaluation
    
    # Supporting entities
    'FirmaLector',           # Reader signature
    'TachaduraYEnmienda',    # Corrections/redactions
    'Idioma',                # Language
    'ProveedorDePapel'       # Paper supplier
]
```

### CELIRU Type Normalization (TYPE_ALIAS_MAP)

The system accepts multiple names for the same entity:

```python
TYPE_ALIAS_MAP = {
    # Author variations
    'author': 'Autor',
    'writer': 'Autor',
    'escritor': 'Autor',
    
    # Book variations
    'book': 'LibroPublicado',
    'libro': 'LibroPublicado',
    'published_book': 'LibroPublicado',
    'presented_book': 'LibroPresentado',
    
    # Report variations
    'reader_report': 'InformeLector',
    'informe': 'InformeLector',
    'report': 'InformeLector',
    
    # Form variations
    'formulario 1': 'Formulario1',
    'formulario_1': 'Formulario1',
    # ... etc
}
```

### CELIRU Property Mapping (ONTOLOGICAL_PROPERTY_MAP)

Each entity type has defined properties:

```python
ONTOLOGICAL_PROPERTY_MAP = {
    'Autor': {
        'nombre': 'name',
        'nacionalidad': 'nationality'
    },
    'LibroPublicado': {
        'titulo': 'title',
        'autor': 'author',
        'fechaPublicacion': 'publication_date',
        'idAutor': 'author_id',
        'idColeccion': 'collection_id'
    },
    'Formulario3': {
        'atacaAlDogma': 'attacks_dogma',
        'atacaALaIglesia': 'attacks_church',
        'atacaASusMinistros': 'attacks_ministers',
        'atacaALaMoral': 'attacks_morals',
        'atacaAlRegimenYASusInstituciones': 'attacks_regime_institutions',
        # ...
    }
}
```

### CELIRU Relationship Rules (RELATIONSHIP_RULES)

Defines required, functional, and optional relationships:

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
    }
}
```

### CELIRU Inverse Relationships (ONTOLOGICAL_INFERENCE_RULES)

Automatic bidirectional relationship creation:

```python
ONTOLOGICAL_INFERENCE_RULES = {
    'INVERSE_PROPERTIES': {
        'DA_COMO_RESULTADO': {
            'inverse': 'RESULTA_DE',
            'domain': 'ExpedienteCensura',
            'range': 'LibroPublicado'
        },
        'TIENE_OBJETO_CENSURA': {
            'inverse': 'ES_CENSURADO_EN',
            'domain': 'ExpedienteCensura',
            'range': 'LibroPresentado'
        },
        'REDACTA': {
            'inverse': 'ES_REDACTADO_POR',
            'domain': 'Lector',
            'range': 'InformeLector'
        },
        'ELABORADO_MEDIANTE': { 
            'domain': 'InformeLector',
            'range': 'Formulario'
        }
        # ... more inverse pairs
    }
}
```

---

## Wikidata Integration

> **Summary:** Wikidata integration enables neoRAG to participate in the global Linked Open Data ecosystem by adopting standardized identifiers and data formats. The system employs Wikidata property codes (P625 for coordinate location, P131 for administrative territorial entity, P1552 for conservation status) and entity codes (Q-codes for controlled vocabulary values). This standardization facilitates cross-dataset interoperability, enabling federated queries across institutional boundaries. neoRAG extends these base properties with domain-specific validation rules—coordinate bounds verification for the Iberian Peninsula, administrative hierarchy constraints for Catalan/Spanish geographic entities, and controlled vocabulary enforcement for historical terminology. The architecture maintains local semantic richness while ensuring global data compatibility.

### Why Wikidata?

Wikidata provides:
1. **Universal identifiers** (P-codes for properties, Q-codes for entities)
2. **Standardized data formats** (coordinates, dates, references)
3. **Linked Open Data compatibility** (RDF/SPARQL export)
4. **Controlled vocabularies** (validated value sets)

### Wikidata Ontology Extension in neoRAG

neoRAG extends and incorporates specific components from the Wikidata ontology to enable interoperability with the global Linked Open Data ecosystem. The system integrates seven key Wikidata properties: **P625** (coordinate location) extended with Spain geographic bounds validation (35-44°N, -9-4°W); **P131** (located in administrative territorial entity) extended with the Catalan/Spanish hierarchy (Municipi→Comarca→Província→Comunitat Autònoma); **P17** (country) defaulting to Spain/Portugal for Iberian data; **P1552** (has quality) extended with a conservation status vocabulary including values like "Confirmada" (Q5727902), "Probable" (Q24574780), "Desapareguda" (Q7240364); **P527** (has part) extended with inhumed typology for mass graves (Civil, Soldat republicà, Soldat rebel); **P1542** (has cause) extended with Spanish Civil War death contexts (Mort en combat, Bombardeig, Repressió rereguarda); and **P2046** (area) for geographic measurements. The system uses standard Wikidata RDF namespaces (`wd:`, `wdt:`, `wds:`, `wdv:`, `wdn:`) for SPARQL export and extends Wikidata data types with domain-specific formats—particularly the globe-coordinate format for precise geographic positioning and hierarchical administrative entity chains. All local values are mapped to their corresponding Wikidata Q-codes, enabling seamless data exchange with the global Linked Open Data ecosystem while maintaining domain-specific validation rules for the Iberian Peninsula context, including coordinate bounds checking, administrative hierarchy validation, historical terminology support, and Catalan/Spanish bilingual compatibility.

#### Property Extensions (P-Codes)

| P-Code | Wikidata Name | neoRAG Extension | Usage |
|--------|---------------|------------------|-------|
| **P625** | coordinate location | Spain bounds (35-44°N, -9-4°W) | Sites, fosses, locations |
| **P131** | located in admin. entity | Catalan hierarchy (Municipi→Comarca→Província) | Admin relationships |
| **P17** | country | Default Spain/Portugal | Country assignment |
| **P1552** | has quality | Conservation status vocabulary | Site preservation |
| **P527** | has part | Inhumed typology (civil, soldiers) | Mass grave composition |
| **P1542** | has cause | Spanish Civil War death contexts | Death classification |
| **P2046** | area | Geographic measurements | Site dimensions |

#### Q-Code Mappings

| Category | Local Value | Wikidata Q-Code |
|----------|-------------|-----------------|
| Conservation (P1552) | Confirmada | Q5727902 |
| | Probable | Q24574780 |
| | Es desconeix | Q24574781 |
| | Desapareguda | Q7240364 |
| Typology (P527) | Civil | Q215627 |
| | Soldat republicà | Q4393580 |
| | Soldat rebel | Q4394260 |
| Death Context (P1542) | Mort en combat | Q210574 |
| | Bombardeig | Q891854 |
| | Repressió rereguarda | Q2001676 |

#### RDF Namespaces

| Prefix | URI | Purpose |
|--------|-----|---------|
| `wd:` | `http://www.wikidata.org/entity/` | Q-code entities |
| `wdt:` | `http://www.wikidata.org/prop/direct/` | P-code properties |
| `wds:` | `http://www.wikidata.org/entity/statement/` | Statement nodes |

### Wikidata Property Mapping

```python
# In relations.py and endpoint.py
wikidata_properties = {
    "P625": "coordinate_location",      # Geographic coordinates
    "P131": "located_in_administrative_territorial_entity",
    "P17": "country",
    "P1552": "has_quality",             # Conservation status
    "P527": "has_part",                 # Composition/parts
    "P1542": "has_cause",               # Cause of event
    "P2046": "area"                     # Geographic area
}
```

### Wikidata Controlled Values

Values mapped to Wikidata Q-codes:

```python
controlled_values = {
    "P1552": {  # has_quality (conservation status)
        "Confirmada": "Q5727902",           # Confirmed
        "Probable": "Q24574780",            # Probable
        "Es desconeix": "Q24574781",        # Unknown
        "Existent": "Q56661804",            # Existing
        "Desapareguda": "Q7240364",         # Disappeared
        "Parcialment destruïda": "Q26884324" # Partially destroyed
    },
    "P527": {   # has_part (inhumed typology)
        "Civil": "Q215627",
        "Soldat republicà": "Q4393580",     # Republican soldier
        "Soldat rebel": "Q4394260"          # Rebel soldier
    },
    "P1542": {  # has_cause (death context)
        "Mort en combat": "Q210574",        # Died in combat
        "Bombardeig": "Q891854",            # Bombing
        "Centre sanitari": "Q16917",        # Medical center
        "Repressió rereguarda": "Q2001676"  # Rearguard repression
    }
}
```

### Wikidata Validation Function

```python
def validate_wikidata_properties(self, properties: Dict) -> Tuple[bool, List[str]]:
    errors = []
    
    # 1. Validate coordinates are within Spain
    if "latitud" in properties and "longitud" in properties:
        lat = float(properties["latitud"])
        lon = float(properties["longitud"])
        if not (35.0 <= lat <= 44.0 and -9.0 <= lon <= 4.0):
            errors.append(f"Coordinates outside Spain: {lat}, {lon}")
    
    # 2. Validate controlled values
    for prop, values in self.controlled_values.items():
        prop_name = self.wikidata_properties.get(prop, prop)
        if prop_name.lower() in properties:
            value = properties[prop_name.lower()]
            if value and value not in values:
                errors.append(f"Invalid value for {prop_name}: {value}")
    
    # 3. Validate administrative hierarchy
    admin_levels = ["municipi", "comarca", "provincia", "comunitat_autonoma"]
    # Must be in correct order...
    
    return len(errors) == 0, errors
```

### Wikidata Normalization Function

```python
def normalize_to_wikidata(self, properties: Dict) -> Dict:
    normalized = {}
    
    # Convert coordinates to Wikidata globe-coordinate format
    if "latitud" in properties and "longitud" in properties:
        normalized["P625"] = {
            "value": {
                "latitude": float(properties["latitud"]),
                "longitude": float(properties["longitud"]),
                "precision": 0.000001,
                "globe": "http://www.wikidata.org/entity/Q2"  # Earth
            },
            "type": "globecoordinate"
        }
    
    # Map controlled values to Q-codes
    for prop, values in self.controlled_values.items():
        prop_name = self.wikidata_properties.get(prop, prop)
        if prop_name.lower() in properties:
            value = properties[prop_name.lower()]
            if value in values:
                normalized[prop] = {
                    "value": values[value],  # Q-code
                    "stated_as": value       # Original text
                }
    
    return normalized
```

### Wikidata RDF Namespaces

For SPARQL export (endpoint.py):

```python
from rdflib import Namespace

WD = Namespace("http://www.wikidata.org/entity/")      # Q entities
WDT = Namespace("http://www.wikidata.org/prop/direct/") # P properties
WDS = Namespace("http://www.wikidata.org/entity/statement/")
WDV = Namespace("http://www.wikidata.org/value/")
WDN = Namespace("http://www.wikidata.org/entity/value/")

# Usage in graph
self.graph.bind("wd", WD)    # wd:Q5727902
self.graph.bind("wdt", WDT)  # wdt:P625
```

---

## Knowledge Graph Structure

> **Summary:** The knowledge graph is implemented in Neo4j, a native graph database that stores entities as nodes and connections as relationships. This graph-based representation enables efficient traversal queries that would require complex joins in relational systems—for instance, multi-hop queries like "retrieve all publications by authors contemporary with a given writer" resolve through direct edge navigation. Each node contains a unique identifier, type label, domain properties, source provenance references, and a vector embedding for semantic similarity search. Relationships include metadata such as confidence scores, source document references, and extraction timestamps. This dual-mode architecture supports both structured graph queries (Cypher/SPARQL) and semantic vector similarity search (RAG), providing comprehensive query capabilities.

### Neo4j Data Model

```
┌─────────────────────────────────────────────────────────────────┐
│                         NEO4J GRAPH                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   (Autor)──────AUTHOR_OF──────▶(LibroPublicado)                │
│      │                              │                           │
│      │                              │                           │
│   CONTEMPORARY_OF              BELONGS_TO                       │
│      │                              │                           │
│      ▼                              ▼                           │
│   (Autor)                      (Coleccion)                      │
│                                     │                           │
│                                 MANAGED_BY                      │
│                                     │                           │
│   (Lector)──────REDACTA──────▶(InformeLector)                  │
│                                     │                           │
│                              ELABORADO_MEDIANTE                 │
│                                     │                           │
│                                     ▼                           │
│                              (Formulario3)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Node Structure

Each node in Neo4j has:

```cypher
(:Entity:Autor {
    id: "autor_cervantes_spanish",
    type: "Autor",
    name: "Miguel de Cervantes",
    nationality: "Spanish",
    sources: ["document_123.rdf"],
    embedding: [0.123, 0.456, ...]  // For semantic search
})
```

### Relationship Structure

```cypher
(autor)-[:AUTHOR_OF {
    confidence: "high",
    source_document: "archivo_censura_1942.pdf",
    extraction_date: "2024-01-15"
}]->(libro)
```

---

## Data Flow

> **Summary:** Data processing follows an 8-stage pipeline that progressively transforms raw input into validated graph structures. Stage 1 (Ingestion) detects file format and extracts content. Stage 2 (Neural Extraction) applies the EXTRACTION_PROMPT via Gemini to generate candidate entities and relationships in JSON format. Stages 3-7 constitute the symbolic validation sequence: type normalization via TYPE_ALIAS_MAP, property validation against ONTOLOGICAL_PROPERTY_MAP, Wikidata format normalization, relationship validation per RELATIONSHIP_RULES, and inverse relationship inference via ONTOLOGICAL_INFERENCE_RULES. Stage 8 (Persistence) writes validated data to Neo4j and generates vector embeddings for semantic search. All operations are instrumented with Langfuse for observability, enabling performance monitoring and error diagnosis.

### Complete Processing Pipeline

#op/acc/question how is the pipeline with different ontologies... from each db?

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: DATA INGESTION                                          │
│ ─────────────────────                                           │
│ • loader.py receives CSV/RDF/SQL file                           │
│ • Detects format and structure                                  │
│ • Extracts raw text/records                                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: NEURAL EXTRACTION (Gemini)                              │
│ ─────────────────────────────────                               │
│ • prompts.py sends structured prompt                            │
│ • EXTRACTION_PROMPT defines entity types                        │
│ • LLM extracts nodes & relationships as JSON                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: TYPE NORMALIZATION                                      │
│ ──────────────────────────                                      │
│ • TYPE_ALIAS_MAP: "writer" → "Autor"                           │
│ • CANONICAL_NODE_TYPES validation                               │
│ • Unknown types flagged or mapped to generic                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: PROPERTY VALIDATION                                     │
│ ─────────────────────────                                       │
│ • ONTOLOGICAL_PROPERTY_MAP: validate per type                   │
│ • Required properties checked                                   │
│ • Property names normalized (Spanish ↔ English)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: WIKIDATA NORMALIZATION                                  │
│ ────────────────────────────                                    │
│ • Coordinates → P625 format                                     │
│ • Controlled values → Q-codes                                   │
│ • Administrative hierarchy → P131                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: RELATIONSHIP VALIDATION                                 │
│ ─────────────────────────────                                   │
│ • RELATIONSHIP_RULES: required relationships exist?             │
│ • Domain/range validation                                       │
│ • Administrative hierarchy order                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 7: INVERSE RELATIONSHIP CREATION                           │
│ ───────────────────────────────────                             │
│ • ONTOLOGICAL_INFERENCE_RULES                                   │
│ • Auto-create: AUTHOR_OF ↔ AUTHORED_BY                         │
│ • Bidirectional graph navigation                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 8: NEO4J WRITE                                             │
│ ──────────────────                                              │
│ • writer.py creates/updates nodes                               │
│ • Entity fusion for duplicates                                  │
│ • Embeddings generated for semantic search                      │
│ • Langfuse logging for observability                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Validation Pipeline

> **Summary:** The validation pipeline implements a multi-layer quality assurance framework, ensuring data integrity before graph persistence. Layer 1 (File Validation) enforces size limits, format requirements, and structural integrity. Layer 2 (Type Validation) applies TYPE_ALIAS_MAP normalization and verifies membership in CANONICAL_NODE_TYPES. Layer 3 (Property Validation) checks ONTOLOGICAL_PROPERTY_MAP compliance and required property presence. Layer 4 (Coordinate Validation) verifies geographic coordinates fall within Iberian Peninsula bounds (35-44°N, -9-4°W). Layer 5 (Relationship Validation) enforces RELATIONSHIP_RULES constraints including domain/range type checking and administrative hierarchy ordering. Layer 6 (Wikidata Validation) confirms controlled value membership and Q-code mapping validity. This layered approach provides defense in depth, with each layer addressing distinct error categories.

### Multi-Layer Validation

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALIDATION LAYERS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: FILE VALIDATION (validation.py)                       │
│  ─────────────────────────────────────────                      │
│  ✓ File size limits                                             │
│  ✓ File extension validation                                    │
│  ✓ SQL content validation (INSERT INTO present)                 │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 2: TYPE VALIDATION (constants.py)                        │
│  ────────────────────────────────────────                       │
│  ✓ TYPE_ALIAS_MAP normalization                                 │
│  ✓ CANONICAL_NODE_TYPES membership                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 3: PROPERTY VALIDATION (prompts.py, writer.py)           │
│  ───────────────────────────────────────────────────            │
│  ✓ ONTOLOGICAL_PROPERTY_MAP compliance                          │
│  ✓ Required properties present                                  │
│  ✓ Data type validation                                         │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 4: COORDINATE VALIDATION (relations.py)                  │
│  ─────────────────────────────────────────────                  │
│  ✓ Latitude: 35.0 - 44.0 (Spain bounds)                        │
│  ✓ Longitude: -9.0 - 4.0 (Spain bounds)                        │
│  ✓ Numeric format validation                                    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 5: RELATIONSHIP VALIDATION (relations.py)                │
│  ───────────────────────────────────────────────                │
│  ✓ RELATIONSHIP_RULES compliance                                │
│  ✓ Domain/range type checking                                   │
│  ✓ Administrative hierarchy order                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 6: WIKIDATA VALIDATION (relations.py)                    │
│  ──────────────────────────────────────────                     │
│  ✓ Controlled value membership                                  │
│  ✓ Q-code mapping validity                                      │
│  ✓ Data format compliance                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Code Reference

> **Summary:** The implementation is organized across several key Python modules. `constants.py` defines all ontological rules including CANONICAL_NODE_TYPES, TYPE_ALIAS_MAP, ONTOLOGICAL_PROPERTY_MAP, and RELATIONSHIP_RULES. `prompts.py` contains the EXTRACTION_PROMPT template for LLM-based entity extraction. `extraction.py` orchestrates the neural-symbolic pipeline, invoking the LLM and applying validation functions. `relations.py` implements relationship validation logic and Wikidata property handling. `writer.py` performs final ontological transformations and Neo4j persistence. `graph_rag.py` implements the RAG query pipeline including vector retrieval and response generation. `endpoint.py` provides SPARQL query support and RDF export functionality. For debugging, `constants.py` (rule definitions) and `extraction.py` (processing flow) serve as primary entry points.

### Key Files

| File                              | Purpose                                |
| --------------------------------- | -------------------------------------- |
| `backend/utils/constants.py`      | All CELIRU ontology definitions        |
| `backend/graph/relations.py`      | Relationship validation + Wikidata     |
| `backend/graph/writer.py`         | Neo4j writing + ontological transforms |
| `backend/core/prompts/prompts.py` | LLM extraction prompt                  |
| `backend/sparql/endpoint.py`      | RDF export + Wikidata namespaces       |
| `backend/ingestion/loader.py`     | Data ingestion + normalization         |

### Constants Quick Reference

```python
# constants.py exports:
CANONICAL_NODE_TYPES      # Valid entity types
TYPE_ALIAS_MAP            # Type normalization
ONTOLOGICAL_PROPERTY_MAP  # Properties per type
ONTOLOGICAL_TRANSFORMATION_RULES  # Key handling rules
ONTOLOGICAL_INFERENCE_RULES       # Inverse relationships
RELATIONSHIP_RULES        # Required/optional relationships
INVERSE_RELATIONSHIPS     # Auto-generated inverse map
ONTOLOGICAL_RELATIONSHIPS # Entity connection rules
DATA_TO_SERVICE_MAPPING   # External API mapping
```

### Example: Complete Entity Processing

```python
# 1. Raw input from LLM
raw_entity = {
    "id": "author_123",
    "type": "writer",  # Non-canonical type
    "properties": {
        "nombre": "Camilo José Cela",
        "nationality": "Spanish"
    }
}

# 2. Type normalization (TYPE_ALIAS_MAP)
normalized_type = TYPE_ALIAS_MAP.get("writer", "writer")
# Result: "Autor"

# 3. Property validation (ONTOLOGICAL_PROPERTY_MAP)
valid_props = ONTOLOGICAL_PROPERTY_MAP["Autor"]
# {"nombre": "name", "nacionalidad": "nationality"}

# 4. ID normalization
normalized_id = "autor_cela_spanish"
# Pattern: autor_{name}_{nationality}

# 5. Final entity
final_entity = {
    "id": "autor_cela_spanish",
    "type": "Autor",
    "properties": {
        "name": "Camilo José Cela",
        "nationality": "Spanish"
    }
}

# 6. Relationship inference (ONTOLOGICAL_INFERENCE_RULES)
# If this author AUTHORED a book, also create:
# book -[AUTHORED_BY]-> author (inverse)
```

---

## Summary: How It All Connects

> **Summary:** neoRAG implements a complete neurosymbolic knowledge management architecture. Heterogeneous data sources (CSV, RDF, SQL, web) undergo neural extraction via Google Gemini, producing candidate entities and relationships. These candidates pass through a multi-stage symbolic validation pipeline enforcing CELIRU domain ontology constraints and Wikidata interoperability standards before persistence to the Neo4j knowledge graph. Query processing employs Retrieval-Augmented Generation: user questions are embedded, matched against graph nodes via vector similarity, and the retrieved context constrains LLM response generation to ensure factual grounding. The architectural principle is clear: CELIRU specifies the domain conceptual schema, Wikidata provides global identifier standards, the validation layer enforces compliance with both, and RAG guarantees response traceability to source evidence.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   CELIRU ONTOLOGY          WIKIDATA STANDARDS                   │
│   ───────────────          ──────────────────                   │
│   Domain-specific          Global interoperability              │
│   entities & rules         identifiers & formats                │
│         │                           │                           │
│         └───────────┬───────────────┘                           │
│                     │                                           │
│                     ▼                                           │
│         ┌───────────────────────┐                               │
│         │   VALIDATION LAYER    │                               │
│         │   (Ground Truth)      │                               │
│         └───────────┬───────────┘                               │
│                     │                                           │
│                     ▼                                           │
│         ┌───────────────────────┐                               │
│         │    KNOWLEDGE GRAPH    │                               │
│         │       (Neo4j)         │                               │
│         └───────────┬───────────┘                               │
│                     │                                           │
│         ┌───────────┴───────────┐                               │
│         │                       │                               │
│         ▼                       ▼                               │
│   ┌───────────┐          ┌───────────┐                         │
│   │   RAG     │          │  SPARQL   │                         │
│   │  Queries  │          │  Export   │                         │
│   └───────────┘          └───────────┘                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**The Key Insight:**
> CELIRU defines **what** can exist in the graph (domain knowledge)
> Wikidata defines **how** to format and identify it (global standards)
> The validation layer ensures **both** are respected
> The knowledge graph stores the **result**

---

*Document generated for neoRAG project - Peninsula Historical Research System*


