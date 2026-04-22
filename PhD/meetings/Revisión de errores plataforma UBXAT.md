---
date: 2026-02-23
authors:
  - Matheus Jenevain
  - Elena Gómez
tags:
  - op/activity/meeting
---
Se exponen las preocupaciones identificadas en la revisión profunda de la entrega realizada por parte de Península. 

Al iniciar se identifica que no se tienen datos en la plataforma otra vez

Se observan errores en especificaciones puntuales de interfáz, arquitectura y desiciones de diseño de la misma. 

Matheus piensa que es mejor tener una reunión preliminar con Thomas para mostrar los distintos aspectos que no están funcionando por capas, desde el exterior, hasta los asuntos más profundos. Lo prioritario es revisar la base de conocimiento ya que la información estructurada con la que se está alimentando no está siendo procesada adecuadamente en la aruquitectura.

Elena pregunta por la decisión de diseño de optar por la estrategia de prompt engineering sobre otras como orquestación de agentes especializados. Matheus expresa preocupación por que si esta decisión de diseño no está funcionando los cambios que habría que hacer son profundos. 

Elena expresa interés en conocer partes del proceso como: 
1. el ground truth mapper
2. `backend/rag/graph_rag.py`(QA_TEMPLATE (graph_rag.py) - For Answering Questions)
3. `EXTRACTION_PROMPT` in `backend/core/prompts/prompts.py`
4. CANONICAL_NODE_TYPES 
5. otros relacionados

Acuerdos: 
1. Matheus escribirá en el chat conjunto con Miquel sus observaciones
2. Elena también
