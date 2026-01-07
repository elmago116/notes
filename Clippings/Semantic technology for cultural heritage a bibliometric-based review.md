---
title: Semantic technology for cultural heritage a bibliometric-based review
year: "2023"
doi: 10.1108/GKMC-04-2023-0125
url: https://www.emerald.com/gkmc
publisher: Emerald
type: article
source: Crossref
base: clippings
last_enrichment_run: 2025-08-20
updated: 2025-08-20
enrichment_attempts:
  - openalex_doi
  - arxiv_doi
  - openalex_title
authors:
  - Sudarsan Desul,
  - Rabindra Kumar Mahapatra,
  - Raj Kishore Patra,
  - Mrutyunjay Sethy
  - Neha Pandey
tags:
  - research_method/ScopingReview
  - Tech/SemanticWeb
  - Humanities/culturalHeritage
  - bibliometrics
apa_citation: Desul, et al., 2023
---
![[Semantic technology for cultural heritage a bibliometric-based review.pdf]]

## PDF text extraction

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/373294609
Semantic technology for cultural heritage: a bibliometric-based review
Article  in   Global Knowledge Memory and Communication · August 2023
DOI: 10.1108/GKMC-04-2023-0125
CITATIONS
4
READS
262
5 authors, including:
Mrutyunjay Sethy
Berhampur University
5 PUBLICATIONS   45 CITATIONS   
SEE PROFILE
Neha Pandey
Berhampur University
7 PUBLICATIONS   46 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Neha Pandey on 13 December 2023.
The user has requested enhancement of the downloaded file.

Semantic technology for cultural
heritage: a bibliometric-based
review
Sudarsan Desul
Department of Library and Information Science, Berhampur University,
Berhampur, India
Rabindra Kumar Mahapatra
Department of Library and Information Science, Tripura University,
Suryamaninagar, India
Raj Kishore Patra
Department of Philosophy, Rajendra University, Balangir, India and
Department of Journalism and Mass Communication, Berhampur University,
Berhampur, India
Mrutyunjay Sethy
Department of Library and Information Science, Berhampur University,
Berhampur, India, and
Neha Pandey
Department of Journalism and Mass Communication, Berhampur University,
Berhampur, India
Abstract
Purpose – The purpose of this study is to review the application of semantic technologies in cultural
heritage (STCH) to achieve interoperability and enable advanced applications like 3D modeling and
augmented reality by enhancing the understanding and appreciation of CH. The study aims to identify the
trends and patterns in using STCH and provide insights for scholars and policymakers on future research
directions.
Design/methodology/approach – This research paper uses a bibliometric study to analyze the articles
published in Scopus and Web of Science (WoS)-indexed journals from 1999 to 2022 on STCH. A total of 580
articles were analyzed using the Biblioshiny package in RStudio.
Findings – The study reveals a substantial increase in STCH publications since 2008, with Italy
leading in contributions. Key research areas such as ontologies, semantic Web, linked data and digital
humanities are extensively explored, highlighting their signi ﬁcance and characteristics within the
STCH research domain.
Research limitations/implications– This study only analyzed articles published in Scopus and WoS-
indexed journals in the English language. Further research could include articles published in other
languages and non-indexed journals.
Originality/value – This study extensively analyses the research published on STCH over the past
23 years, identifying the leading authors, institutions, countries and top research topics. Theﬁndings provide
Since acceptance of this article, the following author has updated their aﬃliation: Sudarsan Desul is
at the Department of Library and Information Science, Tripura University, Suryamaninagar, India.
Semantic
technology
Received 12 April 2023
Revised 2 May 2023
14 June 2023
7J u l y2 0 2 3
Accepted 1 August 2023
Global Knowledge, Memory and
Communication
© Emerald Publishing Limited
2514-9342
DOI 10.1108/GKMC-04-2023-0125
The current issue and full text archive of this journal is available on Emerald Insight at:
https://www.emerald.com/insight/2514-9342.htm

guidelines for future research direction and contribute to the literature on promoting, preserving and
managing the CH globally.
Keywords Cultural heritage, Ontology, Semantic technology, Intangible cultural heritage,
Digital humanities, Linked data
Paper typeResearch paper
1. Introduction
Cultural heritage (CH) is an invaluable legacy of human societies passed down from the past to
the present and future generations, encompassing a wide range of tangible and intangible
elements with cultural, social and economic value. These include historical monuments,
artifacts, traditions and knowledge systems (
Vecco, 2010). Different types of CH exist, such as
tangible CH (physical objects and buildings), intangible CH– traditions and practices (Vecco,
2010), natural heritage– natural landscapes and biodiversity (UNESCO World Heritage Centre,
2021), archaeological heritage– physical remains of past societies (O’Keeffe, 2014), digital CH–
digital artifacts (Landorf, 2020), industrial heritage- remains of industrial sites (Loures, 2008)
and religious heritage– artifacts and practices associated with religion (Stovelet al., 2005).
Preserving, managing and promoting CH is crucial for maintaining cultural diversity,
fostering social cohesion and supporting sustainable development (Bikakiset al., 2021). Various
initiatives and programs have been developed to achieve these goals, such as EUROPEANA,
DARIAH and CrossCult, which seek to manage, share and analyze cultural data. The European
Year of Cultural Heritage in 2018 witnessed numerous events and initiatives aimed at
promoting CH (Moraitouet al., 2022). International organizations like UNESCO play a key role
in setting standards and guidelines for the protection and management of CH.
Traditional approaches such as manual cataloguing, keyword-based search, taxonomies,
relational databases and digital asset management systems were used to manage and access
CH data (Kalita and Deka, 2021; Hyvönen, 2012). However, these approaches had limitations
regarding data integration, semantic representation, search precision and contextual
information management.
In recent years, semantic technologies (ST) have emerged as a promising solution for
addressing the challenges of managing and accessing information in various domains
including, CH (Benjaminset al., 2004). These technologies offer the potential to integrate diverse
data sources, capture complex semantics and enhance search and discovery processes (Lodi
et al., 2017). ST provides tools and methods for representing, integrating and reasoning about
information in a machine-understandable way using formal languages and ontologies.
Given the growing importance of semantic technology in the cultural heritage (STCH)
domain, this literature review and bibliometric analysis aim to provide an overview of the
state-of-the-art research on ST applications in CH. By analyzing existing literature, the
review seeks to identify the main research themes, trends and challenges in theﬁeld.
Furthermore, it aims to highlight the most inﬂuential and cited articles, authors and journals
in the STCH domain. The main research questions of this study are as follows:
RQ1. What are the trend and patterns of research in the domain of STCH during 1990–
2022?
RQ2. Who are the most productive authors, and which countries and institutions have
highest publication in STCH?
RQ3. What are the key themes or sub-themes can be found across the research domain
and the direction for future research?
GKMC

2. Methodology
The study adopts the bibliometric analysis procedure by following the recent works of
Mishra et al. (2022, 2023), Patra et al. (2022) and Acharyya et al. (2023). The bibliometric
analysis process follows aﬁve-stage methodological approach (refer toFigure 1), explained
in the subsequent sections. Later, comprehensive review protocols helped identify research
themes and understand trends and patterns of publication in this domain.
2.1 Selection of bibliographic databases
Scopus and Web of Science (WoS) have earned a reputation for being widely used to collect
bibliographic records and for more comprehensive coverage. Both databases provide a
platform for over 20,000 peer-reviewed journals from various publishing houses and offer
advanced ﬁltering options and data analysis grids for better data management.
Consequently, the required data was collected from both databases to cover a larger study
landscape.
2.2 Formulation of the search strategy and preparation of data set
A preliminary search was conducted to identify alternative or synonymous terms for ST,
ontologies, linked data and metadata in the context of CH. The titles and abstracts of the
articles retrieved during the search were examined, and all synonym keywords were
gathered. A search strategy using Boolean operators (AND/OR) was prepared, and Scopus
and WoS databases were searched for articles published in English between 1999 and 2022
using this strategy. On January 12th, 2023, 1,080 articles were retrieved from Scopus, and
226 articles were retrieved from WoS that matched the deﬁned search criteria and imported
Figure 1.
Workﬂow of the
study
Semantic
technology

the retrieved articles in“.bib” text and“.txt” format from Scopus and WoS, respectively, to
facilitate further analysis. Afterwards, merged the two data sets in RStudio and removed
217 duplicate bibliographies. After theﬁltration process, the merged database remained,
including 1,089 publications.
The Scopus database helped in retrieving 1,080 document results by following the
keyword hunt; TITLE-ABS-KEY (“semantic technology*”OR “Sematic web”OR ontology*
OR “data integration” OR “knowledge representation” OR “metadata” OR “linked data” OR
“knowledge graph”) AND TITLE-ABS-KEY (“heritage conservation” OR “conservation of
heritage”OR “cultural heritage”OR “heritage data”OR “heritage information”OR “heritage
knowledge” OR “heritage conservation” OR “conservation of heritage”) AND [limit-to
(language, “English”)] AND EXCLUDE (PUBYEAR, 2023).
Similarly, the WoS database assisted in acquiring 226 document results by following
keyword search; (“semantic technology*” OR “Sematic web” OR ontology* OR “data
integration” OR “knowledge representation” OR “metadata” OR “linked data” OR “knowledge
graph”;T o p i c )a n d(“heritage conservation” OR “conservation of heritage” OR “cultural
heritage”OR “heritage data”OR “heritage information”OR “heritage knowledge”; Topic).
2.3 Reﬁning the initial results and preparing aﬁnal data set
Just before conducting an exhaustive analysis of the most relevant publications, a screening
process was conducted to reduce the number of identiﬁed studies. This involved reviewing
the titles and abstracts of the publications and assessing whether they were related to
STCH. Based on this screening process, many of the initially identiﬁed research studies were
excluded, resulting in a retention rate of 53% (580 out of 1,089). Subsequently, 580 articles
were selected as theﬁnal sample for further analysis.
2.4 Bibliometric analysis
Bibliometric analysis is a quantitative method used to study and evaluate scientiﬁc
literature based on various bibliographic data, such as citations, authors, journals and
keywords. Two commonly used techniques within bibliometric analysis are performance
analysis and science mapping. Performance analysis in bibliometrics focuses on evaluating
the performance of individuals, institutions, journals or countries based on various
bibliometric indicators. These indicators can include the number of publications, citations
received, h-index, collaboration patterns and productivity over time. Science mapping, also
known as knowledge mapping or research landscape analysis, aims to visualize and explore
the intellectual structure of a particularﬁeld or scientiﬁc domain. It helps identify research
fronts, emerging trends, inﬂuential papers and relationships between topics or concepts.
In this study, we considered eight types of analysis– primary information about the data
set, evolution of publications, most productive authors, most relevant source, most
inﬂuential articles, trending topics and thematic analysis– using Biblioshiny software (
Aria
and Cuccurullo, 2017). Thematic analysis was used to identify research themes in theﬁeld of
STCH. It was based on a co-words network, which was developed using the Biblioshiny
software. This analysis followed a four-stage approach. First, the study identiﬁed the
research themes within the ﬁeld of STCH. Then, it visualized these themes and their
relationships through a thematic network and strategic diagram. The thematic areas within
STCH were deﬁned as part of this process. Finally, the performance of the STSH research
ﬁeld was analyzed.
To visualize the STCH research themes, the density and centrality values were used. The
density of the network quantiﬁed the internal strength of the connections between themes,
GKMC

while centrality measured the degree of interaction between the network and other
networks.
The strategic diagram, represented inFigures 2and 7, is a two-dimensional map divided
into four quadrants based on signiﬁcance. The STCH research themes are depicted as
spheres in this diagram, with the size of each sphere being proportional to the number of
associated publications. Those publications associated with each theme were considered to
provide an overview of the theme. Read for more information about the thematic analysis
(Cobo et al., 2012).
3. Result and analysis
The study monitored the main trends and patterns of research in the domain of STCH
during 1990–2022, and the analysis results are presented in detail below.
3.1 Key information about the data set and document type
Table 1 provides descriptive information on the 580 research STCH domain published
between 1999 and 2022. It was noticed that 580 articles were contributed by 1,425 authors
worldwide, published in 273 journals and used 412 author-speciﬁc keywords in addition to
2,119 keywords plus. In STCH research, the average proportion of citations per publication
was 6.72, while the average proportion of authors, co-authors per paper and the
collaborative index was 2.46, 3.59 and 2.67, respectively.
Figure 3 displays the distribution of document types in the SCTH research. In all
publications, conference papers (59%) and articles (35% of the total) are the main
contributors, whereas other less signiﬁcant outputs for all papers were reviews, editorial
materials, books and book chapters.
3.2 Evolution of publication
Figure 4depicts the evolution of publication over the last 23 years, where it can be seen that
STCH studies began to grow signiﬁcantly after 2008. However, there was a decline in 2011,
Figure 2.
The strategic
diagram
Semantic
technology

2012, 2016 and 2020 before reaching a peak in 2021, with 75 articles published. Since 2008,
535 articles have been published (92% of the studies), and the remaining were published
before 2007. This represents an average of 35 articles published per year. In connection to
citations, those articles published in 2017 received the most citations compared to other
years. Out of all publications, 155 have no citations, 248 works have between 1 and 5
citations, 79 articles have between 6 and 10 citations and 44 seminal works have more than
30 citations.
3.3 Trending topics
Regarding trending topics, the top research keywords of STCH research from 2006 to 2022
are shown inFigure 5. It depicts an analysis of the keywords that occurred most frequently
each year. The research during 2006–2022 primarily focused on CIDOC conceptual reference
model (CRM), knowledge management, heritage ontology, information retrieval, CIDOC/CR,
heritage collections, heterogeneous culture, semantic Web, heritage domain, architectural
heritage, data curation, CH, heritage data, linked data, heritage knowledge, digital
humanities, knowledge graph and data model.
Table 1.
Key information
about data set
Description Results
Timespan 1999:2022
Sources (Journals and Books) 273
Documents 580
Average years from publication 6.83
Average citations per documents 6.729
References 14,316
Keywords plus (ID) 2,119
Author’s keywords (DE) 1,412
Authors 1,425
Single-authored documents 68
Documents per author 0.407
Authors per document 2.46
Co-authors per documents 3.59
Collaboration index 2.67
Source: Table by authors
Figure 3.
Distribution of
document types in the
SCTH research
GKMC

Figure 4.
Year-wise publication
trend in the domain of
STCH
Figure 5.
Trending topics in
STCH research
during 2006 to 2022
Semantic
technology

3.4 Geographical distribution
The geographical contributions in STCH research from 1999 to 2022 are shown inFigure 6.
Italy (26.3%) is the most contributed country that published the maximum papers in STCH
research, followed by Greece (9.3%), China (8%), France (8%), the United Kingdom (6.2%),
the USA (5.9%) and other nation’s tails accordingly. Regarding citations, Italy is the most
cited country acknowledged with the highest number of credentials in STCH research,
followed by Greece (323), the USA (244) and the UK (221).
3.5 Most productive authors
The most proliﬁc authors based on publications from 1999 to 2022 are shown inTable 2.
According to the list, Eero Hyvönen (14 articles) from Aalto University, Finland, Vincenzo
Figure 6.
Geographical
distribution for STCH
research
Table 2.
Top 10 authors based
on publications.
Author Articles h_index TC Affiliation
Eero Hyvönen 14 7 177 Aalto University
Vincenzo Lombardo 11 5 73 University of Turin
Rossana Damiano 10 5 82 University of Turin
Martin Doerr 9 7 505 Foundation for Research and Technology
Harald Sack 9 1 13 Karlsruhe Institute of Technology
Manolis Gergatsoulis 8 5 131 Ionian University
Valentina Anita Carriero 7 3 45 University of Bologna
Nuno Freire 7 3 35 Instituto de Engenharia de Sistemas e
Computadores
Aldo Gangemi 7 3 45 University of Bologna
Antoine Isaac 7 4 41 Vrije Universiteit Amsterdam
Note: TC ¼ total citations count
Source: Table by authors
GKMC

Lombardo (11 articles) and Rossana Damiano (10 articles) from the University of Turin,
Italy are the most productive authors. Martin Doerr (nine articles) from the Foundation for
Research and Technology, Greece and Harald Sack (nine articles) from Ionian University,
Greece, are also other signiﬁcant contributors to a research publication of data analytics.
Regarding citations, Martin Doerr obtained more citations compared to other authors.
3.6 Inﬂuential institutions
The top institutions in STCH have been identiﬁed and presented inTable 3. It can help
scholars to collaborate with those top institutions for their research work. According to the
list, the University of Turin (39) from Italy has more publications, followed by Aalto
University (24) in Finland, the University of Bologna (18) in Italy and Ionian University (10)
in Greece. It was noticed that the most contributing institutions inTable 3belong to Italy (3),
Greece (2), Finland (2), France (1), Germany (1) and India (1).
3.7 Highly preferred sources
Table 4represents the highly published journals related to STCH research from 1999–2021.
CEUR Workshop Proceedings has published the highest number of publications (62) with
102 citations, followed by Computer Science Lecture Notes (Comprising of Series of Lecture
Notes in Artiﬁcial Intelligence and Bioinformatics Lecture Notes; 49 articles) with 308
references and Communications in Computer and Information Science (27 articles) with 91
citations.
4. Thematic analysis of semantic technology for cultural heritage research
The third research question (RQ3) aims to conduct a thematic study of the research
domain based on the authors’ keywords and visualize the resulting themes and sub-
themes. To achieve this, we followed existing papers and used the thematic map module
of Biblioshiny software to create a strategic diagram highlighting the STCH domain’s
major themes.
The study only considered keywords that appeared at leastﬁve times to identify the
domain’s most emphasized and detailed themes and sub-themes. The resulting themes were
formed by grouping related keywords that frequently appeared together in the domain and
were named based on the keywords with the highest frequency. Inﬂuenced by the work of
(
Callon et al., 1991), the strategic diagram generated from the thematic study categorizes
Table 3.
Top 10 institutions
based on
publications
Affiliation Articles Country
University of Turin 39 Italy
Aalto University 24 Finland
University of Bologna 18 Italy
Ionian University 10 Greece
University of Helsinki 10 Finland
Aix Marseille University 7 France
Karlsruhe Institute of Technology 7 Germany
University of Salerno 7 Italy
Indian Institute of Technology 6 India
Institute of Computer Science 6 Greece
Source: Table by authors
Semantic
technology

themes in the STCHﬁeld into four quadrants based on the centrality and density measures
(refer toFigure 7):
(1) The ﬁrst quadrant, “motor themes,” consists of highly central and densely
interconnected themes. These themes are not only important and relevant but also
well-developed and integrated within the STCH network. They play a crucial role
in shaping the STCHﬁeld and will likely to remain signiﬁcant.
(2) The second quadrant includes “niche themes ” that are well-developed and
interconnected but have lower centrality values. These themes have a high level of
coherence within the STCH domain but may have less impact on the overall
advancement of theﬁeld than those in theﬁrst quadrant.
(3) The third quadrant comprises “declining or emerging themes” with low centrality
and density values. These themes need to be well-established and interconnected
within the STCH network. They may be losing relevance or are emerging and
require further development to become more inﬂuential in the STCHﬁeld.
(4) The fourth quadrant consists of “basic and transversal themes ” with high
centrality but low-density values. These themes are highly relevant for expanding
the STCHﬁeld but need to be more effectively established and interconnected with
other themes. They serve as foundational aspects for future exploration and
development in the STCH domain.
Based on Figure 7, the study identiﬁed ten major themes in the STCH research domain:
ontologies, digital humanities, linked data, intangible CH, CH, ontology learning, big data,
CIDOC/CRM, semantic annotation and knowledge management. Among these themes,
ontologies, digital humanities, linked data, CH and knowledge management emerged as the
most inﬂuential and prominent. These themes belong to the motor and basic themes,
characterized by high centrality and density values. This indicates their signiﬁcance and
relevance within the STCHﬁeld. They play a crucial role in shaping theﬁeld and are well-
formed and interconnected with other themes. On the other hand, themes like ontology
learning, big data and CIDOC/CRM appeared in the second quadrant as niche themes. While
these themes are well-developed and interconnected, they have lower centrality values and
may not have as much overall impact on the advancement of the STCHﬁeld. Themes such
Table 4.
Highly preferred
sources
Source Articles Total citations
CEUR Workshop Proceedings 62 102
Lecture Notes in Computer Science (Including Subseries Lecture Notes in
Artiﬁcial Intelligence and Lecture Notes in Bioinformatics) 49 308
Communications in Computer and Information Science 27 91
ACM Journal on Computing and Cultural Heritage 15 107
International Archives of The Photogrammetry Remote Sensing and
Spatial Information Sciences– ISPRS Archives 14 60
Digital Presentation and Preservation of Cultural and Scientiﬁc Heritage 11 15
Semantic Web 11 87
ACM International Conference Proceeding Series 10 41
ISPRS Annals of the Photogrammetry Remote Sensing and Spatial
Information Sciences 9 64
Journal of Cultural Heritage 8 302
Source: Table by authors
GKMC

as intangible CH and semantic annotation were categorized as declining or emerging themes
in the third quadrant. These themes have low centrality and density values, suggesting they
are not well-established or interrelated within the STCH domain. They require further
development and establishment to become more signiﬁcant in theﬁeld. The details of each
theme will be discussed in the following section, providing a comprehensive overview of
their characteristics and relevance within the STCH research domain.
4.1 Cultural heritage
The theme“cultural heritage” is a basic theme of this period. It exhibits strong associations
with subthemes such as ontology and semantic Web, highlighting their crucial role in
organizing and representing CH knowledge (referFigure 8). Another noteworthy subtheme
is linked open data, which emphasizes the value of publishing and interlinking CH data on
the Web. In addition, speciﬁc standards and technologies like CIDOC/CRM and RDFﬁnd
extensive use in documenting and representing CH information. The concept of data
integration stands out prominently, indicating the necessity to merge and harmonize diverse
CH data sets from various sources. Moreover, disciplines like archaeology, digital library
and museum demonstrate strong connections to CH, underscoring their signiﬁcance within
the ﬁeld. Various technologies and techniques, including augmented reality, annotation and
natural language processing, highlight their relevance to CH research and practice. The
analysis covers a wide range of subthemes, encompassing knowledge graphs, inference,
recommender systems, semantic search, crowdsourcing and more.
Out of 580 articles, 175 articles are associated with this theme. Those articles related to
the application of semantic Web technologies and linked open data in the CH domain.
Several papers explore different approaches and frameworks in the digital CH domain.
Figure 7.
Strategic diagram
from 1999 to 2022
Semantic
technology

O’Neill and Stapleton (2022)provided an overview of various standards used, whileGoy
et al. (2020) presented the PRiSMHA project for improving access to historical archives.
Other papers focus on improving recommendations (Benouaret and Lenne, 2015; Grieser
et al., 2011; Noor and Martinez, 2009 ; Sansonetti et al., 2019), achieving semantic
interoperability (Kuo et al., 2018; Niang et al.,2 0 1 7; Vlachidis and Tudhope, 2016) and
documenting CH using standardized vocabularies and ontologies (Cacciotti et al., 2013;
Cacciotti, 2015; Carboni and de Luca, 2016, 2017; Lombardo et al.,2 0 1 7). Some papers
highlight the potential of linked open data (Damova and Dannells, 2011; De Angeliset al.,
2017; Freire et al.,2 0 1 9; Leskinen et al., 2017), while others demonstrate the potential of
ontology-based approaches for accessing and retrieving multimedia CH objects
(Doulaverakis et al.,2 0 0 5; Stalmann et al., 2012). Some papers also survey existing systems
for querying linked open data in the CH domain (Giallonardo et al., 2017). However, there are
only a few articles on querying and reasoning linked open data in the CH domain, and there
is no standard methodology for evaluating the accuracy/quality of ontologies in this area.
4.2 Ontologies
The theme“ontologies” appeared as a Motor theme in the study period and highlights the
importance of ontologies in various aspects of CH (refer toFigure 9). The use of ontologies
contributes to improved semantics and interoperability, enabling effective communication
Figure 8.
Keywords network of
“cultural heritage”
theme
GKMC

and collaboration on a global scale. Visualization techniques supported by ontologies
facilitate a better understanding and representation of CH information. Furthermore,
ontologies are instrumental in 3D modeling, data mining, GIS (Geographic Information
System) and mapping, enhancing the analysis and interpretation of CH data. The
standardization and adherence to ontologies ensure consistency and quality in representing
architectural heritage, cultural differences and historical information. Integrating ontologies
with technologies like application domain extension, building information modeling and
digital twin further enhances the conservation and investigation processes.
The theme features 47 articles that discuss various applications of ontology-based
frameworks (Acierno et al.,2 0 1 7), semantic Web technologies (Bikakis et al., 2021) and
knowledge-based data enrichment (Quattrini et al.,2 0 1 7) in the context of CH conservation
and management. The articles cover topics such as creating ontologies for Andean weaving
knowledge (Brownlow et al., 2015; Isa et al.,2 0 2 0), using soft ontologies and similarity
cluster tools to discover CH resources (Collao et al., 2003), developing spatial ontology for
architectural heritage information (Noardo, 2017) and more (Kokla et al.,2 0 1 9; Noardo, 2016).
Other articles explore using knowledge graphs, ST and mixed reality applications to
visualize CH and provide personalized recommendations to visitors.
Even some articles discussed various approaches to integrating metadata for CH collections
using ontologies (Kakali et al., 2007; Stasinopoulouet al.,2 0 1 0), particularly the CIDOC CRM
ontology (Bountouri and Gergatsoulis, 2011; Gergatsouliset al., 2010a). The use of semantic
mapping (Gaitanou and Gergatsoulis, 2012), query transformation(Gergatsouliset al., 2010b)
Figure 9.
Keywords network of
“ontologies”theme
Semantic
technology

and global ontology construction(Liu, 2007; Lombardo and Pizzo, 2013;Srinivasan and Huang,
2005) are among the methods used to facilitate interoperability and knowledge sharing across
heterogeneous digital museums and collections. The articles also highlight the importance of
using the CIDOC CRM ontology as a standard reference model for mapping cultural metadata
schemas.
Although several ontologies were created for CH, none gained wide attention except
CIDOC CRM. Most scholars were creating their own ontologies for representing CH objects
or sites by extending existing ontologies. Here are some notable examples of ontologies
developed for the CH domain. The DBpedia ontology, BIBFRAME vocabulary, FOAF
vocabulary, Europeana data model, LIDO terminology, AAT ontology, BIBO ontology,
FRBR ontology, CiTO ontology, FaBiO ontology and BCO ontology are a few of the new
ontologies developed for the CH sector in addition to already existing ones like CIDOC CRM
and Dublin core metadata element set (
Naﬁs et al., 2019).
4.3 Digital humanities
The “Digital humanities” theme is another motor theme in the study period and sheds light
on essential aspects of applying ST in the digital humanities domain.Figure 10 shows
keywords that occurred in the“Digital humanities”theme. The use of ST and methodologies
has dramatically advanced the study of humanities disciplines. Metadata plays a crucial role
in organizing and describing digital resources within the context of digital humanities.
Semantic enrichment is a prominent subtheme that enhances the meaning and context of
Figure 10.
Keywords network of
“Digital humanities”
theme
GKMC

digital content. Archives and libraries hold vital importance in the digital humanities
landscape, providing access to extensive collections of digitized materials for research and
analysis. Data integration and interoperation are essential considerations in digital
humanities, enabling the combination and harmonization of diverse data sets for
interdisciplinary research.
The “Digital Humanities” theme features 14 articles covering a range of topics related to
digital humanities, focusing on the use of semantic Web technologies and ontologies to
enhance and support CH data. Some articles explore the use of semantic enrichment and
linked data to improve access and discovery of CH resources, such as museum data (
Angelis
and Kotis, 2021) and traditional dance knowledge (Kalita and Deka, 2020). At the same time,
other articles focus on developing ontological frameworks for CH instruction (Yaco and
Ramaprasad, 2019) and modeling reading processes to understand better how individuals
engage with cultural texts (Cantale et al., 2017). The use of digital humanities approaches to
visualize and evaluate CH ontologies was discussed byCheng and Chou (2022),a sw e l la s
the challenges of reconciling historical person registers as linked open data studied by
Leskinen and Hyvönen (2021). Some other critical publications are thoroughly analyzed in
the following section.
Several critical publications have contributed to theﬁeld of digital humanities and its
intersection with ST.Zeng (2019) emphasizes the importance of semantic enrichment in
enhancing Library, Archives and Museum (LAM) data, showcasing successful applications
and case studies. Hyvönen (2022) addresses the challenges of using heterogeneous and
distributed CH data in digital humanities research, presenting the Sampo model and design
principles for shared data services and semantic portals.Cristofaro et al.(2021) highlight the
signiﬁcance of representing claims in ontologies for digital humanities research, proposing
an ontology-based approach and demonstrating the Claims Annotation Tool.Cheng and
Chou (2022) explore digital humanities approaches for visualizing and evaluating CH
Ontology (CHO), offering insights into ontology evaluation methods. These publications
collectively contribute to advancing semantic enrichment, CH data utilization, claim
representation and ontology evaluation in digital humanities research.
4.4 Linked data and knowledge graph
“Linked data” is a basic theme covered in 66 articles. These articles use linked data and
knowledge graphs to improve various aspects of CH and relatedﬁelds. Figure 11
depicts
keywords that occurred in this theme. The sub-topics covered in these articles include
designing mobile recommender systems for museums (Ruotsalo et al.,2 0 1 3), creating
ontologies for classifying CH data (Naﬁs et al.,2 0 1 9), using deep semantic annotation for CH
images (Wang et al., 2020), building multilingual knowledge graph services for CH (Charles
et al., 2018) and enhancing user experiences in museums through indoor positioning (Duque
Domingo et al., 2017). In addition, the articles explore the use of linked data platforms such
as Wikidata to establish cross-domain data interoperability (Colla et al., 2021; Freire and
Isaac, 2019b). Freire and Proença (2020)also discussed how reasoning on large ontologies
could be used to explore CH repositories. Some critical articles related to knowledge graphs
and linked data are discussed below.
Charles et al. (2018) discussed the challenges and solutions in building a multilingual
knowledge graph for CH objects, whileDíaz-Rodríguez et al.(2022) proposed a methodology
combining deep learning representations with expert knowledge graphs. Earlier,
Eyharabide et al.(2021) proposed a knowledge graph embedding-based domain adaptation
approach for musical instrument recognition. Fan and Wang (2022) also proposed a
knowledge graph construction method for Chinese intangible CH based on a graph attention
Semantic
technology

network (GAT). Finally,El Vaigh et al. (2021) proposed GCNBoost, a novel method for
artwork classiﬁcation that uses label propagation through a knowledge graph.
In Colla et al. (2021) article, the use of Wikidata is explored to create rich semantic
metadata for historical archives, using SPARQL queries and integrating Wikidata into a
metadata authoring tool.Freire and Isaac’s (2019a) research analyzed the challenges and
opportunities associated with using Wikidata’s linked data in various contexts, highlighting
its potential as a resource for improving machine-to-machine communication and data
interpretation. Thalhath et al. (2021) introduced vocabularies and URIs to facilitate the
creation and maintenance of linked data resources, showcasing Wikidata as a central hub
for creating and maintaining linked data.Kesäniemi et al. (2022) described a practical
approach for nonexpert users to maintain CIDOC CRM-based knowledge graphs using
Wikibase and data input conventions, providing an example in CH data management.
Earlier, Debruyne et al.’s (2015) study focused on the technical aspects of a linked data
platform and its potential for enhancing historical record discoverability and accessibility.
Similarly, Eyharabide et al.(2019) presented MusicKG, a project using linked open data to
represent sound and music from the Middle Ages, demonstrating the potential of linked
open data for representing complex historical and cultural information.
4.5 Knowledge management
The theme “knowledge management ” appeared as a basic theme in Figure 7,w h i c h
mainly focuses on using ontology and knowledge management in preserving,
representing and disseminating CH knowledge ( Figure 12). This cluster includes 20
articles covering various topics, such as creating speci ﬁc ontologies to assess
accessibility issues in CH environments ( Martín et al., 2010), using ontologies for
knowledge management in CH catalogues ( Govedarova et al., 2008) and developing
Figure 11.
Keywords network of
“Linked data and
knowledge graph”
theme
GKMC

chatbots (Casillo et al., 2022) and online platforms to enhance learning and access to CH
resources. In addition, other articles within this cluster address topics such as merging
large ontologies using big data graph databases ( Madani et al. , 2019 ), semantic
enrichment of cartography for intangible CH (Fugini et al., 2022) and implementing
technology to support cultural tourism in Latin Latiu ( Bordoni, 2011 ). Two critical
articles related to knowledge graphs and linked data are discussed below.
Md Nasir and Md Noor’s (2010) study pondered the development of an ontology-
based Knowledge Management System (KMS) for the Batik Heritage of Malaysia. The
authors proposed using an ontology to represent the knowledge related to Batik
Heritage and explain the steps taken to construct the ontology.Govedarova et al.(2008)
presented an ontology-based case-based reasoning (CBR) architecture for knowledge
management in the BULCHINO catalogue. The system uses ontology for case
representation and retrieval and CBR for knowledge sharing and reuse. The proposed
architecture is evaluated using a set of use cases, demonstrating its effectiveness in
improving knowledge management in the catalogue.
5. Gaps and opportunities for future research
Based on the thematic analysis, there are several gaps and opportunities for future research
in thisﬁeld. Here are some of them:
Figure 12.
Keywords network of
“Knowledge
management”theme
Semantic
technology

/C15 Evaluation of ontologies: The study highlights that there is no standard
methodology for evaluating the accuracy and quality of ontologies in the CH
domain. Future research can focus on developing evaluation frameworks and
metrics to assess the effectiveness and reliability of ontologies used in STCH
research. This can help ensure the consistency and validity of ontological
representations in theﬁeld.
/C15 Querying and reasoning linked open data: The analysis points out that there is a
lack of research on querying and reasoning linked to open data in the CH domain.
Future studies can explore innovative approaches and techniques for querying and
reasoning over linked open data to extract meaningful insights and knowledge from
diverse CH data sets.
/C15 Utilization of Wikidata: The analysis highlights the potential of using Wikidata as a
resource for linked data and semantic metadata in the CH domain. Future research
can investigate how Wikidata can be leveraged for enriching and expanding CH
data sets. This can create a comprehensive and interconnected knowledge base for
CH research.
/C15 Cultural mapping: Future research can focus on developing a cultural mapping
portal that uses ST to integrate data from diverse sources encompassing tangible
and intangible cultural assets. This portal would provide querying, indexing and
visualization tools, enhancing the accessibility and exploration of cultural
information.
/C15 Ontologies for intangible CH: The study identiﬁed several ontologies developed for
CH, but only a limited number are accessible online. Future research can prioritize
the development of ontologies for intangible CH, particularly focusing on festivals
and practices.
/C15 Data model for heritage sites: Future research can focus on developing a data model
for heritage sites that incorporates points of interest, spatial information and
ontology. This model would enable users to explore their desired information about
speciﬁc places within heritage sites. By implementing this data model, location-
based services and applications could be effectively used in heritage sites.
/C15 Sustainable CH information system: Future research could be devoted to developing
a sustainable CH information system by using semantic networks in Web-based
information search systems.
6. Conclusion
The bibliometric analysis of 580 articles from WoS and Scopus databases, published
between 1999 and 2022, offers a comprehensive overview of the current state of research on
STCH. The study reveals signiﬁcant growth in STCH research since 2008, reaching its peak
in 2021. Conference papers and articles were the most prevalent document types, while
critical research keywords included ontologies, digital humanities, linked data, CH and
knowledge management. Italy emerged as the leading contributor in terms of publications
and citations, followed by Greece, China, France, the UK and the USA. Eero Hyvönen and
Vincenzo Lombardo were identiﬁed as the most productive authors, with the University of
Turin standing out as the most inﬂuential institution in STCH research. Future research can
focus on developing evaluation frameworks and metrics for ontologies in CH, exploring
querying and reasoning methods for linked open data and leveraging Wikidata as a
GKMC

resource for enriching CH data sets. In addition, research can concentrate on developing a
cultural mapping portal, ontologies for intangible CH, a data model for heritage sites and a
sustainable CH information system using semantic networks. Theseﬁndings can beneﬁt
researchers, practitioners and policymakers by identifying research gaps, fostering potential
collaborations and guiding future research directions.
References
Acharyya, T., Sudarsan, D., Mishra, M., Santos, C.A.G., Chand, P., da Silva, R.M. and Pradhan, S. (2023),
“Contextualizing the lake ecosystem syndromes and research development activities in Chilika
Lake (Odisha Coast, India): a bibliometric overview (1970–2021)”, Wetlands Ecology and
Management, Vol. 31 No. 4, pp. 1-21, doi:10.1007/s11273-023-09930-7.
Acierno, M., Cursi, S., Simeone, D. and Fiorani, D. (2017),“Architectural heritage knowledge modelling:
an ontology-based framework for conservation process”, Journal of Cultural Heritage, Vol. 24,
pp. 124-133, doi:10.1016/j.culher.2016.09.010.
Angelis, S. and Kotis, K. (2021),“Generating and exploiting semantically enriched, integrated, linked
and open museum data”, pp. 367-379, doi:10.1007/978-3-030-71903-6_34.
Aria, M. and Cuccurullo, C. (2017), “Bibliometrix: an R-tool for comprehensive science mapping
analysis”, Journal of Informetrics, Vol. 11 No. 4, pp. 959-975, doi:10.1016/j.joi.2017.08.007.
Benjamins, V.R., Contreras, J., Bl/C19azquez, M., Dodero, J.M., Garcia, A., Navas, E., Hernandez, F. and Wert,
C. (2004),Cultural heritage and the semantic web, pp. 433-444, doi:10.1007/978-3-540-25956-5_30.
Benouaret, I. and Lenne, D. (2015), “Combining semantic and collaborative recommendations to
generate personalized museum tours”, New Trends in Databases and Information Systems.
ADBIS 2015. Communications in Computer and Information Science Springer, Cham,
pp. 477-487, doi:10.1007/978-3-319-23201-0_48.
Bikakis, A., Hyvönen, E., Jean, S., Markhoff, B. and Mosca, A. (2021),“Editorial: special issue on
semantic web for cultural heritage”, Semantic Web, Vol. 12 No. 2, pp. 163-167, doi:10.3233/SW-
210425.
Bordoni, L. (2011),“Technologies to support cultural tourism for Latin Latium”, Journal of Hospitality
and Tourism Technology, Vol. 2 No. 2, pp. 96-104, doi:10.1108/17579881111154218.
Bountouri, L. and Gergatsoulis, M. (2011),“The semantic mapping of archival metadata to the CIDOC
CRM ontology”, Journal of Archival Organization, Vol. 9 Nos 3/4, pp. 174-207, doi:10.1080/
15332748.2011.650124.
Brownlow, R., Capuzzi, S., Helmer, S., Martins, L., Normann, I. and Poulovassilis, A. (2015),“An
ontological approach to creating an Andean weaving knowledge base”, Journal on Computing
and Cultural Heritage, Vol. 8 No. 2, doi:10.1145/2700427.
Cacciotti, R. (2015),“Integrated knowledge-based tools for documenting and monitoring damages to
built heritage”, The International Archives of the Photogrammetry, Remote Sensing and Spatial
Information Sciences, Vol. XL-5/W7, pp. 57-63, doi:10.5194/isprsarchives-XL-5-W7-57-2015.
Cacciotti, R., Valach, J., Kuneš,P . ,/C20Cernõanský, M., Blaško, M. and K/C20remen, P. (2013),“Monument
damage information system (MONDIS): an ontological approach to cultural heritage
documentation”, ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial
Information Sciences, Vol. II-5/W1, pp. 55-60, doi:10.5194/isprsannals-II-5-W1-55-2013.
Callon, M., Courtial, J.P. and Laville, F. (1991),“Co-word analysis as a tool for describing the network of
interactions between basic and technological research: the case of polymer chemistry ”,
Scientometrics, Vol. 22 No. 1, pp. 155-205, doi:10.1007/BF02019280.
Cantale, C., Cantone, D., Nicolosi-Asmundo, M. and Santamaria, D.F. (2017),“Distant reading through
ontologies: the case study of Catania’s Benedictines monastery”, JLIS.It, Vol. 8 No. 3, pp. 205-219,
doi: 10.4403/jlis.it-12342.
Semantic
technology

Carboni, N. and de Luca, L. (2016),“Towards a conceptual foundation for documenting tangible and
intangible elements of a cultural object”, Digital Applications in Archaeology and Cultural
Heritage, Vol. 3 No. 4, pp. 108-116, doi:10.1016/j.daach.2016.11.001.
Carboni, N. and de Luca, L. (2017),“Towards a semantic documentation of heritage objects through
visual and iconographical representations”, International Information and Library Review,
Vol. 49 No. 3, pp. 207-217, doi:10.1080/10572317.2017.1353374.
Casillo, M., De Santo, M., Mosca, R. and Santaniello, D. (2022),“An Ontology-based Chatbot to enhance
experiential learning in a cultural heritage scenario”, Frontiers in Artiﬁcial Intelligence, Vol. 5,
doi: 10.3389/frai.2022.808281.
Charles, V., Manguinhas, H., Isaac, A., Freire, N. and Gordea, S. (2018),“Designing a multilingual
knowledge graph as a service for cultural heritage– some challenges and solutions”, International
Conference on Dublin Core and Metadata Applications, DCMI 2018, 2018-Septe, pp. 29-40,
available at: www.scopus.com/inward/record.uri?eid¼2-s2.0-85056832500&partnerID¼40&
md5¼9cf7d7474cff6f34ccd3647fc4cfc8a6
Cheng, Y.-J. and Chou, S.-L. (2022),“Using digital humanity approaches to visualize and evaluate the cultural
heritage ontology”, The Electronic Library, Vol. 40 Nos 1/2, pp. 83-98, doi:10.1108/EL-09-2021-0171.
Cobo, M.J., L/C19opez-Herrera, A.G., Herrera-Viedma, E. and Herrera, F. (2012),“SciMAT: a new science
mapping analysis software tool”, Journal of the American Society for Information Science and
Technology, Vol. 63 No. 8, pp. 1609-1630, doi:10.1002/asi.22688.
Colla, D., Goy, A., Leontino, M. and Magro, D. (2021),“Wikidata support in the creation of rich semantic
metadata for historical archives”, Applied Sciences (Switzerland), Vol. 11 No. 10, doi:10.3390/
app11104378.
Collao, A.J., Jr, Diaz-Kommonen, L., Kaipainen, M. and Pietarila, J. (2003),“Soft ontologies and similarity
cluster tools to facilitate exploration and discovery of cultural heritage resources”, 14th
International Workshop on Database and Expert Systems Applications, DEXA 2003, 2003-
Janua, pp. 75-79, doi:10.1109/DEXA.2003.1232001.
Cristofaro, S., Sanﬁlippo, E.M., Sichera, P. and Spampinato, D. (2021),Towards the Representation of
Claims in Ontologies for the Digital Humanities, SWODCH, Las Vegas.
Damova, M. and Dannells, D. (2011),“Reasonable view of linked data for cultural heritage”, pp. 17-24,
doi: 10.1007/978-3-642-23163-6_3.
De Angelis, A., Gasparetti, F., Micarelli, A. and Sansonetti, G. (2017),“A social cultural recommender
based on linked open data”, Adjunct Publication of the 25th Conference on User Modeling,
Adaptation and Personalization, pp. 329-332, doi:10.1145/3099023.3099092.
Debruyne, C., Beyan, O.D., Grant, R., Collins, S. and Decker, S. (2015), in Kapidakis, S. Mazurek, C. and
Werla M. (Eds),On a linked data platform for Irish historical vital records, Springer International
Publishing, pp. 99-110, doi:10.1007/978-3-319-24592-8_8.
Díaz-Rodríguez, N., Lamas, A., Sanchez, J., Franchi, G., Donadello, I., Tabik, S., Filliat, D., Cruz, P., Montes,
R. and Herrera, F. (2022),“EXplainable Neural-Symbolic learning (X-NeSyL) methodology to fuse
deep learning representations with expert knowledge graphs: the MonuMAI cultural heritage use
case”, Information Fusion, Vol. 79, pp. 58-83, doi:10.1016/j.inffus.2021.09.022.
Doulaverakis, C., Kompatsiaris, Y. and Strintzis, M.G. (2005),“Ontology-based access to multimedia
cultural heritage collections – The REACH project”, EUROCON 2005 – The International
Conference on“Computer as a Tool, p. 151-154, doi:
10.1109/EURCON.2005.1629881.
Duque Domingo, J., Cerrada, C., Valero, E. and Cerrada, J.A. (2017),“A semantic approach to enrich user
experience in museums through indoor positioning”, in S. P., B. J. and O. S.F. (Eds),11th
International Conference on Ubiquitous Computing and Ambient Intelligence, UCAmI 2017:
LNCS, Springer Verlag, Vol. 10586, pp. 612-623, doi:10.1007/978-3-319-67585-5_60.
El Vaigh, C.B., Garcia, N., Renoust, B., Chu, C., Nakashima, Y. and Nagahara, H. (2021),“GCNBoost:
Artwork classiﬁcation by label propagation through a knowledge graph”, 11th ACM International
Conference on Multimedia Retrieval, ICMR 2021, pp. 92-100, doi:10.1145/3460426.3463636.
GKMC

Eyharabide, V., Bekkouch, I.E.I. and Constantin, N.D. (2021),“Knowledge graph embedding-based
domain adaptation for musical instrument recognition”, Computers, Vol. 10 No. 8, doi:10.3390/
computers10080094.
Eyharabide, V., Lully, V. and Morel, F. (2019),“MusicKG: Representations of sound and music in the
middle ages as linked open data”, in A. M., S.-V. Y., C.-M. P., M. M., P. T., and S. H. (Eds),15th
International Conference on Semantic Systems, SEMANTiCS 2019: LNCS, Springer, Vol. 11702,
pp. 57-63. doi:10.1007/978-3-030-33220-4_5.
Fan, T. and Wang, H. (2022),“Research of Chinese intangible cultural heritage knowledge graph
construction and attribute value extraction with graph attention network ”, Information
Processing and Management, Vol. 59 No. 1, p. 102753, doi:10.1016/j.ipm.2021.102753.
Freire, N. and Isaac, A. (2019a),“Technical usability of Wikidata’s linked data: Evaluation of machine
interoperability and data interpretability ”, in A.W. and C.R. (Eds), 22nd International
Conference on Business Information Systems, BIS 2019: LNBIP, Springer, Vol. 373, pp. 556-567,
doi: 10.1007/978-3-030-36691-9_47.
Freire, N. and Isaac, A. (2019b),“Wikidata’s linked data for cultural heritage digital resources: an
evaluation based on the Europeana data model ”, 9th Dublin Core Metadata Initiative
International Conference on Dublin Core and Metadata Applications, DCMI 2019, pp. 59-68,
available at: www.scopus.com/inward/record.uri?eid¼2-s2.0-85088228559&partnerID¼40&
md5¼8aee665ce2663d104fdd3cbbad383845
Freire, N. and Proença, D. (2020),“RDF reasoning on large ontologies: a study on cultural heritage and
wikidata”, in M. I., I. L. and P. E. (Eds),16th IFIP WG 12.5 International Conference on Artiﬁcial
Intelligence Applications and Innovations, AIAI 2020: IFIP, Springer, Vol. 583, pp. 381-393, doi:
10.1007/978-3-030-49161-1_32.
Freire, N., Voorburg, R., Cornelissen, R., de Valk, S., Meijers, E. and Isaac, A. (2019),“Aggregation of
linked data in the cultural heritage domain: a case study in the Europeana network ”,
Information, Vol. 10 No. 8, p. 252, doi:10.3390/info10080252.
Fugini, M., Finocchi, J. and Rossi, E. (2022), “Semantic adaptive enrichment of cartography for
intangible cultural heritage and citizen journalism”, Lecture Notes in Networks and Systems,
Vol. 438, pp. 173-185, doi:10.1007/978-3-030-98012-2_14.
Gaitanou, P. and Gergatsoulis, M. (2012),“Deﬁning a semantic mapping of VRA core 4.0 to the CIDOC
conceptual reference model”, International Journal of Metadata, Semantics and Ontologies, Vol. 7
No. 2, pp. 140-156, doi:10.1504/IJMSO.2012.050017.
Gergatsoulis, M., Bountouri, L., Gaitanou, P. and Papatheodorou, C. (2010a), “Mapping cultural
metadata schemas to CIDOC conceptual reference model”, 6th Hellenic Conference on Artiﬁcial
Intelligence: Theories, Models and Applications, SETN 2010: LNAI, Vol. 6040, pp. 321-326, doi:
10.1007/978-3-642-12842-4_37.
Gergatsoulis, M., Bountouri, L., Gaitanou, P. and Papatheodorou, C. (2010b),“Query transformation in a
CIDOC CRM based cultural metadata integration environment”, 14th European Conference on
Research and Advanced Technology for Digital Libraries, ECDL 2010: LNCS, Vol. 6273,
pp. 38-45. doi:10.1007/978-3-642-15464-5_6.
Giallonardo, E., Sorrentino, C. and Zimeo, E. (2017),“Querying a complex web-based KB for cultural
heritage preservation ”, 2nd International Conference on Knowledge Engineering and
Applications (ICKEA), pp. 183-188, doi:10.1109/ICKEA.2017.8169926.
Govedarova, N., Stoyanov, S. and Popchev, I. (2008), “An ontology based CBR architecture for
knowledge management in BULCHINO catalogue”, 9th International Conference on Computer
Systems and Technologies and Workshop for PhD Students in Computing, CompSysTech’08, doi:
10.1145/1500879.1500953.
Goy, A., Colla, D., Magro, D., Accornero, C., Loreto, F. and Radicioni, D.P. (2020),“Building semantic
metadata for historical archives through an ontology-driven user interface ”, Journal on
Computing and Cultural Heritage, Vol. 13 No. 3, pp. 1-36, doi:10.1145/3402440.
Semantic
technology

Grieser, K., Baldwin, T., Bohnert, F. and Sonenberg, L. (2011),“Using ontological and document
similarity to estimate museum exhibit relatedness”, Journal on Computing and Cultural
Heritage, Vol. 3 No. 3, pp. 1-20, doi:10.1145/1921614.1921617.
Hyvönen, E. (2012),“Publishing and using cultural heritage linked data on the semantic web”, Synthesis
Lectures on the Semantic Web: theory and Technology, Vol. 2 No. 1, pp. 1-159, doi:10.1007/978-3-
031-79438-4.
Hyvönen, E. (2022), “Digital humanities on the semantic web: Sampo model and portal series”,
Semantic Web, Vol. 14 No. 4, pp. 1-16, doi:10.3233/sw-223034.
Isa, W.M.W., Zin, N.A.M., Rosdi, F., Sarim, H.M., Wook, T.S.M.T., Husin, S., Jusoh, S. and Ali, S.K.L.
(2020), “An ontological approach for creating a brassware craft knowledge base”, IEEE Access,
Vol. 8, pp. 163434-163446, doi:10.1109/ACCESS.2020.3022795.
Kakali, C., Lourdi, I., Stasinopoulou, T., Bountouri, L., Papatheodorou, C., Doerr, M. and Gergatsoulis,
M. (2007),“Integrating Dublin core metadata for cultural heritage collections using ontologies”,
International Conference on Dublin Core and Metadata Applications, pp. 128-139.
Kalita, D. and Deka, D. (2020),“Ontology for preserving the knowledge base of traditional dances
(OTD)”, The Electronic Library, Vol. 38 No. 4, pp. 785-803, doi:10.1108/EL-11-2019-0258.
Kalita, D. and Deka, D. (2021),“Searching the great metadata timeline: a review of library metadata
standards from linear cataloguing rules to ontology inspired metadata standards”, Library Hi
Tech, Vol. 39 No. 1, pp. 190-204, doi:10.1108/LHT-08-2019-0168.
Kesäniemi, J., Koho, M. and Hyvönen, E. (2022),“Using Wikibase for managing cultural heritage linked
open data based on CIDOC CRM”, New Trends in Database and Information Systems: ADBIS
2022 Short Papers, Doctoral Consortium and Workshops: DOING, K-GALS, MADEISD,
MegaData, SWODCH,Turin, September 5–8, 2022, pp. 542-549.
Kokla, M., Mostafavi, M.A., Noardo, F. and Spanò, A. (2019), “Towards building a semantic
formalization of (small) historical centres”, in P.V., G.A., S.M., R.F., B.R., P.M., and C.L. (Eds),2nd
International Conference of Geomatics and Restoration, GEORES 2019 (Issue 2/W11 ,
Copernicus GmbH, Vol. 42, pp. 675-683, doi:10.5194/isprs-Archives-XLII-2-W11-675-2019.
Kuo, C.-L., Cheng, Y.-M., Lu, Y.-C., Lin, Y.-C., Yang, W.-B. and Yen, Y.-N. (2018),“A framework for semantic
interoperability in 3D tangible cultural heritage in Taiwan”, pp. 21-29, doi:
10.1007/978-3-030-01765-1_3.
Landorf, C. (2020), “Digital cultural heritage: future visions, a landscape perspective’ international
conference report”, Built Heritage, Vol. 4 No. 1, p. 7, doi:10.1186/s43238-020-00007-5.
Leskinen, P. and Hyvönen, E. (2021),“Reconciling and using historical person registers as linked open data
in the AcademySampo portal and data service”, in H.A., B.E., D.S., F.A., D.Y., B.P., H.A., D.M. and
A.H. (Eds.),20th International Semantic Web Conference, ISWC 2021: LNCS, Springer Science and
Business Media Deutschland GmbH, Vol. 12922, pp. 714-730, doi:10.1007/978-3-030-88361-4_42.
Leskinen, P., Tuominen, J., Heino, E. and Hyvönen, E. (2017),“An ontology and data infrastructure for
publishing and using biographical linked data”, WHiSe@ ISWC, pp. 15-26.
Liu, H.-Z. (2007),“Global ontology construction for heterogeneous digital museums. 6th”, International
Conference on Machine Learning and Cybernetics, ICMLC , pp. 4015-4019, doi: 10.1109/
ICMLC.2007.4370848.
Lodi, G., Asprino, L., Nuzzolese, AG, Presutti, V, Gangemi, A., Recupero, DR, Veninata, C and Orsini, A
(2017),“Semantic web for cultural heritage valorisation”,i nH a i - J e w ,S .( E d ) ,Data Analytics in Digital
Humanities, Multimedia Systems and Applications Springer, Cham, doi:10.1007/978-3-319-54499-1_1.
Lombardo, V. and Pizzo, A. (2013),“Modeling and visualization of drama heritage”, 17th International
Conference on Image Analysis and Processing, ICIAP 2013: LNCS, Vol. 8158, pp. 288-297, doi:
10.1007/978-3-642-41190-8_31.
Lombardo, V., Damiano, R., Pizzo, A. and Terzulli, C. (2017),“The intangible nature of drama documents”,
Proceedings of the 2017 ACM Symposium on Document Engineering, pp. 173-182. doi:10.1145/
3103010.3103019.
GKMC

Loures, L. (2008),“Industrial heritage: the past in the future of the city”, WSEAS Transactions on
Environment and Development, Vol. 4 No. 8, pp. 687-696.
Madani, K., Russo, C. and Rinaldi, A.M. (2019),“Merging large ontologies using BigData GraphDB”,
IEEE International Conference on Big Data, Big Data 2019 Institute of Electrical and
Electronics Engineers, pp. 2383-2392, doi:10.1109/BigData47090.2019.9005991.
Martín, P., Valverde, B., Muñoz, M., Martínez, M. and Finat, J. (2010),“A speciﬁc ontology and related
web services for assessing accessibility issues in cultural heritage environments”, in L.S., V.B.,
D.S., and B.M.A. (Eds),1st International Workshop on Pervasive Web Mapping, Geoprocessing
and Services, WebMGS 2010. International Society for Photogrammetry and Remote Sensing.
available at: www.scopus.com/inward/record.uri?eid¼2-s2.0-84923928230&partnerID¼40&
md5¼871203d4e9d3ccf727af86abf2175ba1
Md Nasir, S.A. and Md Noor, N.L. (2010),“Integrating ontology-based approach in knowledge management
system (KMS): construction of batik heritage ontology”, 2010 International Conference on Science and
Social Research, CSSR 2010, pp. 674-679, doi:10.1109/CSSR.2010.5773866.
M i s h r a ,M . ,D e s u l ,S . ,S a n t o s ,C . A . G . ,M i s h r a ,S . K . ,K a m a l ,A . H . M . ,G o s w a m i ,S . ,... and Baral, K. (2023),“A
bibliometric analysis of sustainable development goals (SDGs): a review of progress, challenges,
and opportunities”, Environment, Development and Sustainability,V o l .1 ,p p .1 - 4 3 ,d o i :10.1007/
s10668-023-03225-w.
Mishra, M., Dash, M.K., Sudarsan, D., Santos, C.A.G., Mishra, S.K., Kar, D., Bhat, I.A., Panda, B.K.,
Sethy, M. and Silva, R.M. (2022),“Assessment of trend and current pattern of open educational
resources: a bibliometric analysis”, The Journal of Academic Librarianship, Vol. 48 No. 3,
p. 102520, doi:10.1016/j.acalib.2022.102520.
Moraitou, E., Christodoulou, Y. and Caridakis, G. (2022), “Semantic models and services for
conservation and restoration of cultural heritage: a comprehensive survey”, Semantic Web,
Vol. 14 No. 2, pp. 1-31, doi:10.3233/sw-223105.
Naﬁs, F., Yahyaouy, A. and Aghoutane, B. (2019),“Ontologies for the classiﬁcation of cultural heritage
data”, International Conference on Wireless Technologies, Embedded and Intelligent Systems
(WITS), pp. 1–7, doi:10.1109/WITS.2019.8723850.
Niang, C., Marinica, C., Markhoff, B., Leboucher, E., Malavergne, O., Bouiller, L., Darrieumerlou, C. and
Laissus, F. (2017),“Supporting semantic interoperability in conservation-restoration domain”,
Journal on Computing and Cultural Heritage, Vol. 10 No. 3, pp. 1-20, doi:10.1145/3097571.
Noardo, F. (2016),“Architectural heritage ontology concepts and some practical issues”, in R.J.G. and G.
C. (Eds), 2nd International Conference on Geographical Information Systems Theory,
Applications and Management, GISTAM 2016 , SciTePress, pp. 168-179, doi: 10.5220/
0005830901680179.
Noardo, F. (2017),“A spatial ontology for architectural heritage information”, in G. C., L. R., and R. J.G.
(Eds), 2nd International Conference on Geographical Information Systems Theory, Applications
and Management, GISTAM 2016, Springer Verlag, Vol. 741, pp. 143-163, doi:10.1007/978-3-
319-62618-5_9.
Noor, S. and Martinez, K. (2009), “Using social data as context for making recommendations”,
Proceedings of the 1st Workshop on Context, Information and Ontologies, pp. 1-8, doi:10.1145/
1552262.1552269.
O’Keeffe, T. (2014),“Heritage and archaeology”, in Smith, C. (Eds),Encyclopedia of Global Archaeology,
Springer, New York, NY, doi:10.1007/978-1-4419-0465-2_1053.
O’Neill, B. and Stapleton, L. (2022),“Digital cultural heritage standards: from silo to semantic web”, AI
and Society, Vol. 37 No. 3, pp. 891-903, doi:10.1007/s00146-021-01371-1.
Patra, R.K., Pandey, N. and Sudarsan, D. (2022),“Bibliometric analysis of fake news indexed in Web of
Science and Scopus (2001-2020)”, Global Knowledge, Memory and Communication, Vol. 72 Nos 6/7,
doi:10.1108/GKMC-11-2021-0177.
Semantic
technology

Quattrini, R., Pierdicca, R. and Morbidoni, C. (2017),“Knowledge-based data enrichment for HBIM: exploring
high-quality models using the semantic-web”, Journal of Cultural Heritage, Vol. 28, pp. 129-139.
Ruotsalo, T., Haav, K., Stoyanov, A., Roche, S., Fani, E., Deliai, R., Mäkelä, E., Kauppinen, T. and
Hyvönen, E. (2013),“SMARTMUSEUM: a mobile recommender system for the web of data”,
Journal of Web Semantics, Vol. 20, pp. 50-67.
Sansonetti, G., Gasparetti, F., Micarelli, A., Cena, F. and Gena, C. (2019), “Enhancing cultural
recommendations through social and linked open data”, User Modeling and User-Adapted
Interaction, Vol. 29 No. 1, pp. 121-159, doi:10.1007/s11257-019-09225-8.
Srinivasan, R. and Huang, J. (2005),“Fluid ontologies for digital museums”, International Journal on
Digital Libraries, Vol. 5 No. 3, pp. 193-204, doi:10.1007/s00799-004-0105-9.
Stalmann, K., Wegener, D., Doerr, M., Josef Hill. and H., Friesen. (2012),“Semantic-based retrieval of
cultural heritage multimedia objects”, International Journal of Semantic Computing, Vol. 6 No. 3,
pp. 315-327, doi:10.1142/S1793351X12400107.
Stasinopoulou, T., Bountouri, L., Kakali, C., Lourdi, I., Papatheodorou, C., Doerr, M. and Gergatsoulis,
M. (2010),“Ontology-Based metadata integration in the cultural heritage domain”, Asian Digital
Libraries. Looking Back 10 Years and Forging New Frontiers, Springer, Berlin Heidelberg,
pp. 165-175, doi:10.1007/978-3-540-77094-7_25.
Stovel, H., Stanley-Price, N. and Killick, R. (2005),“Conservation of living religious heritage”, In
Conservation of Living Religious Heritage: Papers from the ICCROM 2003 Forum on Living
Religious Heritage: Conserving the Sacred, ICCROM, Rome, pp. 1-11.
Thalhath, N., Nagamori, M., Sakaguchi, T. and Sugimoto, S. (2021),“Wikidata centric vocabularies and URIs
for linking data in semantic web driven digital curation”,i nG . E .a n dO . - P .M .( E d s . ) ,14th International
Conference on Metadata and Semantics Research, MTSR 2020: CCIS, Springer Science and Business
Media Deutschland GmbH, Vol. 1355, pp. 336-344, doi:10.1007/978-3-030-71903-6_31.
UNESCO World Heritage Centre (2021),“Natural world heritage [webpage]”, available at:
https://whc.
unesco.org/en/natural-world-heritage/
Vecco, M. (2010),“Ad eﬁnition of cultural heritage: from the tangible to the intangible”, Journal of
Cultural Heritage, Vol. 11 No. 3, pp. 321-324, doi:10.1016/j.culher.2010.01.006.
Vlachidis, A. and Tudhope, D. (2016),“A knowledge-based approach to information extraction for
semantic interoperability in the archaeology domain”, Journal of the Association for Information
Science and Technology, Vol. 67 No. 5, pp. 1138-1152, doi:10.1002/asi.23485.
Wang, X., Song, N., Liu, X. and Xu, L. (2020),“Data modeling and evaluation of deep semantic
annotation for cultural heritage images”, Journal of Documentation, Vol. 77 No. 4, pp. 906-925,
doi: 10.1108/JD-06-2020-0102.
Yaco, S. and Ramaprasad, A. (2019),“Informatics for cultural heritage instruction: an ontological
framework”, Journal of Documentation, Vol. 75 No. 2, pp. 230-246, doi:10.1108/JD-02-2018-0035.
Zeng, M.L. (2019),“Semantic enrichment for enhancing LAM data and supporting digital humanities.
Review article”, El Profesional de la Informaci/C19on, Vol. 28 No. 1, doi:10.3145/epi.2019.ene.03.
Further reading
Bannour, I., Marinica, C. and Bouiller, L. (2018),“CRMCR-A CIDOC-CRM extension for supporting
semantic interoperability in the conservation and restoration domain”,i nA . ,A . C .a n dTH .( E d s ) ,
3rd Digital Heritage International Congress, Digital Heritage 2018. Institute of Electrical and
Electronics Engineers Inc., ETIS, UMR 8051 University Paris Seine, University Cergy-Pontoise,
ENSEA, CNRS, Cergy-Pontoise.
Cantone, D., Nicolosi-Asmundo, M., Santamaria, D.F. and Trapani, F. (2015),Ontoceramic: An OWL
ontology for ceramics classiﬁcation. in A., D., M., M., M., V. (Eds),30th Italian Conference on
Computational Logic, CILC 2015. CEUR-WS, Department of Mathematics and Computer
Science, University of Catania, pp. 122-127.
GKMC

Doerr, M. (2003), “The CIDOC conceptual reference module: an ontological approach to semantic
interoperability of metadata”, AI Magazine, Vol. 24 No. 3, p. 75.
Goy, A., Magro, D. and Rovera, M. (2018),“On the role of thematic roles in a historical event ontology”,
Applied Ontology, Vol. 13 No. 1, pp. 19-39, doi:10.3233/AO-170192.
Hellmund, T., Hertweck, P. and Hilbring, D. (2018),“Introducing the Heracles ontology— semantics for
cultural heritage management”, Heritage, Vol. 1 No. 2, pp. 377-391, doi:10.3390/heritage1020026.
Júnior, R.V.S., Oliveira, G.M.C. and Neto, F.M.M. (2020),“An ontology used to support learning in the
ﬁeld of heritage education”, Proceedings of the 10th Euro-American Conference on Telematics
and Information Systems, ACM, New York, NY, pp. 1-5.
Ma, T.-T., Benferhat, S. and Bouraoui, Z. (2018), “An ontology-based modelling of Vietnamese
traditional dances”, 30th International Conference on Software Engineering and Knowledge
Engineering, SEKE 2018. Knowledge Systems Institute Graduate School, CICT, Can Tho
University, Viet Nam, pp. 64-67.
Oldman, D. and Labs, C.R.M. (2014),“The CIDOC conceptual reference model (CIDOC-CRM): primer”,
CIDOC-CRM Off, available at:www.cidoc-crm.org/sites/default/ﬁles/CRMPrimer_v1.1_1.pdf
Tudorache, T. (2020), “Ontology engineering: Current state, challenges, and future directions ”,
Semantic Web, Vol. 11 No. 1, pp. 125-138, doi:10.3233/SW-190382.
van Hage, W.R., Malais/C19e, V., Segers, R., Hollink, L. and Schreiber, G. (2011),“Design and use of the
simple event model (SEM)”, Journal of Web Semantics, Vol. 9 No. 2, pp. 128-136, doi:10.1016/j.
websem.2011.03.003.
Wei, T., Roche, C., Papadopoulou, M. and Jia, Y. (2020),“An ontology of Chinese ceramic vases”,i nD .A ,
J. D, J. F (Eds),12th International Conference on Knowledge Discovery and Information Retrieval,
KDIR 2020 – Part of the 12th International Joint Conference on Knowledge Discovery,
Knowledge Engineering and Knowledge Management, IC3K 2020 . SciTePress, Condillac
Research Group of LISTIC Lab, University Savoie Mont-Blanc, Rue du Lac Majeur, Le Bourget
du Lac, pp. 53-63.
Wei, T., Roche, C., Papadopoulou, M. and Jia, Y. (2022),“The TAO CI ontology of vases of the Ming and
Qing dynasties”, Applied Ontology, Vol. 17 No. 3, pp. 423-441, doi:10.3233/AO-220270.
Corresponding author
Raj Kishore Patra can be contacted at:
rkpatra_media@yahoo.co.in
For instructions on how to order reprints of this article, please visit our website:
www.emeraldgrouppublishing.com/licensing/reprints.htm
Or contact us for further details:permissions@emeraldinsight.com
Semantic
technology
View publication stats
