# Wikidata Mapping Assessment Report (Evaluacion Prototipo)

**Project:** HerStory / UBXAT (IA Neuro-Simbólica)  
**Basis:** `WIKIDATA_MAPPING_STRATEGY.md` + dataset “Fitxa” descriptions  
**Date:** 2026-03-19

---

## 1. Scope and intent

This report assesses the current Wikidata mapping approach in `WIKIDATA_MAPPING_STRATEGY.md`, focusing on:

1. **Property mapping across sources**: mass graves, censored books, and brigadistas.
2. **Gender gaps and intersectionalities**: how to represent multiple social identities and handle missing/inferred values.
3. **Geolocalization**: admin hierarchies and coordinate modeling.
4. **Provenance**: reference-level sourcing for claims (not just a single “source” field).

It also proposes concrete extensions to better align the KG with Wikidata semantics (properties and reference patterns).

---

## 2. What the current strategy does well

### 2.1 Canonical entities and field-to-property mappings

`WIKIDATA_MAPPING_STRATEGY.md` currently defines explicit mappings for three KG entity families:

- **Person / Brigadista** mapped to `Q5` and uses:
  - `P1476` (name/title), `P569` (birth), `P570` (death), `P19`/`P20` (birth/death place),
  - `P27` (nationality), `P106` (occupation), `P1142` (political ideology),
  - `P21` (sex or gender).
- **Mass grave** mapped to `Q108163` and uses:
  - `P1476` (name), `P131` (admin territorial entity), `P625` (coordinates),
  - `P1120` (victim/death count as currently modeled), `P580`/`P582` (start/end),
  - `P575` (time of discovery/invention) for discovery/excavation date.
- **Document** mapped to `Q49848` and uses:
  - `P1476` (document title), `P50` (author), `P577` (publication date),
  - `P248` (stated in / bibliographic source).

This is a strong foundation because it is deterministic and easy to validate with SPARQL coverage tests.

### 2.2 Mapping hygiene: aliases + fallback behavior

The strategy includes:

- `TYPE_ALIAS_MAP` to normalize entity type aliases (person, grave, document, etc.).
- A clear **fallback** plan for unmapped fields: attempt semantic patterns first, otherwise store literal metadata without blocking ingestion.

---

## 3. Assessment: key gaps for the HerStory use-cases

### 3.1 Censored books are not modeled as censorship actions (yet)

The current strategy models “documents” but does not define a first-class mapping for **censorship decisions/acts** and how they relate to **books**.

From `Fitxa...Cultura_y_censura.docx.md`, the censored-books domain includes entities like:

- “expedient de censura” (censorship file),
- “informe del lector” (reader report),
- forms and agents (reader, editor, importer, paper supplier),
- “llibre analitzat” and “llibre publicat”.

Right now, these would likely collapse into generic `Document` nodes, which loses the ability to query:

- which books were prohibited / suppressed,
- by whom (authority),
- where/when the decision applied,
- and with what evidentiary references.

### 3.2 Provenance is too coarse (risk: unverifiable claims)

The strategy uses `P248` at a node/property level, but the KG needs **reference granularity**:

- Each mapped attribute (gender, coordinates, censorship outcome, dates) should carry references.
- For inferred values (gender inferred from name), provenance and uncertainty must be explicit.

Wikidata’s reference model typically uses a **reference set per statement** (e.g., `P248` and/or `P854`/`P813`).

### 3.3 Gender gaps / intersectionalities are underspecified

The strategy notes a known limitation: gender (`P21`) coverage depends on source data.

However, HerStory’s “Fitxa” indicates multiple fields that matter for intersectionality:

- `SIDBRINT` explicitly tracks gender and also categorical dimensions like **religion** and other identity-related taxonomies (as part of “procedència, gènere, religió, etc.”).
- `IHR` includes a schema with gender fields but also repression-related attributes and many date/location dimensions.

The current mapping only covers a single `P21` statement per person, without a pattern for:

- representing **multi-identity assertions** (e.g., gender + religion + nationality),
- modeling **missing** gender (absence) vs **inferred** gender (uncertainty),
- aligning intersectional combinations to queryable structures.

### 3.4 Mass grave “victim count” ambiguity

The strategy maps `victimas_estimadas` to `P1120`.

According to Wikidata semantics, `P1120` is “number of deaths”. In a mass-grave context, “victims” may be:

- deaths,
- casualties (deaths + injuries),
- missing persons,
- or combined estimated counts.

So the KG should either:

- rename the field mapping to “deaths” when `P1120` is used, or
- add additional casualty/missing properties when the dataset distinguishes them.

---

## 4. Recommended Wikidata-aligned extensions

### 4.1 Extend the model: add an explicit “Censorship decision/act” family

Introduce a KG entity family (mapped to a Wikidata-oriented concept) for censorship outcomes:

1. Model “expedient de censura” as a **censorship act/event node**.
2. Model the prohibited/suppressed book/work (“llibre analitzat” / “llibre publicat”) as a **work/book/document node**.
3. Use `Q543` (censorship concept) as the conceptual anchor for the act type.

Then connect the act to the book using Wikidata’s ban/prohibition semantics:

- Use `P8739` (“prohibits”) from a legal act/decision-like subject to the object (the book/work), with context qualifiers when available.

Important constraint: `P8739` has **usage constraints**; it is intended for subjects that are instances/subclasses of legal acts/decisions/policies/taboos (and similar categories). Practically, this means the KG should model the “censorship decision” as a legal/administrative decision item, not as a plain generic document.

### 4.2 Provenance redesign: statement-level evidence pattern

For each mapped attribute, prefer:

- references containing `P248` (“stated in”) pointing to the bibliographic/archival item,
- and/or retrieval evidence via `P813` (“retrieved from”) when the KG is sourced from an external database/site.

If your Neo4j graph currently stores a single `source` field per node, extend it to either:

- statement-level provenance objects (recommended), or
- at least property-level provenance collections (per property assertion).

This is critical for:

- gender values (especially inferred/inaccurate risk),
- geolocation (coordinates vs locality text),
- censorship outcomes (decision text and where it came from).

### 4.3 Intersectional modeling: represent identities as separate, evidence-backed statements

Use “compositional intersectionality” rather than a single combined label:

- Gender: `P21` for sex/gender identity (explicit values only).
- Religion/worldview: `P140` if available from SIDBRINT/IHR.
- Nationality: `P27`.
- Occupation: `P106`.
- Political ideology: `P1142`.
- Ethnicity/ethnic group: `P172` when present in the sources (not currently mapped in the strategy).

For missing vs inferred gender:

- Missing: absence of `P21` (no value).
- Inferred: store `P21` with a reference that clearly indicates inference provenance (and optionally store an “inference method” metadata field in Neo4j even if you do not map it to a Wikidata qualifier).

This allows fairness-oriented queries like:

- “show women/gender non-male persons with reliable gender evidence only”
- “compute gender gap using evidence-qualified counts”.

### 4.4 Geolocalization: use admin hierarchies + coordinates, and respect Wikidata place semantics

The strategy already maps:

- mass graves: `P131` (admin territorial entity) and `P625` (coordinates).

To improve consistency:

- For “administrative” regions: prefer `P131` and ensure that you store only the most local admin level, following Wikidata guidance.
- For “non-administrative locations” and for event locations: prefer `P276` (location) rather than overusing `P131`.

Then, link the censorship act and/or imprisonment/repression events (from IHR) to place entities using the same admin/coordinate patterns.

### 4.5 Mass grave counts: align “victims” to the appropriate casualty semantics

Update the mapping rule set to distinguish:

- deaths: `P1120`
- casualties: if your data provides it as such (otherwise keep `P1120` but rename in your KG to “deaths”)

At minimum, rename the semantic expectation in the KG so users know whether the number is “deaths” or “estimated victims”.

---

## 5. Proposed mapping tables (extension-focused)

### 5.1 Person / Brigadista (Q5)

Keep the existing mapping, and add (when fields exist in the “Fitxa”):

- Religion: map SIDBRINT “religió” (if present) to `P140`.
- Ethnicity (if present in sources): map to `P172`.
- For intersectional querying: ensure each identity statement is reference-backed (see provenance redesign).

### 5.2 MassGrave (Q108163)

Keep:

- `P131` admin territorial entity
- `P625` coordinate location
- `P575` time of discovery/excavation
- `P580`/`P582` start/end

Refine:

- Rename the victim-count mapping semantics to “deaths” when using `P1120`.

### 5.3 Censored book domain (new act/event family + book/work)

Map from `Cultura_y_censura` entities:

- `expedient de censura` (censorship file) => censorship act/event node (conceptually `Q543`)
- `llibre analitzat` / `llibre publicat` => book/work node
- Decision outcome => connect act -> book via `P8739` (“prohibits”), subject modeled as a legal act/decision-like item
- Add evidence:
  - decision text -> references (`P248` and/or `P813`/URL references in your KG)

Optionally, map `informe del lector` and `lector`:

- report as `Document` with `P50` if an author/reader person exists
- reader as `Person` and link report author.

### 5.4 IHR repression domain (Person + events + provenance)

Use `IHR` schema (as described in its Fitxa):

- Persons: map identity fields to `Q5` with `P21` only when reliable.
- Dates/places: map to event/time properties with `P131`/`P625` patterns.
- Repression type: model as `Concept` nodes and link to the repression event/document with a consistent property in your KG (even if not fully mapped to a single Wikidata PID initially).

---

## 6. Validation checklist (what to test next)

1. **IRI/property alignment**: ensure `P575` uses “time of discovery/invention” semantics; verify it is consistent across mass grave datasets.
2. **Gender coverage**: compute gender gap counts with:
   - all records with `P21`
   - records with `P21` + strong evidence references.
3. **Censorship queryability**:
   - “books prohibited by X authority”
   - “books prohibited in region/time”
4. **Provenance completeness**:
   - % of mapped statements with `P248`/retrieval references.
5. **Geolocation quality**:
   - % of items with `P625` with valid coordinate precision
   - consistency between admin labels (`P131`) and coordinates.

---

## 7. References (Wikidata property semantics)

- `P575` time of discovery or invention: [Property:P575](https://m.wikidata.org/wiki/Property:P575)
- `P21` sex or gender: [Property:P21](https://www.wikidata.org/wiki/Property:P21)
- `P248` stated in: [Property:P248](https://www.wikidata.org/wiki/Property:P248)
- `P813` retrieved from: [Property:P813](https://www.wikidata.org/wiki/Property:P813)
- `P131` located in the administrative territorial entity: [Property:P131](https://www.wikidata.org/wiki/Property:P131)
- `P625` coordinate location: [Property:P625](https://www.wikidata.org/wiki/Property:P625)
- `P8739` prohibits (ban/prohibition semantics + constraints): [Property:P8739](https://www.wikidata.org/wiki/Property:P8739)
- `Q543` censorship (concept anchor): [censorship (Q543)](https://www.wikidata.org/wiki/Q543)
- `P1120` number of deaths: [1120 - Wikidata](https://www.wikidata.org/wiki/Q19542)
- `P140` religion or worldview: [Property:P140](https://www.wikidata.org/wiki/Property:P140)
- `P1476` title: [Property:P1476](https://m.wikidata.org/wiki/Property:P1476)

