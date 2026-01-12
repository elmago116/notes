---
title: UBXAT - Readme (EN)
source: UBXAT - Readme (EN).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---

UBXAT: TECHNICAL DOCUMENTATION
Technical Architecture Overviewubxatii/
src/cognitive_etl/Core ETL engine
graph_builder.pyLangGraph pipeline orchestrationnodes/Processing nodesmodels.pyData models and state definitionsconfig.pyPydantic configuration models
parser.pyDynamic data parsing with GroundTruthMappergemini_*.pyAI-powered processing nodes executor.pyNeo4j execution
api/REST API service
api.pyFastAPI application with CognitiveETLServiceREADME.mdAPI endpoint documentation
data/Data and configuration
ground_truth/JSON mapping files for dynamic behaviorinput/Raw data files for processingoutput/Processed results
config/YAML configuration files
default.yamlMain system configuration
Data Flow
1. Input Processing: Files enter via API or CLI
2. Ground Truth Loading: Dynamic mappers initialize from JSON files
3. LangGraph Pipeline: Sequential processing through AI nodes
4. Neo4j Storage: Results stored as Wikidata-compliant knowledge graph
5. API Responses: Query results returned via REST endpoints
Installation & Configuration
Prerequisites
Python 3.8+
Neo4j Aura account or local Neo4j instance
Google Gemini API key
Environment Setup
Create .env file:
# Neo4j Configuration
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password
# Google Gemini API
GOOGLE_GENAI_API_KEY=your-gemini-api-key
# Processing Parameters

COGNITIVE_ETL_BATCH_SIZE=100
COGNITIVE_ETL_MAX_RETRIES=3
Configuration Files
config/default.yaml
vertexai:
  project: "your-gcp-project"
  location: "us-central1"
  model: "gemini-2.0-flash-lite"
  api_key: "${GOOGLE_GENAI_API_KEY}"
neo4j:
  uri: "${NEO4J_URI}"
  user: "${NEO4J_USERNAME}"
  password: "${NEO4J_PASSWORD}"
processing:
  batch_size: 100
  max_retries: 3
  timeout_seconds: 300
ground_truth:
  base_path: "data/ground_truth"
Usage
Command Line Interface
# Process single file
python main.py --config config/default.yaml --input data/input/file.sql
# Process directory recursively
python main.py --config config/default.yaml --input data/input/ --recursive
# Custom batch size
python main.py --config config/default.yaml --input data/input/file.sql --batch-size 50
REST API

Start API Server
python api/api.py --host 0.0.0.0 --port 8000
ETL Processing
curl -X POST "http://localhost:8000/api/v1/etl/process" \
  -H "Content-Type: application/json" \
  -d '{
    "input_path": "data/input/fosas_comunes.sql",
    "recursive": false,
    "data_format": "auto",
    "batch_size": 100
  }'
SPARQL Queries
curl -X POST "http://localhost:8000/api/v1/sparql" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT ?person ?name WHERE { ?person rdf:type <http://www.wikidata.org/entity/Q5> }"
  }'
Conversational Queries
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Who were the brigadistas?",
    "context_limit": 50
  }'
Ground Truth System
Purpose
Ground truth files enable dynamic behavior without hardcoded mappings. The system learns from these
JSON files to:
Map table names to entity types
Resolve Wikidata QIDs to entity categories

Generate appropriate labels for different data types
Adapt to new data schemas automatically
File Structure
{
  "metadata": {
    "source": "dataset_name",
    "entity_type": "Q5"
  },
  "table_mappings": {
    "table_name": {
      "column_mappings": {
        "field_name": {"wikidata_property": "P1476"}
      }
    }
  }
}
Dynamic Behavior
Entity Resolution: QIDs in ground truth determine entity types
Label Generation: Table names become human-readable labels
Field Mapping: Column names guide semantic mapping
Adaptability: New ground truth files extend system capabilities
Development
Project Structure
Project Structure ubxatii/
src/cognitive_etl/Core engine
__init__.pyPackage exportsconfig.pyPydantic modelsgraph_builder.pyLangGraph orchestrationmodels.pyData modelsnodes/Processing nodes
__init__.pyNode exportsbase.pyBase classesparser.pyDynamic parsing gemini_*.pyAI nodesexecutor.pyNeo4j execution
api/REST API
__init__.pyapi.pyFastAPI appREADME.mdAPI docs
data/Data files
ground_truth/JSON mappingsinput/Raw dataoutput/Results
config/Config files
default.yamlMain config
tests/Test suitesmain.pyCLI entry point
Adding New Data Sources

1. Extend Parser (src/cognitive_etl/nodes/parser.py):
class NewFormatParser(BaseParser):
    def parse_file(self, file_path: str, data_format: DataFormat) -> List[DataChunk]:
        # Implement parsing logic
        pass
2. Update Ground Truth (data/ground_truth/):
{
  "table_mappings": {
    "new_table": {
      "column_mappings": {"field": {"wikidata_property": "P123"}}
    }
  }
}
3. Register in DataParser (src/cognitive_etl/nodes/parser.py):
self.parsers = {
    'new_format': NewFormatParser(config, self.ground_truth_mapper),
    # ... existing parsers
}
Testing
# Run all tests
python -m pytest tests/
# Run specific test file
python -m pytest tests/integration/test_setup.py
# Run with coverage
python -m pytest --cov=src tests/
Debugging
# Enable debug logging
export PYTHONPATH=src:$PYTHONPATH
python -c "
import logging

logging.basicConfig(level=logging.DEBUG)
# Run your code
"
# Check ground truth loading
python -c "
from src.cognitive_etl.nodes.parser import GroundTruthMapper
mapper = GroundTruthMapper()
print(f'Loaded {len(mapper.mappings)} mappings')
for name in mapper.mappings.keys():
    print(f'  - {name}')
"
Performance Tuning
Batch Size: Adjust batch_size in config for memory/performance balance
Retries: Increase max_retries for unreliable network conditions
Caching: Ground truth is loaded once at startup for performance
