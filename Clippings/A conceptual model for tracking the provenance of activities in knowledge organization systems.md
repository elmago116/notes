---
title: A conceptual model for tracking the provenance of activities in knowledge organization systems
source: https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/A-conceptual-model-for-tracking-the-provenance-of
authors:
  - Choi Inkyung
  - Cheng Yi-Yun
published: 2024-09-23
created: 2025-11-28
description: Purpose. The purpose of this study is to develop a conceptual model, ProvKOS, for tracking the provenance of change activities in a knowledge organization
tags:
  - tech/KOS
  - tech/provenance
year: 2025
doi: https://doi-org.sire.ub.edu/10.1108/JD-05-2024-0101
---
[[ A conceptual model for tracking the provenance of activities in knowledge organization systems]]

[Skip to Main Content](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/#skipNav)

[Skip Nav Destination](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/#)

- [Previous Article](https://www-emerald-com.sire.ub.edu/jd/article/81/1/128/1242143/Bibliographical-foundations-of-information-science)
- [Next Article](https://www-emerald-com.sire.ub.edu/jd/article/81/1/168/1242150/Understanding-complex-casual-leisure-information)

Purpose

The purpose of this study is to develop a conceptual model, ProvKOS, for tracking the provenance of change activities in a knowledge organization system (KOS). By extending current provenance practices, this model represents dynamic changes in a KOS more effectively.

Design/methodology/approach

We take a five-step approach to develop the conceptual model, including content analysis of KOS editorial data, environmental scan of existing provenance models, development of persona-specific provenance questions and a participatory design with stakeholders to ensure the model’s utility.

Findings

We introduce (1) a taxonomy of editorial activities for a KOS; (2) a conceptual model ProvKOS, which extends existing models PROV and Simple Knowledge Organization Systems (SKOS). We also provide detailed data dictionaries for the entities, activities and warrants classes proposed in the model. A use case on “gender dysphoria” in Dewey Decimal Classifications (DDCs) is provided to illustrate the implementation of ProvKOS. This shows ProvKOS’s ability to capture KOS changes effectively and to link external resources relating to the changes.

Research limitations/implications

Further validation may be needed to implement the ProvKOS model across various types of KOSs.

Practical implications

ProvKOS can help improve machine readability, querying and analysis of a KOS. Especially within the linked data environment, the enhanced provenance documentation through ProvKOS can enable a network of KOSs, which will then inform better linked data or knowledge graph designs.

Social implications

By facilitating better tracking of changes within a KOS and across KOSs, ProvKOS can enhance the accessibility and usability of knowledge bases across different cultural and social contexts, thus better supporting inclusive information practices.

Originality/value

The proposed model is novel in two ways: one, its ability to represent dynamic change activities in a KOS, which has not been discussed anywhere else; two, it supports the interconnectivity across KOSs by providing a “warrant” class to substantiate the context of changes.

## Notes for digital libraries article
- **Process-driven**:
  - “The purpose of this study is to develop a conceptual model, ProvKOS, for tracking the provenance of change activities in a knowledge organization system (KOS).” (Purpose)
  - “We take a five-step approach to develop the conceptual model, including content analysis of KOS editorial data, environmental scan of existing provenance models, development of persona-specific provenance questions and a participatory design with stakeholders to ensure the model’s utility.” (Design/methodology/approach)
- **Methodological tools**:
  - “We introduce (1) a taxonomy of editorial activities for a KOS; (2) a conceptual model ProvKOS, which extends existing models PROV and Simple Knowledge Organization Systems (SKOS).” (Findings)
  - “The development process of the conceptual model consists of five steps: (1) content analysis of the data; (2) environmental scanning of current provenance models; (3) developing general provenance questions; (4) participatory design involving stakeholders and (5) developing persona-specific provenance queries.” (Method section)
- **Participation level**:
  - “... participatory design involving stakeholders ...” (Design/methodology/approach) – involving editorial managers, information professionals, and researchers in refining the model.
- **Epistemic justice**:
  - “A use case on ‘gender dysphoria’ in Dewey Decimal Classifications (DDCs) is provided to illustrate the implementation of ProvKOS.” (Findings)
  - “By facilitating better tracking of changes within a KOS and across KOSs, ProvKOS can enhance the accessibility and usability of knowledge bases across different cultural and social contexts, thus better supporting inclusive information practices.” (Social implications)

Tracking the change to the elements of a knowledge organization system (KOS) over time is a long-standing research topic in the field of Information Science. For instance, scholars analyzed the change of a subject term in different versions of a bibliographic classification ([Tennis, 2012](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) or examined the historical reconstructions of a biodiversity taxonomy to interpret the choice of changes ([Montoya, 2017](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). However, these studies demonstrated the challenges in finding, accessing and analyzing changes to the elements of a KOS for the following reasons: (1) the activities that point to a change (e.g. cataloging) is a non-linear, dynamic process, and this process usually reflects the worldview of that particular point in time ([Adler *et al*., 2013](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)); (2) nuances in KOS that involve many different types of KOS elements – such as structural changes to the hierarchy or terminological changes to the labels ([Choi, 2018](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Tennis, 2007](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)); (3) evidence for the changes in KOS is not transparent – knowledge on editorial notes or contexts of the changes are very limited ([Gaudet and Dessimoz, 2017](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)).

In provenance research, time and changes are also significant areas of inquiries. Provenance is defined as how something has come to be ([Bettivia *et al*., 2022a](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/), [2023](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)), and by documenting the source and origin of a concept, item or object, provenance is often viewed as an important indicator to enable trust and reproducibility. In this study, the “somethings” are the KOSs. Extant models in provenance research such as PREMIS, PROV, ProvONE or Provlets ([Bettivia *et al*., 2023](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) emphasizes on capturing the Agent, Activity, Entity or Environment of a digitally or computationally-driven application ([Cuevas-Vincenttin *et al*., 2016](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Groth and Moreau, 2013](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)), but these models are not sufficient in capturing the nuances of changes within a KOS. Based on the PROV model, [Li and Sugimoto (2018)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) developed a model to capture provenance descriptions in metadata vocabularies, but the model’s focus on metadata vocabularies suggests that it is not applicable to other forms of KOSs. In particular, provenance descriptions of a classification system with a deep hierarchical relationships and notation practices could not be captured. Other efforts such as the Simple Knowledge Organization System (SKOS) ontology provide provenance descriptions (e.g. change notes or editorial notes), but free-text descriptions in notes are not enough to fully support capabilities to query and analyze the complex changes within a KOS.

In this research, we aim at enhancing the change activities to elements of a KOS to support long-term provenance practices for a KOS management. We demonstrate the implementation of our model on the case of bibliographic classification for representing the structural changes, but our research questions are positioned to address broader issues with provenance of all types of KOSs. Our two research questions are.

*RQ1.*

How can the provenance of a KOS be modeled to better represent the changes within a KOS over time?

*RQ2.*

How can the provenance documentation of a KOS enable the linkage or connection to another KOS?

To address these questions, this study proposes a conceptual model, ProvKOS, that stems from the PROV and the SKOS models to incorporate the different aspects of KOS change found in real-world examples. Then, we take these real-world examples from the DDCs. As the provenance queries are simplified to reflect the functional aspects of a KOS provenance, this paper demonstrates how the conceptual model can be implemented by KOS editorial managers, information professionals or researchers.

This conceptual model addresses provenance queries of a KOS such as follows:

- (1)
	What caused the change?
- (2)
	What is the evidence supporting the change of one subject term to another?
- (3)
	How has a concept within a KOS been changed over time?

There are two contributions of this paper. First, our work models the provenance of KOS by tracking both subtle and substantial changes with a special focus on hierarchical structures and notation practices, ensuring these alterations are captured in a standardized, machine-readable format over time. Second, beyond a particular KOS, our model facilitates the interconnection of disparate KOSs by documenting the rationale behind KOS modifications. This supports the creation of detailed networks between KOSs, which then informs future editorial decision-making and cross-KOS comparisons.

KOSs such as taxonomies, metadata schemas, classifications, thesauri and ontologies undergo frequent changes such as word meanings and usage patterns changes. The importance of documenting these changes to manage how words and meanings evolve over time has been a long-standing scholarly discussion in the field of information science. For example, [Tennis (2012)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) found shifts in the term “Eugenics” in the subject vocabularies of the DDC from a biology-related concept to a social construct over several decades. Other works by [Fox (2016)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/), [Rusquart (2023)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) and [McDonald (2020)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) explore the social and ethical implications of these shifts. However, these changes are often invisible with little or no public documentation.

To resolve the undocumented changes in KOS, researchers have highlighted several important aspects to be documented. [Tennis (2007)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) discussed the possibility of explicitly documenting nuanced changes by KOS editors such as concept replacement, concept refinement or concept reconfiguration. [Choi (2018)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) asserted that both structural and terminological changes in KOS play crucial roles to shape coherency in a KOS. Choi concluded that changes to a concept’s class number (structural change) and labels (terminological change) in bibliographic classifications should be considered. [Coladangelo (2021)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) highlighted the needs to capture multiple viewpoints during vocabulary creation in the context of cultural heritage knowledge. This enables not only transparency in vocabulary changes but also acknowledges the multidimensionality of a KOS.

In addition to individual researchers’ endeavors, there are also organizational efforts to track KOS changes such as the World Wide Web Consortium' (W3C’s) SKOS ontology. The primary focus of SKOS is to make a KOS compatible with the semantic web environment, and some of the classes and properties in SKOS can only support minimal documentation of KOS changes ([Ledl and Voß, 2016](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [“SKOS Primer”, n.d.](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). Documentation properties such as “skos:changeNote,” “skos:historyNote” or “skos:editorialNote” can be leveraged. However, these properties are in unstructured, paragraphed formats which pose difficulties in parsing for further querying and analysis. A more comprehensive model is still much needed to document KOS changes on the class-level to enable provenance queries.

Time and changes are the core concerns in provenance research. As defined by [Bettivia *et al.* (2022a](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/), [2023)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/), “provenance” is how something has come to be. This *something* can be conceptual, physical or digital; in this study, the *somethings* are the KOSs.

Extant models and standards in provenance research focus primarily on applications in the eScience or preservation domains, with an emphasis to manage digital and computational artifacts. The so-called “data provenance” is the ability to capture and track changes in these computational artifacts, deriving from the need to enhance reproducibility with data artifacts that are produced at a speed too fast to be captured. The PROV model is a family of W3C standards for data provenance, including many different serializations such as PROV-DM, PROV-O, PROV-N and PROV-XML ([Groth and Moreau, 2013](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). Provenance in the PROV model is described with three core components: Entity, Activity and Agent. An Entity is often described as a concept, idea or object that can be digital, physical or conceptual; the Activity in PROV is the event, process or changes associated with the Entity and the Agent is the person, software or responsible party of the occurring Activity. Extending the PROV model, ProvONE takes into account the temporal aspects of provenance and models two types of provenance: retrospective provenance and prospective provenance ([Bettivia *et al*., 2022b](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Cuevas-Vincenttin *et al*., 2016](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). Retrospective provenance is associated with an activity that already happened in the past (e.g. change logs), while prospective provenance is forward-looking and associated with what will happen in the future (e.g. workflows and recipes). The distinction between the past and the future in provenance is an useful perspective. This can help support the reproducibility of changes on a same entity over time ([Cuevas-Vincenttin *et al*., 2016](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)).

While issues surrounding data provenance gave birth to many provenance models in the eSciences community, the ability to use or extend these provenance models is a concern that transcends disciplines. For instance, [Li and Sugimoto (2018)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) extended the use of the PROV model to enhance provenance descriptions in metadata vocabularies. The Italian National Institute of Statistics (ISTAT) and Italian Agency for Digitalization (AgID) showcased the application of the PROV framework in publishing classifications in the Linked Open Data environment ([Lodi *et al*., 2014](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). However, the extent to which these current provenance models can capture the nuances of changes in a KOS and be applied to all forms of KOSs has yet to be investigated. Additionally, current provenance models and practices may contain details such as where, when or by whom a resource was created, but contextual information in these models such as *why* something has changed is limited.

As such, we propose the ProvKOS conceptual model in this study to address these gaps and answer the “whys” (or what “warrants” changes in a KOS) when documenting and tracking the provenance of KOSs.

Note that discussions on the theoretical framework of the “warrant” concept are beyond the scope of this study. In this work, we consider the utility of the warrants as “to illuminate where and how the concepts and terms in the designed systems are grounded ([Nylund, 2020](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/), p. 331)”. Nylund analyzed the concept of warrant ([Barité, 2018](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Beghtol, 1986](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) within eighteen articles in library and information science journals. We paid a special attention to *information sources’ warrant* and adopted it in our constructed model.

In this section, we highlight the development process of our conceptual model on representing KOS changes. We aim to make the development process as transparent as possible to document our own provenance in creating the conceptual model.

In exploring provenance data model addressing KOSs, we are specifically interested in whether the models provide contextual metadata surrounding data origins. We want to be able to leverage these kinds of contextual information to enhance the utility of knowledge organization systems. Based on data availability, we pay specific interests to the DDC, and we leverage cases of change in the DDC as motivating examples to help construct the conceptual model and later as an example implementation use case of the model. We envision constructing a conceptual model which could meticulously track the provenance of each data element of a KOS and documenting its evolution over time.

The DDC serves as a foundational knowledge organization system for organizing knowledge across a multitude of domains and disciplines. Its interconnected nature facilitates seamless navigation and discovery of related topics, making it an invaluable resource for information professionals worldwide. Given its wide adoption in public libraries in the USA and other countries, it is important to ensure the reliability and transparency of DDC’s change notes. However, although current editorial activities to the DDC are publicly shared, the insights to why certain class or label changed are often unobtainable due to the complexity of editorial process and documents. There is also a lack of discoverability of knowledge on the evidence of changes, regarding which external resources was discussed, documents used or other references cited. This has posed challenges to researchers and information professionals in effectively sharing, researching or analyzing DDC and in making informed decisions about a DDC concept to their specific needs.

In response to these challenges, our project focuses on enhancing the findability, accessibility, interoperability and reusability (FAIR ) of change activities of a KOS, inspired by examples from the DDC. By making provenance information such as time, location and warrants of a KOS concept visible and shareable, our model can explicitly state the insights needed to navigate and utilize a KOS effectively. This approach not only facilitates informed decision-making but also promotes collaboration and knowledge exchange within the broader information community. Furthermore, to bridge the external resources used referenced in a KOS change, our conceptual provenance model aims to connect various KOSs to the editorial decisions. By establishing connections between changes in one KOS to other KOSs, the reasons behind the changes to a KOS will be made more transparent.

This study utilizes a variety of resources to help construct the conceptual model. These resources include DDC’s Editorial Policy Committee (EPC) exhibits, OCLC’s editorial systems, WebDewey and the 23rd edition of the DDC’s machine-readable cataloging (MARC) classification data. We hope to capture all facets of a KOS that could lead a change in its provenance information in the DDC framework.

The development process of the conceptual model consists of five steps: (1) content analysis of the data; (2) environmental scanning of current provenance models; (3) developing general provenance questions; (4) participatory design involving stakeholders and (5) developing persona-specific provenance queries.

We employ a dual approach with both bottom-up and top-down strategies to develop the conceptual model. These two strategies are detailed in steps (1) and (2), which are developed in an iterative and simultaneous manner.

- (1)
	Content analysis of the data

For the bottom-up approach, data such as EPC exhibits, WebDewey and MARC classification data are analyzed to identify patterns and elements pertinent to provenance. This step involved a thorough content analysis by use of the editing process workflow, with a specific focus on changes to DDC class numbers and concept labels.

- (2)
	Environmental scanning of existing provenance models

For the top-down approach, we conduct an environmental scan to survey existing provenance models such as PROV and ProvOne, as mentioned in the related works section. Additionally, common ontologies for KOS, such as SKOS and SKOS-XL, were also reviewed to ensure the usability of these existing models on the DDC examples. We look specifically for rooms for expansion on these models, namely, if there are any elements or entities missing in describing the change activities of a KOS.

- (3)
	Developing general provenance questions

Steps 1 and 2 inform the development of this step. We develop a set of general provenance questions to capture the necessary data components of provenance. We also examine the different components of a provenance model to devise possible provenance questions a user might ask. These questions are categorized into two main groups: those focusing on tracking changes of a KOS and those gearing toward analytics of a KOS change. We list examples of these general purpose questions in [Table 1](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/).

- (4)
	Participatory design to include stakeholders

Table 1

General provenance questions

| *For tracking changes* |
| --- |
| What warrants the change of term? What warrants the relocation of class? When was the change made? |
| Who made the change? |
| What are the activities of the change? |
| How many times did the term undergo changes? |
| *For analytics* |
| What are the deprecated terms for the past 2 years? Where was this item A classified under in the year of 1990? What is the trajectory of subject B from 1910 to 2020? |
| When did the term C first appeared? |
| How many new terms were made in the new edition? How many terms are revised in the new edition? |
| What are the primary reasons of revision of terms? Which revision activity was used the most? |
| What are the most used external resource for revision? |

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613637)

In addition, we take a participatory design approach to include key stakeholders of a KOS in the conceptual model development process. For the example of DDC, we have been in close communication with editors and the linked data team members of the DDC for their iterative feedback of the model. We want to ensure the model can reflect not only the general purpose queries, but more importantly the key stakeholders’ provenance queries.

- (5)
	Persona-specific provenance queries

Drawing from our ongoing conversations with key stakeholders, we have identified the personas to represent the user groups of the conceptual model. The concept of persona has long been used by the field of Human-Computer Interaction (HCI) and adopted by software design and development ([Harley, 2015](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Nielsen, 2019](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). Personas are fictitious, specific and concrete representations of the target users. It’s utility in gaining insights about users’ goals and scenarios on designing a system has also been widely adopted by ontology design, ontology development or ontology engineering process ([Gangemi and Presutti, 2009](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Souza *et al*., 2019](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Zhang *et al*., 2024](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). The goals and scenarios captured with the personas of targeted users are useful in shaping and defining model requirements. By identifying persona-specific queries, the resulting model can address key stakeholders’ questions.

In our model, personas represent distinct user groups with varying needs and priorities concerning provenance information within knowledge organization systems. These personas include (1) editorial managers who oversee the editorial process of a KOS, (2) information professionals who use KOSs for information retrieval and analysis and (3) researchers who engage with KOSs for research activities and analysis. Specific information needs of each group and their questions are listed in [Table 2](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/).

Table 2

Persona-specific provenance questions

| User role | Main activities | Information needs | Provenance queries of interest |
| --- | --- | --- | --- |
| Editorial manager | Oversees the editorial process of KOS. Ensures the accuracy and integrity of KOS | To obtain information on changes to terms and classes within the KOS To explore the reasons behind revisions and relocations of classes To track the responsible entities for the change To understand the frequency of term revisions | What warrants the change of term? When was the change made? Who made the change? Why was the term changed? How many times did the term undergo changes? |
| Information professional | Utilizes KOS for information retrieval and analysis | To identify outdated terms To trace the trajectory and evolution of subjects over time To assess the frequency and nature of revisions To explore reasons for changes To explore the external resources used for changes | What are outdated terms? Where was item A classified under in 1990? What is the trajectory of subject B from 1910 to 2020? How many new terms were made in DDC 23 edition? What are the primary reasons for revision of terms? |
| Researcher | Engages with KOS to access information for research | To assess the reliability and relevance of terms for changes To study the trajectory and evolution of subjects over time To analyze reasons for changes To assess the external resources used for changes | What is the evidence used for the change? When did the term first appear? How many terms are revised in DDC 23? Which revision activity was used the most? |

**Source(s):** Table by authors’

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613642)

Based on our five-step development process, we find that existing provenance models fell short in describing the nuanced activities for changes in a KOS. We identify key editorial activities of a KOS and construct these into a taxonomy of activities first and later to be partially adopted into the conceptual model. Through the five-step process with content analysis, environmental scan and participatory design, we construct this taxonomy with several iterations. Our goal is to make the taxonomy of activities as simple as possible for practical use and as flexible as possible for generalizability to all KOSs. We identify two main activities of a KOS: *i* *nitiation* and *r* *evision*. For *r* *evision*, we identified five sub-activities, namely *r* *elocation*, *e* *xpansion*, *t* *runcation*, *d* *eprecation* and *r* *eplacement*. See [Figure 1](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) for a visual representation of the taxonomy, and see [Table 3](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) for the full definition and example of each activity.

Figure 1

A taxonomy of activity

Table 3

A taxonomy of activity

<table><thead align=""><tr><th>Activity</th><th>Definition</th><th>Examples for the DDC</th></tr></thead><tbody><tr><td><em>Initiation</em></td><td>A topic newly appeared; new class entity and label entity are generated</td><td>616.85277, gender dysphoria <em>first appeared</em> in Edition 23, July 2023</td></tr><tr><td><em>Revision</em></td><td colspan="2">Class and Label entities are revised in terms of the topic representations<br>Sub-activities of revision include: relocation, expansion, truncation, deprecation and replacement</td></tr><tr><td>Relocation</td><td>A concept is relocated from one class number to another class number but no hierarchical movements involved</td><td>Autism spectrum disorder <em>relocated</em> from 616.8982 to 616.95882</td></tr><tr><td>Expansion</td><td>A class number is further specified thus the class number progressed to the narrower hierarchy</td><td>Other pervasive development disorders <em>expanded</em> from 616.8588 to 616.85883<br>DDC editorial team used the term, “Continuation”</td></tr><tr><td>Truncation</td><td>A class number is generalized thus the class number moves up to the broader hierarchy</td><td>Schizophrenia <em>truncated</em> from 616.8982 to 616.898<br>DDC editorial team used the term, “Discontinuation”</td></tr><tr><td>Deprecation</td><td>A concept or representations of a concept is suspended from the system</td><td>Autism class number 616.85883 is <em>deprecated</em> after relocation</td></tr><tr><td>Replacement</td><td>A label of a concept is modified</td><td>Autism is <em>replaced</em> with autism spectrum disorder</td></tr></tbody></table>

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613646)

The presented taxonomy demonstrates how the analysis of editorial workflow of a DDC example case informs the constructions of the conceptual model. As a result, the taxonomy of editorial activities was generalized to represent the changes to elements within a KOS, from simply removing a concept like the deprecation activity to more complex actions such as expanding or truncating the concepts within a class hierarchy.

Previously, [Tennis (2007)](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) suggested types of changes on concepts in a concept scheme, suggesting the extension of SKOS ontology in order to capture more nuanced editorial changes. Those included refining, lumping and re-configuring, which are covered by “expansion” and “relocation” in this taxonomy. Those editorial changes identified by Tennis *et al*. address extension or progression of the concept scheme as exemplified by the versioning of DCMI Metadata Thesaurus from 2002 to 2004 that was used to index Dublin Core Metadata Initiative (DCMI) proceedings each year (i.e. the 2002 version of DC Terms was a list of terms and from 2003 the term list was expanded into thesaurus). The taxonomy in this paper addressed editorial changes of classification systems with a more complex relationship structure and a long history of changes and thus included “truncation,” “deprecation” and “initiation” which reflect various nuanced editorial changes. We will further discuss the applicability of the conceptual model to other types of KOSs in the Discussion section.

Conceptual models are useful graphical representations to depict how various concepts relate and function ([Cheng, 2023](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/); [Jett *et al*., 2016](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). In this section, we describe our proposed conceptual model, including data dictionary of the classes and properties.

We leverage and expand PROV and SKOS ontologies to create the ProvKOS conceptual model. In this section, we give an overview of the ProvKOS conceptual model’s core structures and a data dictionary of the classes and properties. Similar to the taxonomy of activities, we aim to construct a conceptual model that is simple and easy to use so that our key stakeholders (researchers, information professionals and editorial managers) can adopt the model suiting their information needs.

[Figure 2](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) displays the core, high-level structures of ProvKOS. We inherit core components Entity, Agent and Activity from the PROV model . We observe a need to document and connect external resources as evidence of changes in a KOS, such as mentions of other classifications, citations of recent papers, etc. Thus, we introduce a fourth component to the model “Warrant” to reflect contexts and reasons for changes. We follow the namespace conventions from PROV: the prefix “prov:” refers to classes and properties of PROV ontology, and the prefix of “ProvKOS” refers to our own creation – indicating unique classes and properties we designed to represent KOS provenance that have not been covered by other relevant data models or ontologies.

Figure 2

The core structures of ProvKOS

In this section, we explain in detail each of the core component in ProvKOS, including the definitions of the classes, sub-classes and properties. Some of the expanded terms (with prefixes “ProvKOS:”) are our own creation to reflect the KOS changes.

- (1)
	Entity

In KOSs such as taxonomies and ontologies, concepts (or vocabularies) are represented with string literals or annotated labels. In KOSs such as classifications, concepts are represented in both numeric notations and string literals. Currently, SKOS ontologies use properties for labeling a concept and notations. However, having notations and labels as *properties* instead of *classes* in an ontology can limit the capability to query these changes. To encompass different ways of representing a concept, we identify two unique *sub-classes* of entity for any KOS: Class number and Label. [Figure 3](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) illustrates the prov:Entity and the two new sub-classes.

Figure 3

Entity and sub-classes ClassNumber and Label

Class number refers to the concepts represented with numeric notations (e.g. 616.95882), whereas labels are the literal forms of the term (e.g. autism spectrum disorder.). The proposed sub-classes of Entity in our model are distinctive as they allow a class number and a label of a concept in KOSs to be the unit of change. We leverage existing vocabulary from SKOS-XL (skos extensions) for labels (skosxl:Label). ClassNumber, on the other hand, is associated with specific editorial activities that are distinct from a label in a numeric notation. ProvKOS maintains the flexibility that if one is working with a KOS that does not contain any notations (e.g. a KOS that is not a bibliographic classification system), the Label class can be sufficient to describe the changes solely without using the ClassNumber sub-class. [Table 4](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) shows the definitions for Entity, Label and Class number.

- (2)
	Activity

Table 4

Definition of entity and sub-classes label and class number

| Class | Definition | Superclass |
| --- | --- | --- |
| prov:Entity | An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary. (from PROV-O) | N/A |
| *skosxl:Label* | The class skosxl:Label is a special class of lexical entities. An instance of the class skosxl:Label is a resource and may be named with a URI. An instance of the class skosxl:Label has a single literal form. (from SKOS-XL) | prov:Entity |
| *ClassNumber* | A class number is a numeric or alphanumeric notation to represent a concept, frequently used in KOSs that has hierarchical structure. A concept is defined as a unit of thought, specific ideas or meanings established within a KOS. Class number is assignable to classify information resources. An instance of ClassNumber may be named with a URI | prov:Entity |

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613662)

The taxonomy of activities we develop specified the key editorial activities of any KOS, including two main activities, namely *Initiation* and *Revision*, and five sub-activities of Revision: *Relocation*, *Expansion*, *Truncation*, *Deprecation* and *Replacement*. For the conceptual model, we incorporate properties from the PROV model which asserts Initiation and Revision activities by using “prov:wasGeneratedBy” and “prov:wasRevisionOf” properties. Further, a PROV entity can be invalidated (or deprecated) by an activity with the “prov:wasInvalidatedBy” property. Therefore, in the conceptual model, we incorporate only the four sub-activities from our taxonomy of activities. These four sub-activities (*Expansion*, *Truncation*, *Replacement* and *Relocation*) more accurately reflect how our conceptual model extends the existing PROV model. [Figure 4](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) illustrates the model with these extended activities.

Figure 4

Activity and four ProvKOS sub-classes

Our model for the activities also encompasses other types of KOSs. The activities can be adopted in various ways to represent different levels of specificity in the nuanced KOS changes. For example, if a KOS does not contain numeric notations and most of the changes are to replace old terms with new terms, then “Replacement” can sufficiently capture the activity of this particular KOS. If a KOS is more coarse-grained and does not have various nuanced changes, one can uses the “prov:Activity” class to sufficiently represent any kinds of change. [Table 5](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) provides the full definitions for the four activities included in the conceptual model.

- (3)
	Warrant

Table 5

Definition of activity and sub-classes: Relocation, Expansion, Truncation and Replacement

| Class | Definition | Superclass |
| --- | --- | --- |
| prov: Activity | An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities. (from PROV-O) | N/A |
| *Relocation* | A relocation is a lateral movement of a concept from one position to another (e.g. from a class number to another class number) | prov:Activity |
| *Expansion* | An expansion is to expand the concept with more specificity, thus moving the class number moves down to the narrower hierarchy | prov:Activity |
| *Truncation* | A truncation is to trim the specificity of a concept, so the concept is more generalized and moves up to the broader hierarchy. (i.e. DDC editorial team used the term, “Discontinuation”) | prov:Activity |
| *Replacement* | A replacement is having a label replaced with another label | prov:Activity |

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613667)

The “Warrant” class proposed in this conceptual model is to represent external sources for decision-making on KOS changes. When KOS changes are suggested during the editorial process and discussions, we noticed that the editorial documents frequently include references to external resources. These external resources include citing editorial documents, referencing literature about a topic in discussion or connecting to other relevant concepts and concept schemes. [Figure 5](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) shows the four types of external resources for the Warrant class we create to enhance the linkage between a KOS activity and external resources.

Figure 5

ProvKOS Warrant and sub-classes Document, Literature, Concept and ConceptScheme

For example, in the DDC editorial documents, if a topic in discussion is related to medical subjects, International Classification of Diseases (ICD) and Diagnostic and Statistical Manual of Mental Disorders (DSM) are frequently referenced, we use “Concept” and “ConceptScheme”, derived from the SKOS model to represent these. The connection to external KOSs can then be further leveraged for a representation of the networked KOSs at the concept level. For example, one can aggregate linked concepts from an external KOSs to a certain DDC class and consider them as evidence of semantic similarity. [Table 6](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) provides the definitions for these external resources for Warrant.

Table 6

Definition of Warrant and sub-classes

| Class | Definition | Superclass |
| --- | --- | --- |
| *Warrant* | Any identifiable sources supporting the editorial activities of the KOS | N/A |
| *Document* | Documents are things that record the editorial process which include proposals of changes, discussions of proposals, and suggested changes and its impacts | ProvKOS: Warrant |
| skos:conceptScheme | A KOS providing an warrant for editorial decision-making (from SKOS) | ProvKOS: Warrant |
| skos:concept | A KOS concept providing an warrant for editorial decision-making (from SKOS) | ProvKOS: Warrant |
| *Literature* | Citable publications (e.g. scholarly articles, web links, news report) providing an warrant for editorial decision-making | ProvKOS: Warrant |

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613671)

[Figure 6](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) illustrates the expanded terms and properties of our ProvKOS conceptual model. Given that our conceptual model adopts and expands upon PROV, we maintain the usage of a majority of properties in PROV. New properties are developed to support the new classes in ProvKOS.

The basic properties defined by PROV between Agents and Entities and Agents and Activities are used in this model without any additions or modifications. Between Entities and Activities, ProvKOS adopts two relations from PROV *Generation* and *Invalidation*. In the PROV, *Generation* is defined as a creation of a new Entity by an Activity. *Invalidation* is to destruct, cease or expire of an existing Entity by an Activity. The properties *prov:wasGeneratedBy* and *prov:wasInvalidatedBy* defined in PROV are used to represent *Generation* and *Invalidation*.

As we added sub-classes of Entity to represent changes in KOSs, we introduce a new property to describe a relation between ProvKOS:ClassNumber and *prov:activity*. The “wasAuthorizedBy” property is distinctively defined from *Generation*. Changes to a concept in KOS do not necessarily cause a creation of a new class number all the time because a concept can move from one class number to the other existing class number. Also, a class number can be unassigned by a change activity. Thus, we also introduce the “wasDeprecatedBy” property as an inverse of “wasAuthorizedBy,” which means a temporal invalidation of a class number. Also, sub-classes of Entity, such as ClassNumber and Label, represent a numeric notation and a corresponding human-readable literal string, respectively, and the “hasLabel” property is added to describe a relation between the two.

The class of “Warrant” also leads to the creation of new properties. “wasWarrantedBy” is a property between Activities and Warrants, revealing the editorial evidence the revision activities were based on. The sub-class of Warrant, *Document*, which represents an editorial documents or records in the editorial decision-making process, commonly discusses or mentions justifications for a proposed change in it. Thus, the “cite” property is used to relate *Document* to other sub-classes of Warrant such as *Literature*, *skos:Concept* and *skos:ConceptScheme*. [Table 7](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) provides the full definitions for all properties in the ProvKOS model.

Table 7

Properties in ProvKOS

| Property | Definition | Domain | Range |
| --- | --- | --- | --- |
| prov: wasRevisionOf | | prov:Entity | prov:Entity |
| prov: wasAttributedTo | Attribution is the ascribing of an entity to an agent | prov:Entity | prov:Agent |
| prov: wasAssociatedWith | An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent to achieve some goals in the context of this activity | prov:Activity | prov:Agent |
| prov: startedAtTime | Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not exist before its start. Any usage, generation, or invalidation involving an activity follows the activity’s start. A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that generated the trigger | prov:Activity | XMLSchema |
| prov: endedAtTime | End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists after its end. Any usage, generation, or invalidation involving an activity precedes the activity’s end. An end may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the trigger | prov:Activity | XMLSchema |
| prov: wasGeneratedBy | Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation | prov:Entity | prov:Activity |
| prov: wasInvalidatedBy | Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The entity is no longer available for use (or further invalidation) after invalidation Any generation or usage of an entity precedes its invalidation | prov:Entity | prov:Activity |
| *ProvKOS: wasAuthorizedBy* | An “unassigned” number is being used to represent a concept | ProvKOS ClassNumber | prov:Activity |
| *ProvKOS: wasDeprecatedBy* | The existing number is deprecated becoming “unassigned” | ProvKOS ClassNumber prov:Activity | prov: Activity |
| *ProvKOS: wasWarrantedBy* | Activity was performed based on editorial evidence | prov:Activity | ProvKOS: Warrant |
| *ProvKOS: cite* | Sub-classes of Warrant cite other sub-classes of Warrant | ProvKOS:Warrant | ProvKOS:Warrant |
| *ProvKOS: hasLabel* | ClassNumber has the associated human readable label. One might distinguish a preferred label and an alternative label by using skosxl:prefLabel and skosxl:altLabel for tracking changes to all types of labels | ProvKOS: ClassNumber | skosxl:Label |
| skosxl:literalForm | | skosxl:Label | XMLSchema |
| skos:inScheme | | skos:concept | skos:conceptScheme |

**Source(s):** Table by authors

[View Large](https://www-emerald-com.sire.ub.edu/view-large/90613678)

In this section, we implement the ProvKOS conceptual model with an example use case. The example case is from the recent changes made to WebDewey of DDC 23rd edition.

The EPC exhibit serves as a proposal document for editorial discussions and decision-making procedures of the class number and labels of the DDC. According to the EPC document on the case of “gender dysphoria,” the previous classes associated with gender dysphoria are “616.8527 depressive disorder” and “616.8583 sexual disorders and gender-identity disorders.” These classes are problematic because gender identity is not a disorder, much less a mental disorder as the hierarchy suggests. Therefore, the DDC editorial team decided to make changes on these class numbers and labels.

[Figure 7](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/) illustrates the implementation of the ProvKOS model on documenting the change activities of this case.

Figure 7

Implementing the ProvKOS model to the gender dysphoria example in DDC

*Entities: “ProvKOS:classNumber” and “skos-xl:Label*.*”* The class number of 616.85277 is newly generated by the instance of activity 349,291, and the existing labels of two class numbers – 616.8527 and 616.8583 – are invalidated by the replacement activity.

*Activities: “ProvKOS:Replacement” and “prov:Activity*.*”* The activity instance 349,291 resulted in generation of a new class number and is expressed by the PROV relation, *Generation*. On the other hand, the instance 349,292 is defined as one of the typical activities for KOS-specific changes from the proposed model – *Replacement*.

*Warrant: “ProvKOS:Document*,*” “skos:Concept” and “skos:ConceptScheme*.*”* In the EPC exhibit 144-S61-1, relevant KOSs were discussed to justify the proposal for creating a new class number and updating labels for relevant classes. Although more articles were cited as references in the actual EPC document, we demonstrate how to reference the concept schemes from Homosaurus and the ICD-11 classification.

In this section, we discuss the distinctive features of our ProvKOS conceptual model and what they entail for various types of KOSs.

Our ProvKOS conceptual model captures the hierarchical changes of KOSs. Specifically, the activities identified as “Truncation” and “Expansion” are pivotal in managing the hierarchical relationships in many KOSs. *Truncation* represents the process of generalizing a concept, effectively moving it up within the broader hierarchy. This is often necessary when the scope of a concept needs to be widened, reflecting broader or more generalized topics. Conversely, *Expansion* is employed when the specificity of a concept increases, extending it deeper into a more narrowly defined part of the hierarchy.

The distinction between “Concept” and “Label” in the ProvKOS is particularly pertinent when examining the various approaches to represent classifications between systems like the DDC and Library of Congress Classification (LCC). According to Ford’s study ([Ford, 2013](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) on the LCC as linked data, generation and linkage of classification numbers and schedules are primarily focused on accurately reflecting the conceptual structure, with less emphasis on how these changes impact labels. This highlights a potential need in KOS management by using ProvKOS to explicitly track terminological changes alongside these hierarchical structural changes. That said, exploring the integration of ProvKOS with KOSs like LCC and DDC further could potentially provide valuable insights to other KOSs with hierarchical structures (e.g. taxonomies and thesauri) and terminological changes.

As discussed in the introduction of ProvKOS core structures, the ProvKOS conceptual model is designed to accommodate various types of KOSs. In scenarios where a KOS lacks a structured hierarchy, the model’s application can be adjusted. For example, the use of a generic *Activity* class instead of *Truncation* or *Expansion* sub-classes allows for the representation of a KOS change that are not hierarchical. This flexibility is crucial for adapting the model to various types of KOSs beyond traditional classification systems, such as unstructured vocabulary systems or term lists.

Along with the use of a generic *Activity* class, the *Replacement* activity can be also particularly useful in non-hierarchical systems. This activity does not inherently imply a hierarchical shift but is more concerned with updating the terminology within the KOS to reflect new vocabulary usage. Moreover, the model utilizes the *skosxl:Label* class flexibly, allowing for instances to take either an Internationalized Resource Identifier (IRI) or a literal form without the need to use the *ProvKOS:ClassNumber* for numeric notations. One can make the representation even simpler by using a generic *Entity* class and not using the sub-classes proposed in this model. These can support KOSs such as subject heading lists, taxonomies and thesauri when there is no distinction between concept and label.

For example, ProvKOS entities and properties can address the types of changes identified by International Organization for Standardization (ISO) 25964-1, section 13.6.4 ([International Organization for Standardization, 2011](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) with use of additional entities from skosxl. In thesauri, a concept can be represented as a *prov:Entity* and a preferred term and/or non-preferred term as a *skosxl:prefLabel/skosxl:altLabel*, respectively. As discussed in the data dictionary of ProvKOS, PROV properties *prov:wasGeneratedBy* and *prov:wasInvalidatedBy* describe activities of adding and deleting any entities – a concept, a preferred term and a non-preferred term in the case of thesauri, addressing ISO 25964-1, section 13.6.4 a, b, d and f. Other change activities to terms – such as amending a preferred term or a non-preferred term (ISO 25964-1, section 13.6.4, c), making a preferred term a non-preferred term of another preferred term (ISO 25964-1, section 13.6.4, e), reversing the preference between a preferred and a non-preferred term (ISO 25964-1, section 13.6.4, g) can be described by the sub-class *ProvKOS:Replacement* or a generic *prov:Activity* class with *skosxl:Label*, *skosxl:prefLabel* and *skosxl:altLabel*. *ProvKOS:Expansion, ProvKOS: Truncation* *and* *ProvKOS:Relocation* (or generic class *prov:Activity*) can capture changes to concepts – such as merging two concepts into one (ISO 25964-1, section 13.6.4, i), splitting a concept into two or more, which can sometimes involve selecting an existing non-preferred term to be a preferred term (ISO 25964-1, section 13.6.4, j), altering the hierarchical structure (ISO 25964-1, section 13.6.4, k) and moving a branch of the hierarchy from one place to another (ISO 25964-1, section 13.6.4, l). Additionally, ProvKOS may support ISO 25964-1, section 13.6.4. m, adding or removing associate relationships by utilizing *skosxl:labelRelation* across terms represented as *skosxl:Label, skosxl:prefLabel, skosxl:altLabel*. ProvKOS, however, does not support changes made to annotation texts that are normally captured in a scope note, history note or editorial note, because the purpose of ProvKOS is to provide structured data of those notes that are attributed to the changes.

Overall, as demonstrated by types of changes in thesauri (ISO 259641-1, section 13.6.4), proper usages of skosxl classes *skosxl:Label, skosxl:prefLabel, skosxl:altLabel* and *skosxl:labelRelation* to extend the current ProvKOS would allow a wide range of changes to thesauri and other vocabularies used for retrieving information. ProvKOS’s flexibility ensures the applicability of this conceptual model to all types of KOSs and the customizability of the model to the different information needs by key stakeholders.

The role of Warrant in the ProvKOS model underscores the importance of grounding editorial decisions with verifiable sources. The concepts and terms referenced in a KOS must be valid and sound to substantiate a reliable warrant, which is useful for designing metadata records ([Nylund, 2020](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)). Therefore, warrant is crucial for attributing the sources of information to help determine the reliability of changes within KOSs.

As Sikos ([Sikos *et al*., 2021](https://www-emerald-com.sire.ub.edu/jd/article/81/1/147/1242148/)) notes, to assess trustworthiness of networked knowledge statements from diverse sources, it’s essential to capture the provenance of the data. This is analogous to evaluating changes in KOSs, where decisions can depend heavily on the sources of information. For example, a change based on a widely recognized and validated external source may carry more weight than lesser-known or less formal sources. Example of such highly recognized source includes a major update from a well-established classification system or a recent view-changing publication by well-known scholars.

The ProvKOS model’s incorporation of the “Warrant” class allows for such assessments by documenting the attribution of sources that led the changes. This is particularly helpful in domains that undergo frequent changes. In this regard, ProvKOS can support the linkage of frequent updates in these external sources, thus informing the most updated information or the state-of-the-art insights on a particular concept.

However, there are still challenges with the knowledge extraction of these outside resources. KOSs that implement the ProvKOS model circumvent the knowledge extraction problem by making the annotations as a queryable class. On the other hand, the linked external sources are often still in unstructured textual documents rather than ready-to-use structured data. This hinders the overall searchability of a concept and warrant information. The successful extraction of the full pipeline of warrant information, from the original KOS to the outside resources, thus warrants further investigation to ensure the sustainability of a KOS.

Regarding ontology design with existing semantic web technology, our model suggests the use of a new entity, *Warrant*, instead of embedding the identified source information such as references and related KOSs in the encoding mechanisms such as resource description framework (RDF) or Web Ontology Language' (OWL) statements. Many KOSs, especially in the field of Library and Information Science (LIS), are created, edited and maintained outside of the linked data environment. Some of these were later made compliant with Semantic Web technology. Therefore, the usual editorial workflow and tools in LIS may not be able to integrate RDFs or OWL statements (e.g. RDFs’s annotation as sources of changes). For the KOSs that are compliant with the Semantic Web technology stacks (e.g. web published ontologies with Git repositories to control changes and updates), further investigations on how such provenance data of KOSs can be recorded, queried and analyzed are needed. The expanded discussions will include creating and sharing of provenance data usage policies, provenance data practices guidelines, query templates and use cases examples.

In this study, we develop a conceptual model designed to enhance the tracking of provenance within KOS. We present in this paper our five-step process in developing the conceptual model and the proposed conceptual model with a taxonomy of activities, data dictionaries of key components and expanded terms.

Our first research question asks, “How can the provenance of a KOS be modeled to better represent the changes within a KOS over time?” We develop the conceptual model with both bottom-up and top-down approaches, involving actual examples from existing KOSs and extending frameworks from existing provenance models. Through this process, we identify major activities of changes across KOSs: relocation, expansion, truncation and replacement. By modeling these activities, the ProvKOS model effectively captures nuanced changes of KOS such as modifications in class numbers and labels, hierarchical relocations and the authorization or deprecation of entities.

Our second research question asks, “How can the provenance documentation of a KOS enable the linkage or connection to another KOS?” We observe from the content analysis and stakeholder involvement that there is a need to document the evidence warranted changes within a KOS. These are usually the various types of external resources referenced or cited during KOS editorial decision-making process. The ProvKOS model introduces a “Warrant” class to connect these external resources to the change activities, with types of resources as a document, a piece of literature, a concept or other concept schemes. Through linking these resources, the Warrant class creates a more comprehensive network of KOSs than the current practices in Networked Knowledge Organization Systems Dublin Core Application Profile (NKOS AP) .

This study provides both conceptual and practical implications. Our conceptual contribution is the model itself. We acknowledge that this conceptual model may require further use case implementation with other KOSs to be comprehensive for all KOS types. In our future work, we plan to collect a variety of existing and future use cases of all KOS types. We also hope to initiate conversations and collaboration with scholars and practitioners in the domain of KOS provenance, such as the International Federation of Library Associations and Institutions (IFLA) working group on KOS-D . Through these collaborations, we aim to verify and refine our model to better meet the diverse needs of communities that engage with various KOSs.

The practical implication we foresee for our work is how the structured provenance data for KOS can help improve machine readability, querying and analysis. Especially within the linked data environment, this can help establish networked KOSs, which will then inform better linked data or knowledge graph designs. Furthermore, the developed model provides the basis to assess the impact of structured provenance data on information retrieval quality. In future work, we will conduct comparative information retrieval experiments with the systematic application of ProvKOS to existing KOSs to further evaluate the utility of ProvKOS.

In conclusion, our model introduces a comprehensive framework capable of representing the dynamic changes of KOSs, and it facilitates their interconnectivity through KOS-specific provenance data. Concurrently, the model highlights the ongoing need for iterative refinement and active collaboration to unlock the full potential of provenance data in enhancing the structure and utility of KOSs.

Inkyung Choi and Yi-Yun Cheng contributed equally to this work.

1.

FAIR principle: [https://www-nature-com.sire.ub.edu/articles/sdata201618](https://www-nature-com.sire.ub.edu/articles/sdata201618)

2.

WebDewey: [https://dewey.org/webdewey](https://dewey.org/webdewey)

3.

PROV: [http://www.w3.org/ns/prov](http://www.w3.org/ns/prov)

4.

NKOS DC-AP:[https://nkos.dublincore.org/nkos-ap.html](https://nkos.dublincore.org/nkos-ap.html)

5.

KOS-D:[https://www.ifla.org/projects/ko-system-change-and-data-structure-kos-d/](https://www.ifla.org/projects/ko-system-change-and-data-structure-kos-d/)

Adler

,

M.

,

Tennis

,

J.

,

Milojević

,

S.

,

van Hooland

,

S.

,

Rogers

,

C.

and

West

,

J.D.

(

2013

), “”,

Proceedings of the American Society for Information Science and Technology

, Vol. 

50

No. 

1

, pp. 

1

\-

3

, doi:

[https://doi-org.sire.ub.edu/10.1002/meet.14505001018](https://doi-org.sire.ub.edu/10.1002/meet.14505001018)

.

Barité

,

M.

(

2018

), “”,

Knowledge Organization: KO

, Vol. 

45

No. 

6

, pp. 

517

\-

536

, doi:

[https://doi-org.sire.ub.edu/10.5771/0943-7444-2018-6-517](https://doi-org.sire.ub.edu/10.5771/0943-7444-2018-6-517)

.

Beghtol

,

C.

(

1986

), “”,

Library Resources and Technical Services

, Vol. 

30

No. 

2

, pp. 

109

\-

125

.

Bettivia

,

R.

,

Cheng

,

Y.-Y.

and

Gryk

,

M.

(

2023

), “”,

International Conference on Information

, pp. 

74

\-

82

, doi:

[https://doi-org.sire.ub.edu/10.1007/978-3-031-28032-0\_6](https://doi-org.sire.ub.edu/10.1007/978-3-031-28032-0_6)

.

Cheng

,

Y.-Y.

(

2023

), “”,

Journal of the Association for Information Science and Technology

, doi:

[https://doi-org.sire.ub.edu/10.1002/asi.24848](https://doi-org.sire.ub.edu/10.1002/asi.24848)

.

Choi

,

I.

(

2018

), “”,

Doctoral dissertation, University of Wisconsin-Milwaukee, available at:

[https://www-proquest-com.sire.ub.edu/openview/28ba15047b6d80ccf299d51468d662ca/1?casa\_token=mID7pveHAScAAAAA:PJobftPr67r7s15W2fSSzlLdDzD15900jcbhlec9DuZnKo9bz3P-S2BXNUkfDwuiuxEjG-ewBXA&cbl=18750&pq-origsite=gscholar&parentSessionId=0S73k2UzU%2BT9IV%2Bc8OetAxa6inoDBrvQWOXheFG8yns%3D](https://www-proquest-com.sire.ub.edu/openview/28ba15047b6d80ccf299d51468d662ca/1?casa_token=mID7pveHAScAAAAA:PJobftPr67r7s15W2fSSzlLdDzD15900jcbhlec9DuZnKo9bz3P-S2BXNUkfDwuiuxEjG-ewBXA&cbl=18750&pq-origsite=gscholar&parentSessionId=0S73k2UzU%2BT9IV%2Bc8OetAxa6inoDBrvQWOXh) (

accessed

 25 February 2024).

Coladangelo

,

L.P.

(

2021

), “”,

Knowledge Organization

, Vol. 

48

No. 

3

, pp. 

195

\-

206

, doi:

[https://doi-org.sire.ub.edu/10.5771/0943-7444-2021-3-195](https://doi-org.sire.ub.edu/10.5771/0943-7444-2021-3-195)

.

Cuevas-Vincenttin

,

V.

,

Ludascher

,

B.

,

Missier

,

P.

,

Belhajjame

,

K.

,

Chirigati

,

F.

,

Wei

,

Y.

and

Dey

,

S.

(

2016

), “”,

available at:

[https://purl.dataone.org/provone-v1-dev](https://purl.dataone.org/provone-v1-dev)

Ford

,

K.

(

2013

), “”,

JLIS

, No. 

1

, doi:

[https://doi-org.sire.ub.edu/10.4403/jlis.it-5465](https://doi-org.sire.ub.edu/10.4403/jlis.it-5465)

.

Fox

,

M.J.

(

2016

), “”,

Knowledge Organization

, Vol. 

43

No. 

8

, pp. 

581

\-

593

, doi:

[https://doi-org.sire.ub.edu/10.5771/0943-7444-2016-8-581](https://doi-org.sire.ub.edu/10.5771/0943-7444-2016-8-581)

.

Gangemi

,

A.

and

Presutti

,

V.

(

2009

), “Ontology design patterns \[Journal Abbreviation: Handbook on ontologies\]”, in

Handbook on Ontologies

, pp. 

221

\-

243

, doi:

[https://doi-org.sire.ub.edu/10.1007/978-3-540-92673-3\_10](https://doi-org.sire.ub.edu/10.1007/978-3-540-92673-3_10)

.

Gaudet

,

P.

and

Dessimoz

,

C.

(

2017

), “Gene ontology: Pitfalls, biases, and remedies”, in

The Gene Ontology Handbook

, pp. 

189

\-

205

.

Groth

,

P.

and

Moreau

,

L.

(

2013

), “”,

available at:

[https://www.w3.org/TR/prov-overview/](https://www.w3.org/TR/prov-overview/)

Harley

,

A.

(

2015

),

Personas Make Users Memorable for Product Team Members

,

Nielsen Norman Group

,

available at:

[https://www.nngroup.com/articles/persona/](https://www.nngroup.com/articles/persona/)

International Organization for Standardization

(

2011

),

Information and Documentation — Thesauri and Interoperability with Other Vocabularies

,

Iso

,

available at:

[https://www.iso.org/standard/53657.html](https://www.iso.org/standard/53657.html) (

accessed

 22 July 2024).

Jett

,

J.

,

Sacchi

,

S.

,

Lee

,

J.H.

and

Clarke

,

R.I.

(

2016

), “”,

Journal of the Association for Information Science and Technology

, Vol. 

67

No. 

3

, pp. 

505

\-

517

, doi:

[https://doi-org.sire.ub.edu/10.1002/asi.23409](https://doi-org.sire.ub.edu/10.1002/asi.23409)

.

Ledl

,

A.

and

Voss

,

J.

(

2016

), “”,

TKE 2016 - 12th International Conference on Terminology and Knowledge Engineering

,

Conference Proceedings

,

available at:

[http://sf.cbs.dk/gtw/conferences\_terminology\_and\_knowledge\_engineering/tke\_2016\_copenhagen](http://sf.cbs.dk/gtw/conferences_terminology_and_knowledge_engineering/tke_2016_copenhagen).

Li

,

C.

and

Sugimoto

,

S.

(

2018

), “”,

Journal of Documentation

, Vol. 

74

No. 

1

, pp. 

36

\-

61

, doi:

[https://doi-org.sire.ub.edu/10.1108/JD-03-2017-0042](https://doi-org.sire.ub.edu/10.1108/JD-03-2017-0042)

.

Lodi

,

G.

,

Maccioni

,

A.

,

Scannapieco

,

M.

,

Scanu

,

M.

and

Tosco

,

L.

(

2014

), “”,

SemStats@

.

McDonald

,

C.

(

2020

), “”, pp.

284

\-

292

, doi:

[https://doi-org.sire.ub.edu/10.5771/9783956507762-284](https://doi-org.sire.ub.edu/10.5771/9783956507762-284)

.

Montoya

,

R.D.

(

2017

), “”,

Doctoral dissertation, UCLA

.

Nielsen

,

L.

(

2019

),

Personas - User Focused Design

,

Springer

,

London

, doi:

[https://doi-org.sire.ub.edu/10.1007/978-1-4471-7427-1](https://doi-org.sire.ub.edu/10.1007/978-1-4471-7427-1)

.

Nylund

,

I.B.

(

2020

), “”, pp.

328

\-

337

, doi:

[https://doi-org.sire.ub.edu/10.5771/9783956507762-328](https://doi-org.sire.ub.edu/10.5771/9783956507762-328)

.

Rusquart

,

J.

(

2023

), “”,

Communication, technologies et développement

, Vol. 

14

No. 

14

, doi:

[https://doi-org.sire.ub.edu/10.4000/ctd.9779](https://doi-org.sire.ub.edu/10.4000/ctd.9779)

.

Sikos

,

L.F.

,

Seneviratne

,

O.W.

and

McGuinness

,

D.L.

(

Eds

) (

2021

),

Provenance in Data Science: from Data Models to Context-Aware Knowledge Graphs

,

Springer International Publishing

, doi:

[https://doi-org.sire.ub.edu/10.1007/978-3-030-67681-0](https://doi-org.sire.ub.edu/10.1007/978-3-030-67681-0)

.

Skos primer

(

n.d.

),

available at:

[http://www.w3.org/TR/skos-primer/](http://www.w3.org/TR/skos-primer/)

Souza

,

R.

,

Azevedo

,

L.

,

Lourenço

,

V.

,

Soares

,

E.

,

Thiago

,

R.

,

Brandão

,

R.

,

Civitarese

,

D.

,

Brazil

,

E.

,

Moreno

,

M.

,

Valduriez

,

P.

,

Mattoso

,

M.

,

Cerqueira

,

R.

and

Netto

,

M.A.

(

2019

), “”,

2019 IEEE/ACM Workflows in Support of Large-Scale Science (WORKS)

, pp.

1

\-

10

, doi:

[https://doi-org.sire.ub.edu/10.1109/WORKS49585.2019.00006](https://doi-org.sire.ub.edu/10.1109/WORKS49585.2019.00006)

.

Tennis

,

J.T.

(

2007

), “”,

Bulletin of the American Society for Information Science and Technology

, Vol. 

32

No. 

5

, pp.

13

\-

16

, doi:

[https://doi-org.sire.ub.edu/10.1002/bult.2006.1720320506](https://doi-org.sire.ub.edu/10.1002/bult.2006.1720320506)

.

Tennis

,

J.T.

(

2012

), “”,

Journal of the American Society for Information Science and Technology

, Vol. 

63

No. 

7

, pp. 

1350

\-

1359

, doi:

[https://doi-org.sire.ub.edu/10.1002/asi.22686](https://doi-org.sire.ub.edu/10.1002/asi.22686)

.

Zhang

,

B.

,

Carriero

,

V.A.

,

Schreiberhuber

,

K.

,

Tsaneva

,

S.

,

González

,

L.S.

,

Kim

,

J.

and

de Berardinis

,

J.

(

2024

), “”,

available at:

[http://arxiv.org/abs/2403.05921](http://arxiv.org/abs/2403.05921) (

accessed

 18 March 2024).

## PDF text extraction

A conceptual model for tracking
the provenance of activities in
knowledge organization systems
Inkyung Choi
OCLC Online Computer Library Center Inc, Dublin, Ohio, USA, and
Yi-Yun Cheng
Department of Library and Information Science,
School of Communication and Information,
Rutgers, The State University of New Jersey, Piscataway, New Jersey, USA
Abstract
Purpose – The purpose of this study is to develop a conceptual model, ProvKOS, for tracking the provenance
of change activities in a knowledge organization system (KOS). By extending current provenance practices,
this model represents dynamic changes in a KOS more effectively.
Design/methodology/approach – We take a five-step approach to develop the conceptual model, including
content analysis of KOS editorial data, environmental scan of existing provenance models, development of
persona-specific provenance questions and a participatory design with stakeholders to ensure the model’s utility.
Findings – We introduce (1) a taxonomy of editorial activities for a KOS; (2) a conceptual model ProvKOS,
which extends existing models PROV and Simple Knowledge Organization Systems (SKOS). We also provide
detailed data dictionaries for the entities, activities and warrants classes proposed in the model. A use case on
“gender dysphoria” in Dewey Decimal Classifications (DDCs) is provided to illustrate the implementation of
ProvKOS. This shows ProvKOS’s ability to capture KOS changes effectively and to link external resources
relating to the changes.
Research limitations/implications – Further validation may be needed to implement the ProvKOS model
across various types of KOSs.
Practical implications – ProvKOS can help improve machine readability, querying and analysis of a KOS.
Especially within the linked data environment, the enhanced provenance documentation through ProvKOS
can enable a network of KOSs, which will then inform better linked data or knowledge graph designs.
Social implications – By facilitating better tracking of changes within a KOS and across KOSs, ProvKOS
can enhance the accessibility and usability of knowledge bases across different cultural and social contexts,
thus better supporting inclusive information practices.
Originality/value – The proposed model is novel in two ways: one, its ability to represent dynamic change
activities in a KOS, which has not been discussed anywhere else; two, it supports the interconnectivity across
KOSs by providing a “warrant” class to substantiate the context of changes.
Keywords Provenance, Knowledge organization systems, Conceptual model, Dewey decimal classification
Paper type Research paper
Introduction
Tracking the change to the elements of a knowledge organization system (KOS) over time is
a long-standing research topic in the field of Information Science. For instance, scholars
analyzed the change of a subject term in different versions of a bibliographic classification
(Tennis, 2012) or examined the historical reconstructions of a biodiversity taxonomy to
interpret the choice of changes (Montoya, 2017). However, these studies demonstrated the
challenges in finding, accessing and analyzing changes to the elements of a KOS for the
following reasons: (1) the activities that point to a change (e.g. cataloging) is a non-linear,
dynamic process, and this process usually reflects the worldview of that particular point in
Journal of
Documentation
147
Inkyung Choi and Yi-Yun Cheng contributed equally to this work.
The current issue and full text archive of this journal is available on Emerald Insight at:
https://www.emerald.com/insight/0022-0418.htm
Received 3 May 2024
Revised 30 July 2024
Accepted 7 August 2024
Journal of Documentation
Vol. 81 No. 1, 2025
pp. 147-167
© Emerald Publishing Limited
0022-0418
DOI 10.1108/JD-05-2024-0101
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

time (Adler et al., 2013); (2) nuances in KOS that involve many different types of KOS
elements – such as structural changes to the hierarchy or terminological changes to the
labels (Choi, 2018; Tennis, 2007); (3) evidence for the changes in KOS is not transparent –
knowledge on editorial notes or contexts of the changes are very limited (Gaudet and
Dessimoz, 2017).
In provenance research, time and changes are also significant areas of inquiries.
Provenance is defined as how something has come to be (Bettivia et al., 2022a, 2023), and by
documenting the source and origin of a concept, item or object, provenance is often viewed as
an important indicator to enable trust and reproducibility. In this study, the “somethings” are
the KOSs. Extant models in provenance research such as PREMIS, PROV, ProvONE or
Provlets (Bettivia et al., 2023) emphasizes on capturing the Agent, Activity, Entity or
Environment of a digitally or computationally-driven application (Cuevas-Vincenttin et al.,
2016; Groth and Moreau, 2013), but these models are not sufficient in capturing the nuances
of changes within a KOS. Based on the PROV model, Li and Sugimoto (2018) developed a
model to capture provenance descriptions in metadata vocabularies, but the model’s focus on
metadata vocabularies suggests that it is not applicable to other forms of KOSs. In particular,
provenance descriptions of a classification system with a deep hierarchical relationships and
notation practices could not be captured. Other efforts such as the Simple Knowledge
Organization System (SKOS) ontology provide provenance descriptions (e.g. change notes or
editorial notes), but free-text descriptions in notes are not enough to fully support capabilities
to query and analyze the complex changes within a KOS.
In this research, we aim at enhancing the change activities to elements of a KOS to support
long-term provenance practices for a KOS management. We demonstrate the
implementation of our model on the case of bibliographic classification for representing
the structural changes, but our research questions are positioned to address broader issues
with provenance of all types of KOSs. Our two research questions are.
RQ1. How can the provenance of a KOS be modeled to better represent the changes
within a KOS over time?
RQ2. How can the provenance documentation of a KOS enable the linkage or connection
to another KOS?
To address these questions, this study proposes a conceptual model, ProvKOS, that stems
from the PROV and the SKOS models to incorporate the different aspects of KOS change
found in real-world examples. Then, we take these real-world examples from the DDCs. As
the provenance queries are simplified to reflect the functional aspects of a KOS provenance,
this paper demonstrates how the conceptual model can be implemented by KOS editorial
managers, information professionals or researchers.
This conceptual model addresses provenance queries of a KOS such as follows:
(1) What caused the change?
(2) What is the evidence supporting the change of one subject term to another?
(3) How has a concept within a KOS been changed over time?
There are two contributions of this paper. First, our work models the provenance of KOS by
tracking both subtle and substantial changes with a special focus on hierarchical structures
and notation practices, ensuring these alterations are captured in a standardized, machine-
readable format over time. Second, beyond a particular KOS, our model facilitates the
interconnection of disparate KOSs by documenting the rationale behind KOS modifications.
This supports the creation of detailed networks between KOSs, which then informs future
editorial decision-making and cross-KOS comparisons.
JD
81,1
148
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Related work
Documenting changes in knowledge organization systems (KOSs)
KOSs such as taxonomies, metadata schemas, classifications, thesauri and ontologies undergo
frequent changes such as word meanings and usage patterns changes. The importance of
documenting these changes to manage how words and meanings evolve over time has been a
long-standing scholarly discussion in the field of information science. For example, Tennis
(2012) found shifts in the term “Eugenics” in the subject vocabularies of the DDC from a
biology-related concept to a social construct over several decades. Other works by Fox (2016),
Rusquart (2023) and McDonald (2020) explore the social and ethical implications of these shifts.
However, these changes are often invisible with little or no public documentation.
To resolve the undocumented changes in KOS, researchers have highlighted several
important aspects to be documented. Tennis (2007) discussed the possibility of explicitly
documenting nuanced changes by KOS editors such as concept replacement, concept
refinement or concept reconfiguration. Choi (2018) asserted that both structural and
terminological changes in KOS play crucial roles to shape coherency in a KOS. Choi
concluded that changes to a concept’s class number (structural change) and labels
(terminological change) in bibliographic classifications should be considered. Coladangelo
(2021) highlighted the needs to capture multiple viewpoints during vocabulary creation in
the context of cultural heritage knowledge. This enables not only transparency in vocabulary
changes but also acknowledges the multidimensionality of a KOS.
In addition to individual researchers’ endeavors, there are also organizational efforts to
track KOS changes such as the World Wide Web Consortium’ (W3C’s) SKOS ontology. The
primary focus of SKOS is to make a KOS compatible with the semantic web environment,
and some of the classes and properties in SKOS can only support minimal documentation of
KOS changes (Ledl and Voß, 2016; “SKOS Primer”, n.d.). Documentation properties such as
“skos:changeNote,” “skos:historyNote” or “skos:editorialNote” can be leveraged. However,
these properties are in unstructured, paragraphed formats which pose difficulties in parsing
for further querying and analysis. A more comprehensive model is still much needed to
document KOS changes on the class-level to enable provenance queries.
Current models and practices in provenance research
Time and changes are the core concerns in provenance research. As defined by Bettivia et al.
(2022a, 2023), “provenance” is how something has come to be. This something can be
conceptual, physical or digital; in this study, the somethings are the KOSs.
Extant models and standards in provenance research focus primarily on applications in the
eScience or preservation domains, with an emphasis to manage digital and computational
artifacts. The so-called “data provenance” is the ability to capture and track changes in these
computational artifacts, deriving from the need to enhance reproducibility with data artifacts
that are produced at a speed too fast to be captured. The PROV model is a family of W3C
standards for data provenance, including many different serializations such as PROV-DM,
PROV-O, PROV-N and PROV-XML (Groth and Moreau, 2013). Provenance in the PROV model
is described with three core components: Entity, Activity and Agent. An Entity is often
described as a concept, idea or object that can be digital, physical or conceptual; the Activity in
PROV is the event, process or changes associated with the Entity and the Agent is the person,
software or responsible party of the occurring Activity. Extending the PROV model, ProvONE
takes into account the temporal aspects of provenance and models two types of provenance:
retrospective provenance and prospective provenance (Bettivia et al., 2022b; Cuevas-Vincenttin
et al., 2016). Retrospective provenance is associated with an activity that already happened in
the past (e.g. change logs), while prospective provenance is forward-looking and associated
with what will happen in the future (e.g. workflows and recipes). The distinction between the
Journal of
Documentation
149
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

past and the future in provenance is an useful perspective. This can help support the
reproducibility of changes on a same entity over time (Cuevas-Vincenttin et al., 2016).
Limitations in existing practices and this study
While issues surrounding data provenance gave birth to many provenance models in the
eSciences community, the ability to use or extend these provenance models is a concern that
transcends disciplines. For instance, Li and Sugimoto (2018) extended the use of the PROV
model to enhance provenance descriptions in metadata vocabularies. The Italian National
Institute of Statistics (ISTAT) and Italian Agency for Digitalization (AgID) showcased the
application of the PROV framework in publishing classifications in the Linked Open Data
environment (Lodi et al., 2014). However, the extent to which these current provenance
models can capture the nuances of changes in a KOS and be applied to all forms of KOSs has
yet to be investigated. Additionally, current provenance models and practices may contain
details such as where, when or by whom a resource was created, but contextual information
in these models such as why something has changed is limited.
As such, we propose the ProvKOS conceptual model in this study to address these gaps
and answer the “whys” (or what “warrants” changes in a KOS) when documenting and
tracking the provenance of KOSs.
Note that discussions on the theoretical framework of the “warrant” concept are beyond
the scope of this study. In this work, we consider the utility of the warrants as “to illuminate
where and how the concepts and terms in the designed systems are grounded (Nylund, 2020,
p. 331)”. Nylund analyzed the concept of warrant (Barit �e, 2018; Beghtol, 1986) within eighteen
articles in library and information science journals. We paid a special attention to
information sources’ warrant and adopted it in our constructed model.
Developing the conceptual model
In this section, we highlight the development process of our conceptual model on
representing KOS changes. We aim to make the development process as transparent as
possible to document our own provenance in creating the conceptual model.
Rationale and motivating example
In exploring provenance data model addressing KOSs, we are specifically interested in
whether the models provide contextual metadata surrounding data origins. We want to be
able to leverage these kinds of contextual information to enhance the utility of knowledge
organization systems. Based on data availability, we pay specific interests to the DDC, and
we leverage cases of change in the DDC as motivating examples to help construct the
conceptual model and later as an example implementation use case of the model. We envision
constructing a conceptual model which could meticulously track the provenance of each data
element of a KOS and documenting its evolution over time.
The DDC serves as a foundational knowledge organization system for organizing
knowledge across a multitude of domains and disciplines. Its interconnected nature
facilitates seamless navigation and discovery of related topics, making it an invaluable
resource for information professionals worldwide. Given its wide adoption in public libraries
in the USA and other countries, it is important to ensure the reliability and transparency of
DDC’s change notes. However, although current editorial activities to the DDC are publicly
shared, the insights to why certain class or label changed are often unobtainable due to the
complexity of editorial process and documents. There is also a lack of discoverability of
knowledge on the evidence of changes, regarding which external resources was discussed,
documents used or other references cited. This has posed challenges to researchers and
JD
81,1
150
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

information professionals in effectively sharing, researching or analyzing DDC and in
making informed decisions about a DDC concept to their specific needs.
In response to these challenges, our project focuses on enhancing the findability,
accessibility, interoperability and reusability (FAIR [1]) of change activities of a KOS, inspired
by examples from the DDC. By making provenance information such as time, location and
warrants of a KOS concept visible and shareable, our model can explicitly state the insights
needed to navigate and utilize a KOS effectively. This approach not only facilitates informed
decision-making but also promotes collaboration and knowledge exchange within the broader
information community. Furthermore, to bridge the external resources used referenced in a
KOS change, our conceptual provenance model aims to connect various KOSs to the editorial
decisions. By establishing connections between changes in one KOS to other KOSs, the reasons
behind the changes to a KOS will be made more transparent.
Data sources
This study utilizes a variety of resources to help construct the conceptual model. These
resources include DDC’s Editorial Policy Committee (EPC) exhibits, OCLC’s editorial
systems, WebDewey [2] and the 23rd edition of the DDC’s machine-readable cataloging
(MARC) classification data. We hope to capture all facets of a KOS that could lead a change in
its provenance information in the DDC framework.
Development process
The development process of the conceptual model consists of five steps: (1) content analysis
of the data; (2) environmental scanning of current provenance models; (3) developing general
provenance questions; (4) participatory design involving stakeholders and (5) developing
persona-specific provenance queries.
We employ a dual approach with both bottom-up and top-down strategies to develop the
conceptual model. These two strategies are detailed in steps (1) and (2), which are developed
in an iterative and simultaneous manner.
(1) Content analysis of the data
For the bottom-up approach, data such as EPC exhibits, WebDewey and MARC
classification data are analyzed to identify patterns and elements pertinent to provenance.
This step involved a thorough content analysis by use of the editing process workflow, with a
specific focus on changes to DDC class numbers and concept labels.
(2) Environmental scanning of existing provenance models
For the top-down approach, we conduct an environmental scan to survey existing
provenance models such as PROV and ProvOne, as mentioned in the related works section.
Additionally, common ontologies for KOS, such as SKOS and SKOS-XL, were also reviewed
to ensure the usability of these existing models on the DDC examples. We look specifically for
rooms for expansion on these models, namely, if there are any elements or entities missing in
describing the change activities of a KOS.
(3) Developing general provenance questions
Steps 1 and 2 inform the development of this step. We develop a set of general provenance
questions to capture the necessary data components of provenance. We also examine the
different components of a provenance model to devise possible provenance questions a user
might ask. These questions are categorized into two main groups: those focusing on tracking
changes of a KOS and those gearing toward analytics of a KOS change. We list examples of
these general purpose questions in Table 1.
Journal of
Documentation
151
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

(4) Participatory design to include stakeholders
In addition, we take a participatory design approach to include key stakeholders of a KOS in
the conceptual model development process. For the example of DDC, we have been in close
communication with editors and the linked data team members of the DDC for their iterative
feedback of the model. We want to ensure the model can reflect not only the general purpose
queries, but more importantly the key stakeholders’ provenance queries.
(5) Persona-specific provenance queries
Drawing from our ongoing conversations with key stakeholders, we have identified the
personas to represent the user groups of the conceptual model. The concept of persona has
long been used by the field of Human-Computer Interaction (HCI) and adopted by software
design and development (Harley, 2015; Nielsen, 2019). Personas are fictitious, specific and
concrete representations of the target users. It’s utility in gaining insights about users’ goals
and scenarios on designing a system has also been widely adopted by ontology design,
ontology development or ontology engineering process (Gangemi and Presutti, 2009; Souza
et al., 2019; Zhang et al., 2024). The goals and scenarios captured with the personas of
targeted users are useful in shaping and defining model requirements. By identifying
persona-specific queries, the resulting model can address key stakeholders’ questions.
In our model, personas represent distinct user groups with varying needs and priorities
concerning provenance information within knowledge organization systems. These
personas include (1) editorial managers who oversee the editorial process of a KOS, (2)
information professionals who use KOSs for information retrieval and analysis and (3)
researchers who engage with KOSs for research activities and analysis. Specific information
needs of each group and their questions are listed in Table 2.
A taxonomy of editorial activities for a KOS
Based on our five-step development process, we find that existing provenance models fell
short in describing the nuanced activities for changes in a KOS. We identify key editorial
activities of a KOS and construct these into a taxonomy of activities first and later to be
partially adopted into the conceptual model. Through the five-step process with content
analysis, environmental scan and participatory design, we construct this taxonomy with
several iterations. Our goal is to make the taxonomy of activities as simple as possible for
For tracking changes
What warrants the change of term?
What warrants the relocation of class?
When was the change made?
Who made the change?
What are the activities of the change?
How many times did the term undergo changes?
For analytics
What are the deprecated terms for the past 2 years?
Where was this item A classified under in the year of 1990?
What is the trajectory of subject B from 1910 to 2020?
When did the term C first appeared?
How many new terms were made in the new edition?
How many terms are revised in the new edition?
What are the primary reasons of revision of terms?
Which revision activity was used the most?
What are the most used external resource for revision?
Source(s): Table by authors
Table 1.
General provenance
questions
JD
81,1
152
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

practical use and as flexible as possible for generalizability to all KOSs. We identify two main
activities of a KOS: initiation and revision. For revision, we identified five sub-activities,
namely relocation, expansion, truncation, deprecation and replacement. See Figure 1 for a
User role Main activities Information needs
Provenance queries of
interest
Editorial
manager
Oversees the editorial process
of KOS. Ensures the accuracy
and integrity of KOS
To obtain information on
changes to terms and classes
within the KOS
To explore the reasons
behind revisions and
relocations of classes
To track the responsible
entities for the change
To understand the
frequency of term revisions
What warrants the
change of term?
When was the change
made?
Who made the change?
Why was the term
changed?
How many times did
the term undergo
changes?
Information
professional
Utilizes KOS for information
retrieval and analysis
To identify outdated terms
To trace the trajectory and
evolution of subjects over
time
To assess the frequency and
nature of revisions
To explore reasons for
changes
To explore the external
resources used for changes
What are outdated
terms?
Where was item A
classified under in
1990?
What is the trajectory
of subject B from 1910
to 2020?
How many new terms
were made in DDC 23
edition?
What are the primary
reasons for revision of
terms?
Researcher Engages with KOS to access
information for research
To assess the reliability and
relevance of terms for
changes
To study the trajectory and
evolution of subjects over
time
To analyze reasons for
changes
To assess the external
resources used for changes
What is the evidence
used for the change?
When did the term first
appear?
How many terms are
revised in DDC 23?
Which revision activity
was used the most?
Source(s): Table by authors’
Table 2.
Persona-specific
provenance questions
Figure 1.
A taxonomy of activity
Journal of
Documentation
153
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

visual representation of the taxonomy, and see Table 3 for the full definition and example of
each activity.
The presented taxonomy demonstrates how the analysis of editorial workflow of a DDC
example case informs the constructions of the conceptual model. As a result, the taxonomy of
editorial activities was generalized to represent the changes to elements within a KOS, from
simply removing a concept like the deprecation activity to more complex actions such as
expanding or truncating the concepts within a class hierarchy.
Previously, Tennis (2007) suggested types of changes on concepts in a concept scheme,
suggesting the extension of SKOS ontology in order to capture more nuanced editorial
changes. Those included refining, lumping and re-configuring, which are covered by
“expansion” and “relocation” in this taxonomy. Those editorial changes identified by Tennis
et al. address extension or progression of the concept scheme as exemplified by the
versioning of DCMI Metadata Thesaurus from 2002 to 2004 that was used to index Dublin
Core Metadata Initiative (DCMI) proceedings each year (i.e. the 2002 version of DC Terms
was a list of terms and from 2003 the term list was expanded into thesaurus). The taxonomy
in this paper addressed editorial changes of classification systems with a more complex
relationship structure and a long history of changes and thus included “truncation,”
“deprecation” and “initiation” which reflect various nuanced editorial changes. We will
further discuss the applicability of the conceptual model to other types of KOSs in the
Discussion section.
The proposed conceptual model
Conceptual models are useful graphical representations to depict how various concepts relate
and function (Cheng, 2023; Jett et al., 2016). In this section, we describe our proposed
conceptual model, including data dictionary of the classes and properties.
Activity Definition Examples for the DDC
Initiation A topic newly appeared; new class entity and label
entity are generated
616.85277, gender dysphoria first
appeared in Edition 23, July 2023
Revision Class and Label entities are revised in terms of the topic representations
Sub-activities of revision include: relocation, expansion, truncation, deprecation and
replacement
Relocation A concept is relocated from one class number to
another class number but no hierarchical
movements involved
Autism spectrum disorder relocated
from 616.8982 to 616.95882
Expansion A class number is further specified thus the class
number progressed to the narrower hierarchy
Other pervasive development disorders
expanded from 616.8588 to 616.85883
DDC editorial team used the term,
“Continuation”
Truncation A class number is generalized thus the class
number moves up to the broader hierarchy
Schizophrenia truncated from 616.8982
to 616.898
DDC editorial team used the term,
“Discontinuation”
Deprecation A concept or representations of a concept is
suspended from the system
Autism class number 616.85883 is
deprecated after relocation
Replacement A label of a concept is modified Autism is replaced with autism
spectrum disorder
Source(s): Table by authors
Table 3.
A taxonomy of activity
JD
81,1
154
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

ProvKOS: a conceptual model
We leverage and expand PROV and SKOS ontologies to create the ProvKOS conceptual
model. In this section, we give an overview of the ProvKOS conceptual model’s core
structures and a data dictionary of the classes and properties. Similar to the taxonomy of
activities, we aim to construct a conceptual model that is simple and easy to use so that our
key stakeholders (researchers, information professionals and editorial managers) can adopt
the model suiting their information needs.
Figure 2 displays the core, high-level structures of ProvKOS. We inherit core components
Entity, Agent and Activity from the PROV model [3]. We observe a need to document and
connect external resources as evidence of changes in a KOS, such as mentions of other
classifications, citations of recent papers, etc. Thus, we introduce a fourth component to the
model “Warrant” to reflect contexts and reasons for changes. We follow the namespace
conventions from PROV: the prefix “prov:” refers to classes and properties of PROV
ontology, and the prefix of “ProvKOS” refers to our own creation – indicating unique classes
and properties we designed to represent KOS provenance that have not been covered by
other relevant data models or ontologies.
Data dictionary
In this section, we explain in detail each of the core component in ProvKOS, including the
definitions of the classes, sub-classes and properties. Some of the expanded terms (with
prefixes “ProvKOS:”) are our own creation to reflect the KOS changes.
(1) Entity
In KOSs such as taxonomies and ontologies, concepts (or vocabularies) are represented with
string literals or annotated labels. In KOSs such as classifications, concepts are represented
in both numeric notations and string literals. Currently, SKOS ontologies use properties for
labeling a concept and notations. However, having notations and labels as properties instead
of classes in an ontology can limit the capability to query these changes. To encompass
Figure 2.
The core structures of
ProvKOS
Journal of
Documentation
155
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

different ways of representing a concept, we identify two unique sub-classes of entity for any
KOS: Class number and Label. Figure 3 illustrates the prov:Entity and the two new sub-
classes.
Class number refers to the concepts represented with numeric notations (e.g. 616.95882),
whereas labels are the literal forms of the term (e.g. autism spectrum disorder.). The proposed
sub-classes of Entity in our model are distinctive as they allow a class number and a label of a
concept in KOSs to be the unit of change. We leverage existing vocabulary from SKOS-XL
(skos extensions) for labels (skosxl:Label). ClassNumber, on the other hand, is associated
with specific editorial activities that are distinct from a label in a numeric notation. ProvKOS
maintains the flexibility that if one is working with a KOS that does not contain any notations
(e.g. a KOS that is not a bibliographic classification system), the Label class can be sufficient
to describe the changes solely without using the ClassNumber sub-class. Table 4 shows the
definitions for Entity, Label and Class number.
(2) Activity
The taxonomy of activities we develop specified the key editorial activities of any KOS,
including two main activities, namely Initiation and Revision, and five sub-activities of
Revision: Relocation, Expansion, Truncation, Deprecation and Replacement. For the
conceptual model, we incorporate properties from the PROV model which asserts Initiation
and Revision activities by using “prov:wasGeneratedBy” and “prov:wasRevisionOf”
properties. Further, a PROV entity can be invalidated (or deprecated) by an activity with
Class Definition Superclass
prov:Entity An entity is a physical, digital, conceptual, or other kind of thing with some
fixed aspects; entities may be real or imaginary. (from PROV-O)
N/A
skosxl:Label The class skosxl:Label is a special class of lexical entities. An instance of the
class skosxl:Label is a resource and may be named with a URI. An instance of
the class skosxl:Label has a single literal form. (from SKOS-XL)
prov:Entity
ClassNumber A class number is a numeric or alphanumeric notation to represent a concept,
frequently used in KOSs that has hierarchical structure. A concept is defined
as a unit of thought, specific ideas or meanings established within a KOS. Class
number is assignable to classify information resources. An instance of
ClassNumber may be named with a URI
prov:Entity
Source(s): Table by authors
Figure 3.
Entity and sub-classes
ClassNumber
and Label
Table 4.
Definition of entity and
sub-classes label and
class number
JD
81,1
156
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

the “prov:wasInvalidatedBy” property. Therefore, in the conceptual model, we incorporate
only the four sub-activities from our taxonomy of activities. These four sub-activities
(Expansion, Truncation, Replacement and Relocation) more accurately reflect how our
conceptual model extends the existing PROV model. Figure 4 illustrates the model with
these extended activities.
Our model for the activities also encompasses other types of KOSs. The activities can be
adopted in various ways to represent different levels of specificity in the nuanced KOS
changes. For example, if a KOS does not contain numeric notations and most of the changes
are to replace old terms with new terms, then “Replacement” can sufficiently capture the
activity of this particular KOS. If a KOS is more coarse-grained and does not have various
nuanced changes, one can uses the “prov:Activity” class to sufficiently represent any kinds
of change. Table 5 provides the full definitions for the four activities included in the
conceptual model.
(3) Warrant
The “Warrant” class proposed in this conceptual model is to represent external sources for
decision-making on KOS changes. When KOS changes are suggested during the editorial
process and discussions, we noticed that the editorial documents frequently include
references to external resources. These external resources include citing editorial documents,
referencing literature about a topic in discussion or connecting to other relevant concepts and
concept schemes. Figure 5 shows the four types of external resources for the Warrant class
we create to enhance the linkage between a KOS activity and external resources.
For example, in the DDC editorial documents, if a topic in discussion is related to medical
subjects, International Classification of Diseases (ICD) and Diagnostic and Statistical Manual
of Mental Disorders (DSM) are frequently referenced, we use “Concept” and
Class Definition Superclass
prov:
Activity
An activity is something that occurs over a period of time and acts upon or
with entities; it may include consuming, processing, transforming,
modifying, relocating, using, or generating entities. (from PROV-O)
N/A
Relocation A relocation is a lateral movement of a concept from one position to another
(e.g. from a class number to another class number)
prov:Activity
Expansion An expansion is to expand the concept with more specificity, thus moving
the class number moves down to the narrower hierarchy
prov:Activity
Truncation A truncation is to trim the specificity of a concept, so the concept is more
generalized and moves up to the broader hierarchy. (i.e. DDC editorial team
used the term, “Discontinuation”)
prov:Activity
Replacement A replacement is having a label replaced with another label prov:Activity
Source(s): Table by authors
Figure 4.
Activity and four
ProvKOS sub-classes
Table 5.
Definition of activity
and sub-classes:
Relocation, Expansion,
Truncation and
Replacement
Journal of
Documentation
157
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

“ConceptScheme”, derived from the SKOS model to represent these. The connection to
external KOSs can then be further leveraged for a representation of the networked KOSs at
the concept level. For example, one can aggregate linked concepts from an external KOSs to a
certain DDC class and consider them as evidence of semantic similarity. Table 6 provides the
definitions for these external resources for Warrant.
ProvKOS: expanded terms and properties
Figure 6 illustrates the expanded terms and properties of our ProvKOS conceptual model.
Given that our conceptual model adopts and expands upon PROV, we maintain the usage of a
majority of properties in PROV. New properties are developed to support the new classes in
ProvKOS.
The basic properties defined by PROV between Agents and Entities and Agents and
Activities are used in this model without any additions or modifications. Between Entities
and Activities, ProvKOS adopts two relations from PROV Generation and Invalidation. In
the PROV, Generation is defined as a creation of a new Entity by an Activity. Invalidation is
to destruct, cease or expire of an existing Entity by an Activity. The properties
prov:wasGeneratedBy and prov:wasInvalidatedBy defined in PROV are used to represent
Generation and Invalidation.
As we added sub-classes of Entity to represent changes in KOSs, we introduce a new
property to describe a relation between ProvKOS:ClassNumber and prov:activity. The
“wasAuthorizedBy” property is distinctively defined from Generation. Changes to a
concept in KOS do not necessarily cause a creation of a new class number all the time
because a concept can move from one class number to the other existing class number.
Also, a class number can be unassigned by a change activity. Thus, we also introduce
Class Definition Superclass
Warrant Any identifiable sources supporting the editorial activities of the
KOS
N/A
Document Documents are things that record the editorial process which
include proposals of changes, discussions of proposals, and
suggested changes and its impacts
ProvKOS:
Warrant
skos:conceptScheme A KOS providing an warrant for editorial decision-making (from
SKOS)
ProvKOS:
Warrant
skos:concept A KOS concept providing an warrant for editorial decision-making
(from SKOS)
ProvKOS:
Warrant
Literature Citable publications (e.g. scholarly articles, web links, news report)
providing an warrant for editorial decision-making
ProvKOS:
Warrant
Source(s): Table by authors
Figure 5.
ProvKOS Warrant and
sub-classes Document,
Literature, Concept
and ConceptScheme
Table 6.
Definition of Warrant
and sub-classes
JD
81,1
158
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

the “wasDeprecatedBy” property as an inverse of “wasAuthorizedBy,” which means
a temporal invalidation of a class number. Also, sub-classes of Entity, such as
ClassNumber and Label, represent a numeric notation and a corresponding human-
readable literal string, respectively, and the “hasLabel” property is added to describe a
relation between the two.
The class of “Warrant” also leads to the creation of new properties. “wasWarrantedBy” is
a property between Activities and Warrants, revealing the editorial evidence the revision
activities were based on. The sub-class of Warrant, Document, which represents an editorial
documents or records in the editorial decision-making process, commonly discusses or
mentions justifications for a proposed change in it. Thus, the “cite” property is used to relate
Document to other sub-classes of Warrant such as Literature, skos:Concept and
skos:ConceptScheme. Table 7 provides the full definitions for all properties in the
ProvKOS model.
Use case: gender dysphoria in DDC
In this section, we implement the ProvKOS conceptual model with an example use case. The
example case is from the recent changes made to WebDewey of DDC 23rd edition.
The EPC exhibit serves as a proposal document for editorial discussions and decision-
making procedures of the class number and labels of the DDC. According to the EPC
document on the case of “gender dysphoria,” the previous classes associated with gender
dysphoria are “616.8527 depressive disorder” and “616.8583 sexual disorders and gender-
identity disorders.” These classes are problematic because gender identity is not a disorder,
much less a mental disorder as the hierarchy suggests. Therefore, the DDC editorial team
decided to make changes on these class numbers and labels.
Figure 7 illustrates the implementation of the ProvKOS model on documenting the change
activities of this case.
Figure 6.
Classes and properties
– expanded terms
Journal of
Documentation
159
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Property Definition Domain Range
prov: wasRevisionOf prov:Entity prov:Entity
prov:
wasAttributedTo
Attribution is the ascribing of an
entity to an agent
prov:Entity prov:Agent
prov:
wasAssociatedWith
An activity association is an
assignment of responsibility to an
agent for an activity, indicating that
the agent had a role in the activity.
It further allows for a plan to be
specified, which is the plan
intended by the agent to achieve
some goals in the context of this
activity
prov:Activity prov:Agent
prov: startedAtTime Start is when an activity is deemed
to have been started by an entity,
known as trigger. The activity did
not exist before its start. Any usage,
generation, or invalidation
involving an activity follows the
activity’s start. A start may refer to
a trigger entity that set off the
activity, or to an activity, known as
starter, that generated the trigger
prov:Activity XMLSchema
#delete/dateTime
prov: endedAtTime End is when an activity is deemed
to have been ended by an entity,
known as trigger. The activity no
longer exists after its end. Any
usage, generation, or invalidation
involving an activity precedes the
activity’s end. An end may refer to a
trigger entity that terminated the
activity, or to an activity, known as
ender that generated the trigger
prov:Activity XMLSchema
#delete/dateTime
prov:
wasGeneratedBy
Generation is the completion of
production of a new entity by an
activity. This entity did not exist
before generation and becomes
available for usage after this
generation
prov:Entity prov:Activity
prov:
wasInvalidatedBy
Invalidation is the start of the
destruction, cessation, or expiry of
an existing entity by an activity.
The entity is no longer available for
use (or further invalidation) after
invalidation
Any generation or usage of an
entity precedes its invalidation
prov:Entity prov:Activity
ProvKOS:
wasAuthorizedBy
An “unassigned” number is being
used to represent a concept
ProvKOS
ClassNumber
prov:Activity
ProvKOS:
wasDeprecatedBy
The existing number is deprecated
becoming “unassigned”
ProvKOS
ClassNumber
prov:Activity
prov: Activity
ProvKOS:
wasWarrantedBy
Activity was performed based on
editorial evidence
prov:Activity ProvKOS: Warrant
(continued )
Table 7.
Properties in ProvKOS
JD
81,1
160
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Entities: “ProvKOS:classNumber” and “skos-xl:Label.” The class number of 616.85277 is
newly generated by the instance of activity 349,291, and the existing labels of two class
numbers – 616.8527 and 616.8583 – are invalidated by the replacement activity.
Activities: “ProvKOS:Replacement” and “prov:Activity.” The activity instance 349,291
resulted in generation of a new class number and is expressed by the PROV relation,
Generation. On the other hand, the instance 349,292 is defined as one of the typical activities
for KOS-specific changes from the proposed model – Replacement.
Warrant: “ProvKOS:Document,” “skos:Concept” and “skos:ConceptScheme.” In the EPC
exhibit 144-S61-1, relevant KOSs were discussed to justify the proposal for creating a new
class number and updating labels for relevant classes. Although more articles were cited as
references in the actual EPC document, we demonstrate how to reference the concept
schemes from Homosaurus and the ICD-11 classification.
Property Definition Domain Range
ProvKOS: cite Sub-classes of Warrant cite other
sub-classes of Warrant
ProvKOS:Warrant ProvKOS:Warrant
ProvKOS: hasLabel ClassNumber has the associated
human readable label. One might
distinguish a preferred label and an
alternative label by using
skosxl:prefLabel and
skosxl:altLabel for tracking
changes to all types of labels
ProvKOS:
ClassNumber
skosxl:Label
skosxl:literalForm skosxl:Label XMLSchema
#delete/string
skos:inScheme skos:concept skos:conceptScheme
Source(s): Table by authors
Table 7.
Figure 7.
Implementing the
ProvKOS model to the
gender dysphoria
example in DDC
Journal of
Documentation
161
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Discussion
In this section, we discuss the distinctive features of our ProvKOS conceptual model and
what they entail for various types of KOSs.
Documenting KOS hierarchical structural changes alongside terminological changes
Our ProvKOS conceptual model captures the hierarchical changes of KOSs. Specifically, the
activities identified as “Truncation” and “Expansion” are pivotal in managing the
hierarchical relationships in many KOSs. Truncation represents the process of
generalizing a concept, effectively moving it up within the broader hierarchy. This is
often necessary when the scope of a concept needs to be widened, reflecting broader or more
generalized topics. Conversely, Expansion is employed when the specificity of a concept
increases, extending it deeper into a more narrowly defined part of the hierarchy.
The distinction between “Concept” and “Label” in the ProvKOS is particularly pertinent
when examining the various approaches to represent classifications between systems like
the DDC and Library of Congress Classification (LCC). According to Ford’s study (Ford,
2013) on the LCC as linked data, generation and linkage of classification numbers and
schedules are primarily focused on accurately reflecting the conceptual structure, with less
emphasis on how these changes impact labels. This highlights a potential need in KOS
management by using ProvKOS to explicitly track terminological changes alongside these
hierarchical structural changes. That said, exploring the integration of ProvKOS with KOSs
like LCC and DDC further could potentially provide valuable insights to other KOSs with
hierarchical structures (e.g. taxonomies and thesauri) and terminological changes.
Flexible adaptation of ProvKOS to various types of KOSs
As discussed in the introduction of ProvKOS core structures, the ProvKOS conceptual model
is designed to accommodate various types of KOSs. In scenarios where a KOS lacks a
structured hierarchy, the model’s application can be adjusted. For example, the use of a
generic Activity class instead of Truncation or Expansion sub-classes allows for the
representation of a KOS change that are not hierarchical. This flexibility is crucial for
adapting the model to various types of KOSs beyond traditional classification systems, such
as unstructured vocabulary systems or term lists.
Along with the use of a generic Activity class, the Replacement activity can be also
particularly useful in non-hierarchical systems. This activity does not inherently imply a
hierarchical shift but is more concerned with updating the terminology within the KOS to
reflect new vocabulary usage. Moreover, the model utilizes the skosxl:Label class flexibly,
allowing for instances to take either an Internationalized Resource Identifier (IRI) or a literal
form without the need to use the ProvKOS:ClassNumber for numeric notations. One can
make the representation even simpler by using a generic Entity class and not using the sub-
classes proposed in this model. These can support KOSs such as subject heading lists,
taxonomies and thesauri when there is no distinction between concept and label.
For example, ProvKOS entities and properties can address the types of changes identified
by International Organization for Standardization (ISO) 25964-1, section 13.6.4 (International
Organization for Standardization, 2011) with use of additional entities from skosxl. In
thesauri, a concept can be represented as a prov:Entity and a preferred term and/or non-
preferred term as a skosxl:prefLabel/skosxl:altLabel, respectively. As discussed in the data
dictionary of ProvKOS, PROV properties prov:wasGeneratedBy and prov:wasInvalidatedBy
describe activities of adding and deleting any entities – a concept, a preferred term and a non-
preferred term in the case of thesauri, addressing ISO 25964-1, section 13.6.4 a, b, d and f. Other
change activities to terms – such as amending a preferred term or a non-preferred term (ISO
25964-1, section 13.6.4, c), making a preferred term a non-preferred term of another preferred
JD
81,1
162
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

term (ISO 25964-1, section 13.6.4, e), reversing the preference between a preferred and a non-
preferred term (ISO 25964-1, section 13.6.4, g) can be described by the sub-class
ProvKOS:Replacement or a generic prov:Activity class with skosxl:Label, skosxl:prefLabel
and skosxl:altLabel. ProvKOS:Expansion, ProvKOS: Truncation and ProvKOS:Relocation (or
generic class prov:Activity) can capture changes to concepts – such as merging two concepts
into one (ISO 25964-1, section 13.6.4, i), splitting a concept into two or more, which can
sometimes involve selecting an existing non-preferred term to be a preferred term (ISO
25964-1, section 13.6.4, j), altering the hierarchical structure (ISO 25964-1, section 13.6.4, k) and
moving a branch of the hierarchy from one place to another (ISO 25964-1, section 13.6.4, l).
Additionally, ProvKOS may support ISO 25964-1, section 13.6.4. m, adding or removing
associate relationships by utilizing skosxl:labelRelation across terms represented as
skosxl:Label, skosxl:prefLabel, skosxl:altLabel. ProvKOS, however, does not support changes
made to annotation texts that are normally captured in a scope note, history note or editorial
note, because the purpose of ProvKOS is to provide structured data of those notes that are
attributed to the changes.
Overall, as demonstrated by types of changes in thesauri (ISO 259641-1, section 13.6.4),
proper usages of skosxl classes skosxl:Label, skosxl:prefLabel, skosxl:altLabel and
skosxl:labelRelation to extend the current ProvKOS would allow a wide range of changes
to thesauri and other vocabularies used for retrieving information. ProvKOS’s flexibility
ensures the applicability of this conceptual model to all types of KOSs and the
customizability of the model to the different information needs by key stakeholders.
External sources as warrant in editorial decision-making
The role of Warrant in the ProvKOS model underscores the importance of grounding
editorial decisions with verifiable sources. The concepts and terms referenced in a KOS must
be valid and sound to substantiate a reliable warrant, which is useful for designing metadata
records (Nylund, 2020). Therefore, warrant is crucial for attributing the sources of
information to help determine the reliability of changes within KOSs.
As Sikos (Sikos et al., 2021) notes, to assess trustworthiness of networked knowledge
statements from diverse sources, it’s essential to capture the provenance of the data. This is
analogous to evaluating changes in KOSs, where decisions can depend heavily on the sources
of information. For example, a change based on a widely recognized and validated external
source may carry more weight than lesser-known or less formal sources. Example of such
highly recognized source includes a major update from a well-established classification
system or a recent view-changing publication by well-known scholars.
The ProvKOS model’s incorporation of the “Warrant” class allows for such assessments
by documenting the attribution of sources that led the changes. This is particularly helpful in
domains that undergo frequent changes. In this regard, ProvKOS can support the linkage of
frequent updates in these external sources, thus informing the most updated information or
the state-of-the-art insights on a particular concept.
However, there are still challenges with the knowledge extraction of these outside resources.
KOSs that implement the ProvKOS model circumvent the knowledge extraction problem by
making the annotations as a queryable class. On the other hand, the linked external sources are
often still in unstructured textual documents rather than ready-to-use structured data. This
hinders the overall searchability of a concept and warrant information. The successful
extraction of the full pipeline of warrant information, from the original KOS to the outside
resources, thus warrants further investigation to ensure the sustainability of a KOS.
Regarding ontology design with existing semantic web technology, our model suggests
the use of a new entity, Warrant, instead of embedding the identified source information such
as references and related KOSs in the encoding mechanisms such as resource description
Journal of
Documentation
163
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

framework (RDF) or Web Ontology Language’ (OWL) statements. Many KOSs, especially in
the field of Library and Information Science (LIS), are created, edited and maintained outside
of the linked data environment. Some of these were later made compliant with Semantic Web
technology. Therefore, the usual editorial workflow and tools in LIS may not be able to
integrate RDFs or OWL statements (e.g. RDFs’s annotation as sources of changes). For the
KOSs that are compliant with the Semantic Web technology stacks (e.g. web published
ontologies with Git repositories to control changes and updates), further investigations on
how such provenance data of KOSs can be recorded, queried and analyzed are needed. The
expanded discussions will include creating and sharing of provenance data usage policies,
provenance data practices guidelines, query templates and use cases examples.
Conclusion
In this study, we develop a conceptual model designed to enhance the tracking of provenance
within KOS. We present in this paper our five-step process in developing the conceptual
model and the proposed conceptual model with a taxonomy of activities, data dictionaries of
key components and expanded terms.
Our first research question asks, “How can the provenance of a KOS be modeled to better
represent the changes within a KOS over time?” We develop the conceptual model with both
bottom-up and top-down approaches, involving actual examples from existing KOSs and
extending frameworks from existing provenance models. Through this process, we identify
major activities of changes across KOSs: relocation, expansion, truncation and replacement.
By modeling these activities, the ProvKOS model effectively captures nuanced changes of
KOS such as modifications in class numbers and labels, hierarchical relocations and the
authorization or deprecation of entities.
Our second research question asks, “How can the provenance documentation of a KOS
enable the linkage or connection to another KOS?” We observe from the content analysis and
stakeholder involvement that there is a need to document the evidence warranted changes
within a KOS. These are usually the various types of external resources referenced or cited
during KOS editorial decision-making process. The ProvKOS model introduces a “Warrant”
class to connect these external resources to the change activities, with types of resources as a
document, a piece of literature, a concept or other concept schemes. Through linking these
resources, the Warrant class creates a more comprehensive network of KOSs than the current
practices in Networked Knowledge Organization Systems Dublin Core Application Profile
(NKOS AP) [4].
This study provides both conceptual and practical implications. Our conceptual
contribution is the model itself. We acknowledge that this conceptual model may require
further use case implementation with other KOSs to be comprehensive for all KOS types. In
our future work, we plan to collect a variety of existing and future use cases of all KOS types.
We also hope to initiate conversations and collaboration with scholars and practitioners in
the domain of KOS provenance, such as the International Federation of Library Associations
and Institutions (IFLA) working group on KOS-D [5]. Through these collaborations, we aim
to verify and refine our model to better meet the diverse needs of communities that engage
with various KOSs.
The practical implication we foresee for our work is how the structured provenance data for
KOS can help improve machine readability, querying and analysis. Especially within the
linked data environment, this can help establish networked KOSs, which will then inform
better linked data or knowledge graph designs. Furthermore, the developed model provides the
basis to assess the impact of structured provenance data on information retrieval quality. In
future work, we will conduct comparative information retrieval experiments with the
systematic application of ProvKOS to existing KOSs to further evaluate the utility of ProvKOS.
JD
81,1
164
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

In conclusion, our model introduces a comprehensive framework capable of representing
the dynamic changes of KOSs, and it facilitates their interconnectivity through KOS-specific
provenance data. Concurrently, the model highlights the ongoing need for iterative
refinement and active collaboration to unlock the full potential of provenance data in
enhancing the structure and utility of KOSs.
Notes
1. FAIR principle: https://www.nature.com/articles/sdata201618
2. WebDewey: https://dewey.org/webdewey
3. PROV: http://www.w3.org/ns/prov
4. NKOS DC-AP:https://nkos.dublincore.org/nkos-ap.html
5. KOS-D:https://www.ifla.org/projects/ko-system-change-and-data-structure-kos-d/
References
Adler, M., Tennis, J., Milojevi �c, S., van Hooland, S., Rogers, C. and West, J.D. (2013), “The temporal
dimension in the study of knowledge bases: approaches to understanding knowledge creation
and representation over time”, Proceedings of the American Society for Information Science and
Technology, Vol. 50 No. 1, pp. 1-3, doi: 10.1002/meet.14505001018.
Barit �e, M. (2018), “Literary warrant”, Knowledge Organization: KO, Vol. 45 No. 6, pp. 517-536, doi: 10.
5771/0943-7444-2018-6-517.
Beghtol, C. (1986), “Semantic validity: concepts of warrant in bibliographic classification systems”,
Library Resources and Technical Services, Vol. 30 No. 2, pp. 109-125.
Bettivia, R., Cheng, Y.-Y. and Gryk, M.R. (2022a), Documenting the Future: Navigating Provenance
Metadata Standards, Springer, Cham.
Bettivia, R., Cheng, Y.-Y. and Gryk, M.R. (2022b), “Provone”, in Documenting the Future: Navigating
Provenance Metadata Standards, Springer, pp. 41-56.
Bettivia, R., Cheng, Y.-Y. and Gryk, M. (2023), “What does provenance lack: how retrospective and
prospective met the subjunctive”, International Conference on Information, pp. 74-82, doi: 10.
1007/978-3-031-28032-0_6.
Cheng, Y.-Y. (2023), “Under whose wings? A conceptual model for incorporating historical sovereignty
information in biodiversity data”, Journal of the Association for Information Science and
Technology, doi: 10.1002/asi.24848.
Choi, I. (2018), “Toward a model of intercultural warrant: a case of the korean decimal classification’s
cross-cultural adaptation of the Dewey decimal classification - ProQuest”, Doctoral
dissertation, University of Wisconsin-Milwaukee, available at: https://www.proquest.com/
openview/28ba15047b6d80ccf299d51468d662ca/1?casa_token5mID7pveHAScAAAAA:
PJobftPr67r7s15W2fSSzlLdDzD15900jcbhlec9DuZnKo9bz3P-S2BXNUkfDwuiuxEjG-
ewBXA&cbl518750&pq-origsite5gscholar&parentSessionId50S73k2UzU%2BT9IV%2Bc8O
etAxa6inoDBrvQWOXheFG8yns%3D (accessed 25 February 2024).
Coladangelo, L.P. (2021), “Organizing controversy: toward cultural hospitality in controlled
vocabularies through semantic annotation”, Knowledge Organization, Vol. 48 No. 3,
pp. 195-206, doi: 10.5771/0943-7444-2021-3-195.
Cuevas-Vincenttin, V., Ludascher, B., Missier, P., Belhajjame, K., Chirigati, F., Wei, Y. and Dey, S.
(2016), “Provone: a prov extension data model for scientific workflow provenance”, available at:
https://purl.dataone.org/provone-v1-dev
Ford, K. (2013), “LC classification as linked data”, JLIS, No. 1, doi: 10.4403/jlis.it-5465.
Journal of
Documentation
165
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Fox, M.J. (2016), “Subjects in doubt: the ontogeny of intersex in the dewey decimal classification”,
Knowledge Organization, Vol. 43 No. 8, pp. 581-593, doi: 10.5771/0943-7444-2016-8-581.
Gangemi, A. and Presutti, V. (2009), “Ontology design patterns [Journal Abbreviation: Handbook on
ontologies]”, in Handbook on Ontologies, pp. 221-243, doi: 10.1007/978-3-540-92673-3_10.
Gaudet, P. and Dessimoz, C. (2017), “Gene ontology: Pitfalls, biases, and remedies”, in The Gene
Ontology Handbook, pp. 189-205.
Groth, P. and Moreau, L. (2013), “Prov-overview: an overview of the prov family of documents”,
available at: https://www.w3.org/TR/prov-overview/
Harley, A. (2015), Personas Make Users Memorable for Product Team Members, Nielsen Norman
Group, available at: https://www.nngroup.com/articles/persona/
International Organization for Standardization (2011), Information and Documentation — Thesauri
and Interoperability with Other Vocabularies, Iso, available at: https://www.iso.org/standard/
53657.html (accessed 22 July 2024).
Jett, J., Sacchi, S., Lee, J.H. and Clarke, R.I. (2016), “A conceptual model for video games and
interactive media”, Journal of the Association for Information Science and Technology, Vol. 67
No. 3, pp. 505-517, doi: 10.1002/asi.23409.
Ledl, A. and Voss, J. (2016), “Describing Knowledge Organization Systems in BARTOC and JSKOS”,
TKE 2016 - 12th International Conference on Terminology and Knowledge Engineering,
Conference Proceedings, available at: http://sf.cbs.dk/gtw/conferences_terminology_and_
knowledge_engineering/tke_2016_copenhagen.
Li, C. and Sugimoto, S. (2018), “Provenance description of metadata application profiles for long-term
maintenance of metadata schemas [Publisher: Emerald Publishing Limited]”, Journal of
Documentation, Vol. 74 No. 1, pp. 36-61, doi: 10.1108/JD-03-2017-0042.
Lodi, G., Maccioni, A., Scannapieco, M., Scanu, M. and Tosco, L. (2014), “Publishing official
classifications in linked open data”, SemStats@.
McDonald, C. (2020), “Call us by our name(s): shifting representations of the transgender community
in classificatory practice”, pp. 284-292, doi: 10.5771/9783956507762-284.
Montoya, R.D. (2017), “Contingent consensus: documentary control in biodiversity classifications”,
Doctoral dissertation, UCLA.
Nielsen, L. (2019), Personas - User Focused Design, Springer, London, doi: 10.1007/978-1-4471-7427-1.
Nylund, I.B. (2020), “Using the concept of warrant in designing metadata for enterprise search”,
pp. 328-337, doi: 10.5771/9783956507762-328.
Rusquart, J. (2023), “The ontogeny of the subject as an approach to the ethical evaluation of
classification systems. mental health case study [Number: 14 Publisher: La Chaire Pratiques
�emergentes en technologies et communication pour le d �eveloppement]”, Communication,
technologies et d �eveloppement, Vol. 14 No. 14, doi: 10.4000/ctd.9779.
Sikos, L.F., Seneviratne, O.W. and McGuinness, D.L. (Eds) (2021), Provenance in Data Science: from
Data Models to Context-Aware Knowledge Graphs, Springer International Publishing, doi: 10.
1007/978-3-030-67681-0.
Skos primer (n.d.), available at: http://www.w3.org/TR/skos-primer/
Souza, R., Azevedo, L., Lourenço, V., Soares, E., Thiago, R., Brand ~ao, R., Civitarese, D., Brazil, E.,
Moreno, M., Valduriez, P., Mattoso, M., Cerqueira, R. and Netto, M.A. (2019), “Provenance data
in the machine learning lifecycle in computational science and engineering”, 2019 IEEE/ACM
Workflows in Support of Large-Scale Science (WORKS), pp. 1-10, doi: 10.1109/WORKS49585.
2019.00006.
Tennis, J.T. (2007), “Versioning concept schemes for persistent retrieval”, Bulletin of the American
Society for Information Science and Technology, Vol. 32 No. 5, pp. 13-16, doi: 10.1002/bult.2006.
1720320506.
JD
81,1
166
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025

Tennis, J.T. (2012), “The strange case of eugenics: a subject’s ontogeny in a long-lived classification
scheme and the question of collocative integrity”, Journal of the American Society for
Information Science and Technology, Vol. 63 No. 7, pp. 1350-1359, doi: 10.1002/asi.22686.
Zhang, B., Carriero, V.A., Schreiberhuber, K., Tsaneva, S., Gonz �alez, L.S., Kim, J. and de Berardinis, J.
(2024), “OntoChat: a framework for conversational ontology engineering using language
models”, available at: http://arxiv.org/abs/2403.05921 (accessed 18 March 2024).
Corresponding author
Inkyung Choi can be contacted at: choii@oclc.org
For instructions on how to order reprints of this article, please visit our website:
www.emeraldgrouppublishing.com/licensing/reprints.htm
Or contact us for further details: permissions@emeraldinsight.com
Journal of
Documentation
167
Downloaded from http://www.emerald.com/jd/article-pdf/81/1/147/9678749/jd-05-2024-0101.pdf by Universitat de Barcelona user on 28 November 2025
