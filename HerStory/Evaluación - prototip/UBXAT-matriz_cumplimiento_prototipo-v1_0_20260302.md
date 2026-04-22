**Documentación vinculada a las columnas de la tabla:**

- **Componente/Funcionalidad (Licitación):** TD44_1 Memòria
  justificativa 2024_198.docx y TD79_1 PPT 2024_198.docx

- **Propuesta Península (Memoria técnica):** Memoria tecnica.pdf

- **Evidencia del fabricante (Guías UBXAT / API):** documentos
  proporcionados por Península y
  HerStory_kgConstruction-v2Def_20250611.docx

- **Evidencia de evaluación/validación de UBXAT:**
  UBXAT-protocolo_evaluación_requerimientos-v1_0_20260305.docx y
  UBXAT-resumen_aspectos_evaluables-v1_0_20260305.docx

**Leyenda de la columna "Estado":**

- ✅ Desarrollado

- 🟡 Parcial o no demostrable del todo

- ❌ No documentado (no se puede verificar con los PDFs/PNG disponibles)

# Backend

## A) Ingesta/ETL y administración de datos

  -------------------------------------------------------------------------------------------------------------------------------------------------
  **Capa            **Componente/Funcionalidad   **Propuesta      **Evidencia del  **Evidencia de          **Estado**    **Riesgo/impacto
  (Backend/UI)**    (Licitación)**               Península        fabricante       evaluación/validación                 (trazado)**
                                                 (Memoria         (Guías UBXAT /   de UBXAT**                            
                                                 técnica)**       API)**                                                 
  ----------------- ---------------------------- ---------------- ---------------- ----------------------- ------------- --------------------------
  Backend           **Construcción del Knowledge Requisito        La documentación Evaluación: "no         **🟡 Parcial  **Riesgo alto**: si el KG
  (**RESULTADO**)   Graph a partir de los        explícito TD44-2 UBXAT describe   evaluado / preparan BD" o no          no está probado como
                    requisitos establecidos en                    ingesta/ETL e    → no hay prueba         demostrable   "construido según
                    la fase de diseño**                           integración con  ejecutada que confirme  del todo**    requisitos",
                                                                  el grafo, pero   la construcción del KG                SPARQL/Q&A/visualización
                                                                  la "construcción según requisitos                      quedan comprometidos.
                                                                  del KG según                                           
                                                                  requisitos de                                          
                                                                  diseño" no                                             
                                                                  aparece como                                           
                                                                  evidencia                                              
                                                                  separada (queda                                        
                                                                  implícita)                                             

  Backend           Ingesta y procesamiento de   ETL,             Módulo de        Evaluación: sin prueba  **🟡 Parcial  **Riesgo alto**: sin ETL
  (**MECANISMO**)   datos (ETL) para alimentar   transformación y ingesta/ETL      ejecutada (no evaluado) o no          probado no se garantiza la
                    el KG                        carga a grafo    documentado                              demostrable   generación/actualización
                                                                  (guía +                                  del todo**    del KG.
                                                                  API/operativa)                                         
  -------------------------------------------------------------------------------------------------------------------------------------------------

## B) SPARQL / consultas avanzadas 

  ----------------------------------------------------------------------------------------------------------------------------------------------------
  **Capa           **Componente/Funcionalidad   **Propuesta   **Evidencia del    **Evidencia de          **Estado**       **Riesgo/impacto (trazado)**
  (Backend/UI)**   (Licitación)**               Península     fabricante (Docs   evaluación/validación                    
                                                (Memoria      UBXAT)**           de UBXAT**                               
                                                técnica)**                                                                
  ---------------- ---------------------------- ------------- ------------------ ----------------------- ---------------- ----------------------------
  Backend          Endpoint SPARQL operativo    SPARQL como   Guía + API SPARQL  Pruebas ejecutadas      **✅             **Riesgo bajo**:
                                                pilar de      (/api/v1/sparql)   (POST) con              Desarrollado**   interoperabilidad/consulta
                                                consulta                         comportamiento esperado                  por API validada.

  Backend          SELECT / FILTER / LIMIT /    Consultas     Soporte SPARQL     Pruebas muestran count  **✅             **Riesgo bajo**: capacidades
                   ASK / COUNT                  completas     descrito           numérico y ASK          Desarrollado**   críticas confirmadas.
                                                                                 booleano, etc.                           

  UI               Coherencia resultados UI vs  ---           UI muestra         Evaluación indica       **🟡 Parcial o   **Riesgo medio**: UI puede
                   servidor                                   resultados         discrepancias UI vs     no demostrable   inducir a error aunque
                                                                                 servidor                del todo**       backend funcione.

  UI               Biblioteca de consultas      Prevista      Presente           Evaluación: pocas       **🟡 Parcial o   **Riesgo medio**: limita
                   predefinidas (UI)                                             opciones/feedback       no demostrable   operativa de usuario no
                                                                                 limitado;               del todo**       técnico.
                                                                                 previsualización                         
                                                                                 truncada → "Parcial"                     
  ----------------------------------------------------------------------------------------------------------------------------------------------------

## C) Módulo Agente / Conversacional 

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Capa             **Componente/Funcionalidad   **Propuesta Península    **Evidencia del   **Evidencia de            **Estado**       **Riesgo/impacto
  (Backend/UI)**     (Licitación)**               (Memoria técnica)**      fabricante (Guías evaluación/validación de                   (trazado)**
                                                                           UBXAT / API)**    UBXAT**                                    
  ------------------ ---------------------------- ------------------------ ----------------- ------------------------- ---------------- ------------------------
  Backend (función)  Q&A en lenguaje natural con  Agente conversacional,   API chat + guía   Evaluación: se puede      **🟡 Parcial o   **Riesgo alto**: el
                     recuperación de información  extracción y respuesta   agente            interactuar pero "no      no demostrable   objetivo principal
                                                                                             recupera información" /   del todo**       (consulta asistida)
                                                                                             respuestas inconsistentes                  queda debilitado.

  Backend            **Disponibilidad de un LLM y Requisito TD44-1 (LLM +  Integración con   Hay interacción de chat,  **🟡 Parcial o   **Riesgo muy alto**:
                     entrenamiento/ajuste para    entrenamiento/ajuste; se LLM documentada   pero no evidencia de      no demostrable   requisito clave; si no
                     los objetivos del proyecto** valora reutilización     (p. ej. Gemini) + entrenamiento/ajuste ni   del todo**       hay ajuste/adecuación y
                                                  LLM)                     canal de chat en  de logro de objetivos (y                   no logra recuperación
                                                                           API/plataforma    además falla                               fiable, impacta el
                                                                                             recuperación)                              cumplimiento del
                                                                                                                                        prototipo.

  Backend            **Integración                TD44-4 (integración en   Arquitectura con  Evaluación: el agente no  **🟡 Parcial o   **Riesgo alto**: si el
  (integración)      neuro-simbólica: integrar    prototipo) + "mecanismos LLM + KG/Neo4j +  recupera info y           no demostrable   LLM no usa el KG de
                     KG/razonamiento (simbólico)  de integración" como     SPARQL/API        desaparecen               del todo**       forma efectiva (y
                     y LLM en un prototipo**      componente clave (TD79)  documentada       trazabilidad/confianza;                    trazable), se pierde el
                                                                                             la integración                             valor diferencial NeSy.
                                                                                             "end-to-end" efectiva no                   
                                                                                             queda validada                             

  UI                 Trazabilidad (fuentes /      Prometida                Guías describen   Evaluación: no muestra    **❌ No          **Riesgo alto**: sin
  (explicabilidad)   source chips)                (explicabilidad/ética)   fuentes           procedencia y desaparece  documentado (no  trazas baja confianza y
                                                                                             en versión posterior →    se puede         auditabilidad.
                                                                                             "No cumple"               verificar con    
                                                                                                                       los PDFs/PNG     
                                                                                                                       disponibles)**   

  UI (calidad)       Indicador de confianza       Previsto                 (Documentado en   Evaluación: desaparece →  **❌ No          **Riesgo medio-alto**:
                                                                           versiones)        "No cumple"               documentado (no  dificulta detectar
                                                                                                                       se puede         respuestas
                                                                                                                       verificar con    débiles/alucinaciones.
                                                                                                                       los PDFs/PNG     
                                                                                                                       disponibles)**   

  UI (operación)     Historial / reiniciar sesión Previsto                 (Aparece en       Evaluación: desaparece →  **❌ No          **Riesgo medio**:
                                                                           guías/versions)   "No cumple"               documentado (no  empeora repetibilidad de
                                                                                                                       se puede         pruebas/consultas.
                                                                                                                       verificar con    
                                                                                                                       los PDFs/PNG     
                                                                                                                       disponibles)**   

  UI (rendimiento)   Métricas de rendimiento      Previstas                Guías describen   Evaluación: "Cumple"      **✅             **Riesgo bajo**: medida
                     (tiempo)                                              métricas                                    Desarrollado**   disponible.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------

## D) Inclusión y diversidad (perspectiva de género) 

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  **Capa           **Componente/Funcionalidad   **Propuesta Península  **Evidencia del      **Evidencia de          **Estado**       **Riesgo/impacto
  (Backend/UI)**   (Licitación)**               (Memoria técnica)**    fabricante (docs     evaluación/validación                    (trazado)**
                                                                       UBXAT)**             de UBXAT**                               
  ---------------- ---------------------------- ---------------------- -------------------- ----------------------- ---------------- ------------------
  Backend          Perspectiva de género y      Requisito transversal  Documentación de     Evaluación: "No cumple" **❌ No          **Riesgo muy
  (resultado)      consultas "gender-aware"     con foco en            prompts/estrategia   (no se obtienen         documentado (no  alto**: eje de
                                                explicabilidad/ética   "gender-aware"       resultados esperados en se puede         requisitos; afecta
                                                (TD44)                                      práctica)               verificar con    conformidad global
                                                                                                                    los PDFs/PNG     del prototipo.
                                                                                                                    disponibles)**   

  -----------------------------------------------------------------------------------------------------------------------------------------------------

## E) KG-to-text (Wikipedia) 

  -------------------------------------------------------------------------------------------------------------------------------------------
  **Capa           **Componente/Funcionalidad   **Propuesta   **Evidencia del   **Evidencia de            **Estado**       **Riesgo/impacto
  (Backend/UI)**   (Licitación)**               Península     fabricante        evaluación/validación**                    (trazado)**
                                                (Memoria      (UBXAT)**                                                    
                                                técnica)**                                                                 
  ---------------- ---------------------------- ------------- ----------------- ------------------------- ---------------- ------------------
  Backend          KG-to-text para redacción    Requisito     No hay            No hay pruebas ni         **❌ No          **Riesgo muy
                   automática de artículos      TD44-5        módulo/endpoint   validación aportada       documentado (no  alto**: falta una
                   Wikipedia                                  documentado en                              se puede         función
                                                              guías disponibles                           verificar con    prioritaria del
                                                                                                          los PDFs/PNG     proyecto.
                                                                                                          disponibles)**   

  -------------------------------------------------------------------------------------------------------------------------------------------

# Frontend

## F) Plataforma Web (UI/UX), accesibilidad e idiomas 

  ---------------------------------------------------------------------------------------------------------------------------------------------
  **Capa           **Componente/Funcionalidad   **Propuesta    **Evidencia   **Evidencia de            **Estado**       **Riesgo/impacto
  (Backend/UI)**   (Licitación)**               Península      del           evaluación/validación**                    (trazado)**
                                                (Memoria       fabricante                                               
                                                técnica)**     (Guías                                                   
                                                               UBXAT)**                                                 
  ---------------- ---------------------------- -------------- ------------- ------------------------- ---------------- -----------------------
  UI               Accesibilidad WCAG           Compromiso     Sin           Evaluación: "No tiene     **❌ No          **Riesgo alto**: puede
                                                WCAG           validación    criterios de              documentado (no  impedir adopción y
                                                               WCAG en guías accesibilidad (WCAG) --   se puede         supone no conformidad
                                                                             No cumple"                verificar con    transversal.
                                                                                                       los PDFs/PNG     
                                                                                                       disponibles)**   

  UI               Responsive (móvil/tablet)    Prometido      ---           Evaluación: mobile no     **❌ No          **Riesgo medio-alto**:
                                                                             funciona bien / versión   documentado (no  limita uso en
                                                                             desktop → "No cumple"     se puede         dispositivos y
                                                                                                       verificar con    operativa real.
                                                                                                       los PDFs/PNG     
                                                                                                       disponibles)**   

  UI               Idiomas CAT/ES/EN            ---            ---           Evaluación:               **🟡 Parcial o   **Riesgo medio**:
                   consistentes                                              inconsistencia de idioma  no demostrable   fricción de uso y
                                                                             → "Parcial"               del todo**       posible no conformidad
                                                                                                                        lingüística.

  UI               Monitorización visible en UI Prevista       Documentada   Evaluación: desaparece en **❌ No          **Riesgo medio**:
                                                               (según        versión posterior → "No   documentado (no  dificulta
                                                               versiones)    cumple"                   se puede         diagnóstico/operación
                                                                                                       verificar con    desde UI.
                                                                                                       los PDFs/PNG     
                                                                                                       disponibles)**   

  UI               Barra de navegación          UI             Presente      Evaluación: "Cumple"      **✅             **Riesgo bajo**.
                                                estructurada                                           Desarrollado**   
  ---------------------------------------------------------------------------------------------------------------------------------------------

## G) Grafo: visualización y transparencia 

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  **Capa           **Componente/Funcionalidad   **Propuesta Península  **Evidencia   **Evidencia de            **Estado**       **Riesgo/impacto
  (Backend/UI)**   (Licitación)**               (Memoria técnica)**    del           evaluación/validación**                    (trazado)**
                                                                       fabricante                                               
                                                                       (Guías                                                   
                                                                       UBXAT)**                                                 
  ---------------- ---------------------------- ---------------------- ------------- ------------------------- ---------------- -----------------------
  UI               Exploración visual           Prevista               Descrita      Evaluación: existe pero   **🟡 Parcial o   **Riesgo medio**:
                   (pan/zoom)                                                        con limitaciones          no demostrable   reduce utilidad para
                                                                                                               del todo**       inspección/validación
                                                                                                                                del grafo.

  UI               Inspección detallada de nodo Prevista               Descrita      Evaluación: no muestra    **🟡 Parcial o   **Riesgo medio**:
                                                                                     detalle completo →        no demostrable   dificulta auditoría y
                                                                                     "Parcial"                 del todo**       depuración.

  UI               Transparencia de             Implicada por          ---           Evaluación: "No hay       **❌ No          **Riesgo alto**: afecta
                   criterio/perspectiva (por    explicabilidad/ética                 transparencia..." → "No   documentado (no  interpretabilidad y
                   qué se muestran datos)                                            cumple"                   se puede         confianza; puede
                                                                                                               verificar con    invalidar el uso
                                                                                                               los PDFs/PNG     analítico.
                                                                                                               disponibles)**   

  UI               Panel de control             Previsto               Descrito      Evaluación: "Cumple"      **✅             **Riesgo bajo**.
                   (estadísticas                                                                               Desarrollado**   
                   nodos/relaciones)                                                                                            
  -----------------------------------------------------------------------------------------------------------------------------------------------------

# Resumen

## A) Ingesta/ETL y administración de datos (BACKEND)

**Cumple:** hay documentación de módulo de ingesta/ETL y operativa para
alimentar el grafo.\
**Falla / no se demuestra:** la evaluación indica que **no se evaluó**
(preparan BD), por lo que no queda probado que el KG esté construido
según requisitos de diseño ni que el ETL funcione end-to-end.\
**Riesgo dominante:** **alto** por dependencia en cascada (SPARQL, Q&A y
visualización dependen del KG/ETL).

## B) SPARQL / consultas avanzadas (BACKEND primero)

**Cumple:** el **backend SPARQL** queda validado con pruebas ejecutadas
(endpoint, ASK/COUNT, etc.).\
**Falla / parcial:** la capa **UI** presenta discrepancias frente al
servidor y la biblioteca de consultas es limitada (parcial).\
**Riesgo dominante:** **medio**, por riesgo de interpretación errónea en
UI aunque el backend funcione bien.

## C) Módulo Agente / Conversacional (BACKEND)

**Cumple:** existe el canal conversacional (API/guías) y métricas de
rendimiento (tiempo) evaluadas como "cumple".\
**Falla / parcial:** el Q&A **no recupera información** de forma fiable;
además desaparecen elementos clave de explicabilidad (fuentes),
confianza e historial en versiones posteriores.\
**Riesgo dominante:** **alto--muy alto**, porque compromete el objetivo
principal del prototipo y debilita la integración neuro-simbólica
(TD44-1 y TD44-4).

## D) Inclusión y diversidad (perspectiva de género) (BACKEND/criterio funcional)

**Cumple:** el fabricante documenta enfoque/prompting "gender-aware".\
**Falla:** la evaluación concluye "no cumple" en la práctica (no se
obtienen los resultados esperados), pese a estar descrito en
documentación.\
**Riesgo dominante:** **muy alto**, por ser un eje de requisitos y
afectar a la conformidad global (dimensión ética/explicabilidad).

## E) KG-to-text (Wikipedia) (BACKEND)

**Cumple:** --- (no se aporta evidencia funcional ni de módulo).\
**Falla:** no hay módulo/endpoint documentado ni pruebas de KG-to-text,
pese a ser función prioritaria explícita en TD44.\
**Riesgo dominante:** **muy alto**, por ausencia de una de las dos
aplicaciones prioritarias del proyecto.

## F) Plataforma Web (UI/UX), accesibilidad e idiomas (FRONTEND)

**Cumple:** navegación general ("barra de navegación") evaluada como
"cumple".\
**Falla:** accesibilidad WCAG y responsive **no cumplen**;
monitorización UI desaparece en versiones; idiomas son inconsistentes
(parcial).\
**Riesgo dominante:** **alto**, por impacto directo en adopción/uso y
posibles incumplimientos transversales de interfaz.

## G) Grafo: visualización y transparencia (FRONTEND)

**Cumple:** panel de control (estadísticas) "cumple";
exploración/inspección existen pero con limitaciones (parcial).\
**Falla:** falta de **transparencia** sobre por qué se muestran
determinados datos (no cumple), afectando interpretabilidad.\
**Riesgo dominante:** **alto**, por pérdida de confianza/auditabilidad
en la capa de análisis del conocimiento.
