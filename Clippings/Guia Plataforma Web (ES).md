---
title: Guía Plataforma Web (ES)
source: Guia Plataforma Web (ES).pdf
type: PDF extraction
tags:
  - op/projects/peninsula
---

[[PDF/Peninsula/Guia Plataforma Web (ES).pdf]]

## Guía de Usuario - UBXAT

### Introducción

UBXAT es una plataforma avanzada de gestión del conocimiento diseñada para la exploración y análisis de datos históricos relativos a la Guerra Civil Española. El sistema integra tecnologías de procesamiento de lenguaje natural y grafos de conocimiento para facilitar el estudio de brigadistas internacionales y fosas comunes. Esta guía detalla las funcionalidades operativas de la interfaz web.

### Funcionalidades Principales

La plataforma UBXAT permite ejecutar las siguientes operaciones:

- **Interacción mediante lenguaje natural**: Consultas directas sobre registros de brigadistas, geolocalización de fosas y fuentes documentales.
- **Análisis visual de datos**: Exploración de un grafo interactivo que representa las entidades y sus relaciones.
- **Consultas técnicas (SPARQL)**: Ejecución de consultas complejas sobre la base de datos de conocimiento.
- **Ingesta y procesamiento de datos**: Herramientas para la carga y transformación de nuevos activos de información.
- **Monitorización del sistema**: Supervisión del estado operativo de los servicios en tiempo real.

### Navegación y Estructura de la Interfaz

La interfaz se divide en dos componentes principales de navegación:

1. **Panel Lateral**: Acceso directo a los cuatro módulos operativos del sistema.
2. **Cabecera**: Indicador de la sección activa y controles de actualización de datos.

---

### 1. Módulo Agente (Asistente Inteligente)

Este módulo constituye la interfaz principal de consulta, permitiendo al usuario obtener información precisa sin necesidad de conocimientos técnicos en bases de datos.

**Procedimiento de consulta**

1. Seleccionar la opción Agente en el panel lateral.
2. Introducir la consulta en el campo de texto inferior.
3. Ejecutar mediante la tecla Enter o el botón Enviar.

**Capacidades del asistente**

- **Evaluación de confianza**: Un indicador visual (verde, amarillo o rojo) determina el grado de fiabilidad de la respuesta generada.
- **Trazabilidad de información**: El sistema muestra los "chips" de fuentes consultadas, permitiendo verificar el origen de los datos.
- **Métricas de rendimiento**: Visualización del tiempo de procesamiento de cada respuesta.
- **Gestión de historial**: Herramientas para copiar respuestas al portapapeles o reiniciar la sesión de chat para nuevas consultas.

---

### 2. Módulo Grafo de Conocimiento (Visualización Interactiva)

Representación gráfica de la red de entidades históricas y sus interconexiones.

**Clasificación de entidades por nodos**

- **Nodos Rojos**: Personal (Brigadistas).
- **Nodos Azules**: Localizaciones geográficas y eventos históricos.
- **Nodos Verdes**: Documentación y archivos de referencia.
- **Nodos Naranjas**: Registros de fosas comunes.

**Interacción y análisis**

- **Navegación**: El usuario puede realizar desplazamientos (pan) y ajustes de escala (zoom) para explorar la red.
- **Inspección**: Al seleccionar un nodo, se despliega la información detallada asociada a dicha entidad.
- **Panel de Control**: Ubicado en el margen inferior izquierdo, proporciona estadísticas en tiempo real sobre el volumen de nodos y relaciones procesadas.

---

### 3. Módulo SPARQL (Consultas Avanzadas)

Sección orientada a usuarios técnicos para la extracción de datos estructurados mediante el lenguaje de consulta SPARQL.

**Ejecución de consultas**

El sistema ofrece una biblioteca de consultas predefinidas que cubren los casos de uso más frecuentes:

- Listados de personas con metadatos de nacimiento/fallecimiento.
- Geolocalización de fosas con coordenadas específicas.
- Análisis de la densidad de relaciones entre entidades.
- Verificaciones de existencia de datos (Consultas ASK).

**Gestión de resultados**

Los datos se devuelven en formato JSON, garantizando la compatibilidad para su posterior exportación o análisis externo. Se incluye una función de copia rápida para facilitar el flujo de trabajo.

---

### 4. Módulo Ingestar (Administración de Datos)

Herramienta dedicada a la expansión de la base de conocimiento mediante la carga de nuevos datasets.

**Flujo de trabajo de ingesta**

1. **Carga de Archivos**: Soporte para formatos estructurados (SQL, CSV, JSON).
2. **Configuración del proceso ETL**: Definición de parámetros como la detección automática de formato y el tamaño de lote (batch size) para optimizar el rendimiento.
3. **Ejecución**: El sistema permite monitorizar el progreso de la carga en tiempo real.

**Registro de actividad**

El módulo mantiene un registro de:

- Archivos disponibles en el servidor (nombre, tipo, peso y fecha).
- Estado de los procesos (En progreso, Completados o Fallidos).

---

### Mantenimiento y Estado del Sistema

La plataforma integra mecanismos de autodiagnóstico visibles para el usuario:

- **Estado de la API**: Indicadores de conexión con el motor Cognitive ETL.
- **Sincronización**: Alertas sobre la disponibilidad del servicio de chat y actualización del grafo.

---

### Recomendaciones de uso profesional

- Para obtener resultados óptimos en el módulo Agente, se recomienda el uso de consultas precisas y contextualizadas.
- En caso de latencia elevada durante la carga del grafo, utilice los controles de zoom para segmentar la vista de interés.
- Ante cualquier incidencia técnica persistente, se sugiere refrescar la sesión o verificar los indicadores de estado en la sección de administración.

*Nota: Posibles refinamientos sean aplicados a la interfaz.*
