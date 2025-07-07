# Database Schema: A Relational Approach

This document outlines the relational model of the Censura database, designed to manage the process of censorship, publication, and importation of literary works. The structure is centered around a main entity, `EXPEDIENTES`, which acts as a central hub connecting various processes and entities.

## Core Concepts

The database is structured around a few core entities, from which most other data tables are derived.

### 1. `EXPEDIENTES` (Dossiers)

This is the central entity of the model. Each `EXPEDIENTE` represents a complete dossier for a book, tracking it from its initial submission to its final publication and beyond. It links together information about the book itself, censorship reports, import requests, and publication details.

### 2. `AUTOR` (Authors) and `LIBROS` (Books)

-   **AUTOR**: Stores information about the authors.
-   **LIBROS_PRESENTADOS** & **LIBROS_PUBLICADOS**: These tables store details about books, differentiating between those that are submitted (`PRESENTADOS`) and those that are officially published (`PUBLICADOS`).
-   **Junction Tables**: `AUTOR_LIBROS_PRESENTADOS` and `AUTOR_LIBROS_PUBLICADOS` are junction tables that create a many-to-many relationship between authors and books, allowing a book to have multiple authors and an author to have multiple books.

### 3. Censorship and Review Process

-   **LECTORES**: Contains information about the reviewers or "readers" who assess the books.
-   **INFORMES_DE_LECTORES**: Each record is a report filed by a reader, linked to a specific `EXPEDIENTE`.
-   **TACHADURAS_Y_ENMIENDAS**: "Redactions and Amendments". This table details specific censorship actions taken within a report.
-   **FIRMAS_LECTORES**: Stores signatures from the readers, linked to the readers themselves.

### 4. Importation and Publication Process

-   **SOLICITUDES_DE_IMPORTACION**: This extensive table manages requests to import books. It contains a wealth of detail about the book's physical characteristics (paper type, size, etc.) and the commercial aspects of the importation. It is directly linked to an `EXPEDIENTE`.
-   **IMPORTADORES**, **EDITORES**, **PROVEEDORES_DEL_PAPEL**: These tables manage the entities involved in the importation and publication supply chain: importers, editors, and paper suppliers.
-   **Link Tables**: The model uses several link tables (e.g., `SOLICITUDES_IMPORTACION_COLECCION`, `SOLICITUDES_PUBLICACION_EDITORES`) to manage the many-to-many relationships between a publication/importation request and the various entities involved.

## Relational Integrity

The model heavily relies on **foreign keys (FK)** to maintain relational integrity. The `FK` fields in each table link back to the primary key (PK) of another table, creating a well-structured and interconnected web of data.

For example:
-   `LIBROS_PUBLICADOS.FK_idExpediente` links a published book back to its main dossier in `EXPEDIENTES`.
-   `INFORME_LECTOR_LECTORES` links a specific report (`FK_InformeLector`) with a specific reader (`FK_idLector`), demonstrating how junction tables are used to resolve many-to-many relationships.
-   The various `_EN_OTRAS_BASES_DE_DATOS` tables are designed to link entities within this database to external data sources, using a URL as a primary key.

## Summary

This relational model is designed to be a comprehensive system for tracking the lifecycle of a book through a state-controlled censorship and publication process. By centralizing information around the `EXPEDIENTES` table and using junction tables to manage complex relationships, the database provides a robust and scalable way to manage a large amount of interconnected information.

## Integration with Wikidata Properties

This database can be significantly enriched by linking its entities to Wikidata, a free and open knowledge base. Using Wikidata properties would allow for the integration of standardized, multilingual, and interconnected data, enhancing the overall value of the information stored.

Below are some key entities from this database and the corresponding Wikidata properties that could be used to augment them.

### **`AUTOR` (Author)**
-   **[P21](https://www.wikidata.org/wiki/Property:P21)**: `sex or gender` (to complement `Genero_autor`).
-   **[P735](https://www.wikidata.org/wiki/Property:P735)**: `given name` & **[P734](https://www.wikidata.org/wiki/Property:P734)**: `family name` (for a more granular name structure than `Titulo_nombre_autor`).
-   **[P569](https://www.wikidata.org/wiki/Property:P569)**: `date of birth` & **[P570](https://www.wikidata.org/wiki/Property:P570)**: `date of death`.
-   **[P27](https://www.wikidata.org/wiki/Property:P27)**: `country of citizenship`.
-   **[P106](https://www.wikidata.org/wiki/Property:P106)**: `occupation` (e.g., "novelist," "poet," "journalist").
-   **[P19](https://www.wikidata.org/wiki/Property:P19)**: `place of birth` & **[P20](https://www.wikidata.org/wiki/Property:P20)**: `place of death`.

### **`LIBROS_PUBLICADOS` (Published Book)**
-   **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (e.g., "novel," "anthology," "non-fiction book").
-   **[P50](https://www.wikidata.org/wiki/Property:P50)**: `author` (linking to the author's Wikidata item).
-   **[P1476](https://www.wikidata.org/wiki/Property:P1476)**: `title` (to store the original or official title).
-   **[P577](https://www.wikidata.org/wiki/Property:P577)**: `publication date`.
-   **[P407](https://www.wikidata.org/wiki/Property:P407)**: `language of work or name` (linking to a language's Wikidata item).
-   **[P123](https://www.wikidata.org/wiki/Property:P123)**: `publisher` (linking to the publisher's Wikidata item).
-   **[P212](https://www.wikidata.org/wiki/Property:P212)**: `ISBN-13` & **[P957](https://www.wikidata.org/wiki/Property:P957)**: `ISBN-10` (for standardized book identification).
-   **[P921](https://www.wikidata.org/wiki/Property:P921)**: `main subject` (to describe the primary topics of the book).
-   **[P361](https://www.wikidata.org/wiki/Property:P361)**: `part of` (if the book belongs to a larger work or series).

### **`EDITORES` (Publisher)**
-   **[P159](https://www.wikidata.org/wiki/Property:P159)**: `headquarters location`.
-   **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country`.
-   **[P571](https://www.wikidata.org/wiki/Property:P571)**: `inception` (date of establishment).
-   **[P856](https://www.wikidata.org/wiki/Property:P856)**: `official website`.

### **`IDIOMA` (Language)**
-   **[P424](https://www.wikidata.org/wiki/Property:P424)**: `Wikimedia language code` (e.g., "es" for Spanish, "en" for English).
-   **[P220](https://www.wikidata.org/wiki/Property:P220)**: `language family`.

### Implementation Approach
To implement this, new columns could be added to the existing tables to store the Wikidata Q-identifiers (e.g., a `wikidata_id` column in the `AUTOR` table). This would create a robust link between the internal database records and the vast, interconnected data available on Wikidata, opening up new possibilities for data analysis and discovery.

### **Wikidata Properties for Wars and Conflicts**
To extend the database to include contextual information about historical conflicts, such as civil wars, the following Wikidata properties are essential. This would be particularly relevant if a book or author is associated with a specific conflict.

-   **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` - Used to classify the event (e.g., "war," "battle," "civil war," "military conflict").
-   **[P607](https://www.wikidata.org/wiki/Property:P607)**: `participated in conflict` - A key property to link a person (like an `AUTOR`) or a military unit to a specific conflict.
-   **[P361](https://www.wikidata.org/wiki/Property:P361)**: `part of` - To indicate that a specific battle or event is part of a larger war.
-   **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country` - The country where the conflict primarily takes place.
-   **[P276](https://www.wikidata.org/wiki/Property:P276)**: `location` - For more specific geographical locations of battles or events within a war.
-   **[P580](https://www.wikidata.org/wiki/Property:P580)**: `start time` & **[P582](https://www.wikidata.org/wiki/Property:P582)**: `end time` - To define the duration of the conflict.
-   **[P710](https://www.wikidata.org/wiki/Property:P710)**: `participant` - To list the main belligerents in a conflict (e.g., countries, armed groups).
-   **[P1120](https://www.wikidata.org/wiki/Property:P1120)**: `number of deaths` - To record the human cost of the conflict.
-   **[P2348](https://www.wikidata.org/wiki/Property:P2348)**: `time period` - To link the conflict to a broader historical era.
-   **[P1264](https://www.wikidata.org/wiki/Property:P1264)**: `valid in period` - To specify the time period in which the information is valid.
-   **[P457](https://www.wikidata.org/wiki/Property:P457)**: `foundational text` - Can be used to link to peace treaties or declarations of war.

By creating a new table, for instance `CONFLICTOS`, with columns corresponding to these properties, one could effectively model historical events and link them to the books and authors in the existing schema, providing deep contextual background.

#### Example of Use: George Orwell in the Spanish Civil War

To model the fact that George Orwell participated in the Spanish Civil War—an experience he famously documented in his memoir *Homage to Catalonia*—you would use two separate Wikidata items connected by the properties:

1.  **On George Orwell's Item ([Q3335](https://www.wikidata.org/wiki/Q3335))**:
    -   You would add the property **`participated in conflict` ([P607](https://www.wikidata.org/wiki/Property:P607))**.
    -   The value for this property would be a link to the Wikidata item for the **Spanish Civil War ([Q10859](https://www.wikidata.org/wiki/Q10859))**.

2.  **On the Spanish Civil War's Item ([Q10859](https://www.wikidata.org/wiki/Q10859))**:
    -   This item has the property **`instance of` ([P31](https://www.wikidata.org/wiki/Property:P31))**.
    -   The value for this property is **`civil war` ([Q8465](https://www.wikidata.org/wiki/Q8465))**.

This two-step structure allows for immense flexibility. The same `participated in conflict` property can link an individual to any military event, while the specific nature of that event (e.g., a civil war, a world war, or a specific battle) is defined on the event's own Wikidata page.

#### Example of Use: Francisco Franco and the Francoist Dictatorship

Here is how to model the relationship between a head of state and the historical period of their rule:

1.  **On Francisco Franco's Item ([Q29179](https://www.wikidata.org/wiki/Q29179))**:
    -   One would add the property **`head of state` ([P35](https://www.wikidata.org/wiki/Property:P35))**.
    -   The value for this property would be a link to the Wikidata item for **Francoist Spain ([Q13474305](https://www.wikidata.org/wiki/Q13474305))**.

2.  **On Francoist Spain's Item ([Q13474305](https://www.wikidata.org/wiki/Q13474305))**:
    -   This item has the property **`instance of` ([P31](https://www.wikidata.org/wiki/Property:P31))**, with values like `historical country` or `historical period`.
    -   It also has its own **`head of state` ([P35](https://www.wikidata.org/wiki/Property:P35))** property, with the value pointing back to **Francisco Franco ([Q29179](https://www.wikidata.org/wiki/Q29179))**.

This demonstrates how Wikidata creates a reciprocal link, defining the person's role in the historical period and, conversely, defining the head of state for that period. 