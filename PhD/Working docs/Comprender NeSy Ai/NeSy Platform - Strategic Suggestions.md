---
date: 2026-02-24
tags:
  - op/doc/reporte
  - tech/NeSyAI
  - design/strategy
  - op/projects/peninsula
---

## Strategic suggestions for a successful neurosymbolic platform

### 1. Clarify the target NeSy architecture and roadmap

- **Differentiate system states**
  - Document UBXAT as a pipeline neurosymbolic system: Cognitive ETL (Neural→Symbolic) → KG → RAG, as reflected in `UBXAT_Workflow_Explanation` and `Memoria técnica Peninsula – Lista de requisitos`.
  - Treat the HerStory-NeSyAI taxonomy (fine-tuning, runtime KG write-back, OWL/RDFS reasoning) as a roadmap: explicitly mark which capabilities are implemented and which are planned (phase 2+).
- **Phase evolution toward a closed-loop agent**
  - Phase 1: Current Cognitive ETL + RAG, read-only KG at query time.
  - Phase 2: Human-in-the-loop write-back (curators validate suggested triples from QA or analysis sessions before insertion into the KG).
  - Phase 3: Selective automatic write-back with strong guards (confidence thresholds, change-review workflows, regression tests on KG quality), approximating the Type 6 “closed-loop” agent described in the HerStory-NeSyAI taxonomy and KG+LLM literature.

### 2. Strengthen KG↔LLM synergy (dual direction)

- **Make dual-direction integration explicit**
  - Maintain LLM→KG roles already present: ETL extraction, schema mapping, entity resolution, ontological normalization.
  - Systematically extend KG→LLM use: all LLM prompts (ETL, QA, explanation) should receive explicit ground-truth snippets and ontology constraints, not only raw text.
- **Introduce a subgraph-construction step for QA**
  - Before each QA answer, construct a small, task-specific subgraph: select a minimal neighborhood around entities relevant to the question using ground-truth rules.
  - Pass only this subgraph (plus key metadata like provenance and confidence) as symbolic context to Gemini to reduce hallucination risk and follow budget-aware context construction practices from recent KG+LLM work.
- **Use agents or modular components for different reasoning roles**
  - Separate components (or “agents”) for: subgraph construction, evidence selection, SPARQL→Cypher translation, and answer composition.
  - Log which component contributed which evidence to final answers, supporting explainability and debugging.

### 3. Treat Ground Truth + ontology as the symbolic core

- **Version and govern ground-truth assets**
  - Maintain versioned ground-truth packages per domain (SIDBRINT, censorship, mass graves, etc.) with explicit change logs and impact notes.
  - Require that any change to mappings, inverse relationships, or gender rules includes: (a) updated unit tests; (b) at least one domain expert review.
- **Layered symbolic reasoning**
  - Start from the current rule-based validation (type normalization, inverse relationships, constraints on relations) and selectively add OWL/RDFS reasoning where it yields clear benefits (e.g. geographic containment, event hierarchies, gender/intersectional taxonomies).
  - Keep reasoning “narrow but deep”: focus on domains where entailment is analytically important (e.g. regional aggregations, censorship typologies) rather than global-heavy reasoning.
- **Explicitly connect symbolic rules to NeSy objectives**
  - For each major rule family (e.g. relationship rules, gender normalization, location hierarchy), document:
    - Its epistemic role (e.g. avoid erasing certain identities, maintain administrative coherence).
    - The expected effect on LLM outputs (e.g. constrain which relations can be proposed, which groupings are valid).

### 4. Operationalize human-centred and epistemic-justice goals

- **Align validity threats and HCAI variables with design decisions**
  - Map threats listed in `Tests y evaluación` (trust, bias/fairness, interaction complexity, privacy, ethics) to:
    - Concrete interface features (confidence indicators, KG path visualizations, plain-language explanations of system limits).
    - Logging/metrics (trust ratings in user studies, frequency of “I disagree” feedback, measured cognitive load).
- **Use the Peninsula/UBXAT interface modules as levers**
  - Agent module:
    - Keep confidence colours and source chips, but add a “show reasoning path” that reveals a compressed KG explanation (entities, relationships and constraints used).
    - Provide a feedback channel for “this feels biased/incorrect” that ties into evaluation protocols.
  - Graph module:
    - Offer filters that make gender and intersectional attributes visible and explorable without forcing binary views.
    - Provide clear provenance for sensitive nodes (censorship decisions, mass graves, victims) and allow researchers to annotate or flag problematic representations.
- **Plan for co-production and participatory refinement**
  - Use co-creation sessions to:
    - Elicit information needs (including “unknown unknowns”, following Ford/Bawden/Robinson and Shenton’s framework cited in `Tests y evaluación`).
    - Validate whether KG structures and RAG answers support those needs.

### 5. Design a coherent evaluation stack for NeSy behaviour

- **Three-layer evaluation plan**
  - Layer A – Symbolic/KG quality:
    - Coverage, consistency, correctness of entities and relations against expert-annotated ground truth (as in the “experts annotate prerequisite relations” model cited in your KG-evaluation notes).
    - Inter-annotator agreement metrics (e.g. Cohen’s kappa) for key relation types.
  - Layer B – NeSy system behaviour:
    - ETL accuracy (entity/relationship extraction precision and recall).
    - SPARQL→Cypher translation correctness and performance.
    - RAG factuality and hallucination rate (answers must be entailed or strongly supported by KG context).
    - Explainability: can users reconstruct why an answer was produced from KG evidence.
  - Layer C – HCAI and UCD:
    - Usability and interaction quality (task success, time, errors, SUS-like scales).
    - Trust, perceived fairness, and perceived cognitive load (e.g. NASA-TLX or adapted scales from your cited HCAI and cognitive-load works).
    - Co-production dynamics, alignment with epistemic-justice goals.
- **Tie each requirement to at least one test**
  - Extend the `Memoria técnica` and Peninsula checklists so that:
    - Every “requisito” has at least one associated test (unit, integration, user study, or analytic check).
    - Tests explicitly mention whether they concern the neural part, the symbolic part, or their interaction.

### 6. Make inclusion, bias, and gender-aware reasoning technically testable

- **Gender-aware query triad (NL, SPARQL, Cypher)**
  - Use the definitions in `UBXAT - Perspective and Prompts (EN)` to build canonical test suites where:
    - A query about women/men/other identities in natural language, SPARQL, and Cypher all resolve to the same result set.
    - Variants in language (Spanish/Catalan/English) and phrasing do not change the semantic intent once normalized.
  - Track discrepancies as NeSy bugs, not “just” UX issues.
- **Bias probes and intersectional coverage**
  - Define probe questions and KG slices where expected distributions are known (e.g. percentage of women brigadistas, representation of certain ethnicities if modeled).
  - Compare system answers and visualizations to KG ground truth and log over/under-representation patterns.
- **Monitor pipeline-embedded bias**
  - At ETL stage: log which records are dropped or down-weighted by either LLM extraction or symbolic validation, broken down by sensitive attributes where possible.
  - At QA stage: log which groups appear in answers relative to their KG prevalence; investigate systematic gaps as potential bias from prompts, ground truth, or graph incompleteness.

### 7. Governance, observability, and sustainability

- **Define NeSy-specific observability metrics**
  - Leverage Langfuse and existing logs to track:
    - KG consistency violations per ingestion job.
    - SPARQL→Cypher translation failures or deviations from expected results.
    - Hallucination incidents per 100 QA answers (detected by inconsistency with KG or manual review).
    - Average subgraph size passed to Gemini for QA (to balance completeness vs cost and cognitive load).
- **Embed environmental and social considerations**
  - Maintain the current strategy of using base models with neurosymbolic adaptation (prompts + ground truth) as first choice; justify any shift to fine-tuning with:
    - A clear research/epistemic benefit not reachable via adaptation alone.
    - An explicit energy and cost budget, in line with `Memoria técnica` guidance on environmental impact.
  - Document how architectural choices (batch size, caching, vector indexing) impact both performance and energy consumption.

### 8. Alignment with HerStory-NeSyAI taxonomic classification

- **Kautz Type 6 and pipeline patterns**  
  The phased roadmap (Section 1) makes explicit how the current Cognitive ETL + RAG pipeline corresponds to Type 2/3 patterns, while planned runtime write-back and stronger reasoning move the platform toward the Type 6 “Neuro[Symbolic]” closed-loop agent described in the taxonomy.

- **Yu’s learning–reasoning triad**  
  Strengthening KG↔LLM synergy and Ground Truth governance (Sections 2–3) operationalizes “Learning–reasoning” as the primary mode: learning and reasoning interact iteratively through extraction, validation, and (future) write-back. Any future fine-tuning guided by KG/ontology constraints would explicitly instantiate “Reasoning for learning” as discussed in the NeSyAI text.

- **Pan’s “Synergized LLMs + KGs”**  
  Dual-direction integration (LLM→KG in ETL and KG→LLM in RAG and prompts) directly implements the “Synergized” label: KGs enhance LLMs at inference time, while LLMs augment and maintain KGs through ETL and prospective runtime updates.

- **Hybrid / bidirectional characterizations (Zhu & Sun; Bader & Hitzler; Pacheco)**  
  The bias, gender-aware, and epistemic-justice workflows (Sections 4–6) rely on bidirectional flow: symbolic constraints guide neural behavior and neural outputs feed back into symbolic structures under governance, matching the “Hybrid”, bidirectional, coupled and increasingly symmetric, interleaved interaction style identified in the NeSyAI classification.

- **Coverage profile (Colelough & Regli, De Boer, Arachchige)**  
  The evaluation and observability stack (Sections 5–7) concretizes the strong scores in Knowledge Representation, Learning & Inference, and Logic & Reasoning, while the UI, trust, and feedback features target the moderate–strong Explainability/Trustworthiness and Meta-cognition dimensions, aligning implementation strategy with the classification’s coverage profile and closed-loop semantic-tool agent pattern.

### 9. Relating UBXAT digestion, NeSyAI taxonomy, and *Knowledge Graphs and LLMs in Action*

- **Architectural convergence and gap**  
  `UBXAT digestión de procesos` and the NeSyAI taxonomy both describe a Cognitive ETL → KG → RAG pipeline that aspires to a closed-loop neuro-symbolic agent. *Knowledge Graphs and LLMs in Action* (Parts 1–3) provides a similar story arc: foundational hybrid-intelligence patterns (chapters 1–2), KG construction from structured and unstructured data (3–6), and LLM-assisted extraction and interpretation. Strategically, this triangulation supports keeping UBXAT’s current state clearly labeled as “pipeline/hybrid IAS” while using the NeSyAI labels and Negro et al.’s patterns as the explicit roadmap to a more integrated IAS-style system.

- **Archives and humanities as first-class use cases**  
  The book’s “archives challenge” and Rockefeller Archive Center case (chapters 5–6) mirror HerStory’s historical and cultural-heritage focus. UBXAT’s domain (SIDBRINT, CeLRu, mass graves) can be positioned as a concrete instantiation of the “archives → KG → LLM” pipeline they describe, but extended with stronger epistemic-justice and gender-aware constraints documented in UBXAT and NeSyAI notes. This justifies investing in domain-specific ontologies and ground truth as a differentiator versus generic KG+LLM platforms.

- **Designing intelligent systems and IASs**  
  In chapters 2 and 6, Negro et al. frame intelligent systems and “intelligent application systems” (IASs) around characteristics like explainability, reasoning over KGs, and mixed inductive/deductive engines. The NeSyAI taxonomy already classifies HerStory as a hybrid, KG-centred IAS; UBXAT digestion notes reveal where implementation still falls short (no fine-tuning, write-back confined to ETL, limited explicit reasoning). Strategic suggestion: use the IAS criteria from the book as a checklist to prioritise which NeSyAI “future capabilities” become concrete UBXAT milestones (e.g. transparent reasoning paths, richer KG-based explanations).

- **Methodological alignment for KG building from text**  
  Chapters 5–7 outline LLM-assisted knowledge extraction, normalization, and NED pipelines that strongly resemble UBXAT’s Cognitive ETL and HerStory’s `kgConstruction` methodology. The digestion note’s emphasis on ontology reuse, ORSD, and methodological rigor can be reframed as providing the “KG engineering backbone” that the book assumes but does not specialise for epistemic-justice contexts. Strategically, this supports treating UBXAT + HerStory methodology as a domain-specific reference implementation of the book’s general KG-from-text recipes.

- **Positioning and communication**  
  Taken together, `UBXAT digestión de procesos`, the NeSyAI taxonomy, and *Knowledge Graphs and LLMs in Action* allow a coherent narrative: UBXAT is a humanities-focused, epistemic-justice-oriented instantiation of the hybrid KG+LLM IAS patterns advocated by Negro et al., currently at a pipeline/hybrid stage but deliberately moving toward the closed-loop, Type 6 neuro-symbolic behaviour described in the NeSyAI classification. This narrative can be used both for external positioning (grant proposals, papers) and internal roadmap alignment (what to implement next and why).