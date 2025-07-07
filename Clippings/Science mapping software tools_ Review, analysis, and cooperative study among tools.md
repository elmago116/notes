---
title: "Science mapping software tools: Review, analysis, and cooperative study among tools"
source: https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/asi.21525
author:
  - "[[Wiley Online Library]]"
published: 
created: 2025-05-12
description: Science mapping aims to build bibliometric maps that describe how specific disciplines, scientific domains, or research fields are conceptually, intellectually, and socially structured. Different tec...
tags:
  - bibliometrics/KW
  - bibliometrics/software
---
citar APA: Cobo, M.J., López-Herrera, A.G., Herrera-Viedma, E. and Herrera, F. (2011), Science mapping software tools: Review, analysis, and cooperative study among tools. J. Am. Soc. Inf. Sci., 62: 1382-1402. [https://doi-org.sire.ub.edu/10.1002/asi.21525](https://doi-org.sire.ub.edu/10.1002/asi.21525)


[[Science mapping software tools_ Review, analysis, and cooperative study among tools.pdf]]

[[Science mapping software tools- Review, analysis, and cooperative study among tools_note.pdf]]
## Abstract

Science mapping aims to build bibliometric maps that describe how specific disciplines, scientific domains, or research fields are conceptually, intellectually, and socially structured. Different techniques and software tools have been proposed to carry out science mapping analysis. The aim of this article is to review, analyze, and compare some of these software tools, taking into account aspects such as the bibliometric techniques available and the different kinds of analysis.

## Introduction

Science mapping, or bibliometric mapping, is an important research topic in the field of bibliometrics (Morris & Van Der Veer Martens, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib42); van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)). It attempts to find representations of intellectual connections within the dynamically changing system of scientific knowledge (Small, [1997](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib66)). In other words, science mapping aims at displaying the structural and dynamic aspects of scientific research (Börner, Chen, & Boyack, [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib8); Morris & Van Der Veer Martens; Noyons, Moed, & Luwel, [1999a](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib45)).

The general workflow in a science mapping analysis has different steps: data retrieval, preprocessing, network extraction, normalization, mapping, analysis and visualization. At the end of this process, the analyst has to interpret and obtain some conclusions from the results.

There are different bibliometric sources where the data can be retrieved, such as the ISI Web of Science (WoS) or Scopus. Moreover, a science mapping analysis can be performed using patent or funding data.

The preprocessing step is maybe one of the most important ones. The goodness of the result will depend on the quality of the data. Several preprocessing methods can be applied, for example, to detect duplicate and misspelled elements.

Different approaches have been developed to extract networks using the selected units of analysis (authors, documents, journals, and terms). *Co-word* analysis (Callon, Courtial, Turner, & Bauin, [1983](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib12)) uses the most important words or keywords of the documents to study the conceptual structure of a research field. *Co-author* analyzes the authors and their affiliations to study the social structure and collaboration networks (Gänzel, [2001](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib25); Peters & van Raan, [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib48)). Finally, the cited references are used to analyze the intellectual base used by the research field or to analyze the documents that cite the same references. In this sense, *bibliographic coupling* (Kessler, [1963](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib33)) analyzes the citing documents, whereas *co-citation* analysis (Small, [1973](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib65)) studies the cited documents. Other approaches such as author bibliographic coupling (Zhao & Strotmann, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib83)), author co-citation (White & Griffith, [1981](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib79)), journal bibliographic coupling (Gao & Guan, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib26); Small & Koenig, [1977](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib70)), and journal co-citation (McCain, [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib39)) are examples of macro analysis using aggregated data.

Once the network has been built, a normalization process is commonly performed over the relation (edges) between its nodes by using similarity measures. A review of similarity measures used in science mapping was carried out in (van Eck & Waltman, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib74)).

With the normalized data different techniques can be used to build the map (mapping process; Börner et al., [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib29)). Dimensionality reduction techniques such as principal component analysis or multidimensional scaling (MDS), clustering algorithms and Pathfinder networks (PFNETs) are widely used.

Analysis methods for science mapping allow us to extract useful knowledge from data. *Network analysis* (Carrington, Scott, & Wasserman, [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib78); Cook & Holder, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib19); Skillicorn, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib63); Wasserman& Faust, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib78)) allows us to perform a statistical analysis over the generated maps to show different measures of the whole network or measures of the relationship or overlapping (the Jaccard's Index can be used to do that) of the different detected clusters (if a clustering algorithm has been applied). *Temporal analysis* (Garfield, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib27); Price & Gürsey, [1975](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib54)) aims to show the conceptual, intellectual, or social evolution of the research field, discovering patterns, trends, seasonality, and outliers. *Burst detection* (Kleinberg, [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib34)), a particular temporal analysis, aims to find features that have high intensity over finite durations of time periods. Finally, *geospatial analysis* (Batty, [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib6); Leydesdorff & Persson, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib35); Small & Garfield, [1985](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib69)) aims to discover where something happens and what its impact on neighbouring areas is.

Additionally, visualization techniques are used to represent a science map and the result of the different analyses, for example, the networks can be represented using *heliocentric maps* (Moya-Anegón et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib43)), *geometrical models* (Skupin, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib64)), *thematic networks* (Bailón-Moreno, Jurado-Alameda, & Ruíz-Baños, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2); Cobo, López-Herrera, Herrera-Viedma, & Herrera, [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)), ==or maps where the proximity between items represents their similarity (Davidson, Wylie, & Boyack, [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib21); Polanco, François, & Lamirel, [2001](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib50); van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75))==. To show the evolution in different time periods, *Cluster string* (Small, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib68); Small & Upham, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib71); Upham & Small, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib72)), and *thematic areas* (Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)) can be used.

Although the science mapping analysis can be performed using generic social network analysis tools such as Pajek (Batagelj & Mrvar, [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib5)) and UCINET (Borgatti, Everett, & Freeman, [2002](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib7)), or bioinformatics software such as Cytoscape (Shannon et al., [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib61)), there are other software tools specifically developed for this purpose. Some of these software tools are specifically conceived for scientific science mapping and others may be used in nonscientific domains. Some of these software tools have been implemented only for visualizing science maps and others allow us to visualize and also build the maps. A list of generic software tools used in scientometrics research is shown in Börner et al. ([2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib9)).

The aim of this article is to present a deep comparative study of nine representative science mapping software tools by showing their advantages, drawbacks and most important differences. We analyze the following software tools: Bibexcel (Persson, Danell, & Wiborg ==Schneider, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib47)), CiteSpace II (Chen, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib14), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib15)), CoPalRed (Bailón-Moreno, Jurado-Alameda, Ruíz-Baños, & Courtial, [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib3); Bailón-Moreno et al., [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2)), IN-SPIRE (Wise, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib80)), Leydesdorff's Software, Network Workbench Tool (Börner et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib9); Herr, Huang, Penumarthy, & Börner, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib29)), Science of Science (Sci <sup>2</sup>) Tool (Sci <sup>2</sup> Team, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib60)), VantagePoint (Porter & Cunningham, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib51)), and VOSViewer (van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75))==. Each one provides us with its own view of the data due to the fact that they implement different analysis techniques and algorithms. We should point out that they present complementary characteristics, and, therefore, it could be desirable to take their synergies to perform a complete science mapping analysis. We complete our analysis by showing the performance of all software tools with an example, and analyze some positive synergies among them.

This article is organized as follows. In the Science Mapping section, some concepts on science mapping are presented. The Software Tools Designed to Perform a Science Mapping Analysis: A Survey section describes the software tools to be analyzed. In the Comparative Study section, a comparison is made among the described software tools. In the Analysis of Generated Maps: A Cooperative Study Among Tools section, we show the performance of the software tools with a set of data and analyze their possible positive synergies. In the Lessons Learned section, we note some lessons learned. Finally, some concluding remarks are made.

## Science Mapping

Science mapping or bibliometric mapping is a spatial representation of how disciplines, fields, specialities, and individual documents or authors are related to one another (Small, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib67)). It is focused on monitoring a scientific field and delimiting research areas to determine its cognitive structure and its evolution (Noyons, Moed, & van Raan, [1999b](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib46)).

In this section, different important aspects of a science mapping analysis are described, such as: (a) the data sources, (b) the units of analysis, (c) the data preprocessing, (d) the similarity measures that can be used to normalize the relations between the units of analysis, (e) the mapping steps, (f) the types of methods of analysis that can be employed, (g) some visualization techniques, and finally, (h) interpretation of results.

### Data Sources

Nowadays, there are several online bibliographic (and also bibliometric) databases where scientific works and documents and their citations are stored. These sources of bibliographic information allow us to search and retrieve information about the majority of scientific fields. Undoubtedly, the most important bibliographic databases are ISI WoS ([http://www.webofknowledge.com.sire.ub.edu](http://www.webofknowledge.com.sire.ub.edu/)), Scopus ([http://www-scopus-com.sire.ub.edu](http://www-scopus-com.sire.ub.edu/)), Google Scholar ([http://scholar.google.com](http://scholar.google.com/)), and NLM's MEDLINE ([http://www.ncbi.nlm. nih.gov/pubmed](http://www.ncbi.nlm.nih.gov/pubmed)).

ISI WoS, Scopus, and Google Scholar do not cover the scientific fields and journals in the same way, as different studies show. There are different studies (Bar-Ilan, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib4); Falagas, Pitsouni, Malietzis, & Pappas, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib24); Mikki, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib40)) that relate this fact. Moreover, downloading large datasets from Google Scholar is difficult and a dump of the entire dataset is not available.

There are other bibliographic sources that can be used, such as: arXiv ([http://arxiv.org](http://arxiv.org/)), CiteSeerX ([http://citeseerx.ist.psu.edu/](http://citeseerx.ist.psu.edu/)), Digital Bibliography & Library Project (DBPL; [http://dblp.uni-trier.de/](http://dblp.uni-trier.de/)), SAO/NASA Astrophysics Data System (ADS; [http://adswww.harvard.edu/](http://adswww.harvard.edu/)), Science Direct ([http://www.sciencedirect.com.sire.ub.edu/](http://www.sciencedirect.com.sire.ub.edu/))

Patent data and funding data are also frequently used. Patent data can be retrieved from specific data sources such as the United States Patent and Trademark Office (USPTO; [http://www.uspto.gov/](http://www.uspto.gov/)) or the Derwent Innovations Index provided by ISI WoS. Funding data can be downloaded from the National Science Foundation ([http://www.nsf.gov/](http://www.nsf.gov/))

### Units of Analysis in Bibliometric Techniques

The most common units of analysis in science mapping are journals, documents, cited references, authors (the author's affiliation can also be used), and descriptive terms or words (Börner et al., [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib8)). The words can be selected from the title, abstract, body of the document, or some combinations of them. Furthermore, we can select the original keywords of the documents (author's keywords) or the indexing ones provided by the bibliographic data sources (e.g., ISI Keywords Plus) as words to analyze.

Several relations among the units of analysis can be established. Usually, the units of analysis are used as a co-occurrence data by the science mapping process, that is, the similarity between the units of analysis is usually measured counting the times that two units appear together in the documents. Furthermore, direct linkage can be used to obtain the relations among units.

The relation among units can be represented as a graph or network, where the units are the nodes and the relations among them represent an edge between two nodes, that is, by using relationships among units of analysis, different bibliometric networks can be built.

In Table [1](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl1), a taxonomy of the most common bibliometric techniques according to the units of analysis used and the established relationships among them is presented.

<table><thead><tr><th colspan="2">Bibliometric technique</th><th>Unit of analysis used</th><th>Kind of relation</th></tr></thead><tbody><tr><td>Bibliographic coupling</td><td>Author</td><td>Author's oeuvres</td><td>Common references among author's oeuvres</td></tr><tr><td></td><td>Document</td><td>Document</td><td>Common references among documents</td></tr><tr><td></td><td>Journal</td><td>Journal's oeuvres</td><td>Common references among journal's oeuvres</td></tr><tr><td>Co-author</td><td>Author</td><td>Author's name</td><td>Authors' co-occurrence</td></tr><tr><td></td><td>Country</td><td>Country from affiliation</td><td>Countries' co-occurrence</td></tr><tr><td></td><td>Institution</td><td>Institution from affiliation</td><td>Institutions' co-occurrence</td></tr><tr><td>Co-citation</td><td>Author</td><td>Author's reference</td><td>Co-cited author</td></tr><tr><td></td><td>Document</td><td>Reference</td><td>Co-cited documents</td></tr><tr><td></td><td>Journal</td><td>Journal's reference</td><td>Co-cited journal</td></tr><tr><td>Co-word</td><td></td><td>Keyword, or term extracted from</td><td>Terms' co-occurrence title, abstract or document's body</td></tr></tbody></table>

Different aspects of a research field can be analyzed depending on the selected units of analysis, for example, by using the authors (co-author or co-authorship analysis) the social structure of a scientific field can be analyzed (Gänzel, [2001](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib25); Peters & van Raan, [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib48)). Likewise, by using the author's affiliations—co-institution, co-university, or co-country—, the international dimension of the research field is studied. On the other hand, co-word (Callon et al., [1983](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib12)) analysis is used to show the conceptual structure and the main concepts treated by a field. Co-citation (Small, [1973](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib65)) and bibliographic coupling (Kessler, [1963](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib33)) are used to analyze the intellectual structure of a scientific research field. The difference between bibliographic coupling and co-citation is that bibliographic coupling is a fixed and permanent relationship because it depends on the references contained in coupled documents, whereas co-citation will vary over time (Jarneving, [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib31)).

Bibliographic coupling and co-citation can be extended using journals and authors. Particularly, author bibliographic coupling (Zhao & Strotmann, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib83)) aims at discovering co-author relationships between authors that cite the same references, whereas journal bibliographic coupling (Gao & Guan, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib26); Small & Koenig, [1977](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib70)) aims at discovering the journals that cite the same references. On the other hand, author co-citation (White & Griffith, [1981](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib79)) aims to discover the authors that are frequently cited together, whereas journal co-citation analysis (McCain, [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib39)) discovers the journals that are co-cited frequently. Furthermore, journal bibliographic coupling and journal co-citation can be extended to a category journal level. This supra-level of journal co-citation has been used to study the marrow of science (Moya-Anegón et al., [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib44)) using the ISI categories.

Finally, a relation between units can be established using direct linkages, for example, a document-document, author-author, or journal-journal citation network. Furthermore, a relation can be established using different units, for example, an author-paper (consumed/produced) network.

### Data Preprocessing

The data retrieved from the bibliographic sources normally contains errors, for example, misspelling in the author's name, in the journal title, or in the references list. Sometimes, additional information has to be added to the original data, for example, if the author's address is incomplete or wrong. For this reason, a science mapping analysis cannot be applied directly to the data retrieved from the bibliographic sources, that is to say, a preprocessing process over the retrieved data is necessary. In fact, the preprocessing step is perhaps one of the most important for improving the quality of the units of analysis (mainly authors and words) and thus to obtain better results in the science mapping analysis.

Different preprocessing processes can be applied to prepare the data to get a good performance in the science mapping analysis:
- Detecting duplicate and misspelling items. Sometimes, there are items in the data that represent the same object or concept but with different spelling, for example, an author's name can be written in different ways (e.g., Garfield, E.; Eugene Garfield), and yet each way represents the same author. In other cases, a concept can be represented with different words (lexical forms) or acronyms, and yet represent the same concept. To detect duplicate items and misspelling enables these errors to be fixed.
- The time slice process is useful to divide the data into different time subperiods, or time slices, to analyze the evolution of the research field under study. This process is only necessary if the science mapping analysis is made in the context of a longitudinal study (Garfield, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib27); Price & Gürsey, [1975](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib54)).
- Data reduction aims to select the most important data. Normally, we have a large amount of data. With such a quantity of data, it could be difficult to get good and clear results in the science mapping analysis. For this reason, it is ordinarily carried out using a portion of the data. This portion could be, for example, the most cited articles, the most productive authors, and the journals with the best performance metrics.
- Networks preprocessing can be used to select the most important nodes of the network of relationships between the units of analysis (bibliometric networks) according to different measures, removing the isolated nodes, removing the less important links between nodes, etc.

### Normalization Process

When the network of relationships between the selected units of analysis has been built, a transformation is first applied to the data to derive similarities from the data or, more specifically, to normalize the data (van Eck & Waltman, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib74)).

Different similarity measures have been used in the literature, the most popular being *Salton's Cosine* (Salton & McGill, [1983](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib58)), *Jaccard's Index* (Peters & van Raan, [1993](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib49)), *Equivalence Index* (Callon, Courtial, & Laville, [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib11)), and *Association Strength* (Coulter, Monarch, & Konda, [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib20); van Eck & Waltman, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib73)), which is also known as *Proximity Index* (Peters & van Raan, [1993](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib49); Rip & Courtial, [1984](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib56)) or *Probabilistic Affinity Index* (Zitt, Bassecoulard, & Okubo, [2000](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib84)).

Usually, a normalization of the document's terms is needed; for example, if a co-citation analysis is performed and various clusters are detected, then a label should be set to each one. This label should be selected using the most important document's terms of the cluster. The text normalization sets a weight to each term according to its importance in the corpus. Different text normalization measures can be applied (Baeza-Yates & Ribeiro-Neto, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib1); Chen, Ibekwe-SanJuan, & Hou, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib16); Salton & McGill, [1983](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib58)): tf·idf, latent semantic analysis, log-likelihood ratio tests, log entropy, mutual information, etc.

### The Mapping Step

The mapping step is the most important one. The process itself is responsible for building the map by applying a mapping algorithm to the whole network formed using the relationships among the selected units of analysis.

Different techniques have been proposed to build the map (Börner et al., [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib8)). Dimensionality reduction techniques such as principal component analysis or MDS are used to transform the network into a low-dimension space (often two-dimension). Clustering algorithms are used to perform community detection, splitting the global network into different subnetworks. Recently, some authors have proposed new and different clustering algorithms to carry out this task: *Streemer* (Kandylas, Upham, & Ungar, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib32)), *spectral clustering* (Chen et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib17)), *modularity maximization* (Chen & Redner, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib17)). and a *bootstrap resampling* with a significance clustering (Rosvall & Bergstrom, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib57)), among others. Finally, Pathfinder networks (PFNETs) are used to identify the backbone of the network (Quirin, Cordón, Santamaría, Vargas-Quesada, & Moya-Anegón, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib55); Schvaneveldt, Durso, & Dearholt. [1989](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib59)). Furthermore, general graph mining techniques (Cook & Holder, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib19); Skillicorn, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib63)) or social network analysis (Carrington et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib13); Wasserman & Faust, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib78)) can be used in the mapping step.

The information obtained and the kind of map built will depend of the applied technique.

### Analysis Methods

Once the map has been built, different analyses can be applied to extract useful knowledge.

*Network analysis* (Carrington et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib13); Cook & Holder, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib19); Skillicorn, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib63); Wasserman & Faust, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib78)) allows us to perform a statistical analysis over the generated map in the later step, for example, different measures on the network, such as the total number of nodes and isolated nodes, average degree, the number of weakly connected components, or the graph density can be measured. If a community detection algorithm was applied to build the map, then Callon's centrality and density (Callon et al., [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib11); Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)) or other values that measure the relationships among the detected clusters can be used. Moreover, the overlapping between the clusters can be measured using, for example, the Jaccard's Index. Furthermore, if documents are assigned to each cluster, a performed analysis can be carried out to obtain quantitative or qualitative measures of each cluster (Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)).

Another important analysis that can be performed in a science mapping process is the *temporal analysis,* which aims to identify the nature of phenomena represented by a sequence of observations such as patterns, trends, seasonality, and outliers. In other words, it aims to analyze the evolution of the research field across different periods of time. This task can be performed using a longitudinal framework (Garfield, [1994](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib27); Price & Gürsey, [1975](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib54)).

*Burst detection* is a kind of temporal analysis. It aims to find features that have a high intensity over finite durations of time periods. In Kleinberg ([2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib34)), an algorithm to deal with this problem was described.

Finally, *geospatial analysis* (Batty, [2003](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib6); Leydesdorff & Persson, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib35); Small & Garfield, [1985](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib69)) aims to answer the question of where something happens and with what impact on neighbouring areas. Geospatial analysis requires spatial attribute values or geolocations for the units of analysis; this data is usually extracted from affiliation data.

### Visualization Techniques

As we have shown in the previous subsection, the output of each analysis method is different. The visualization technique employed is very important to a good understanding and better interpretation of the output.

The networks and subnetworks detected in the mapping step can be represented using *heliocentric maps* (Moya-Anegón et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib43)), *geometrical models* (Skupin, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib64)), and *thematic networks* (Bailón-Moreno et al., [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2); Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)). Another approach consists of representing the networks in a map, where the distance between two items reflects the strength of the relation between both (Davidson et al., [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib21); Fabrikant, Montello, & Mark, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib23); Polanco et al., [2001](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib50); van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)). A smaller distance generally indicates a stronger relation (van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)).

If a community detection is applied, then the different clusters detected (subnetworks) can be categorized using a strategic diagram. A *strategic diagram* (Callon et al., [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib11); Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)) is a two-dimensional space built by plotting themes according to different measures extracted using a post network analysis.

To show the evolution of detected clusters in successive time periods (temporal analysis), different techniques have been used: *Cluster string* (Small, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib68); Small & Upham, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib71); Upham & Small, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib72)), *rolling clustering* ( Kandylas et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib32)), *alluvial diagrams* (Rosvall & Bergstrom, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib57)), *ThemeRiver visualization* (Havre, Hetzler, Whitney, & Nowell, [2002](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib28)), and *thematic areas* (Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)). Other authors propose laying out the graph of a given time period, taking into account the previous and subsequent ones ( Leydesdorff & Schank, [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib36)), or to pack synthesized temporal changes into a single graph (Chen, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib14); Chen et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib16)).

Geospatial results are usually visualized over a world or a thematic map. As an example, if a co-author analysis is applied and then a community detection is performed, the detected clusters of authors can be represented as a network in which each node is laid out over the author's country.

### Interpretation

When the science mapping analysis has finished, the analyst has to interpret the results and maps using their experience and knowledge.

In the interpretation step, the analyst looks to discover and extract useful knowledge that could be used to make decisions on which policies to implement.

## Software Tools Designed to Perform a Science Mapping Analysis: A Survey

Although the science mapping analysis can be performed using generic software for social network analysis (Börner et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib9)), there are other software tools specifically developed for science mapping analysis.

In this section, we present nine representative software tools specifically developed to analyze scientific domains by means of science mapping. These software tools are as follows:
- Bibexcel (Persson et al., [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib47))
- CiteSpace II (Chen, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib14), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib15))
- CoPalRed (Bailón-Moreno et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib3), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2))
- IN-SPIRE (Wise, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib80))
- Leydesdorff's Software
- Network Workbench Tool (Börner et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib9); Herr et al., [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib29))
- Sci <sup>2</sup> Tool (Sci <sup>2</sup> Team, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib60))
- VantagePoint (Porter & Cunningham, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib51))
- VOSViewer (van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75))

In Table [2](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl2) some details of these software tools are described.

| Software tool | Last version | Year | Developed by |
| --- | --- | --- | --- |
| Bibexcel | 2010–09–22 | 2010 | University of Umeå (Sweden) |
| CiteSpace | 2.2.R9 | 2010 | Drexel University (USA) |
| CoPalRed | 1.0 beta | 2005 | University of Granada (Spain) |
| IN-SPIRE | 5 | 2010 | Pacific Northwest National Laboratory |
| Leydesdorff's Software | N/A | N/A | University of Amsterdam (The Netherlands) |
| Network Workbench Tool | 1.0.0 | 2009 | Indiana University (USA) |
| Science of Science (Sci <sup>2</sup>) Tool | 0.0.3 alpha | 2010 | Indiana University (USA) |
| VantagePoint | 7 | 2010 | Search Technology, Inc. |
| VOSViewer | 1.2.1 | 2010 | Leiden University (The Netherlands) |

### Bibexcel

Bibexcel ([http://www.umu.se/inforsk/](http://www.umu.se/inforsk/) Bibexcel; Persson et al., [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib47)) is a bibliometric tool developed at the University of Umeå (Sweden). This tool was specifically developed to manage the bibliometric data and build maps, which can be read by software such as Excel, SPSS, UCINET (Borgatti et al., [2002](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib7)), and Pajek (Batagelj & Mrvar, [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib5)). Bibexcel is freely accessible for academic nonprofit use.

Bibexcel can read data retrieved from different bibliographic sources, such as ISI Web of Science (WoS), Scopus, and the Procite export format.

Bibexcel allows different preprocessing over the textual data to be performed, for example, an English word stemmer can be applied and duplicate documents can be deleted. Moreover, Bibexcel enables the deletion of low frequency items and keeps only the strongest links.

Different bibliometric networks can be extracted. The principal ones are as follows: co-citation, bibliographic coupling, co-author, and co-word. Furthermore, different co-occurrence matrices can be extracted using any document's field, or some combination of fields. The matrices can be normalized using three different measures: Salton's Cosine, Jaccard's Index, and the Vladutz and Cook measures.

To the normalized data, the user can apply a clustering algorithm or prepare a matrix for an MDS analysis (using external software). Bibexcel does not present an adequate visualization tool for the output, but it presents different export options that make data visualization possible using external software like Pajek, UCINET or SPSS. The bibliometric networks can also be exported.

### CiteSpace II

CiteSpace ([http://cluster.cis.drexel.edu/∼cchen/citespace](http://cluster.cis.drexel.edu/~cchen/citespace); Chen, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib14), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib15)) was developed at Drexel University (USA) and it can be freely downloaded. It is a software tool developed to detect, analyze, and visualize patterns and trends in scientific literature. Its primary goal is to facilitate the analysis of emerging trends in a knowledge domain.

CiteSpace can read different formats of bibliographic sources, such as WoS, PubMed, arXiv, and SAO/NASA Astrophysics Data System (ADS). Furthermore, CiteSpace is able to read grants data such as NSF Awards and patent data from Derwent Innovations Index.

Different kinds of bibliometric networks can be constructed: co-author, co-author institutions, co-author countries, co-grants,[1](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note1) [1](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note1_note_0 "Link to note") subject categories co-occurrence, co-word, documents co-citation, author co-citation, journal co-citation, and documents bibliographic coupling. The networks, or graphs, can be built for different time periods to analyze the evolution of the studied domain. Moreover, the analyst can filter the items with which the networks are built to select the most important of them (e.g., select the 100 most cited items from each time slice). The matrix (network) is normalized using Salton's Cosine, Dice, or the Jaccard's Index.

Once the networks have been built, CiteSpace allows us to visualize them and perform several analyses on them. CiteSpace allows the analyst to perform a spectral clustering and a citation burst detection. In addition, CiteSpace has three visualization modes (Chen, [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib15)): cluster view, time line, and time zone.

If clusters are detected, CiteSpace can assign labels to each one using the most important terms extracted from the keywords, title, or abstract. The terms are measured using the tf·idf, log-likelihood ratio tests, or mutual information (Chen et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib16)).

### CoPalRed

CoPalRed ([http://ec3.ugr.es/copalred/](http://ec3.ugr.es/copalred/); Bailón-Moreno et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib3), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2)) is a commercial software developed by the research group EC <sup>3</sup> at the University of Granada (Spain). It is specifically designed to perform co-word analysis using the keywords of scientific documents. It is described as a Knowledge System, which collects the information contained in databases and transforms it into new knowledge.

This software tool reads files in comma-separated values format (csv), generated through the reference manager software Procite.

One of the strengths of CoPalRed is that it contains a preprocessing module that allows users to normalize the keywords in a simple way. With this module, the user can unify items (lexical items) that represent the same concept. Once the keywords are unified, CoPalRed builds a co-occurrence matrix and normalizes it using the equivalence index (Callon et al., [1991](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib11)).

CoPalRed performs three kinds of analysis: structural analysis, strategic analysis, and dynamic analysis.
- Structural analysis. It shows the knowledge in the form of thematic networks in which words and their relationships are drawn.
- Strategic analysis. It places each thematic network in a relative position within the global thematic network using two criteria: centrality (or intensity of its external relations) and density (according to their internal cohesion density).
- Dynamic analysis. CoPalRed analyzes the transformations of the thematic networks over time. It identifies approaches, bifurcations, appearances, and disappearances of themes.

CoPalRed visualizes the results using strategic diagrams, themes, and thematic networks (Bailón-Moreno et al., [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib3), [2006](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib2); López-Herrera et al., [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib38), [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib37)). Each theme has assigned a label that is the name of the most central node (keyword) of its associated thematic network. Furthermore, each theme can be represented in the strategic diagram as a sphere, where its volume is proportional to the number of documents belonging to it. In the same way, each node (keyword) of the thematic network can be represented as a sphere where its volume is proportional to the keyword's frequency.

### IN-SPIRE

IN-SPIRE ([http://in-spire.pnl.gov](http://in-spire.pnl.gov/); Wise, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib80)) is a commercial visual document analysis software tool that gives the analyst the ability to uncover relationships, trends, and themes hidden within data to obtain new knowledge and new insights. IN-SPIRE uses landscape metaphor to help the user to easily discover the relationship among documents and the sets of documents that are very similar. This tool uses statistical word patterns to characterize documents based on their context (Hetzler & Turner, [2005](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib30)). IN-SPIRE derived from the SPIRE project funded by the Department of Energy and the U.S. intelligence agencies. It has been developed at Pacific Northwest National Laboratory (United States).

IN-SPIRE can read unformatted documents (ASCII text) or formatted documents such as HTML and XML. Furthermore, it can read data from Microsoft Excel documents and csv formatted files. The software allows the user to select the fields that will be used to measure the similarity among documents and other meta-fields such as the title of the documents and the associated date.

Unlike the other analyzed software tools, IN-SPIRE does not extract bibliometric networks from the selected field. It uses a field or a set of fields to calculate the similarity among documents using its own text engine (Wise, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib80)). In short, it uses the vector space model (Salton & McGill, [1983](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib58)), and thus each document is represented as a vector of terms. So, if keywords are selected as the field, then the similarity measure will show whether two documents have similar keywords. Although IN-SPIRE is able to build a map using any field, its text engine works better if words are selected as the field. The text engine needs a large amount of data to correctly detect the similarities among documents.

When the similarities among documents have been calculated, IN-SPIRE performs a cluster algorithm called “ *Fast Divisive Clustering* ” (Wise, [1999](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib80)). At the end of the clustering process, several themes (sets of documents) are generated. Each theme has as its name the more frequently appearing terms (using tf·idf) of its documents.

IN-SPIRE provides two different visualization techniques, which are the flagship of the software: *Galaxies* and *ThemeScape* ™. The Galaxies visualization employs the metaphor of documents as stars in the night sky. On the other hand, ThemeScape is constructed directly from the distribution of documents in the Galaxies visualization, representing themes as sedimentary layers that together create the appearance of a natural landscape. In the ThemeScape visualization, the height of its peaks corresponds to topic strength at those locations; the extent of its peaks corresponds to the area and brightness of the themes in the Galaxies visualization. In both visualizations, the proximity of two items (documents) reveals the similarity between them. Related documents are grouped together and common themes are highlighted.

IN-SPIRE provides a set of tools that help the analyst to discover knowledge within the corpus of studied documents:
- Time slicer allows us to see how particular themes grow or shrink over time and can show how the mix of themes in the galaxy changes over time.
- The Groups tool defines a collection of documents within the studied corpus.
- The Facets allows us to discover relationships between calculated themes as well as groups defined by the user.
- Robust query capabilities that support boolean, word proximity, phrase, or example-based searches.
- The Correlation tool allows us to discover correlation between the groups.

### Leydesdorff's Software

Leydesdorff's software ([http://www.leydesdorff.net](http://www.leydesdorff.net/)) is a set of command-line programs that enable a science mapping with different analysis functions to be performed. It was developed at the University of Amsterdam (The Netherlands). The set of programs is freely accessible to the academic community.

The different programs allow the performance of several bibliometric analyses: co-word, co-author, author bibliographic coupling, journal bibliographic coupling, and author co-citation. The results can be visualized using external software such as Pajek (Batagelj & Mrvar, [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib5)), UCINET (Borgatti et al., [2002](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib7)), Network Workbench Tool (see Subsection 3.6), or the Sci <sup>2</sup> Tool (see Subsection 3.7). Moreover, international and institutional collaboration, and collaboration at the level of cities can be analyzed. The visualization of these collaboration networks can be done using Google Maps and external software. The different matrices are normalized using the Salton's Cosine measure.

There are programs for organizing the data downloaded from different sources (WoS, Scopus, Google Scholar, and Google) into a database. This database will be the input file of the different analysis programs.

The set of programs does not allow the data to be preprocessed; so, for example, to perform a longitudinal analysis, external software is needed to split the data into different time periods.

### Network Workbench Tool

The Network Workbench (NWB) Tool ([http://nwb.slis. indiana.edu](http://nwb.slis.indiana.edu/)) is a general network analysis, modelling, and visualization toolkit for physics, biomedical, and social science researchers (Börner et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib9); Herr et al., [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib29)). It was developed by the *Cyberinfrastructure for Network Science Center* at Indiana University (USA) and is freely accessible.

The NWB Tool provides specific algorithms to deal with publications data to construct and analyze bibliometric networks and maps. The tool is able to read different bibliometric data formats such as ISI WoS, Scopus, Bibtex, and EndNote Export Format. It can also read funding data from the National Science Foundation (NFS) and other scholarly data in csv format.

The NWB Tool allows the data to be preprocessed, different kinds of networks to be built, a graph analysis over the built networks to be performed, and finally their visualization. Moreover, the tool is able to carry out a temporal analysis.
- Data preprocessing is performed removing duplicate records, dividing the data by different time periods, and detecting and unifying duplicate items with different spelling (i.e., items that represent the same author in a co-author analysis or terms that represent the same concept in a co-word analysis).
- The NWB Tool allows different kinds of networks to be built: documents co-citation, co-author, co-word, and documents bibliographic coupling. Furthermore, the tool can build networks by direct linkage; for example, it can build an author-document network (consumed/produced) or a direct citation network.
- Several algorithms can be used to perform the mapping step and a graph analysis on the generated networks. Furthermore, the tool is able to carry out a burst detection to identify increases in the usage frequency of items.
- The visualization of the generated graphs is carried out through different external plugins (e.g., GUESS, Jung). Furthermore, several graph layouts can be applied such as the DrL algorithm, which is the opensource successor of VxOrd (Davidson, Hendrickson, Johnson, Meyers, & Wylie, [2001](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib22)) that was used in the VxInsight program (Boyack, Wylie, & Davidson, [2002](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib10); Davidson et al., [1998](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib21)).

### Sci2 Tool

The Sci <sup>2</sup> Tool ([http://sci.slis.indiana.edu](http://sci.slis.indiana.edu/)) is a modular toolset specifically designed to perform the study of science. It supports temporal, geospatial, topical, and network analysis and the visualization of datasets at the micro (individual), meso (local), and macro (global) levels (Sci <sup>2</sup> Team, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib60)). It was developed by *Cyberinfrastructure for Network Science Center* at Indiana University (USA) and it is freely accessible.

The Sci <sup>2</sup> Tool is similar to the NWB Tool (see Network Workbench Tool section), but it is specifically focused on science studies and has specific algorithms to deal with this topic. The most important strength of the tool could be that it provides several methods to deal with bibliometric data, to prepare it for later analysis.

Similarly to the NWB Tool, the Sci <sup>2</sup> Tool is able to read different bibliographic data formats: ISI WoS, Scopus, Bibtex, and EndNote Export Format. It can also read funding data from the National Science Foundation (NFS) and other scholarly data in csv format.

The Sci <sup>2</sup> Tool allows the data to be prepared and preprocessed, extracting different types of networks, performing a temporal, geospatial, topical, and network analysis, and finally visualizing the results through different plugins and layout algorithms. Sci <sup>2</sup> Tool includes the DrL layout algorithm.

The data preparation cleans the bibliographic data and creates different networks and tables that can be used in preprocessing, analysis, and visualization. Principally, the networks that can be extracted are as follows: co-author, co-PI (Principal investigator), co-word, document co-citation, journal co-citation, author co-citation, author bibliographic coupling, document bibliographic coupling, and journal bibliographic coupling. Moreover, the tool can build different direct linkage networks such as author-citation, document-citation, source-citation paper, and, finally, author-document (consumed/produced) network.

The tool contains several algorithms to perform the mapping step and next applies different analyses. The mapping step can be performed using community detection and backbone identification. Temporal analysis is performed slicing the data into different time periods and through a burst detection. Geospatial analysis is performed through geocoding and geospatial thematic maps. Topic analysis is performed through a burst detection over the words and a co-word analysis. Network analysis allows a statistical analysis and the application of different algorithms over the networks.

### VantagePoint

VantagePoint ([http://www.thevantagepoint.com/](http://www.thevantagepoint.com/); Porter & Cunningham, [2004](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib51)) is a powerful commercial text-mining software tool for discovering knowledge in search results from patent and literature databases, or generally from structured texts. It allows the user to analyze large volumes of structured text to discover patterns and relationships and quickly address *who, what, when*, and *where*. It was developed by Search Technology Inc. (USA). VantagePoint has been used to perform several science mapping analyses (Morel, Serruya, Penna, & Guimarães, [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib41); Porter & Youtie, [2009a](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib52),[2009b](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib53); Shapira, Youtie, & Porter, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib62)).

VantagePoint has 180 import filters that allow the user to import data from almost any literature or patent database. Furthermore, it has import filters to load data from Microsoft Excel and Access, XML file format [2](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note2) [2](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note2_note_1 "Link to note") or used-defined filters.

Once the dataset is loaded, VantagePoint shows the different fields included in the dataset; for example, if the dataset contains bibliographical information, then the fields could be the title, authors, affiliations, abstract, and references of the documents (records).

The VantagePoint graphic interface has three parts: the workspace, the title view, and the detail windows. The workspace displays all of the lists, matrices, and map views generated by the user. The title view displays the titles of the records in the dataset for a selected set of items. Finally, the detail window shows the co-occurrence of items in one field (any field can be selected) with items or nodes selected using lists or charts.

This software tool allows us to build different lists from any field. The lists show all of the field's items from the dataset. In the list view, for each item, the number of records where the item appears and the number of instances (number of times that the items appear in the dataset, taking into account the duplicate items in the records) is shown. The items of a list can be assigned to several groups. Groups are useful for defining a portion of the dataset to reduce the data used in the later analysis, for example, a group containing the top 30 authors can be built. The items can be associated with more than one group.

One strength of VantagePoint is its preprocessing and data cleaning tools. A list can be cleaned or reduced using the Cleanup function, which attempts to identify the items that may be equivalents, performing fuzzy near matches on specific fields. Moreover, a list can be cleaned, applying a thesaurus. Although VantagePoint has several predefined thesauruses that can be easily used, the user can define his/her own thesaurus or edit an existing thesaurus using the Thesaurus Editor. Any change performed over a list will generate a new list, so we always keep the original data.

VantagePoint allows several kinds of matrices to be built that show the records in the dataset contained in two given lists:
- Co-occurrence matrix: it shows the number of records in which the element i (from the first list) and the element j (from the second list) appear together.
- Auto-correlation matrix: it shows the correlations among items in a list.
- Cross-correlation matrix: it shows the correlations among items in a list based on the values of another list.
- Factor matrix: it is the result of a principal component analysis. The factor matrix shows the items in rows and the factors in columns.

VantagePoint also allows different matrices to be built that can be used as the input in the mapping process: co-author (using the author's name, affiliation or country), co-citation (using the reference, reference's author or source), and co-word (using any set of terms). Furthermore, if the selected lists to build the matrix are different, heterogeneous matrices can be built; for example, the user can build a matrix of author per year to analyze the author's productivity. The matrices can be exported into a text file, or the user can directly copy a selection of the matrix and paste it in Microsoft Excel.

The correlation matrices can be normalized using Pearson's r, Salton's Cosine or the Max Proportional measures. Furthermore, the co-occurrence matrix can be normalized using the tf·idf similarity measure.

VantagePoint includes three kinds of maps that correspond to the three last matrices: cross-correlation map, auto-correlation map, and factor map. These maps are a graphical representation of the corresponding matrices. In the cross-correlation maps, the similarity between items is measured using the cosine. In the factor map, and auto-correlation the similarity measure used is Pearson's r.

Finally, VantagePoint also includes the capability to execute Visual Basic scripts to make repetitive (and/or complex) actions that a user may require.

### VOSViewer

VOSViewer ([http://www.vosviewver.com](http://www.vosviewver.com/); van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)) is a software tool specifically designed for constructing and visualizing bibliometric maps, paying special attention to the graphical representation of such maps. It is appropriate to represent big maps since zoom functionality, special labelling algorithms, and density metaphors are used. The software tool was developed by the *Centre for Science and Technology Studies* at Leiden University (The Netherlands) and it is freely available to the bibliometric research community.

Although VOSViewer can be used to construct and visualize bibliometric maps of any kind of co-occurrence data, the software tool does not allow any co-occurrence matrix from the bibliometric data to be extracted and built. To do this, an external process is needed. Furthermore, the software tool has no preprocessing modules to prepare the data for later analysis.

To lay out the elements on the maps, the VOS mapping technique (van Eck, Waltman, Dekker, & van den Berg, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib76)) is used by VOSViewer. This technique builds a similarity matrix from a co-occurrence matrix using a similarity measure known as the association strength (van Eck & Waltman, [2007](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib73), [2009](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib74)). The VOS mapping technique builds a two-dimensional map in which the elements are located in such way that the distance between any pair of items reflects their similarity as accurately as possible. The idea of the VOS mapping technique is to minimize a weighted sum of squared Euclidean distances between all pairs of items through an optimization process.

Although VOSViewer implements the VOS mapping technique, the program can also be used to view any two-dimensional map constructed with other techniques. VOSViewer allows us to perform a community detection using the VOS clustering technique, which is related to the technique of modularity-based clustering (Waltman et al., [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)). Once the map is built, VOSViewer allows its examination through four views:
- Label view. In this view each element is represented by a label and also by a circle. The more important an item, the larger its label and its circle. Thanks to an intelligent algorithm, which shows only the most important labels (most frequent) depending on the level of zoom, the software tool avoids the label overlapping. The circles that have the same color belong to the same cluster. This color is the same as the corresponding cluster's color in the cluster view.
- Density view. In this view, each item is represented by a label in a similar way as in the label view. Each point in the map has a color that depends on the density of items at that point, which depends both on the number of neighbouring items and on the weights of these items. VOSViewer calculates the density of each point according to the equation defined by (van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)), which uses a Gaussian kernel function. The density is translated using a color scheme (for more information see van Eck & Waltman; [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75))).
- Cluster density view. This view is available only if items have been previously assigned to a cluster. The cluster density view is similar to the ordinary density view except that the density of items is displayed separately for each cluster of items.
- Scatter view. This is a simple view in which items are indicated by a small circle and in which no labels are displayed.

## Comparative Study

As mentioned above, in this article, we also present a comparative study of the nine software tools described above. In such a way, we are able to highlight the main differences and positive synergies existing among the different software tools. To do so, we analyze the nine software tools taking into account five points of view: (a) the preprocessing methods, (b) the bibiometric networks available, (c) the normalization measures used, (d) the type of analysis, and finally, (e) other secondary aspects.

### Preprocessing Methods

Special modules to perform a preprocessing of the data are important characteristics of a science mapping software tool. In Table [3](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl3), the principal preprocessing modules available in each software tool are shown.

| Software tool | De-duplication | Time slicing | Data reduction | Network reduction |
| --- | --- | --- | --- | --- |
| Bibexcel |  |  | x | x |
| CiteSpace |  | x | x | x |
| CoPalRed | x | x | x |  |
| IN-SPIRE |  |  | x |  |
| Leydesdorff's Software |  |  |  |  |
| Network Workbench Tool | x | x | x | x |
| Science of Science Tool | x | x | x | x |
| VantagePoint | x | x | x |  |
| VOSViewer |  |  |  |  |

The module to detect duplicate items is important, for example, in co-word analysis or co-author analysis. With this module, a user could decide to join two or more items that represent the same concept or the same author. This module does not only merge two items but also selects or sums up the attribute value, for example, the times cited of the original records.

A time slicing option is needed if the user wants to analyze the evolution of the domains under study. A module for reducing the data is useful if the user wants to filter the data to analyze the most important information.

Finally, network reduction is useful to filter the nodes or links of a network (similar to the reducing data module), or to apply a pruning algorithm to the networks.

Only NWB Tool and Sci <sup>2</sup> Tool have the four preprocessing modules. By contrast, Leydesdorff's Software and VOSViewer do not have any of these modules, which is a strong drawback.

IN-SPIRE performs the time slicing directly over the data. It does not need to preprocess the data to split the dataset into different slices.

### Bibliometric Relation Between Units of Analysis

An important consideration in the use of some science mapping software tools is whether they are able to establish different relationships between the units of analysis, that is, if they are able to extract different bibliometric networks.

In Table [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl4), the different bibliometric networks available are shown for each software tool. The column “ *others* ” means that the software tool is able to build other un-common or heterogeneous networks or matrices.

<table><thead><tr><td></td><th colspan="3">Bibliographic coupling</th><th colspan="3">Co-author</th><th colspan="3">Co-citation</th><td></td><td></td><td></td></tr><tr><th>Software tool</th><th>Author (ABCA)</th><th>Document (DBCA)</th><th>Journal (JBCA)</th><th>Author (ACAA)</th><th>Country (CCAA)</th><th>Institution (ICAA)</th><th>Author (ACA)</th><th>Document (DCA)</th><th>Journal (JCA)</th><th>Co-word (CWA)</th><th>Direct Linkage (DL)</th><th>Others</th></tr></thead><tbody><tr><td>Bibexcel</td><td></td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>CiteSpace</td><td></td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>CoPalRed</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>IN-SPIRE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Leydesdorff's</td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Software</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Network</td><td></td><td>x</td><td></td><td>x</td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td>x</td><td></td></tr><tr><td>Workbench</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tool</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Science of Science Tool</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>VantagePoint</td><td></td><td></td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>VOSViewer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

Although there are no software tools able to build all of the different varieties of bibliometric networks, Bibexcel, CiteSpace, Leydesdorff's Software, Sci <sup>2</sup> Tool, and VantagePoint are the software tools able to build the majority of them. By contrast, VOSViewer is not able to build any of them; it is focused only on visualizing bibliometric maps. CoPalRed is focused only on one kind of bibliometric network. Finally, although IN-SPIRE can construct the maps using any field of the dataset, its way of representing the documents, by using the vector space model, makes it difficult to generate the maps using other fields such as the authors. It works better using words.

Some software tools allow the extraction of un-common networks, for example, the co-grant networks available in CiteSpace, co-PI networks available in Sci <sup>2</sup> Tool, or the particular matrices that are extracted by Bibexcel and VantagePoint using a set of specific documents' fields. Furthermore, some software such as Bibexcel and VantagePoint allow us to extract heterogeneous networks using different fields in the rows and columns, for example, a matrix showing the authors per years can be extracted.

Finally, NWB Tool and Sci <sup>2</sup> Tool can extract bibliometric networks using direct linkage.

### Normalization Measures

Once the bibliometric networks have been built, a normalization process can be carried out using different similarity measures. In Table [5](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl5), the measures used for each software tool are shown.

| Software tool | Measure |
| --- | --- |
| Bibexcel | Salton's Cosine, Jaccard's Index, or the Vladutz and Cook measures |
| CiteSpace | Salton's Cosine, Dice or Jaccard Strength |
| CoPalRed | Equivalence Index |
| IN-SPIRE | Conditional Probability |
| Leydesdorff's Software | Salton's Cosine |
| Network Workbench Tool | User defined |
| Science of Science Tool | User defined |
| VantagePoint | Pearson's r, Salton's Cosine or the Max Proportional |
| VOSViewer | Association Strength |

Three of the analyzed software tools use Salton's Cosine as a similarity measure. Other software tools like NWB Tool and Sci <sup>2</sup> Tool allow the users to define their own measures.

### Methods of Analysis

Different methods of analysis can be applied. In Table [6](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl6), the different methods of analysis available for each software tool are shown.

| Software tool | Burst detection | Geospatial | Network | Temporal |
| --- | --- | --- | --- | --- |
| Bibexcel |  |  | x |  |
| CiteSpace | x | x | x | x |
| CoPalRed |  |  | x | x |
| IN-SPIRE | x |  | x | x |
| Leydesdorff's Software |  |  |  |  |
| Network Workbench Tool | x |  | x | x |
| Science of Science Tool | x | x | x | x |
| VantagePoint | x | x | x | x |
| VOSViewer |  |  | x |  |

Only CiteSpace, Sci <sup>2</sup> Tool, and VantagePoint use the four kinds of analysis. Leydesdorff's Software does not carry out any of them.

CiteSpace and Sci <sup>2</sup> Tool have geocoding capabilities. CiteSpace uses Google and Yahoo!'s geocoder over the institutional data available. On the other hand, Sci <sup>2</sup> Tool uses Yahoo!'s geocoding service and an internal geocoder over any field that contains geographical data, such as institutional address and conference location.

### Other Aspects

In this subsection, we compare the software tools according to other aspects such as documentation/help, free or commercial availability, whether the source code is available, the possibility of installing the software in different platforms, and the extendability of the software.

NWB Tool and Sci <sup>2</sup> Tool have a great user guide where the tools are explained in detail. Furthermore, the user guide explains important aspects of science mapping; these are the only tools that explain this issue. VantagePoint has a good user guide and online help, and its website provides a large amount of video-tutorials. IN-SPIRE has a great website with video tutorials and online help. VOSViewer has a good manual. CiteSpace has a big wiki where important issues are described. Leydesdorff's Software has a good description and user guide for each of its command-line programs on its website.

Only three of the nine described software tools are commercial: CoPalRed, IN-SPIRE, and VantagePoint. The remaining software tools are freely available.

Taking into account the availability of the source code, only NWB Tool and Sci <sup>2</sup> make their source code available.

CiteSpace, NWB Tool, Sci <sup>2</sup> Tool, and VOSViewer were developed using the Java programming language, so they can be used with any platform (Windows, MacOS, Linux, etc.). On the other hand, Bibexcel, CoPalRed, IN-SPIRE, Leydesdorff's Software, and VantagePoint run only under Windows.

Finally, taking into account the possibilities of extending the software tools, NWB Tool and Sci <sup>2</sup> Tool are built over Cyberinfrastructure Shell (CIShell; [http://cishell.org/](http://cishell.org/)), so it can be extended using this platform. According to the description given on its website, CIShell “is an open source, community-driven platform for the integration and utilization of datasets, algorithms, tools, and computing resources.” VantagePoint can be extended using VisualBasic scripts.

## Analysis of Generated Maps: A Cooperative Study Among Tools

To complete the comparative study among the software tools, in this section, we develop a cooperative study of the software tools with a set of data. This cooperative use of different software tools gives us the opportunity to discover the possible positive synergies that could generate the joint use of these software tools.

To make a better comparison between software, a common science mapping analysis over a specific unit of analysis has to be performed. As was shown in Table [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl4), the analyzed software tools are unable to extract the same bibliometric networks, with co-word network the only one available in each software tool. For this reason, we select the words (or keywords) as the unit of analysis to perform the science mapping analysis.

As an example, we study the conceptual structure (Cobo et al., [2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)) of the research field of fuzzy set theory (FST; Zadeh, [1965](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib81), [2008](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib82)) by using the publications that have appeared in the most important and prestigious journals during 2005 to 2009, according to their impact factor,[3](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note3) [3](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note3_note_2 "Link to note") on the topic: *Fuzzy Sets and Systems* and *IEEE Transactions on Fuzzy Systems*. Cobo et al. ([2011](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib18)), who studied their conceptual evolution across five different periods of time, made a deep analysis of these journals recently. In this section, we use the last period of time (2005-2009) of that analysis.

The amount of documents analyzed was 1,576, and they were downloaded [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note4) [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note4_note_3 "Link to note") from the WoS. Specifically, 1,086 documents were published by the journal *Fuzzy Sets and Systems*, and 490 by *IEEE Transactions on Fuzzy Systems*.

The author's keywords and Keywords Plus of each document were used in the analysis. After a de-duplicating step (CoPalRed was used to carry out this task), there were 5,034 keywords. CoPalRed allows us to export the documents with the preprocessed items in a csv file, so this will be the input for the remaining software tools when possible. The whole network build from the co-occurrence of these keywords contains an amount of 25,705 links.

In what follows, the different results obtained by the software tools are shown. The comparative study has been performed using the software tools able to visualize the results. For this reason, Bibexcel and Leydesdorff's software have not been used.

First, a co-word analysis was performed using CiteSpace. Given that it does not allow us to load the data in csv format, the dataset had to be loaded without any preprocessing from an ISIWoS format file. In Figure [1](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig1), the map generated by CiteSpace is shown. The map was made using the top 200 keywords. The lines between nodes represent the cosine similarity measure. The shadowed nodes represent clusters and the clusters' names were chosen selecting the most important keywords from each cluster according to the tf·idf measure. Inside each cluster there is a sphere which represents its centroid, and its volume is proportional to the size of the cluster.

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/75e6d10b-1783-47d4-bf78-aeddce96b085/mfig001.jpg)

Figure 1 Open in figure viewer PowerPoint Map generated by CiteSpace. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

We have to say that the printed out map does not show the power of CiteSpace. To make a good interpretation of the obtained results, the analyst should interact with CiteSpace's user interface, which allows us to perform a variety of analyses, different layouts, etc. Furthermore, the analyst can zoom in and zoom out on the network to appreciate the details of a local area.

Second, in Figure [2](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig2a) the result obtained by CoPalRed is shown. In Figure [2a](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig2a) the generated strategic diagram is shown, and in Figure [2b](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig2b) the thematic network of a specific theme (*FUZZY-CONTROL*) is drawn. CoPalRed generated the maps using those keywords with a frequency equal to or higher than five and a co-occurrence value equal to or higher than three. The whole network contains 229 nodes and 432 links between them after this pruning. With this pruning, we maintain the most frequent and important keywords. The strategic diagram shows the main detected themes studied by the FST field in the studied period, categorizing them in four classes according to their *Callon's density* and *Callon's centrality* measures. Each theme in the strategic diagram is associated with a sphere and a label. Labels were chosen selecting the most central node of its associated thematic networks, where each node corresponds with a keyword. The volume of spheres represents the number of documents associated with each theme (or keyword in thematic networks). This information is also associated with the labels. Finally, the size of the lines in thematic networks represents the degree of association (equivalence index) between two nodes.

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/ddaf5749-2e75-4713-9496-86eb4c0c0ac2/mfig002.jpg)

Figure 2a Open in figure viewer PowerPoint CoPalRed's results—(a) Strategic diagram. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/1df2dc09-6eb1-43b4-b31f-d064987649ea/mfig003.jpg)

Figure 2b Open in figure viewer PowerPoint CoPalRed's results— (b) Thematic network. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

Third, the csv file exported by CoPalRed was loaded in IN-SPIRE. After defining the dataset, and selecting the terms, IN-SPIRE generated two maps: the Galaxy view (Figure [3](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig3)) and Theme view (Figure [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig4)).

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/db3711c9-9446-4ef8-a9af-be5ffe2f1f9e/mfig004.jpg)

Figure 3 Open in figure viewer PowerPoint IN-SPIRE's Galaxy view. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/a98a95f0-f7de-41b4-a19e-4b2885372623/mfig005.jpg)

Figure 4 Open in figure viewer PowerPoint IN-SPIRE's Theme view.

In the galaxy view, the shadows represent groups of documents that are considered to be similar. The names of these themes are generated using the most important keywords according to their tf·idf measure. In the Theme view, the height of each peak corresponds to topic strength at that location, and the extent of each peak corresponds to the area and brightness of the corresponding theme in the Galaxy view.

As we can see in both the Galaxy and Theme views, IN-SPIRE did not detect many themes, because of the way in which it interprets the data. Unlike the other software tools analyzed, IN-SPIRE uses the vector space model to represent the documents, so it needs a large amount of terms to correctly detect the themes. In our dataset, the documents do not contain the necessary keywords, so IN-SPIRE could not determine correctly the similarity among documents. Probably if we had used the abstract or the full text of the documents, IN-SPIRE would have to obtain better results.

Now, the csv file was loaded into Sci <sup>2</sup> Tool,[5](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note5) [5](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#note5_note_4 "Link to note") and a co-occurrence network using the keywords (author's keywords and Keywords Plus) was created. We applied a weak component clustering to the whole network obtained after dropping the keywords with a frequency below five and the links with a co-occurrence value below three (the whole network is the same as the generated by CoPalRed). The biggest weak component is shown in Figure [5](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig5). The size of the nodes is proportional to the respective keyword's frequency, and the size of the lines represents the co-occurrence (without normalization) of the linked nodes. Only the names of the top 50 keywords are shown. The color of the nodes varies in a linear way from gray to black according to their frequency, and the color of the links varies from green to black according to their co-occurrence value. The network was laid out using the GUESS plugin.

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/0516d00a-d88e-48dd-bc8a-141b69f5d122/mfig006.jpg)

Figure 5 Open in figure viewer PowerPoint Map generated by Science of Science (Sci 2 ) Tool. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

Fifth, a Factor Map was built by VantagePoint (Figure [6](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig6)) using those keywords with a frequency equal to or higher than five (after this pruning the dataset contains 392 keywords). Each node represents a cluster of terms. The label of each theme was chosen selecting its most important term. The size of nodes is proportional to the number of documents, and the line between nodes represents the similarity (Pearson's r) between factors.

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/b6a9fbdf-3228-4173-a479-681f6636d542/mfig007.jpg)

Figure 6 Open in figure viewer PowerPoint Map generated by VantagePoint. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

Finally, the co-occurrence matrix generated by CoPalRed was transferred to the VOSViewer format to visualize the results of a co-word analysis. In Figure [7](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig7), the cluster view is shown. We can observe how the different keywords are laid out over a horizontal line. This means that the keywords placed on the left are very dissimilar to those placed on the right side of the maps. The size of the keywords' labels is proportional to their frequency, VOSViewer visualizes only the labels of the most important ones (most frequent) in the higher zoomed view. VOSViewer selects a random different color for each cluster. Inside each cluster, the strength of a color at one point represents the density of this point. The density is measured using a Gaussian kernel function (van Eck & Waltman, [2010](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#bib75)).

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/5e984a09-40ae-46e1-b422-1a6a77771e93/mfig008.jpg)

Figure 7 Open in figure viewer PowerPoint VOSViewer's cluster view. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

Similarly to CiteSpace, the printed out map of VOSViewer does not show the power of its graphic user interface. In each view, the user can zoom in on a specific area to discover the items hidden under the most important ones. As an example, in Figure [8](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#fig8), an enlarged, zoom-in view of the cluster visualization focused on the keywords *FUZZY-TOPOLOGY* and *T-NORM* is shown.

![Details are in the caption following the image](https://onlinelibrary-wiley-com.sire.ub.edu/cms/asset/1e5ae5e2-2768-4f39-9a5b-10a582a1647d/mfig009.jpg)

Figure 8 Open in figure viewer PowerPoint VOSViewer's cluster zoom-in view. \[Color figure can be viewed in the online issue, which is available at wileyonlinelibrary.com.\]

## Lessons Learned

As has been shown in both the Comparative Study section and the Analysis of Generated Maps: A Cooperative Study among Tools section, each software tool has different characteristics. Several software tools have powerful preprocessing techniques, others allow the generation of a high quantity of bibliometric networks, and others are focused only on one kind of bibliometric network. Finally, not all the processes of analysis are available in each software tool. For this reason, a deep science mapping analysis requires the use of different tools.

The preprocessing capabilities of VantagePoint are one of its main strengths. It incorporates a high quantity of import filters that allows us to load data from almost all the bibliographical sources. Moreover, the clean-up list method and the possibility of applying a thesaurus to carry out this task, helps the preprocessing task, especially the de-duplicating process. Vantage-Point allows us to export the results into a csv file, so other software tools can read this data to perform their own science mapping analysis over the preprocessed data.

CoPalRed has a good de-duplicating process too, but it is focused only on one kind of unit, the keywords. NWB Tool and Sci <sup>2</sup> Tool have a de-duplicating module, but this needs an external process to be performed using external software. However, both NWB Tool and Sci <sup>2</sup> Tool have a good network reduction process.

The software tools allow us to generate various kinds of bibliometric networks, but as was shown in Table [4](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl4), there is no single software tool able to extract all of them.

Taking into account the maps and visualizations generated by each software tool, as shown in the Analysis of Generated Maps: A Cooperative Study among Tools section, there are several differences between them:
- CiteSpace is able to visualize the networks using different layouts. The name of the detected clusters can be assigned using different metrics. Finally, the user graphic-interface allows us to interact with the network to carry out a good exploration of it.
- CoPalRed groups the items (keywords) under themes, and they are categorized in a strategic diagram according to their centrality and density. This categorization allows us to detect the *motor themes* of the field. For each theme, CoPalRed generates a thematic network where the relation between its keywords is shown.
- IN-SPIRE allows us to visualize two kinds of map, if sufficient data are provided. In the Theme view, the analyst can detect the most important zones of the map (where more documents are localized). The Galaxy view allows us to easily detect similar documents based on their content.
- NWB Tool and Sci <sup>2</sup> Tool generate similar visualizations. They allow us to visualize the networks using different plugins and applying different layouts and scripts to customize the view. Sci <sup>2</sup> Tool incorporates thematic maps where the information is shown over a world map.
- VantagePoint has three kinds of map that allow several views to be created. In the map view, VantagePoint shows a legend that explains the size of the lines, being the only software that produces this legend. Maybe one strength of this software tool is the user graphic-interface that allows the user to select a set of items from the map, whereupon it shows the documents associated with these items and other information in the detail window.
- VOSViewer has a powerful user graphic-interface that allows us to examine the generated maps easily. Detecting (in a visual way) the most important themes is not always easy, and in the cluster view it is difficult to say to which cluster the keywords that are between two clusters (borderline keywords) belong.

According to the methods of analysis available there are differences between the software tools; for example, the geospatial analysis is available only in CiteSpace, Sci <sup>2</sup> Tool, and VantagePoint, and only the first two have geocoding capabilities that allow us to represent the network over a world map (using Google Maps or Yahoo! Maps).

In Table [7](https://onlinelibrary-wiley-com.sire.ub.edu/doi/10.1002/#tbl7), we show a short summary of their characteristics according to the four aspects considered in the analysis developed. As we can observe, the software tools CiteSpace, IN-SPIRE, NWB Tool, Sci <sup>2</sup> Tool, and VantagePoint could be identified as the more complete ones.

| Software tool | Preprocessing | Networks | Normalization | Analysis |
| --- | --- | --- | --- | --- |
| Bibexcel | Data and networks reduction | DBCA, ACAA, CCAA, ICAA, ACA, DCA, JCA, CWA, Others | Salton's Cosine, Jaccard's Index, or the Vladutz and Cook measures | Network |
| CiteSpace | Time slicing and data and networks reduction | DBCA, ACAA, CCAA, ICAA, ACA, DCA, JCA, CWA, Others | Salton's Cosine, Dice or Jaccard Strength | Burst detection, geospatial, network, temporal |
| CoPalRed | De-duplication, Time slicing, data reduction | CWA | Equivalence index | Network, temporal |
| IN-SPIRE | Data reduction | CWA | Conditional probability | Bust detection, network, temporal |
| Leydesdorff's Software |  | ABCA, JBCA, ACAA, CCAA, ICAA, ACA, CWA | Salton's Cosine |  |
| Network Workbench Tool | De-duplication, time slicing and data and networks reduction | DBCA, ACAA, DCA, CWA, DL | User defined | Burst detection, network, temporal |
| Science of Science Tool | De-duplication, time slicing and data and networks reduction | ABCA, DBCA, JBCA, ACAA, ACA, DCA, JCA, CWA, DL, Others | User defined | Burst detection, geospatial, network, temporal |
| VantagePoint | De-duplication, time slicing and data reduction | ACAA, CCAA, ICAA, ACA, DCA, JCA, CWA, Others | Pearson's r, Salton's Cosine or the Max Proportional | Burst detection, geospatial, network, temporal |
| VOSViewer |  |  | Association Strength | Network |

We should point out that NWB Tool and Sci <sup>2</sup> Tool have a great deal in common becasue they share algorithms and have several algorithms in common. NWB Tool is a network analysis, modelling, and visualization toolkit, whereas Sci <sup>2</sup> Tool is a modular toolset specifically designed to perform the study of science, but the Cyberinfrastructure for Network Science Center has developed them both and they share several algorithms and methods. Nevertheless, some capabilities such as geocoding are unique to Sci <sup>2</sup> Tool.

It is sometimes difficult to import a specific dataset into the nine described software tools. At other times, it is difficult to modify them or incorporate new measures, algorithms, and visualizations. For this reason, extension capabilities such as those provided by NWB Tool, Sci <sup>2</sup> Tool, and VantagePoint are very useful.

As mentioned above, each software tool has different characteristics and implements different techniques that are carried out with different algorithms. Consequently, each software tool gives its particular view of the studied field. The combined use of different science mapping software tools could allow us to develop a complete science mapping analysis. Therefore, we think that the cooperation among tools could generate a positive synergy that would give us the possibility of extracting unknown knowledge that would otherwise remain undiscovered.

## Concluding Remarks

An analysis of science mapping software tools has been carried out. Specifically, we have analyzed nine representative science mapping software tools: Bibexcel, CiteSpace II, CoPalRed, IN-SPIRE, Leydesdorff's Software, Network Workbench Tool, Sci <sup>2</sup> Tool, VantagePoint, and VOSViewer.

These software tools present different characteristics; for example, some of them are focused only on visualization and others have different preprocessing modules. There is not one software tool that we could consider the best one. Consequently, we think that a complete science mapping analysis of a particular field should be made using a variety of these software tools to gather all the important knowledge and different perspectives; for example, the preprocessing step is very important and the analyst has to use a software tool to help carry out this task. Not all the software tools are able to extract all the bibliometric networks, and, so, different tools have to be used to analyze a field from different perspectives (intellectual, social, or conceptual). The software tools have different analysis methods (although some of them are common), which allow the analyst to discover different knowledge. Finally, because the visualizations are different in each one, different views of the field can be generated and these help to interpret and analyze the results. This cooperation among tools gives a positive synergy, which allows us to extract the knowledge hidden behind the data.

Considering the results obtained in the Analysis of Generated Maps: A Cooperative Study among Tools section, where co-word was the unique analysis technique used to analyze the FST field, and the positive synergies of using several software tools drawn in the Lessons Learned section, we think that a thorough analysis of any field could be carried out using the powerful of each tool. So, for example, a co-word analysis performed by CoPalRed could be complemented by IN-SPIRE using the terms extracted from abstracts and titles. Moreover, IN-SPIRE could show the conceptual changes over time using its Time tools. In addition, CiteSpace and Sci <sup>2</sup> could perform an intellectual and social analysis. CiteSpace could be used for a document co-citation analysis and Sci <sup>2</sup> for a co-author analysis. The resulting network of authors could be displayed over a world map using the geolocation capabilities of Sci <sup>2</sup>. Finally, VantagePoint could be used to build a factor map on keywords, and show the institutional affiliation related to the most interesting detected factors.

We should point out that this study does not incorporate all of the science mapping software tools used around the world. This is because researchers usually use their own ad hoc software tools and algorithms, perhaps motivated by the lack of flexibility of available software tools. Although these could have similar characteristics to the ones presented here, they remain unpublished. Sometimes, these tools are unpublished becuase they were developed to perform a specific and ad hoc analysis and these developed pieces of software remained in the background.

## Acknowledgements

This work has been developed with the support of Project 90/07 (Ministry of Public Works and Transport) and Excellence Andalusian Project TIC5299. We thank the Pacific Northwest National Laboratory and Search Technology Inc. for providing us a trial version of IN-SPIRE and VantagePoint, respectively, and for their help and support.

## References

## Citing Literature

[Download PDF](https://onlinelibrary-wiley-com.sire.ub.edu/doi/pdf/10.1002/asi.21525)