
[[ISO-IEC 22989]] - Standard de Information technology — Artificial intelligence — Artificial intelligence concepts and terminology y la ISO/IEC 25010 - Standard de modelos de calidad de productos de software.




# Procedimiento recomendado: ISO/IEC 25010 aplicado al análisis funcional para el rediseño del sistema de información HerStory

**Referencias:**  
- [ISO/IEC 25010 – Modelo de calidad del producto software](https://iso25000.com/index.php/normas-iso-25000/iso-25010)  
- [Análisis funcional (ATI)](https://www.atinfo.net/lineas-de-negocio/software-estudios-previos-y-desarrollo/152-v2-analisis-funcional)

---

## 1. Interpretación del plan

### 1.1 Relación entre ISO 25010 y análisis funcional

- **ISO 25010** define el modelo de calidad del producto: el grado en que el software satisface requisitos de los usuarios y aporta valor. Las características y subcaracterísticas del modelo son el marco para **evaluar** el producto.
- **Análisis funcional** (enfoque ATI) ordena el trabajo en tres niveles: (1) requisitos del negocio (por qué se hace el proyecto), (2) requisitos del usuario (qué podrán hacer los usuarios), (3) requisitos funcionales (qué debe implantar el desarrollo). El análisis debe ser sensible al contexto humano y sociológico del uso del sistema.
- **Aplicación al rediseño de HerStory:** usar las **características de calidad ISO 25010** como criterios para derivar y priorizar requisitos en cada nivel del análisis funcional, y para definir criterios de evaluación del sistema rediseñado.

### 1.2 Características de calidad ISO 25010 (resumen operativo)

| Característica | Subcaracterísticas relevantes para HerStory |
|----------------|--------------------------------------------|
| **Adecuación funcional** | Completitud funcional, corrección funcional, pertinencia funcional |
| **Eficiencia de desempeño** | Comportamiento temporal, utilización de recursos, capacidad |
| **Compatibilidad** | Coexistencia, interoperabilidad |
| **Capacidad de interacción (usabilidad)** | Reconocibilidad de la adecuación, aprendizabilidad, operabilidad, protección contra errores, involucración del usuario, **inclusividad**, asistencia al usuario, auto-descriptividad |
| **Fiabilidad** | Madurez, disponibilidad, tolerancia a fallos, recuperabilidad |
| **Seguridad de la información** | Confidencialidad, integridad, no repudio, responsabilidad, autenticidad |
| **Mantenibilidad** | Modularidad, reutilización, analizabilidad, modificabilidad, posibilidad de prueba |
| **Portabilidad** | Adaptabilidad, instalabilidad, reemplazabilidad |

*Fuente: [ISO 25010](https://iso25000.com/index.php/normas-iso-25000/iso-25010).*

Para HerStory (ciencia ciudadana, memoria democrática, género e interseccionalidad) son especialmente críticas: **adecuación funcional**, **capacidad de interacción** (con foco en inclusividad y operabilidad), **seguridad de la información** y **compatibilidad** (interoperabilidad con datos y sistemas externos).

---

## 2. Procedimiento recomendado en fases

### Fase 0. Definición del alcance del rediseño

- Documentar objetivos del rediseño (por qué se rediseña: mantenibilidad, usabilidad, inclusión, rendimiento, etc.).
- Delimitar el sistema de información HerStory (componentes, usuarios objetivo, datos y procesos clave).
- Registrar restricciones (plazos, recursos, normativa, LAECSP si aplica).

*Salida:* documento de alcance y criterios de éxito alineados con las características ISO 25010 que se priorizan.

---

### Fase 1. Requisitos del negocio (nivel 1) y mapeo a características de calidad

1. **Identificar requisitos del negocio** (objetivos del proyecto HerStory):  
   - Ej.: soporte a la investigación en memoria democrática y género, participación ciudadana, preservación y acceso a fuentes, transparencia y gobernanza de datos.
2. **Asignar cada objetivo a una o varias características ISO 25010** (tabla de trazabilidad):  
   - Ej.: “Participación ciudadana y usabilidad por perfiles diversos” → Adecuación funcional + Capacidad de interacción (inclusividad, operabilidad).  
   - “Datos abiertos y reutilizables” → Compatibilidad (interoperabilidad) + Portabilidad.
3. **Priorizar características** para el rediseño (por impacto en negocio y en usuarios).

*Salida:* tabla negocio ↔ características ISO 25010; lista priorizada de características para el análisis funcional.

---

### Fase 2. Requisitos del usuario (nivel 2) desde las subcaracterísticas

1. **Por cada característica priorizada**, derivar requisitos del usuario a partir de las **subcaracterísticas** ISO 25010:  
   - Adecuación funcional: tareas y objetivos de usuario que el sistema debe cubrir (completitud), resultados correctos (corrección), funciones que faciliten esas tareas (pertinencia).  
   - Capacidad de interacción: que el usuario entienda si el sistema le es adecuado (reconocibilidad), pueda aprenderlo en un tiempo razonable (aprendizabilidad), operarlo con facilidad (operabilidad), estar protegido frente a errores, sentirse motivado (involucración), y que personas con distintos contextos puedan usarlo (**inclusividad**).  
   - Compatibilidad: intercambio de información con otros sistemas (interoperabilidad) y coexistencia en el mismo entorno.
2. **Validar con usuarios/stakeholders** (comunidad académica, ciudadanía, equipos técnicos) que los requisitos del usuario reflejan necesidades reales y el contexto sociológico del uso (según enfoque ATI).
3. **Documentar** cada requisito del usuario con identificador, descripción y subcaracterística ISO 25010 asociada.

*Salida:* lista de requisitos del usuario trazables a subcaracterísticas ISO 25010 y validados con stakeholders.

---

### Fase 3. Requisitos funcionales (nivel 3) y criterios de aceptación

1. **Descomponer cada requisito del usuario** en requisitos funcionales concretos (qué debe implantar el equipo de desarrollo): funciones, estructuras de datos, flujos, integraciones.
2. **Definir criterios de aceptación** expresados en términos de **subcaracterísticas ISO 25010**:  
   - Ej.: “La búsqueda semántica devuelve resultados correctos para consultas tipo X” (corrección funcional).  
   - “La interfaz cumple criterios WCAG 2.1 nivel AA” (inclusividad).  
   - “Los tiempos de respuesta para consultas estándar son ≤ Y segundos” (comportamiento temporal).
3. **Revisar coherencia** con la memoria técnica y la lista de requisitos existentes del prototipo (p. ej. [[Pruebas_basicas_protitipo/Memoria técnica + Lista de requisitos 1]]) y con normativa (LAECSP, protección de datos, accesibilidad).
4. **Registrar trazabilidad** requisito del negocio → requisito del usuario → requisito funcional → subcaracterística ISO 25010.

*Salida:* especificación de requisitos funcionales con criterios de aceptación y matriz de trazabilidad a ISO 25010.

---

### Fase 4. Diseño y rediseño con criterios de calidad

1. **Arquitectura y diseño** del sistema de información HerStory de forma que satisfaga los requisitos funcionales y las subcaracterísticas priorizadas (modularidad, interoperabilidad, seguridad, inclusividad).
2. **Revisar** que el diseño permita **evaluar** luego el producto según ISO 25010: definición de métricas o indicadores por subcaracterística (p. ej. cobertura de tareas, tiempo de aprendizaje, cumplimiento WCAG, tiempos de respuesta).
3. **Documentar** decisiones de diseño que afecten a calidad (gestión de datos personales, sesgos, gobernanza, APIs).

*Salida:* documento de diseño/rediseño con justificación respecto a características y subcaracterísticas ISO 25010; borrador de plan de evaluación.

---

### Fase 5. Evaluación del producto rediseñado (ciclo de verificación)

1. **Definir el plan de evaluación** usando el modelo ISO 25010: para cada subcaracterística priorizada, método de medición o valoración (pruebas, inspección, métricas).
2. **Ejecutar evaluaciones** (pruebas funcionales, de usabilidad, de rendimiento, de accesibilidad, de interoperabilidad) y registrar resultados.
3. **Comparar** con los criterios de aceptación definidos en Fase 3 y con los objetivos de negocio de Fase 1.
4. **Iterar** sobre requisitos o diseño si no se alcanzan los niveles de calidad acordados.

*Salida:* informe de evaluación del producto frente a ISO 25010; acciones de mejora si aplica.

---

## 3. Resumen de productos de trabajo

| Fase | Producto principal |
|------|---------------------|
| 0 | Alcance del rediseño y criterios de éxito |
| 1 | Tabla negocio ↔ ISO 25010; priorización de características |
| 2 | Requisitos del usuario trazables a subcaracterísticas; validación con stakeholders |
| 3 | Requisitos funcionales, criterios de aceptación, matriz de trazabilidad |
| 4 | Diseño/rediseño documentado; plan de evaluación (borrador) |
| 5 | Plan de evaluación ejecutado; informe de evaluación y mejoras |

---

## 4. Referencias

- ISO/IEC 25010:2011 (SQuaRE – Modelo de calidad del producto software). Resumen operativo: [iso25000.com – ISO 25010](https://iso25000.com/index.php/normas-iso-25000/iso-25010).
- Análisis funcional en estudios previos y desarrollo de software: identificación de necesidades por eslabón (negocio, usuario, desarrollo) y sensibilidad al contexto social y legal. [ATI – Análisis funcional](https://www.atinfo.net/lineas-de-negocio/software-estudios-previos-y-desarrollo/152-v2-analisis-funcional).
- Contexto HerStory: [[Qué significa HerStory como Proyecto de ciencia ciudadana]]; requisitos y memoria técnica: [[Pruebas_basicas_protitipo/Memoria técnica + Lista de requisitos 1]].
