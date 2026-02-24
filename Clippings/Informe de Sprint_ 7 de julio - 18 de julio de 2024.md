---
title: Informe de Sprint 7 de julio - 18 de julio de 2024
year:
type: article
base: clippings
source: pdf
tags:
  - op/projects/peninsula
---

Linked PDF file(s) for **Informe de Sprint 7 de julio - 18 de julio de 2024**:

- [[PDF/Peninsula/Informe de Sprint_ 7 de julio - 18 de julio de 2024.pdf]]
- [[PDF/Peninsula/Informe de Sprint_ 7 de julio - 18 de julio de 2024.sync-conflict-20251201-093143-LONMVRE.pdf]]

## PDF text extraction

Tarea  Épica  
Título  Épico:  Implementación  y  Estandarización  del  Knowledge  Graph  bajo  Protocolo  
Wikidata
 
Descripción:  
El
 
objetivo
 
de
 
esta
 
épica
 
es
 
evolucionar
 
nuestro
 
sistema
 
de
 
datos
 
para
 
que
 
sea
 
completamente
 
compatible
 
con
 
los
 
estándares
 
y
 
protocolos
 
de
 
Wikidata.
 
Esto
 
implica
 
mapear
 
nuestras
 
entidades
 
(nodos)
 
y
 
sus
 
interconexiones
 
(relaciones),
 
asegurar
 
la
 
correcta
 
ingesta
 
de
 
datos,
 
e
 
implementar
 
un
 
endpoint
 
SPARQL
 
funcional
 
para
 
consultas
 
avanzadas.
 
La
 
épica
 
culmina
 
con
 
el
 
despliegue
 
de
 
una
 
solución
 
robusta,
 
probada
 
y
 
documentada.
 
 
Plan  de  Sprint  Detallado  (7  al  18  de  julio)  
Semana  1:  Mapeo,  Reglas  y  Configuración  del  Endpoint  
●  Tarea  1:  Definición  de  puntos  de  alcance  para  tareas  ○  Descripción:  Reunión  inicial  del  sprint  para  clarificar  los  detalles,  
dependencias
 
y
 
los
 
criterios
 
de
 
aceptación
 
de
 
cada
 
tarea.
 
El
 
objetivo
 
es
 
asegurar
 
que
 
todo
 
el
 
equipo
 
esté
 
alineado
 
y
 
no
 
haya
 
ambigüedades.
 ○  Criterios  de  Aceptación:  ■  Todos  los  miembros  del  equipo  confirman  entender  el  alcance  de  
cada
 
tarea.
 ■  Se  han  identificado  y  documentado  las  dependencias  entre  tareas.  ■  El  objetivo  del  sprint  es  claro  y  aceptado  por  el  equipo.  
 ●  Tarea  2:  Mapear  denominaciones  de  nodos  a  protocolo  Wikidata  ○  Descripción:  Analizar  las  entidades  actuales  ("nodos")  de  nuestro  modelo  de  
datos
 
y
 
establecer
 
su
 
correspondencia
 
directa
 
con
 
las
 
entidades
 
(items,
 
Q-numbers)
 
del
 
protocolo
 
Wikidata.
 ○  Criterios  de  Aceptación:  ■  Existe  un  documento  o  tabla  de  mapeo  (ej.  en  Confluence,  un  CSV)  
que
 
relaciona
 
cada
 
nodo
 
de
 
nuestro
 
sistema
 
con
 
su
 
correspondiente
 
Q-number
 
de
 
Wikidata.
 ■  El  100%  de  los  nodos  definidos  en  el  alcance  están  mapeados.  ■  El  mapeo  ha  sido  revisado  y  aprobado  por  el  líder  técnico  o  Product  
Owner.
 
 ●  Tarea  3:  Mapear  denominaciones  de  relaciones  a  protocolo  Wikidata  ○  Descripción:  Analizar  las  conexiones  y  vínculos  entre  nuestros  nodos  y  
mapearlos
 
a
 
las
 
propiedades
 
(P-numbers)
 
de
 
Wikidata
 
que
 
mejor
 
representen
 
dicha
 
relación.
 ○  Criterios  de  Aceptación:  

■  Existe  un  documento  o  tabla  de  mapeo  que  relaciona  cada  tipo  de  
relación
 
de
 
nuestro
 
sistema
 
con
 
su
 
correspondiente
 
P-number
 
de
 
Wikidata.
 ■  El  100%  de  las  relaciones  definidas  en  el  alcance  están  mapeadas.  ■  El  mapeo  ha  sido  validado  para  asegurar  la  coherencia  semántica.  
 ●  Tarea  4:  Restricciones  y  aplicaciones  para  reglas  según  documento  de  Miquet  ○  Descripción:  Implementar  en  el  código  la  lógica  de  negocio,  validaciones  de  
datos
 
y
 
restricciones
 
especificadas
 
en
 
el
 
"documento
 
de
 
Miquet".
 
Estas
 
reglas
 
operarán
 
sobre
 
la
 
estructura
 
ya
 
estandarizada
 
con
 
el
 
protocolo
 
Wikidata.
 ○  Criterios  de  Aceptación:  ■  El  código  que  implementa  las  reglas  está  subido  al  repositorio.  ■  Existen  pruebas  unitarias  que  validan  el  comportamiento  de  cada  
regla
 
(casos
 
de
 
éxito
 
y
 
de
 
fallo).
 ■  Una  revisión  de  código  confirma  que  las  reglas  implementadas  se  
corresponden
 
con
 
lo
 
especificado
 
en
 
el
 
documento
 
de
 
Miquet.
 
 ●  Tarea  5:  Exposición  de  endpoint  preparado  para  consultas  de  SPARQL  ○  Descripción:  Configurar  y  desplegar  el  servicio  (endpoint)  que  permitirá  
realizar
 
consultas
 
al
 
grafo
 
de
 
conocimiento
 
utilizando
 
el
 
lenguaje
 
estándar
 
SPARQL.
 
En
 
esta
 
fase,
 
el
 
endpoint
 
debe
 
estar
 
operativo
 
y
 
accesible
 
para
 
el
 
equipo
 
en
 
el
 
entorno
 
de
 
pruebas.
 ○  Criterios  de  Aceptación:  ■  El  endpoint  tiene  una  URL  accesible  desde  el  entorno  de  
desarrollo/staging.
 ■  El  endpoint  responde  con  un  código  200  a  una  consulta  SPARQL  
válida
 
y
 
simple
 
(ej.
 
un
 
SELECT
 
?s
 
?p
 
?o
 
LIMIT
 
10).
 ■  El  endpoint  responde  con  un  código  de  error  (ej.  400)  a  una  consulta  
SPARQL
 
con
 
sintaxis
 
incorrecta.
 
 
Semana  2:  Pruebas,  Despliegue  y  Cierre  
●  Tarea  6:  Testing  de  la  ingesta  de  SQL  ○  Descripción:  Realizar  un  conjunto  de  pruebas  para  verificar  que  el  proceso  
de
 
importación/transformación
 
de
 
datos
 
desde
 
las
 
bases
 
de
 
datos
 
SQL
 
al
 
nuevo
 
formato
 
del
 
grafo
 
(alineado
 
con
 
Wikidata)
 
funciona
 
correctamente,
 
sin
 
pérdida
 
de
 
datos
 
y
 
aplicando
 
el
 
mapeo
 
correctamente.
 ○  Criterios  de  Aceptación:  ■  Se  ha  ejecutado  un  plan  de  pruebas  que  compara  datos  de  origen  
(SQL)
 
con
 
los
 
datos
 
resultantes
 
en
 
el
 
grafo.
 ■  Se  verifica  que  no  hay  pérdida  de  datos  para  un  conjunto  de  registros  
de
 
muestra.
 ■  Los  datos  en  el  grafo  utilizan  correctamente  los  mapeos  de  nodos  y  
relaciones
 
definidos
 
previamente.
 
 

●  Tarea  7:  Testing  del  endpoint  SPARQL  ○  Descripción:  Ejecutar  un  plan  de  pruebas  exhaustivo  sobre  el  endpoint  
SPARQL
 
para
 
validar
 
su
 
funcionalidad,
 
corrección
 
de
 
los
 
datos
 
devueltos
 
y
 
rendimiento.
 ○  Criterios  de  Aceptación:  ■  Se  ejecutan  consultas  SPARQL  complejas  que  devuelven  los  
resultados
 
esperados
 
según
 
los
 
datos
 
de
 
prueba.
 ■  Las  consultas  sobre  datos  inexistentes  devuelven  un  resultado  vacío  
y
 
no
 
un
 
error.
 ■  El  tiempo  de  respuesta  para  consultas  de  referencia  se  encuentra  
dentro
 
de
 
un
 
umbral
 
aceptable
 
(ej.
 
<
 
2
 
segundos).
 
 ●  Tarea  8:  Redeploy  ○  Descripción:  Desplegar  la  versión  final,  estable  e  integrada  de  la  aplicación  
en
 
el
 
entorno
 
de
 
destino
 
(ej.
 
Staging
 
o
 
Producción),
 
incluyendo
 
todas
 
las
 
nuevas
 
funcionalidades
 
y
 
correcciones
 
del
 
sprint.
 ○  Criterios  de  Aceptación:  ■  El  pipeline  de  despliegue  se  ha  ejecutado  sin  errores.  ■  La  nueva  versión  de  la  aplicación  está  activa  en  el  entorno  de  destino.  ■  Se  realiza  una  comprobación  básica  (smoke  test)  post-despliegue  
para
 
confirmar
 
que
 
el
 
servicio
 
está
 
operativo.
 
 
Cierre
 
del
 
Sprint
 
(Viernes
 
18
 
de
 
julio)
 
●  Tarea  9:  Demo  y  Revisión  del  Sprint  ○  Descripción:  Presentar  a  los  stakeholders  y  al  Product  Owner  los  
incrementos
 
de
 
producto
 
funcionales
 
y
 
completados
 
durante
 
el
 
sprint
 
para
 
mostrar
 
el
 
valor
 
entregado
 
y
 
recoger
 
feedback.
 ○  Criterios  de  Aceptación:  ■  La  sesión  de  demo  se  ha  realizado  con  la  asistencia  de  los  
stakeholders
 
clave.
 ■  Se  ha  mostrado  en  vivo  el  funcionamiento  del  mapeo,  las  reglas  
aplicadas
 
y
 
la
 
ejecución
 
de
 
consultas
 
en
 
el
 
endpoint
 
SPARQL.
 ■  El  feedback  de  los  stakeholders  ha  sido  recopilado  y  documentado  
para
 
futuros
 
sprints.
 
 ●  Tarea  10:  Retrospectiva  del  Sprint  ○  Descripción:  Reunión  interna  del  equipo  de  desarrollo  para  inspeccionar  el  
sprint
 
que
 
finaliza
 
(procesos,
 
herramientas,
 
comunicación)
 
y
 
crear
 
un
 
plan
 
de
 
mejoras
 
para
 
el
 
siguiente.
 ○  Criterios  de  Aceptación:  ■  La  sesión  de  retrospectiva  se  ha  realizado  con  la  participación  de  todo  
el
 
equipo.
 ■  Se  han  identificado  los  puntos  a  mantener  (qué  funcionó  bien)  y  los  
puntos
 
a
 
mejorar.
 ■  Se  han  definido  al  menos  1-2  acciones  de  mejora  concretas  y  
asignables
 
para
 
el
 
próximo
 
sprint.
