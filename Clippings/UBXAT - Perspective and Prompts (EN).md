---
title: UBXAT - Perspective and Prompts (EN)
source: UBXAT - Perspective & Prompts (EN).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---

[[PDF/Peninsula/UBXAT - Perspective & Prompts (EN).pdf]]

## PERSPECTIVE ON PROMPTS IN UBXAT

### Overview

UBXAT uses a unified concept approach where entities like "author", "person", "brigadista" are gender-neutral by default. However, the system maintains gender information through Wikidata property P21 (sex or gender) to enable gender-specific queries when needed.

### Core Principles

#### 1. Unified Concepts

Entities in UBXAT are represented using gender-neutral concepts:

- **Author (P50)**: Represents any author regardless of gender
- **Person (Q5)**: Represents any human entity
- **Brigadista**: Represents any international brigade member

This approach ensures that:

- Data modeling remains consistent
- Queries can work without gender specification
- Gender information is preserved but not required

#### 2. Gender Storage

Gender information is stored using Wikidata Property P21 (sex or gender). The `normalize_gender` transformation ensures consistent gender values across the knowledge graph.

### Querying by Gender

**Natural Language Queries**

When asking about women or men in natural language, the system understands gender-specific requests.

Examples:

- Query about women: "How many women were in the international brigades?"; "List all female authors in the database"; "Show me documents written by women"
- Query about men: "How many men were brigadistas?"; "Find all male authors"
- Gender-neutral: "List all authors"; "Show me all brigadistas"; "Find documents by any author"

**SPARQL Queries**

To query specifically for women, use P21 with appropriate gender values. Example: Find all women who were brigadistas (SELECT ?person ?name ?gender WHERE { ?person rdf:type wd:Q5 ; wdt:P1476 ?name ; wdt:P21 ?gender . FILTER(...) }). Similar pattern for men and for documents by female authors.

**Cypher Queries**

The system automatically translates SPARQL to Cypher. Direct Cypher example: MATCH (person:Entity) WHERE person.type = 'Q5' AND person.gender IS NOT NULL AND (person.gender CONTAINS 'female' OR person.gender CONTAINS 'woman' OR person.gender CONTAINS 'mujer') RETURN person.id, person.title, person.gender LIMIT 100.

### Prompt Engineering for Gender-Aware Queries

**Conversational API (/api/v1/chat)**

The system automatically handles gender-aware queries through context-aware prompts:

1. **Detects gender-specific terms**: "women", "female", "mujer", "mujeres"; "men", "male", "hombre", "hombres"
2. **Enhances the query with gender context**: e.g. User: "How many women were brigadistas?" → Entity type: Q5; Gender filter: P21 = female/woman; Additional context from knowledge graph
3. **Generates appropriate response** using the enhanced context

**Best Practices for Prompts**

- Good: Specific and clear ("List all female authors who wrote about the Spanish Civil War"; "How many women brigadistas came from the United States?"); gender-neutral when appropriate ("List all authors"; "Show all brigadistas")
- Avoid: Vague gender references ("Show me the authors" when you mean female authors); mixed concepts ("Women and documents" — unclear relationship)

### Implementation Details

**Ground Truth Mapping**

Gender information is mapped through ground truth files:

- File: `data/ground_truth/sidbrint_consolidated_wikidata_mapping.json` — field_brigadista_genere → P21, property_label "sex or gender", transformations: ["normalize_gender"]
- File: `data/ground_truth/autor_wikidata_mapping.json` — relationships.author → P50, target_class Q5 (author is always a person; person can have P21; traversal: Document → P50 → Person → P21 → Gender)

### Examples

**Example 1: Counting Women Brigadistas**

Natural Language: "How many women were in the international brigades?"

SPARQL: SELECT (COUNT(?person) as ?count) WHERE { ?person rdf:type wd:Q5 . ?person wdt:P21 ?gender . FILTER(regex(?gender, "female|woman|mujer", "i")) }

Expected response: { "count": 150, "context": "Found 150 women in the international brigades database" }

**Example 2: Documents by Female Authors**

Natural Language: "Show me all documents written by women"

SPARQL: SELECT ?doc ?title ?authorName WHERE { ?doc rdf:type wd:Q49848 . ?doc wdt:P1476 ?title . ?doc wdt:P50 ?author . ?author wdt:P1476 ?authorName . ?author wdt:P21 ?gender . FILTER(regex(?gender, "female|woman|mujer", "i")) } LIMIT 50

**Example 3: Gender Distribution Analysis**

Natural Language: "What is the gender distribution of brigadistas by country?"

SPARQL: SELECT ?country ?gender (COUNT(?person) as ?count) WHERE { ?person rdf:type wd:Q5 . ?person wdt:P21 ?gender . ?person wdt:P27 ?country . } GROUP BY ?country ?gender ORDER BY ?country ?gender

### Wikidata Gender Values (QIDs)

- Q6581072: female; Q6581097: male; Q1052281: transgender female; Q2449503: transgender male; Q1097630: intersex; Q48270: non-binary. The system normalizes various representations to these standard values.

### Troubleshooting

**Issue: Gender queries return no results**

Possible causes: Gender data not present in source data; gender values not normalized correctly; query filter too restrictive.

Solution: Check what gender values exist with SELECT DISTINCT ?gender (COUNT(?person) as ?count) WHERE { ?person rdf:type wd:Q5 . ?person wdt:P21 ?gender . } GROUP BY ?gender

**Issue: Author queries don't include gender**

Possible causes: Author relationship not properly linked to person entity; person entity missing gender property.

Solution: Verify author-person-gender chain with SELECT ?doc ?author ?gender WHERE { ?doc rdf:type wd:Q49848 . ?doc wdt:P50 ?author . OPTIONAL { ?author wdt:P21 ?gender . } } LIMIT 10

### Summary

- Unified concepts (author, person) are gender-neutral by design
- Gender information is preserved via Wikidata P21 property
- Gender-specific queries are supported through natural language and SPARQL
- Prompts automatically detect gender-specific terms and enhance queries
- Ground truth mappings ensure consistent gender data handling
- The system works with unified concepts while maintaining the ability to query and analyze data by gender when needed
