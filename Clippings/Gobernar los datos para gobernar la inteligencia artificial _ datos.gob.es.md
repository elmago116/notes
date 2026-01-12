---
title: Gobernar los datos para gobernar la inteligencia artificial | datos.gob.es
source: https://datos.gob.es/es/blog/gobernar-los-datos-para-gobernar-la-inteligencia-artificial
authors: "[[Gobernar los datos para gobernar la inteligencia artificial | datos.gob.es]]"
published:
created: 2026-01-09
description: Plataforma de datos abiertos del Gobierno de España
tags:
  - op/tools
  - tech/Ai
  - op/suggested/tutors
DOI:
Type: Web
year:
---
[![Inicio](https://datos.gob.es/themes/custom/dge_theme/logo.svg)](https://datos.gob.es/es/ "Inicio")

## Gobernar los datos para gobernar la inteligencia artificial

Fecha publicación 24/07/2024

![tablet con iconos IA](https://datos.gob.es/sites/default/files/styles/wide/public/blog/image/58.jpg?itok=tSTT3HOP)

Descripción

La publicación el **viernes 12 de julio de 2024 del** [**Reglamento de Inteligencia Artificial**](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=OJ%3AL_202401689) (RIA o *AIA* en sus siglas en inglés) abre una nueva etapa en el marco regulatorio europeo y global. La norma se caracteriza por tratar de conjugar dos almas. De un lado se trata de asegurar que la tecnología **no genere riesgos sistémicos** para la democracia, la garantía de nuestros derechos y el ecosistema socioeconómico en su conjunto. De otro lado, se busca un **enfoque orientado al desarrollo de producto** de modo que responda a los altos estándares de fiabilidad, seguridad y cumplimiento normativo definidos por la Unión Europea.

## Ámbito de aplicación de la norma

La norma permite **diferenciar entre sistemas de bajo y medio riesgo, sistemas de alto riesgo y modelos de IA de uso general**. Para calificar los sistemas, el RIA define criterios relacionados con el sector regulado por la Unión Europea (Anexo I) y define el contenido y alcance de aquellos sistemas que por su naturaleza y finalidad podrían generar riesgos (Anexo III). Los modelos son altamente dependientes del volumen de datos, sus capacidades y la carga operacional.

El **RIA solo afecta a los dos últimos casos: sistemas de alto riesgo y modelos de IA de uso general**. Los sistemas de alto riesgo exigen la evaluación de la conformidad a través de organismos notificados. Estos son entidades ante las que se presentan evidencias de que el desarrollo se ajusta al RIA. En este sentido, los modelos están sujetos a fórmulas de control por la Comisión que aseguran la prevención de riesgos sistémicos. No obstante, estamos ante un marco normativo **flexible que favorece la investigación,** relajando su aplicación en entornos de experimentación, así como mediante el despliegue de *sandboxes* para el desarrollo.

La norma establece una serie de **“ *requisitos de los sistemas de IA de alto riesgo* ”** (sección segunda del capítulo tercero) que deberían constituir un **marco de referencia para el desarrollo de cualquier sistema e inspirar los códigos de buenas prácticas, normas técnicas y esquemas de certificación**. Entre ellos, ocupa un lugar central el artículo 10 sobre “ ***datos y gobernanza de datos* ”**. Este proporciona indicaciones muy precisas sobre las condiciones de diseño de los sistemas de IA, particularmente cuando supongan tratar datos personales o cuando se proyecten sobre personas físicas.

Esta gobernanza debería considerarse por quienes proporcionen la **infraestructura básica y/o los conjuntos de datos, gestionen espacios de datos** o los llamados *Digital Innovation Hub* s, que **ofrezcan servicios de soporte**. En nuestro ecosistema, caracterizado por una alta prevalencia de PYMEs y/o equipos de investigación, la gobernanza de datos se proyecta sobre la **calidad, seguridad y fiabilidad** en sus acciones y resultados. Por ello es necesario **asegurar los valores que el RIA impone a los conjuntos de datos de entrenamiento, validación y prueba en sistemas de alto riesgo** y, en su caso, cuando se empleen técnicas que impliquen el entrenamiento de modelos de IA.

Estos valores pueden alinearse con los principios del artículo 5 del [**Reglamento General de Protección de Datos (RGPD)**](https://www.boe.es/buscar/doc.php?id=DOUE-L-2016-80807) y los enriquecen y complementan. A ellos se añade el enfoque de riesgo y la protección de datos desde el diseño y por defecto. Relacionar unos y otros constituye un ejercicio sin duda interesante.

## Garantizar el origen legítimo de los datos: Lealtad y licitud

Junto a la referencia común a la cadena de valor asociada a los datos, hay que referirse a una **cadena de custodia**  que garantice la legalidad en los **procesos de recogida de datos**. El origen de los datos, particularmente en el caso de los datos personales, debe ser **lícito, legítimo y su uso coherente con la finalidad original de su recogida**. Por ello es indispensable una adecuada **catalogación de los conjuntos de datos en origen** que asegure una correcta descripción de su legitimidad y condiciones de uso.

Esta es una cuestión que afecta a los entornos de *open data*, a los organismos y servicios de acceso a datos detallados en el [Reglamento de gobernanza de datos](https://datos.gob.es/es/blog/la-aplicacion-del-reglamento-ue-sobre-gobernanza-de-datos-en-las-administraciones-publicas) (*DGA* en sus siglas en inglés) o el [Espacio Europeo de Datos de Salud](https://www.consilium.europa.eu/es/press/press-releases/2024/03/15/european-health-data-space-council-and-parliament-strike-provisional-deal/) (*EHDS*) y a buen seguro inspirará futuras regulaciones. Lo usual será combinar fuentes externas de datos con la información que maneja la PYME.

## Minimización de los datos, exactitud y limitación de finalidad

El RIA ordena, de una parte, **realizar una evaluación de la disponibilidad, la cantidad y la adecuación de los conjuntos de datos necesarios**. De otra, exige que **los conjuntos de datos de entrenamiento, validación y prueba sean pertinentes, suficientemente representativos y posean las propiedades estadísticas adecuadas**. Esta tarea es muy relevante para los derechos de las personas o los colectivos afectados por el sistema. Además, en la mayor medida posible, carecerán de errores y estarán completos en vista de su finalidad prevista. RIA predica estas propiedades para cada conjunto de datos individualmente o para una combinación de estos.

Para la consecución de tales objetivos resulta necesario asegurar el despliegue de las técnicas adecuadas:

- **Realizar las operaciones de tratamiento oportunas** **para la preparación de los datos**, como la anotación, el etiquetado, la depuración, la actualización, el enriquecimiento y la agregación.
- **Formular supuestos**, en particular en lo que respecta a la información que se supone que miden y representan los datos. O, dicho en un lenguaje más coloquial, definir los casos de uso.
- **Tener en cuenta**, en la medida necesaria para la finalidad prevista, **las características o elementos particulares del entorno** geográfico, contextual, conductual o funcional específico en el que está previsto que se utilice el sistema de IA de alto riesgo.

## Aplicar las lecciones aprendidas desde la protección de datos, desde el diseño y por defecto

El artículo 10 de RIA obliga a documentar las decisiones pertinentes relativas al diseño y a detectar lagunas o deficiencias pertinentes en los datos que impidan el cumplimiento del RIA y la forma de subsanarlas. En resumen, **no basta con garantizar la gobernanza de datos, también es necesario proporcionar evidencia documental y mantener una actitud proactiva y vigilante** durante todo el ciclo de vida de los sistemas de información.

Estas dos obligaciones integran la clave de bóveda del sistema. Y su lectura debería ser incluso mucho más amplia en la dimensión jurídica. Las lecciones aprendidas en el RGPD enseñan que existe una doble condición para la responsabilidad proactiva y la garantía de los derechos fundamentales. La primera es intrínseca y material: **el despliegue de la ingeniería de la privacidad al servicio de la protección de datos desde el diseño y por defecto asegura el cumplimiento del RGPD**. La segunda es contextual: los tratamientos de datos personales no se dan en el vacío, sino en un **contexto amplio y complejo** regulado por otros sectores del Ordenamiento.

La gobernanza de datos opera estructuralmente desde los cimientos a la bóveda de los sistemas de información basados en IA. Asegurar que exista, sea adecuada y funcional es esencial. Así lo ha entendido la Estrategia de Inteligencia Artificial 2024 del Gobierno de España que trata de dotar al país de esas palancas que dinamicen nuestro desarrollo.

RIA plantea un salto cualitativo y subraya el enfoque funcional desde el que deben leerse los principios de protección de datos subrayando la dimensión poblacional. Ello obliga a repensar las condiciones en las que se ha venido cumpliendo el RGPD en la Unión Europea. Urge abandonar los modelos basados en plantillas que la empresa de consultoría copia-pega. Es evidente que las listas de control y la estandarización son imprescindibles. Sin embargo, su efectividad es altamente dependiente del ajuste fino. Y ello obliga a apelar particularmente a los profesionales que soportan el cumplimiento de este objetivo a dedicar sus mayores esfuerzos para dotar de sentido profundo al cumplimiento del Reglamento de Inteligencia Artificial.

Puedes ver un resumen del reglamento en la siguiente infografía:

[![Captura de la infografía](https://datos.gob.es/sites/default/files/datosgobes/datos-gobernanza-reglamento-europeo-es.jpg)](https://datos.gob.es/sites/default/files/blog/file/datos-gobernanza-reglamento-europeo-es.pdf "aquí")

Puedes accerder a la versión accesible e interactiva [aquí](https://datos.gob.es/sites/default/files/blog/file/datos-gobernanza-reglamento-europeo-es.pdf)

---

*Contenido elaborado por Ricard Martínez Martínez, Director de la Cátedra de Privacidad y Transformación Digital, Departamento de Derecho Constitucional de la Universitat de València. Los contenidos y los puntos de vista reflejados en esta publicación son responsabilidad exclusiva de su autor.*

### Documentación

| Infografía resumen del Reglamento | 1.80 MB | PDF |  |
| --- | --- | --- | --- |

- [Añadir nuevo comentario](https://datos.gob.es/es/blog/# "Comparte tus ideas y opiniones.")