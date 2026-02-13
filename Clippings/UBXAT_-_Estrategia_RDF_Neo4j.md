---
title: UBXAT - Estrategia RDF Neo4j
type: article
base: clippings
source: pdf
tags:
  - Tech/SemanticWeb
  - op/projects/UBXAT
  - op/projects/peninsula
---

Linked PDF file(s) for **UBXAT - Estrategia RDF Neo4j**:

- [[PDF/Peninsula/UBXAT_-_Estrategia_RDF_Neo4j.pdf]]

## PDF text extraction

UBXAT - Estrategia Neo4j + RDF
Resumen
Este proyecto implementa un sistema híbrido que combina Neo4j (grafo de propiedades) como
almacenamiento principal y RDF/SPARQL como capa de consulta y exportación semántica. La
arquitectura permite:
1. Almacenamiento nativo en Neo4j: Datos estructurados como nodos y relaciones con propiedades.
2. Consulta mediante SPARQL: Conversión dinámica de consultas SPARQL a Cypher.
3. Exportación RDF: Capacidad de exportar datos de Neo4j a formato RDF.
4. Ingestión desde RDF: Carga de datos RDF que se transforman en estructuras Neo4j.
Flujo de Datos: RDF → Neo4j
1. Ingestión de Datos RDF
Proceso:
1. Archivo RDF (.ttl, .rdf, .n3, .jsonld)
2. UnifiedDataLoader.load_data()
3. Convierte RDF a texto estructurado
4. Extracción con Gemini
5. Creación de objeto (nodos + relaciones)
6. Creación de objeto + chunks
7. Neo4j (nodos :Entity con propiedades)
Detalles técnicos:
• Se cuenta con un loader unificado que carga archivos RDF usando rdflib.
• Convierte los triples RDF a texto estructurado para procesamiento por LLM.
• Se usa la extracción para obtener entidades y relaciones según la ontología.
• Se escriben los datos en Neo4j aplicando transformaciones ontológicas y evitando errores cartesianos.


Flujo de Datos: Neo4j → RDF (SPARQL Endpoint)
2. Consulta SPARQL sobre Neo4j
Proceso:
1. Consulta SPARQL (SELECT, ASK, CONSTRUCT, DESCRIBE)
2. Analiza la consulta
3. Convierte a Cypher
4. Ejecuta en Neo4j
5. Formatea como RDF/SPARQL
6. Respuesta JSON/XML/CSV en formato SPARQL
Características:
• Conversión dinámica: Las consultas SPARQL se traducen automáticamente a Cypher.
• Soporte completo: SELECT, ASK, CONSTRUCT, DESCRIBE, FILTER, ORDER BY, GROUP BY,
agregaciones.
• Mapeo de propiedades: Convierte propiedades Wikidata (P625, P131, etc.) a propiedades Neo4j.
• Namespaces: Soporta namespaces de Wikidata (wdt:, wd:).
Ejemplo de conversión:
# SPARQL
SELECT ?entity WHERE {
?entity a ks:Person
} LIMIT 10
# Cypher generado
MATCH (entity:Entity {type: 'Person'})
RETURN entity.id as entity
LIMIT 10
Transformaciones Ontológicas
3. Mapeo de Propiedades y Relaciones
Transformaciones aplicadas:


1. Propiedades Wikidata → Neo4j:
◦ P625(coordinate location) → coordinate_location(objeto Point)
◦ P131(located in) → relaciones LOCATED_IN
◦ P1552(has quality) → array qualities
◦ P527(has part) → array parts
2. Normalización de tipos:
◦ Tipos de entidades se normalizan según CANONICAL_NODE_TYPES.
◦ Alias de tipos se mapean (ej: "Brigadista" → "Person").
3. Relaciones bidireccionales:
◦ Se crean automáticamente relaciones inversas según INVERSE_RELATIONSHIPS.
◦ Ej: AUTHOREDcrea automáticamente AUTHORED_BYen dirección inversa.
Capas de la Arquitectura
Capa 1: Almacenamiento (Neo4j)
Responsabilidades:
• Almacenar nodos :Entitycon propiedades.
• Almacenar relaciones tipadas entre entidades.
• Índices vectoriales para búsqueda semántica (Chunknodes).
• Metadatos de fuentes (sourcesarray en cada entidad).
Estructura típica:
(:Entity {
id: "autor_juan_perez",
type: "Person",
nombre: "Juan Pérez",
nacionalidad: "España",
sources: ["documento1.rdf", "documento2.csv"]
})
-[:AUTHORED]->
(:Entity {
id: "libro_pub_historia_espana",
type: "LibroPublicado",
titulo: "Historia de España"
})


Capa 2: Extracción y Transformación
Responsabilidades:
• Extraer entidades y relaciones de texto/RDF/CSV usando Gemini.
• Aplicar reglas ontológicas.
• Normalizar IDs y tipos.
• Validar propiedades según ontología.
Acciones:
• Extracción con LLM.
• Escritura con transformaciones.
• Validación de relaciones.
Capa 3: Consulta RDF/SPARQL
Responsabilidades:
• Exponer endpoint SPARQL estándar.
• Convertir SPARQL a Cypher.
• Formatear respuestas en formatos RDF (JSON, XML, CSV).
• Mantener compatibilidad con estándares semánticos.
Endpoints:
• GET/POST /sparql/: Ejecutar consultas SPARQL.
• GET /sparql/schema: Obtener esquema de la base de datos.
• GET /sparql/explain: Explicar plan de ejecución.
• GET /sparql/status: Estado del servicio.
Capa 4: RAG (Retrieval Augmented Generation)
Responsabilidades:
• Búsqueda semántica usando embeddings.
• Consulta del grafo para contexto.
• Generación de respuestas con Gemini.


Componentes:
• Cadena RAG completa con Langchain y Langfuse.
• Usa Neo4jVectorpara búsqueda vectorial.
• Integra contexto del grafo en respuestas.
Flujos de Interacción
Flujo 1: Ingestión RDF → Neo4j
1. Usuario carga archivo RDF
2. UnifiedDataLoader.parse_rdf()
◦ Carga triples RDF.
◦ Convierte a texto estructurado.
3. extractGraph()
◦ Gemini analiza texto.
◦ Extrae entidades y relaciones.
◦ Aplica ontología.
4. GraphWriter.write_graph_document()
◦ Transforma propiedades (Wikidata → Neo4j).
◦ Escribe nodos en Neo4j.
◦ Crea relaciones con validación.
5. Neo4j almacena datos.
Flujo 2: Consulta SPARQL → Neo4j → RDF
1. Cliente envía consulta SPARQL
POST /sparql/?format=json
2. AdvancedSPARQLEndpoint._parse_sparql_query()
◦ Analiza sintaxis SPARQL.
◦ Extrae variables, filtros, agregaciones.
3. _sparql_to_cypher_advanced()
◦ Convierte patrones SPARQL a Cypher.
◦ Mapea namespaces (ks:, wdt:).
◦ Traduce propiedades Wikidata.
4. _execute_cypher_query()


◦ Ejecuta Cypher en Neo4j.
◦ Obtiene resultados.
5. _format_sparql_response()
◦ Formatea como SPARQL Results JSON.
◦ Convierte valores a formato RDF.
◦ Aplica namespaces.
6. Respuesta SPARQL estándar.
Flujo 3: RAG con Contexto del Grafo
1. Usuario hace pregunta
2. queryGraph()
◦ Busca chunks relevantes (vectorial).
◦ Obtiene entidades relacionadas (Cypher).
3. Construye contexto
◦ Combina texto de chunks.
◦ Incluye información del grafo.
4. Gemini genera respuesta
◦ Usa contexto del grafo.
◦ Cita fuentes y entidades.
Puntos de Integración Clave
1. Conversión SPARQL → Cypher
Lógica principal:
• Convierte patrones SPARQL a MATCH de Cypher.
• Convierte FILTER a WHERE de Cypher.
• Convierte SELECT a RETURN de Cypher.
Mapeos importantes:
• ?entity a ks:Person→ MATCH (entity:Entity {type: 'Person'})
• ?entity wdt:P625 ?coord→ WHERE entity.coordinate_location IS NOT NULL
• ?entity ks:nombre ?name→ WHERE entity.nombre = ?name


2. Transformación de Propiedades Wikidata
Transformaciones:
• Coordenadas: lat + lon→ coordinate_location(objeto Point con P625).
• Cualidades: categoria→ qualitiesarray con referencias Q de Wikidata.
• Partes: tipologia_inhumados→ partsarray con referencias Q.
• Referencias: Crea objetos de referencia con P248, P854, P813, P1476.
3. Normalización de Entidades
Proceso:
• normalize_type_name(): Normaliza tipos según CANONICAL_NODE_TYPES.
• normalize_id(): Genera IDs consistentes según tipo y propiedades.
• validate_properties(): Valida propiedades según ONTOLOGICAL_PROPERTY_MAP.
Ventajas de esta Arquitectura
1. Flexibilidad:
◦ Almacenamiento eficiente en Neo4j (propiedades nativas).
◦ Consulta estándar mediante SPARQL (interoperabilidad).
2. Escalabilidad:
◦ Neo4j maneja grandes grafos eficientemente.
◦ Índices vectoriales para búsqueda semántica rápida.
3. Interoperabilidad:
◦ Endpoint SPARQL estándar permite integración con herramientas RDF.
◦ Exportación a formatos RDF para intercambio de datos.
4. Inteligencia:
◦ Gemini extrae conocimiento de texto no estructurado.
◦ Transformaciones ontológicas aseguran consistencia.
5. Trazabilidad:
◦ Cada entidad rastrea sus fuentes (sourcesarray).
◦ Referencias completas con metadatos (P248, P854, etc.).
Limitaciones y Consideraciones
1. Conversión SPARQL → Cypher:
◦ No todas las características SPARQL 1.1 están soportadas.


◦ Algunas consultas complejas pueden requerir optimización manual.
2. Sincronización:
◦ Los datos se almacenan solo en Neo4j.
◦ El endpoint SPARQL es de solo lectura (no modifica datos).
3. Performance:
◦ La conversión SPARQL → Cypher añade overhead.
◦ Consultas muy complejas pueden ser más lentas que Cypher nativo.
