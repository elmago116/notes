---
tags:
  - op/doc/reporte
authors:
  - Elena Gómez
date: 2026-02-01
---
[[Peninsula UBXAT - Tests realizados]]
[[UBXAT digestión de procesos]]
[[UBXAT SPARQL (EN)]]
[[UBXAT API Module (EN)]]
[[UBXAT_Workflow_Explanation]]
[[Memoria tecnica Peninsula - Lista de requisitos]]

Se realizarán tres formas de evaluación para definir compliance de la entrega: 
1. Un checklist minucioso de todos los elementos acordados (según el documento)
2. Ejercicios con cada módulo según la documentación aportada para los mismos en las guías de uso. 
3. Un ejercicio comparativo propuesto por la UB para comparación de resultados.

# Lista de chequeo desde Memoria Técnica y manuales

Se aplicará el siguiente checklist de presencia/ausencia de elementos acordados dependiendo del documento que los sugiere como funcionales. Se aplicará el siguiente checklist de presencia/ausencia de elementos acordados dependiendo del documento que los sugiere como funcionales. Se mantendrá el idioma del documento para mantener la coherencia.

## 1. Documento fuente: [[Memoria tecnica - planteamiento incial del proyecto.pdf]]

### Col·laboració i equips
- [ ] Definir composició dels equips (Peninsula i UB) i responsabilitats per fase — *No documentat als guides*
- [ ] Peninsula: PM, arquitecte, desenvolupadors (NLP, ML, grafs), expert dades, expert UI/accessibilitat — *No documentat*
- [ ] UB: IP, requisits funcionals, selecció de dades, model de dades, avaluació i validació — *No documentat*
- [ ] Integrar estudiant de doctorat — *No documentat*
- [ ] Canals de comunicació, reunions, eines, metodologia (Gantt, riscos, comitè) — *No documentat*
- [ ] Transferència de coneixement, documentació, repositori — *No documentat*
### Dades
 - [ ] Selecció de dades obertes (rellevància, qualitat, formats, llicències) — *ONTOLOGY_GUIDE: fonts CSV, RDF, SQL; qualitat via validació*
- [ ] Fonts: dades estructurades (CSV, JSON, RDF) i no estructurades — *Guides: CSV, RDF, SQL; text via LLM*
- [ ] Processament: neteja, transformació, integració; NER/relacions; record linking, schema mapping — *GROUND_TRUTH: TYPE_ALIAS_MAP, ONTOLOGICAL_PROPERTY_MAP, RELATIONSHIP_RULES, integració al graf*
### Programari i tecnologies
- [ ] Grafs de coneixement: Neo4j (representació, consultes, raonament) — *Memoria: Neo4j (representació, consultes, raonament). Sprint: grafo de conocimiento, endpoint SPARQL*
- [ ] **IA/LLM**: Langchain (MLE externs, pipelines, agents); Node.js informes/panells — *Memoria: Langchain (MLE externs, pipelines de text, agents de diàleg); Node.js informes i panells*
- [ ] Python; PyTorch, TensorFlow — *Memoria: Python; llibreries Pytorch i Tensorflow*
- [ ] PostgreSQL (dades no graf, geo, vectors) — *Memoria: PostgreSQL, dades relacionales, extensions geoespacials, indexació de vectors*
- [ ] Stack codi obert memòria (Transformers, RDFlib, NetworkX, React/Vue, Docker) — *Memoria: Hugging Face Transformers, PyTorch/TensorFlow, RDFlib, NetworkX, Matplotlib/Seaborn, React o Vue.js, Docker*
- [ ] Integració: Flask/FastAPI, RabbitMQ/Kafka, NiFi/Airflow, Docker/Kubernetes — *Memoria: Flask/FastAPI/Django, RabbitMQ/Kafka, Apache NiFi/Airflow, Docker i Kubernetes. Sprint: endpoint SPARQL, redeploy*

### Llicències i drets d’ús
- [ ] Dades: CC BY/BY-SA, Open Data Commons; no ús sense llicència — *No documentat*
- [ ] Programari: MIT/Apache/BSD/GPL; README amb llicències; control UB — *No documentat*
### Accessibilitat i documentació
- [ ] Organitzar dades i codi; documentar — *Memoria: Accessibilitat i documentació; organitzar dades i codi de manera estructurada i documentar exhaustivament*
- [ ] Dades: estructura jeràrquica, metadades en JSON, esquema del graf documentat — *Parcial: esquema implícit a CELIRU; metadades JSON no*
- [ ] Codi: mòduls (NLP, graf, UI, dades), Git, README, manual, desplegament — *Guides: mòduls backend; README/manual no*

### Requisits funcionals i de disseny
1. **Interfície d’usuari**
- [ ] Interfície neta, minimalista, accessible (WCAG), paleta, tipografia — *Memoria: Interfície d'usuari; neta i minimalista; paleta de colors suau; tipografia clara, estàndards d'accessibilitat web*
- [ ] Responsive (escriptori, mòbil, tauleta) — *Memoria: disseny responsive (escriptori, portàtil, tauleta, mòbil)*
- [ ] Cerca intel·ligent, navegació, menús, formularis — *Memoria: barra de navegació, menús desplegables, botons, formularis; funció de cerca intel·ligent (paraules clau o frases, resultats per coincidència)*
- [ ] Accessibilitat: contrastos, text alternatiu, teclat, mida de text, personalització — *Memoria: contrastos adequats; text alternatiu; navegació per teclat i focus visible; control de mida de text; WCAG; opcions de personalització (colors, mida de font, tema)*

2. **NLP**
- [ ] Anàlisi semàntica, entitats, relacions, desambiguació — *Memoria: NPL; anàlisi semàntica, entitats, conceptes i relacions; desambiguació lèxica; anàlisi de dependències; word embeddings*
- [ ] NER i RE — *Memoria: NER (reconeixement d’entitats nombrades) i RE (relació entre entitats)*
- [ ] Topic modeling — *Memoria: topic modeling per a temàtiques i indexació*
- [ ] Generació de respostes: LLM, coherència amb context — *Memoria: generació de respostes amb LLM pre-entrenats; coherència amb el context; aprenentatge per reforç; resum; classificació per rellevància*
- [ ] Fine-tuning, feedback d’usuaris, monitoratge — *Memoria: feedback d’usuaris per entrenar models; fine-tuning; monitoratge de rendiment i detecció d’errors/inconsistències*
- [ ] Monitoratge de rendiment i errors — *Memoria: monitoratge de rendiment i detecció d’errors/inconsistències*

3. **Raonament simbòlic**
- [ ] Inferència sobre el graf; consultes tipus SPARQL; relacions implícites — *Memoria: inferència lògica sobre el graf; consultes SPARQL; deducció de relacions implícites. Sprint: endpoint SPARQL, consultes al grafo*
- [ ] Raonament basat en regles — *Memoria: raonament basat en regles (rule-based reasoning). Sprint: regles segons document de Miquet, restriccions i validacions*
- [ ] Ontologies (classes, propietats, relacions); vocabulari controlat; OWL; ontologies gènere — *Memoria: ontologies formals (OWL); vocabulari controlat (LOV); ontologies per a diversitat de gènere i interseccionalitats*
- [ ] Integració amb LLM: graph embeddings, prompt engineering —*Memoria: graph embeddings; prompt engineering (Langchain) per guiar respostes amb informació del graf; rule induction*
- [ ] Motor Neo4j; avaluació del raonament — *Memoria: motor de raonament Neo4j; tècniques d’avaluació per mesurar eficàcia del raonament i qualitat de les respostes. Sprint: tasques sobre mapeo, regles, endpoint SPARQL, testing*

4. **Integració**
- [ ] APIs REST (HTTP, JSON) documentades i exemples — *Memoria: APIs REST (HTTP, JSON) per consultar el graf, consultes en llenguatge natural, respostes estructurades; documentació detallada i exemples*
- [ ] Missatgeria (RabbitMQ, Kafka), logs, alertes — *Memoria: missatgeria asíncrona (RabbitMQ, Kafka) per sistemes heterogenis, monitoratge, logs i alertes*
- [ ] ETL / connectors (SQL, CSV, web); mapatge al graf — *Memoria: mecanismes ETL, connectors (SQL, CSV, serveis web), mapatge de dades al graf. Sprint: ingesta SQL al graf, mapeo nodos/relaciones a Wikidata*
- [ ] Microserveis, APIs, escalabilitat — *Memoria: arquitectura basada en microserveis; comunicació via APIs; escalabilitat i substitució de components*

5. **Inclusió i diversitat**
- [ ] Criteris de selecció de dades (gènere, interseccionalitats), revisió de biaixos — *Memoria: Inclusió i diversitat; prioritat a dades que reflecteixin diversitat de gènere i interseccionalitats; evitar biaixos; revisió manual per identificar biaixos*
- [ ] Representació (cis/trans/no binari, ètnia, orientació) — *Memoria: dades sobre persones cisgènere, transgènere i no binàries; orígens ètnics, cultures, orientacions sexuals i identitats de gènere*
- [ ] Augmentació/dades sintètiques identificades — *Memoria: augmentació de dades / dades sintètiques només si cal i identificades com a tals; preferència per dades reals*
- [ ] Entrenament: desbiaixament, supervisió per equitat — *Memoria: regularització i desbiaixament; supervisió del rendiment per a equitat i imparcialitat; classificació de dades per gènere, ètnia, etc.*

6. **Responsabilitat ètica i qualitat**
- [ ] Proves unitàries, integració, rendiment, usabilitat, acceptació UB — *Memoria: proves unitàries; proves d’integració; proves de rendiment; proves d’usabilitat amb usuaris reals; proves d’acceptació per la UB; gestió de canvis i d’errors. Sprint: proves unitàries per a les regles (Tarea 4); testing ingesta SQL (Tarea 6); testing endpoint SPARQL (Tarea 7); smoke test post-despliegue (Tarea 8); demo i revisió (Tarea 9)*
- [ ] Explicabilitat / transparència — *Memoria: tècniques d’explicabilitat (paraules/frases rellevants; visualització de relacions en grafs); interpretability en llenguatge natural*
- [ ] Privacitat: anonimització, consentiment, dades públiques, seguretat — *Memoria: Privacitat; anonimització; no recollir dades personals sense consentiment; dades externes d’accés públic; mesures de seguretat*
- [ ] Biaixos: monitoratge, auditoria, feedback i correcció — *Memoria: monitoratge continu per detectar tendències discriminatoris; auditoria algorítmica; mecanisme de feedback per respostes inadequades i correcció de biaixos/estereotips*

## 2. Documentos fuente: [[Guia Plataforma Web (ES)]] / [[Web Platform User Guide (EN)]]

1. **Funcionalidades Principales:**
	1. Interacción mediante lenguaje natural: 
	- [ ] Consultas directas sobre registros de brigadistas,
	- [ ] geolocalización de fosas y fuentes documentales. 
	 2. **Análisis visual de datos:** 
	- [ ] Exploración de un grafo interactivo que representa las entidades y sus relaciones. 
	3. **Consultas técnicas (SPARQL)**: 
	- [ ] Ejecución de consultas complejas sobre la base de datos de conocimiento. 
	4. **Ingesta y procesamiento de datos:** 
	- [ ] Herramientas para la carga y transformación de nuevos activos de información. 
	5. **Monitorización del sistema:** 
	- [ ] Supervisión del estado operativo de los servicios en tiempo real.
2. Módulo agente: 
	1. Capacidades 
	- [ ] Evaluación de confianza: Un indicador visual (verde, amarillo o rojo) determina el grado de fiabilidad de la respuesta generada.
	- [ ] Trazabilidad de información: El sistema muestra los “chips” de fuentes consultadas, permitiendo verificar el origen de los datos
	- [ ] Métricas de rendimiento: Visualización del tiempo de procesamiento de cada respuesta.
	- [ ] Gestión de historial: Herramientas para copiar respuestas al portapapeles o reiniciar la sesión de chat para nuevas consultas.
3. Módulo grafo de conocimiento: 
	- [ ] Clasificación de entidades por nodos (Nodos Rojos: Personal (Brigadistas). Nodos Azules: Localizaciones geográficas y eventos históricos. Nodos Verdes: Documentación y archivos de referencia. Nodos Naranjas: Registros de fosas comunes.)
	- [ ] Navegación: El usuario puede realizar desplazamientos (pan) y ajustes de escala (zoom) para explorar la red. 
	- [ ] Inspección: Al seleccionar un nodo, se despliega la información detallada asociada a dicha entidad. 
	- [ ] Panel de Control: Ubicado en el margen inferior izquierdo, proporciona estadísticas en tiempo real sobre el volumen de nodos y relaciones procesadas.
4. Módulo SPARQL (Consultas Avanzadas)
	- [ ] El sistema ofrece una biblioteca de consultas predefinidas que cubren los casos de uso más frecuentes
	- [ ] Los datos se devuelven en formato JSON, garantizando la compatibilidad para su posterior exportación o análisis externo. Se incluye una función de copia rápida para facilitar el flujo de trabajo.
 5. Módulo Ingestar (Administración de Datos)
	 - [ ] Carga de Archivos: Soporte para formatos estructurados (SQL, CSV, JSON). 
	 - [ ] Configuración del proceso ETL: Definición de parámetros como la detección automática de formato y el tamaño de lote (batch size) para optimizar el rendimiento. 
	 - [ ] Ejecución: El sistema permite monitorizar el progreso de la carga en tiempo real.
	1. El módulo mantiene un registro de: 
		- [ ] Archivos disponibles en el servidor (nombre, tipo, peso y fecha).
		- [ ] Estado de los procesos (En progreso, Completados o Fallidos).
	2. La plataforma integra mecanismos de autodiagnóstico visibles para el usuario: 
		- [ ] Estado de la API: Indicadores de conexión con el motor Cognitive ETL. 
		- [ ] Sincronización: Alertas sobre la disponibilidad del servicio de chat y actualización del grafo.

## Documento fuente: [[UBXAT - Perspective and Prompts (EN)]]

Core Principles:
1. Unified concepts
Data modeling remains consistent 
Queries can work without gender specification 
Gender information is preserved but not required

2. Gender storage and Gender-aware queries
- [ ]  When asking about women or men in natural language, the system understands gender-specific requests

1. Prompt Engineering for Gender-Aware Queries
	 - [ ] Natural language queries
	 - [ ] SPARQL queries
	 - [ ] Traduction to Cypher queries
	1. Conversacional API Prompts:
		 - [ ] Detects gender-specific terms
		 - [ ] Enhances the query with gender context
		 - [ ] Generates appropriate response using the enhanced context
	2. Ground Truth Mapping for gender
		1. Author relationships P50 (person entity)
	
2. Counting Women Brigadistas
3. Gender Distribution Analysis

## Documento fuente: [[UBXAT - SPARQL Integration Guide (EN).pdf]]

3. SPARQL Queries
		1. Request Format
		2. SELECT Queries 
			1. Basic triple patterns: ?subject ?predicate ?object 
			2. FILTER clauses: Basic string and numeric comparisons 
			3. LIMIT/OFFSET: Result pagination 
		3. ASK Queries 
			1. Boolean queries: Check for pattern existence 
			2. Supported: Basic ASK queries 
		4. COUNT Queries (Extended) 
			1. Custom COUNT syntax: COUNT(?variable) 
			2. Automatic translation: To optimized Cypher aggregation queries
		5. Capacidad: 
			1. El sistema ofrece una biblioteca de consultas predefinidas que cubren los casos de uso más frecuentes: 
				1. Listados de personas con metadatos de nacimiento/fallecimiento.
				2. Geolocalización de fosas con coordenadas específicas. 
				3. Análisis de la densidad de relaciones entre entidades. 
				4. Verificaciones de existencia de datos (Consultas ASK).
			2. Los datos se devuelven en formato JSON, garantizando la compatibilidad para su posterior exportación o análisis externo. Se incluye una función de copia rápida para facilitar el flujo de trabajo.
		6. Automatic Query Enhancement: the system enhances SPARQL queries with ground truth intelligence: 
			1. Variable Resolution: Maps SPARQL variables to ground truth entity types 
			2. Field Mapping: Uses ground truth to determine relevant search fields 
			3. Query Optimization: Generates efficient Cypher based on learned patterns
		7. Query Optimization 
			1. Use LIMIT: Always limit result sets for performance 
			2. Filter early: Apply restrictive filters first 
			3. Ground truth awareness: System automatically optimizes based on learned patterns
		8. Adding New Entity Types
			1. Update ground truth: Add new entity mappings to JSON files 
			2. Test queries: Verify new entity types work with SPARQL 
			3. Update documentation: Add new entity examples
		9. Supporting SPARQL Features 1
			1. Extend translator: Modify #op/acc/question _generate_cypher_from_sparql_with_ground_truth() 
			2. Add test cases: Ensure new features work correctly 
			3. Update documentation: Document new supported features
## Documento fuente: [[UBXAT_-_Estrategia_RDF_Neo4j]]
1. [ ] Almacenamiento nativo en Neo4j: Datos estructurados como nodos y relaciones con propiedades.
2. [ ] Consulta mediante SPARQL: Conversión dinámica de consultas SPARQL a Cypher.
3. [ ] Exportación RDF: Capacidad de exportar datos de Neo4j a formato RDF.
4. [ ] Ingestión desde RDF: Carga de datos RDF que se transforman en estructuras Neo4j.
5. [ ] Conversión dinámica: Las consultas SPARQL se traducen automáticamente a Cypher.
6. [ ] Soporte completo: SELECT, ASK, CONSTRUCT, DESCRIBE, FILTER, ORDER BY, GROUP BY, agregaciones.
7. [ ] Mapeo de propiedades: Convierte propiedades Wikidata (P625, P131, etc.) a propiedades Neo4j.
8. [ ] Namespaces: Soporta namespaces de Wikidata (wdt:, wd:)
9. [ ] 1. Propiedades Wikidata → Neo4j (revisar mapeo)
10. [ ] Normalización de tipos (Tipos de entidades se normalizan según CANONICAL_NODE_TYPES Alias de tipos se mapean (ej: "Brigadista" → "Person").
11. [ ] Relaciones bidireccionales: Se crean automáticamente relaciones inversas según INVERSE_RELATIONSHIPS.

> [!pregunta|] 
> #op/acc/question sobre la manera de probar la ingesta tengo muchas dudas, pensé que lo tenía claro. Una manera de evaluar sería con una nueva base de datos, en alguna reunión habías dicho que podíamos ensayar con la de Maestras y llevadores? recuerdo mal?
> No sé si soy muy entrometida, a mi me gustaría ver el *GroundTruthMapper: Dynamic entity resolution using ground truth data as source of truth* 

## Documento fuente: [[UBXAT API Module (EN)]] y [[UBXAT - Readme (EN)]]

> [!pregunta|]
> Esta parte no sé cómo evaluarla, la parte de monitoreo creo que la podría hacer Matheus?

1. ETL Processing Flow 
	1. Receive processing request with file paths and parameters 
	2. Validate input files and determine data formats 
	3. Execute LangGraph pipeline with Gemini AI components 
	4. Store results in Neo4j knowledge graph 5. Return processing status and metrics

2. Query Processing Flow 
	1. Receive SPARQL or natural language query 
	2. Extract search terms using ground truth mappings 
	3. Gather relevant context from Neo4j 
	4. Generate AI-powered response using Gemini 5. Return structured response with sources

3. Conversational Flow 
	1. Parse natural language question 
	2. Extract entities using dynamic keyword mapping 
	3. Query knowledge graph for relevant context 
	4. Generate conversational response with Gemini 
	5. Include source references and confidence scores

Ground Truth Integration The API uses ground truth data for dynamic behavior: Entity Resolution: Maps Wikidata QIDs to entity types using ground truth Keyword Extraction: Generates search terms from table names and field mappings Query Generation: Creates Cypher queries using schema information from ground truth Label Generation: Produces human-readable labels from ground truth table names

> [!inquetud]
> No sé si soy muy entrometida, a mi me gustaría ver el _GroundTruthMapper: Dynamic entity resolution using ground truth data as source of truth_

> [!Preguntas en general]
> 1. Cómo puede entenderse mejor de donde viene el porcentaje de confianza
> 2. Cómo interpretar el porcentaje de error en las inconsistencias de generación de relaciones por parte de Gemini
> 3. Se hizo en algun sentido una evaluación relacionada con sesgos? 

# Explorando los documentos se extraen estos test hechos en el proceso: 

### 1. **Pruebas unitarias para reglas de negocio** (Tarea 4 - Sprint)

- **Ubicación**: `Informe de Sprint_ 7 de julio - 18 de julio de 2024.md`

- **Qué se probó**: Pruebas unitarias que validan el comportamiento de cada regla de negocio implementada

- **Criterios de aceptación**:

- El código que implementa las reglas está subido al repositorio

- Existen pruebas unitarias que validan el comportamiento de cada regla (casos de prueba para escenarios positivos/negativos)

- Las reglas siguen las especificaciones del documento de Miquel

### 2. **Testing de ingesta de SQL** (Tarea 6 - Sprint)

- **Ubicación**: `Informe de Sprint_ 7 de julio - 18 de julio de 2024.md`

- **Qué se probó**: Conjunto de pruebas para verificar que el proceso de importación/transformación de datos desde bases de datos SQL al nuevo formato del grafo (alineado con Wikidata) funciona correctamente

- **Plan de pruebas incluye**:

- Comparación de datos de origen (SQL) con los datos resultantes en el grafo

- Verificación de que no hay pérdida de datos para un conjunto de registros de muestra

- Verificación de que los datos en el grafo utilizan correctamente los mapeos de nodos y relaciones definidos previamente

- **Enfoque**: Integridad de datos y corrección de mapeos

### 3. **Testing del endpoint SPARQL** (Tarea 7 - Sprint)

- **Ubicación**: `Informe de Sprint_ 7 de julio - 18 de julio de 2024.md`

- **Qué se probó**: Plan de pruebas exhaustivo sobre el endpoint SPARQL para validar su funcionalidad, corrección de los datos devueltos y rendimiento

- **Casos de prueba**:

- Se ejecutan consultas SPARQL complejas que devuelven los resultados esperados según los datos de prueba

- Las consultas sobre datos inexistentes devuelven un resultado vacío (no un error)

- El tiempo de respuesta para consultas de referencia se encuentra dentro de un umbral aceptable (ej. < 2 segundos)

- **Validación adicional**:

- El endpoint tiene una URL accesible desde el entorno de desarrollo/staging

- El endpoint responde con código 200 a una consulta SPARQL válida

- El endpoint responde con código de error (ej. 400) a una consulta SPARQL con sintaxis incorrecta


### 4. **Smoke test post-despliegue** (Tarea 8 - Sprint)

- **Ubicación**: `Informe de Sprint_ 7 de julio - 18 de julio de 2024.md`

- **Qué se probó**: Verificación básica post-despliegue

- **Criterios de aceptación**:

- El pipeline de despliegue se ha ejecutado sin errores

- La nueva versión de la aplicación está activa en el entorno de destino

- Se realiza una comprobación básica (smoke test) post-despliegue para confirmar que el servicio está operativo

### 5. **Tests de carga** (planificado - Fase de Desarrollo)

- **Ubicación**: `UBXAT_-_Fase_de_Desarrollo_-_Action_Plan(v2).md`

- **Qué se probará**: Pruebas de carga exhaustivas para validar el rendimiento de la plataforma

- **Propósito**: Validar el rendimiento bajo diferentes escenarios de demanda

- **Estado**: Planificado para Sprint 2 (Optimización y Rendimiento)

### 6. **Cobertura de código** (planificado - Fase de Desarrollo)

- **Ubicación**: `UBXAT_-_Fase_de_Desarrollo_-_Action_Plan(v2).md`

- **Qué se probará**: Pruebas unitarias y de integración con objetivo mínimo del 80% de cobertura de código

- **Enfoque**: Atención especial a refactors y procesos con alta complejidad algorítmica (Big O)

- **Estado**: Planificado
### 7. **Infraestructura de testing** (mencionado en documentación)

- **Ubicación**: `UBXAT - Readme (EN).md`

- **Estructura de test suite**:

- Directorio `tests/` con suites de pruebas

- Comandos: `python -m pytest tests/`, `python -m pytest tests/integration/test_setup.py`

- Cobertura: `python -m pytest --cov=src tests/`
### 8. **Tests de validación de datos** (en curso)

- **Ubicación**: Múltiples documentos (`UBXAT_-_Estrategia_RDF_Neo4j.md`, `UBXAT API Module (EN).md`)

- **Qué se prueba**:

- Validación de propiedades según ontología (`validate_properties()`)

- Validación de relaciones (`validate_relationships()`)

- Validación de archivos de entrada (detección de formato, validación de archivos)

- Tests de manejo de errores (códigos de estado 400, 404, 500, 503)
### 9. **Validación de coherencia semántica** (Tarea 3 - Sprint)

- **Ubicación**: `Informe de Sprint_ 7 de julio - 18 de julio de 2024.md`

- **Qué se probó**: Validación de que los mapeos de relaciones aseguran coherencia semántica

- **Criterios de aceptación**: El 100% de las relaciones definidas en el alcance están mapeadas; el mapeo ha sido validado para asegurar la coherencia semántica
## Resumen 

**Tests ejecutados**: Pruebas unitarias, tests de ingesta SQL, tests del endpoint SPARQL, y smoke tests post-despliegue.

**Tests planificados**: Tests de carga y objetivos de cobertura de código (80%) para la fase de desarrollo.

**Infraestructura**: Utiliza pytest con reportes de cobertura. 