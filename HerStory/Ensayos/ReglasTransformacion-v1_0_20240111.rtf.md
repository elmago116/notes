**Reglas básicas de transformación de bases de datos relacionales en bases de datos RDF**

# Primera parte de la transformación: Generación de la ontología a partir de las tablas y columnas del esquema de la base de datos relacional.

| Esquema de la base de datos relacional | Ontología para el conjunto de datos RDF |
| ----- | ----- |
| ***Regla 1: Tabla no asociativa*** ¿Cómo la identificamos? Cuando una tabla contiene solo una clave primaria o cuando la tabla contiene columnas de clave primaria que no son claves foráneas de otras dos tablas distintas. Por ejemplo: ***FOTOGRAFÍAS*** | Cada tabla no asociativa se asigna a una clase ontológica. El nombre de la clase se construye así: a) comienza con una letra mayúscula y b) incorpora el nombre de la entidad correspondiente en el diseño lógico, preferentemente en singular. Es necesario identificarla con un URI/IRI diseñado de acuerdo con la estrategia de designación de recursos. Por ejemplo: ***mcv-ont:Fotografía*** |

| Esquema de la base de datos relacional | Ontología para el conjunto de datos RDF |
| :---- | ----- |
| ***Regla 2: Tabla de vínculo o asociativa*** ¿Cómo la identificamos? Cuando sus columnas de clave primaria son únicamente claves foráneas de dos otras tablas. Por ejemplo: ***FOTO\_MATERIA*** | **Opción 1: La tabla asociativa no incluye más columnas que las claves foráneas.** Paso 1: Mapeamos las columnas de las claves foráneas a dos propiedades de objeto. El nombre de la primera propiedad de objeto se construye así: a) comienza con el valor fijo *has* (o *tiene* o *te…*) con letra minúscula; y b) continúa con el nombre del atributo correspondiente en el diseño lógico que comienza con letra mayúscula, y preferentemente en singular. Por ejemplo: ***mcv- ont:tieneDescriptor***. El segundo nombre de la propiedad de objeto se construye así: a) comienza con el valor fijo *is* (o *es*…) con letra minúscula; b) continúa con el nombre del atributo correspondiente en el diseño lógico que comienza con letra mayúscula; y c) finaliza con el valor fijo *Of* (o *De*…) con la primera letra mayúscula. Por ejemplo: ***mcv-ont:esDescriptorDe***. Es necesario identificarlas con un URI/IRI diseñado de acuerdo con el patrón establecido en la estrategia de designación de recursos. Paso 2: Para cada propiedad de objeto se especifica la cardinalidad mínima. Paso 3: Las dos propiedades de tipo objeto se declaran inversas entre ellas. Paso 4: Las restricciones de dominio y de rango se asignan a la primera propiedad de objeto. Restricción de dominio (*rdfs:domain*): Se especifica utilizando la clase correspondiente a la tabla que contiene la clave foránea. Restricción de rango (*rdfs:range*): Se especifica utilizando la clase de la tabla que contiene la clave principal vinculada a la clave foránea de la otra tabla. |

|  |  |
| :---- | :---- |
|  | **Opción 2: La tabla asociativa incluye más columnas que las claves foráneas.** Aplicamos los cuatro pasos mencionados en la Opción 1, y, además, los dos pasos adicionales siguientes. Paso 5: Creamos una clase para la tabla no asociativa, de acuerdo con la **Regla 1**. Paso 6: Creamos una propiedad de tipo de dato para cada columna que no es clave primaria, de acuerdo con la **Regla 3**. |

| Esquema de la base de datos relacional | Ontología para el conjunto de datos RDF |
| :---- | ----- |
| ***Regla 3: Columna*** del tipo clave foránea en tablas no asociativas o principales. Por ejemplo: en la tabla ***FOTOGRAFÍAS***, la columna ***Fotógrafo***, que contiene las claves foráneas de la tabla ***FOTÓGRAFOS*** con la que se relaciona. | **Dos propiedades del tipo *owl:ObjectProperty*** Paso 1: Las columnas que contienen claves foráneas se mapean a dos propiedades de objeto con los siguientes nombres. El nombre de la **primera propiedad de objeto** se construye así: a) comienza con el valor fijo *has* (o *tiene* o *te…*) con letra minúscula; y b) continúa con el nombre del atributo correspondiente en el diseño lógico que comienza con letra mayúscula y preferentemente en singular. Por ejemplo, El segundo nombre de la **segunda propiedad de objeto** se construye así: a) comienza con el valor fijo *is* (o *es*…) con letra minúscula; b) continúa con el nombre del atributo correspondiente en el diseño lógico que comienza con letra mayúscula; y c) finaliza con el valor fijo *of* (o *de*…) con letra mayúscula. Es necesario identificarlas con un URI/IRI diseñado de acuerdo con el patrón establecido en la estrategia de designación de recursos. Paso 2: Cada propiedad de objeto se declara como funcional. Paso 3: Las dos propiedades de objeto se declaran inversas entre ellas. Paso 4: El dominio y rango se asignan a la primera propiedad de objeto. La restricción de dominio (*rdfs:domain*) será la clase correspondiente a la tabla del esquema relacional que contiene las claves foráneas. Por ejemplo, para la propiedad ***mcv-ont:tieneFotógrafo***, la restricción de dominio será la clase ***mcv-ont:Fotografía***. La restricción de rango (*rdfs:range*) será la clase correspondiente a la tabla del esquema relacional a la que se refieren las claves foráneas. Por ejemplo, para la propiedad ***mcv-ont:tieneFotógrafo***, la restricción de rango será la clase ***mcv- ont:Fotógrafo***. |

|  | Es necesario identificarlas con un URI/IRI diseñado de acuerdo con el patrón establecido en la estrategia de designación de recursos. Paso 5: Cada propiedad de objeto tendrá asignada una restricción de cardinalidad mínima. |
| :---- | :---- |

| Esquema de la base de datos relacional | Ontología para el conjunto de datos RDF |  |
| ----- | ----- | :---- |
| ***Regla 4:*** Columna de tipo diferente a clave foránea, primaria o única, o restricción de verificación (***check constraint***). | **Opción 1:** Tras el análisis de los valores de las celdas, llegamos a la conclusión que NO pueden convertirse en entidades diferenciadas e independientes de la entidad que describen que en la base de datos relacional. Por ejemplo: La columna ***Año de producción*** incluye como valores los años en que las películas fueron producidas. Estos valores son relevantes ÚNICAMENTE para la descripción de las ocurrencias de la tabla PELÍCULA. | ***Se transformará en una propiedad del tipo owl:DatatypeProperty*** Paso 1: La columna se mapea a una única propiedad de datos. Para generar el nombre local utilizamos el atributo correspondiente en el diseño lógico con la primera letra en minúscula. Es necesario identificarlas con un URI/IRI diseñado de acuerdo con el patrón establecido en la estrategia de designación de recursos. Por ejemplo: ***mcv-ont:anyoToma*** Paso 2: El dominio y rango se asignan a una de las propiedades de objeto. La restricción de dominio (*rdfs:domain*) será la clase correspondiente a la tabla del esquema relacional que contiene la columna. Por ejemplo, para la propiedad ***mcv-ont:anyoToma*** la restricción de dominio será la clase ***mcv-ont:Fotografía***. La restricción de rango (*rdfs:range*) será el tipo de datos que mejor representa a los valores de la columna en el esquema relacional. Por ejemplo, para la propiedad ***mcv-ont:anyoToma*** el tipo de datos que mejor representa sus valores |

|  |  | es *xsd:gYear*. Sobre el mapeo entre tipos de datos SQL y XSD, véase el Anexo 1\. |
| :---- | :---- | :---- |
|  | **Opción 2:** Tras el análisis de los valores de las celdas, llegamos a la conclusión que contienen referencias a entidades que, además de describir la entidad de cada fila, pueden tener una existencia diferenciada e independiente en el contexto del dominio de la base de datos. Por ejemplo: La columna ***imagenDigital*** incluye como valores las URI de las imágenes resultantes de la digitalización. Estos valores se refieren a una entidad que tiene una existencia diferenciada e independiente en el dominio de la colección fotográfica; por ejemplo, podemos tener metadatos técnicos, descriptivos, etc. | ***Se transformará en d*****os propiedades del tipo *owl:ObjectProperty Seguiremos los pasos y requerimientos de la Regla 3, por lo que respecta la declaración de las propiedades, y de la Regla*** Por ejemplo: ***mcv:imagenDigital*** La restricción de dominio (*rdfs:domain*) será la clase correspondiente a la tabla del esquema relacional que contiene la columna. Por ejemplo, para la propiedad ***mcv-ont:imagenDigital***, la restricción de dominio será la clase ***mcv-ont:Fotografía***. Para la restricción de rango (*rdfs:range*), será necesario definir una nueva clase relativa a los valores de la columna objeto de transformación, que no existe en el esquema de la base de datos relacional. Por ejemplo, para la propiedad ***mcv- ont:imagenDigital*** definiremos la nueva clase ***mcv-ont:ImageDigital***. |

| Esquema de la base de datos relacional | Ontología para el conjunto de datos RDF |
| :---- | ----- |
| **Regla 5:** La especificación del modelo ER establece que ninguna entidad se superpone. | Definición del axioma de disyunción entre todas las clases creadas en las Reglas 1 a 4, mediante el constructo ***owl:disjointWith***. |

# Anexo 1: Mapeo de tipos de datos de SQL a XSD

| Tipos de datos SQL | Tipos de datos XSD |
| :---- | :---- |
| **Number** |  |
| Decimal, Numeric | Decimal |
| Real | Float |
| Float | Double |
| Integer, Int | Integer, positiveInteger, negativeInteger |
| BigInt | Long |
| SmallInt | Short |
| TinyInt | UnsignedByte |
| **Character, string** |  |
| Char, VarChar | String |
| Nchar, nvarchar, text, ntext String | String |
| **Date, Time** |  |
| DateTime | DateTime |
| Date | Data |
| Time | Time |
| **Other data types** |  |
| Binary, VarBinary | Base64Binary |
| Bit | Boolean |
| Variant | anyType |
| Interval | Duration |

Fuentes

Huve, Cristiane Aparecida Gonçalves. (2017). *An architecture for mapping relational database to ontology* \[Dissertation presented as partial requirement to obtain a master’s degree.\]. Federal University of Paraná.

Huve, Cristiane, Porn, Alex, & Peres, Leticia. (2019). Architecture for Mapping Relational Database to OWL Ontology: An Approach to Enrich Ontology Terminology Validated with Mutation Test: *Proceedings of the 21st International Conference on Enterprise Information Systems*, 320-  
327\. [https://doi.org/10.5220/0007752803200327](https://doi.org/10.5220/0007752803200327)

Michel, F., Montagnat, J., y Faron-Zucker, C. (2014). *A survey of RDB to RDF translation approaches and tools* . Sophia Antipolis. Recuperado de [http://www.w3.org/TR/sparql11-overview](http://www.w3.org/TR/sparql11-overview)

Zhao, Z., Han, S., y Kim, J. (2019). “R2LD: Schema-based Graph Mapping of relational databases to Linked Open Data for multimedia resources data”. *Multimedia tools and applications*, 78(20), 28835–28851. [https://doi.org/10.1007/s11042-019-7281-5](https://doi.org/10.1007/s11042-019-7281-5)