---
title: "Técnicas RAG: cómo funcionan y ejemplos de casos de uso | datos.gob.es"
source: https://datos.gob.es/es/blog/tecnicas-rag-como-funcionan-y-ejemplos-de-casos-de-uso
author:
  - "[[Técnicas RAG: cómo funcionan y ejemplos de casos de uso | datos.gob.es]]"
published:
created: 2025-11-29
description: Plataforma de datos abiertos del Gobierno de España
tags:
  - op/doc/tool
DOI: Tech/RAG, op/repport
---
[![Inicio](https://datos.gob.es/themes/custom/dge_theme/logo.svg)](https://datos.gob.es/es/ "Inicio")

## Técnicas RAG: cómo funcionan y ejemplos de casos de uso

Fecha publicación 21/08/2024

![mobile phone with ai](https://datos.gob.es/sites/default/files/styles/wide/public/blog/image/69_0.jpg?itok=E7kYiiAL)

Descripción

En los últimos meses hemos visto cómo los grandes modelos del lenguaje (*LLM* en sus siglas en inglés) que habilitan las aplicaciones de Inteligencia artificial generativa (*GenA I*) han ido mejorando en cuanto a su precisión y confiabilidad. Las técnicas de *RAG (Retrieval Augmented Generation)* nos han permitido utilizar toda la potencia de la comunicación en lenguaje natural (*NLP*) con las máquinas para explorar bases de conocimiento propias y extraer información procesada en forma de respuestas a nuestras preguntas. En este  artículo  profundizamos en las técnicas *RAG* con el objetivo de conocer mejor su funcionamiento y todas las posibilidades que nos ofrecen en el contexto de la IA generativa.

## ¿Qué son las técnicas RAG?

No es la primera vez que hablamos de las técnicas *RAG*. [En este artículo](https://datos.gob.es/es/blog/rag-retrieval-augmented-generation-la-llave-que-abre-la-puerta-de-la-precision-los-modelos-del) ya introdujimos el tema, explicando de forma sencilla en qué consisten, cuáles son sus principales ventajas y qué beneficios aporta en el uso de la IA Generativa.

Recordemos por un momento sus principales claves. *RAG*, del inglés, ***Retrieval Augmented Generation***, viene a traducirse cómo **Generación Aumentada por Recuperación** (de información). Es decir, *RAG*  consiste en lo siguiente: cuando un usuario realiza una pregunta -normalmente en un interfaz conversacional-, la Inteligencia Artificial (IA), antes de proporcionar la respuesta directa -que podría dar haciendo uso de la base de conocimiento (fijo) con la que ha sido entrenada-, realiza un **proceso de búsqueda y procesamiento de información en una base de datos** específica proporcionada previamente, complementaria a la del entrenamiento. Cuando hablamos de una base de datos nos referimos a una base de conocimiento previamente preparada a partir de un conjunto de documentos que el sistema utilizará para proporcionar respuestas más precisas. De esta forma, cuando hacen uso de las técnicas *RAG*, las interfaces conversacionales producen **respuestas más precisas y adaptadas a un contexto concreto**.

*Fuente: Elaboración propia*

*Diagrama conceptual del funcionamiento de un asistente o interfaz conversacional sin hacer uso de RAG (arriba) y haciendo uso de RAG (abajo).*

Haciendo un símil con el ámbito médico, podríamos decir que el uso de *RAG* es como si un médico, con amplia experiencia y, por lo tanto, altamente entrenado, además de los conocimientos adquiridos durante su formación académica y años de experiencia, tuviera acceso rápido y sin esfuerzo a los últimos estudios, análisis y bases de datos médicas al instante, antes de proporcionar un diagnóstico. La formación académica y los años de experiencia equivalen [al entrenamiento](https://datos.gob.es/es/blog/gpt-3-simplemente-un-paso-mas-en-el-procesado-del-lenguaje-natural) del modelo grande del lenguaje (*LLM*) y el “mágico” acceso a los últimos estudios y bases de datos específicas pueden asimilarse a lo que proporciona las técnicas *RAG*.

Evidentemente, en el ejemplo que acabamos de poner, la buena práctica médica hace indispensables ambos elementos que el cerebro humano sabe combinar de forma natural, aunque no sin esfuerzo y tiempo, incluso disponiendo de las herramientas digitales actuales, que hacen más sencilla e inmediata la búsqueda de información.

## Proceso Detallado de RAG1

En detalle, un algoritmo *RAG* realiza las siguientes etapas:

**1\. Recepción de la pregunta.** El sistema recibe una pregunta del usuario. Esta pregunta se procesa para extraer las palabras clave y entender la intención.

**2\. Recuperación de documentos.** La pregunta se envía al modelo de recuperación.

- **Ejemplo de Recuperación basada en *embeddings*:**  
	1. La pregunta se convierte en un vector de *embeddings* utilizando un modelo pre-entrenado.
	2. Este vector se compara con los vectores de documentos en la base de datos.
	3. Se seleccionan los documentos con mayor similitud.
- **Ejemplo de BM25:**  
	1. Se [*tokeniza*](https://en.wikipedia.org/wiki/Lexical_analysis) la pregunta y se comparan las palabras clave con los índices invertidos de la base de datos.
	2. Se recuperan los documentos más relevantes según una puntuación de relevancia.

**3\. Filtrado y clasificación.** Los documentos recuperados se filtran para eliminar redundancias y clasificarlos según su relevancia. Pueden aplicarse técnicas adicionales como [*reranking*](https://www.pinecone.io/learn/series/rag/rerankers/) utilizando modelos más sofisticados.

**4\. Generación de la respuesta.** Los documentos filtrados se concatenan con la pregunta del usuario y se introducen en el modelo de generación. El *LLM* utiliza la información combinada para generar una respuesta que es coherente y directamente relevante a la pregunta. Por ejemplo, si utilizamos **GPT-3.5** como *LLM***,** la entrada al modelo incluye tanto la pregunta del usuario como fragmentos de los documentos recuperados. Finalmente, el modelo genera texto utilizando su capacidad para comprender el contexto de la información proporcionada.

En la siguiente sección vamos a ver algunas aplicaciones en las que la Inteligencia Artificial y los modelos grandes del lenguaje juegan un papel diferenciador y, en concreto, vamos a analizar cómo se benefician estos casos de usos de la aplicación de las técnicas *RAG*.

## Ejemplos de casos de uso que se benefician sustancialmente de usar RAG frente a no usar RAG

**1\. Atención al Cliente en *eCommerce***

- **Sin *RAG*:**
	- Un chatbot básico puede dar respuestas genéricas y potencialmente incorrectas sobre políticas de devolución.
	- Ejemplo: *Por favor, revise nuestra política de devoluciones en el sitio web*.
- **Con *RAG*:**
	- El chatbot accede a la base de datos de políticas actualizadas y proporciona una respuesta específica y precisa.
	- Ejemplo: *Puede devolver los productos dentro de 30 días desde la compra, siempre que estén en su embalaje original. Consulte más detalles \[aquí\]*.

**2\. Diagnóstico Médico**

- **Sin *RAG*:**
	- Un asistente virtual de salud podría ofrecer recomendaciones basadas solo en su entrenamiento previo, sin acceso a la información médica más reciente.
	- Ejemplo: *Es posible que tenga gripe. Consulte a su médico*
- **Con *RAG*:**
	- El asistente puede recuperar información de bases de datos médicas recientes y proporcionar un diagnóstico más preciso y actualizado.
	- Ejemplo: *Según los síntomas y los estudios recientes publicados en PubMed, podría estar enfrentando una infección viral. Consulte a su médico para un diagnóstico preciso.*

**3\. Asistencia en Investigación Académica**

- **Sin *RAG*:**
	- Un investigador recibe respuestas limitadas a lo que el modelo ya sabe, lo que puede no ser suficiente para temas altamente especializados.
	- Ejemplo: *Los modelos de crecimiento económico son importantes para entender la economía.*
- **Con *RAG*:**
	- El asistente recupera y analiza artículos académicos relevantes, proporcionando información detallada y precisa.
	- Ejemplo: *Según el estudio de 2023 en 'Journal of Economic Growth', el modelo XYZ ha mostrado un 20% más de precisión en la predicción de tendencias económicas en mercados emergentes.*

**4\. Periodismo**

- **Sin *RAG*:**
	- Un periodista recibe información genérica que puede no estar actualizada ni ser precisa.
	- Ejemplo: *La inteligencia artificial está cambiando muchas industrias.*
- **Con *RAG*:**
	- El asistente recupera datos específicos de estudios y artículos recientes, ofreciendo una base sólida para el artículo.
	- Ejemplo: *Según un informe de 2024 de 'TechCrunch', la adopción de IA en el sector financiero ha aumentado en un 35% en el último año, mejorando la eficiencia operativa y reduciendo costos*.

Por supuesto, para la mayoría de los usuarios que hemos experimentado los interfaces conversacionales más accesibles, como [ChatGPT](https://openai.com/chatgpt/), [Gemini](https://gemini.google.com/?hl=es-ES) o [Bing](https://www.microsoft.com/es-es/bing?form=MA13FV), podemos constatar que **las respuestas suelen ser completas y bastante precisas cuando se trata de preguntas de ámbito general**. Esto es porque estos agentes hacen uso de métodos *RAG* y otras técnicas avanzadas para proporcionar las respuestas. Sin embargo, no hay que remontarse mucho tiempo atrás en el que los asistentes conversacionales, como [Alexa](https://developer.amazon.com/es-ES/alexa), [Siri](https://www.apple.com/es/siri/) u [*OK Google*](https://assistant.google.com/intl/es_es/)*,* proporcionaban respuestas extremadamente simples y muy similares a las que explicamos en los ejemplos anteriores cuando no se hace uso de *RAG*.

## Conclusiones

Las técnicas de Generación Aumentada por Recuperación (*RAG*) mejora la precisión y relevancia de las respuestas de los modelos de lenguaje al combinar recuperación de documentos y generación de texto. Utilizando métodos de recuperación como BM25 o DPR y modelos avanzados de lenguaje, *RAG* proporciona respuestas más contextualizadas, actualizadas y precisas. En la actualidad, RAG es la clave para el desarrollo exponencial de la IA en el ámbito de los datos privados de empresas y organizaciones. En los próximos meses se espera una adopción masiva de *RAG* en diversas industrias, optimizando la atención al cliente, diagnósticos médicos, investigación académica y periodismo, gracias a su capacidad para integrar información relevante y actual en tiempo real.

*<sup>1. </sup> Para entender mejor esta sección, recomendamos al lector la lectura de [este trabajo previo](https://datos.gob.es/sites/default/files/datosgobes/tecnologias_emergentes_y_opendata_pln_awareness.pdf) en el que explicamos de forma didáctica los fundamentos del procesamiento del lenguaje natural y cómo enseñamos a leer a las máquinas.*

---

Contenido elaborado por Alejandro Alija,experto en Transformación Digital e Innovación. Los contenidos y los puntos de vista reflejados en esta publicación son responsabilidad exclusiva de su autor.

- [Añadir nuevo comentario](https://datos.gob.es/es/blog/# "Comparte tus ideas y opiniones.")