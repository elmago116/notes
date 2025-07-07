# SIDBRINT Database Schema: A Relational Approach

This document outlines the relational model of the SIDBRINT database, designed to manage biographical, historical, and documentary information about the International Brigades who participated in the Spanish Civil War. The structure is centered around a main entity, `BRIGADISTES`, which acts as a central hub connecting various biographical, military, and documentary processes.

## Core Concepts

The database is structured around a few core entities, from which most other data tables are derived, focusing on the comprehensive documentation of International Brigade members and their experiences.

### 1. `BRIGADISTES` (Brigade Members)

This is the central entity of the model. Each `BRIGADISTES` record represents a complete biographical profile of an International Brigade member, tracking their personal information, military service, ideological affiliations, and documentary sources. It links together information about their origins, military participation, ideological background, and the sources that document their experiences.

Key attributes include:
- Personal identification (name, alias, birth/death dates and locations)
- Country of origin and birth location
- Biographical data according to sources
- Geographic localization of birth and death

### 2. Personal and Professional Background

- **PROFESSIONS**: Stores information about the various professional occupations of brigade members.
- **PROCEDENCIA_RELIGIO_ETNIA**: Manages ethnic, religious, and origin characteristics of brigade members.
- **TIPUS_CARACTERISTICA**: Classifies different types of personal characteristics (ethnicity, religion, origin).
- **Junction Tables**: `BRIGADISTES_PROFESSIONS` and `BRIGADISTES_ETNIA_RELIGIO` create many-to-many relationships allowing brigade members to have multiple professions and characteristics.

### 3. Ideological and Political Affiliations

- **IDEOLOGIES_POLITIQUES**: Contains information about political ideologies represented among the brigade members.
- **ORGANITZACIONS**: Stores details about political organizations and groups with which brigade members were affiliated.
- **MOVIMENTS**: Documents political and social movements in which brigade members participated.
- **Junction Tables**: `BRIGADISTES_IDEOLOGIA`, `BRIGADISTES_ORGANITZACIONS`, and `BRIGADISTES_MOVIMENTS` manage the complex relationships between individuals and their political affiliations.

### 4. Military and Historical Context

- **ESDEVENIMENTS**: Records historical events and military actions in which brigade members participated.
- **ESTRUCTURES**: Documents military structures, units, and organizational hierarchies within the International Brigades.
- **PRESONS_CAMPS**: Manages information about prisons and camps where brigade members were detained.
- **ESPAIS_SANITARIS**: Records medical facilities and healthcare spaces where brigade members received treatment.
- **Junction Tables**: Multiple junction tables (`BRIGADISTES_ESDEVENIMENTS`, `BRIGADISTES_ESTRUCTURES`, `BRIGADISTES_PRESONS_CAMPS`, `BRIGADISTES_ESPAIS_SANITARIS`) connect individuals to their military and historical experiences.

### 5. Documentary Sources and References

- **FONTS**: This extensive table manages all documentary sources, including books, articles, memoirs, and archival materials that provide information about brigade members. It contains detailed bibliographic information including author, publication date, editor, and location.
- **IDIOMES**: Manages the languages in which sources are written.
- **ENFOCAMENTS**: Categorizes different analytical approaches or perspectives taken by sources.
- **LITERATURA_MITJANS_COMUNICACIO**: Documents different types of literature and media formats.
- **CULTURA**: Records cultural aspects and contexts addressed in sources.
- **TIPUS_DOCUMENTAL**: Classifies different types of documentary sources.
- **Junction Tables**: Multiple junction tables (`FONTS_BRIGADISTES`, `FONTS_FONTS`, `FONTS_IDIOMES`, `FONTS_ENFOCAMENTS`, `FONTS_LITERATURA_MITJANS`, `FONTS_CULTURA`, `FONTS_TIPUS_DOCUMENTAL`) create sophisticated relationships between sources and their characteristics.

## Relational Integrity

The model heavily relies on **foreign keys (FK)** to maintain relational integrity. The `FK` fields in each table link back to the primary key (PK) of another table, creating a well-structured and interconnected web of biographical and historical data.

For example:
- `BRIGADISTES_PROFESSIONS.fk_idBrigadista` links professional information back to the main brigade member record.
- `FONTS_BRIGADISTES` connects documentary sources with the specific brigade members they document.
- `BRIGADISTES_ESDEVENIMENTS.fk_idBrigadista` and `BRIGADISTES_ESDEVENIMENTS.fk_idEsdeveniment` create the many-to-many relationship between individuals and historical events.

The model also includes self-referential relationships, such as `FONTS_FONTS`, which allows sources to reference other sources, creating a network of bibliographic connections.

## Summary

This relational model is designed to be a comprehensive system for tracking the complex biographical, military, and documentary history of International Brigade members. By centralizing information around the `BRIGADISTES` table and using junction tables to manage complex relationships, the database provides a robust and scalable way to manage the multifaceted nature of wartime biographical documentation.

The model recognizes that brigade members existed within multiple overlapping contexts - personal, professional, ideological, military, and documentary - and provides the flexibility to capture these complex relationships while maintaining data integrity.

## Integration with Wikidata Properties

This database can be significantly enriched by linking its entities to Wikidata, a free and open knowledge base. Using Wikidata properties would allow for the integration of standardized, multilingual, and interconnected data, enhancing the overall value of the biographical and historical information stored.

Below are some key entities from this database and the corresponding Wikidata properties that could be used to augment them.

### **`BRIGADISTES` (Brigade Member)**
- **[P21](https://www.wikidata.org/wiki/Property:P21)**: `sex or gender`
- **[P735](https://www.wikidata.org/wiki/Property:P735)**: `given name` & **[P734](https://www.wikidata.org/wiki/Property:P734)**: `family name`
- **[P569](https://www.wikidata.org/wiki/Property:P569)**: `date of birth` & **[P570](https://www.wikidata.org/wiki/Property:P570)**: `date of death`
- **[P19](https://www.wikidata.org/wiki/Property:P19)**: `place of birth` & **[P20](https://www.wikidata.org/wiki/Property:P20)**: `place of death`
- **[P27](https://www.wikidata.org/wiki/Property:P27)**: `country of citizenship`
- **[P1559](https://www.wikidata.org/wiki/Property:P1559)**: `name in native language`
- **[P742](https://www.wikidata.org/wiki/Property:P742)**: `pseudonym` (for aliases)
- **[P607](https://www.wikidata.org/wiki/Property:P607)**: `conflict` (Spanish Civil War)
- **[P241](https://www.wikidata.org/wiki/Property:P241)**: `military branch` (International Brigades)

### **`PROFESSIONS` (Professions)**
- **[P106](https://www.wikidata.org/wiki/Property:P106)**: `occupation`
- **[P425](https://www.wikidata.org/wiki/Property:P425)**: `field of work`
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (profession, job, craft)

### **`IDEOLOGIES_POLITIQUES` (Political Ideologies)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (political ideology, political movement)
- **[P361](https://www.wikidata.org/wiki/Property:P361)**: `part of` (broader political movements)
- **[P1269](https://www.wikidata.org/wiki/Property:P1269)**: `facet of` (political spectrum)

### **`ORGANITZACIONS` (Organizations)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (political party, organization, trade union)
- **[P571](https://www.wikidata.org/wiki/Property:P571)**: `inception` (founding date)
- **[P576](https://www.wikidata.org/wiki/Property:P576)**: `dissolved, abolished or demolished date`
- **[P159](https://www.wikidata.org/wiki/Property:P159)**: `headquarters location`
- **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country`
- **[P1142](https://www.wikidata.org/wiki/Property:P1142)**: `political ideology`

### **`ESDEVENIMENTS` (Events)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (battle, military operation, historical event)
- **[P361](https://www.wikidata.org/wiki/Property:P361)**: `part of` (Spanish Civil War)
- **[P580](https://www.wikidata.org/wiki/Property:P580)**: `start time` & **[P582](https://www.wikidata.org/wiki/Property:P582)**: `end time`
- **[P276](https://www.wikidata.org/wiki/Property:P276)**: `location`
- **[P710](https://www.wikidata.org/wiki/Property:P710)**: `participant`
- **[P1120](https://www.wikidata.org/wiki/Property:P1120)**: `number of deaths`

### **`ESTRUCTURES` (Military Structures)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (military unit, brigade, battalion)
- **[P361](https://www.wikidata.org/wiki/Property:P361)**: `part of` (International Brigades)
- **[P607](https://www.wikidata.org/wiki/Property:P607)**: `conflict` (Spanish Civil War)
- **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country`
- **[P241](https://www.wikidata.org/wiki/Property:P241)**: `military branch`

### **`FONTS` (Documentary Sources)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (book, article, memoir, archival document)
- **[P50](https://www.wikidata.org/wiki/Property:P50)**: `author`
- **[P1476](https://www.wikidata.org/wiki/Property:P1476)**: `title`
- **[P577](https://www.wikidata.org/wiki/Property:P577)**: `publication date`
- **[P407](https://www.wikidata.org/wiki/Property:P407)**: `language of work or name`
- **[P123](https://www.wikidata.org/wiki/Property:P123)**: `publisher`
- **[P921](https://www.wikidata.org/wiki/Property:P921)**: `main subject` (Spanish Civil War, International Brigades)
- **[P276](https://www.wikidata.org/wiki/Property:P276)**: `location` (place of publication)

### **`PRESONS_CAMPS` (Prisons and Camps)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (prison, concentration camp, internment camp)
- **[P276](https://www.wikidata.org/wiki/Property:P276)**: `location`
- **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country`
- **[P571](https://www.wikidata.org/wiki/Property:P571)**: `inception` & **[P576](https://www.wikidata.org/wiki/Property:P576)**: `dissolved, abolished or demolished date`
- **[P137](https://www.wikidata.org/wiki/Property:P137)**: `operator` (controlling authority)

### **`ESPAIS_SANITARIS` (Medical Facilities)**
- **[P31](https://www.wikidata.org/wiki/Property:P31)**: `instance of` (hospital, field hospital, medical facility)
- **[P276](https://www.wikidata.org/wiki/Property:P276)**: `location`
- **[P17](https://www.wikidata.org/wiki/Property:P17)**: `country`
- **[P607](https://www.wikidata.org/wiki/Property:P607)**: `conflict` (if military medical facility)

### Implementation Approach
To implement this, new columns could be added to the existing tables to store the Wikidata Q-identifiers (e.g., a `wikidata_id` column in the `BRIGADISTES` table). This would create a robust link between the internal database records and the vast, interconnected data available on Wikidata, opening up new possibilities for biographical research and historical analysis.

### **Special Considerations for Spanish Civil War Context**
The SIDBRINT database deals with a specific historical conflict, requiring particular attention to war-related Wikidata properties:

#### **Spanish Civil War Integration**
- **[Q10859](https://www.wikidata.org/wiki/Q10859)**: Spanish Civil War - The main conflict item
- **[Q1137851](https://www.wikidata.org/wiki/Q1137851)**: International Brigades - The main organization
- **[Q8465](https://www.wikidata.org/wiki/Q8465)**: Civil war - Instance classification
- **[Q29](https://www.wikidata.org/wiki/Q29)**: Spain - Primary location

#### **Historical Period Linking**
- **[P2348](https://www.wikidata.org/wiki/Property:P2348)**: `time period` - Link to 1930s Spain
- **[P1264](https://www.wikidata.org/wiki/Property:P1264)**: `valid in period` - Temporal validity of information
- **[P1476](https://www.wikidata.org/wiki/Property:P1476)**: `title` - Historical period names

#### **Example of Use: A French Brigade Member**
To model a French International Brigade member who participated in the Battle of Madrid:

1. **On the Brigade Member's Record**:
   - `country of citizenship` ([P27](https://www.wikidata.org/wiki/Property:P27)) → France ([Q142](https://www.wikidata.org/wiki/Q142))
   - `conflict` ([P607](https://www.wikidata.org/wiki/Property:P607)) → Spanish Civil War ([Q10859](https://www.wikidata.org/wiki/Q10859))
   - `military branch` ([P241](https://www.wikidata.org/wiki/Property:P241)) → International Brigades ([Q1137851](https://www.wikidata.org/wiki/Q1137851))

2. **On the Event Record (Battle of Madrid)**:
   - `instance of` ([P31](https://www.wikidata.org/wiki/Property:P31)) → Battle ([Q178561](https://www.wikidata.org/wiki/Q178561))
   - `part of` ([P361](https://www.wikidata.org/wiki/Property:P361)) → Spanish Civil War ([Q10859](https://www.wikidata.org/wiki/Q10859))
   - `participant` ([P710](https://www.wikidata.org/wiki/Property:P710)) → International Brigades ([Q1137851](https://www.wikidata.org/wiki/Q1137851))

This creates a comprehensive network of biographical, military, and historical connections that enhances the research value of the SIDBRINT database. 