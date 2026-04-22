# Primeras búsquedas
![[Presentación de avances.pdf#page=9&rect=115,52,905,487|Presentación de avances, p.9]]

## Sugeridos por lectura

- "usability" AND "knowledge graph"​
    
- "buscador" "Searcher" "interface" AND "Knowledge graph"​
    
- "knowledge graph" AND "User centered design" AND "humanities"​
    
- "knowledge graph" AND "User centered design" AND "History"​
    
- human-centered AND artificial AND intelligence​
    
- HCD (human centered design) / DCH (diseño centrado en el humano) #op/suggestedByarticle​
    
-  Human-centered interaction, interaction patterns #op/suggestedByarticle​
    
- Diseño participativo / Participatory design OR Innovación social / Social innovation OR Diseño interactivo​
    
- Diseño ontológico OR "CK theory"  #op/suggestedByarticle AND "knowledge graphs"​
    
- Digital hermeneutics AND 'Semantic web"​
- user-generated metadata
- multi stakeholder  ontology curation
- 

## Perplexity
- ("knowledge graphs" OR "semantic networks") AND ("semantic frames" OR "frame semantics") AND ("historical corpus" OR "historical texts")​
    
- Grafos de conocimiento basados en datos enlazados #op/suggestedBytutors, RDF #op/suggestedBytutors​
    
- Semantic frames #op/suggestedBytutors #research_method/perplexity o Semantic data ​
    
- Buscadores (motores de búsqueda? #op/question)

## Tutors

- Bias AND (librar* OR archive* OR museum* OR database* OR GLAM) AND ("AI driven cataloguing" OR "AI driven classification" OR "AI driven indexing" OR "AI driven metadata" OR "AI based cataloguing" OR "AI based classification" OR "AI based indexing" OR "AI based metadata") #op/suggestedBytutors ​
- UCD (user centered design) OR DCU (diseño centrado en el usuario) #op/suggestedBytutors​ 
- UX (user experience) / EU (Experiencia de usuario) #op/suggestedBytutors, User interface.​
- LIS o GLAM

# Búsquedas segmentadas por title, abstract y keywords

## Resumen de Resultados

| Estrategia de Búsqueda                  | Resultados en Scopus | Resultados en WoS |     |
| :-------------------------------------- | :------------------- | :---------------- | --- |
| 1. Enfoque en Diseño Participativo      | 94                   | 106/83            |     |
| 2. Tecnologías Semánticas/Web Semántica | 349/1412             | 133               |     |
| 3. Humanidades Digitales y Sector GLAM  | 215                  | 244               |     |

# Búsquedas para mapa

[[Search equations on Scopus]]
[[Search equations on WoS]] - [[search-history WoS.txt]]


| Component            | Participatory Design        | Semantic Tech                | GLAM/Digital Humanities     |
| :------------------- | :-------------------------- | :--------------------------- | :-------------------------- |
| **Core Concepts**    | Co-creation, UCD            | RDF, Ontologies              | Metadata, Cultural Heritage |
| **Proximity**        | `NEAR/5` for design-process | `W/5` semantic relationships | `W/3` historical links      |
| **Wildcards** -broad | `design*` (covers -ing/-er) | `graph*` (graphs/graphical)  | `collection*`               |
| **Limits**           | COMP/SOCI/ARTS              | COMP/DECI                    | Libraries/Museums indexes   |
|                      |                             |                              |                             |

## **1. Participatory Design Focus**

### Scopus:

```sql
TITLE-ABS-KEY(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND SUBJAREA(COMP OR SOCI OR ARTS)
AND PUBYEAR > 2014
```

n = 474

- [x] [[metadataScopus1.ris]]

**Key GLAM Integration**
`("metadata usability" OR "cultural heritage metadata" OR "GLAM interoperability")`
*From your paste.txt's "User-centered metadata schema" and FAIR principles*

### WoS core collection
#op/buscar https://www.webofscience.com/wos/woscc/summary/044c0fc3-5ca4-470d-b44f-f24abb58eb67-01690f7ece/relevance/1 

```sql
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" OR "Social Sciences, Interdisciplinary" OR "Art" OR "Arts & Humanities Other Topics")
AND PY=2015-2025
```
 N=106
 - [x] [[metadataWoS1.ris]]

<mark class="hltr-orange">Web of science recommended adding some keywords: 
</mark> https://www.webofscience.com/wos/woscc/summary/45714983-d13a-4fbd-b3be-94f096d973af-016910a80b/relevance/1 


```sql 
TS=(
    (
        ("participatory design" OR "co-creation*" OR "user centered design" OR "human centered interaction" OR "social innovation")
        AND 
        ("knowledge graph*" OR "CK theory" OR "interaction patterns" OR "usability testing" OR "cognitive load")
    )
    OR 
    (
        ("metadata usability" OR "cultural heritage metadata" OR "GLAM interoperability")
        AND 
        ("knowledge graph*" OR "CK theory" OR "interaction patterns" OR "usability testing" OR "cognitive load")
    )
)
AND WC=("Computer Science, Information Systems" OR "Social Sciences, Interdisciplinary" OR "Art")

```
- [x]  [[metadataWoS1+.ris]]
N=83

## **2. Semantic Technologies/Semantic Web**

### Scopus
#### Proximity Search Strategy
```sql
TITLE-ABS-KEY( ("semantic web" OR "linked data" OR "RDF mapping" OR "FAIR data" OR "ontology engineering") W/5 ("knowledge graph*" OR "frame semantics" OR "polyvocality" OR "multimodal data" OR "bias reduction") ) AND PUBYEAR > 2014
```

N=349

#### Broad: 

```sql
TITLE-ABS-KEY(
    (
        ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
        OR "archival discover*" OR "cultural heritage" OR "historical corpus"
        OR "user-centered metadata" OR "metadata schema")
        AND 
        ("data stori*" OR "interactive visual*" OR "user test*" 
        OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
    )
    OR 
    (
        ("semantic web" OR "RDF mapping" OR "ontology engineering") 
        W/5 
        ("digital humanit*" OR "GLAM sector" OR "historical memory")
    )
    OR
    ("knowledge graph*" OR "frame semantics" OR "polyvocality" OR "multimodal data" OR "bias reduction")
)
AND (INDEXTERMS("libraries" OR "museums" OR "archives" OR "cultural heritage") OR TITLE-ABS-KEY("libraries" OR "museums" OR "archives" OR "cultural heritage"))
AND PUBYEAR > 2014

```
N= 1412


- [x] [[metadataScopus2.ris]]


- [x]  **Historical Content Filter** 
`("historical corpus" OR "digital humanities" OR "post-colonial heritage")`
*From your PDF notes on polyvocality in historical contexts*


### WoS core collection:
```sql
TS=(
    (
        ("semantic web" OR "linked data" OR "RDF mapping" 
        OR "FAIR data" OR "ontology engineering")
        NEAR/5 
        ("knowledge graph*" OR "frame semantics" OR "polyvocality" 
        OR "multimodal data" OR "bias reduction")
    )
)
AND WC=(
    "Computer Science, Artificial Intelligence" OR
    "Computer Science, Information Systems" OR
    "Computer Science, Interdisciplinary Applications" OR
    "Computer Science, Theory & Methods" OR
    "Operations Research & Management Science"
)
AND PY=2015-2025

```
N=133

- [x] [[metadataWoS2.ris]]

[(hay otras keywords pero abren mucho la búsqueda y no se percibe aporte)]()




---

## **3. Digital Humanities \& GLAM Sector** - fixed

### Scopus:
```sql
TITLE-ABS-KEY (
    (
        ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
        OR "archival discover*" OR "cultural heritage" OR "historical corpus"
        OR "user-centered metadata" OR "metadata schema")
        AND 
        ("data stori*" OR "interactive visual*" OR "user test*" 
        OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
    )
    OR 
    (
        ("semantic web" OR "RDF mapping" OR "ontology engineering") 
        W/5 
        ("digital humanit*" OR "GLAM sector" OR "historical memory")
    )
)
AND INDEXTERMS("libraries" OR "museums" OR "archives" OR "cultural heritage")
AND PUBYEAR > 2014
```

N= 215
- [x] [[metadataScopus3.ris]]
### WoS core collection: 

```sql
TS=(
    (
        ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
        OR "archival discover*" OR "cultural heritage" OR "historical corpus"
        OR "user-centered metadata" OR "metadata schema")
        AND 
        ("data stori*" OR "interactive visual*" OR "user test*" 
        OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
    )
    OR 
    (
        ("semantic web" OR "RDF mapping" OR "ontology engineering") 
        NEAR/5 
        ("digital humanit*" OR "GLAM sector" OR "historical memory")
    )
)
AND TS=("libraries" OR "museums" OR "archives" OR "cultural heritage")
AND PY=2015-2025

```
N=244
- [x]  [[metadataWoS3.ris]]


## Reviews:

### Scopus
#op/explore 

### WoS core collection

https://www.webofscience.com/wos/woscc/summary/1c615152-e3c8-43be-a8cc-50412080dbcb-0169122ae9/relevance/1 

``` sql
((TS=((
    ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
    OR "archival discover*" OR "cultural heritage" OR "historical corpus" 
    OR "user-centered metadata" OR "metadata schema") 
    AND 
    ("data stori*" OR "interactive visual*" OR "user test*" 
    OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
) 
OR 
    (("semantic web" OR "RDF mapping" OR "ontology engineering") 
    NEAR/5 
    ("digital humanit*" OR "GLAM sector" OR "historical memory"))
)
AND TS=("libraries" OR "museums" OR "archives" OR "cultural heritage" OR "archives")
AND PY=2015-2025) OR (QMTS=("linked open data")) OR (QMTS=("wikidata")) OR (QMTS=("glam"))) NOT (QMTS=("VR") OR QMTS=("AR"))
```
N=43 (well narrowed too)



```sql
TS=(
    (
        ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
        OR "archival discover*" OR "cultural heritage" OR "historical corpus" 
        OR "user-centered metadata" OR "metadata schema")
        AND 
        ("data stori*" OR "interactive visual*" OR "user test*" 
        OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
    )
    OR 
    (
        ("semantic web" OR "RDF mapping" OR "ontology engineering") 
        NEAR/5 
        ("digital humanit*" OR "GLAM sector" OR "historical memory")
    )
    OR 
    ("linked open data" OR "wikidata" OR "glam")
)
AND TS=("libraries" OR "museums" OR "archives" OR "cultural heritage")
AND PY=2015-2025
NOT TS=("VR" OR "AR")

```

N= 14 (very well narrowed)
#op/buscar #op/leer 