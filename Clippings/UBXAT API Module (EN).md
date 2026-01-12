---
title: UBXAT API Module (EN)
source: UBXAT API Module (EN).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---
[[UBXAT API Module (EN)]]

UBXAT API MODULE
Overview
REST API service that provides programmatic access to the UBXAT: ETL pipeline. Enables ETL processing,
SPARQL/Cypher queries, and conversational interactions with the knowledge graph.
Architecture
Core Components
CognitiveETLService: Main service class managing ETL operations, Neo4j connections, and AI integrations
GroundTruthMapper: Dynamic entity resolution using ground truth data as source of truth
Pipeline Integration: Direct access to LangGraph ETL pipeline for processing
FastAPI Application: REST API server with automatic OpenAPI documentation
Key Classes
ProcessRequest: ETL processing job parameters
SparqlRequest: SPARQL query execution parameters
ChatRequest: Conversational query parameters
Response models for structured API responses
Endpoints
ETL Operations
POST /api/v1/etl/process: Execute ETL pipeline on input files
GET /api/v1/etl/status/{job_id}: Check processing job status
Query Operations
POST /api/v1/sparql: Execute SPARQL queries against knowledge graph

POST /api/v1/chat: Conversational queries with AI-powered responses
System Operations
GET /api/v1/status: Service health and configuration status
GET /api/v1/metrics: Processing metrics and performance data
GET /api/v1/health: Basic health check
GET /api/v1/ground-truth: Available ground truth mappings
File Operations
GET /api/v1/files: List available input files
POST /api/v1/files/upload: Upload files for processing
Data Flow
ETL Processing Flow
1. Receive processing request with file paths and parameters
2. Validate input files and determine data formats
3. Execute LangGraph pipeline with Gemini AI components
4. Store results in Neo4j knowledge graph
5. Return processing status and metrics
Query Processing Flow
1. Receive SPARQL or natural language query
2. Extract search terms using ground truth mappings
3. Gather relevant context from Neo4j
4. Generate AI-powered response using Gemini
5. Return structured response with sources

Conversational Flow
1. Parse natural language question
2. Extract entities using dynamic keyword mapping
3. Query knowledge graph for relevant context
4. Generate conversational response with Gemini
5. Include source references and confidence scores
Ground Truth Integration
The API uses ground truth data for dynamic behavior:
Entity Resolution: Maps Wikidata QIDs to entity types using ground truth
Keyword Extraction: Generates search terms from table names and field mappings
Query Generation: Creates Cypher queries using schema information from ground truth
Label Generation: Produces human-readable labels from ground truth table names
Dependencies
External Services
Neo4j: Graph database for knowledge graph storage
Google Gemini: AI model for analysis and response generation
Google Vertex AI: Alternative AI service provider
Python Libraries
FastAPI: Web framework for API endpoints
LangChain: Integration with AI models
Pydantic: Data validation and serialization
Neo4j Python Driver: Database connectivity
Configuration
Environment Variables
NEO4J_URI: Neo4j connection string

NEO4J_USERNAME: Neo4j authentication username
NEO4J_PASSWORD: Neo4j authentication password
GOOGLE_GENAI_API_KEY: Gemini API key
Configuration Files
config/default.yaml: Main configuration with processing parameters
data/ground_truth/*.json: Ground truth mappings for dynamic behavior
Error Handling
400: Bad request parameters
404: Resource not found
500: Internal server error
503: Service unavailable (Neo4j connection issues)
All errors include detailed error messages and appropriate HTTP status codes.
Usage
# Start API server
python api/api.py --host 0.0.0.0 --port 8000
# Example ETL request
curl -X POST "http://localhost:8000/api/v1/etl/process" \
  -H "Content-Type: application/json" \
  -d '{"input_path": "data/input/file.sql", "recursive": false}'
# Example SPARQL query
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT ?person WHERE { ?person rdf:type <http://www.wikidata.org/entity/Q5> }"}'
# Example chat query
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{"question": "Who were the brigadistas?", "context_limit": 50}'
