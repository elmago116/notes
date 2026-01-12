---
title: UBXAT SPARQL (EN)
source: UBXAT SPARQL (EN).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---
[[UBXAT SPARQL (EN).pdf]]

UBXAT SPARQL INTEGRATION GUIDE
Technical documentation for SPARQL query integration with the UBXAT knowledge graph.
Overview
UBXAT provides SPARQL 1.1 query capabilities over historical knowledge graphs stored in Neo4j. The system
automatically translates SPARQL queries to Cypher for execution against the underlying graph database.
SPARQL Endpoint
Base URL
POST http://localhost:8000/api/v1/sparql
Request Format
{
  "query": "SPARQL query string",
  "format": "json"
}
Response Format
{
  "results": [
    {
      "variable1": {"value": "result_value", "type": "literal|uri"},
      "variable2": {"value": "result_value"}
    }
  ]
}
Supported SPARQL Features

Query Types
SELECT Queries
Basic triple patterns: ?subject ?predicate ?object
FILTER clauses: Basic string and numeric comparisons
LIMIT/OFFSET: Result pagination
ASK Queries
Boolean queries: Check for pattern existence
Supported: Basic ASK queries
COUNT Queries (Extended)
Custom COUNT syntax: COUNT(?variable)
Automatic translation: To optimized Cypher aggregation queries
SPARQL-to-Cypher Translation
The system automatically translates SPARQL queries to Cypher using ground truth mappings:
Example Translations
SPARQL:
SELECT ?person ?name WHERE {
  ?person rdf:type <http://www.wikidata.org/entity/Q5> .
  ?person <http://www.wikidata.org/prop/direct/P1476> ?name
}
LIMIT 10
Generated Cypher:
MATCH (person:Entity)
WHERE person.type = 'Q5' AND exists(person.name)
RETURN person.id as person, person.name as name
LIMIT 10

Ground Truth Enhanced Cypher:
MATCH (n:Entity)
WHERE n.text CONTAINS 'brigadista' OR n.text CONTAINS 'persona'
RETURN n.id as person, n.title as name
LIMIT 10
Ground Truth Integration
Dynamic Entity Resolution
SPARQL variables are resolved using ground truth mappings:
Q5 (human) →  Maps to tables containing "brigadista", "persona", "voluntario"
Q108163 (mass grave) →  Maps to tables containing "fosa", "enterramiento"
Q49848 (document) →  Maps to tables containing "documento", "fuente"
Automatic Query Enhancement
The system enhances SPARQL queries with ground truth intelligence:
1. Variable Resolution: Maps SPARQL variables to ground truth entity types
2. Field Mapping: Uses ground truth to determine relevant search fields
3. Query Optimization: Generates efficient Cypher based on learned patterns
Usage Examples
Basic Entity Queries
Find All Persons
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT ?person ?name WHERE { ?person rdf:type <http://www.wikidata.org/entity/Q5> ; <ht
  }'

Find Mass Graves
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT ?grave ?location WHERE { ?grave rdf:type <http://www.wikidata.org/entity/Q108163
  }'
Count Queries
Count Brigadistas
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT (COUNT(?person) as ?count) WHERE { ?person rdf:type <http://www.wikidata.org/ent
  }'
Advanced Queries
Find Documents by Author
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT ?doc ?title ?author WHERE { ?doc rdf:type <http://www.wikidata.org/entity/Q49848
  }'
Integration Patterns
Python Client
import requests
class UBXATSparqlClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def query(self, sparql_query):
        response = requests.post(
            f"{self.base_url}/api/v1/sparql",
            json={"query": sparql_query}
        )
        return response.json()
# Usage
client = UBXATSparqlClient()
results = client.query("""
    SELECT ?person ?name WHERE {
        ?person rdf:type <http://www.wikidata.org/entity/Q5> .
        ?person <http://www.wikidata.org/prop/direct/P1476> ?name
    } LIMIT 10
""")
JavaScript/Node.js Client
class UBXATSparqlClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
    }
    async query(sparqlQuery) {
        const response = await fetch(`${this.baseUrl}/api/v1/sparql`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: sparqlQuery })
        });
        return response.json();
    }
}
// Usage
const client = new UBXATSparqlClient();
const results = await client.query(`
    SELECT ?person ?name WHERE {
        ?person rdf:type <http://www.wikidata.org/entity/Q5> .
        ?person <http://www.wikidata.org/prop/direct/P1476> ?name
    } LIMIT 10
`);
Command Line Tool
# Save query to file
cat > query.sparql << 'EOF'
SELECT ?person ?name WHERE {

  ?person rdf:type <http://www.wikidata.org/entity/Q5> .
  ?person <http://www.wikidata.org/prop/direct/P1476> ?name
} LIMIT 10
EOF
# Execute query
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d @<(jq -n --arg query "$(cat query.sparql)" '{query: $query}')
Wikidata Property Mappings
Common Properties
Wikidata Property SPARQL Property Description
P1476 wdt:P1476 Title
P569 wdt:P569 Date of birth
P570 wdt:P570 Date of death
P27 wdt:P27 Country of citizenship
P625 wdt:P625 Coordinate location
P50 wdt:P50 Author
P577 wdt:P577 Publication date
Entity Types
Wikidata Entity Description
Q5 Human/Person
Q108163 Mass grave
Q49848 Document
Q17334923 Location
Performance Considerations

Query Optimization
1. Use LIMIT: Always limit result sets for performance
2. Filter early: Apply restrictive filters first
3. Ground truth awareness: System automatically optimizes based on learned patterns
Caching Strategy
Ground truth mappings are cached at startup
Entity type resolutions are computed once per query type
Cypher translations are generated dynamically per query
Error Handling
Common Errors
Invalid SPARQL Syntax
{
  "detail": "SPARQL parsing failed: Invalid syntax"
}
Unsupported Features
{
  "detail": "SPARQL feature not supported: OPTIONAL clauses"
}
Ground Truth Missing
{
  "detail": "No ground truth mapping available for entity type"
}

Error Recovery
1. Simplify queries: Remove complex SPARQL features
2. Check entity types: Ensure QIDs are in ground truth mappings
3. Use basic patterns: Start with simple triple patterns
Extending SPARQL Support
Adding New Entity Types
1. Update ground truth: Add new entity mappings to JSON files
2. Test queries: Verify new entity types work with SPARQL
3. Update documentation: Add new entity examples
Supporting New SPARQL Features
1. Extend translator: Modify _generate_cypher_from_sparql_with_ground_truth()
2. Add test cases: Ensure new features work correctly
3. Update documentation: Document new supported features
Troubleshooting
Query Returns Empty Results
1. Check if data exists in Neo4j
2. Verify ground truth mappings are loaded
3. Test with simpler queries first
Performance Issues
1. Add LIMIT clauses to queries
2. Check Neo4j query execution plans
3. Review ground truth mappings for optimization opportunities

Integration Issues
1. Verify API endpoint is accessible
2. Check authentication if required
3. Validate SPARQL syntax with a SPARQL validator
Future Enhancements
Full SPARQL 1.1 support: OPTIONAL, UNION, subqueries
Federated queries: Query multiple knowledge graphs
Result caching: Cache frequent query results
Query optimization: Advanced Cypher generation strategies
