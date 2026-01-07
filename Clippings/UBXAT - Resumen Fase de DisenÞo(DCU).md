---
title: UBXAT - Resumen Fase de DisenÞo(DCU)
type: article
base: clippings
source: pdf
tags:
  - op/projects/UBXAT
  - op/projects/peninsula
---

Linked PDF file(s) for **UBXAT - Resumen Fase de DisenÞo(DCU)**:

- [[PDF/Peninsula/UBXAT - Resumen Fase de DisenÞo(DCU).pdf]]

## PDF text extraction

Resumen Ejecutivo y Metodología Aplicada
Resumen Ejecutivo del Proyecto UBXAT
Este informe detalla los hallazgos obtenidos durante la Fase 0 del proyecto UBXAT II, la cual se centró
en una profunda investigación y análisis de las necesidades del usuario final. El principal objetivo de
esta fase fue aplicar una metodología de Diseño Centrado en el Usuario (DCU) para garantizar que la
arquitectura técnica del sistema no solo responda a problemas reales de los investigadores, sino que
también mejore significativamente su experiencia y cumpla con estrictos requisitos de inclusión. Los
resultados aquí presentados han sido fundamentales para definir las prioridades funcionales del
pipeline de datos y de la extracción de conocimiento del sistema.
Metodología de Diseño Centrado en el Usuario (DCU)
Se implementó un enfoque metodológico cualitativo mixto a lo largo de varias semanas. Este proceso
involucró a un grupo diverso de participantes, incluyendo perfiles de investigador/a senior, analista de
datos y gestor/a de proyectos de investigación. Para complementar las entrevistas y talleres, se
analizaron informes y publicaciones previas de los participantes con el fin de comprender en
profundidad el tipo de relaciones, entidades y conexiones que buscan identificar en sus conjuntos de
datos.


Perfiles de Usuario y Hallazgos Clave
Perfil de Usuario Principal (Persona)
Los descubrimientos de la fase de investigación se consolidaron en dos perfiles de usuario principales.
A continuación, se detalla el perfil más representativo, que encapsula las necesidades y frustraciones
más comunes identificadas.
• Nombre: Dra. Elena Torres
• Rol: Investigadora Postdoctoral en Ciencias Sociales
• Biografía: La Dra. Torres trabaja en un proyecto complejo que requiere el cruce de datos de
diversas fuentes: subvenciones públicas en formato SQL, publicaciones académicas en CSV y
perfiles de organizaciones obtenidos mediante scraping web. No se considera una experta en
gestión de bases de datos y su mayor frustración es la enorme cantidad de tiempo que debe
invertir en la limpieza y unificación de datos, en lugar de dedicarlo al análisis y la generación de
conocimiento.
• Objetivos Clave:
◦ Descubrir relaciones no evidentes entre las entidades financiadoras y las líneas de
investigación emergentes.
◦ Identificar rápidamente a expertos y especialistas en un dominio de conocimiento específico.
◦ Visualizar y analizar las redes de colaboración que existen entre diferentes instituciones y
organizaciones.
• Frustraciones Principales:
◦ "La misma organización aparece con tres nombres diferentes en tres archivos distintos, lo que
hace imposible unificar la información."
◦ "Paso semanas enteras preparando los datos antes de poder hacer la primera pregunta
relevante para mi investigación."
◦ "No puedo realizar búsquedas conceptuales o semánticas; estoy limitada a buscar por
palabras clave exactas."
Hallazgos Clave e Implicaciones para la Arquitectura
La investigación DCU reveló necesidades críticas que han influido directamente en el diseño de la
arquitectura técnica de UBXAT II. La siguiente tabla resume la conexión entre los problemas del
usuario y las soluciones técnicas propuestas.
Hallazgo Clave del
Usuario Implicación para la Arquitectura de UBXAT II
"Necesitamos unificar
entidades duplicadas
automáticamente."
Justifica la necesidad de una fusión inteligente de entidades en la base de
datos de grafos (Neo4j), basada tanto en identificadores canónicos como en
similitud semántica calculada mediante embeddings vectoriales.
"Quiero buscar por Valida el uso de un Modelo de Lenguaje Grande (LLM) para generar


Hallazgo Clave del
Usuario Implicación para la Arquitectura de UBXAT II
conceptos, no por texto
exacto."
embeddings vectoriales de las entidades, permitiendo búsquedas semánticas
avanzadas que superan las limitaciones de las búsquedas por palabras clave.
"Es crucial entender de
dónde viene cada dato
para validar mis hallazgos."
Requiere una trazabilidad completa del pipeline de datos. Esto respalda la
integración con Langfuse para monitorear cada transformación desde la
fuente original hasta el grafo final.
"La estructura de los datos
es compleja; necesito ver
las conexiones
visualmente."
Impulsa la elección de una base de datos de grafos (Neo4j) como núcleo del
sistema, ya que su modelo es inherentemente visual y relacional, lo que facilita
la creación de futuras interfaces de exploración interactiva.


Fase de Diseño Detallada: Mapeo, Extracción
y Fusión
La fase de diseño fue crucial para asegurar que el sistema UBXAT pudiera interpretar, estandarizar y
conectar información de fuentes dispares de manera coherente. El núcleo de esta fase se centró en
una estrategia de mapeo ontológico robusta y en el uso de Modelos de Lenguaje Grandes (LLMs) para
la extracción y fusión de entidades.
Estrategia de Mapeo y Estandarización Ontológica
El primer paso fue establecer un lenguaje común para datos provenientes de múltiples formatos
(SQL, CSV, web, etc.). La estrategia se basó en la conversión de toda la información a RDF (Resource
Description Framework) como paso intermedio, lo que permite una representación estandarizada en
formato de tripletas (sujeto-predicado-objeto).
• Mapeo del Diccionario de Datos: Para las bases de datos SQL, el módulo SQLDataLoader
interpreta el esquema, mapeando tablas como clases, columnas como propiedades y filas como
instancias. Este proceso traduce la estructura relacional a una estructura de grafo.
• Identificadores Únicos (URIs): Se tratan los IDs de las entidades de origen como "recursos" con
un URI único. Esto facilita la conexión con grafos de conocimiento externos y enriquece el modelo
semánticamente.
• Normalización Multilingüe: Se implementó un proceso para estandarizar el contenido en inglés,
catalán y español, asegurando la coherencia y facilitando búsquedas y procesamientos
multilingües.
Proceso con LLMs para Extracción y Fusión
Una vez los datos están en formato RDF, el sistema utiliza LLMs para realizar tareas avanzadas de
extracción de entidades y, de forma crucial, para fusionar entidades que provienen de diferentes
bases de datos originales.
1. Extracción Asistida por IA: Un LLM analiza los datos para extraer entidades (nodos) y relaciones
(aristas) que no eran explícitas en el esquema original. Este proceso es personalizable mediante
prompts para adaptarlo a dominios específicos.
2. Matching Semántico con Embeddings: Para cada entidad, el modelo de Google GenAI genera
un vector numérico (embedding) que captura su significado semántico. Estos vectores son la
clave para comparar entidades de forma conceptual.
3. Fusión Inteligente en Neo4j: Al añadir una nueva entidad, el sistema primero busca si ya existe
una similar. Esta búsqueda se realiza de dos maneras:
◦ Coincidencia de Identificador: Búsqueda por el mismo ID canónico.
◦ Similitud Vectorial: Se usa el embedding de la nueva entidad para buscar en el índice
vectorial de Neo4j las entidades más cercanas semánticamente. Si la similitud supera un
umbral, la información se fusiona con el nodo existente en lugar de crear un duplicado.
Este mecanismo permite consolidar entidades como "Empresa X" (de un CSV) y "Org. X" (de una base
SQL) en un único nodo dentro del grafo de conocimiento.


Consolidación del Grafo y Trazabilidad
• Consolidación de Grafos: El sistema consolida el grafo generado a partir de una nueva ingesta de
datos con el grafo de conocimiento general preexistente, creando una visión unificada y
constantemente enriquecida.
• Trazabilidad con Langfuse: Cada paso del pipeline, desde la carga de un archivo hasta la fusión
de un nodo, es registrado en Langfuse. Esto permite un análisis detallado del rendimiento, los
costes de las llamadas al LLM y la depuración, asegurando que cada dato tenga un origen
trazable.
• Conservación de la Fuente de la Verdad: Se establecieron pipelines para conservar los datos de
caché y, más importante, los datos de origen intactos. Esto actúa como una salvaguarda para
resolver discrepancias o corregir errores sin perder la información original.


Requisitos de Inclusión, Accesibilidad y
Conclusiones
Requisitos de Inclusión de Género y Accesibilidad
Durante toda la fase de investigación se promovió activamente un ambiente inclusivo, lo que derivó
en la definición de requisitos específicos para el desarrollo del proyecto UBXAT II.
• Lenguaje Inclusivo: Se ha establecido como requisito fundamental que cualquier futura interfaz
de usuario o herramienta de visualización utilice un lenguaje neutro en cuanto al género para
evitar sesgos.
• Representatividad en los Datos: Durante las fases de prueba y validación, se utilizarán conjuntos
de datos de muestra que aseguren una representación equitativa de género y otros colectivos,
con el fin de evitar la perpetuación de sesgos históricos.
• Accesibilidad Web: Se ha definido que cualquier herramienta de visualización o consulta que se
desarrolle sobre la plataforma UBXAT II deberá cumplir, como mínimo, con las pautas de
accesibilidad WCAG 2.1 nivel AA, garantizando que sea usable por personas con diversas
capacidades.
Conclusión de la Fase
La ejecución de la fase de Diseño Centrado en el Usuario ha sido fundamental para asegurar que el
potente motor técnico de UBXAT II no sea únicamente una proeza de ingeniería, sino una
herramienta útil, usable e inclusiva. Los hallazgos y el diseño resultante están directamente
orientados a resolver los problemas reales de los investigadores, con el objetivo de acelerar
significativamente su capacidad de análisis y descubrimiento de conocimiento.
