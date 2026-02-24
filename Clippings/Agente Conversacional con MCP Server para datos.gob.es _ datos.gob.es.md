---
title: "Agente Conversacional con MCP Server para datos.gob.es | datos.gob.es"
source: "https://datos.gob.es/es/conocimiento/agente-conversacional-con-mcp-server-para-datosgobes"
authors: "[[Agente Conversacional con MCP Server para datos.gob.es | datos.gob.es]]"
published:
created: 2026-02-16
description: "Plataforma de datos abiertos del Gobierno de España"
tags:
  - "op/doc/tool"
  - "tech/MCP"
DOI:
Type:
year:
---
[![Inicio](https://datos.gob.es/themes/custom/dge_theme/logo.svg)](https://datos.gob.es/es/ "Inicio")

## Agente Conversacional con MCP Server para datos.gob.es

Fecha publicación 12/01/2026

Fecha actualización 26/01/2026

Tipo [Ejercicios de datos](https://datos.gob.es/es/conocimiento/tipo/ejercicios-de-datos-342)

Descripción

Los agentes de IA (como los de Google ADK, LangChain, etc.) son "cerebros". Pero un cerebro sin "manos" no puede actuar en el mundo real (consultar APIs, buscar en bases de datos, etc.). Esas "manos" son las **herramientas**.

El desafío es: ¿cómo conectas el cerebro con las manos de forma estándar, desacoplada y escalable? La respuesta es el **Model Context Protocol (MCP)**.

Como ejercicio práctico, construiremos un sistema de agente conversacional que permite explorar el Catálogo Nacional de datos abiertos albergado en datos.gob.es mediante preguntas en lenguaje natural, facilitando así el acceso a datos públicos.

En este ejercicio práctico, el objetivo principal es ilustrar, paso a paso, cómo **construir un servidor de herramientas independiente que hable el protocolo MCP**.

Para hacer este ejercicio tangible y no solo teórico, usaremos, FastMCP para construir el servidor. Para probar que nuestro servidor funciona, crearemos un agente simple con Google ADK que lo consuma. El caso de uso (consultar la API de [datos.gob.es](https://datos.gob.es/)) ilustra esta conexión entre herramientas y agentes. **El verdadero aprendizaje es la arquitectura, que podrías reutilizar para cualquier API o base de datos**.

A continuación se muestran las tecnologías que usaremos y un esquema de cómo están realizados entre sí los diferentes componentes

- FastMCP (mcp.server.fastmcp): implementación ligera del protocolo MCP que permite crear servidores de herramientas con muy poco código mediante decoradores Python. Es el 'protagonista' del ejercicio.
- Google ADK (Agent Development Kit): *framework* para definir el agente de IA, su *prompt* y conectarlo a las herramientas. Es el 'cliente' que prueba nuestro servidor.
- FastAPI: para servir el agente como una API REST con interfaz web interactiva.
- httpx: para realizar llamadas asíncronas a la API externa de datos.gob.es.
- Docker y Docker Compose: para paquetizar y orquestar los dos microservicios, permitiendo que se ejecuten y comuniquen de forma aislada.

![Diagrama que indica el flujo de preguntas, respuestas y llamadas entre cliente, servidor MCP y la fuente de los datos](https://datos.gob.es/sites/default/files/inline-images/agente-conversacional-con-mcp-server-para-datosgobes_figura-1.png)  

Figura 1. Arquitectura desacoplada con comunicación MCP.

El diagrama ilustra una arquitectura desacoplada dividida en cuatro componentes principales que se comunican mediante el protocolo MCP. Cuando el usuario realiza una consulta en lenguaje natural, el Agente ADK (basado en Google Gemini) procesa la intención y se comunica con el servidor MCP a través del Protocolo MCP, que actúa como intermediario estandarizado. El servidor MCP expone cuatro herramientas especializadas (buscar *datasets*, listar temáticas, buscar por temática y obtener detalles) que encapsulan toda la lógica de negocio para interactuar con la API externa de datos.gob.es. Una vez que las herramientas ejecutan las consultas necesarias y reciben los datos del catálogo nacional, el resultado se propaga de vuelta al agente, que finalmente genera una respuesta comprensible para el usuario, completando así el ciclo de comunicación entre el "cerebro" (agente) y las "manos" (herramientas).

[Accede al repositorio del laboratorio de datos en GitHub](https://github.com/Admindatosgobes/Laboratorio-de-Datos/tree/main/Data%20Science/Agente%20Conversacional%20con%20MCP%20server)

[Ejecuta el código de pre-procesamiento de datos sobre Google Colab](https://colab.research.google.com/github/Admindatosgobes/Laboratorio-de-Datos/blob/main/Data%20Science/Agente%20Conversacional%20con%20MCP%20server/notebook.ipynb)

## La arquitectura: servidor MCP y agente consumidor

La clave de este ejercicio es entender la relación cliente-servidor:

1. El Servidor (*Backend*): es el protagonista de este ejercicio. Su único trabajo es definir la lógica de negocio (las "herramientas") y exponerlas al mundo exterior usando el "contrato" estándar de MCP. Es el responsable de encapsular toda la lógica de comunicación con la API de datos.gob.es.
2. El Agente (*Frontend*): es el "cliente" o "consumidor" de nuestro servidor. Su rol en este ejercicio es probar que nuestro servidor MCP funciona. Lo usamos para conectarnos, descubrir las herramientas que el servidor ofrece y llamarlas.
3. El Protocolo MCP: es el "lenguaje" o "contrato" que permite que el agente y el servidor se entiendan sin necesidad de conocer los detalles internos del otro.

## Proceso de desarrollo

El núcleo del ejercicio se divide en tres partes: crear el servidor, crear un cliente para probarlo y ejecutarlos.

### 1\. El servidor de herramientas (el backend con MCP)

Aquí es donde reside la lógica de negocio y el foco de este tutorial. En el archivo principal (server.py), definimos funciones Python simples y usamos el decorador @mcp.tool de FastMCP para exponerlas como 'herramientas' consumibles.

La *description* que añadimos al decorador es crucial, ya que es la documentación que cualquier cliente MCP (incluyendo nuestro agente ADK) leerá para saber cuándo y cómo usar cada herramienta.

Las herramientas que definiremos en el ejercicio son:

- buscar\_datasets(titulo: str): para buscar *datasets* por palabras clave en el título.
- listar\_tematicas(): para descubrir qué categorías de datos existen.
- buscar\_por\_tematica(tematica\_id: str): para encontrar *datasets* de un tema específico.
- obtener\_detalle\_dataset(dataset\_id: str): para obtener la información completa de un *dataset*.

### 2\. El agente consumidor (el frontend con Google ADK)

Una vez construido nuestro servidor MCP, necesitamos una forma de probarlo. Aquí es donde entra Google ADK. Lo usamos para crear un "agente consumidor" simple.

La magia de la conexión ocurre en el argumento *tools*. En lugar de definir las herramientas localmente, simplemente le pasamos la URL de nuestro servidor MCP. El agente, al iniciarse, consultará esa URL, leerá el "contrato" MCP y sabrá automáticamente qué herramientas tiene disponibles y cómo usarlas.

```python
# Ejemplo de configuración en agent.py
root_agent = LlmAgent(
   ...
   instruction="Eres un asistente especializado en datos.gob.es...",
   tools=[
       MCPToolset(
           connection_params=StreamableHTTPConnectionParams(
               url="http://mcp-server:8000/mcp",
           ),
       )
   ]
)
```

### 3\. Orquestación con Docker Compose

Finalmente, para ejecutar nuestro Servidor MCP y el agente consumidor juntos, usamos docker-compose.yml. Docker Compose se encarga de construir las imágenes de cada servicio, crear una red privada para que se comuniquen (por eso el agente puede llamar a [http://mcp-server:8000](http://mcp-server:8000/)) y exponer los puertos necesarios.

## Probando el servidor MCP en acción

Una vez que ejecutamos docker-compose up --build, podemos acceder a la interfaz web del agente ([http://localhost:8080](http://localhost:8080/)).

El objetivo de esta prueba no es solo ver si el bot responde bien, sino verificar que nuestro servidor MCP funciona correctamente y que el agente ADK (nuestro cliente de prueba) puede descubrir y usar las herramientas que este expone.

![En esta captura se pregunta al agente por las herramientas y temáticas disponibles. También da un ejemplo preguntando por los datasets de medio ambiente](https://datos.gob.es/sites/default/files/inline-images/agente-conversacional-con-mcp-server-para-datosgobes_figura-2.png)  

Figura 2. Pantalla del agente demostrando sus herramientas.

El verdadero poder del desacoplamiento se ve cuando el agente encadena lógicamente las herramientas que nuestro servidor le proveyó.

![En esta otra captura, pregunta al agente por datos sobre calidad del aire, y sobre datasets de transporte con detalles del primer resultado, demostrando su efectividad](https://datos.gob.es/sites/default/files/inline-images/agente-conversacional-con-mcp-server-para-datosgobes_figura-3.png)  

Figura 3. Pantalla del agente demostrando el uso conjunto de las herramientas.

## ¿Qué puedes aprender?

El objetivo de este ejercicio es aprender los fundamentos de una arquitectura de agentes moderna, centrándonos en el servidor de herramientas. En concreto:

- Cómo construir un servidor MCP: cómo crear un servidor de herramientas desde cero que hable MCP, usando decoradores como @mcp.tool.
- El patrón de una arquitectura desacoplada: el patrón fundamental de separar el 'cerebro' (LLM) de las 'herramientas' (lógica de negocio).
- Descubrimiento dinámico de herramientas: cómo un agente (en este caso, de ADK) puede conectarse dinámicamente a un servidor MCP para descubrir y consumir herramientas.
- Integración de API externas: el proceso de 'envolver' una API compleja (como la de datos.gob.es) en funciones simples dentro de un servidor de herramientas.
- Orquestación con Docker: cómo gestionar un proyecto de microservicios para desarrollo.

## Conclusiones y futuro

Hemos construido un servidor de herramientas MCP robusto y funcional. El verdadero valor de este ejercicio es el cómo: una arquitectura escalable centrada en un servidor de herramientas que habla un protocolo estándar.

Esta arquitectura basada en MCP es increíblemente flexible. El caso de datos.gob.es es solo un ejemplo. Podríamos fácilmente:

- Cambiar el caso de uso: reemplazar el server.py por uno que conecte a una base de datos interna o a la API de Spotify, y cualquier agente que hable MCP (no solo ADK) podría consumirlo.
- Cambiar el "cerebro": cambiar el agente ADK por un agente de LangChain o cualquier otro cliente MCP, y nuestro servidor de herramientas seguiría funcionando sin cambios.

Para aquellos interesados en llevar este análisis al siguiente nivel, las posibilidades se centran en mejorar el servidor MCP:

- Implementar más herramientas: añadir filtros por formato, publicador o fecha al servidor MCP.
- Integrar caché: usar Redis en el servidor MCP para cachear las respuestas de la API y mejorar la velocidad.
- Añadir persistencia: guardar el historial de chat en una base de datos (esto sí sería en el lado del agente).

Más allá de estas mejoras técnicas, esta arquitectura abre la puerta a múltiples aplicaciones en contextos muy diversos.

- Periodistas y académicos pueden disponer de asistentes de investigación que les ayuden a descubrir conjuntos de datos relevantes en segundos.
- Organizaciones de transparencia pueden construir herramientas de monitorización que detecten automáticamente nuevas publicaciones de datos de contratación pública o presupuestos.
- Consultoras y equipos de inteligencia de negocio pueden desarrollar sistemas que crucen información de múltiples fuentes gubernamentales para elaborar informes sectoriales.
- Incluso en el ámbito educativo, esta arquitectura sirve como base didáctica para enseñar conceptos avanzados de programación asíncrona, integración de API y diseño de agentes de IA.

El patrón que hemos construido —un servidor de herramientas desacoplado que habla un protocolo estándar— es la base sobre la que puedes desarrollar soluciones adaptadas a tus necesidades específicas, independientemente del dominio o la fuente de datos con la que trabajes.  

[casos de uso](https://datos.gob.es/es/etiquetas/casos-de-uso-0)

[Ciencia y tecnología](https://datos.gob.es/es/etiquetas/ciencia-y-tecnologia-0)

### Contenido relacionado

- [Añadir nuevo comentario](https://datos.gob.es/es/conocimiento/# "Comparte tus ideas y opiniones.")