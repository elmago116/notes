---
title: Sistema General - Cultura y Censura Knowledge Graph
source: sistema_general.pdf
type: PDF extraction
tags:
  - op/projects/peninsula
  - tech/UBXAT
---

[[PDF/Peninsula/sistema_general.pdf]]

## Cultura y Censura - Knowledge Graph - Sistema General

Visitar Knowledge Graph - Cultura y Censura

---

### Flujo de Procesamiento

#### 1. Ingesta de Datos

Cuando subes un archivo (RDF, CSV, o SQL), el sistema: detecta el formato automáticamente por extensión y contenido; valida que el archivo es procesable; verifica si ya fue procesado (evita duplicados); crea una copia en el directorio de datos permanente.

#### 2. Análisis Estructural Previo

**Para archivos RDF:** Analiza y prepara el grafo completo con rdflib; identifica tipos de entidades (rdf:type); enumera predicados y frecuencias; detecta espacios y datos usados; analiza patrones de conexión.

**Para archivos CSV:** Analiza headers para columnas geográficas; identifica jerarquías administrativas; detecta coordenadas (latitud/longitud); reconoce tipos de datos en cada columna.

#### 3. Extracción de Entidades y Relaciones

Google Generative AI (Gemini) con prompt especializado. El modelo detecta automáticamente el tipo de archivo por patrones en el texto.

- Recibe contenido estructurado; aplica reglas según tipo (RDF/N-Triples, CSV, SQL/foreign_keys); genera JSON con entidades y relaciones; normaliza IDs (incl. latitud/longitud).

**Tipos soportados:** RDF/Turtle (metadatos Dublin Core, brigadistas); CSV (fosas comunes, sitios históricos); SQL (INSERT normalizados).

**Relaciones:** Documentales, geográficas, sociales e históricas, temáticas.

#### 4. Almacenamiento en Neo4j

Entidades → nodos Entity con propiedades; relaciones → aristas tipificadas; embeddings por chunk (Google AI); índices vectoriales para búsqueda semántica.

#### 5. Indexación y Vínculos Cruzados

Vincula entidades entre fuentes; co-ocurrencia; conexiones geográficas; trazabilidad a documentos fuente.

---

### Tipos de Relaciones Principales

**Documentales:** DOCUMENTS, AUTHORED, MENTIONS, CONTAINS_INFORMATION_ABOUT.

**Personales/Sociales:** BELONGS_TO, SERVED_IN, CONTEMPORARY_OF, COLLEAGUE_OF.

**Geográficas:** LOCATED_IN, BORN_IN/DIED_IN, ACTIVE_IN, COORDINATES_AT.

**Temáticas:** PARTICIPATED_IN, ASSOCIATED_WITH, RELATED_TO.

---

### Tipos de Entidades

Person (full_name, nationality, military_unit, birth_date); Document (title, content_type, author, creation_date); Organization; Location; Site; Concept; Event.

---

### Motor de Consultas

**Búsqueda semántica:** Pregunta → embedding → búsqueda en índice vectorial → entidades relevantes → expansión por relaciones → respuesta con contexto expandido.

**Navegación de grafo:** Selección de entidad; consulta Neo4j; filtro por tipo de relación; expansión gradual; agrupación de nodos.

---

### Gestión, Rendimiento, Escalabilidad

Chunks (límite 100 por proceso); índices Neo4j; consultas parametrizadas; paginación; procesamiento asíncrono; detección de duplicados; normalización de IDs.

---

### Visualización y Robustez

Grafo: layout por entidades relacionadas; colores por tipo; filtros dinámicos. Análisis: comunidades temáticas; centralidad; densidad por área; evolución temporal. Validación de datos; control de relaciones; recuperación ante errores (rollback, reintentos).

---

### Próximos Pasos

Cache dinámico; ampliación ventana de contexto (escalar chunks); estrategias para tipos complejos (coordenadas, lugares frecuentes).
