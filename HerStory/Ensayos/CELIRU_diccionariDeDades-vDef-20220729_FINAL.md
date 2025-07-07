# Diccionari de dades

Versió: 2023/12/04

Contenido  
[Entidad *Editor*	2](#[nova]-entidad-autoría)

[Entidad *Expediente de censura*	4](#entidad-expediente-de-censura)

[Entidad *Formulario 0*	13](#entidad-formulario-0)

[Entidad *Formulario 1*	14](#entidad-formulario-1)

[Entidad *Formulario 2*	16](#entidad-formulario-2)

[Entidad *Formulario 3*	18](#entidad-formulario-3)

[Entidad *Importación*	22](#entidad-formulario-3)

[Entidad *Importador*	23](#entidad-importador)

[Entidad *Informe de Lector*	25](#entidad-informe-de-lector)

[Entidad *Lector*	30](#entidad-lector)

[Entidad *Libro analizado*	33](#entidad-libro-presentado-a-censura)

[Entidad *Libro publicado*	36](#entidad-libro-publicado)

[Entidad *Proveedor de papel*	51](#entidad-proveedor-de-papel)

[Entidad *Solicitud de publicación*	53](#entidad-solicitud-de-publicación)

# \[NOVA\] Entidad *Autoría* {#[nova]-entidad-autoría}

**Nombre y apellido**

**Género:** \[Taxonomía: Maculino o Femenino\]

# Entidad *Editor*

| nombre\_del\_atributo                                                                        | ID\_Editor                                                                                                                                                   |
| :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Etiqueta**                                                                                 | Identificador del editor                                                                                                                                     |
| **Etiqueta en la base de datos**                                                             | Identificador del editor                                                                                                                                     |
| **Tipo de campo en base de datos**                                                           | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen**                                                           | Local                                                                                                                                                        |
| **Definición**                                                                               | Clave principal de cada registro de la entidad Editor                                                                                                        |
| **Tratamiento documental**                                                                   | Se asigna un único valor a cada registro de forma automática.                                                                                                |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón.                                                          |
| **Obligatoriedad**                                                                           | Sí                                                                                                                                                           |
| **Repetibilidad**                                                                            | No                                                                                                                                                           |
| **Indexación**                                                                               | Sí                                                                                                                                                           |
| **Ejemplos**                                                                                 |                                                                                                                                                              |
| **Comentarios**                                                                              |                                                                                                                                                              |
| **posible name property desde los diagramas**                                                | Nombre_del_editor                                                                                                                                            |
| **Equivalencias con otros esquemas**                                                         |                                                                                                                                                              |

| nombre\_del\_atributo | Nombre (M8145) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_NOMBRE\>  |
| **Etiqueta en la base de datos** | Nombre del editor Nombre del editor (estado) |
| **Tipo de campo en base de datos** | Nombre del editor: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_nombre_editor/storage) field\_nombre\_editor Nombre del editor (estado): Taxonomía  field\_nombre\_editor\_status |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Persona física o jurídica que edita libros.  |
| **Tratamiento documental** | Control de autoridades de lectores, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. Tipo de campo en Drupal: Texto(sin formato) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe consignarse la forma más completa del nombre, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de editor son las solicitudes de publicación. **TODO SGBD:** La información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte) |
| **Obligatoriedad** | SÍ. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_editor |
| **Equivalencias con otros esquemas** | EAC: nameEntry ISAAR(CPF) 5.1.2. Formas autorizadas del nombre ISAAR(CPF) 5.1.3. Formas paralelas del nombre ISAAR(CPF) 5.1.4. Formas autorizadas del nombre según otras reglas ISAAR(CPF) 5.1.5. Otras formas del nombre ISDIAH 5.1.2. Formas autorizadas del nombre  ISDIAH 5.1.3. Formas paralelas del nombre ISDIAH 5.1.4. Otras formas del nombre |

| nombre\_del\_atributo | genero\_editor |
| :---- | :---- |
| **Etiqueta** | Género |
| **Etiqueta en la base de datos** | Género |
| **Tipo de campo en base de datos** | [Taxonomía](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Identificación del género si el editor es una persona física.  |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Uno dos valores a elegir entre los siguientes: Desconocido Hombre Mujer No binario Persona jurídica Desconocido, Hombre, Mujer y No binario se asignan si el editor es una persona física. De lo contrario, se asigna directamente el valor “Persona jurídica”. |
| **Obligatoriedad** | Sí. En caso que sea imposible identificarlo a partir de la documentación disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_editor |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | owl:sameAs |
| :---- | :---- |
| **Etiqueta** | sameAs |
| **Etiqueta en la base de datos** | Información sobre el editor en otras bases de datos |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_owl_sameas/storage) |
| **Esquema de metadatos de origen** | The OWL 2 Schema vocabulary (OWL 2\) https://www.w3.org/TR/2004/REC-owl-ref-20040210/ |
| **Definición** | Código de identificación asignado a la entidad por otro sistema de información.   La propiedad de OWL owl:sameAs vincula a un individuo con otro individuo. Tal declaración owl:sameAs indica que dos referencias URI en realidad se refieren a lo mismo: los individuos tienen la misma "identidad". |
| **Tratamiento documental** | URI de las instancias que son considerades idénticas. Los conjuntos de datos donde se intentaran localitzar los URI de recursos idénticos son: AGA, BNE, Dbpedia y Wikidata.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **SGBD**: Establecimiento del mecanismo de reconciliación con los conjuntos de datos externos. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISAAR(CPF) 5.1.6. Identificadores para instituciones  *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* [https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/](https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos_3978/): \<AGE\_IDCOMP\> |

\[Entre Expediente de censura y Libro publicado\] Da como resultado 

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Libro publicado y Expediente de censura\] Resulta del expediente de censura

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Da como resultado”.


\[Entre Expediente de censura y Libro presentado a censura\] Tiene como objeto de censura

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation\_2  
* És obligatori

\[Entre Libro presentado a censura y Expediente de censura\] Se presenta en el expediente de censura

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Tiene como objeto de censura”


\[Entre Expediente de censura e Informe del lector\] Contiene el informe del lector

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_n\_relation  
* És obligatori

\[Entre Informe del lector y Expediente de censura\] Forma parte del expediente de censura

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Contiene el informe del lector”.


\[Entre Expediente de censura y Solicitud de importación\] Contiene la solicitud de importación

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation\_3  
* No és obligatori

\[Entre Solicitud de importación y Expediente de censura\] Forma parte del expediente de censura

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Contiene la solicitud de importación”.


\[Entre Expediente de censura y Solicitud de publicación\] Contiene la solicitud de publicación

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation\_4  
* No és obligatori

\[Entre Solicitud de publicación y Expediente de censura\] Forma parte del expediente de censura

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Contiene la solicitud de publicación”.

**Eliminado:**

| nombre\_del\_atributo | Identificador (M7693) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_ID\>  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Código que representa al editor de forma única y permanente dentro del entorno concreto de información archivística |
| **Tratamiento documental** | El identificador se genera en forma de Uniform Resource Identifier (URI). **TODO SGBD**: Determinará el patrón de los URI del proyecto.  Tipo de campo en Drupal: [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_age_id/storage) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | EL URI se genera automáticamente a partir del patrón establecido para el proyecto. |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISDIAH 5.1.1. Identificador ISAAR(CPF) 5.1.6. Identificadores para instituciones |

# Entidad *Expediente de censura* {#entidad-expediente-de-censura}

He incorporat dos nous valors en la taxonomía del camp Resolución: ***Autorizado con carácter de tolerado***, ***Autorizado con condiciones*** i ***Autorizado en edición de lujo***

| nombre\_del\_atributo | ID Expediente |
| :---- | :---- |
| **Etiqueta** | Identificador del expediente |
| **Etiqueta en la base de datos** | Identificador del expediente de censura |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Expediente de censura |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. Texto (sin formato) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | ID_Expediente |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ead3:unitid |
| :---- | :---- |
| **Etiqueta** | ID of the Unit |
| **Etiqueta en la base de datos** | Identificador del expediente en AGA Identificador del expediente en AGA (estado) |
| **Tipo de campo en base de datos** | Identificador del expediente en AGA [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) Identificador del expediente en AGA (estado) Taxonomía  |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Proporciona un identificador únic del recurs descrit. |
| **Tratamiento documental** | Procede de AGA |
| **Instrucciones para la entrada de datos (otras que las dadas en Tratamiento documental)** |  |
| **Obligatoriedad** | SI. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | ES.28005.AGA/6.5.1.1.1.25.7.1//AGA,21,05780,0006 (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-unitid |
| **posible name property desde los diagramas** | Identificador_AHA_ead_unitid |
| **Equivalencias con otros esquemas** | ISAD(G) 3.1.1 MODS \<identifier\> NEDA-MC  \<DOC\_ID\> NEDA-MC  \<DOC\_IDCOMP\> NEDA-MC  \<REG\_ID\> |

| nombre\_del\_atributo | ead3:physloc |
| :---- | :---- |
| **Etiqueta** | Physical Location  |
| **Etiqueta en la base de datos** | Topográfico AGA Topográfico AGA (estado) |
| **Tipo de campo en base de datos** | Topográfico AGA [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) Topográfico AGA (estado) Taxonomía  |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Especifica la ubicación física de los materiales. Numeración correlativa para localizar la unidad de instalación en el depósito. |
| **Tratamiento documental** | Procede de AGA |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | SÍ. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | AGA,21,05780,0006 (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-physloc |
| **posible name property desde los diagramas** | Localizacion_fisica_ead_physloc |
| **Equivalencias con otros esquemas** | ISAD(G) 3.1.1. Código de referencia MARC 852 \<DOC\_LOCALIZ\> |

| nombre\_del\_atributo | ead3:unittitle |
| :---- | :---- |
| **Etiqueta** | Title of the Unit  |
| **Etiqueta en la base de datos** | Título del expediente |
| **Tipo de campo en base de datos** | [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_titulo_del_expediente/storage) |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Denominación o título atribuido al expediente por el proyecto. |
| **Tratamiento documental** | Patrón de título a partir de valores de otros atributos.  **TODO SGBD**: Configura el patrón, y la obtención automática de datos a partir de otros atributos. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Componentes del patrón: *Expediente de \[importación/publicación\] de \[Título del libro\] de \[Autor\] de \[Editorial\], entre \[Fechas extremas\].* |
| **Obligatoriedad** | SÍ |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | Expediente de censura de la adaptación de la obra "La dama boba", de Lope de Vega, realizada por Federico García Lorca, para ser representada en el Teatro Español (Madrid). (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-unittitle |
| **posible name property desde los diagramas** | Titulo_expedient |
| **Equivalencias con otros esquemas** | ISAD(G) 3.1.2 MARC 130, 240, 245 MODS \<titleInfo\>\<title\> \<DOC\_NOMBRE\> \<DOC\_TIPODOC\> |

| nombre\_del\_atributo | ead3:origination |
| :---- | :---- |
| **Etiqueta** | Origination |
| **Etiqueta en la base de datos** | Conservador del expediente |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_conservador_del_expediente/storage) |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Persona física o jurídica que ha conservado los documentos. |
| **Tratamiento documental** | Vocabulario controlado |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe entrarse UNO de los siguientes valores del vocabulario controlado: Archivo General de la Administración (Alcalá de Henares) **TODO Iván** |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | Dirección General de Seguridad (España) (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-origination |
| **Equivalencias con otros esquemas** | ISAD(G) 3.2.1 MARC 100, 110, 111 MODS \<name\> NO NEDA-MC |

| nombre\_del\_atributo | ead3:scopecontent |
| :---- | :---- |
| **Etiqueta** | Scope and Content  |
| **Etiqueta en la base de datos** | El expediente contiene |
| **Tipo de campo en base de datos** | [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_scopecontent/storage) |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Relación de los documentos contenidos en el expediente y, cuando está disponible, enlace con sus ficheros resultantes de la digitalización. |
| **Tratamiento documental** | Patrón de datos  **TODO SGBD**: Configuración del patrón, y del procedimiento de inserción de los ficheros resultantes de la digitalización. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | ***El expediente contiene:***  Y, a continuación, la relación ordenada de los títulos de los documentos, siguiendo el patrón: ***Número de orden*** seguido de la identificación del documento formado por: ***Tipo de documento / Autor / Detalles relevantes / (Lugar y fecha de emisión del documento) / Enlace con el documento digitalizado en versión PDF.***  Ejemplo:  ***El expediente contiene:1\. Informe de la asesoría jurídica autorizando el estreno en el Teatro Español de Madrid (Madrid, 27 de agosto de 1935\) \[fichero.pdf\].*** |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí. Los ficheros PDF son imágenes no buscables. |
| **Ejemplos** | Título formal: "Expediente de censura de "La dama boba" de Federico García Lorca (autor). Teatro Español y Chopera del Retiro".El expediente contiene:1\. Informe de la asesoría jurídica autorizando el estreno en el Teatro Español de Madrid (Madrid, 27 de agosto de 1935).2\. Mecanuscrito de la obra, con la firma de Federico García Lorca en la portada. (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-scopecontent |
| **posible name property desde los diagramas** | Expedient_conte_ead_scopecontent |
| **Equivalencias con otros esquemas** | ISAD(G) 3.3.1 MARC 520 MODS \<abstract\> \<DOC\_TIPODOC\> |

| nombre\_del\_atributo | ead3:phystech |
| :---- | :---- |
| **Etiqueta** | Physical Characteristics and Technical Requirements  |
| **Etiqueta en la base de datos** | Estado del expediente |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_estado_del_expediente/storage) |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Para describir el estado físico de los materiales y/o requisitos técnicos que afectan a su uso.  |
| **Tratamiento documental** | Vocabulario controlado |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Un valor a elegir entre los siguientes: Consultable  No consultable por deterioro No consultable por desaparición |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Estado_del_expediente_ead_phystech |
| **Equivalencias con otros esquemas** | ISAD(G) 3.4.4 MARC 340, 538  \<DOC\_CONSERV\> |

| nombre\_del\_atributo | ead3:datesinglef |
| :---- | :---- |
| **Etiqueta** | Single Date |
| **Etiqueta en la base de datos** | Fechas extremas de creación de la documentación Fechas extremas de creación de la documentación (estado) |
| **Tipo de campo en base de datos** | Fechas extremas de creación de la documentación: Intervalo de fechas Fechas extremas de creación de la documentación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | EAD 3 https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html |
| **Definición** | Fechas extremas de creación de la documentación. |
| **Tratamiento documental** | Patrón de fechas: AAAA-MM-DD-AAAA-MM-DD 1936-01-??-1938-12-?? \= 1936-01-01-1938-12-31 |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | A partir de la documentación del expediente, se determinan las fechas extremas. |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. Si todavía no se han incorporado las fechas, se introduce el valor “Pendiente”. |
| **Repetibilidad** | No |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc.  |
| **Ejemplos** | 1935 (http://pares.mcu.es/ParesBusquedas20/catalogo/description/3536579?nm) |
| **Comentarios** | https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html\#elem-unitdatestructured |
| **Equivalencias con otros esquemas** | ISAD(G) 3.1.3 MARC 245 subfield f for inclusive dates, 245 subfield g for bulk dates, or 260 subfield c MODS \<originInfo\>\<dateCreated\> |

| nombre\_del\_atributo | observaciones\_miembros\_proyecto |
| :---- | :---- |
| **Etiqueta** | Observaciones miembros proyecto |
| **Etiqueta en la base de datos** | Observaciones de los miembros del proyecto |
| **Tipo de campo en base de datos** | [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_observaciones_usuarios_pro/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Notas y comentarios dirigidos a los miembros del proyecto. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: Posibilidad de ocultarlo en la interfaz de usuarios. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Observaciones_de_los_miembros_del_proyecto |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | observaciones\_usuarios\_proyecto |
| :---- | :---- |
| **Etiqueta** | Observaciones usuarios proyecto |
| **Etiqueta en la base de datos** | Observaciones |
| **Tipo de campo en base de datos** | [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_observaciones_usuarios_pro/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Notas y comentarios dirigidos a los usuarios de la base de datos. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | La descripción puede concretar el valor “Otros” del atributo ***resolución***. Tipo de campo en Drupal: Texto(largo con formato) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Observaciones_usuarios_proyecto |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | resolucion |
| :---- | :---- |
| **Etiqueta** | Resolución |
| **Etiqueta en la base de datos** | Resolución |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_censorship_file_resolution/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Resolución definitiva de la solicitud de publicación o importación. |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Un valor a elegir entre los siguientes: Autorizado  Prohibido o suspendido Suspendido temporalmente Silencio administrativo ***Autorizado con carácter de tolerado Autorizado con condiciones Autorizado en edición de lujo*** Otros Notas de aplicación de los valores. El valor “Autorizado” puede significar autorizada la importación o la publicación, según el caso. El valor “Otros” se concreta en el atributo ***observaciones\_usuarios\_proyecto***. |
| **Obligatoriedad** | SÍ. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. Si todavía no se ha incorporado la resolución, se introduce el valor “Pendiente”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Resolucion_resolucion |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | fecha\_de\_entrada |
| :---- | :---- |
| **Etiqueta** | Fecha de entrada |
| **Etiqueta en la base de datos** | Fecha de entrada Fecha de entrada (estado) |
| **Tipo de campo en base de datos** | Fecha de entrada: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_entry_date/storage) Fecha de entrada (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Fecha de entrada tal y como consta en el expediente original. |
| **Tratamiento documental** | Patrón de fechas: AAAA-MM-DD |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | NO |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Fecha_de_entrada |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | fecha\_de\_salida |
| :---- | :---- |
| **Etiqueta** | Fecha de salida |
| **Etiqueta en la base de datos** | Fecha de salida Fecha de salida (estado) |
| **Tipo de campo en base de datos** | Fecha de salida: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_entry_date/storage) Fecha de salida (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Fecha de salida tal y como consta en el expediente original. |
| **Tratamiento documental** | Patrón de fechas: AAAA-MM-DD |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Repetibilidad** | NO |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Fecha_de_salida |
| **Equivalencias con otros esquemas** |  |

**Eliminado**

| nombre\_del\_atributo | DOC\_IDCOMP |
| :---- | :---- |
| **Etiqueta** | Identificador complementario |
| **Esquema de metadatos de origen** | NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte https://www.culturaydeporte.gob.es/cultura/areas/archivos/mc/cneda/documentacion/normas/neda-mc.html |
| **Definición** | Código de identificación asignado a la entidad por otro sistema de información. |
| **Tratamiento documental** | Identificador del expediente, en la forma más completa, tal como consta en el original del ARCHIVO GENERAL DE LA ADMINISTRACIÓN (ALCALÁ DE HENARES, ESPAÑA) https://www.culturaydeporte.gob.es/cultura/areas/archivos/mc/archivos/aga/bases-de-datos.html |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | AGA, Sección Cultura 21/07062, Expediente 5440-46 |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | ISAD(G) 3.1.1. Código de referencia EAD \<altformavail\> \<DOC\_IDCOMP\> |

# Entidad *Formulario 0* {#entidad-formulario-0}

* Generalmente, anteriores a 1939\.  
* Norma aplicable: **TODO Ivan/Miquel**

| nombre\_del\_atributo | ID\_Formulario\_0 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 0 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 0 |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | comentario |
| :---- | :---- |
| **Etiqueta** | Comentario |
| **Etiqueta en la base de datos** | Comentario Comentario (estado) |
| **Tipo de campo en base de datos** | Comentario: [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/form_0/fields/node.form_0.field_observations/storage) Comentario (estado): Taxonomía |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”.  |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Formulario 0\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 0 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Formulario 1* {#entidad-formulario-1}

* Entre 1939 y? **TODO Ivan/Miquel**.  
* Norma aplicable: **TODO Ivan/Miquel**

| nombre\_del\_atributo | ID\_Formulario\_1 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 1 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Tipo de campo en base de datos** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 1 |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | valor\_literario\_o\_artistico |
| :---- | :---- |
| **Etiqueta** | Valor literario o artístico |
| **Etiqueta en la base de datos** | Valor literario o artístico Valor literario o artístico (estado) |
| **Tipo de campo en base de datos** | Valor literario o artístico: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Valor literario o artístico (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | valor\_documental |
| :---- | :---- |
| **Etiqueta** | Valor documental |
| **Etiqueta en la base de datos** | Valor documental Valor documental (estado) |
| **Tipo de campo en base de datos** | Valor documental: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Valor documental (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | otras\_observaciones |
| :---- | :---- |
| **Etiqueta** | Otras observaciones |
| **Etiqueta en la base de datos** | Otras observaciones Otras observaciones (estado) |
| **Tipo de campo en base de datos** | Otras observaciones: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Otras observaciones (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Formulario 1\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 1 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Formulario 2* {#entidad-formulario-2}

* Entre ? y ? **TODO Ivan/Miquel**.  
* Norma aplicable: **TODO Ivan/Miquel**

| nombre\_del\_atributo | ID\_Formulario\_2 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 2 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 2 |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_al\_dogma\_o\_a\_la\_moral |
| :---- | :---- |
| **Etiqueta** | Ataca al dogma o a la moral |
| **Etiqueta en la base de datos** | ¿Ataca al dogma o a la moral? ¿Ataca al dogma o a la moral? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca al dogma o a la moral?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca al dogma o a la moral? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_las\_instituciones\_del\_regimen |
| :---- | :---- |
| **Etiqueta** | Ataca a las instituciones del régimen |
| **Etiqueta en la base de datos** | ¿Ataca a las instituciones del régimen? ¿Ataca a las instituciones del régimen? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a las instituciones del régimen?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a las instituciones del régimen? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tiene\_valor\_literario\_o\_documental |
| :---- | :---- |
| **Etiqueta** | Tiene valor literario o documental |
| **Etiqueta en la base de datos** | ¿Tiene valor literario o documental? ¿Tiene valor literario o documental? (estado) |
| **Tipo de campo en base de datos** | ¿Tiene valor literario o documental?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Tiene valor literario o documental? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | razones\_circunstanciales\_que\_aconsejan\_una\_ u\_otra\_decision |
| :---- | :---- |
| **Etiqueta** | Razones circunstanciales que aconsejan una u otra decisión |
| **Etiqueta en la base de datos** | Razones circunstanciales que aconsejan una u otra decisión Razones circunstanciales que aconsejan una u otra decisión (estado) |
| **Tipo de campo en base de datos** | Razones circunstanciales que aconsejan una u otra decisión: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Razones circunstanciales que aconsejan una u otra decisión (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en Tratamiento documental)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Formulario 2\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 2 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Formulario 3* {#entidad-formulario-3}

* Entre ? y ? **TODO Ivan/Miquel**.  
* Norma aplicable: **TODO Ivan/Miquel**

| nombre\_del\_atributo | ID\_Formulario\_3 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 3 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 3 |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_al\_dogma |
| :---- | :---- |
| **Etiqueta** | Ataca al dogma |
| **Etiqueta en la base de datos** | ¿Ataca al dogma? ¿Ataca al dogma? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca al dogma?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca al dogma? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_la\_iglesia |
| :---- | :---- |
| **Etiqueta** | Ataca a la Iglesia |
| **Etiqueta en la base de datos** | ¿Ataca a la Iglesia? ¿Ataca a la Iglesia? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a la Iglesia?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a la Iglesia? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_sus\_ministros |
| :---- | :---- |
| **Etiqueta** | Ataca a sus ministros |
| **Etiqueta en la base de datos** | ¿Ataca a sus ministros? ¿Ataca a sus ministros? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a sus ministros?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a sus ministros? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_la\_moral |
| :---- | :---- |
| **Etiqueta** | Ataca a la moral |
| **Etiqueta en la base de datos** | ¿Ataca a la moral? ¿Ataca a la moral? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a la moral?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a la moral? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_al\_regimen\_y\_ a\_sus\_instituciones |
| :---- | :---- |
| **Etiqueta** | Ataca al régimen y a sus instituciones |
| **Etiqueta en la base de datos** | ¿Ataca al régimen y a sus instituciones? ¿Ataca al régimen y a sus instituciones? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca al régimen y a sus instituciones?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca al régimen y a sus instituciones? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_las\_personas\_que\_colaboran\_o\_han\_colaborado\_con\_el\_regimen |
| :---- | :---- |
| **Etiqueta** | Ataca a las personas que colaboran o han colaborado con el régimen |
| **Etiqueta en la base de datos** | ¿Ataca a las personas que colaboran o han colaborado con el régimen? ¿Ataca a las personas que colaboran o han colaborado con el régimen? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a las personas que colaboran o han colaborado con el régimen?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a las personas que colaboran o han colaborado con el régimen? (estado): Taxonomia  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | resultando |
| :---- | :---- |
| **Etiqueta** | Resultando |
| **Etiqueta en la base de datos** | Resultando Resultando (estado) |
| **Tipo de campo en base de datos** | Resultando: [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/form_3/fields/node.form_3.field_resultando/storage) Resultando (estado): Taxonomía resultando\_status |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Formulario 3\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 3 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Formulario 4*

* Formulario de la solicitud de circulación.  
* Norma aplicable: **TODO Ivan/Miquel**

**DUBTE: És necessari incorporar el camp *firma*?**

**DUBTE: Cal incorporar també el camp *enmienda*?**

| nombre\_del\_atributo | ID\_Formulario\_4 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 4 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 4\. |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | valor\_literario |
| :---- | :---- |
| **Etiqueta** | Valor literario  |
| **Etiqueta en la base de datos** | Valor literario Valor literario (estado) |
| **Tipo de campo en base de datos** | Valor literario: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Valor literario (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | valor\_documental |
| :---- | :---- |
| **Etiqueta** | Valor documental |
| **Etiqueta en la base de datos** | Valor documental Valor documental (estado) |
| **Tipo de campo en base de datos** | Valor documental: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Valor documental (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |
| **nombre\_del\_atributo** | matiz\_politico |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tachaduras |
| :---- | :---- |
| **Etiqueta** | Tachaduras  |
| **Etiqueta en la base de datos** | Tachaduras  |
| **Tipo de campo en base de datos** | Archivo |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Tachaduras obtenidas a partir del documento original. |
| **Tratamiento documental** | Dos opciones: Inserción de la imagen. Transcripción desde el original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODEDCIDE SGBD**: En caso que una tachadura tenga vinculada una enmienda, se podrá generar el atributo de la enmienda, y ambos elementos estarán relacionados mediante un código. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Únicamente en el caso de las transcripciones. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | otras\_observaciones |
| :---- | :---- |
| **Etiqueta** | Otras observaciones |
| **Etiqueta en la base de datos** | Otras observaciones Otras observaciones (estado) |
| **Tipo de campo en base de datos** | Otras observaciones: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Otras observaciones (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

 \[Entre Informe del lector y Formulario 4\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 4 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Formulario 5*

* Formulario de la solicitud de traducción.  
* Norma aplicable: **TODO Ivan/Miquel**

| nombre\_del\_atributo | ID\_Formulario\_5 |
| :---- | :---- |
| **Etiqueta** | Identificador del formulario 5 |
| **Etiqueta en la base de datos** | Identificador del formulario |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Formulario 5\. |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_al\_dogma\_o\_a\_la\_moral |
| :---- | :---- |
| **Etiqueta** | Ataca al dogma o a la moral |
| **Etiqueta en la base de datos** | ¿Ataca al dogma o a la moral? ¿Ataca al dogma o a la moral? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca al dogma o a la moral?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca al dogma o a la moral? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | ataca\_a\_las\_instituciones\_del\_regimen |
| :---- | :---- |
| **Etiqueta** | Ataca a las instituciones del régimen |
| **Etiqueta en la base de datos** | ¿Ataca a las instituciones del régimen? ¿Ataca a las instituciones del régimen? (estado) |
| **Tipo de campo en base de datos** | ¿Ataca a las instituciones del régimen?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Ataca a las instituciones del régimen? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tiene\_valor\_literario\_o\_documental |
| :---- | :---- |
| **Etiqueta** | Tiene valor literario o documental |
| **Etiqueta en la base de datos** | ¿Tiene valor literario o documental? ¿Tiene valor literario o documental? (estado) |
| **Tipo de campo en base de datos** | ¿Tiene valor literario o documental?: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) ¿Tiene valor literario o documental? (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | razones\_circunstanciales\_que\_aconsejan\_una\_ u\_otra\_decision |
| :---- | :---- |
| **Etiqueta** | Razones circunstanciales que aconsejan una u otra decisión |
| **Etiqueta en la base de datos** | Razones circunstanciales que aconsejan una u otra decisión Razones circunstanciales que aconsejan una u otra decisión (estado) |
| **Tipo de campo en base de datos** | Razones circunstanciales que aconsejan una u otra decisión: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Razones circunstanciales que aconsejan una u otra decisión (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en Tratamiento documental)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | observaciones |
| :---- | :---- |
| **Etiqueta** | Observaciones |
| **Etiqueta en la base de datos** | Observaciones Observaciones (estado) |
| **Tipo de campo en base de datos** | Observaciones: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Observaciones (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Formulario 5\] Ha sido elaborado mediante el formulario

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_one\_to\_one\_relation  
* No és obligatori

\[Entre Formulario 5 e Informe del lector\] Es formulario del informe del lector

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Ha sido elaborado mediante el formulario”.

# Entidad *Importador* {#entidad-importador}

| nombre\_del\_atributo | ID\_Importador |
| :---- | :---- |
| **Etiqueta** | Identificador del importador |
| **Etiqueta en la base de datos** | Identificador del importador |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Importador |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_importador |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Nombre (M8145) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_NOMBRE\>  |
| **Etiqueta en la base de datos** | Nombre del importador Nombre del importador (estado) |
| **Tipo de campo en base de datos** | Nombre del importador: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_nombre_editor/storage) Nombre del importador (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Persona física o jurídica que tiene la intención de importar un documento.  |
| **Tratamiento documental** | Control de autoridades, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe consignarse la forma más completa del importador, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de importador son los documentos de solicitud de importación/publicación. **TODO SGBD:** En caso de persona física, la información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte) |
| **Obligatoriedad** | SÍ. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | Figueroa Gineco |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_importador |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | genero\_importador |
| :---- | :---- |
| **Etiqueta** | Género |
| **Etiqueta en la base de datos** | Género |
| **Tipo de campo en base de datos** | [Taxonomía](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Identificación del género si el importador es una persona física.  |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Uno dos valores a elegir entre los siguientes: Desconocido Hombre Mujer No binario Persona jurídica Desconocido, Hombre, Mujer y No binario se asignan si el importador es una persona física. De lo contrario, se asigna directamente el valor “Persona jurídica”. |
| **Obligatoriedad** | Sí. En caso que sea imposible identificarlo a partir de la documentación disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Genero |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | owl:sameAs |
| :---- | :---- |
| **Etiqueta** | sameAs |
| **Etiqueta en la base de datos** | Información sobre el importador en otras bases de datos |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_owl_sameas/storage) |
| **Esquema de metadatos de origen** | The OWL 2 Schema vocabulary (OWL 2\) https://www.w3.org/TR/2004/REC-owl-ref-20040210/ |
| **Definición** | Código de identificación asignado a la entidad por otro sistema de información. *Código de referencia* The built-in OWL property [owl:sameAs](http://www.w3.org/TR/2004/REC-owl-semantics-20040210/#owl_sameAs) links an individual to an individual. Such an owl:sameAs statement indicates that two URI references actually refer to the same thing: the individuals have the same "identity". |
| **Tratamiento documental** | URI de las instancias que son considerades idénticas. Los conjuntos de datos donde se intentaran localitzar los URI de recursos idénticos son: AGA, BNE, Dbpedia y Wikidata.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: Establecimiento del mecanismo de reconciliación con los conjuntos de datos externos. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISAAR(CPF) 5.1.6. Identificadores para instituciones  *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* [https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/](https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos_3978/): \<AGE\_IDCOMP\> |

**Eliminado:**

| nombre\_del\_atributo | Identificador (M7693) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_ID\>  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Código que representa al importador de forma única y permanente dentro del entorno concreto de información archivística |
| **Tratamiento documental** | El identificador se genera en forma de Uniform Resource Identifier (URI). **TODO SGBD**: Determinará el patrón de los URI del proyecto. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | EL URI se genera automáticamente a partir del patrón establecido para el proyecto. |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISDIAH 5.1.1. Identificador ISAAR(CPF) 5.1.6. Identificadores para instituciones |

# Entidad *Informe de Lector* {#entidad-informe-de-lector}

| nombre\_del\_atributo | ID\_Informe\_Lector |
| :---- | :---- |
| **Etiqueta** | Identificador del informe del lector |
| **Etiqueta en la base de datos** | Identificador del informe del lector |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Informe de lector |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | idInformesLector |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Nombre (M2608) |
| :---- | :---- |
| **Etiqueta** | \<DOC\_NOMBRE\> |
| **Etiqueta en la base de datos** | Título del informe del lector |
| **Tipo de campo en base de datos** | [Texto (largo con formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_titulo_del_expediente/storage) |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Denominación o título atribuido al informe de lector por el proyecto. |
| **Tratamiento documental** | Patrón de título a partir de valores de otros atributos.  **TODO SGBD**: Configura el patrón, y la obtención automática de datos a partir de otros atributos. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Para el nombre atribuido por los miembros del proyecto, la estructuración de los datos se realizará aplicando el siguiente esquema de valores: *Informe del lector \[nombre del lector\] sobre \[título\] de \[autor\] publicado por \[editorial\], entre \[fecha del informe\]*  |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre |
| **Equivalencias con otros esquemas** | EAD [https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html](https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html): unittitle ISAD(G) [https://cultura.gencat.cat/web/.content/dgpc/arxius\_despublicada/norma\_de\_descripcio\_arxivistica\_de\_catalunya/arxius/isad2\_catala.pdf](https://cultura.gencat.cat/web/.content/dgpc/arxius_despublicada/norma_de_descripcio_arxivistica_de_catalunya/arxius/isad2_catala.pdf): 3.1.2 MODS [https://www.loc.gov/standards/mods/mods-outline-3-7.html](https://www.loc.gov/standards/mods/mods-outline-3-7.html): \<titleInfo\>\<title\> MARC 130, 240, 245  |

| nombre\_del\_atributo | Fecha (M1810) |
| :---- | :---- |
| **Etiqueta** | \<DOC\_FECHA\> |
| **Etiqueta en la base de datos** | Fecha de emisión del informe del lector Fecha de emisión del informe del lector (estado) |
| **Tipo de campo en base de datos** | Fecha de emisión del informe del lector: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_datesingle/storage)  Fecha de emisión del informe del lector (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Fecha de emisión del informe. |
| **Tratamiento documental** | Patrón de fechas: DD-MM-AAAA  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Se consignará la fecha que aparezca en la documentación original.  |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Fecha |
| **Equivalencias con otros esquemas** | EAD [https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html](https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html): unitdate ISAD(G) [https://cultura.gencat.cat/web/.content/dgpc/arxius\_despublicada/norma\_de\_descripcio\_arxivistica\_de\_catalunya/arxius/isad2\_catala.pdf](https://cultura.gencat.cat/web/.content/dgpc/arxius_despublicada/norma_de_descripcio_arxivistica_de_catalunya/arxius/isad2_catala.pdf): 3.1.3 MARC 245 subfield f for inclusive dates, 245 subfield g for bulk dates, or 260 subfield c MODS [https://www.loc.gov/standards/mods/mods-outline-3-7.html](https://www.loc.gov/standards/mods/mods-outline-3-7.html): \<originInfo\>\<dateCreated\> |

| nombre\_del\_atributo | tachaduras |
| :---- | :---- |
| **Etiqueta** | Tachaduras  |
| **Etiqueta en la base de datos** | Tachaduras  |
| **Tipo de campo en base de datos** | Archivo |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Tachaduras obtenidas a partir del documento original. |
| **Tratamiento documental** | Dos opciones: Inserción de la imagen. Transcripción desde el original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: En caso que una tachadura tenga vinculada una enmienda, se podrá generar el atributo de la enmienda, y ambos elementos estarán relacionados mediante un código. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Únicamente en el caso de las transcripciones. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | enmiendas |
| :---- | :---- |
| **Etiqueta** | Enmiendas |
| **Etiqueta en la base de datos** | Enmiendas |
| **Tipo de campo en base de datos** | Archivo |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Enmiendas obtenidas a partir del original. |
| **Tratamiento documental** | Dos opciones: Inserción de la imagen. Transcripción desde el original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: En caso que una tachadura tenga vinculada una enmienda, se podrá generar el atributo de la enmienda, y ambos elementos estarán relacionados mediante un código. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Únicamente en el caso de las transcripciones. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | propuesta\_de\_resolucion\_1 |
| :---- | :---- |
| **Etiqueta** | Propuesta de resolución transcrita |
| **Etiqueta en la base de datos** | Propuesta de resolución transcrita Propuesta de resolución transcrita (estado) |
| **Tipo de campo en base de datos** | Propuesta de resolución transcrita: Fecha Propuesta de resolución transcrita (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Propuesta de resolución a la solicitud de importación o publicación tal y como es formulada por el lector.  |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Transcripción desde el original. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | propuesta\_de\_resolucion\_2 |
| :---- | :---- |
| **Etiqueta** | Propuesta de resolución a partir de un vocabulario controlado |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Propuesta de resolución a la solicitud de importación o publicación expresada a través de categorías.  |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Un valor a elegir entre los siguientes: Autorizado  Prohibido o suspendido Suspendido temporalmente Silencio administrativo No se manifiesta Notas de aplicación de los valores. El valor “Autorizado” puede significar autorizada la importación o la publicación, según el caso. |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Informe del lector y Lector\] Redacta

* S’incorpora aquesta relació.   
* Camp del tipus:  field\_n\_to\_one\_relation  
* És obligatori

\[Entre Lector e Informe del lector\] Es redactor de 

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Redacta”.

**Eliminado:**

| nombre\_del\_atributo | Identificador (M1104) |
| :---- | :---- |
| **Etiqueta** | \<DOC\_ID\> |
| **Esquema de metadatos de origen** | NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Código que representa el informe de lector de forma única y permanente dentro del entorno de información archivística. Código de referencia. |
| **Tratamiento documental** | El identificador se genera en forma de Uniform Resource Identifier (URI). **TODO SGBD**: Determinará el patrón de los URI del proyecto. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | EL URI se genera automáticamente a partir del patrón establecido para el proyecto. Tipo de campo en Drupal: [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_age_id/storage) |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAD [https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html](https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html): unitid ISAD(G) [https://cultura.gencat.cat/web/.content/dgpc/arxius\_despublicada/norma\_de\_descripcio\_arxivistica\_de\_catalunya/arxius/isad2\_catala.pdf](https://cultura.gencat.cat/web/.content/dgpc/arxius_despublicada/norma_de_descripcio_arxivistica_de_catalunya/arxius/isad2_catala.pdf): 3.1.1 MODS [https://www.loc.gov/standards/mods/mods-outline-3-7.html](https://www.loc.gov/standards/mods/mods-outline-3-7.html): \<identifier\> |

# Entidad *Lector* {#entidad-lector}

| nombre\_del\_atributo | ID\_Lector |
| :---- | :---- |
| **Etiqueta** | Identificador del lector |
| **Etiqueta en la base de datos** | Identificador del lector |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Lector |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | FK_idLector |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Nombre (M8145) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_NOMBRE\>  |
| **Etiqueta en la base de datos** | Nombre del lector Nombre del lector (estado) |
| **Tipo de campo en base de datos** | Nombre del lector: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_nombre_editor/storage) Nombre del lector (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Persona física que ha elaborado el informe de lector.  |
| **Tratamiento documental** | Control de autoridades de lectores, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe consignarse la forma más completa del nombre, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de creador son los informes de lector. **TODO SGBD:** La información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte) |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: nameEntry ISAAR(CPF) 5.1.2. Formas autorizadas del nombre ISAAR(CPF) 5.1.3. Formas paralelas del nombre ISAAR(CPF) 5.1.4. Formas autorizadas del nombre según otras reglas ISAAR(CPF) 5.1.5. Otras formas del nombre ISDIAH 5.1.2. Formas autorizadas del nombre  ISDIAH 5.1.3. Formas paralelas del nombre ISDIAH 5.1.4. Otras formas del nombre |

| nombre\_del\_atributo | Tipo específico de entidad (M7418) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_TIPOENT\> |
| **Etiqueta en la base de datos** | Tipo de lector |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/reader/fields/node.reader.field_reader_type/storage) |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Tipo de lector de acuerdo con un vocabulario controlado. |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Uno dos valores a elegir entre los siguientes: Lector civil  Lector eclesiástico Tipo de campo en Drupal: Referencia de entidad |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityType ISAAR(CPF) 5.1.1. Tipo de entidad |

| nombre\_del\_atributo | owl:sameAs |
| :---- | :---- |
| **Etiqueta** | sameAs |
| **Etiqueta en la base de datos** | Información sobre el lector en otras bases de datos |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_owl_sameas/storage) |
| **Esquema de metadatos de origen** | The OWL 2 Schema vocabulary (OWL 2\) https://www.w3.org/TR/2004/REC-owl-ref-20040210/ |
| **Definición** | Código de identificación asignado a la entidad por otro sistema de información. *Código de referencia* The built-in OWL property [owl:sameAs](http://www.w3.org/TR/2004/REC-owl-semantics-20040210/#owl_sameAs) links an individual to an individual. Such an owl:sameAs statement indicates that two URI references actually refer to the same thing: the individuals have the same "identity". |
| **Tratamiento documental** | URI de las instancias que son considerades idénticas. Los conjuntos de datos donde se intentaran localitzar los URI de recursos idénticos son: AGA, BNE, Dbpedia y Wikidata.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **SGBD TODO**: Establecimiento del mecanismo de reconciliación con los conjuntos de datos externos. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISAAR(CPF) 5.1.6. Identificadores para instituciones  *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* [https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/](https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos_3978/): \<AGE\_IDCOMP\> |

| nombre\_del\_atributo | genero\_lector |
| :---- | :---- |
| **Etiqueta** | Género |
| **Etiqueta en la base de datos** | Género |
| **Tipo de campo en base de datos** | [Taxonomía](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Identificación del género del lector.  |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Uno dos valores a elegir entre los siguientes: Desconocido Hombre Mujer No binario  |
| **Obligatoriedad** | Sí. En caso que sea imposible identificarlo a partir de la documentación disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | FK_idLector |
| **Equivalencias con otros esquemas** |  |

**Eliminado:**

| nombre\_del\_atributo | Identificador (M7693) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_ID\>  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Código que representa al lector de forma única y permanente dentro del entorno concreto de información archivística |
| **Tratamiento documental** | Multivalor: El identificador se genera en forma de Uniform Resource Identifier (URI). identificador proporcionado por el AGA, formado por la combinación Número-Letra **TODO SGBD**: Determinará el patrón de los URI del proyecto.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  EL URI se genera automáticamente a partir del patrón establecido para el proyecto. |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISDIAH 5.1.1. Identificador ISAAR(CPF) 5.1.6. Identificadores para instituciones |

# Entidad *Libro presentado a censura* {#entidad-libro-presentado-a-censura}

En caso de partes componentes, se describe la parte, no el todo. El todo se informa en el campo “Forma parte de”.

| nombre\_del\_atributo | ID\_Libro\_Presentado |
| :---- | :---- |
| **Etiqueta** | Identificador del libro presentado a censura |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Libro presentado a censura |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | FK_LibroPresentado |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | dcterms:creator |
| :---- | :---- |
| **Etiqueta** | Creator |
| **Etiqueta en la base de datos** | Autor Autor (estado) |
| **Tipo de campo en base de datos** | Autor: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_creator/storage) Autor (estado): Taxonomía  |
| **Esquema de metadatos de origen** | DCMI Metadata Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Persona física o jurídica que tiene la responsabilidad principal de la creación del contenido del recurso. |
| **Tratamiento documental** | Control de autoridades de creadores, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe consignarse la forma más completa del nombre, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de creador son los documentos de solicitud de importación/publicación. **TODO SGBD:** La información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte) |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. Puede indicarse “Anónimo” si no tiene una autoría reconocida. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | dcterms:contributor |
| :---- | :---- |
| **Etiqueta** | Contributor |
| **Etiqueta en la base de datos** | Contributor Contributor (estado) |
| **Tipo de campo en base de datos** | Contribuidor: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_contributor/storage) Contribuidor (estado): Taxonomía  |
| **Esquema de metadatos de origen** | DCMI Metadata Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Una persona física o jurídica reponsable de realizar constribuciones al contenido del recurso. |
| **Tratamiento documental** | Vocabulario controlado de tipos de contribuciones, y control de autoridades de contribuidores, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Para cada contribuidor debe seleccionarse el tipo de contribución a partir del vocabulario controlado, y debe consignarse la forma más completa del nombre del contribuidor, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de contribuidor son los documentos de solicitud de importación/publicación. **TODO SGBD:** En caso de persona física, la información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte). |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | dcterms:title |
| :---- | :---- |
| **Etiqueta** | Title |
| **Esquema de metadatos de origen** | DCMI Metadata Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | A name given to the resource. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El título se da tal y como aparece en los documentos del expediente, pero respetando los criterios ortográficos de cada lengua en lo que respecta a la capitalización de las palabras.  |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | dcterms:relation |
| :---- | :---- |
| **Etiqueta** | Relation |
|  | Está relacionado con/es versión de |
| **Esquema de metadatos de origen** | DCMI Metadata Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Referencia al recurso relacionado.  |
| **Tratamiento documental** | dcterms:title \= "el recurs actual" dcterms: relation \= "tipo de relación \[espacio\] identificador único del recurso relacionado" donde "tipo de relación" es una marca \[token\] extraída del siguiente vocabulario controlado:  IsPartOf IsVersionOf IsFormatOf  IsReferencedBy isReplacedBy IsRequiredBy |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | Title="Reading Turgenev"Relation \="IsPartOf Two Lives" \[collection of two novellas, one of which is "Reading Turgenev"\] |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | texto\_completo |
| :---- | :---- |
| **Etiqueta** | Texto completo |
| **Etiqueta en la base de datos** | Texto completo |
| **Tipo de campo en base de datos** | Archivo[https://censurarusa.enproves.net/admin/structure/types/manage/published\_book/fields/node.published\_book.field\_identificador\_del\_libro\_pu/storage](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Acceso al texto completo del libro analizado.  |
| **Tratamiento documental** | Inserción de la imagen generada por la digitalización del expediente. **TODO SGBD**: Mecanismo de inserción de la imagen. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | No |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Título uniforme  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 240 |
| **Etiqueta en la base de datos** | Título uniforme |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Título uniforme de una obra cuando la descripción bibliográfica tiene como punto de acceso principal un campo que contiene un nombre de persona (campo 100), de entidad (campo 110\) o de congreso (campo 111). Se utiliza un título uniforme cuando una obra se ha publicado con diferentes títulos y hay que elegir uno determinado que la represente.   |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. Las reglas de catalogación prescriben también el uso de este campo cuando hay que añadir o suprimir algo al título. En este último caso, puede que el título no varíe en realidad. El título que aparece en la obra se registra en el campo 245 (Mención de título). El campo 240 no se utiliza cuando en el registro figura el campo 130 (Encabezamiento principal-Título uniforme). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador: Impresión o visualización. 0 \- No se imprime ni se visualiza. 1 \- Se imprime o se visualiza Segundo indicador: Caracteres que no alfabetizan. 0-9 \- Número de caracteres que no alfabetizan Códigos de subcampo  $a Título uniforme (NR)  $d Fecha de la firma de un tratado (R)  $f Fecha de la obra (NR)  $g Información miscelánea (R)  $h Tipo de material (NR)  $k Subencabezamiento de forma (R)  $l Lengua de la obra (NR)  $m Medio de interpretación (R)  $n Número de parte o sección de la obra (R)  $o Arreglo (NR)  $p Nombre de parte o sección de la obra (R)  $r Tonalidad (NR)  $s Versión (R)  $0 Número de control del registro de autoridad o número normalizado (R)  $1 URI de un objeto del mundo real (R)  $2 Fuente del encabezamiento o término (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No  |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 240 10$aVoïna i mir$lEspañol |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

# Entidad *Libro publicado* {#entidad-libro-publicado}

| nombre\_del\_atributo | ID\_Libro\_Publicado |
| :---- | :---- |
| **Etiqueta** | Identificador del libro publicado |
| **Etiqueta en la base de datos** | Identificador del libro publicado |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Libro publicado |
| **Tratamiento documental** | k |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | idLibrosPublicados |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Número de control BNE  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 001 |
| **Etiqueta en la base de datos** | Número de control BNE |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Contiene el número de control asignado por la BNE. En los procesos de intercambio, la entidad que lo inicia debe proporcionar a las organizaciones que participan la documentación sobre la estructura del número de control y sus pautas de aplicación. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | En la BNE, incluye el código de subcampo $a por defecto. |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | SÍ |
| **Ejemplos** | 001 $abimo0001486120 |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Numero_de_control_BNE |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Número de copyright o de depósito legal   |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 017 |
| **Etiqueta en la base de datos** | Número de copyright o de depósito legal |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Número de registro de copyright o de depósito legal para un documento que se adquirió por copyright o por depósito legal. La agencia que asigna el número siempre se incluye junto con el número de copyright o de depósito legal. El campo se repite cuando más de una agencia ha asignado un número de copyright o de depósito legal. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. No definido. \# \- No definido Segundo indicador. Control de la visualización associada. \# \- Número de copyright o de depósito legal. 8 \- No genera ninguna visualización asociada Códigos de subcampo  $a Número de copyright o de depósito legal (R)  $b Agencia que asigna el número (NR)  $d Fecha (R)  $i Texto de visualización (NR)  $z Número de copyright o de depósito legal cancelado/no válido (R)  $2 Fuente (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | 017   $aB 2685-1959$bOficina Depósito Legal Barcelona |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Numero_de_Copyright_o_de_DL |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Código de lengua   |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 041 |
| **Etiqueta en la base de datos** | Código de lengua  |
| **Tipo de campo en base de datos** | Referencia de entidad |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Códigos de las lenguas asociadas a un documento. Se incluye en registros de documentos multilingües, o que incluyen una traducción, o documentos en los que el medio de comunicación es un lenguaje de signos. Las fuentes de los códigos son la MARC Code List for Languages u otras listas de códigos, como la ISO 639-1 (Codes for the representation of names of languages \- Part 1 : alpha-2 code). |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. Indicación de traducción. \# \- No se proporciona información. 0 \- El documento no es ni incluye una traducción. 1 \- El documento es o incluye una traducción  Segundo indicador. Fuente del código. \# \- Código MARC de lengua. El código se toma de: MARC Code List for Languages. 7 \- Fuente especificada en el subcampo $2  Códigos de subcampo  $a Código de lengua del texto/banda sonora o título independiente (R)  $b Código de lengua del sumario o resumen (R)  $d Código de lengua del texto cantado o hablado (R)  $e Código de lengua de los libretos (R)  $f Código de lengua de la tabla de contenido (R)  $g Código de lengua del material anejo si no son libretos ni transcripciones (R)  $h Código de lengua original (R)  $i Código de lengua de los intertítulos (R)  $j Código de lengua de los subtítulos (R)  $k Código de lengua de las traducciones intermedias (R)  $m Código de lengua del material anejo original si no son libretos (R)  $n Código de lengua del libreto original (R)  $p Código de lengua de los subtítulos accesibles abiertos o cerrados (R)  $q Código de lengua de audio accesible (R)  $r Código de lengua de lenguaje visual accesible (no textual) (R)  $t Código de lengua de las transcripciones anejas para materiales audiovisuales (R)  $2 Fuente del código (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | 041\. 1 $aspa$hrus |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Numero_de_Copyright_o_de_DL |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Punto de acceso principal  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 1XX |
| **Etiqueta en la base de datos** | Punto de acceso principal |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Los campos 100, 110, 111 y 130 contienen un encabezamiento de nombre (de persona, entidad o congeso) o título uniforme utilizados como encabezamiento principal. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. El punto de acceso principal se escoge en función de las reglas de catalogación de la BNE: Reglas de Catalogación [http://www.bne.es/media/Perfiles/Bibliotecarios/reglas-catalogacion.pdf](http://www.bne.es/media/Perfiles/Bibliotecarios/reglas-catalogacion.pdf). Generalmente se asigna a la persona que es responsable principal de la obra. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Por ejemplo, en el caso de “100 \- Punto de acceso principal \- Nombre de persona” las incorporaciones pueden ser las siguientes: Primer indicador: 0 – Nombre; 1 \- Apellido(s); 3 \- Nombre de familia Segundo indicador: No definido Códigos de subcampo: $a Nombre de persona (NR)  $b Numeración (NR)  $c Títulos y otros términos asociados al nombre (R)  $d Fechas asociadas al nombre (NR)  $e Término indicativo de función (R)  $f Fecha de publicación (NR)  $g Información miscelánea (R)  $j Calificador de atribución (R)  $k Subencabezamiento de forma (R)  $l Lengua de la obra (NR)  $n Número de parte o sección de la obra (R)  $p Nombre de parte o sección de la obra (R)  $q Forma desarrollada del nombre (NR)  $t Título de la obra (NR)  $u Filiación (NR)  $0 Número de control del registro de autoridad o número normalizado (R)  $1 URI de un objeto del mundo real (R)  $2 Fuente del encabezamiento o término (NR)  $4 Relación (R)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No  |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 100 1\# $aTolstói, Lev$d1828-1910 |
| **Comentarios** | 100 \- Punto de acceso principal \- Nombre de persona 110 \- Punto de acceso principal \- Nombre de entidad 111 \- Punto de acceso principal \- Nombre de congreso 130 \- Punto de acceso principal \- Título uniforme |
| **posible name property desde los diagramas** | Punto_de_acceso_principal |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Título uniforme  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 240 |
| **Etiqueta en la base de datos** | Punto de acceso principal |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Título uniforme de una obra cuando la descripción bibliográfica tiene como punto de acceso principal un campo que contiene un nombre de persona (campo 100), de entidad (campo 110\) o de congreso (campo 111). Se utiliza un título uniforme cuando una obra se ha publicado con diferentes títulos y hay que elegir uno determinado que la represente.   |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. Las reglas de catalogación prescriben también el uso de este campo cuando hay que añadir o suprimir algo al título. En este último caso, puede que el título no varíe en realidad. El título que aparece en la obra se registra en el campo 245 (Mención de título). El campo 240 no se utiliza cuando en el registro figura el campo 130 (Encabezamiento principal-Título uniforme). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador: Impresión o visualización. 0 \- No se imprime ni se visualiza. 1 \- Se imprime o se visualiza Segundo indicador: Caracteres que no alfabetizan. 0-9 \- Número de caracteres que no alfabetizan Códigos de subcampo  $a Título uniforme (NR)  $d Fecha de la firma de un tratado (R)  $f Fecha de la obra (NR)  $g Información miscelánea (R)  $h Tipo de material (NR)  $k Subencabezamiento de forma (R)  $l Lengua de la obra (NR)  $m Medio de interpretación (R)  $n Número de parte o sección de la obra (R)  $o Arreglo (NR)  $p Nombre de parte o sección de la obra (R)  $r Tonalidad (NR)  $s Versión (R)  $0 Número de control del registro de autoridad o número normalizado (R)  $1 URI de un objeto del mundo real (R)  $2 Fuente del encabezamiento o término (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No  |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 240 10$aVoïna i mir$lEspañol |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Titulo_Uniforme |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Mención de título   |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 245 |
| **Etiqueta en la base de datos** | Mención de título |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Área de título y mención de responsabilidad de la descripción bibliográfica de una obra. El campo de la mención de título consiste en el título propiamente dicho y también puede contener la designación general de material (tipo de material), el resto de título, información complementaria sobre el título, el resto de la transcripción de la portada y la mención de responsabilidad. El título propiamente dicho incluye el título en breve y el título alternativo, el número de la parte o sección y el nombre de ésta. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. Punto de acceso adicional de título. 0 \- No hay punto de acceso adicional. 1 \- Hay punto de acceso adicional Segundo indicador. Caracteres que no alfabetizan. 0 \- No hay caracteres que no alfabeticen. 1-9 \- Número de caracteres que no alfabetizan Códigos de subcampo  $a Título (NR)  $b Resto del título (NR)  $c Mención de responsabilidad, etc. (NR)  $f Fechas extremas (NR)  $g Fechas predominantes (NR)  $h Tipo de material (NR)  $k Forma (R)  $n Número de parte o sección de la obra (R)  $p Nombre de parte o sección de la obra (R)  $s Versión (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 245 13$aLa guerra y la paz$h\[Texto impreso\]$cLeon Tolstoi ; traducción directa del ruso por Francisco José Alcántara y José Laín Entralgo |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Mencion_de_titulo |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Publicación, distribución, etc. (pie de imprenta)   |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 260 |
| **Etiqueta en la base de datos** | Publicación, distribución, etc. (pie de imprenta) |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Información relativa a la publicación, impresión, distribución, emisión, lanzamiento o producción de una obra. Para los documentos inéditos o los materiales que se controlan de forma colectiva, puede no utilizarse este campo o, de utilizarse, puede contener solamente el subcampo $c (Fecha de publicación, distribución, etc.). |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. Secuencia de menciones de publicación. \# \- No aplicable/No se da información/Primer editor disponible. 2 \- Editor intermedio. 3 \- Editor actual/último Segundo indicador. No definido. \# \- No definido Códigos de subcampo  $a Lugar de publicación, distribución, etc. (R)  $b Nombre del editor, distribuidor, etc. (R)  $c Fecha de publicación, distribución, etc. (R)  $e Lugar de fabricación (R)  $f Fabricante (R)  $g Fecha de fabricación (R)  $3 Especificación de materiales (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | 260   $aBarcelona$bVergara$c\[1960\]$fGrafesa |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Publicacion_distribucion_etc |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Descripción física  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 300  |
| **Etiqueta en la base de datos** | Descripción física |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Descripción física del documento, incluyendo la extensión del mismo, sus dimensiones y otros detalles físicos, así como una descripción del material anejo y del tipo y tamaño de la unidad. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. Los datos de este campo se incluyen normalmente de acuerdo con las especificaciones de las distintas reglas de catalogación. En los registros creados de acuerdo con reglas de catalogación basadas en las ISBD (Descripción Bibliográfica Internacional Normalizada), existe una relación entre la puntuación ISBD prescrita y la identificación de los datos de un subcampo determinado. Los registros bibliográficos creados según las AACR2 siguen los principios ISBD para descripción y puntuación. La mayor parte de los ejemplos de esta sección ilustran la puntuación ISBD prescrita asociada a subcampos determinados. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. No definido. \# \- No definido Segundo indicador. No definido. \# \- No definido Códigos de subcampo:  $a Extensión (R)  $b Otras características físicas (NR)  $c Dimensiones (R)  $e Material anejo (NR)  $f Tipo de unidad (R)  $g Tamaño de la unidad (R)  $3 Especificación de materiales (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | 300   $a2 v., 17 h. de lám.$c18 cm |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Publicacion_distribucion_etc |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Mención de serie  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 490  |
| **Etiqueta en la base de datos** | Mención de serie |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Mención de serie para un título de serie.  |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. Del campo 490 no se genera punto de acceso adicional de serie. Siempre que se utiliza un campo 490 y se quiere hacer un punto de acceso adicional de serie, se incluyen en el registro bibliográfico tanto la mención de serie (campo 490\) como su correspondiente punto de acceso adicional de serie (campos 800-830). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Primer indicador. Política de recuperación de series. 0 \- Serie sin recuperación. 1 \- Serie con recuperación Segundo indicador. No definido. \# \- No definido Códigos de subcampo  $a Mención de serie (R)  $l Signatura topográfica de la Biblioteca del Congreso (NR)  $v Designación de volumen o secuencia (R)  $x Número Internacional Normalizado para Publicaciones Seriadas (ISSN) (R)  $3 Especificación de materiales (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | 490 0 $aClásicos "Vergara" |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Mencion_de_la_serie |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Encabezamiento de materia  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 6XX |
| **Etiqueta en la base de datos** | Encabezamiento de materia  |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Los campos 6XX contienen encabezamientos y términos de materia. La mayoría de estos campos contienen puntos de acceso adicionales o términos de materia basados en las listas y ficheros de autoridad identificados a partir del segundo indicador (Sistema de encabezamientos de materia/tesauro) o del subcampo $2 (Fuente del encabezamiento o término). En el campo 653 (Término de indización-No controlado) se incluyen términos no controlados para recuperar el contenido de un documento. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. La BNE no asigna este atributo a las obras de literatura. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Por ejemplo, en el caso de “650 \- Punto de acceso adicional de materia \- Término de materia” las incorporaciones pueden ser las siguientes: Primer indicador. Nivel de materia. \# \- No se proporciona información. 0 \- No se especifica. 1 – Principal. 2 – Secundaria Segundo indicador. 7 \- Fuente especificada en el subcampo $2 Códigos de subcampo.  Término principal  $a Término de materia o nombre geográfico como elemento inicial (NR)  $b Término de materia que sigue a un nombre geográfico como elemento inicial (NR)  $c Localización del acontecimiento (NR)  $d Fechas vigentes (NR)  $e Término indicativo de función (R)  $g Información miscelánea (R)  $4 Relación (R)  Subdivisiones de materia  $v Subdivisión de forma (R)  $x Subdivisión de materia general (R)  $y Subdivisión cronológica (R)  $z Subdivisión geográfica (R)  Subcampos de control  $0 Número de control del registro de autoridad o número normalizado (R)  $1 URI de un objeto del mundo real (R)  $2 Fuente del encabezamiento o término (NR)  $3 Especificación de materiales (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No  |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** | 600 \- Punto de acceso adicional de materia \- Nombre de persona 610 \- Punto de acceso adicional de materia \- Nombre de entidad corporativa 611 \- Punto de acceso adicional de materia \- Nombre de congreso 630 \- Punto de acceso adicional de materia \- Título uniforme 647 \- Punto de acceso adicional de materia \- Nombre del acontecimiento 648 \- Punto de acceso adicional de materia \- Término cronológico 650 \- Punto de acceso adicional de materia \- Término de materia 651 \- Punto de acceso adicional de materia \- Nombre geográfico 653 \- Término de indización \- No controlado 654 \- Punto de acceso adicional \- Términos de materia por facetas 655 \- Término de indización \- Género/forma 656 \- Término de indización \- Profesión 657 \- Término de indización \- Función 658 \- Término de indización \- Objetivo curricular 662 \- Punto de acceso adicional de materia \- Nombre jerárquico de lugar 688 \- Punto de acceso adicional de materia \- Tipo de entidad no especificada 69X \- Campos locales de encabezamiento de materia |
| **posible name property desde los diagramas** | Encabezamiento_de_Materia |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Punto de acceso adicional  |
| :---- | :---- |
| **Etiqueta** | Etiqueta: 70X-75X |
| **Etiqueta en la base de datos** | Punto de acceso adicional  |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | MARC21 [http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21\_registros-bibliograficos.pdf](http://www.bne.es/webdocs/Inicio/Perfiles/Bibliotecarios/MARC21_registros-bibliograficos.pdf) |
| **Definición** | Puntos de acceso adicionales que facilitan otro acceso a un registro bibliográfico a partir de nombres y/o títulos que se relacionan de distintas maneras con una obra. Se hacen puntos de acceso adicionales para personas, entidades y congresos que tengan algún tipo de responsabilidad en la creación de la obra, incluidas las responsabilidades intelectuales y de edición. También se incluyen puntos de acceso adicionales para otros títulos controlados que estén relacionados con la obra a la que corresponde el registro, como por ejemplo otras ediciones, etc. El campo 740 contiene títulos no controlados que se refieren a una parte del documento que se cataloga, o bien a un documento relacionado. Se asignan puntos de acceso adicionales de personas, entidades, congresos y títulos a los que no se accede con los encabezamientos de materia o de serie. Los campos 752-754 facilitan el acceso a un documento a través de otros aspectos de su contenido o de su descripción. |
| **Tratamiento documental** | Este atributo es importado desde la BNE siempre que el registro bibliográfico al que pertenece esté disponible en su catálogo. El punto de acceso principal se escoge en función de las reglas de catalogación de la BNE: Reglas de Catalogación [http://www.bne.es/media/Perfiles/Bibliotecarios/reglas-catalogacion.pdf](http://www.bne.es/media/Perfiles/Bibliotecarios/reglas-catalogacion.pdf).  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Puede incorporar indicadores (primero y segundo) y códigos de subcampo. Por ejemplo, en el caso de “700 \- Punto de acceso adicional \- Nombre de persona” las incorporaciones pueden ser las siguientes: Primer indicador. Tipo de elemento inicial del nombre de persona. 0 – Nombre. 1 \- Apellido(s). 3 \- Nombre de familia Segundo indicador. Tipo de punto de acceso adicional. \# \- No se proporciona información. 2 \- Entrada analítica Códigos de subcampo  $a Nombre de persona (NR)  $b Numeración (NR)  $c Títulos y otros términos asociados al nombre (R)  $d Fechas asociadas al nombre (NR)  $e Término indicativo de función (R)  $f Fecha de publicación (NR)  $g Información miscelánea (R)  $h Tipo de material (NR)  $i Información sobre la relación (R)  $j Calificador de la atribución (R)  $k Subencabezamiento de forma (R)  $l Lengua de la obra (NR)  $m Medio de interpretación (R)  $n Número de parte o sección de la obra (R)  $o Arreglo (NR)  $p Nombre de parte o sección de la obra (R)  $q Forma desarrollada del nombre (NR)  $r Tonalidad (NR)  $s Versión (R)  $t Título de la obra (NR)  $u Filiación (NR)  $x Número Internacional Normalizado para Publicaciones Seriadas (ISSN) (NR)  $0 Número de control del registro de autoridad o número normalizado (R)  $1 URI de un objeto del mundo real (R)  $2 Fuente del encabezamiento o término (NR)  $3 Especificación de materiales (NR)  $4 Relación (R)  $5 Institución que aplica el campo (NR)  $6 Enlace (NR)  $8 Enlace entre campos y número de secuencia (R) |
| **Obligatoriedad** | No  |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** | 700 \- Punto de acceso adicional \- Nombre de persona  710 \- Punto de acceso adicional \- Nombre de entidad  711 \- Punto de acceso adicional \- Nombre de congreso  720 \- Punto de acceso adicional \- Nombre no controlado  730 \- Punto de acceso adicional \- Título uniforme  740 \- Punto de acceso adicional \- Título relacionado o analítico o no controlado  751 \- Punto de acceso adicional \- Nombre geográfico  752 \- Punto de acceso adicional \- Nombre jerárquico de lugar 753 \- Información técnica sobre acceso a archivos de ordenador 754 \- Punto de acceso adicional \- Identificación taxonómica 758 – Identificador del recurso |
| **posible name property desde los diagramas** | Punto_de_Acceso_adicional |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | texto\_completo |
| :---- | :---- |
| **Etiqueta** | Texto completo |
| **Etiqueta en la base de datos** | Texto completo |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_full_text/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Acceso al texto completo del libro disponible en alguna colección digital (por ejemplo, la Biblioteca Digital Hispánica).  |
| **Tratamiento documental** | El valor es el enlace del documento. Preferentemente, la URI y el DOI. En su defecto, el URL.  Las fuentes donde localizar el texto completo del documento son: La Biblioteca Digital Hispánica (BDH). El enlace al texto completo en la BDH está disponible en el Catálogo bibliográfico de la BNE y, en consecuencia, debe importarse junto con el resto de atributos. En concreto, el enlace a la BDH se incorpora en el campo 856 del registro en el Catálogo bibliográfico de la BNE. HISPANA, buscador de objetos digitales del Ministerio de Cultura [https://hispana.mcu.es/es/inicio/inicio.do](https://hispana.mcu.es/es/inicio/inicio.do) Europeana https://www.europeana.eu/en  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** | [http://bdh-rd.bne.es/viewer.vm?id=0000255755\&page=1](http://bdh-rd.bne.es/viewer.vm?id=0000255755&page=1) \[disponible en el registro bibliográfico de la BNE, en el campo 856\. 41|uhttp://bdh-rd.bne.es/viewer.vm?id=0000255755\&page=1|yBiblioteca Digital Hispánica\]  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Texto_del_enlace |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | owl:sameAs |
| :---- | :---- |
| **Etiqueta** | sameAs |
| **Etiqueta en la base de datos** | Información sobre la obra publicada en otras bases de datos |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_full_text/storage) |
| **Esquema de metadatos de origen** | The OWL 2 Schema vocabulary (OWL 2\) https://www.w3.org/TR/2004/REC-owl-ref-20040210/ |
| **Definición** | The built-in OWL property [owl:sameAs](http://www.w3.org/TR/2004/REC-owl-semantics-20040210/#owl_sameAs) links an individual to an individual. Such an owl:sameAs statement indicates that two URI references actually refer to the same thing: the individuals have the same "identity". |
| **Tratamiento documental** | Siempre que una edición (manifestación) de una obra esté disponible en la BNE, debe incorporarse la URI de dicha edición en datos.bne.es https://datos.bne.es/inicio.html. El patrón de esta URI es el espacio de nombres  [http://datos.bne.es/edicion/](http://datos.bne.es/edicion/), seguido del valor en el campo “Número de control BNE” (001). Por ejemplo, [http://datos.bne.es/edicion/bimo0001486120](http://datos.bne.es/edicion/bimo0001486120).   |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: Establecimiento del mecanismo de reconciliación con los conjuntos de datos externos. |
| **Obligatoriedad** | No |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | http://datos.bne.es/edicion/bimo0001486120 |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

# Entidad *Proveedor de papel* {#entidad-proveedor-de-papel}

| nombre\_del\_atributo | ID\_Proveedor\_Papel |
| :---- | :---- |
| **Etiqueta** | Identificador del proveedor de papel |
| **Etiqueta en la base de datos** | Identificador del proveedor de papel |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Proveedor de papel |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_proveedor_de_papel |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Nombre (M8145) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_NOMBRE\>  |
| **Etiqueta en la base de datos** | Nombre del proveedor de papel Nombre del proveedor de papel (estado) |
| **Tipo de campo en base de datos** | Nombre del proveedor de papel: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_nombre_editor/storage) Nombre del proveedor de papel (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Persona física o jurídica que provee de papel para la publicación de libros.  |
| **Tratamiento documental** | Control de autoridades de lectores, para incorporar la forma más completa del nombre. **TODO SGBD:** Corregir la forma incompleta de denominación del importador incorporada antes de localizar una forma más completa. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe consignarse la forma más completa del nombre, de forma uniforme en el contexto de la base de datos.  La fuente principal del nombre de proveedor de papel son las solicitudes de publicación. **TODO SGBD:** La información de este atributo puede desplegarse mediante subatributos: Nombre Primer\_apellido Segundo\_apellido (fecha\_de\_nacimiento-fecha\_de\_muerte) |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Nombre_del_proveedor |
| **Equivalencias con otros esquemas** | EAC: nameEntry ISAAR(CPF) 5.1.2. Formas autorizadas del nombre ISAAR(CPF) 5.1.3. Formas paralelas del nombre ISAAR(CPF) 5.1.4. Formas autorizadas del nombre según otras reglas ISAAR(CPF) 5.1.5. Otras formas del nombre ISDIAH 5.1.2. Formas autorizadas del nombre  ISDIAH 5.1.3. Formas paralelas del nombre ISDIAH 5.1.4. Otras formas del nombre |

| nombre\_del\_atributo | owl:sameAs |
| :---- | :---- |
| **Etiqueta** | sameAs |
| **Etiqueta en la base de datos** | Información sobre el proveedor de papel en otras bases de datos |
| **Tipo de campo en base de datos** | [Enlace](https://censurarusa.enproves.net/admin/structure/types/manage/editor/fields/node.editor.field_owl_sameas/storage) |
| **Esquema de metadatos de origen** | The OWL 2 Schema vocabulary (OWL 2\) https://www.w3.org/TR/2004/REC-owl-ref-20040210/ |
| **Definición** | Código de identificación asignado a la entidad por otro sistema de información.   La propiedad de OWL owl:sameAs vincula a un individuo con otro individuo. Tal declaración owl:sameAs indica que dos referencias URI en realidad se refieren a lo mismo: los individuos tienen la misma "identidad". |
| **Tratamiento documental** | URI de las instancias que son considerades idénticas. Los conjuntos de datos donde se intentaran localitzar los URI de recursos idénticos son: AGA, BNE, Dbpedia y Wikidata.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: Establecimiento del mecanismo de reconciliación con los conjuntos de datos externos. |
| **Obligatoriedad** | No |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISAAR(CPF) 5.1.6. Identificadores para instituciones  *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* [https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/](https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos_3978/): \<AGE\_IDCOMP\> |

| nombre\_del\_atributo | genero\_proveedor\_papel |
| :---- | :---- |
| **Etiqueta** | Género |
| **Etiqueta en la base de datos** | Género |
| **Tipo de campo en base de datos** | [Taxonomía](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_id_expe_censu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Identificación del género si el proveedor de papel es una persona física.  |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Uno dos valores a elegir entre los siguientes: Desconocido Hombre Mujer No binario Persona jurídica Desconocido, Hombre, Mujer y No binario se asignan si el proveedor de papel es una persona física. De lo contrario, se asigna directamente el valor “Persona jurídica”. |
| **Obligatoriedad** | Sí. En caso que sea imposible identificarlo a partir de la documentación disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Genero |
| **Equivalencias con otros esquemas** |  |

**Eliminado:**

| nombre\_del\_atributo | Identificador (M7693) |
| :---- | :---- |
| **Etiqueta** | \<AGE\_ID\>  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Código que representa al proveedor de papel de forma única y permanente dentro del entorno concreto de información archivística |
| **Tratamiento documental** | El identificador se genera en forma de Uniform Resource Identifier (URI). **TODO SGBD**: Determinará el patrón de los URI del proyecto.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | EL URI se genera automáticamente a partir del patrón establecido para el proyecto. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAC: entityId ISDIAH 5.1.1. Identificador ISAAR(CPF) 5.1.6. Identificadores para instituciones |

# Entidad *Solicitud de importación*

| nombre\_del\_atributo | ID\_Solicitud\_Importacion |
| :---- | :---- |
| **Etiqueta** | Identificador de la solicitud de importación |
| **Etiqueta en la base de datos** | Identificador de la solicitud de importación |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Solicitud de importación |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | NO |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | idSolicitudImportacion |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | cantidad\_a\_importar |
| :---- | :---- |
| **Etiqueta** | Cantidad a importar |
| **Etiqueta en la base de datos** | Cantidad a importar Cantidad a importar (estado) |
| **Tipo de campo en base de datos** | Cantidad a importar: [Enter](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Cantidad a importar (estado): Taxonomía |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Número de ejemplares previstos para la importación. |
| **Tratamiento documental** | Número entero positivo (xsd: positiveInteger). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original.  |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Cantidad_a_importar |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | pais\_de\_origen |
| :---- | :---- |
| **Etiqueta** | País de origen |
| **Etiqueta en la base de datos** | País de origen |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/import/fields/node.import.field_country_of_origin/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | País de origen de la importación. |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe entrarse UNO de los siguientes valores del vocabulario controlado: *ISO 3166-1*. |
| **Obligatoriedad** | Sí. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Pais_de_origen |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_contributor/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | El valor se da tal y como aparece en el documento original, mediante transcripción. Un valor muy frecuente es Nulo. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Mota_Politico |
| **Equivalencias con otros esquemas** |  |

\[Entre Solicitud de importación e Importador\] Tiene como importador solicitante

* S’incorpora aquesta relació.   
* Camp del tipus:  n\_to\_m\_relation  
* És obligatori

\[Entre Importador y Solicitud de importación\] Es solicitante de

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Tiene como importador solicitante

# Entidad *Solicitud de publicación* {#entidad-solicitud-de-publicación}

| nombre\_del\_atributo | ID\_Solicitud\_Publicación |
| :---- | :---- |
| **Etiqueta** | Identificador de la solicitud de publicación |
| **Etiqueta en la base de datos** | Identificador de la solicitud de publicación |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Solicitud de publicación |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | NO |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | idSolcitudPublicacionEditores |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tirada |
| :---- | :---- |
| **Etiqueta** | Tirada |
| **Etiqueta en la base de datos** | Tirada Tirada (estado) |
| **Tipo de campo en base de datos** | Tirada: [Número (entero)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_tirada/storage) Tirada (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Número de ejemplares previstos para la publicación. |
| **Tratamiento documental** | Número entero positivo (xsd:positiveInteger). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original.  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Extensión (5.1) |
| :---- | :---- |
| **Etiqueta** | Volúmenes y páginas |
| **Etiqueta en la base de datos** | Volúmenes y páginas Volúmenes y páginas (estado) |
| **Tipo de campo en base de datos** | Volúmenes y páginas: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Volúmenes y páginas (estado): Taxonomía |
| **Esquema de metadatos de origen** | ISBD Edición Consolidada https://www.ifla.org/wp-content/uploads/2019/05/assets/hq/publications/series/44-es.pdf |
| **Definición** | Extensión: Número de unidades y/o subunidades que componen el recurso, ej. Los volúmenes- y/o páginas de un texto impreso. |
| **Tratamiento documental** | Designación específica del material (coincide con el elemento “5.1.2 Designación específica del material”): Ordinal de volúmenes expresado con el tipo de datos xsd:integer. Ejemplos: 1 v.; 3 v. Paginación (coincide con el elemento “5.1.4 Paginación”).  Si “Designación específica del material” incluye un solo volumen, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.1 Recursos en una unidad física”. Ejemplo: 327 p. 321 hojas 80 p. Nota: Verso de las páginas en blanco 56 hojas Nota: Hojas impresas por ambas caras  Si “Designación específica del material” incluye dos o más volúmenes, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.2 Recursos en más de una unidad física”. Ejemplos: 3 v. (vi, 310 p.; vi, 434 p.; viii, 492 p.)  3 v. (vi, 310 p., 20 hojas de láminas; viii, 432 p., 32 hojas de láminas; x, 490 p., 52 hojas de láminas) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD:** El SGBD tiene que tratarlo como un atributo compuesto (“composite attribute”): “An attribute that can be further subdivided to yield additional attributes. For example, a phone number such as 615-898-2368 may be divided into an area code (615), an exchange number (898), and a four-digit code (2368). Compare to simple attribute.” En el atributo principal se situará “Serie”. En los atributos adicionales se situarán: 5.1.2 Designación específica del material  5.1.4 Paginación |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | “Etiquetas del Formato MARC 21, en el que se indican los elementos descriptivos de las diferentes áreas (ISBD-G)”: (Fernández Porcel & Zaborras, 2010): 300\#\#|aExtensión y designación física del material :|bMención de otras características físicas ;|cDimensiones \+|eMaterial anejo  MARC to Dublin Core Crosswalk [https://www.loc.gov/marc/marc2dc.html](https://www.loc.gov/marc/marc2dc.html).  MARC to Dublin Core Crosswalk (Qualified): dcterms:extent (parcialmente, 300$a) |

| nombre\_del\_atributo | dcterms:format |
| :---- | :---- |
| **Etiqueta** | Format |
| **Etiqueta en la base de datos** | Formato Formato (estado) |
| **Tipo de campo en base de datos** | Formato: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Formato (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Dimensiones del libro. Corresponde al campo “Formato” en la solicitud de publicación. |
| **Tratamiento documental** | **TODO Ivan/Miquel** Vocabulario controlado de dimensiones. Si lo localizamos y las designaciones son aplicables a las explicaciones de los expedientes. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 12 x 17 cm |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | **TODO Miquel**: Analizar la correspondencia una vez definido correctamente “formato”. |

| nombre\_del\_atributo | dcterms:type |
| :---- | :---- |
| **Etiqueta** | Carácter |
| **Etiqueta en la base de datos** | Carácter de la publicación Carácter de la publicación (estado) |
| **Tipo de campo en base de datos** | Carácter de la publicación: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Carácter de la publicación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Género en sentido amplio. Corresponde al campo “Carácter” en la solicitud de publicación. |
| **Tratamiento documental** | Vocabulario libre. Valor que aparece en el documento original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | clase\_de\_papel |
| :---- | :---- |
| **Etiqueta** | Clase de papel |
| **Etiqueta en la base de datos** | Clase de papel Clase de papel (estado) |
| **Tipo de campo en base de datos** | Clase de papel: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Clase de papel (estado): taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | **TODO Ivan/Miquel: Si es posible, la definición tiene que estar respaldada por una disposición normativa.** |
| **Tratamiento documental** | Un valor extraído de un vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO Ivan/Miquel** Vocabulario controlado de clases de papel. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | Alisado corriente |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | medida\_de\_papel |
| :---- | :---- |
| **Etiqueta** | Medida de papel |
| **Etiqueta en la base de datos** | Medida de papel Medida de papel (estado) |
| **Tipo de campo en base de datos** | Medida de papel: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Medida de papel (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | **TODO Ivan/Miquel Si es posible, la definición tiene que estar respaldada por una disposición normativa.** |
| **Tratamiento documental** | **TODO** Vocabulario controlado de medidas de papel. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 70 x 100 cm |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | peso\_de\_papel |
| :---- | :---- |
| **Etiqueta** | Peso de papel |
| **Etiqueta en la base de datos** | Peso de papel Peso de papel (estado) |
| **Tipo de campo en base de datos** | Peso de papel: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Peso de papel (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | **TODO Ivan/Miquel Si es posible, la definición tiene que estar respaldada por una disposición normativa.** |
| **Tratamiento documental** | **TODO** Ivan/Miquel Vocabulario controlado de pesos de papel. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 26,5 kg. |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Área de serie y recurso monográfico multiparte (6) |
| :---- | :---- |
| **Etiqueta** | Serie y recurso monográfico multiparte |
| **Etiqueta en la base de datos** | Colección Colección (estado) |
| **Tipo de campo en base de datos** | Colección: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Colección (estado): Taxonomía  |
| **Esquema de metadatos de origen** | ISBD Edición Consolidada https://www.ifla.org/wp-content/uploads/2019/05/assets/hq/publications/series/44-es.pdf |
| **Definición** | El área de serie y recursos monográfico multiparte se usa cuando el recurso que se describe pertenece a un recurso bibliográfico mayor: serie o recurso monográfico multiparte.  |
| **Tratamiento documental** | El área de serie y recurso monográfico multiparte incluye el título propiamente dicho de una serie o recurso monográfico multiparte, el título paralelo de una serie o recurso monográfico multiparte, la información complementaria del título de una serie o recurso monográfico multiparte, las menciones de responsabilidad de una serie o recurso monográfico multiparte, el número internacional normalizado de una serie o recurso monográfico multiparte, la numeración en una serie o recurso monográfico multiparte. Es especialmente importante tener en cuenta la explicación de los términos ―título común‖ y ―título dependiente‖, que establece que estos términos, según se usan en las especificaciones, cubren las situaciones siguientes: (a) un título común con un título de sección, (b) una serie principal con una subserie y (c) un título común con un título dependiente de un recurso monográfico multiparte. Cuando un recurso pertenece a más de un recurso bibliográfico mayor, el área 6 contiene más de una mención de serie. El orden de dichas menciones viene determinado por el orden de preferencia de las fuentes para el área; en el caso de que estas posean igual valor, el orden sigue la secuencia de la información que figura en la fuente elegida. Un recurso continuado o un recurso monográfico multiparte pueden ser parte de una serie mayor. Recommended practice is to identify the series with a URI. If this is not possible or feasible, a literal value that identifies the creator may be provided. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD tiene que tratarlo como un atributo  compuesto (“composite attribute”): “An attribute that can be further subdivided to yield additional attributes. For example, a phone number such as 615-898-2368 may be divided into an area code (615), an exchange number (898), and a four-digit code (2368). Compare to simple attribute.” En el atributo principal se situará “Serie”. En los atributos adicionales se situarán: 6.1 Título propiamente dicho de una serie o recurso monográfico multiparte.  6.2 Título paralelo de una serie o recurso monográfico multiparte.  6.3 Información complementaria del título de una serie o recurso monográfico multiparte.  6.4 Menciones de responsabilidad de una serie o recurso monográfico multiparte.  6.5 Número internacional normalizado de una serie o recurso monográfico multiparte.  6.6 Numeración en una serie o recurso monográfico multiparte.    |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | “Etiquetas del Formato MARC 21, en el que se indican los elementos descriptivos de las diferentes áreas (ISBD-G)”: (Fernández Porcel & Zaborras, 2010): 490 1\#|aTítulo de la serie \=|aTítulo paralelo de la serie / mención de responsabilidad;|vnúmero de serie,|xISSN de la serie.|pTítulo de la subserie/mención de res-ponsabilidad de la subserie ;|vNúmero de la subserie  MARC to Dublin Core Crosswalk [https://www.loc.gov/marc/marc2dc.html](https://www.loc.gov/marc/marc2dc.html).  MARC to Dublin Core Crosswalk (Qualified): dcterms: isPartOf |

| nombre\_del\_atributo | dcterms:language |
| :---- | :---- |
| **Etiqueta** | Language |
| **Etiqueta en la base de datos** | Idioma |
| **Tipo de campo en base de datos** | [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_language/storage) |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Lengua del ejemplar presentado a censura. |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Debe entrarse UNO de los siguientes valores del vocabulario controlado: ISO 639-2 o ISO 639-3, or a literal value consisting of an IETF Best Current Practice 47 \[[IETF-BCP47](https://tools.ietf.org/html/bcp47) https://www.rfc-editor.org/info/bcp47\] language tag. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | Sí |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | MARC to Dublin Core Crosswalk [https://www.loc.gov/marc/marc2dc.html](https://www.loc.gov/marc/marc2dc.html).  MARC to Dublin Core Crosswalk (Qualified): 008/35-37 \--\> IS0369-2	  041 with no $2 \--\> ISO639-2	  041 with $2=iso639-3 \--\> ISO639-3 041 with $2=rfc1766 \--\> RFC1766	  041 with $2=rfc3066 \--\> RFC3066 041 with $2=rfc4646 \--\> RFC4646 |

| nombre\_del\_atributo | precio\_de\_venta |
| :---- | :---- |
| **Etiqueta** | Precio de venta |
| **Etiqueta en la base de datos** | Precio de venta Precio de venta (estado) |
| **Tipo de campo en base de datos** | Precio de venta: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_sale_price/storage) Precio de venta (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Precio de venta del libro. |
| **Tratamiento documental** | Número entero positivo (xsd: positiveInteger). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_contributor/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | El valor se da tal y como aparece en el documento original, mediante transcripción. Un valor muy frecuente es Nulo. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Solicitud de publicación y Editor\] Tiene como editor solicitante

* S’incorpora aquesta relació.   
* Camp del tipus:  n\_to\_m\_relation  
* És obligatori

\[Entre Editor y Solicitud de publicación\] Es solicitante de

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Tiene como editor solicitante”

\[Entre Solicitud de publicación y Proveedor de papel\] El papel de la publicación es provisto por

* S’incorpora aquesta relació.   
* Camp del tipus:  n\_to\_m\_relation\_2  
* No és obligatori

\[Entre Proveedor de papel y Solicitud de publicación\]  Provee de papel en la solicitud de publicación

* Aquesta relació no s’incorpora perquè s’infereix a partir de “El papel de la publicación es provisto por”

# Entidad *Solicitud de traducción*

| nombre\_del\_atributo | ID\_Solicitud\_Traduccion |
| :---- | :---- |
| **Etiqueta** | Identificador de la solicitud de traducción |
| **Etiqueta en la base de datos** | Identificador de la solicitud de traducción |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Solicitud de traducción. |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | NO |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tirada |
| :---- | :---- |
| **Etiqueta** | Tirada |
| **Etiqueta en la base de datos** | Tirada Tirada (estado) |
| **Tipo de campo en base de datos** | Tirada: [Número (entero)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_tirada/storage) Tirada (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Número de ejemplares previstos para la publicación. |
| **Tratamiento documental** | Número entero positivo (xsd:positiveInteger). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original.  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Extensión (5.1) |
| :---- | :---- |
| **Etiqueta** | Volúmenes y páginas |
| **Etiqueta en la base de datos** | Volúmenes y páginas Volúmenes y páginas (estado) |
| **Tipo de campo en base de datos** | Volúmenes y páginas: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Volúmenes y páginas (estado): Taxonomía |
| **Esquema de metadatos de origen** | ISBD Edición Consolidada https://www.ifla.org/wp-content/uploads/2019/05/assets/hq/publications/series/44-es.pdf |
| **Definición** | Extensión: Número de unidades y/o subunidades que componen el recurso, ej. Los volúmenes- y/o páginas de un texto impreso. |
| **Tratamiento documental** | Designación específica del material (coincide con el elemento “5.1.2 Designación específica del material”): Ordinal de volúmenes expresado con el tipo de datos xsd:integer. Ejemplos: 1 v.; 3 v. Paginación (coincide con el elemento “5.1.4 Paginación”).  Si “Designación específica del material” incluye un solo volumen, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.1 Recursos en una unidad física”. Ejemplo: 327 p. 321 hojas 80 p. Nota: Verso de las páginas en blanco 56 hojas Nota: Hojas impresas por ambas caras  Si “Designación específica del material” incluye dos o más volúmenes, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.2 Recursos en más de una unidad física”. Ejemplos: 3 v. (vi, 310 p.; vi, 434 p.; viii, 492 p.)  3 v. (vi, 310 p., 20 hojas de láminas; viii, 432 p., 32 hojas de láminas; x, 490 p., 52 hojas de láminas) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD:** El SGBD tiene que tratarlo como un atributo compuesto (“composite attribute”): “An attribute that can be further subdivided to yield additional attributes. For example, a phone number such as 615-898-2368 may be divided into an area code (615), an exchange number (898), and a four-digit code (2368). Compare to simple attribute.” En el atributo principal se situará “Serie”. En los atributos adicionales se situarán: 5.1.2 Designación específica del material  5.1.4 Paginación |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | “Etiquetas del Formato MARC 21, en el que se indican los elementos descriptivos de las diferentes áreas (ISBD-G)”: (Fernández Porcel & Zaborras, 2010): 300\#\#|aExtensión y designación física del material :|bMención de otras características físicas ;|cDimensiones \+|eMaterial anejo  MARC to Dublin Core Crosswalk [https://www.loc.gov/marc/marc2dc.html](https://www.loc.gov/marc/marc2dc.html).  MARC to Dublin Core Crosswalk (Qualified): dcterms:extent (parcialmente, 300$a) |

| nombre\_del\_atributo | dcterms:format |
| :---- | :---- |
| **Etiqueta** | Format |
| **Etiqueta en la base de datos** | Formato Formato (estado) |
| **Tipo de campo en base de datos** | Formato: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Formato (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Dimensiones del libro. Corresponde al campo “Formato” en la solicitud de publicación. |
| **Tratamiento documental** | **TODO Ivan/Miquel** Vocabulario controlado de dimensiones. Si lo localizamos y las designaciones son aplicables a las explicaciones de los expedientes. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 12 x 17 cm |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | **TODO Miquel**: Analizar la correspondencia una vez definido correctamente “formato”. |

| nombre\_del\_atributo | dcterms:type |
| :---- | :---- |
| **Etiqueta** | Carácter |
| **Etiqueta en la base de datos** | Carácter de la publicación Carácter de la publicación (estado) |
| **Tipo de campo en base de datos** | Carácter de la publicación: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Carácter de la publicación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Género en sentido amplio. Corresponde al campo “Carácter” en la solicitud de publicación. |
| **Tratamiento documental** | Vocabulario libre. Valor que aparece en el documento original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | clase\_de\_impreso |
| :---- | :---- |
| **Etiqueta** | Clase de impreso |
| **Etiqueta en la base de datos** | Clase de impreso Clase de impreso (estado) |
| **Tipo de campo en base de datos** | Clase de impreso: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Clase de impreso (estado): taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Corresponde al campo “Clase de impreso” en la solicitud de traducción. |
| **Tratamiento documental** | Un valor extraído de un vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO Ivan/Miquel** Vocabulario controlado de clases de impresos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | Libro |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Fecha (M1810) |
| :---- | :---- |
| **Etiqueta** | \<DOC\_FECHA\> |
| **Etiqueta en la base de datos** | Fecha de presentación de la solicitud de traducción Fecha de presentación de la solicitud de traducción (estado) |
| **Tipo de campo en base de datos** | Fecha de presentación de la solicitud de traducción: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_datesingle/storage)  Fecha de presentación de la solicitud de traducción (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Fecha de emisión de la solicitud de traducción. |
| **Tratamiento documental** | Patrón de fechas: DD-MM-AAAA  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Se consignará la fecha que aparezca en la documentación original.  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAD [https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html](https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html): unitdate ISAD(G) [https://cultura.gencat.cat/web/.content/dgpc/arxius\_despublicada/norma\_de\_descripcio\_arxivistica\_de\_catalunya/arxius/isad2\_catala.pdf](https://cultura.gencat.cat/web/.content/dgpc/arxius_despublicada/norma_de_descripcio_arxivistica_de_catalunya/arxius/isad2_catala.pdf): 3.1.3 MARC 245 subfield f for inclusive dates, 245 subfield g for bulk dates, or 260 subfield c MODS [https://www.loc.gov/standards/mods/mods-outline-3-7.html](https://www.loc.gov/standards/mods/mods-outline-3-7.html): \<originInfo\>\<dateCreated\> |

| nombre\_del\_atributo | observaciones |
| :---- | :---- |
| **Etiqueta** | Observaciones |
| **Etiqueta en la base de datos** | Observaciones Observaciones (estado) |
| **Tipo de campo en base de datos** | Observaciones: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) Observaciones (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en solicitud de traducción. |
| **Tratamiento documental** | Vocabulario libre. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original, mediante transcripción. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos. Tipo de campo en Drupal: Texto(sin formato) |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_contributor/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | El valor se da tal y como aparece en el documento original, mediante transcripción. Un valor muy frecuente es Nulo. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos.  |
| **Instrucciones para la entrada de datos (otras que las dadas en Tratamiento documental)** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

\[Entre Solicitud de traducción y Editor\] Tiene como editor solicitante

* S’incorpora aquesta relació.   
* Camp del tipus:  n\_to\_m\_relation  
* És obligatori

\[Entre Editor y Solicitud de traducción\] Es solicitante de

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Tiene como editor solicitante”

# Entidad *Solicitud de circulación*

| nombre\_del\_atributo | ID\_Solicitud\_Circulacion |
| :---- | :---- |
| **Etiqueta** | Identificador de la solicitud de circulación |
| **Etiqueta en la base de datos** | Identificador de la solicitud de circulación |
| **Tipo de campo en base de datos** | [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/published_book/fields/node.published_book.field_identificador_del_libro_pu/storage) |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Clave principal de cada registro de la entidad Solicitud de circulación. |
| **Tratamiento documental** | Se asigna un único valor a cada registro de forma automática. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD**: El SGBD asignará un valor a cada registro de forma automática a partir de un patrón. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | NO |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | tirada |
| :---- | :---- |
| **Etiqueta** | Tirada |
| **Etiqueta en la base de datos** | Tirada Tirada (estado) |
| **Tipo de campo en base de datos** | Tirada: [Número (entero)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_tirada/storage) Tirada (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Número de ejemplares previstos para la publicación. |
| **Tratamiento documental** | Número entero positivo (xsd:positiveInteger). |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | El valor se da tal y como aparece en el documento original.  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Tirada |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Extensión (5.1) |
| :---- | :---- |
| **Etiqueta** | Volúmenes y páginas |
| **Etiqueta en la base de datos** | Volúmenes y páginas Volúmenes y páginas (estado) |
| **Tipo de campo en base de datos** | Volúmenes y páginas: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Volúmenes y páginas (estado): Taxonomía |
| **Esquema de metadatos de origen** | ISBD Edición Consolidada https://www.ifla.org/wp-content/uploads/2019/05/assets/hq/publications/series/44-es.pdf |
| **Definición** | Extensión: Número de unidades y/o subunidades que componen el recurso, ej. Los volúmenes- y/o páginas de un texto impreso. |
| **Tratamiento documental** | Designación específica del material (coincide con el elemento “5.1.2 Designación específica del material”): Ordinal de volúmenes expresado con el tipo de datos xsd:integer. Ejemplos: 1 v.; 3 v. Paginación (coincide con el elemento “5.1.4 Paginación”).  Si “Designación específica del material” incluye un solo volumen, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.1 Recursos en una unidad física”. Ejemplo: 327 p. 321 hojas 80 p. Nota: Verso de las páginas en blanco 56 hojas Nota: Hojas impresas por ambas caras  Si “Designación específica del material” incluye dos o más volúmenes, se incluye el número de páginas la descripción puede seguir las directrices del subelemento “5.1.4.2 Recursos en más de una unidad física”. Ejemplos: 3 v. (vi, 310 p.; vi, 434 p.; viii, 492 p.)  3 v. (vi, 310 p., 20 hojas de láminas; viii, 432 p., 32 hojas de láminas; x, 490 p., 52 hojas de láminas) |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | **TODO SGBD:** El SGBD tiene que tratarlo como un atributo compuesto (“composite attribute”): “An attribute that can be further subdivided to yield additional attributes. For example, a phone number such as 615-898-2368 may be divided into an area code (615), an exchange number (898), and a four-digit code (2368). Compare to simple attribute.” En el atributo principal se situará “Serie”. En los atributos adicionales se situarán: 5.1.2 Designación específica del material  5.1.4 Paginación |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | “Etiquetas del Formato MARC 21, en el que se indican los elementos descriptivos de las diferentes áreas (ISBD-G)”: (Fernández Porcel & Zaborras, 2010): 300\#\#|aExtensión y designación física del material :|bMención de otras características físicas ;|cDimensiones \+|eMaterial anejo  MARC to Dublin Core Crosswalk [https://www.loc.gov/marc/marc2dc.html](https://www.loc.gov/marc/marc2dc.html).  MARC to Dublin Core Crosswalk (Qualified): dcterms:extent (parcialmente, 300$a) |

| nombre\_del\_atributo | dcterms:format |
| :---- | :---- |
| **Etiqueta** | Format |
| **Etiqueta en la base de datos** | Formato Formato (estado) |
| **Tipo de campo en base de datos** | Formato: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Formato (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Dimensiones del libro. Corresponde al campo “Formato” en la solicitud de circulación. |
| **Tratamiento documental** | **TODO Ivan/Miquel** Vocabulario controlado de dimensiones. Si lo localizamos y las designaciones son aplicables a las explicaciones de los expedientes. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** | 12 x 17 cm |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Formato_estado |
| **Equivalencias con otros esquemas** | **TODO Miquel**: Analizar la correspondencia una vez definido correctamente “formato”. |

| nombre\_del\_atributo | dcterms:type |
| :---- | :---- |
| **Etiqueta** | Carácter |
| **Etiqueta en la base de datos** | Carácter de la publicación Carácter de la publicación (estado) |
| **Tipo de campo en base de datos** | Carácter de la publicación: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/publication/fields/node.publication.field_extension/storage) Carácter de la publicación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Dublin Core Terms https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| **Definición** | Género en sentido amplio. Corresponde al campo “Carácter” en la solicitud de circulación. |
| **Tratamiento documental** | Vocabulario libre. Valor que aparece en el documento original. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | fecha\_entrada\_solicitud\_circulacion |
| :---- | :---- |
| **Etiqueta** | Fecha de entrada de solicitud de circulación |
| **Etiqueta en la base de datos** | Fecha de entrada de solicitud de circulación Fecha de entrada de solicitud de circulación (estado) |
| **Tipo de campo en base de datos** | Fecha de entrada de solicitud de circulación: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_entry_date/storage) Fecha de entrada de solicitud de circulación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Fecha de entrada tal y como consta en la solicitud de circulación original. |
| **Tratamiento documental** | Patrón de fechas: AAAA-MM-DD |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | NO |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | fecha\_de\_salida\_solicitud\_circulacion |
| :---- | :---- |
| **Etiqueta** | Fecha de salida de solicitud de circulación |
| **Etiqueta en la base de datos** | Fecha de salida de solicitud de circulación Fecha de salida de solicitud de circulación (estado) |
| **Tipo de campo en base de datos** | Fecha de salida de solicitud de circulación: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_entry_date/storage) Fecha de salida de solicitud de circulación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Fecha de salida tal y como consta en la solicitud de circulación original. |
| **Tratamiento documental** | Patrón de fechas: AAAA-MM-DD |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** |  |
| **Obligatoriedad** | No. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Repetibilidad** | NO |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Caracter_de_la_publicacion_estado |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | Fecha (M1810) |
| :---- | :---- |
| **Etiqueta** | \<DOC\_FECHA\> |
| **Etiqueta en la base de datos** | Fecha de edición Fecha de edición (estado) |
| **Tipo de campo en base de datos** | Fecha de edición: [Fecha](https://censurarusa.enproves.net/admin/structure/types/manage/censorship_file/fields/node.censorship_file.field_datesingle/storage)  Fecha de edición (estado): Taxonomía  |
| **Esquema de metadatos de origen** | *NEDA-MC: modelo conceptual de descripción archivística Ministerio de Educación, Cultura y Deporte* https://www.libreria.culturaydeporte.gob.es/libro/neda-mc-modelo-conceptual-de-descripcion-archivistica-entidades-relaciones-y-atributos\_3978/ |
| **Definición** | Fecha de edición prevista. |
| **Tratamiento documental** | Patrón de fechas: DD-MM-AAAA  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Se consignará la fecha que aparezca en la documentación original.  |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Repetibilidad** | No |
| **Indexación** | Sí. La indización debe permitir la búsqueda por componentes de las fechas (por ejemplo, mes y año), por intervalos de fechas, etc. |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** | EAD [https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html](https://www.loc.gov/ead/EAD3taglib/EAD3-TL-eng.html): unitdate ISAD(G) [https://cultura.gencat.cat/web/.content/dgpc/arxius\_despublicada/norma\_de\_descripcio\_arxivistica\_de\_catalunya/arxius/isad2\_catala.pdf](https://cultura.gencat.cat/web/.content/dgpc/arxius_despublicada/norma_de_descripcio_arxivistica_de_catalunya/arxius/isad2_catala.pdf): 3.1.3 MARC 245 subfield f for inclusive dates, 245 subfield g for bulk dates, or 260 subfield c MODS [https://www.loc.gov/standards/mods/mods-outline-3-7.html](https://www.loc.gov/standards/mods/mods-outline-3-7.html): \<originInfo\>\<dateCreated\> |

| nombre\_del\_atributo | resolucion\_solicitud\_circulacion |
| :---- | :---- |
| **Etiqueta** | Resolución de la solicitud de circulación |
| **Etiqueta en la base de datos** | Resolución de la solicitud de circulación Resolución de la solicitud de circulación (estado) |
| **Tipo de campo en base de datos** | Resolución de la solicitud de circulación: [Referencia de entidad](https://censurarusa.enproves.net/admin/structure/types/manage/solicitud_de_circulacion/fields/node.solicitud_de_circulacion.field_resolucion_solicitud_circu/storage) Resolución de la solicitud de circulación (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Resolución definitiva de la solicitud de circulación. |
| **Tratamiento documental** | Vocabulario controlado. |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | Un valor a elegir entre los siguientes: Autorizado  Autorizado con condiciones Prohibido Otros Notas de aplicación de los valores. El valor “Autorizado” puede significar autorizada la importación o la publicación, según el caso. El valor “Otros” se concreta en el atributo ***observaciones\_usuarios\_proyecto***. |
| **Obligatoriedad** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. Si todavía no se ha incorporado la resolución, se introduce el valor “Pendiente”. |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **Equivalencias con otros esquemas** |  |

| nombre\_del\_atributo | matiz\_politico |
| :---- | :---- |
| **Etiqueta** | Matiz político |
| **Etiqueta en la base de datos** | Matiz político Matiz político (estado) |
| **Tipo de campo en base de datos** | Matiz político: [Texto (sin formato)](https://censurarusa.enproves.net/admin/structure/types/manage/analyzed_book/fields/node.analyzed_book.field_contributor/storage) Matiz político (estado): Taxonomía  |
| **Esquema de metadatos de origen** | Local |
| **Definición** | Contenido del campo correspondiente en el formulario, tal y como ha sido cumplimentado por el lector encargado de la valoración de la obra. |
| **Tratamiento documental** | El valor se da tal y como aparece en el documento original, mediante transcripción. Un valor muy frecuente es Nulo. En caso que el formulario original no contenga esta información, se deja blanco en la base de datos.  |
| **Instrucciones para la entrada de datos (otras que las dadas en *Tratamiento documental*)** | No. En caso que no sea legible, se incorpora el valor “No legible”. En caso que no esté disponible, se incorpora el valor “No disponible”. |
| **Obligatoriedad** | Sí |
| **Repetibilidad** | No |
| **Indexación** | Sí |
| **Ejemplos** |  |
| **Comentarios** |  |
| **posible name property desde los diagramas** | Mota_Politico |
| **Equivalencias con otros esquemas** |  |

\[Entre Solicitud de circulación y Editor\] Tiene como editor solicitante

* S’incorpora aquesta relació.   
* Camp del tipus:  n\_to\_m\_relation  
* És obligatori

\[Entre Editor y Solicitud de circulación\] Es solicitante de

* Aquesta relació no s’incorpora perquè s’infereix a partir de “Tiene como editor solicitante”

