
## Descripción de la metodología



> ([[Science mapping software tools_ Review, analysis, and cooperative study among tools.pdf#page=1&annotation=230R|Science mapping software tools_ Review, analysis, and cooperative study among tools, p.1]])
> The general workflow in a science mapping analysis has different steps: data retrieval, preprocessing, network extraction, normalization, mapping, analysis and visualization. At the end of this process, the analyst has to interpret and obtain some conclusions from the results
> 
> Process: 
> 1. Download the data and preprocessing 
> 2. Extract networks
> 3. Data normalization
> 4. Map building


> 9. Analysis methods 
> 10. Visualization techniques 

> [!PDF|255, 208, 0] [[An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field.pdf#page=4&annotation=1041R|An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field, p.149]]
> > The first step is to collect the raw data.
> > 
> 
> 

> ([[An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field.pdf#page=3&selection=105,0,106,78&color=yellow|An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field, p.148]])
> 11. To detect the themes treated by the research field by means of co-word analysis for each studied subperiod. 
> 12. To layout in a low dimensional space the results of the first step (themes).
> 13. To analyze the evolution of the detected themes through the different subperiods studied, in order to detect the main general thematic areas of the research field, their origins and their inter-relationships. 
> 14. To carry out a performance analysis of the different periods, themes and thematic areas, by means of quantitative and impact measures.

## Data Selection and Data Analysis

### Data Selection Data Source

#### Search Terms
[[Ecuaciones de búsqueda]]

#### Delimitación de la estrategia de búsqueda

Participatory Design Focus
Semantic Technologies/Semantic Web
Digital Humanities \& GLAM Sector** - fixed

| Estrategia de Búsqueda                  | Resultados en Scopus | Resultados en WoS |
| :-------------------------------------- | :------------------- | :---------------- |
| 1. Enfoque en Diseño Participativo      | 94                   | 106/83            |
| 2. Tecnologías Semánticas/Web Semántica | 349/1412             | 133               |
| 3. Humanidades Digitales y Sector GLAM  | 215                  | 244               |

#### Estrategias de búsqueda aplicadas en el diseño de las ecuaciones

| Feature            | Proximity Search                                                                                      | Focused Search                                                                                                          | Broad Search                                                                                                                                                              |
| :----------------- | :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Recall**         | Medium                                                                                                | Low                                                                                                                     | High                                                                                                                                                                      |
| **Precision**      | Medium                                                                                                | High                                                                                                                    | Low                                                                                                                                                                       |
| **Best For**       | Concept relationships                                                                                 | Hypothesis testing                                                                                                      | Exploratory research                                                                                                                                                      |
| **Database Tools** | `W/n`, `NEAR/n`                                                                                       | Field-specific tags                                                                                                     | Wildcards (`*`)                                                                                                                                                           |
| **Use**            | When studying emerging interdisciplinary                                                              | for systematic reviews requiring strict inclusion criteria                                                              | Start with **Broad Search** when mapping a new research domain                                                                                                            |
|                    | Studies show proximity searching improves recall by 18-25% compared to basic Boolean searches [^6_6]. | MeSH-term searches achieve 75% recall vs. 54% for text-word searches, while maintaining 47.7% precision vs. 34.4%[^6_2] | This approach captures variant spellings (e.g., "co-creation"/"cocreation") and interdisciplinary connections, though with lower precision (34.4% vs. MeSH's 47.7%)[^6_2] |
[[MeSH and text-word search strategies_ precision, recall, and their implications for library instruction - PMC]]

[[What is proximity searching_ - LibAnswers]]

#### Eligibility and Appraisal

to give a summary of a field or study topic. Peer-reviewed publications listed in Scopus and WoS core XXX that were published between 2014 and 2025 are taken into account in this study. Our analysis includes XXXX articles in total.

Another eligibility criteria was that the record had a complete metadata or that it would be feasible to complete it. 

##### Pre processing
1. Metadatos completos?
- Cantidad inicial: Total record counts (2,660 total)
- Sin DOI: Records missing DOI metadata (476 total), +91 DOIs added (from 2,184 → 2,275)
- Sin Autores: Records missing author metadata  (158 records that were missing author information - mostly conference proceedings)
- Kept: 2,502 clean records with complete metadata

1. Autores normalizados?
- 2,933 total authors processed across all 5 RIS files
- 2,160 authors normalized (73.6% normalization rate)
- 773 authors were already in the correct format

##### Sample characteristics

| **Document Type**                            | **Scopus** | **Web of Science** | **Total** | **Percentage** | **Description**                          |
| -------------------------------------------- | ---------- | ------------------ | --------- | -------------- | ---------------------------------------- |
| **JOUR** (Journal Articles)                  | 800        | 268                | **1,068** | **42.7%**      | Peer-reviewed research articles          |
| **CONF** (Conference Proceedings) **CPAPER** | 1,082      | 287                | **1,369** | **54.7%**      | Conference presentations and proceedings |
| **CHAP** (Book Chapters)                     | 51         | 5                  | **56**    | **2.2%**       | Chapters in edited books                 |
| **BOOK** (Books)                             | 7          | 2                  | **9**     | **0.4%**       | Complete monographs                      |
| **TOTAL**                                    | **1,940**  | **562**            | **2,502** | **100.0%**     | Final dataset with complete metadata     |

### Data Analysis

### Software

#### SciMAT

> ([[!!Scoping Review on Research at the Boundary Between Learning and Working- A Bibliometric Mapping Analysis of the Last Decade.pdf#page=7&selection=31,35,38,15&color=yellow|!!Scoping Review on Research at the Boundary Between Learning and Working- A Bibliometric Mapping Analysis of the Last Decade, p.176]])
> The simple center algorithm is an accepted and often used algorithm in co-word-studies. Furthermore, "the simple centers algorithm automatically returns labelled clusters, so a post-process to label the clusters is not needed." (Cobo et al., 2011b, p. 149).

![[rayones de proceso.png]]


![[!!Scoping Review on Research at the Boundary Between Learning and Working- A Bibliometric Mapping Analysis of the Last Decade.pdf#page=7&rect=89,195,516,481|!!Scoping Review on Research at the Boundary Between Learning and Working- A Bibliometric Mapping Analysis of the Last Decade, p.176]]

> ([[An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field.pdf#page=5&annotation=1044R|An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field, p.150]])
> "Centrality measures the strength of ==external ties to other themes==. We can understand this value as a measure of the importance of a theme in the development of the entire research field analyzed".

> ([[An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field.pdf#page=5&annotation=1038R|An approach for detecting, quantifying, and visualizing the evolution of a research field- A practical application to the Fuzzy Sets Theory field, p.150]])
> Density measures the strength of ==internal ties among all keywords describing the research theme==. This value can be understood as a measure of the theme's development.


**Motor Themes (High Centrality + High Density):**
- Mature intersections like "metadata standards in cultural heritage"

**Basic Themes (High Centrality + Low Density):**
- Broad concepts like "user-centered design" or "semantic web"

**Niche Themes (Low Centrality + High Density):**
- Specialized applications like "VR interfaces for museums"

**Emerging Themes (Low Centrality + Low Density):**
- New intersections like "AI-assisted curation with user feedback"



### Databases




### Search equations:

[[Ecuaciones de búsqueda]]

Estrategias de diseño de las ecuaciones de búsqueda

| Component            | Participatory Design        | Semantic Tech                | GLAM/Digital Humanities     |
| :------------------- | :-------------------------- | :--------------------------- | :-------------------------- |
| **Core Concepts**    | Co-creation, UCD            | RDF, Ontologies              | Metadata, Cultural Heritage |
| **Proximity**        | `NEAR/5` for design-process | `W/5` semantic relationships | `W/3` historical links      |
| **Wildcards** -broad | `design*` (covers -ing/-er) | `graph*` (graphs/graphical)  | `collection*`               |
| **Limits**           | COMP/SOCI/ARTS              | COMP/DECI                    | Libraries/Museums indexes   |
|                      |                             |                              |                             |




