---
date: 2026-01-30
tags:
  - op/doc/reporte
  - HerStory
  - tech/NeSyAI
  - op/activity/Aiinteraction
  - op/projects/peninsula
---

## HerStory-NeSyAI taxonomy and its source trail

*Revisado con los .md enlazados a los PDFs de `PDF/Peninsula/` (clippings en Clippings y HerStory/Técnica de inv). Las fuentes Peninsula citadas en este documento enlazan siempre al archivo .md correspondiente.*

This note links the consolidated taxonomic classification in `[[HerStory-NeSyAI A Multi-Framework Taxonomic Classification of the Neuro-Symbolic Generative System]]` ("this exact text") with the project and PhD working notes that justify each group of conclusions.

### 1. Neurosymbolic architecture and KG+LLM synergy

- **Classification claim (NeSyAI text)**: HerStory is a *neuro-symbolic generative AI system built around an LLM coupled with a KG and a retrieval layer*, framed as a *closed-loop neuro-symbolic agent* with *bidirectional flow* (neural→symbolic write-back and symbolic→neural grounding).
- **Implementation sources**
  - `[[HerStory/Raw material/ONTOLOGY_GUIDE|neoRAG Ontology Architecture Guide]]`: describes the neurosymbolic architecture (LLM + CELIRU ontology + Wikidata + Neo4j), the RAG question-answering flow, and the validation pipeline that turns raw data into a KG with embeddings.
  - `[[HerStory/Raw material/GROUND_TRUTH_AND_PROMPT_GUIDE|Ground Truth and Structured Prompt Guide]]`: details the ground-truth rule base, the structured extraction prompt, and the neural→symbolic validation steps that underpin the "learning for reasoning" aspect of the taxonomy.

### 2. Hybrid / symbiotic human–AI framing

- **Classification claim (NeSyAI text)**: Placement of HerStory within hybrid and symbiotic human–AI systems (e.g., De Boer's "closed-loop semantic-tool agent pattern", Sheth's "lift + compress", and Colelough & Regli's coverage of Hybrid Intelligence dimensions).
- **Conceptual PhD sources**
  - `[[Hybrids - Symbiosis definitions]]`: curates definitions and citations on Hybrid Intelligence and Symbiotic AI, providing the vocabulary (collaborative, bidirectional, mixed human–AI teams) that the NeSyAI text uses to characterise HerStory as more than a "tool-augmented" LLM.
  - `[[NeSy Ai - semantic use-case inventory]]`: situates HerStory within a corpus of semantic/KG projects and participatory knowledge-graph systems; this comparative inventory supports the "synergized LLMs + KGs" label (Pan et al.) by showing how HerStory's loop aligns with and extends existing KG-based cultural-heritage systems.

### 3. KG-centred, participatory and epistemic-justice orientation

- **Classification claim (NeSyAI text)**: Strong scores in Knowledge Representation, Learning & Inference, and Logic & Reasoning, with *moderate–strong explainability/trustworthiness* and *moderate meta‑cognition*, grounded in KG/ontology centrality and community/participatory processes.
- **PhD methodological / ethical sources**
  - `[[Epistemic justice]]`: frames the normative goals (epistemic justice, community agency) that motivate KG design and evaluation; this underlies the emphasis on provenance, bias-aware modelling, and participatory enrichment highlighted in the NeSyAI taxonomy.
  - `[[Se busca con HerStory - guidelines]]` and `[[Tests y evaluación]]`: provide design and evaluation criteria for HerStory as a research infrastructure, connecting taxonomic claims about explainability, trust, and iterative refinement with concrete user-facing guidelines and test plans.

### 4. Workflow, tools, and interaction patterns

- **Classification claim (NeSyAI text)**: HerStory as a *closed-loop semantic-tool orchestration pattern* (De Boer et al.; Arachchige et al.) with *interleaved*, *symmetric*, *coupled* interaction between neural and symbolic components, where the KG and ontology are not passive but active in reasoning and updating.
- **Operational / workflow sources**
  - `[[UBXAT_Workflow_Explanation]]` and `[[UBXAT]]`: describe the human-in-the-loop workflow for using the system (upload, curation, querying, interpretation), supporting the view of HerStory as a semantic tool used in ongoing research practice rather than a one-shot model.
  - **Peninsula PDF-linked clippings**: [[Guia Plataforma Web (ES)]], [[Web Platform User Guide (EN)]] (cuatro módulos: Agente, Grafo, SPARQL, Ingestar; evaluación de confianza, chips de fuentes; brigadistas/fosas/Guerra Civil); [[UBXAT - Readme (EN)]] (API ETL/SPARQL/chat, CLI, ground_truth); [[Sistema general - Cultura y Censura KG]] (flujo de procesamiento, motor de consultas). These clippings document the operational interface and workflows described in the Peninsula PDFs.
  - `[[Methods UCD-SC]]` and `[[NeSy Ai - semantic use-case inventory]]`: connect HerStory's technical loop to user-centred and participatory methods (UCD, co-design, evaluation), explaining how human activities are interleaved with neural and symbolic processes in the operational lifecycle.

### 5. Positioning within the research landscape

- **Classification claim (NeSyAI text)**: Consolidated labels across multiple taxonomies (Kautz Type 6, Yu's learning–reasoning, Pan's "Synergized LLMs + KGs", Zhu & Sun's "Hybrid", Pacheco's coupled/symmetric/interleaved, etc.).
- **Literature-anchoring sources in PhD notes**
  - `[[Hybrids - Symbiosis definitions]]`: collects canonical definitions and key references on hybrid and neurosymbolic systems (e.g., Van Harmelen & Teije "boxology", neuro-symbolic AI surveys), which are cited in the NeSyAI classification.
  - `[[NeSy Ai - semantic use-case inventory]]`: maps related KG/LLM projects and participatory semantic portals, providing the comparative basis for claims that HerStory represents a "synergized" and "multi-integration" architecture within the broader NeSy AI and cultural-heritage KG landscape.

---

## 6. Summary: Document relationships and discrepancies

### Shared architecture across all documents

All documents (`GROUND_TRUTH_AND_PROMPT_GUIDE.md`, `ONTOLOGY_GUIDE.md`, Peninsula/UBXAT notes and their PDF-linked clippings, and this taxonomy source-links note) describe the **same core neurosymbolic architecture**:

- **LLM (Gemini) + ground truth/ontology + Neo4j KG + embeddings + RAG QA**
- **Neurosymbolic integration**: neural extraction/embeddings combined with symbolic rules (Wikidata, CELIRU-like constraints, ontological transformations, inverse relationships)
- **Same architectural layers**: Ingestion/ETL with LLM extraction → validation → Neo4j; RDF/SPARQL ↔ Neo4j bridge; RAG layer for question answering

**Peninsula clippings (PDF-linked .md)** confirm and detail this architecture: [[Sistema general - Cultura y Censura KG]] (flujo ingesta→análisis estructural rdflib/headers→Gemini→Neo4j embeddings→indexación; chunks 100; motor de consultas semántico); [[UBXAT - General Platform Overview (EN)]] (Cognitive ETL, zero-config ingestion, Gemini, Neo4j Aura, LangGraph, conversational API); [[UBXAT_-_Estrategia_RDF_Neo4j]] (RDF↔Neo4j, Capa 4 RAG con Langchain/Langfuse y Neo4jVector); [[UBXAT - Readme (EN)]] (LangGraph pipeline, ground_truth JSON, endpoints ETL/SPARQL/chat).

### neoRAG guides vs Peninsula/UBXAT documentation

**neoRAG raw guides** (`GROUND_TRUTH_AND_PROMPT_GUIDE.md`, `ONTOLOGY_GUIDE.md`):
- **Generic, system-level technical documentation**: define ground-truth constants, ontological maps, relationship rules, inference rules; explain structured extraction prompt and RAG QA template; present clean neurosymbolic pipeline (raw data → Gemini + prompt → validation → Neo4j → RAG)
- **Ontology + prompt centric**: focus on what rules exist and how prompts encode them

**Peninsula/UBXAT documentation** (PDFs en `PDF/Peninsula/` y sus clippings .md en Clippings):
- **Project/deployment-level documentation**: frame UBXAT as Cognitive ETL platform for historians, with LangGraph orchestration, batch processing, API endpoints, example workflows; deeper engineering details (LangGraph nodes, APIs, env vars, performance); emphasize RDF↔Neo4j strategy, SPARQL→Cypher translation, specific historical domains (SIDBRINT, CeLRu, mass graves / Democratic memory).
- **Platform + workflow centric**: focus on how the system is used and deployed.
- **Sources (clippings linked to Peninsula PDFs)**: [[UBXAT - General Platform Overview (EN)]] (zero-config ingestion, Gemini, Neo4j Aura, LangGraph, conversational API, use cases International Brigades / Mass Graves); [[UBXAT - Readme (EN)]] (graph_builder.py, parser, gemini_*.py, executor, FastAPI, `/api/v1/etl/process`, `/api/v1/sparql`, `/api/v1/chat`, ground_truth JSON, default.yaml, batch 100); [[UBXAT_-_Estrategia_RDF_Neo4j]] (RDF↔Neo4j flows, UnifiedDataLoader, rdflib, SELECT/ASK/CONSTRUCT/DESCRIBE, Capa 4 RAG with Langchain and Langfuse, Neo4jVector); [[Sistema general - Cultura y Censura KG]] (flujo ingesta→análisis estructural rdflib/headers→Gemini→Neo4j embeddings→indexación; chunks límite 100; tipos entidades/relaciones; motor de consultas semántico); [[Guia Plataforma Web (ES)]] (cuatro módulos: Agente, Grafo de Conocimiento, SPARQL, Ingestar; evaluación de confianza verde/amarillo/rojo; chips de fuentes; nodos por color; brigadistas/fosas/Guerra Civil); [[UBXAT SPARQL (EN)]] (POST `/api/v1/sparql`, ground truth Q5/Q108163/Q49848, traducción SPARQL→Cypher); [[UBXAT - Perspective and Prompts (EN)]] (conceptos género-neutral, P21 sex or gender, consultas por género en lenguaje natural y SPARQL/Cypher).

#### Element-by-element: what each does in UBXAT

| Element | Function in the system |
|--------|------------------------|
| **Cognitive ETL platform for historians** | Positions UBXAT as the tool that *extracts* heterogeneous historical data (SQL, CSV, RDF, PDF), *transforms* it via AI into a knowledge graph, and *loads* it into Neo4j—so historians can query and analyse it without doing low-level ETL themselves. |
| **LangGraph orchestration** | Coordinates the multi-step pipeline as a *stateful graph*: parser → Gemini analyzer → schema mapper → entity resolver → Cypher generator. Manages shared state, conditional branching, retries, and batch progress instead of a single linear script. |
| **Batch processing** | Processes input in configurable chunks (e.g. default 100 items) so large files don’t overload memory or API limits; state tracks which batches are done and allows parallel or sequential handling. |
| **API endpoints** | Expose ETL (e.g. `/api/v1/etl/process`), chat (`/api/v1/chat`), and SPARQL (e.g. `POST /sparql`) so clients can trigger ingestion, ask questions, or run semantic queries without touching the codebase. |
| **Example workflows** | Document concrete user journeys (researcher: upload → query → visualize; developer: extend parser → update ground truth → test; analyst: configure prompts → apply to graph → export) so deployment and usage are repeatable. |
| **LangGraph nodes** | Individual steps in the graph: e.g. *Parser node* (format detection, ground truth load), *Gemini Analyzer* (LLM extraction), *Schema Mapper* (type/property normalization), *Entity Resolver* (dedup via ID + embeddings), *Cypher Generator* (Neo4j write). Each reads/writes shared state. |
| **APIs** | Same as *API endpoints*: the REST/SPARQL surfaces that external tools and the UI use to drive ETL, conversational QA, and graph queries. |
| **Env vars** | Configuration (e.g. `NEO4J_URI`, `GOOGLE_GENAI_API_KEY`, `COGNITIVE_ETL_BATCH_SIZE`, `COGNITIVE_ETL_MAX_RETRIES`) so the same code runs in dev/staging/prod without hardcoding secrets or tuning. |
| **Performance** | Addressed via batch size, caching of ground truth, vector indices in Neo4j, retry logic, and (in Fase de Desarrollo) load tests and metrics; ensures the platform scales to large historical datasets. |
| **RDF↔Neo4j strategy** | *Ingestion*: RDF (e.g. .ttl) → unified loader → triples to text → Gemini extraction → ontological transform → Neo4j. *Query/export*: Neo4j → Cypher execution → RDF-shaped results (e.g. SPARQL JSON). Keeps a single storage (Neo4j) while supporting semantic standards. |
| **SPARQL→Cypher translation** | Lets users query the graph with SPARQL; the endpoint parses SPARQL, uses ground truth to map QIDs/properties to Neo4j schema, generates Cypher, runs it, and returns SPARQL Results JSON so the graph is consumable by RDF/LOD tools. |
| **Specific historical domains (SIDBRINT, CeLRu, mass graves)** | Ground truth and prompts are tailored to these datasets: e.g. SIDBRINT (International Brigades), CeLRu (Francoist censorship), mass graves / Democratic memory. Entity types, properties, and relationships reflect these domains so extraction and validation are domain-accurate. |
| **Capa 4 RAG (Estrategia RDF Neo4j)** | Búsqueda semántica con embeddings; consulta del grafo para contexto; generación de respuestas con Gemini; cadena RAG con Langchain y Langfuse; Neo4jVector para búsqueda vectorial ([[UBXAT_-_Estrategia_RDF_Neo4j]]). |
| **Interfaz web (Guía Plataforma Web)** | Cuatro módulos: Agente (consulta en lenguaje natural, evaluación de confianza verde/amarillo/rojo, chips de fuentes, métricas de rendimiento, historial), Grafo de Conocimiento (nodos por color: rojo=personal, azul=localizaciones/eventos, verde=documentación, naranja=fosas), SPARQL (biblioteca de consultas predefinidas), Ingestar (SQL/CSV/JSON, configuración ETL, monitorización); estado API y sincronización ([[Guia Plataforma Web (ES)]]). |
| **Ground truth dinámico (Readme)** | Archivos JSON en `data/ground_truth/` mapean nombres de tabla a tipos de entidad, QIDs de Wikidata a categorías; el sistema adapta el comportamiento sin mapeos hardcodeados ([[UBXAT - Readme (EN)]]). |
| **Perspectiva de género y prompts (Perspective & Prompts)** | Conceptos unificados género-neutral (Author P50, Person Q5, Brigadista); género vía P21 (sex or gender) y transformación `normalize_gender`; consultas por género en lenguaje natural, SPARQL y Cypher; ground truth en sidbrint_consolidated_wikidata_mapping.json y autor_wikidata_mapping.json ([[UBXAT - Perspective and Prompts (EN)]]). |

**Key difference**: neoRAG guides are **ontology + prompt centric**; Peninsula/UBXAT are **platform + workflow centric**, but they describe the same pipeline anchored in the Peninsula use-case.

### Peninsula PDF-linked clippings (evidence)

Documentos .md enlazados a los PDFs de `PDF/Peninsula/` que sustentan la digestión anterior. Enlazar siempre al .md para comprobar el contenido.

| Clipping (.md) | Qué aporta a la digestión |
|----------------|---------------------------|
| [[UBXAT - General Platform Overview (EN)]] | Cognitive ETL, zero-config ingestion (SQL, CSV, RDF), Gemini, Neo4j Aura, LangGraph, conversational API, use cases International Brigades / Mass Graves, beneficios (80% reducción tiempo, democratización). |
| [[UBXAT - Readme (EN)]] | Arquitectura técnica (graph_builder.py, parser, gemini_*.py, executor), FastAPI, endpoints `/api/v1/etl/process`, `/api/v1/sparql`, `/api/v1/chat`, ground_truth JSON, default.yaml, batch 100, CLI, estructura del proyecto. |
| [[UBXAT_-_Estrategia_RDF_Neo4j]] | Flujos RDF↔Neo4j; ingesta RDF (UnifiedDataLoader, rdflib, Gemini, Neo4j); consulta SPARQL (SELECT, ASK, CONSTRUCT, DESCRIBE); transformaciones ontológicas; capas (almacenamiento, extracción, SPARQL, RAG); Langchain, Langfuse, Neo4jVector. |
| [[Sistema general - Cultura y Censura KG]] | Flujo: ingesta → análisis estructural (rdflib/headers) → extracción Gemini → Neo4j (embeddings, índices vectoriales) → indexación; chunks límite 100; tipos entidades/relaciones; motor de consultas (búsqueda semántica, navegación de grafo); robustez. |
| [[Guia Plataforma Web (ES)]] | Interfaz: cuatro módulos (Agente, Grafo, SPARQL, Ingestar), panel lateral y cabecera, evaluación de confianza, chips de fuentes, nodos por color, brigadistas/fosas/Guerra Civil Española. |
| [[Web Platform User Guide (EN)]] | Mismo contenido que Guía Plataforma Web (ES) en inglés. |
| [[UBXAT SPARQL (EN)]] | Endpoint POST `/api/v1/sparql`; traducción SPARQL→Cypher; SELECT/ASK/COUNT; resolución de variables con ground truth (Q5, Q108163, Q49848); ejemplos curl. |
| [[UBXAT - Perspective and Prompts (EN)]] | Conceptos género-neutral; P21 para género; consultas por género (lenguaje natural, SPARQL, Cypher); prompt engineering para `/api/v1/chat`; ground truth sidbrint/autor. |
| [[HerStory/Técnica de inv/UB Knowledge graph - Guía]] | Configuración de prompts: reglas de extracción, foco de entidades, tipos de relaciones, presets (A1, Mapas, Red social, Quien escribió qué); UI "Configurar Prompt". |

Otros PDFs de Peninsula con clipping: [[Gmail - UBXAT - [Fase de Desarrollo - Entregables]]], [[Informe de Sprint_ 7 de julio - 18 de julio de 2024]], [[Memoria tecnica - planteamiento incial del proyecto]], [[MemoriaCT-individual-2023-ingles-221223]], [[UBXAT - Resumen Ejecutivo y Metodología AplicadaResumen Ejecutivo del Proyecto UBXAT(DCU)]], [[UBXAT_-_Fase_de_Desarrollo_-_Action_Plan(v2)]], [[UBXAT API Module (EN)]] — aportan contexto de proyecto, entregables, sprints, memoria técnica y plan de desarrollo.

### Role of this taxonomy source-links note

This note (`HerStory-NeSyAI taxonomy - source links.md`) is **purely meta/documentary**: it does not define architecture; instead it:
- Maps taxonomic claims in `[[HerStory-NeSyAI A Multi-Framework Taxonomic Classification...]]` (Kautz Type 6, Pan "Synergized", etc.) to specific markdown sources (neoRAG guides + PhD notes)
- Functions as a **traceability layer**: "this classification sentence ⇄ this markdown note and system doc"

While neoRAG/UBXAT docs describe **what the system does**, this note describes **where the research narrative gets its evidence**.

### Conceptual vs current-implementation discrepancies

**Critical difference** between:
- **NeSyAI classification text** (summarized/linked by this note): claims fine-tuned LLM, runtime KG write-back, OWL/RDFS inference, closed-loop Type 6 "neural engine with symbolic reasoning invoked"
- **UBXAT workflow/Estrategia docs**: currently state no fine-tuning (base Gemini, adaptation via prompts + ground truth), KG writes only in ETL (query-time is read-only RAG), ontology use/validation but no explicit OWL reasoner documented, architecture closer to forward ETL→KG→RAG pipeline (Kautz Type 2/3) than fully closed-loop agent

**Interpretation**: neoRAG guides + UBXAT docs converge on the **same implemented architecture** (Cognitive ETL + KG + RAG, neurosymbolic but mostly pipeline-shaped). The NeSyAI classification describes a **more advanced, bidirectional, closed-loop variant** (fine-tuning + runtime write-back + explicit reasoning), which UBXAT documentation itself treats as **intended/future/broader HerStory system**, not (yet) the strict current UBXAT implementation. #op/acc/question where?

### One-sentence synthesis

All these documents describe the same neurosymbolic KG+LLM ecosystem: neoRAG guides give the **abstract architecture**, Peninsula/UBXAT notes and their **PDF-linked clippings** (Overview, Readme, Estrategia RDF Neo4j, Sistema general, Guía Plataforma Web, SPARQL Guide, Perspective & Prompts, etc.) give the **concrete platform and workflows**, and this taxonomy source-links note ties a **multi-taxonomy research classification** back to those implementation and theory notes—while also making visible where the classification is **slightly ahead of** the currently documented UBXAT implementation (fine-tuning, runtime write-back, stronger reasoning).

---

Together, these working notes and raw-material guides provide the documentary basis for each family of claims in `[[HerStory-NeSyAI A Multi-Framework Taxonomic Classification of the Neuro-Symbolic Generative System]]`, connecting the taxonomic "labels" back to concrete architectures, workflows, ethical framings, and comparative literature reviews.

### 7. HerStory_kgConstruction vs NeSyAI classification (how "intelligence" is framed)

- **HerStory_kgConstruction-v2Def_20250611**: frames HerStory almost entirely as a **symbolic knowledge‑engineering pipeline**. The focus is on phases, processes, and methodologies for database access, ontology design, KG implementation, enrichment, linking, and publication (Radulovic et al., Noy & McGuinness, LOT, etc.). Large Language Models only appear late, as **one option among others for extracting semantic frames/triples from text**, not as an agent or "intelligence" in their own right.
- **HerStory‑NeSyAI classification text**: reframes the same ontology/KG assets as part of a **neuro‑symbolic generative system**. Here, the LLM is treated as an **active controller** that queries the KG, triggers OWL/RDFS inference, and (in the target design) **writes back new triples at runtime**, producing a **closed‑loop, bidirectional coupling** between neural and symbolic components.
- **Neuro‑symbolic framing difference**: in `kgConstruction`, the KG+ontology pipeline is **methodological infrastructure** (symbolic, engineering‑centric), and LLMs are primarily **tools for extraction**. In the NeSyAI taxonomy, the same infrastructure becomes the **symbolic substrate of a neurosymbolic agent**, and the KG+ontology+reasoner are explicitly analysed across multiple NeSy taxonomies (Kautz Type 6, Pan “Synergized”, Yu “learning–reasoning”, Zhu & Sun “Hybrid”, Pacheco “coupled/symmetric/interleaved”) to argue that HerStory is not just “RAG with a KG”, but a **hybrid intelligence loop where symbolic state and neural behaviour co‑evolve**.
