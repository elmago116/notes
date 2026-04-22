
**Proyecto:** UBXAT

**Fecha de respuesta:** 17 de marzo de 2026

**Referencia** **interna:** UBXAT-matriz_cumplimiento_prototipo-v1_0_20260302

# 1.      Acreditación documental y funcional de procesos completados

Todos los entregables listados a continuación están versionados en el repositorio Git del proyecto ( branch: develop ) y son auditables por el equipo técnico del cliente bajo petición.

**1.1**     **Backend** **—** **Ingesta** **/** **ETL** **(Sección** **A)**

| **Entregable**                                                          | **Evidencia**                                                                                                                          |     |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --- |
| Módulo ETL documentado (guía + operativa API)                           | docs/COMPLIANCE_RESPONSE.md  [[COMPLIANCE_RESPONSE]]                                                                                   |     |
| Notebook de integración ETL ejecutado (health, status, files, métricas) | notebooks/nb_03_etl_integration.ipynb — 9 células ejecutadas, 3+ entidades de ground-truth verificadas [[nb_03_etl_integration.ipynb]] |     |
| Estrategia de mapeo Wikidata / entidades KG                             | docs/WIKIDATA_MAPPING_STRATEGY.md [[WIKIDATA_MAPPING_STRATEGY]]                                                                        |     |

**1.2**         **Backend** **—** **SPARQL** **/** **Consultas** **avanzadas** **(Sección** **B)**

| **Entregable**                                             | **Evidencia**                                                                                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint /api/v1/sparql<br><br>operativo                   | notebooks/nb_01_sparql_coverage.ipynb — ASK, COUNT, SELECT, FILTER, LIMIT/OFFSET, relaciones validados [[nb_01_sparql_coverage.ipynb]] |
| Corrección query Estadístiques (UI coherente con servidor) | frontend/src/components/SPARQLQuery.jsx — #op/matheus<br><br>UNION COUNT(DISTINCT) per tipo de entidad                                 |

  

|                                                                    |                                                                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Entregable**                                                     | **Evidencia**                                                                                              |
| Biblioteca de consultas predefinidas con previsualización completa | SPARQLQuery.jsx — 5 queries predefinidas + atributo #op/matheus<br><br>title en celdas para IRIs completas |

**1.3**        **Backend** **—** **Módulo** **Agente** **/** **Conversacional** **(Sección** **C)**

|                                                    |                                                                                                                                                          |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entregable**                                     | **Evidencia**                                                                                                                                            |
| Canal conversacional operativo con recuperación KG | notebooks/nb_02_agent_chat.ipynb — T1 (estructura respuesta), T2 (source chips), T3 (varianza confianza), T4 (execution_time) [[nb_02_agent_chat.ipynb]] |
| Source chips (trazabilidad de fuentes) en UI       | frontend/src/components/ChatBox.jsx — chips de fuente visibles en cada respuesta del asistente #op/matheus                                               |
| Indicador de confianza en UI                       | ChatBox.jsx — porcentaje de confianza sobre cada respuesta del asistente #op/matheus                                                                     |
| Historial / reiniciar sesión en UI                 | ChatBox.jsx — botón "Nou fil" que reinicia mensajes al welcome #op/matheus                                                                               |
| Métricas de rendimiento (tiempo)                   | nb_02 T4 + nb_03 — execution_time validado en respuestas API [[nb_02_agent_chat.ipynb]] y [[nb_03_etl_integration.ipynb]]                                |

**1.4**          **Backend** **—** **KG-to-text** **/** **Redacción** **automática** **Wikipedia** **(Sección** **E)**

|                                                              |                                                                                                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Entregable**                                               | **Evidencia**                                                                                                                        |
| Endpoint POST<br><br>/api/v1/kg-to-text                      | api/api.py — modelos KGToTextRequest / #op/matheus<br><br>KGToTextResponse , servicio, ruta                                          |
| 9 tests unitarios pasando (pytest/anyio)                     | tests/unit/test_kg_to_text.py — validación IRI, generación SPARQL, prompt builder (CA/ES/EN), campos respuesta, ruta 400 #op/matheus |
| Sección Articles en UI con generación desde node_id o SPARQL | frontend/src/components/KGToText.jsx #op/matheus                                                                                     |
| Método cliente<br><br>apiService.kgToText()                  | frontend/src/api/apiClient.js #op/matheus                                                                                            |

**1.5**        **Frontend** **—** **Plataforma** **Web,** **accesibilidad,** **idiomas** **(Sección** **F)**

|                                                                                  |                                                                                                                                                                                           |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entregable**                                                                   | **Evidencia**                                                                                                                                                                             |
| Atributos WCAG: aria- current , role="main" , aria-<br><br>label , role="status" | App.jsx + ChatBox.jsx #op/matheus                                                                                                                                                         |
| Sidebar responsive                                                               | App.jsx — sidebar oculto en mobile, contenido a pantalla completa #op/matheus                                                                                                             |
| Sección de monitorización del sistema visible en UI                              | frontend/src/components/ServiceStatus.jsx — sección "Sistema" en navegación #op/matheus                                                                                                   |
| Strings i18n CA/ES/EN para todas las secciones nuevas                            | frontend/src/i18n/locales/{ca,es,en}.json — claves nav.articles , nav.status , content.articlesTitle , content.statusTitle , ui.resetChat , ui.confidence + 9 claves KGToText #op/matheus |

**1.6**        **Frontend** **—** **Grafo:** **visualización** **y** **transparencia** **(Sección** **G)**

|                                                                 |                                                                                                           |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Entregable**                                                  | **Evidencia**                                                                                             |
| Inspección detallada de nodo (panel lateral con propiedades KG) | RDFView.jsx — clic en nodo abre panel con todas las propiedades recuperadas del KG vía SPARQL #op/matheus |
| Transparencia de criterio: tipo de entidad por nodo             | RDFView.jsx — etiqueta Brigadista / Fossa / Document en panel de inspección #op/matheus                   |
| Pan/zoom: ajuste automático al cargar datos                     | RDFView.jsx — zoomToFit al completar la carga del grafo #op/matheus                                       |
| Panel de estadísticas (nodos/relaciones/tipos)                  | RDFView.jsx — preexistente, validado #op/matheus                                                          |

**1.7**        **Documentación** **de** **carga** **(Sección** **A/C** **—** **rendimiento)**

|                                     |                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| **Entregable**                      | **Evidencia**                                                                         |
| Informe de prueba de carga (Locust) | docs/LOAD_TEST_REPORT.md — metodología, escenarios, umbrales p95 [[LOAD_TEST_REPORT]] |


# 2.           Respuesta específica a cada punto de la matriz (v1.0 de 2026-03-02)

[[HerStory/Evaluación - prototip/UBXAT-matriz_cumplimiento_prototipo-v1_0_20260302.docx]]

**A)**   **Ingesta/ETL** **y** **administración** **de** **datos**

## A.1        — Construcción del KG a partir de requisitos de diseño

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado actual:_ 🟡 Parcial — acreditado documentalmente y con notebooks ejecutados sobre entorno de desarrollo. La validación end-to-end sobre datos de producción (corpus completo de brigadas internacionales) está incluida en ==el calendario de corrección (ver §3, hito A-1). #op/acc/fix 

_Evidencia:_ [[nb_03_etl_integration.ipynb]] , [[WIKIDATA_MAPPING_STRATEGY]]

Código:
🗓️ - Presente en cronograma
❓- dudas
❎ - desacuerdo - revisar



## A.2          — Ingesta y procesamiento ETL 🗓️

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ 🟡 Parcial — módulo ETL operativo y documentado; pendiente ejecución demostrada con dataset de producción.

_Evidencia:_ nb_03_etl_integration.ipynb células 4–7

**B)**   **SPARQL** **/** **Consultas** **avanzadas**

## B.1       — Endpoint SPARQL operativo ❓

_Estado_ _en_ _matriz:_ ✅

_Estado_ _actual:_ ✅ Sin cambios requeridos.

> preguntas en proceso sobre la traducción de Sparql a Cypher

## B.2         — SELECT / FILTER / LIMIT / ASK / COUNT ✅

_Estado_ _en_ _matriz:_ ✅

_Estado_ _actual:_ ✅ Sin cambios requeridos.

## B.3         — Coherencia resultados UI vs servidor ❓

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ ✅ **Corregido.** La query "Estadístiques" que producía un producto cartesiano por OPTIONAL múltiple ha sido reemplazada por UNION COUNT(DISTINCT ?entity) por tipo,

coincidiendo con la lógica del backend. #op/matheus

> No puedo hacer consultas por API entonces no puedo comprobar esto, no sé si cambió la dirección o el usuario.

## B.4          — Biblioteca de consultas predefinidas / previsualización ❎

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ ✅ **Corregido.** Se mantienen 5 consultas predefinidas cubriendo los tipos de entidad del proyecto. Las celdas de resultados incluyen atributo title con el valor completo, eliminando la limitación de truncado #op/acc/question .

> No se ha corregido, la consulta de **nodos principales** arroja error (Error: SPARQL query failed: SPARQL translation failed: Could not parse Cypher from Gemini response); la consulta de **personas** devuelve las 4 personas que alcanza pero no metadatos de nacimiento o muerte ni fosa; la consulta de **fosas comunes** devuelve 9 resultados (que son las que arroja de ese tipo) el nodo (número), NodeLabel (fosa),Label (repite fosa), Location(numero sin referencia); la consulta **estadísticas** debería devolver una tabla con cantidad de fosas, brigadistas y documentos y devuelve la suma total (61), igual sucede con la búsqueda **tipos de entidades**. 

**C)**   **Módulo** **Agente** **/** **Conversacional**

## C.1       — Q&A en lenguaje natural con recuperación de información ❓

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ 🟡 Parcial — el canal funciona y devuelve respuestas con fuentes. La fiabilidad de la recuperación (grounding KG→LLM) está sujeta a la calidad y completitud del grafo de conocimiento

cargado. Se incluye plan de mejora en §3, hito C-1.

_Evidencia:_ nb_02_agent_chat.ipynb T1–T4

> observación: la respuesta empieza con un encabezado de JSON. cómo se sabe esto? podemos ver si el grafo está manteniendo "provenance"?. las respuestas se pueden copiar. Podría descargarse la conversación completa? se habló en reunión. 

## C.2         — Disponibilidad LLM y entrenamiento/ajuste 🗓️

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ 🟡 Parcial — integración con Gemini operativa. El ajuste específico al dominio (brigadas internacionales, terminología del proyecto) se abordará mediante prompt engineering avanzado y enriquecimiento del contexto KG (ver §3, hito C-2).

## C.3         — Integración neuro-simbólica (KG + LLM) 🗓️

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ 🟡 Parcial — la arquitectura es neuro-simbólica (Neo4j + SPARQL + Gemini). La efectividad end-to-end mejorará proporcionalmente al enriquecimiento del KG (hitos A-1 y C-1).

## C.4          — Trazabilidad / source chips en UI ❓

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** Source chips visibles en cada respuesta del asistente. 

> Estamos entendiendo source as "provenance" ?. Debería proporcionarse esta información tanto en consultas con SQL como en el agente conversacional (se dice que mejorará luego de C2 y C3). Reaparece la información sobre la base de conocimiento. 

## C.5         — Indicador de confianza en UI ❓

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** Porcentaje de confianza mostrado bajo cada respuesta cuando el backend lo provee.

> Aparecen dos indicadores de confianza distintos, ninguno provee explicación o alguna pista para saber a que confianza se refiere. Uno aparece entre el texto con número decimal (1.0 o 2.0 - sin escala) y el segundo fuera del texto de respuesta con formato de porcentaje y no varía. 
## C.6         — Historial / reiniciar sesión ❓

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** Botón "Nou fil" que reinicia el hilo conversacional.

> Sí está implementado, el historial se reinicia al salir del agente conversacional también. 

## C.7         — Métricas de rendimiento (tiempo) ✅

_Estado_ _en_ _matriz:_ ✅

_Estado_ _actual:_ ✅ Sin cambios requeridos.
  

**D)**  **Inclusión** **y** **diversidad** **—** **perspectiva** **de** **género**

## D.1      — Consultas gender-aware 🗓️

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ 🟡 Parcial — el backend implementa vocabulario gender-aware y query de contexto con propiedad P21. La limitación actual es la ausencia del atributo P21 en el dataset de producción cargado en el KG. La carga de datos con género es el hito D-1 del calendario (ver §3).

> Pregunta: integración de otras entity properties para la interseccionalidad y la subrepresentación?
  

**E)**   **KG-to-text** **(Wikipedia)**

## E.1       — KG-to-text para redacción automática ❎

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado** **completamente.** Endpoint POST /api/v1/kg-to-text

operativo, validado con 9 tests unitarios, interfaz de usuario en sección "Articles", soporte CA/ES/EN.

> La interacción con el nodo genera errores al intentar con "fosas comunes", también con un ID, o con algun wikidata property. 

**F)**   **Plataforma** **Web,** **accesibilidad** **e** **idiomas**

## F.1     — Accesibilidad WCAG 🗓️

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado** (nivel AA básico): aria-current="page" en navegación, role="main" en contenido principal, aria-label en botones de acción, role="status" en indicadores de carga. La auditoría WCAG completa (contraste, teclado, screen reader) se realizará en el hito F-1.

## F.2        — Responsive (móvil/tablet) 🗓️

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** Sidebar oculto en mobile — el contenido ocupa pantalla completa. Prueba completa de dispositivos incluida en hito F-1.

> Hay mejoras, todos los módulos se muestran. Para que el menú aparezca hay que girar el dispositivo de manera horizontal. Aun no se acomoda la pantalla.

## F.3       — Idiomas CAT/ES/EN consistentes 🗓️

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ 🟡 Parcial — todas las secciones nuevas tienen strings en los 3 idiomas. La auditoría completa de strings sin traducción o hardcodeados está incluida en hito F-2.

> En UI, es consistente, en el módulo de chat también. 

## F.4        — Monitorización visible en UI ❓

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** Sección "Sistema" en navegación con panel de estado de servicios backend visible desde la UI.

> la sección sistema muestra las métricas generales de Neo4j aura, esto es monitorización visible?

## F.5       — Barra de navegación ✅

_Estado_ _en_ _matriz:_ ✅

_Estado_ _actual:_ ✅ Sin cambios requeridos.  

**G)**  **Grafo:** **visualización** **y** **transparencia**

## G.1      — Exploración visual (pan/zoom) ✅

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ ✅ **Mejorado.** Ajuste automático al cargar los datos del grafo, además de los controles manuales ya existentes.

> Hay un control visual de zoom, mejora

## G.2        — Inspección detallada de nodo ❎ 🗓️

_Estado_ _en_ _matriz:_ 🟡 Parcial

_Estado_ _actual:_ ✅ **Implementado.** Panel lateral de inspección: al clicar un nodo se muestra nombre, tipo de entidad y todas las propiedades recuperadas del KG.

> El componente nombrado aparece al cliquear el nodo, no contiene más propiedades que las mismas que aparecían antes al acercar el puntero al nodo. No se especifica el hito del cronograma en el que se trabajará este componente. La funcionalidad nombrada como "interactividad del nodo" se refería además a la ampliación de las relaciones del nodo? esto no se nombra. El código de color y los nodos del grafo no son consistentes, las relaciones funcionan mejor aunque también se debe confirmar.

## G.3        — Transparencia de criterio (por qué se muestran los datos) ❓

_Estado_ _en_ _matriz:_ ❌

_Estado_ _actual:_ ✅ **Implementado.** El panel de inspección muestra el tipo de entidad en lenguaje natural (Brigadista / Fossa / Document) junto a todas las propiedades KG del nodo, haciendo explícito el origen y criterio de clasificación.

> No me queda claro a qué se refieren con "origen y criterio de clasificación". Si es el panel anterior se evidencian las fosas pero no los brigadistas ni los documentos. Tampoco aparecen todas las propiedades del nodo ni se relaciona esto con las tareas de completar el grafo de conocimiento. 

## G.4         — Panel de control (estadísticas)

_Estado_ _en_ _matriz:_ ✅

_Estado_ _actual:_ ✅ Sin cambios requeridos.  

# Preguntas:
1. Raonament basat en regles, avaluació del raonament
2. Privacitat: anonimització, consentiment, dades públiques, seguretat (hacerlas evidentes en la docuementación que se entrega del proyecto)
3. Cómo funciona lo que se nombra cómo geolocalización de fosas y fuentes documentales? (aparece el nombre de la comarca pero hay georeferenciación en el grafo?)
4. Análisis de la densidad de relaciones entre entidades.
5. Automatic Query Enhancement: the system enhances SPARQL queries with ground truth intelligence: Variable Resolution: Maps SPARQL variables to ground truth entity types
6. Ground truth awareness: System automatically optimizes based on learned patterns . Adding New Entity Types. Update ground truth: Add new entity mappings to JSON files. Verify new entity types work with SPARQL (está entre las propuestas de capacidades del módulo SPARQL)


# 3.          Calendario de corrección de incumplimientos materiales pendientes

![](file:////Users/elenagomez/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)Plazo contractual máximo: **28** **de** **septiembre** **de** **2026** Fecha de este documento: 17 de marzo de 2026 Ventana de trabajo disponible: ![](data:image/png;base64,/9j/4AAQSkZJRgABAQAAkACQAAD/4QCARXhpZgAATU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAKgAgAEAAAAAQAAAAigAwAEAAAAAQAAAA4AAAAA/+0AOFBob3Rvc2hvcCAzLjAAOEJJTQQEAAAAAAAAOEJJTQQlAAAAAAAQ1B2M2Y8AsgTpgAmY7PhCfv/AABEIAA4ACAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2wBDAAICAgICAgMCAgMFAwMDBQYFBQUFBggGBgYGBggKCAgICAgICgoKCgoKCgoMDAwMDAwODg4ODg8PDw8PDw8PDw//2wBDAQICAgQEBAcEBAcQCwkLEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBD/3QAEAAH/2gAMAwEAAhEDEQA/AP38or5M8PfAH4kaTruk6lqHxEub20huba8voGN4RPJbyLKU+e6ZWVyuCWXp/CelfWdAH//Z)  **28 semanas**

**Hitos** **y** **entregables**

|   |   |   |   |   |
|---|---|---|---|---|
|**ID**|**Sección**|**Incumplimiento**|**Entregable**|**Fecha límite**|
|**A-****1**|A|KG no validado con datos de producción|Carga del corpus completo en entorno de staging; notebook nb_03 ejecutado sobre datos reales con ≥ 3 entidades de cada tipo (Q5/Q108163/Q49848); informe de cobertura|**30** **abril**<br><br>**2026**|
|**D-1**|D|Propiedad P21 (género) ausente en KG|Carga de atributo P21 para todos los registros de Persona (Q5) disponibles; validación con query nb_01 Block 7 ejecutando sin error|**30** **abril**<br><br>**2026**|
|**F-1**|F|Accesibilidad WCAG y<br><br>responsive no auditados completamente|Auditoría WCAG AA con herramienta automatizada (axe / Lighthouse); corrección de los hallazgos críticos; informe de resultados; prueba en dispositivo móvil real|**30** **mayo**<br><br>**2026**|
|**F-****2**|F|Strings sin traducir o hardcodeados|Auditoría completa de los 3 ficheros i18n; corrección de claves ausentes o inconsistentes; test de idioma sobre todas las vistas|**30** **mayo**<br><br>**2026**|

|   |   |   |   |   |
|---|---|---|---|---|
|**ID**|**Sección**|**Incumplimiento**|**Entregable**|**Fecha límite**|
|**C-1**|C|Q&A no recupera información de forma fiable|Mejora del contexto KG→LLM: enriquecimiento de embeddings/contexto SPARQL, ajuste de prompts al dominio; validación con nb_02 T1– T6 completos|**30** **junio**<br><br>**2026**|
|**C-****2**|C|LLM sin ajuste específico al dominio|Entrega de documento de estrategia de ajuste (prompt engineering + retrieval); ejecución de serie de pruebas de Q&A sobre preguntas de referencia del proyecto; informe de evaluación|**31** **julio**<br><br>**2026**|
|**A-****2**|A|ETL no probado end-to-end en producción|Demostración documentada de ingesta completa (fichero fuente → Neo4j → SPARQL validado); log de ejecución adjunto|**31** **agosto**<br><br>**2026**|
|**VAL**|Todos|Validación final integrada|Ejecución completa de los 4 notebooks ( nb_01 – nb_04 ) sobre el entorno de<br><br>producción con datos reales; resultado ≥ 90% de checks pasando; entrega de informe de cierre|**19**<br><br>**septiembre** **2026**|

# 4.            Confirmación formal de recursos asignados

Los siguientes recursos están efectivamente asignados a la resolución de los incumplimientos materiales identificados en este documento:

|   |   |   |
|---|---|---|
|**Recurso**|**Perfil**|**Dedicación** **estimada**|
|[Thomas Gomez — Responsable datos]|Software Engineer / Historiador|24 h/semana|


# 5.          Documentación adjunta

Los siguientes ficheros se entregan junto a este documento como evidencia auditable:

docs/

├── RESPUESTA_REQUERIMIENTO_CUMPLIMIENTO_20260317.md    ← este documento

├── COMPLIANCE_RESPONSE.md                              ← respuesta técnica detallada (Stream C)

├── WIKIDATA_MAPPING_STRATEGY.md                        ← estrategia de mapeo entidades

└── LOAD_TEST_REPORT.md                                 ← informe de carga

(Locust)

  

notebooks/

├── nb_01_sparql_coverage.ipynb     ← cobertura SPARQL (B)

├── nb_02_agent_chat.ipynb          ← agente conversacional (C)

├── nb_03_etl_integration.ipynb     ← integración ETL (A)

└── nb_04_kg_validation.ipynb       ← validación estructura KG (A/G)

tests/unit/

└── test_kg_to_text.py              ← 9 tests unitarios KG-to-text (E)

|   |
|---|
||
|||

  

_Documento_ _generado_ _el_ _2026-03-17._