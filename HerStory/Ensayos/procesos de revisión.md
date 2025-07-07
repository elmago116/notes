# Procesos de Revisión - Inventario de Transformaciones

## Objetivo
Este documento establece los procesos sistemáticos para revisar y detectar inexactitudes o errores en el inventario de reglas de transformación de base de datos a ontología OWL.

## 1. Revisión de Consistencia Estructural

### 1.1 Verificación de Reglas de Transformación
- [ ] **Consistencia de aplicación de reglas**: Verificar que todas las tablas catalogadas como "no asociativas" apliquen efectivamente la Regla 1
- [ ] **Consistencia de tablas asociativas**: Confirmar que todas las tablas con solo claves foráneas apliquen la Regla 2
- [ ] **Coherencia en nomenclatura**: Revisar que los nombres de clases y propiedades sigan convenciones consistentes

### 1.2 Validación de Mapeo Tabla-Clase
- [ ] Verificar que cada tabla tenga una correspondencia clara en la sección de clases
- [ ] Confirmar que todas las clases listadas en "Tabla 1: Clases" tengan origen en las reglas generales
- [ ] Revisar que no existan clases huérfanas o tablas sin transformar

## 2. Revisión de Sintaxis Turtle (TTL)

### 2.1 Validación Sintáctica
- [ ] **Prefijos y espacios de nombres**: Verificar que todos los ejemplos usen prefijos consistentes
- [ ] **Terminación de sentencias**: Confirmar que todas las expresiones TTL terminen correctamente con punto (.)
- [ ] **Uso de palabras clave OWL**: Validar `owl:Class`, `owl:DatatypeProperty`, `owl:ObjectProperty`, `rdfs:domain`, `rdfs:range`

### 2.2 Revisión de Tipos de Datos
- [ ] Verificar que los rangos de datos sean apropiados (`xsd:string`, `xsd:date`)
- [ ] Confirmar coherencia en el uso de tipos de datos para propiedades similares
- [ ] Revisar que las fechas usen `xsd:date` y los textos `xsd:string`

## 3. Revisión de Relaciones y Propiedades

### 3.1 Validación de Propiedades Inversas
- [ ] **Completitud de pares inversos**: Verificar que cada `owl:ObjectProperty` tenga su propiedad inversa correspondiente
- [ ] **Coherencia de dominios y rangos**: Confirmar que el dominio de una propiedad sea el rango de su inversa
- [ ] **Nomenclatura de inversas**: Revisar que los nombres de propiedades inversas sean semánticamente correctos

### 3.2 Verificación de Dominios y Rangos
- [ ] Confirmar que todos los dominios y rangos referencien clases existentes
- [ ] Verificar que las relaciones many-to-many se modelen correctamente
- [ ] Revisar que no existan referencias circulares problemáticas

## 4. Revisión de Completitud

### 4.1 Cobertura de Transformación
- [ ] **Tablas faltantes**: Identificar si existen tablas mencionadas pero no transformadas
- [ ] **Atributos omitidos**: Verificar que todos los atributos significativos estén incluidos
- [ ] **Relaciones implícitas**: Buscar relaciones que puedan haberse pasado por alto

### 4.2 Consistencia de Inventario
- [ ] Confirmar que todas las clases en "Tabla 1" tengan propiedades correspondientes en "Tabla 2"
- [ ] Verificar que todas las relaciones tengan sus inversas listadas
- [ ] Revisar que las inferencias sean completas y correctas

## 5. Revisión Lógica y Semántica

### 5.1 Validación de Inferencias
- [ ] **Correctitud lógica**: Verificar que las inferencias listadas sean lógicamente válidas
- [ ] **Completitud de inferencias**: Identificar inferencias obvias que puedan faltar
- [ ] **Propiedades funcionales**: Revisar si alguna propiedad debería ser declarada como funcional

### 5.2 Coherencia Semántica
- [ ] Verificar que los nombres de clases y propiedades reflejen correctamente su propósito
- [ ] Confirmar que las relaciones entre entidades sean semánticamente correctas
- [ ] Revisar que no existan ambigüedades en las definiciones

## 6. Validación Técnica

### 6.1 Conformidad con Estándares OWL
- [ ] Verificar que la sintaxis cumpla con OWL 2 DL
- [ ] Confirmar que no existan construcciones que puedan causar inconsistencias
- [ ] Revisar que las declaraciones de clases e propiedades sean completas

### 6.2 Testeo de Consistencia
- [ ] **Validación con reasoner**: Usar un reasoner OWL para detectar inconsistencias
- [ ] **Verificación de instancias de ejemplo**: Crear instancias de prueba para validar el modelo
- [ ] **Detección de clases vacías**: Identificar si alguna clase nunca podría tener instancias

## 7. Lista de Verificación Específica

### Errores Comunes a Buscar:
- [ ] **Duplicación de propiedades**: Misma propiedad definida múltiples veces con diferentes dominios/rangos
- [ ] **Referencias inconsistentes**: Nombres de clases que varían entre secciones
- [ ] **Falta de simetría**: Relaciones que deberían ser simétricas pero no están modeladas como tal
- [ ] **Cardinalidades implícitas**: Relaciones que necesitan restricciones de cardinalidad
- [ ] **Jerarquías faltantes**: Posibles relaciones de herencia entre clases no identificadas

## 8. Proceso de Documentación de Errores

### 8.1 Registro de Hallazgos
Para cada error encontrado, documentar:
- **Ubicación**: Tabla/sección específica donde se encuentra el error
- **Tipo de error**: Sintáctico, semántico, lógico, de completitud
- **Descripción**: Explicación clara del problema
- **Propuesta de corrección**: Solución sugerida
- **Prioridad**: Alta, Media, Baja

### 8.2 Seguimiento de Correcciones
- [ ] Crear tabla de seguimiento de errores identificados
- [ ] Establecer responsable de cada corrección
- [ ] Definir cronograma de implementación de correcciones
- [ ] Planificar re-revisión post-corrección

## 9. Herramientas Recomendadas

### 9.1 Validadores Sintácticos
- **Protégé**: Para validación visual y detección de inconsistencias
- **Apache Jena**: Para validación programática de sintaxis TTL
- **TopBraid Composer**: Para modelado y validación avanzada

### 9.2 Reasoners
- **HermiT**: Para detección de inconsistencias lógicas
- **Pellet**: Para inferencias y validación de completitud
- **FaCT++**: Para verificación de satisfacibilidad

## 10. Errores Comunes en Transformaciones DB→OWL

### 10.1 Errores Específicos de Automatización con IA

#### Patrones de Error de IA:
- [ ] **Sobre-generalización de patrones**: La IA aplica reglas demasiado generales sin considerar contexto específico
- [ ] **Interpretación literal sin semántica**: Traduce nombres y estructuras sin entender el significado del dominio
- [ ] **Creación de propiedades redundantes**: Genera múltiples propiedades para la misma relación semántica
- [ ] **Inconsistencia en convenciones de nombres**: Mezcla diferentes estilos de nomenclatura (camelCase, snake_case, etc.)
- [ ] **Pérdida de restricciones implícitas**: No captura restricciones de negocio que están implícitas en la DB
- [ ] **Mapeo incorrecto de tipos NULL**: Manejo inadecuado de valores opcionales vs obligatorios
- [ ] **Sobre-especificación de jerarquías**: Crea jerarquías de clases innecesariamente complejas
- [ ] **Ignorar metadatos de DB**: No utiliza comentarios, restricciones CHECK, o triggers existentes

#### Validaciones Anti-IA:
- [ ] **Verificar coherencia semántica**: Confirmar que los nombres generados tengan sentido en el dominio
- [ ] **Revisar cardinalidades inferidas**: Validar que las restricciones de cardinalidad sean correctas
- [ ] **Evaluar necesidad de cada propiedad**: Eliminar propiedades duplicadas o innecesarias
- [ ] **Verificar interpretación de relaciones**: Confirmar que las FK se interpreten semánticamente

### 10.2 Errores Generales en Transformaciones DB→OWL

#### Errores Estructurales:
- [ ] **Tabla = Clase (siempre)**: Asumir que toda tabla debe ser una clase OWL
- [ ] **Ignorar tablas de lookup**: No reconocer tablas de valores controlados como individuos
- [ ] **Mal manejo de herencia**: No identificar relaciones IS-A implícitas en la estructura
- [ ] **Confundir atributos con relaciones**: Tratar FK como DatatypeProperty en lugar de ObjectProperty
- [ ] **Pérdida de restricciones de integridad**: No traducir constraints de DB a restricciones OWL

#### Errores de Modelado:
- [ ] **Relaciones Many-to-Many mal modeladas**: Crear clases intermedias innecesarias
- [ ] **Propiedades inversas faltantes**: No definir owl:inverseOf para relaciones bidireccionales
- [ ] **Rangos y dominios incorrectos**: Especificar tipos de datos inapropiados
- [ ] **Mixing schema con instancias**: Incluir datos específicos en la definición ontológica
- [ ] **Cardinalidades mal especificadas**: Usar Functional/InverseFunctional incorrectamente

#### Errores Técnicos:
- [ ] **Sintaxis TTL incorrecta**: Errores de puntuación, prefijos, o terminación de sentencias
- [ ] **Espacios de nombres inconsistentes**: Mezclar diferentes URIs base sin justificación
- [ ] **Tipos de datos XSD incorrectos**: Usar xsd:string para fechas, números, etc.
- [ ] **Annotations mal formadas**: rdfs:label, rdfs:comment con sintaxis incorrecta
- [ ] **Importación de ontologías faltante**: No declarar dependencias necesarias

### 10.3 Errores Semánticos Críticos

#### Pérdida de Semántica de Dominio:
- [ ] **Nombres sin significado**: Usar IDs técnicos en lugar de nombres descriptivos
- [ ] **Relaciones ambiguas**: Propiedades que no expresan claramente la relación semántica
- [ ] **Contexto temporal perdido**: No capturar aspectos temporales de las relaciones
- [ ] **Jerarquías planas**: No identificar taxonomías naturales del dominio
- [ ] **Polisemia no resuelta**: Mismo nombre para conceptos diferentes

#### Problemas de Expresividad:
- [ ] **Sub-especificación**: Modelo demasiado general, pierde restricciones importantes
- [ ] **Sobre-especificación**: Modelo demasiado restrictivo, no permite casos válidos
- [ ] **Inconsistencias lógicas**: Restricciones contradictorias que causan unsatisfiability
- [ ] **Propiedades no transitivas**: No identificar relaciones que deberían ser transitivas
- [ ] **Equivalencias perdidas**: No identificar clases o propiedades equivalentes

### 10.4 Lista de Verificación Anti-Errores

#### Para Detectar Errores de IA:
- [ ] ¿Los nombres de clases/propiedades son semánticamente coherentes?
- [ ] ¿Existen propiedades duplicadas con nombres diferentes?
- [ ] ¿Las cardinalidades reflejan las reglas de negocio reales?
- [ ] ¿Se han preservado todas las restricciones de integridad importantes?
- [ ] ¿La jerarquía de clases es necesaria y correcta?

#### Para Detectar Errores Generales:
- [ ] ¿Cada relación many-to-many está correctamente modelada?
- [ ] ¿Todas las ObjectProperties tienen sus inversas definidas?
- [ ] ¿Los tipos de datos XSD son apropiados para cada DatatypeProperty?
- [ ] ¿Las restricciones de cardinalidad son correctas y completas?
- [ ] ¿Se han identificado todas las posibles equivalencias entre clases?

#### Para Detectar Errores Semánticos:
- [ ] ¿El modelo captura correctamente el conocimiento del dominio?
- [ ] ¿Las relaciones expresan claramente su significado semántico?
- [ ] ¿Se han preservado aspectos temporales y contextuales importantes?
- [ ] ¿Existen ambigüedades que puedan causar malinterpretaciones?
- [ ] ¿El modelo es suficientemente expresivo para el propósito previsto?

## 11. Cronograma Sugerido

1. **Semana 1**: Revisión estructural y sintáctica (Secciones 1-2)
2. **Semana 2**: Validación de relaciones y completitud (Secciones 3-4)
3. **Semana 3**: Revisión lógica y técnica (Secciones 5-6)
4. **Semana 4**: Detección de errores comunes y correcciones finales (Sección 10)

---

**Nota**: Este proceso debe ejecutarse de manera iterativa, ya que las correcciones en una sección pueden revelar problemas en otras áreas del inventario. La sección de errores comunes debe aplicarse transversalmente durante toda la revisión. 