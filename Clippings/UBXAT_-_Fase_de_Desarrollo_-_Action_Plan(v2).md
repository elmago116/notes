---
title: UBXAT - Fase de Desarrollo - Action Plan(v2)
type: article
base: clippings
source: pdf
tags:
  - op/projects/UBXAT
  - op/projects/peninsula
---

Linked PDF file(s) for **UBXAT - Fase de Desarrollo - Action Plan(v2)**:

- [[PDF/Peninsula/UBXAT_-_Fase_de_Desarrollo_-_Action_Plan(v2).pdf]]

## PDF text extraction

UBXAT - Fase de Desarrollo
Visión General del Plan de Acción
Este documento define la estrategia de acción para la fase de desarrollo del proyecto UBXAT.
Partiendo de los avances de la fase de diseño inicial, se han identificado brechas en infraestructura,
código y aprovisionamiento que deben ser abordadas de manera sistemática para garantizar la
viabilidad, escalabilidad y seguridad del producto final, en línea con nuestra metodología P²M.
Plan de Acción por Áreas de Prioridad
A continuación, se detallan las acciones a ejecutar, organizadas por área de enfoque y priorizadas
según su impacto en el proyecto.
1. Infraestructura (Prioridad Alta)
La base de la infraestructura es crítica para asegurar un servicio estable y que pueda crecer conforme
a la demanda.
1.1 Escalabilidad y Disponibilidad
• Implementación de Cluster Neo4j: Se desplegará una configuración multi-nodo para la base de
datos Neo4j. Esto es fundamental para garantizar alta disponibilidad y distribuir la carga, evitando
puntos únicos de fallo.
• Auto-escalado de Neo4j: Se configurarán mecanismos de auto-escalado basados en métricas de
carga y uso para ajustar los recursos dinámicamente, optimizando costes y rendimiento.
• Instancia de Pre-producción CI/CD: Se establecerá un entorno de pre-producción para servicios
y bases de datos, integrado en el pipeline de Integración y Despliegue Continuo (CI/CD) para
validar cambios antes de su paso a producción.
1.2 Monitorización y Observabilidad
• Abstracción con Langfuse: Se integrará Langfuse como plataforma de observabilidad. Esto
permitirá un análisis detallado del rendimiento de los modelos de lenguaje, la depuración de
trazas y la monitorización de costes y latencia, tal como se define en nuestras herramientas
estándar.
1.3 Seguridad de Producción
• Autenticación de Usuarios: Se implementará un sistema de autenticación único basado en JWT


para los endpoints SPARQL y REST, asegurando el acceso controlado a los datos.
• Cifrado de Datos: Se aplicará el cifrado de datos tanto en reposo como en tránsito. Se evaluarán
estrategias de caché con Redis o S3 para mejorar el rendimiento sin comprometer la seguridad.
• Auditoría de Accesos: Se registrarán y auditarán todos los accesos a los servicios como parte de
la documentación de seguridad y cumplimiento.
2. Desarrollo (Prioridad Media-Alta)
Las tareas de desarrollo se enfocarán en la optimización del núcleo funcional, la calidad del código y
la robustez de las APIs.
2.1 Optimización de RAG
• Caché de Respuestas: Se implementará un sistema de caché para las respuestas de los agentes y
las trazas más frecuentes, con el fin de reducir la latencia y el coste computacional.
2.2 API y Endpoints
• Documentación con Swagger: Se utilizará Swagger para documentar y permitir pruebas
interactivas de los endpoints REST y SPARQL, facilitando la integración por parte de terceros.
• Integración SPARQL: Se completará y mantendrá actualizada toda la documentación relativa a la
integración y uso del endpoint SPARQL.
2.3 Estrategias de Carga
• Plan de Carga de Datos: Se definirán e implementarán las estrategias para la carga inicial y
continua de datos, estableciendo métricas para monitorizar el volumen y el uso.
2.4 Testing y Calidad
• Tests de Carga: Se realizarán pruebas de carga exhaustivas para validar el rendimiento de la
plataforma bajo diferentes escenarios de demanda.
• Cobertura de Código: Se establecerá un objetivo mínimo del 80% de cobertura de código en las
pruebas unitarias y de integración, con especial atención a los refactors y procesos con alta
complejidad algorítmica (Big O).


3. Aprovisionamiento (Prioridad Media)
Se automatizará la creación y gestión de entornos para garantizar consistencia y agilidad en los
despliegues.
3.1 Entornos Completos
• Infrastructure as Code (IaC): Se utilizará Terraform para definir la infraestructura como código,
permitiendo la replicación exacta y automatizada de los entornos de pre-producción y
producción.
• Gestión de Secretos: Se empleará una solución como Vault para la gestión segura de
credenciales, claves de API y otra información sensible.
3.2 Configuración y Despliegue
• Rollback Automático: Los pipelines de despliegue incluirán mecanismos de rollback automático
que se activarán en caso de fallo, minimizando el tiempo de inactividad.
• Pipelines de Seguridad: Se integrarán herramientas de análisis de seguridad y observabilidad
dentro de los pipelines de CI/CD.
3.3 Documentación del Sistema General
• Documentación Funcional: Se elaborará una documentación completa que incluya casos de uso,
ejemplos de consulta, descripciones de la arquitectura y definiciones de entidades.
• Cuotas de Recursos: Se definirán las cuotas y límites de recursos para eventuales planes de uso
por parte de terceros.
Ciclo de Desarrollo Propuesto
El desarrollo se organizará en Sprints iterativos, un principio clave de la metodología P²M para
entregar valor de forma temprana y frecuente. Cada Sprint se enfocará en un conjunto específico de
objetivos.
Sprint 1: Foundation (Seguridad y Estabilidad)
• Implementación de autenticación y autorización básica.
• Configuración del sistema de logging y monitoreo inicial.
• Establecimiento de rutinas de tests y copias de seguridad.
• Elaboración de la documentación inicial del sistema.


Sprint 2: Scale (Rendimiento y Escalabilidad)
• Desarrollo de los procesos de ingesta de datos.
• Aplicación de optimizaciones en la base de datos.
• Implementación de estrategias de caching y mejoras de rendimiento.
• Configuración de métricas avanzadas de monitorización.
Sprint 3: Polish (Experiencia de Usuario)
• Refinamiento de las funcionalidades de consulta para el usuario final.
• Incorporación de feedback para realizar ajustes finales.
• Pulido general de la interfaz y la experiencia de usuario.
Gestión de Riesgos
Se ha realizado una identificación inicial de riesgos técnicos que serán mitigados y monitorizados de
forma continua a lo largo del proyecto.
• Rendimiento en la Carga de Datos: La organización y el volumen de la carga de datos pueden
afectar negativamente al rendimiento. Se mitigará con un diseño de ingesta optimizado y
pruebas de carga.
• Limitaciones de la API de Google Gen AI: Las versiones beta de la librería de Python (0.5/0.6)
pueden presentar limitaciones o inestabilidad. Se gestionará mediante la encapsulación del
código y la planificación de posibles refactors.
• Calidad de los Datos: El mantenimiento de una alta calidad en los datos de origen es crítico para
la precisión del sistema. Se establecerán procesos de validación y limpieza.
• Escalabilidad de Costes: Un uso intensivo de la plataforma podría derivar en un incremento
significativo de los costes. Se mitigará mediante la optimización de consultas, el uso de caché y la
monitorización constante con Langfuse.
Análisis de Costes de Infraestructura (Neo4j)
Para asegurar la justificación continua del negocio, se ha realizado un análisis de los planes de servicio
de Neo4j AuraDB, la base de datos gráfica gestionada que se utilizará como núcleo del sistema.


Comparativa de Tiers de AuraDB
Característica AuraDB
Free AuraDB Professional AuraDB Business Critical
Costo $0 Desde $65/GB/mes
(mínimo 1GB) Desde $146/GB/mes (mínimo 2GB)
Nodos Hasta
200,000 Sin límite explícito Sin límite explícito
Relaciones Hasta
400,000 Sin límite explícito Sin límite explícito
Memoria
(RAM) Fija Desde 1GB hasta 128GB Desde 2GB hasta 512GB
Disponibilidad Zona única,
sin SLA
Clúster de 3 zonas con
conmutación por error
automática
Clúster de 3 zonas de alta disponibilidad con
SLA del 99.95%
Copias de
Seguridad
Snapshot
único
exportable
Copias de seguridad
diarias con retención de
7 días
Copias de seguridad diarias con retención de
30 días y restauración a un punto en el tiempo
(PITR) por hora
Soporte
Basado en
la
comunidad
Soporte estándar Soporte 24/7
Seguridad
Cifrado en
tránsito y
en reposo
Control de acceso
basado en roles Seguridad granular a nivel de esquema
Tarifas Detalladas: AuraDB Professional (Recomendado)
Memoria CPU Espacio Coste por Hora Coste Mensual Estimado
1GB 1 CPU 2GB $0.09/hora $65.70/mes
2GB 1 CPU 4GB $0.18/hora $131.40/mes
4GB 1 CPU 8GB $0.36/hora $262.80/mes
8GB 2 CPU 16GB $0.72/hora $525.60/mes


Memoria CPU Espacio Coste por Hora Coste Mensual Estimado
16GB 3 CPU 32GB $1.44/hora $1,051.20/mes
24GB 5 CPU 48GB $2.16/hora $1,576.80/mes
32GB 6 CPU 64GB $2.88/hora $2,102.40/mes
48GB 10 CPU 96GB $4.32/hora $3,153.60/mes
64GB 12 CPU 128GB $5.76/hora $4,204.80/mes
Para que la instancia de producción esté acorde con la carga y el volumen de datos previstos, es
necesario contar con el tier AuraDB Professional, que no plantea límites de nodos ni relaciones. Se
recomienda una instancia inicial con 2GB de Memoria RAM y 4GB de espacio para una carga
mediana de demanda, con la posibilidad de escalar a un tier superior para asegurar la capacidad de
ingesta de las tres bases de datos planificadas. Las copias de seguridad diarias que ofrece este plan
son un activo valioso para abordar las tareas de estabilidad y mantenimiento del sistema.
