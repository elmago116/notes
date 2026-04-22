# Comparación de inventario UB con Peninsula

**Análisis comparativo de metodologías de transformación de datos a grafo de conocimiento**

---

## Resumen Ejecutivo

Comparación entre dos enfoques para transformar datos estructurados (RDF, CSV, SQL):

- **Enfoque UB**: Transformación manual sistemática basada en reglas ontológicas
- **Enfoque Península**: Procesamiento automatizado con inteligencia artificial

---

## 1. Metodologías de Transformación

### 1.1 Universidad de Barcelona - Enfoque Manual

**Características:**
- **Método**: 4 reglas de transformación predefinidas
- **Base**: Ingeniería ontológica formal y Web Semántica  
- **Input**: BD relacional "Cultura y Censura" con esquema conocido
- **Output**: Ontología OWL/RDF con relaciones explícitas

**Reglas aplicadas:**
1. Tabla no asociativa → Clase ontológica (`owl:Class`)
2. Tabla asociativa → Propiedades inversas (`owl:ObjectProperty`) 
3. Clave foránea → Propiedad de objeto
4. Atributo regular → Propiedad de datos (`owl:DatatypeProperty`)

### 1.2 Península - Enfoque Automatizado

**Características:**
- **Método**: Pipeline de 5 fases con Google Gemini AI
- **Base**: Procesamiento de lenguaje natural y ML
- **Input**: Archivos RDF, CSV, SQL de cualquier dominio
- **Output**: Grafo de propiedades Neo4j con búsqueda semántica

**Pipeline:**
1. **Ingesta**: Detección automática de formatos
2. **Análisis**: Fragmentación con IA  
3. **Extracción**: Detección automática de entidades
4. **Almacenamiento**: Neo4j con embeddings
5. **Enriquecimiento**: Entity linking automático

---

## 2. Definición de Entidades

### 2.1 UB - 15 Clases Específicas del Dominio

| Clase OWL | Origen | Propósito |
|-----------|--------|-----------|
| `:Expediente` | EXPEDIENTES | Documentos archivísticos |
| `:LibroPublicado` | LIBROS_PUBLICADOS | Obras publicadas |
| `:Autor` | AUTOR | Autores y escritores |
| `:Lector` | LECTORES | Censores oficiales |
| `:Editor` | EDITORES | Casas editoriales |

**Ejemplo formal:**
```turtle
:LibroPublicado a owl:Class .
:tieneAutor a owl:ObjectProperty ; 
    rdfs:domain :LibroPublicado ; 
    rdfs:range :Autor .
```

### 2.2 Península - 6 Tipos Genéricos

| Tipo | Propiedades Dinámicas |
|------|----------------------|
| **Person** | `full_name`, `nationality`, `birth_date` |
| **Document** | `title`, `content_type`, `author` |
| **Organization** | `name`, `type`, `founding_date` |
| **Location** | `name`, `coordinates`, `admin_level` |
| **Event** | `name`, `date`, `participants` |
| **Concept** | `name`, `description`, `domain` |

---

## 3. Tecnologías y Capacidades

### 3.1 Stack Tecnológico

| Componente | UB | Península |
|------------|----|-----------| 
| **Modelado** | OWL 2.0 | Neo4j Property Graph |
| **Consultas** | SPARQL | Cypher + Semantic Search |
| **Procesamiento** | Manual | Google Gemini AI |
| **Escalabilidad** | BD específica | Múltiples formatos |

### 3.2 Soporte de Formatos

| Formato | UB | Península |
|---------|----|---------| 
| **RDF/Turtle** | ✅ Nativo | ✅ Parsing automático |
| **CSV** | ❌ Transformación manual | ✅ Detección automática |
| **SQL** | ❌ Transformación manual | ✅ Parsing INSERT |
| **Texto libre** | ❌ No soportado | ✅ Extracción NLP |

---

## 4. Ventajas y Limitaciones

### 4.1 Universidad de Barcelona

**✅ Ventajas:**
- Precisión semántica absoluta (100%)
- Cumplimiento total estándares W3C
- Reasoning formal con inferencias lógicas
- Interoperabilidad garantizada con sistemas RDF

**❌ Limitaciones:**
- Proceso manual intensivo en tiempo
- Escalabilidad limitada a BD específicas
- Requiere expertise en ingeniería ontológica
- Inflexible ante cambios de esquema

### 4.2 Península

**✅ Ventajas:**
- Automatización completa del proceso
- Flexibilidad para múltiples formatos
- Escalabilidad horizontal (100 chunks/proceso)
- Búsqueda en lenguaje natural

**❌ Limitaciones:**
- Precisión probabilística (99%, 1% error)
- Dependencia de infraestructura cloud
- Menos control semántico explícito
- No garantiza consistencia lógica formal

---

## 5. Casos de Uso Recomendados

### 5.1 Usar Enfoque UB cuando:
- Se requiere máxima precisión semántica
- BD patrimoniales con esquemas definidos
- Investigación académica con reasoning formal
- Interoperabilidad crítica con sistemas LOD

### 5.2 Usar Enfoque Península cuando:
- Proyectos de gran escala multi-fuente
- Datos heterogéneos y no estructurados
- Aplicaciones con búsqueda natural
- Rapid prototyping de sistemas

---

## 6. Recomendación para HerStory

### Enfoque Híbrido Sugerido

**Fase 1 (UB)**: 
- Crear ontología formal de referencia
- Definir clases core del dominio
- Establecer reglas de validación

**Fase 2 (Península)**:
- Pipeline automatizado para nuevas fuentes
- Búsqueda semántica para usuarios
- Escalado multiidioma

**Arquitectura combinada:**
```
Datos → Pipeline Península → Neo4j → Validation → Ontología UB → RDF Store
                                  ↓
                            Semantic Search UI
```

**Beneficios:**
- Precisión semántica + automatización
- Estándares formales + flexibilidad  
- Control académico + usabilidad


Estimated Precision Rates by Component:
🎯 Overall System Precision: 75-85%
📊 Breakdown by Processing Stage:
Stage	Claimed	Realistic Estimate	Factors Affecting Accuracy
Entity Extraction	99%	80-90%	Historical names, OCR errors, ambiguous references
Relationship Detection	99%	70-80%	Complex historical relationships, implicit connections
Cross-source Linking	99%	65-75%	Name variations, temporal inconsistencies
Semantic Coherence	99%	75-85%	Domain-specific terminology, multilingual content
🔍 Key Factors Reducing Precision:
Domain-Specific Challenges:
Historical data complexity: Multiple name variants, uncertain dates
Multilingual content: Catalan, Spanish, potentially Latin terms
Cultural context: Requires deep historical knowledge
OCR artifacts: Digitized documents with scanning errors
Technical Limitations:
Multi-step pipeline: Errors compound across 5 processing phases
LLM hallucinations: Google Gemini can generate plausible but incorrect connections
Chunk processing: Context loss when splitting large documents
Cross-format inconsistencies: RDF, CSV, SQL data integration challenges
📈 Realistic Performance by Data Type:
Apply to Comparación ...
)
🎯 Validation Evidence:
The system includes validation with 0.85 threshold, which actually suggests they expect 15% uncertainty in their quality metrics - contradicting the 99% claim.
threshold
🏆 

---

*HerStory Project - Técnica de Investigación*  
*Versión 1.0 - Enero 2025* 