---
title: "Frame-based terminology applied to military science: transforming a glossary into a knowledge resource - Lexicography"
source: "https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y"
author:
  - "[[SpringerLink]]"
published: 2019-11-20
created: 2025-05-15
description: "This paper describes a Frame-Based Terminology approach to the military terminology of the Spanish Armed Forces. The alphabetically organized (PD0-000) glo"
tags:
  - "op/suggestedBytutors"
---
## Frame-based terminology applied to military science: transforming a glossary into a knowledge resource

- Original Paper
- Published:
- Volume 6, pages 105–131, (2019)
- [Cite this article](https://link-springer-com.sire.ub.edu/article/10.1007/#citeas)

Access provided by Universitat de Barcelona CRAI Biblioteca

 [![](https://media-springernature-com.sire.ub.edu/w72/springer-static/cover-hires/journal/40607?as=webp) Lexicography](https://link-springer-com.sire.ub.edu/journal/40607)

## Abstract

This paper describes a Frame-Based Terminology approach to the military terminology of the Spanish Armed Forces. The alphabetically organized (PD0-000) glossary of military terms of the Spanish Armed Forces was transformed into MiliMarco \[MiliFrame\], a bilingual terminological knowledge base in which each concept appears within a hierarchy of conceptual categories and a semantic network. Frame-based resources enhance access to domain knowledge in a contextualized way, since embedding concepts in a knowledge structure activates associative information in semantic memory and promotes context availability. The design and population of MiliMarco involved the analysis and transformation of the content in the glossary entries as well as the extraction of new information. For this purpose, specialized knowledge structures were elaborated from the definitions in the glossary and from the lexicalization of semantic relations in the corpus. New concepts were added to fill the gaps in the glossary and additional data categories were included, such as images, collocations, and contexts. Previous work on military ontologies, usually in the form of controlled, structured vocabularies, is limited to a specific domain (e.g., military intelligence). MiliMarco has the advantage of providing an expanded view of the military domain in the form of conceptual networks combined with linguistic contexts that go far beyond simple hierarchies. Although still an ongoing project, the resulting knowledge base is currently a concept-oriented resource where users can browse through the conceptual hierarchy and semantic networks based on their cognitive and communicative needs.

### Similar content being viewed by others

### Maintaining the balance between knowledge and the lexicon in terminology: a methodology based on frame semantics

Article 21 February 2018

### LingFN: A Framenet for the Linguistic Domain

Chapter © 2023

### FrameNet-Based Automatic Suggestion of Translation Equivalents

Chapter © 2016

[Use our pre-submission checklist](https://beta-springernature-com.sire.ub.edu/pre-submission?journalId=40607)

Avoid common mistakes on your manuscript.

## 1 Introduction

This paper describes a Frame-Based Terminology (FBT) approach (Faber [2012](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR7 "Faber, Pamela (ed.). 2012. A cognitive linguistics view of terminology and specialized language. Berlin: De Gruyter."), [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR8 "Faber, Pamela. 2015. Frames as a framework for terminology. In Handbook of terminology, ed. H.J. Kockaert and F. Steurs, 14–33. Amsterdam: John Benjamins.")) to the military terminology of the Spanish Armed Forces. Promoting successful communication in multilingual scenarios evidently entails more than facilitating a standardized alphabetical list of terms. Since misinterpreted messages can have dramatic consequences in military settings, text senders and receivers should possess the same domain knowledge to facilitate mutual understanding. This objective is easier to achieve when terminological resources are context-oriented or frame-based. Knowledge of terminological units and their meanings also signifies being aware of how these units combine with others and in which scenarios these combinations may occur. Users must be able to understand the range of contexts activated within the specialized domain, and to have a grasp of the concepts and categories participating in them.

This paper explains how the PD0-000 glossary of military terms of the Spanish Armed Forces \[partially based on the *NATO Glossary of Terms and Definitions* (AAP-06)\] was transformed into MiliMarco \[MiliFrame\], a bilingual terminological knowledge base in which each concept appears within the context of a semantic network that highlights conceptual structure and semantic relations with other concepts.

The design and population of MiliMarco involved the analysis and transformation of the content in the glossary as well as the inclusion of new information. For instance, specialized knowledge structures were extracted from the definitions in the glossary and from the lexicalization of semantic relations in the corpus. New concepts were added to fill the gaps encountered in the glossary and new data categories were included, such as images, collocations, and contexts.

The rest of this paper is organized as follows. Section [2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec2) describes previous work in the military domain and provides a concise outline of Frame-Based Terminology. Section  [3](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec6) describes the PD0-000 military glossary and the method used to transform it into a knowledge base. Section  [4](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec11) presents the results and discusses some of the problems encountered. The conclusions are given in Sect. [5](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec12).

## 2 Theoretical and applied framework

### 2.1 Previous work in military terminology management

Militerm <sup><a href="https://link-springer-com.sire.ub.edu/article/10.1007/#Fn1"><span>Footnote </span>1</a></sup> is a multilingual military term base focusing on security and defense policy developed by the Estonian Language Institute. It contains 4038 concept entries and a total of 17,415 terms in Estonian, English, French, and German. Militerm data categories include definitions, related concepts, term types, and sources.

However, in Military Science, NATO resources are the major reference point for terminology management. NATO terminology is based on the *Concise Oxford English Dictionary* (Stevenson [2011](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR4 "Stevenson, A. (ed.). 2011. Concise Oxford english dictionary, 12th ed. Oxford: Oxford University Press.")) and *Le Petit Robert* (Rey [2019](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR13 "Rey, Alan (ed.). 2019. Le Petit Robert de la Langue Française. Paris: Le Robert.")). Specific NATO-agreed terminology is developed when the terminology contained in these dictionaries or developed by recognized international standards organizations is inadequate for NATO purposes.

According to the NATO Terminology Directive, the general principles underlying termhood and definitions are transparency, conciseness, stability, consistency, completeness, and univocity. Nevertheless, there is still much room for improvement. Language has long been neglected in military history despite the fact that conflicts are almost always between people who speak different language. As an example, Jones and Askew ([2014](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR11 "Jones, Ian, and Louise Askew. 2014. Meeting the language challenges of NATO operations: policy, practice and professionalization. London: Palgrave McMillan."): 58) highlight the lack of reference resources that linguists had to face during the operation of Bosnia Herzegovina: “many of the linguists I met in SFOR <sup><a href="https://link-springer-com.sire.ub.edu/article/10.1007/#Fn2"><span>Footnote </span>2</a></sup> had, therefore, brought their own dictionaries to their offices. Not unsurprisingly, many different dictionaries were being used, which did not help to promote standardization of terminology”.

One possible reason for language comprehension problems in military settings could be the lack of interoperability of NATO glossaries as well as their format, since terms can only be accessed alphabetically. For this reason, a new resource called NATOTerm has been created as the central repository for all non-classified NATO-Agreed terminology. NATOTerm is concept-oriented and structured in three levels. At each level, there are different data categories: (1) record level (security, domain, project, etc.); (2) language level (approval status, definition, source, comments, notes, examples, related concepts, graphics, etc.); (3) term level (type, source, acceptability, grammar, usage, approval status, etc.). NATOTerm users include military linguists, civilian interpreters, editors, translators, assistants, and local personnel. The functions of linguistic support include command-level relations with authorities and parties, operations at the tactical and other levels, human intelligence, psychological operations, public affairs, legal affairs, contracting, logistics, policing, civil-military cooperation, administration of local personnel and training of indigenous forces, medical services, etc. (NATO [2011](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR14 "NATO (North Atlantic Treaty Organization). 2011. Linguistic Support for Operations, ALING P-1. 
http://nso.nato.int/nso/zPublic/ap/alingp-1.pdf
.")).

Although the former NTMS (NATO Terminology Management System) termbase already included domain-related contextual information in certain entries in the form of a qualifier at the beginning of a definition, that was not sufficient. This is why, NATOTerm is gradually being provided with conceptual structure in the form of a set of domains, known as the NATOTerm taxonomy (Jones [2011](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR10 "Jones, Ian. 2011. The NATO terminology programme and NATOTerm. In Proceedings of the 33rd Translating and the Computer Conference, London. 
http://www.mt-archive.info/Aslib-2011-Jones.pdf
.")). These domains mostly refer to the range of subjects dealt with by the various NATO committees, agencies, and groups in the documents which they produce (i.e., political affairs, law and regulations, defense, etc.). However, the path to conceptual organization is difficult and progress seems to be extremely slow, since no efforts have been made to provide NATOTerm with a more strictly defined hierarchical organization of concepts. One obstacle is the difficulty in finding points of conceptual convergence, given the differences in the armed forces in countries around the world. In an effort to harmonize these differences, there have been initiatives, such as the construction of military ontologies.

### 2.2 Previous work in military ontologies

As is well known, an ontology is a conceptual representation that labels, defines, and structures the categories, properties, and relations between concepts in a given domain. In Military Science, a well-defined concept system for knowledge sharing is crucial, because military operations are no longer conducted by one nation. In this context, having a common understanding and making assumptions explicit becomes pivotal. Not surprisingly, in recent years, there have been various proposals to fill this gap.

More specifically, the Muninn Military Ontology <sup><a href="https://link-springer-com.sire.ub.edu/article/10.1007/#Fn3"><span>Footnote </span>3</a></sup> defines a set of classes and properties that encode information about the structure of the armed forces and military history. This ontology (last updated July 2015) is largely centered on the domains of military trade, appointment, and rank in different countries (USA, Russia, England, Australia, Sweden, etc.). The concept designations or terms included were extracted from military databases, Wikipedia, and books.

In a more specific context, Valente et al. ([2005](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR24 "Valente, Andre, Douglas Holmes, and Frank C. Alvidrez. 2005. Using a military information ontology to build semantic architecture models for airspace systems. IEEE Aerospace Conference Proceedings. 
https://doi-org.sire.ub.edu/10.1109/aero.2005.1559635
.")) propose a Military Information Ontology (MilInfo) that was developed as a foundation for semantic architecture models for airspace systems. It is primarily centered on military information, an extremely valuable commodity, which is the key to success in any military operation. This ontology, whose top-level concepts were taken from OpenCyc, allows users to make queries regarding aspects of military information, such as content, significance, composition, source, quality, analysis, and constraints. For example, it differentiates between A bstract I nformation \[document content\] and I nformation B earing O bject \[the document itself\]. Other projects in progress by the same authors are an ontology for Military Communications and another for Military Organizations.

Yoo et al. ([2014](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR25 "Yoo, Donghee, Sungchun No, and Minyoung Ra. 2014. A practical military ontology construction for the intelligent army tactical command information system. International Journal of Computers, Communications and Control 9 (1): 93–100.")) developed a military ontology for the Korean government as part of the Army Tactical Command Information System (ATCIS), which focuses on the domains of information (reporting battlefield situations), operation (decision-making and orders), and firepower (strike orders and priorities). They used the information in the ATCIS database to build a basic ontology, which they enlarged using a mixed bottom-up and top-down approach. They are currently expanding their work to create an integrated ontology of the three domains.

Other research on ontology construction for military applications includes Bowman et al. ([2001](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR1 "Bowman, Michael, Antonio López Jr., and Gheorghe Tecuci. 2001. Ontology development for military applications. In Proceedings of the Southeastern Regional ACM Conference, Atlanta, GA, March 16–17.")), Tolk and Smith ([2011](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR23 "Tolk, Andreas, and Barry Smith. 2011. Command and Control Ontology. International Journal of Intelligent Defence Support Systems 4: 209.")), and Nguyen et al. ([2010](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR19 "Nguyen, Duc N., Joseph B. Kopena, Thau Loo Boon, and William C. Regli. 2010. Ontologies for distributed command and control messaging. In Proceedings of the 2010 conference on formal ontology in information systems: proceedings of the sixth international conference (FOIS 2010), ed. A. Galton and R. Mizoguchi, 373–384. Amsterdam: IOS Press.")). Interestingly, the major focus in all of this work seems to be on military intelligence. Their target is ontology building—usually in the form of controlled, structured vocabularies—designed to allow the consistent description and analysis of heterogeneous bodies of data. Such vocabularies also are a means of linking terms in different languages by means of a common conceptual framework to facilitate mutual understanding. Though MiliMarco is by no means a formal ontology, this was also one of its goals. As shall be seen, MiliMarco is different from previous work, because it has the advantage of providing an expanded view of the military domain in the form of conceptual networks combined with linguistic contexts that go far beyond simple hierarchies.

### 2.3 Frame-based terminology

From a terminological perspective, MiliMarco incorporates aspects of NATOTerm, such as its three-level structure, data categories, and targeted user profiles; and aspects of the ontology-oriented approach, such as the categorization of military concepts in semantic structures. Underlying MiliMarco is a hierarchical structure of basic military concepts, which has been enhanced with more specific ones extracted from military texts (a corpus specifically compiled for the project) and the glossary itself. Concepts are viewed in semantic networks as conceived in Frame-Based Terminology (FBT) (Faber [2012](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR7 "Faber, Pamela (ed.). 2012. A cognitive linguistics view of terminology and specialized language. Berlin: De Gruyter."), [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR8 "Faber, Pamela. 2015. Frames as a framework for terminology. In Handbook of terminology, ed. H.J. Kockaert and F. Steurs, 14–33. Amsterdam: John Benjamins.")), a theory that focuses on: (1) conceptual organization; (2) the multidimensional nature of terminological units; and (3) the extraction of semantic and syntactic information from multilingual corpora.

The FBT approach to terminology and terminology management applies the notion of ‘frame’, defined as “a schematisation of experience (a knowledge structure), which is represented at the conceptual level and held in long-term memory and which relates elements and entities associated with a particular culturally embedded scene, situation, or event from human experience” (Evans and Green [2007](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR6 "Evans, Vyvyan, and Melanie Green. 2007. Cognitive linguistics: an introduction. New York: Routledge."): 85). Since frames highlight non-hierarchical as well as hierarchical conceptual relations, they provide a much richer representation and are also the foundation for the specification of conceptual categories and the generation of semantic networks. The following sections describe the creation of MiliMarco, a terminological knowledge base for the Spanish Armed Forces.

## 3 Materials and methods

The main aim of transforming alphabetical resources and making them more conceptual is to enhance knowledge understanding and acquisition. The military glossary that required a ‘total makeover’ was the *PD0* - *000 Glosario de Términos Militares*, official publication of the *Mando de Adiestramiento y Doctrina* (MADOC) of the Spanish Armed Forces. It had initially been published in March 2004. It underwent various revisions until the current glossary (2014), which has been adapted to the new doctrinal framework.

The first step was to extract the basic military concepts from the most frequent headwords (e.g., *fuerza* \[force\], *operación* \[operation\], *arma* \[weapon\], *instalación* \[installation\], etc.) as well as the information implicitly codified in the glossary term entries (i.e., hypernyms codified as the genus of definitions). These terms were used to create a kernel representation that was enhanced with concepts from upper level general ontologies (e.g. entidad \[entity\] → entidad no - animada \[inanimate entity\] → entidad concreta no - animada \[inanimate concrete entity\] → arma \[weapon\]) and also with more specific ones (arma \[weapon\] → misil \[missile\] → missile aire - tierra \[air - to - ground missile\]), collected from corpus information and the glossary. These were integrated into class hierarchies. In this sense, the approach was both bottom-up and top-down.

The current PD0-000 glossary is composed of 2259 entries arranged in alphabetical order. Each entry is accompanied by a definition, though some entries (those for polysemic terms) contain various definitions. Furthermore, the definitions, which had been formulated by military authorities, could not be altered even to improve their style and content. Apart from definitions, term entries are sometimes accompanied by synonyms, variants, abbreviations, and notes, which needed to be reconfigured according to the concept-oriented approach. Tables [1](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab1), [2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab2), [3](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab3) show four entries from the PD0-000, which illustrate data categories of terms (with synonyms, variants, and abbreviations), definitions, English equivalents, and notes.

**Table 1 Entries for ***autenticación/autentificación*** in the *Glosario de Términos Militares* (PD0 000)**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/1)

**Table 2 Entry for *derecho de autodefensa* \[right to self-defense\] and *autodefensa* \[self-defense\] in the *Glosario de Términos Militares* (PD0 000)**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/2)

**Table 3 Entry for *fuerza de reacción* \[reaction force\] in the *Glosario de Términos Militares* (PD0 000)**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/3)

The glossary uses different (and often confusing) ways to express synonyms, variants, and abbreviations. For example, when two terms (i.e., *autenticación* \[authentication\] and *autentificación* \[authentification\]) are interchangeable, they both appear as headwords in the term entry, in italics and separated by a slash (Table  [1](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab1)).

However, when two terms (e.g., *autodefensa* \[self-defense\] and *derecho de autodefensa* \[right to self-defense\] refer to the same concept, but one of them is the preferred term, only the preferred term (i.e., *derecho de autodefensa* \[right to self-defense\]) appears with a definition and full description. As shown in Table  [2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab2), the non-preferred term (*autodefensa* \[self-defense\]) is accompanied by the note *Véase* \[See\] followed by the name of the preferred entry, *derecho de autodefensa* \[right to self-defense\]).

Nevertheless, as can be observed, in the entry for *fuerza de reacción* \[reaction force\] (Table  [3](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab3)), when variants appear in the form of abbreviations, the English terms (RF, MDF, and AF) are often used. They are followed by the English headword in brackets. In this entry, notes are also used to include conceptual information, such as the subclasses of *reaction force* (i.e., *immediate reaction force* and *rapid reaction force*). This information was extremely useful for us, but unfortunately, its inclusion was the exception rather than the rule.

The subsections that follow explain the main steps in the process of creating the conceptual structure for the concepts in this glossary to transform it into a military knowledge base.

### 3.1 Terminology knowledge base design

The design and creation of a termbase stems from an explicit (or implicit) commitment to a set of premises regarding knowledge representation. The transmission and acquisition of technical information are enhanced when knowledge resources are designed, so that users, whether human or artificial, can easily access concepts and associate information to understand and acquire specialized knowledge.

Generally speaking, any terminology resource design project involves the following steps: (1) delimitation of the domain; (2) identification of the target group; (3) collection of documentation; (4) extraction of term and concept information; (5) selection of concepts to be included; (6) identification of concept relations and elaboration of concept systems; (7) elaboration of definitions; (8) selection and evaluation of terms (Dobrina [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR5 "Dobrina, Claudia. 2015. Getting to the Core of a Terminological Project. In Handbook of terminology, ed. H.J. Kockaert and F. Steurs, 180–202. Amsterdam: John Benjamins.")). At this stage, certain decisions must also be made about the type and scope of data categories, the granularity of the data in each entry or the definition of preset values for picklist-type data (Cerrella Bauer [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR2 "Cerrella Bauer, S. 2015. Managing terminology projects: concepts, tools and methods. In Handbook of terminology, ed. H.J. Kockaert and F. Steurs, 324–340. Amsterdam: John Benjamins.")).

After performing these tasks, designers must then decide how to present information. Apart from content, data presentation also depends on other aspects (Steurs et al. [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR22 "Steurs, Frieda, Ken De Wachter, and Evy De Malsche. 2015. Terminology Tools. In Handbook of terminology, ed. H.J. Kockaert and F. Steurs, 222–249. Amsterdam/Philadelphia: Benjamins.")), such as modes of visualization and interaction with the tool. The tool used for visualization of information and interaction was the ThinkMap visualization software package (Thinkmap.com). Evidently, the design parameters should be in consonance with user needs as well as their reasons for consulting the knowledge resource. In this regard, MiliMarco considered the same user types and communication needs as those considered in NATOTerm.

The microstructure of a terminological knowledge base comprises the data categories in each entry. The selection of fields reflects the information that users wish to know about concepts and terms (e.g., definition, part of speech, context, collocations, etc.). In regards to the macrostructure of the termbase, the choice of structure is just as important, since it affects the speed and types of possible knowledge access (e.g., frame-based, semantic networks, alphabetical order, etc.). From a multilingual perspective, conceptual structure in terminology resources can act as an anchor point for linking terms in different languages. In this way, it also provides a foundation for interlinguistic correspondence.

The new design of an entry in the MiliMarco \[MiliFrame\] knowledge base was partially based on NATOTerm. It also took into account the recommendations of TerminOrgs (Terminology for Large Organizations), a consortium that foments terminology management as part of the identity construction and communication strategy of large companies and organisms. From the TBX standard provided by TerminOrgs, we selected a series of data categories in line with the latest ISO standards, which were tailored to the context of the Spanish Armed Forces. Table [4](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab4) summarizes the structure of these fields at three levels (concept–language–term) along with the nature of each data category (i.e., mandatory, automatic, pick list, free text, etc.).

**Table 4 Knowledge base structure**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/4)

These data fields provide the contextual information for each entry in the form of usage examples (i.e., context) and phraseological constructions (i.e., collocations) or with regard to other concepts (i.e., conceptual categories and semantic relations). The design of the resource also accounts for the theoretical and practical considerations in NATO documents on terminology management (e.g., *Guidance for the Development and Publication of NATO Terminology*). For example *Term type* states whether the term is obsolete or preferred, and whether it is an abbreviation, acronym, etc. *Semantic relations* associate each entry with others that are semantically linked to it, similar to the field “related terms” in NATOTerm.

### 3.2 Identification of inventory of basic conceptual categories and relations in the glossary definitions

Although information was extracted from linguistic data, the assumption was that the resulting semantic networks encoded conceptual knowledge that was non-language-specific. However, non-language-specific information not only comes in the form of semantic relations, but also in the form of conceptual invariants encoded in a wide range of languages that are used for specialized communication.

As previously mentioned, an in-depth analysis of the glossary revealed the underlying structure of the domain. Any glossary of specialized knowledge units tells a story about the domain and the contexts activated within it. The terms and their patterns are like pieces in a jigsaw puzzle. The conceptual structure underlying the glossary can be extracted by specifying the relations between terms and then filling in the empty spaces. The terms in the glossary evidently encode the important actions and processes carried out, the actors or agents that participate in them, and the instruments used to perform them. The most knowledge structures that link categories and concepts are indicative of the most frequent actions, processes, and events that take place within the domain.

For design purposes, language structure was used as a conceptual mirror to extract the structure of a domain from the terminographic definitions in the glossary. Firstly, the superordinate term (*genus*) in each definition was used as a guideline for assigning each concept a general category. Then, semantic relations were extracted from the definitions’ *differentiae* to relate categories in a general frame-like structure and concepts in semantic networks (see Sect. [3.4](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec10)). Thus, the glossary was first converted into a pre-network structure derived from the glossary’s definitions and then enriched with corpus information (see Sect. [3.2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Sec8)).

For example, the definitions in Table [5](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab5) indicate that blister agent and pulmonary agent are both hyponyms of chemical weapon agent, since both are defined as chemical agent, whereas chemical agent contains a more superordinate *genus* (i.e., chemical substance). Therefore, the genus makes category membership explicit.

**Table 5 Definitions of chemical agent and its hyponyms blister agent and pulmonary agent in the glossary**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/5)

Furthermore, from the analysis of *differentiae,* we can extract the typical roles participating in military events (i.e., agent, action, patient, result, etc.) as well as the semantic relations (i.e., *type\_of*, *used\_during*, *has\_function*, *affects*, *result\_of*, *causes*, etc.) according to which the domain can be structured.

All of the glossary entries were analyzed following this procedure and classified in an inventory of conceptual categories, namely entities, actions, time, space, and attributes (Table  [6](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab6)). E ntities are divided into animate \_ entity and inanimate \_ entity. inanimate \_ entity is subdivided into concrete and abstract. There are also general categories for action, situation, measurement, and attribute. The main categories within animate \_ entity are military role, military group, installation, and equipment. Important abstract entities are cognitive (plan, strategy) and regulatory (rules, regulations, principles). In regard to actions, not surprisingly, the most important are those related to combat, movement, defense / protection, and manipulation (especially use of weapons and vehicles). Finally, the most important types of attribute are those related to capacity and power.

**Table 6 General conceptual categories**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/6)

These conceptual categories hold relations with each other in different knowledge structures composed of the following participants: agent, action, patient, and result / objective. These are the same participants that were extracted from the analysis of definitions in Table  [5](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab5).

Figure [1](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig1) shows the general military frame where all concepts and categories are accommodated within the domain. This frame structure, though not directly implemented in the resource, was the macrostructure or template underlying the relations between more specific conceptual categories. For example, agents are usually the armed forces (e.g., navy) or mental entities (e.g., plan) that initiate an action (e.g., attack) with an instrument (e.g., weapon) affecting patients, which can be animate entities (e.g., civilian) or locations (e.g., country), causing a result (e.g. peace).

![figure 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig1_HTML.png?as=webp)

**Fig. 1**

### 3.3 Corpus compilation and information extraction

Corpus information complemented the categories and relations first extracted from the definitions in the glossary. A bilingual corpus of approximately 30,000,000 words was compiled in English (15 million words) and Spanish (15 million words). This documentation process required the collaboration of various branches of the Spanish Armed Forces as well as access to classified information. The corpus compilation process was composed of the following stages: (1) identification of relevant documents; (2) downloading files and converting them into txt format; (3) semi-automatic cleaning of files to avoid codification problems with NotePad ++; (4) uploading files to a corpus analysis application (i.e., Sketch Engine); (5) corpus compilation with a lemmatizer, a POS Tagger and sketch grammars, one of the functionalities of Sketch Engine that permits the analysis of terms’ collocational behavior.

The compilation of both corpora was carried out both manually and automatically. Approximately half of the documents were those provided by the MADOC, which came from sources such as *Revista Española de Defensa*, *Boina Negra*, *Revista de Sanidad Militar,* publications on military doctrine, instruction manuals, and a wide range of NATO documents. When both corpora were uploaded to Sketch Engine, terms were automatically extracted to obtain new seed words which, though not included in the glossary, were sufficiently representative to be included in the knowledge base. They were used to automatically search the Internet for new corpus texts with the WebBootCaT tool, integrated in Sketch Engine. These key words also included a selection of those from the glossary, so that the corpus texts would be in consonance with the terms in the glossary. This allowed us to double the size of the corpus.

Once the corpus was compiled, the following types of data category were extracted from the corpus and populated in the knowledge base: conceptual categories, semantic relations, synonyms, term equivalents, contexts, and collocations. Sketch Engine offers different functionalities that can assist in the extraction of such data. For example, bilingual word sketches help to establish bilingual correspondences as well as to extract semantic relations, contexts, collocations, and new concepts and terms.

For example, in Fig. [2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig2), the modifiers of both *operación* and *operation* provide many hyponyms of the concept, whereas the verbs provide valuable information for the extraction of both semantic relations and collocations. For instance, the verbs that collocate with *operación/operation* as an object (e.g., *conducir* and *conduct*; *ejecutar* and *execute*; *apoyar* and *support*) can be extracted in a parallel view and their equivalence can be easily established.

![figure 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig2_HTML.png?as=webp)

**Fig. 2**

In contrast, other verbs such as *incluir* and *include* can be used to extract semantic relations and/or knowledge-rich contexts, since they often act as knowledge patterns (KPs) expressing hyponymic or meronymic relations. KPs are the lexico-syntactic patterns that usually codify semantic relations in natural language (Meyer [2001](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR18 "Meyer, Ingrid. 2001. Extracting knowledge-rich contexts for terminography: a conceptual and methodological framework. In Recent advances in computational terminology, ed. D. Bourigault, C. Jacquemin, and M.C. L’Homme, 279–302. Amsterdam: John Benjamins."); Marshman [2002](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR17 "Marshman, Elizabeth. 2002. The cause-effect relation in a biopharmaceutical corpus: English knowledge patterns. In: Proceedings of the 6th International Conference on Terminology and Knowledge Engineering, Nancy, France, pp 89–94.")). For example from the concordances in Fig. [3](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig3), thanks to the *includ\** KP, *nuclear war* and *conflict prevention* can be extracted as hyponyms of *military operation*, whereas *contaminated operations* and *uncontaminated operations* can be divided into different phases: *triage* and *emergency treatment*, and *treatment* and *final disposition*, respectively.

![figure 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig3_HTML.png?as=webp)

**Fig. 3**

KPs can be collected and stored in the form of a customized sketch grammar to extract semantic word sketches (León-Araúz et al. [2016](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR16 "León-Araúz, Pilar, Antonio San Martín, and Pamela Faber. 2016. Pattern-based word sketches for the extraction of semantic relations. In Proceedings of the 5th International Workshop on Computational Terminology (Computerm 2016), Osaka, Japan, pp. 73–82."); León-Araúz and San Martín [2018](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR15 "León-Araúz, Pilar, and Antonio San Martín. 2018. The EcoLexicon semantic sketch grammar: from knowledge patterns to word sketches. In Proceedings of the LREC 2018 workshop “Globalex 2018 – Lexicography and WordNets”, ed. I. Kerneman,  and S. Krek, 94–99. Globalex: Miyazaki.")). Thanks to these sketch grammars, developed by the authors of this paper, a set of concordances, based on a given semantic relation, can be accessed with a single click. Figure  [4](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig4) shows different types of operations (*area operation*, *COIN operation*, *maritime special operation*, *amphibious operation*, *UN* - *sponsored operation*, *defensive cyber operation*, *offensive cyber operation*, *joint operation*, *UW operation*, *combat operation*, *non-combatant evacuation operation*, *air operation*, *cyberspace operation*, *special operation*, *humanitarian relief operation*, etc.) that were generated, thanks to the activation of different KPs (*namely*, *including*, *like*, *any other*, *such as*, *i.e., are*, etc.)

![figure 4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig4_HTML.png?as=webp)

**Fig. 4**

Likewise, sketch grammars can also be designed to extract the multiword terms (MWTs) derived from a particular term, whether it acts as the head or the modifier.

From all of the entries in the glossary, a first set was selected and queried in the corpus, based on the multiword terms with a common head. In this way, conceptual gaps in the glossary were identified and new concepts were accommodated in the conceptual structure derived from the glossary.

For instance, Spanish has many terms that contain *operación* \[operation\] as their head (e.g., *operación especial* \[special operation\], *operación anfibia* \[amphibious operation\], *operación de mantenimiento de la paz* \[peacekeeping operation\], etc.). However, not all of the compounds found in the corpora were included in the glossary, such as *operación táctica* \[tactical operation\] or *combat operation,* in spite of being frequent modifiers of *operación* (Fig. [2](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig2)) and *operation* (Fig. [5](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig5)).

![figure 5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig5_HTML.png?as=webp)

**Fig. 5**

From the concordances of *operación táctica* \[tactical operation\] (Fig. [6](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig6)), which can be reused as contexts in the knowledge base, other types of information can be extracted based on the analysis of modifiers and KPs. These include hyponyms (e.g., *operación psicológica táctica* \[tactical psychological operation\], or *operación aéreo táctica* \[tactical air operation\]), other related concepts (e.g., *centro de operaciones tácticas* \[tactical operation center\]), synonyms and morphosyntactic variants (e.g., *operación aérea táctica* \[tactical air operation\] and *operación aéreo táctica* \[tactical air operation\]), abbreviations (e.g., OPSIC for *operación psicológica táctica* \[tactical psychological operation\]), and collocations (e.g., *llevar a cabo* \[carry out\], *ejecutar* \[execute\], *realizar* \[perform\], etc.).

![figure 6](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig6_HTML.png?as=webp)

**Fig. 6**

### 3.4 Specification of semantic networks stemming from conceptual propositions

Based on the general military frame (Fig. [1](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig1)) and the analysis of definitions and corpus information, concepts were structured in semantic networks by identifying and representing semantic relations, as shown in Fig. [7](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig7) for the concept operación militar \[*military operation*\]. The inventory of semantic relations so far is the following: *type\_of*, *part\_of*, *phase\_of*, *instrument\_of*, *controls*, *location\_of*, *attribute\_of*, *target\_of*, *affects*, *domain\_of*, *effected\_by*, *represents*, *measures*, *destroys*, *delimited\_by*, *result\_of*, *causes*, and *has\_function*.

![figure 7](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig7_HTML.png?as=webp)

**Fig. 7**

As depicted in the semantic network in Fig. [7](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig7), operación militar \[military operation\] is mostly characterized by the *type\_of* relation to its hyponyms. However, also present are meronymic relations (misión \[mission\] *part\_of* operación militar \[military operation\]) and non-hierarchical relations (marco operativo \[operational framework\] *represents* operación militar \[military operation\]).

The concept, operación militar \[military operation\], is an important conceptual category as reflected by the many subconcepts lexicalized. Its semantic relations were inferred from the implicit knowledge contained in the glossary definitions and the explicit knowledge derived from the analysis of KPs found in the corpus. However, the language structure of compound terms can also be used to derive important information about semantic relations. For example, *operación* \[operation\] is the head of many MWTs, such as *operación de apoyo* \[support operation\], *operación de extracción* \[extraction operation\], etc. Such terms are a frequent way to condense and concentrate domain-specific knowledge (Sager et al. [1980](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR20 "Sager, Juan C., David Dungworth, and Peter F. McDonald. 1980. English Special Languages. Principles and Practice in Science and Technology. Wiesbaden, Germany: Oscar Brandstetter Verlag."); Štekauer et al. [2012](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR21 "Štekauer, Pavol, Salvador Valera, and Lívia Körtvélyessy. 2012. Word-formation in the World’s Languages: a Typological Survey. Cambridge: Cambridge University Press."); Fernández-Domínguez [2016](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR9 "Fernández-Domínguez, Jesús. 2016. A morphosemantic investigation of term formation processes in english and spanish. Lang Contrast 16 (1): 54–83.")).

This type of concept specialization involves a slot-filling mechanism where the modifier is inserted into a slot in the head-noun schema, also known as its micro-context (Cabezas-García and Faber [2018](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#ref-CR3 "Cabezas-García, Melania, and Pamela Faber. 2018. Phraseology in specialized resources: an approach to complex nominals. Lexicography 5 (1): 55–83.")). In an MWT, the modifier is directly related to the base meaning of the head noun as (under)specified in the definition and is interpreted accordingly. Slots for *operation* correspond to agent, objective, scope, and location. The glossary definitions for *military operation* and a few of its subtypes are given in Table  [7](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab7).

**Table 7 Definitional hierarchy of military operation and subtypes**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/7)

Since the definitions only provided very general information, it was necessary to enrich them with corpus data in the form of other multiword terms corresponding to the specialization of slots in the head-noun schema. For example, military operation (operation carried out by the military) reflects an agent slot, whereas peace support operation (operation carried out to support peace) reflects the purpose of the operation. The structure of the category of military operation was found to have a five-dimensional structure, specified as follows in the MWTs:

- agent slot: armed forces of one or various nations.
- purpose / objective slot: support (mainly for peace) and extraction (evacuation).
- location slot: air/water/land.
- scope slot: range/nature.
- theme slot: intelligence.

Table [8](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Tab8) shows the full specification of each dimension with the corresponding Spanish terms. This means that the hyponymic relation *type\_of* can be further specified according to each dimension and that the semantic network of operación militar \[military operation\] and its subtypes should be enriched with more non-hierarchical relations, namely those related to agents (e.g., *causes*, *result\_of*), purpose (e.g. *has\_function*), location (e.g., *delimited\_by*, *location\_of*), scope, and theme (e.g., *has\_function*, *affects*).

**Table 8 Specification of the five-dimensional structure of operación militar**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y/tables/8)

## 4 Results and discussion

This project posed a series of challenges related to the existing as well as the missing information in the glossary. For example, the definitions, many of which were not consistently formulated or did not adequately clarify the term defined, could not be altered to make their structure more uniform or clearer, because they are standardized by the Spanish military forces.

Another challenge stemmed from the conversion of a term-oriented glossary into a concept-oriented knowledge base. This involved the following: (1) creating different entries for terms with various definitions; (2) disambiguating polysemic terms; (3) adding synonyms and identifying different definitions that pointed to the same concept and merging them in a single entry (sometimes several definitions were provided not because the term was polysemic, but because the sources were different); (4) converting the semantic information contained in the definitions and notes of each entry into conceptual propositions in the knowledge base.

The few English terms in the glossary (706) were linked to each concept entry and new equivalents were included for the rest of them. When possible, equivalents from NATOTerm were used, but in many cases, it was necessary to use corpus information to fill the gaps. In addition, new concepts and terms were included based on the gaps encountered in the glossary and the terms extracted from the corpus.

After applying the automatic term extraction functionality in Sketch Engine, a list of term candidates was collected. These new terms were added (1) as synonyms and variants in the existing entries; (2) as new concept entries when they were not available in the glossary; (3) as collocational information associated with terms.

New concept entries were also created based on the analysis of MWTs and querying the corpus with their most recurrent heads. This allowed us to identify hierarchical inconsistencies. For example, in the case of apoyo \[support\] and its subtypes, the glossary reflected an inconsistent granularity level. While *logistic support*, and all of its subtypes, were present at different hierarchical levels, *fire support* was not even included as an entry, even though seven different hyponyms of *fire support* were found in the corpus and despite the fact that many other related concepts were included in the glossary (*fire support unit*, *fire support coordinator*, *quick fire support plan*, *fire support coordination line*, *fire support officer*, etc.).

Therefore, new entries were added either as top-level umbrella concepts, to make category membership explicit, or at intermediate and subordinate hierarchical levels to make the hierarchy coherent at all levels. Furthermore, there were certain terms that were not found in the corpus, at least not as they appeared in the glossary. For instance, *fuego en eficacia* (fire for effect) is only found in the corpus as *fuego de eficacia*, where the preposition *en* (in) changes to *de* (of). When comparing the terms in the glossary with those of the corpus, other inconsistences were found regarding MWT formation. For example, *base de apoyo avanzado* (forward mounting base) coexists with *base de apoyo avanzada*. According to inflection rules in Spanish, in the first case, *avanzado* \[forward\] (masculine) agrees with *apoyo* \[support\], whereas in the second case, *avanzada* (feminine) complements *base*. In the same manner, the order of MWT components does not follow a systematic pattern, since terms like *dosis de radiación crónica* and *dosis crónica de radiación* \[chronic radiation dose\] have the same frequency in the corpus. In these cases, all possible variants were collected, and experts will be the ones to ultimately categorize each of them as preferred, accepted, or deprecated.

Regarding semantic networks, thanks to definition and MWT analysis, word sketches, and KP-based sketch grammars and queries, semantic relations were extracted from the corpus and represented in the knowledge base in semantic networks. Finally, images were collected from public repositories, based on the information conveyed and the nature of the concepts described, to enhance the conceptual structure shown in their semantic network.

Currently, MiliMarco shows all this information in a dynamic concept-oriented interface (see Fig. [8](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig8)). It is publicly available in [https://www.ecolexicon.ugr.es/milimarco](https://www.ecolexicon.ugr.es/milimarco) and contains 2354 entries, 5409 terms in Spanish and English, and 2803 conceptual propositions. As can be seen, the upper area shows the definition, terms, and images for each military concept. On the left panel, users can access entries by browsing through conceptual categories, whereas on the right and main area of the screen, semantic networks are shown. Users can click on any of the concepts in this network and reconfigure their structure around the new concept in an interactive way. They can even change the settings to customize the networks (i.e., number of nodes, relations displayed, distance between nodes, labels of the relations, etc.).

![figure 8](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig8_HTML.png?as=webp)

**Fig. 8**

There are also different access and visualization modes of concepts, such as a tree-like structure (Fig. [9](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig9)), where only *type\_of* relations are shown. Users can also opt to access concepts alphabetically (Fig. [10](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig10)).

![figure 9](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig9_HTML.png?as=webp)

**Fig. 9**

![figure 10](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig10_HTML.png?as=webp)

**Fig. 10**

Finally, in the upper ribbon, users can find: (1) definitions in which all terms have a hyperlink to their entry; (2) term information, such as terms, synonyms, variants, equivalents, sources, term types, etc. and access to concordances; (3) images. When clicking on the *Ver concordancias* \[See concordances\] button or when typing the term in the corresponding box, different contexts from the corpus are shown (Fig. [11](https://link-springer-com.sire.ub.edu/article/10.1007/s40607-019-00060-y#Fig11)). Therefore, users can access each entry by different means: (1) by querying a particular concept/term in the search box; (2) by clicking in the terms contained in definitions; (3) by browsing through the networks; (4) by browsing through the list of conceptual categories; or (5) by clicking in the alphabetically arranged list of concepts.

![figure 11](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs40607-019-00060-y/MediaObjects/40607_2019_60_Fig11_HTML.png?as=webp)

**Fig. 11**

As highlighted in this description, MiliMarco provides a wide range of information regarding military concepts that give users access to both semantic and linguistic contexts. It is thus an improvement over a conventional termbase, not to say a glossary, and provides a new ontological view of the military domain that is quite different from previous work.

## 5 Conclusions

Inevitably, the design and information included in a terminology knowledge base depend on user needs and the decoding and/or encoding tasks to be carried out by them. This is less a question of the number of data categories, and more a question of effective information access, extraction, and analysis. Conceptual data can be extracted from definitions (semantic analysis) and texts (corpus analysis), or by eliciting information from experts by means of a protocol involving a questionnaire, discussion group, a series of intensive interviews, etc. Designers can also use both methods and place their main focus on one or the other, depending on the context.

A terminological knowledge base can have an alphabetical search mechanism, but at the same time, it can also allow users to opt for a conceptual search. Although electronic resources do not have the space constraints of paper documents, other problems can arise, since decoding the meaning underlying a set of terms in a specialized field is an extremely complex task. One of the difficulties is the perception of conceptual similarities, relations, and patterns in term meaning within a highly specialized domain such as military science. The other difficulty is linked to the choice and configuration of design parameters.

For this proposal, we took the *Glosario de Términos Militares* (PD0-000) and structured it conceptually. Our analysis was mainly based on semantic and corpus analysis, though the results were also subjected to expert validation. The implicit conceptual structure underlying the glossary highlights the important structuring role of actions and processes in regards to object categories, as shown in the general military event and as exemplified in the multidimensional structure of military operations.

MiliMarco has been successfully completed since the 2259 terms in the *Glosario de Términos Militares* (PD0 000) have been conceptually organized in categories and contextualized in semantic networks. It is available on a ThinkMap platform, which allows information to be viewed in multiple formats. The project is still ongoing, because even though English and Spanish designations are given for each concept, other languages (e.g., French, German, and Italian) should also be included. This would entail creating a corpus for each new language. The knowledge base should be further enriched with more multimodal information, such as images and videos. It also needs to be tested in the field to evaluate its usefulness for different language-understanding tasks. Even though there is still much to be done, MiliMarco is an extremely sophisticated terminology resource that provides a wide range of information-sharing possibilities in multinational military scenarios.

## Notes

1. [http://termin.eki.ee/militerm/](http://termin.eki.ee/militerm/).
2. Stabilization Force, a NATO-led peacekeeping force after the Bosnian war.
3. [http://rdf.muninn-project.org/ontologies/military.html](http://rdf.muninn-project.org/ontologies/military.html).

## References

- Bowman, Michael, Antonio López Jr., and Gheorghe Tecuci. 2001. Ontology development for military applications. In *Proceedings of the Southeastern Regional ACM Conference*, Atlanta, GA, March 16–17.
- Cerrella Bauer, S. 2015. Managing terminology projects: concepts, tools and methods. In *Handbook of terminology*, ed. H.J. Kockaert and F. Steurs, 324–340. Amsterdam: John Benjamins.
	[Chapter](https://doi-org.sire.ub.edu/10.1075%2Fhot.1.17man1)
- Cabezas-García, Melania, and Pamela Faber. 2018. Phraseology in specialized resources: an approach to complex nominals. *Lexicography* 5 (1): 55–83.
	[Article](https://link-springer-com.sire.ub.edu/doi/10.1007/s40607-018-0046-x)
- Stevenson, A. (ed.). 2011. *Concise Oxford english dictionary*, 12th ed. Oxford: Oxford University Press.
	[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Concise%20Oxford%20english%20dictionary&publication_year=2011)
- Dobrina, Claudia. 2015. Getting to the Core of a Terminological Project. In *Handbook of terminology*, ed. H.J. Kockaert and F. Steurs, 180–202. Amsterdam: John Benjamins.
	[Chapter](https://doi-org.sire.ub.edu/10.1075%2Fhot.1.get1)
- Evans, Vyvyan, and Melanie Green. 2007. *Cognitive linguistics: an introduction*. New York: Routledge.
- Faber, Pamela (ed.). 2012. *A cognitive linguistics view of terminology and specialized language*. Berlin: De Gruyter.
	[Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20cognitive%20linguistics%20view%20of%20terminology%20and%20specialized%20language&publication_year=2012)
- Faber, Pamela. 2015. Frames as a framework for terminology. In *Handbook of terminology*, ed. H.J. Kockaert and F. Steurs, 14–33. Amsterdam: John Benjamins.
	[Chapter](https://doi-org.sire.ub.edu/10.1075%2Fhot.1.02fra1)
- Fernández-Domínguez, Jesús. 2016. A morphosemantic investigation of term formation processes in english and spanish. *Lang Contrast* 16 (1): 54–83.
	[Article](https://doi-org.sire.ub.edu/10.1075%2Flic.16.1.03fer)
- Jones, Ian. 2011. The NATO terminology programme and NATOTerm. In *Proceedings of the 33rd Translating and the Computer Conference*, London. [http://www.mt-archive.info/Aslib-2011-Jones.pdf](http://www.mt-archive.info/Aslib-2011-Jones.pdf).
- Jones, Ian, and Louise Askew. 2014. *Meeting the language challenges of NATO operations: policy, practice and professionalization*. London: Palgrave McMillan.
	[Book](https://doi-org.sire.ub.edu/10.1057%2F9781137312563)
- León-Araúz, Pilar, and Antonio San Martín. 2018. The EcoLexicon semantic sketch grammar: from knowledge patterns to word sketches. In *Proceedings of the LREC 2018 workshop “Globalex 2018 – Lexicography and WordNets”*, ed. I. Kerneman, and S. Krek, 94–99. Globalex: Miyazaki.
- León-Araúz, Pilar, Antonio San Martín, and Pamela Faber. 2016. Pattern-based word sketches for the extraction of semantic relations. In *Proceedings of the 5th International Workshop on Computational Terminology (Computerm 2016)*, Osaka, Japan, pp. 73–82.
- Marshman, Elizabeth. 2002. The cause-effect relation in a biopharmaceutical corpus: English knowledge patterns. In: *Proceedings of the 6th International Conference on Terminology and Knowledge Engineering*, Nancy, France, pp 89–94.
- Meyer, Ingrid. 2001. Extracting knowledge-rich contexts for terminography: a conceptual and methodological framework. In *Recent advances in computational terminology*, ed. D. Bourigault, C. Jacquemin, and M.C. L’Homme, 279–302. Amsterdam: John Benjamins.
	[Chapter](https://doi-org.sire.ub.edu/10.1075%2Fnlp.2.15mey)
- NATO (North Atlantic Treaty Organization). 2011. *Linguistic Support for Operations, ALING P-1*. [http://nso.nato.int/nso/zPublic/ap/alingp-1.pdf](http://nso.nato.int/nso/zPublic/ap/alingp-1.pdf).
- Nguyen, Duc N., Joseph B. Kopena, Thau Loo Boon, and William C. Regli. 2010. Ontologies for distributed command and control messaging. In *Proceedings of the 2010 conference on formal ontology in information systems: proceedings of the sixth international conference (FOIS 2010)*, ed. A. Galton and R. Mizoguchi, 373–384. Amsterdam: IOS Press.
- Rey, Alan (ed.). 2019. *Le Petit Robert de la Langue Française*. Paris: Le Robert.
	[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Le%20Petit%20Robert%20de%20la%20Langue%20Fran%C3%A7aise&publication_year=2019)
- Sager, Juan C., David Dungworth, and Peter F. McDonald. 1980. *English Special Languages. Principles and Practice in Science and Technology*. Wiesbaden, Germany: Oscar Brandstetter Verlag.
- Štekauer, Pavol, Salvador Valera, and Lívia Körtvélyessy. 2012. *Word-formation in the World’s Languages: a Typological Survey*. Cambridge: Cambridge University Press.
	[Book](https://doi-org.sire.ub.edu/10.1017%2FCBO9780511895005)
- Steurs, Frieda, Ken De Wachter, and Evy De Malsche. 2015. Terminology Tools. In *Handbook of terminology*, ed. H.J. Kockaert and F. Steurs, 222–249. Amsterdam/Philadelphia: Benjamins.
	[Chapter](https://doi-org.sire.ub.edu/10.1075%2Fhot.1.12ter3)
- Tolk, Andreas, and Barry Smith. 2011. Command and Control Ontology. *International Journal of Intelligent Defence Support Systems* 4: 209.
- Valente, Andre, Douglas Holmes, and Frank C. Alvidrez. 2005. Using a military information ontology to build semantic architecture models for airspace systems. *IEEE Aerospace Conference Proceedings*. [https://doi-org.sire.ub.edu/10.1109/aero.2005.1559635](https://doi-org.sire.ub.edu/10.1109/aero.2005.1559635).
	[Article](https://doi-org.sire.ub.edu/10.1109%2Faero.2005.1559635)
- Yoo, Donghee, Sungchun No, and Minyoung Ra. 2014. A practical military ontology construction for the intelligent army tactical command information system. *International Journal of Computers, Communications and Control* 9 (1): 93–100.
	[Article](https://doi-org.sire.ub.edu/10.15837%2Fijccc.2014.1.49)

[Download references](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/s40607-019-00060-y?format=refman&flavour=references)

## Acknowledgements

This research was carried out as part of the projects FFI2017-89127-P, funded by the Spanish Ministry of Economy and Competitiveness; and PIN 5/18, funded by the CEMIX UGR-MADOC.

## Author information

### Authors and Affiliations

1. Department of Translation and Interpreting, University of Granada, Buensuceso, 11, 18002, Granada, Spain
	Pamela Faber & Pilar León-Araúz

### Corresponding author

Correspondence to [Pilar León-Araúz](https://link-springer-com.sire.ub.edu/article/10.1007/).

## Ethics declarations

### Conflict of interest

On behalf of all authors, the corresponding author states that there is no conflict of interest.

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

## About this article

[![Check for updates. Verify currency and authenticity via CrossMark](https://link-springer-com.sire.ub.edu/article/10.1007/)](https://crossmark-crossref-org.sire.ub.edu/dialog/?doi=10.1007/s40607-019-00060-y)

### Cite this article

Faber, P., León-Araúz, P. Frame-based terminology applied to military science: transforming a glossary into a knowledge resource. *Lexicography ASIALEX* **6**, 105–131 (2019). https://doi-org.sire.ub.edu/10.1007/s40607-019-00060-y

[Download citation](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/s40607-019-00060-y?format=refman&flavour=citation)

- Received:
- Accepted:
- Published:
- Issue Date:
- DOI: https://doi.org/10.1007/s40607-019-00060-y

### Share this article

Anyone you share the following link with will be able to read this content:

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Terminology knowledge base](https://link-springer-com.sire.ub.edu/search?query=Terminology%20knowledge%20base&facet-discipline=%22Linguistics%22)
- [Military science](https://link-springer-com.sire.ub.edu/search?query=Military%20science&facet-discipline=%22Linguistics%22)
- [Frame-based terminology](https://link-springer-com.sire.ub.edu/search?query=Frame-based%20terminology&facet-discipline=%22Linguistics%22)
- [Corpus linguistics](https://link-springer-com.sire.ub.edu/search?query=Corpus%20linguistics&facet-discipline=%22Linguistics%22)

This website sets only cookies which are necessary for it to function. They are used to enable core functionality such as security, network management and accessibility. These cookies cannot be switched off in our systems. You may disable these by changing your browser settings, but this may affect how the website functions. Please view our privacy policy for further details on how we process your information.