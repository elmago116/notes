---
title: "Determining gender in academic authorship: a comprehensive and methodical approach"
source: "https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/Determining-gender-in-academic-authorship-a"
authors: "[[Boté-Vericad]],[[Juan-José]],[[Centelles]],[[Miquel]],[[Ferran-Ferrer]],[[Núria]]"
published: 2025-03-26
created: 2026-02-02
description: "Purpose. This study introduces an advanced method for ascertaining the gender identity of scientific authors of academic papers indexed in Web of Science"
tags:
  - "themes/gender"
DOI:
Type:
year:
---
[Skip to Main Content](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/#skipNav)

[Skip Nav Destination](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/#)

- [Previous Article](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/311/1246569/Exploring-trends-and-gaps-in-sustainable-e-library)
- [Next Article](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/367/1246536/Automated-data-management-practices-in-university)

Purpose

This study introduces an advanced method for ascertaining the gender identity of scientific authors of academic papers indexed in Web of Science or Scopus. This study aims to improve gender information retrieval, thereby benefiting gender-based bibliometric studies.

Design/methodology/approach

A sample of 187 authors was examined using two identification methods: manual examination and R scripts performing queries in different databases. Gender verification involved consulting databases such as Scopus, ORCID, Virtual International Authority File (VIAF), Wikidata and Gender-API.

Findings

Findings revealed that manual checks identified the gender of 50.8% of authors in Wikidata and 37.43% in VIAF, achieving high reliability but varying success across datasets. The R script identified 42.24% of authors in Wikidata and 31.01% in VIAF, underscoring the value of automated tools despite limitations. In addition, this study identifies and addresses biases in automated gender identification practices, which have contributed to the underrepresentation of women in bibliometric studies.

Originality/value

The study emphasizes the need for more accessible data, including linked open data, to refine author gender identification within the scientific domain. By highlighting and mitigating biases in automated methods, this dual-method approach not only enhances gender identification accuracy but also contributes to more equitable representation in academic bibliometric analyses.

An extensive body of research emphasizes the advantages of equity and diversity in enhancing academic and organizational excellence ([Dewidar *et al.*, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Encouraging equity and diversity in academia is an imperative objective. Identifying the gender of authors empowers institutions and publishers to proactively address potential disparities and biases in the representation of different genders and other intersectionalities within academic literature, thus fostering equal opportunities for all scholars.

Despite the recognized importance of gender equity, there is a lack of systematic methodologies for accurately identifying the gender of academic authors ([González-Salmón and Robinson-García, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). This gap hinders efforts to monitor and address gender disparities in scholarly publications. This study aims to develop and evaluate both manual and automatic processes for gender identification of authors in academic papers. By using multiple databases and tools, the research seeks to provide a robust methodology that can be integrated into bibliometric analyses. The findings will inform policy development, support institutions and publishers in promoting gender equity and contribute to the broader efforts of creating an inclusive academic environment.

This study highlights gender disparities in academic authorship using manual and automated methods. Libraries, digital databases like Scopus and Web of Science (WoS), serve important functions in curating and disseminating knowledge. The findings aim to improve author metadata management and promote gender equity in global research.

There are growing bodies of evidence demonstrating the benefits of equity, diversity and inclusion (EDI) on academic and organizational excellence ([Maes *et al.*, 2012](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Ensuring diversity and inclusivity in academia is a crucial goal. By identifying the gender of authors, institutions and publishers can monitor and address potential disparities and biases in the representation of different genders in academic literature. This promotes equal opportunities for all scholars. The importance of accurate gender identification is emphasized in the context of policy development in higher education. Accurate gender identification is essential for formulating and evaluating policies and initiatives aimed at addressing gender disparities in academia. It provides the necessary data to track progress and assess the impact of interventions ([Maes *et al.*, 2012](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Finally, ensuring that academic work accurately reflects the contributions of all authors is not only a fundamental ethical imperative but also a matter of integrity. Gender identification is one crucial aspect of acknowledging and respecting authorship. Visibility is the first step to inclusion ([Agapoff and Van Schalkwyk, 2023](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

The discussion surrounding gender equity in academia has led to a debate on whether journals should identify the gender of their authors. Proponents of this measure argue that such transparency could reveal existing disparities, prompting reforms to balance representation. They envisage a scholarly environment where individuals of all genders receive equal opportunities and recognition. Identifying gender could, for example, highlight biases in peer review processes, ensuring a fair evaluation of all research regardless of the author’s gender ([Llorens *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Conversely, critics raise concerns about privacy and the potential reinforcement of stereotypes. They worry that awareness of an author’s gender might inadvertently introduce bias, detracting from the merit-based assessment of their work. Studies on implicit bias support this concern, although research on blind hiring practices has shown mixed results, with gendered constructions sometimes reemerging to reintroduce discrimination in certain contexts ([Foley and Williamson, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Sugimoto *et al.*, 2019](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). In addition, the administrative burden of tracking and publishing gender data must be considered, particularly for journals with limited resources ([Budden *et al.*, 2008](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

Advocates suggest a compromise: voluntary gender self-reporting combined with robust anti-bias training for reviewers. This approach respects individual privacy while promoting transparency. At the same time, strengthening blind review processes could help mitigate unconscious bias. In this ongoing dialogue, the academic community must carefully weigh the benefits of gender identification against potential drawbacks, aiming for a future where scholarly contributions are valued solely for their intellectual merit. The academic community must consider the benefits of gender identification against potential drawbacks, aiming for a future where scholarly contributions are valued solely for their intellectual merit ([Llorens *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

In academia, identifying the gender of authors is essential for understanding and addressing gender disparities. Several methods are used for this purpose, each with distinct advantages and challenges. Manual inspection, involving human verification of names, is highly accurate but labor-intensive and this process does not fully resolve the issue. Gender name databases like Gender API ([VanHelene *et al.*, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)) and Genderize.io ([Sebo, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)) offer probabilistic gender identification based on names, providing scalable yet sometimes culturally limited accuracy. Advanced techniques use natural language processing (NLP) and machine learning models, delivering improved accuracy by analyzing contextual information, albeit requiring technical expertise. Cross-referencing social media profiles ([Robinson-Garcia *et al.*, 2020](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)), although effective, raises privacy concerns. Email address analysis and institutional records, including ORCID data, provide reliable but occasionally inaccessible data. Each method, from manual inspection to advanced computational techniques, serves different needs, balancing accuracy, scalability and ethical considerations. Combining these approaches can enhance reliability, offering a detailed understanding of gender representation in academic publishing.

Moreover, this study recognizes that biases in automated gender identification methods intensify the underrepresentation of women in academic bibliometric analyses. By employing a dual-method approach, this research aims to address these biases and propose a more inclusive methodology.

Recent research has brought to light the persistent gender disparities across various academic domains. Multiple studies have consistently shown the underrepresentation of women and non-binary individuals in general ([Lerchenmüller *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Son and Bell, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)), and this imbalance extends to specific fields, including health ([Burgwal *et al.*, 2019](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Patel *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Boté Vericad, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)), social sciences ([Trepte and Loths, 2020](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Casad *et al.*, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)) and STEM ([Carter *et al.*, 2019](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Casad *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Cimpian *et al.*, 2020](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

In science, and particularly in research fields related to gender studies, sociology, psychology and more, the gender identity of authors can be relevant to the research itself. Knowing the author’s gender may provide valuable context for interpreting and analyzing the research ([Ni *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). In addition, there is another area of concern, which pertains to the assessment of the impact of this research ([Fox and Paine, 2019](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Gender may impact the visibility and impact of academic work. Knowing the gender of authors can be essential for impact assessment, particularly in fields where gender may influence recognition and opportunities ([Kaatz *et al.*, 2014](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). The identification of the gender of authors plays a crucial role in the impact assessment of academic work. Knowing the gender of authors can provide valuable insights into potential biases and disparities in citation rates, funding opportunities and overall visibility within the academic community. By collecting and analyzing gender data, we can assess whether there are systematic differences in the reception and influence of research based on the author’s gender. This information is essential for developing targeted strategies to promote equity and inclusivity in academia. Journal editors, who often request demographic information, including gender, from authors during the submission process, are in a unique position to facilitate this comprehensive impact assessment. Their role is vital in ensuring that gender-related factors are considered, enabling a more nuanced understanding of the dynamics influencing academic impact. Moreover, in some cases, identifying the gender of authors adds transparency to research findings, particularly when addressing gender-specific issues or making claims related to gender ([Heidari *et al.*, 2016](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Recent studies in bibliometrics have shown that integrating multiple methods enhances data accuracy, particularly for assessing author demographics in academic research ([Boté-Vericad *et al.*, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Sugimoto *et al.*, 2019](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); West *et al.*, 2013). However, the accuracy of automated tools remains a concern. [Liu *et al.* (2024)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) found that tools like genderize.io often misclassify individuals, especially with culturally ambiguous names, suggesting a need for manual review in smaller, accuracy-sensitive studies.

While the underrepresentation of women and non-binary individuals in academic authorship is a critical issue, it is part of a larger pattern of gender disparities that permeate various aspects of academic life. These disparities have significant implications for career advancement, access to funding and overall professional development in academia.

The “leaky pipeline” phenomenon describes how women are disproportionately lost at each stage of the academic career ladder, from graduate school to tenured professorships ([Ceci *et al.*, 2014](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). This phenomenon is particularly pronounced in fields like STEM, where the representation of women decreases significantly at higher academic ranks ([Kaminski and Geisler, 2012](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

The reasons behind these disparities are varied. They include implicit biases in hiring and promotion processes, differences in networking opportunities and the impact of family responsibilities, which often disproportionately affect women ([Moss-Racusin *et al.*, 2012](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Moreover, women in academia frequently report experiencing a lack of mentorship and sponsorship compared to their male peers, further hindering their career progression ([Chisholm-Burns *et al.*, 2017](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Gender disparities in academia are closely linked to differences in career trajectories between men and women. Research consistently shows that women are less likely to be promoted to senior academic positions compared to their male counterparts, even when controlling for factors such as publication record and research impact ([Shen, 2013](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Monroe *et al.*, 2008](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Automated methods, often used to analyze demographic trends, can introduce additional challenges due to cultural biases in gender identification, as shown in studies by [Ikae and Savoy (2022)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) and [Karimi *et al.* (2016)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/). These limitations highlight the importance of detailed methodologies to address such biases effectively. Automated methods used in gender identification often perpetuate cultural and systemic biases, further marginalizing underrepresented groups such as women and non-binary individuals. This study directly addresses these challenges by employing a detailed, dual-method approach to improve accuracy and mitigate these biases.

These gender disparities in career advancement and funding opportunities contribute to the perpetuation of inequality in academia, affecting the individuals directly involved and the academic community and society at large. The underrepresentation of women and non-binary scholars in senior academic positions and their limited access to funding resources can result in a narrower range of research perspectives and topics being explored ([Avolio *et al.*, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Daitch *et al.*, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). This lack of diversity can hinder scientific progress and the development of more comprehensive and inclusive knowledge ([Hofstra *et al.*, 2020](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

Moreover, the systemic nature of these disparities emphasizes the importance of institutional policies and interventions aimed at promoting gender equity. Addressing these issues requires a comprehensive approach that includes revising hiring and promotion practices, providing targeted support for women and non-binary scholars and ensuring transparency and fairness in the allocation of research funding ([Nguyen *et al.*, 2023](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Schmaling and Gallo, 2023](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). By highlighting the broader implications of gender disparities, this research contributes to ongoing efforts to create a more equitable and inclusive academic environment. Open data initiatives, as suggested by [Piwowar *et al.* (2018)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), are vital to ensuring transparency and inclusivity in bibliometric analyses, which can inform targeted interventions to mitigate gender disparities

The data set of authorships used in this study originates from a prior bibliographic systematic review on the gender gap in Wikipedia ([Ferran-Ferrer *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Data for this review were sourced from Scopus and WoS ([Ferran-Ferrer *et al.*, 2023](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Ferran-Ferrer *et al.*, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Building on this foundation, our study employs a robust methodology to determine the gender identities of scientific authors.

In this section, we outline a structured approach for systematically organizing and executing procedures to accurately identify gender references in academic papers. The methodology is consistent, reliable and cost-effective, using linked open data, APIs and R scripts to access and analyze data sets. The R scripts, available for download, enable replication of the study ([Boté-Vericad, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Comprehensive data analysis was conducted using R, whereas Python was used for visualization and graphics generation.

Initially, ChatGPT was explored as a potential tool to assist in automating the retrieval of author data, including ORCID IDs, affiliations and Wikidata IDs. However, during preliminary testing, significant limitations were encountered. These included its inability to directly access the Wikidata API and issues with exhaustive searches, which frequently resulted in timeout errors. Due to these challenges, ChatGPT was ultimately not used in the final workflow.

It is crucial to emphasize that our methodology is conscientious in the sense that we recognize the importance of conducting gender identification in a sensitive and ethical manner, respecting individuals’ self-identified gender and their privacy rights. While the need for gender identification is evident, it must be balanced with careful consideration of privacy and data protection concerns. To ensure the reliability of our coding process, two independent researchers separately assessed and assigned gender labels to the 187 authors, obtaining a high level of agreement with a score of 0.848 in reliability Krippendorff’s alpha coefficient.

First, we initiated the process with a hands-on identification, following a methodology similar to previous studies ([Minguillón *et al.*, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)) for analyzing the gender of Wikipedia editors. Following this method, we implemented a manual systematic procedure guided by a set of straightforward steps. First, when users explicitly disclosed their gender information in their institutional web pages (i.e. universities, research centers), we used this provided data to categorize their gender. Leveraging the grammatical gender inherent in some languages, such Spanish, we used expressions such as “soy abogada” (“I’m a \[woman\] lawyer”) to identify the author as a woman. Furthermore, we also attempted to infer the user’s gender from their real name, as many grammatical gender languages’ names inherently imply a specific gender and can be readily classified as male or female. However, in cases where names were ambiguous and could be associated with both genders, we refrained from applying this rule, prioritizing accuracy over assumption. Ultimately, when none of the aforementioned methods yielded a definitive gender determination, we categorized the user as “unknown” for the sake of clarity. It is worth noting that our manual identification process specifically included a category for non-binary authors. In cases where explicit non-binary identities were disclosed, such as through pronouns or self-identification on institutional web pages, we categorized them accordingly. However, this method was limited in identifying non-binary individuals when such information was not explicitly available.

The automatic methodology, as shown in [Figure 1](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), is deployed over a series of scripts, each dedicated to querying a particular data source or processing the data to prepare for subsequent queries. Our process is divided into four primary stages, each designed to contribute to the study’s overall robustness and comprehensiveness: data cleaning and author separation; name and surname retrieval, normalizing the names of authorships and data extraction with Scopus, include the diversity of different names for a given individual, extraction of the gender identity using several sources of information:

Figure 1.

The automatic process of obtaining the gender (or gender/sex in the case of wikidata) from academic paper authors

- Data cleaning and author separation: The first step of our method involved an in-depth cleaning of the entire dataset to ensure its integrity and reliability. Subsequent to this, we separated the individual authors from the collective dataset. This preparatory step was essential for creating a cleaned and organized list of authors, thereby laying the groundwork for the subsequent phases of gender identification. It also implies removing duplicates and normalizing the list. We have also normalized authors who had different names in different publications in our dataset ([Boté-Vericad *et al.*, 2022](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).
- Name and surname retrieval: With a cleaned dataset in hand, the next step involved the extraction of the first names and surnames of all the authors. This phase was pivotal for gathering the basic identifiers that would be used in later stages for the purpose of gender identification.
- In addition to normalizing the names of the authors, we create a spreadsheet with at least 3 columns: given name, last name, Scopus ID.

#### 3.2.1 Extracting identifiers and names: Scopus and ORCID.

The initial script queries the Elsevier API to extract ORCID IDs and name variants for authors using Scopus Author IDs. In parallel, an additional script harnesses the ORCID API to fetch name variants associated with the ORCID IDs.

Scopus on download bibliographic records provide the author ID in Scopus. This is very helpful in the process to automatize the data extraction. WoS does not yet provide the Author ID at the moment of writing this paper. We performed a search in Scopus using the Scopus API and using as a main parameter, the Author ID provided by Scopus in the bibliography record. Once the author was found, we extracted the ORCID ID of the author when available. We added a new column to the spreadsheet with the ORCID ID.

ORCID API: Having the credentials for the ORCID API, we performed different queries in ORCID, a globally recognized academic database, using the SCOPUS ID, the ORCID ID and all possible names of the author obtained from the ORCID API. The goal was to locate possible name variants for each author, thereby enhancing the reliability of our identification process. Where ORCID identifiers were not initially available, we endeavored to obtain them, adding an additional layer of verification to our methodology.

#### 3.2.2 Gender identification through multiple databases: Wikidata API, Virtual International Authority File and Gender-API.

Concluding the process, we used different databases to extract the gender of the authors. We used the API of Wikidata in the automatic process, using its provision of unique IDs for authors and its inclusion of gender/sex data. Similarly, Virtual International Authority File (VIAF) provides gender information, though its representation may vary depending on the contributing institutions and regional norms. These data sets enable both gender-specific and broader demographic analyses, which are foundational to this study. The script employs a dual strategy of ORCID-based and name-based querying to maximize data retrieval. In addition, name variants are formatted and consolidated to aid the querying process. In addition, the Wikidata Query Service (WDQS) allows complex, real-time data retrieval from Wikidata’s extensive database using SPARQL, with visualization options, subject to performance-maintaining limitations linked to the current backend solution.

We also used the VIAF for identifying the authors’ gender. VIAF has some limitations on searching gender authors automatically as one author may have more than one identifier. This script focuses on fetching gender information from VIAF, leveraging both existing VIAF IDs and name variants for querying. The script processes rows with non-empty and empty VIAF IDs separately, ensuring exhaustive querying and data retrieval.

Each script meticulously handles data, ensuring the accuracy and integrity of the retrieved information. The scripts are designed to be modular and extendable, enabling the incorporation of additional data sources or querying strategies as needed.

A final step has been performed through an automatic search process in the Gender-API service. Gender-API is a premium web service powered by artificial intelligence designed to ascertain the gender associated with a given first name. It achieves this by analyzing a vast amount of data to determine whether a name is more likely to be used by males or females. The API returns the gender as “male”, “female” or “unknown”, along with a percentage accuracy score indicating the level of certainty regarding the gender determination.

By adopting this methodical sequence of steps, we were able to significantly augment the depth and breadth of our gender identity detection, thus enhancing the robustness and reliability of our study.

#### 3.2.3 Data processing.

In each stage, rigorous data processing steps are used to prepare data for subsequent queries. Name formatting, merging and the removal of duplicates are meticulously performed to ensure the accuracy of queries and the integrity of the enriched data set. The enriched data set is exported to a new Excel file after each stage of enrichment, ensuring the preservation of data and facilitating potential audits of the enrichment process.

The following is a detailed description of the methodology, which is divided into two primary stages: author identification and gender classification.

1. Stage 1: Author identification:
	- List of authors: The process begins with a normalized and unified list of authors. This list is the foundational dataset for the subsequent steps.
	- Scopus: The authors are first queried in Scopus to retrieve their Scopus Author IDs. Additional names associated with these IDs in Scopus are also gathered.
		- – Output: Scopus Author ID and other names in Scopus.
	- ORCID: The data from Scopus is then queried in ORCID to find corresponding ORCID IDs and any other names associated with these IDs.
		- – Output: ORCID IDs and other names in ORCID.
	- Wikidata: The ORCID data, along with all associated names, is queried in Wikidata. This step retrieves Wikidata IDs, gender information and VIAF IDs if available.
		- – Output: Wikidata ID, gender and VIAF ID.
	- VIAF: Using the Wikidata and ORCID information, the data set is then queried in VIAF to obtain VIAF IDs and any additional names associated with the authors.
		- – Output: VIAF ID and all associated names.
2. Stage 2: Gender classification:
	- Gender API: Finally, the authors' given names are processed through a Gender API to determine the probabilistic gender.
		- – Output: Probabilistic gender based on given names.

Throughout these stages, meticulous data processing ensures that the names are formatted consistently, merged correctly and duplicates are removed. This rigorous approach guarantees that the data set is accurate and reliable. Each stage of enrichment results in the creation of a new Excel file, which not only preserves the data but also allows for easy auditing and verification of the enrichment process.

This is a comprehensive overview of the methodology used for author identification and gender classification using Wikidata. The description follows the sequence of operations and elaborates on the rationale behind each step. The methodology is divided into two primary stages: author identification and gender classification.

Our approach integrates multiple databases to improve the accuracy of gender identification, but it is essential to recognize the inherent limitations and biases in each source. Wikidata, though widely used, includes gender/sex data curated by volunteers, often concentrated in North America and Europe, leading to regional biases and the underrepresentation of authors from other areas ([Piscopo and Simperl, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Similarly, VIAF aggregates global authority data but reflects the norms of contributing institutions, which vary by country, and its reliance on institutional records can exclude independent researchers or those from underrepresented regions ([Leuner, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Gender-API, an AI-based service, offers gender inference from names but struggles with culturally diverse or gender-neutral names, often misclassifying individuals from less represented cultures ([Santamaría and Mihaljević, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Keyes, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). These limitations highlight the importance of designing methodologies that account for diverse gender identities and cultural contexts.

Manual gender identification involves interpreting names, pronouns or contextual clues, making it subjective and prone to biases, particularly with unfamiliar or culturally specific names ([Larivière *et al.*, 2013](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Researchers may apply stereotypes or make errors, leading to misclassification and compromising data reliability. This method is labor-intensive and impractical for large data sets, requiring significant time and resources ([Mihaljević-Brandt *et al.*, 2016](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). In addition, manual methods struggle with accurately classifying non-binary identities, reinforcing binary frameworks if these identities are not explicitly considered in the research design ([Keyes, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

This study adopts a nuanced approach to gender classification by incorporating a “non-binary” category for non-cisgender identities, addressing gaps in traditional binary frameworks ([Keyes, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Santamaría and Mihaljević, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Manual identification relied on explicit self-identification through pronouns, institutional web pages or other direct references. Non-binary identities were included only when clearly expressed. Automated methods, such as those using Gender-API, VIAF and Wikidata, were limited by binary classification systems, failing to identify non-binary authors unless explicitly recorded ([Binns, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/); [Boté-Vericad *et al.*, 2024](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

This approach ensures some inclusivity but highlights significant limitations. Manual processes depend on explicit disclosure, potentially excluding individuals whose identities are not overtly expressed. Automated tools perpetuate binary assumptions, marginalizing underrepresented groups and reinforcing systemic biases ([Santamaría and Mihaljević, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). These challenges emphasize the urgent need for inclusive algorithms and metadata standards to represent diverse identities effectively. Incorporating a “non-binary” category represents a step toward equitable gender analysis. It enhances data accuracy and fosters inclusivity, bridging critical gaps in bibliometric tools. Expanding gender identification methods aligns with diversity and innovation principles, fostering equity in academia and driving societal progress ([Hofstra *et al.*, 2020](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Future efforts must focus on improving algorithms and metadata to support non-binary representation, ensuring fair and representative bibliometric systems.

Our results show that since the manual intervention is accurate (50.8% in Wikidata and 37.43% in VIAF), we obtain similar results with our scripts (42.24% in Wikidata and 31.01% in VIAF). It is necessary to consider that we performed in Wikidata and VIAF by dual search. This is what we search in Wikidata by the ORCID and the combination names. We also search in VIAF by a combination of VIAF ID and the combination of different names. The percentages reported in this section represent the proportion of authors successfully identified using each method (manual or automated) relative to the total sample size (187 authors). These figures differ from metrics reported in the abstract, which summarize overall success rates across data sets. Manual detection identified 50.8% of authors in Wikidata and 37.43% in VIAF, whereas automated detection identified 42.24% in Wikidata and 31.01% in VIAF.

[Table 1](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) provides a detailed breakdown of gender identification success rates using manual and automated methods across Wikidata, VIAF and Gender-API. Manual identification consistently outperformed automated methods in both databases, with a success rate of 50.8% in Wikidata and 37.43% in VIAF. This highlights the ability of manual methods to account for cultural and linguistic nuances that automated systems often miss. While manual identification included a non-binary category, its applicability was limited by the availability of explicit self-identification. Automated methods (e.g. Gender-API) were unable to classify non-binary identities due to their reliance on binary frameworks, underscoring the need for more inclusive tools in future research. Similar observations were noted by [Ikae and Savoy (2022)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), who found that while automated classification on platforms like Twitter is feasible, it often struggles with accuracy due to cultural and linguistic diversity.

Table 1.

Results obtained by different methods of gender identification

<table><thead align="bottom"><tr><th rowspan="2">Source</th><th rowspan="2">Gender</th><th colspan="2">Achievement of Identification (187 authors)</th></tr><tr><th>Manual intervention</th><th>Automatic intervention</th></tr></thead><tbody><tr><td rowspan="4">Wikidata API</td><td>Female</td><td>47</td><td>32</td></tr><tr><td>Male</td><td>47</td><td>28</td></tr><tr><td>Non-binary</td><td>1</td><td>1</td></tr><tr><td>Gender non-specified</td><td>0</td><td>18</td></tr><tr><td>Total</td><td></td><td>95 (50.8%)</td><td>79 (42.25%)</td></tr><tr><td rowspan="3">VIAF</td><td>Female</td><td>37</td><td>20</td></tr><tr><td>Male</td><td>33</td><td>24</td></tr><tr><td>Gender non-specified</td><td>0</td><td>14</td></tr><tr><td>Total</td><td></td><td>70 (37.43%)</td><td>58 (31.01%)</td></tr><tr><td rowspan="3">Gender-API</td><td>Female</td><td>–</td><td>24</td></tr><tr><td>Male</td><td>–</td><td>26</td></tr><tr><td>Gender non-specified</td><td>–</td><td>0</td></tr><tr><td>Total</td><td></td><td>–</td><td>50 (26.73%)</td></tr><tr><td rowspan="2">Manual identification</td><td>Female</td><td>12</td><td>–</td></tr><tr><td>Male</td><td>10</td><td>–</td></tr><tr><td>Total</td><td></td><td>22 (11.76%)</td><td>–</td></tr><tr><td>Total</td><td></td><td>187</td><td>187</td></tr></tbody></table>

**Source(s):** Authors’ own work

[View large](https://www-emerald-com.sire.ub.edu/view-large/91149860)

[Figure 2](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) provides a comparative analysis of the effectiveness of manual versus automated gender identification methods across three different databases: Wikidata, VIAF and Gender-API. Each bar represents the percentage of successful gender identifications relative to the total number of authors analyzed (187), allowing for a clear visualization of the performance of each method. In the Wikidata category, manual identification achieved a success rate of approximately 50.8%, whereas the automated process was slightly lower at 42.25%. This discrepancy suggests that while automated methods are effective, they may miss certain nuances that manual identification captures, particularly in ambiguous or culturally specific cases.

Figure 2.

Comparison of manual vs automated gender identification success rates across databases

For the VIAF database, the success rate was again higher for manual identification, with 37.43% compared to 31.01% for automated methods. This indicates that the manual approach might be more adept at navigating the complexities of VIAF’s data, such as handling different name formats or integrating information from various sources. In the Gender-API category, only the automated method is represented, with a success rate of 26.73%. This is because Gender-API relies entirely on an automated process to infer gender from names, and no manual comparison was performed. The lower success rate here compared to the other databases may reflect the limitations of this API, particularly its reliance on name-based inferences without additional contextual data. This limitation aligns with findings by [Karimi *et al.* (2016)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), who noted biases in name-based gender inference tools, especially in regions where certain names cross gender boundaries. They observed that image-based gender recognition could enhance accuracy by capturing non-linguistic cues, an approach not viable in our text-based data set but potentially valuable for future research. Our findings align with [Liu *et al.* (2024)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), who observed that genderize.io misclassified a notable portion of individuals, especially in cases involving culturally ambiguous names. This comparison further underscores the limitations of automated-only approaches, reinforcing the value of our dual-method approach for more nuanced and accurate gender identification.

Looking deeper in the automatic processes, the results ([Table 2](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)) showed that Wikidata revealed 32 females (17.1%) and 28 males (14.9%) identified through ORCID database and textual searches, with non-binary and unspecified genders accounting for the remainder. VIAF data showed a higher identification via VIAF ID for females (10.1%) and for males (12.8%). Gender-API reported a near even split with females at 48.4% and males at 51.1%. Particularly, the majority of individuals (139 out of 187) had a gender identification accuracy greater than 90%, with no “unknown” classifications encountered.

Table 2.

Results of the automatic process in detail

| Gender | ORCID found   in Wikidata | Textual search found in Wikidata   (non-duplicates from ORCID) | Total |
| --- | --- | --- | --- |
| Females | 13 | 19 | 32 |
| Males | 16 | 12 | 28 |
| Non-binary | 0 | 1 | 1 |
| Gender non-specified | 9 | 9 | 18 |
| Total | 38 | 41 | 79 (42.25%) |
|  | VIAF search by VIAF ID | Textual search found in VIAF | Total |
| Females | 16 | 4 | 20 |
| Males | 8 | 16 | 24 |
| Gender non-specified | 0 | 14 | 14 |
| Total | 24 | 33 | 58 (31.01%) |
|  |  | Textual search in Gender-API | Total |
| Females |  | 91 | 91 (48.4%) |
| Males |  | 96 | 96 (51.1%) |
| Total |  |  | 187 (100%) |

**Source(s):** Authors’ own work

[View large](https://www-emerald-com.sire.ub.edu/view-large/91149865)

In [Figure 3](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), the graph compares how manual and automated methods identify gender across Wikidata, VIAF and Gender-API. For Wikidata, manual identification found 47 males and 47 females, with one non-binary author and no gender-unspecified cases. Automated methods identified fewer individuals (32 females, 28 males) and classified 18 as gender-unspecified. For VIAF, manual methods identified 37 females and 33 males with no non-binary cases. Automated processes identified fewer authors (20 females, 24 males) and classified 14 as gender-unspecified. For Gender-API, automated methods found 24 females and 26 males with no non-binary or gender-unspecified cases due to the system’s binary classification approach. Manual methods handle non-binary classifications better but are resource-intensive. Automated systems are efficient but struggle with ambiguous cases and tend to classify more individuals as gender-unspecified. Gender-API enforces binary classifications, potentially misclassifying non-binary identities.

Figure 3.

A breakdown by gender across databases

Preliminary tests, as shown in [Figure 4](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), were conducted using ChatGPT Premium to explore its potential for automating gender identification tasks. While it successfully retrieved ORCID IDs in isolated cases, its browsing-based system proved limited in obtaining Wikidata IDs and gender information. The process was largely manual, requiring one-by-one queries, and ChatGPT struggled to handle bulk data efficiently. For instance, as shown in [Figure 2](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/), the first query (e.g. Andreas Kaltenbrunner) worked correctly, but subsequent attempts with a list of names resulted in incomplete tasks and errors. These limitations highlight significant challenges in using ChatGPT for large-scale gender identification.

Figure 4.

Test for gender identification using ChatGPT premium

Discrepancies between manual and automated gender identification arise due to cultural context and broader data sources. Manual methods can accurately classify names with regional gender variations, whereas tools like Gender-API rely on statistical correlations ([Santamaría and Mihaljević, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Automated systems also lack access to institutional websites, leading to data gaps ([Keyes, 2018](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). In addition, automated tools struggle with non-binary identities due to binary frameworks, often misclassifying or omitting them. Enhancing algorithms with diverse data and nuanced gender classifications can improve accuracy and reduce reliance on manual methods.

Integrating a dual-method approach, combining manual and automated gender identification, into bibliometric tools like Scopus and WoS can enhance the accuracy and inclusivity of gender data. Automated methods efficiently process large data sets, providing initial classifications, whereas manual verification addresses discrepancies, particularly with culturally specific or ambiguous names ([Mihaljević-Brandt *et al.*, 2016](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). This hybrid approach ensures broader and more accurate gender representation, mitigating issues where automated systems may misclassify or leave some identities unspecified ([Cruz-Castro and Sanz-Menendez, 2021](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)).

By incorporating non-binary and gender-nonconforming identities, this dual-method approach enhances gender analysis; ensuring diverse identities are reflected in databases. Automated tools handle most classifications, with manual checks for complex cases, optimizing accuracy and efficiency. Academic institutions and publishers can adopt this method to assess gender representation and address disparities. Policymakers and funding agencies can use the improved data for targeted gender equity initiatives, such as monitoring the impact of policies on research funding. Ultimately, this approach promotes reliable gender data, supports gender-related research and fosters equity in academic publishing and policy-making.

The dual-method approach combining manual and automated processes aligns with trends in bibliometric studies, as evidenced by [West *et al.* (2013)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) and [Sugimoto *et al.* (2019)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/). These studies underscore the limitations of relying exclusively on automated data retrieval, especially when examining nuanced variables like author gender in large bibliometric data sets. By applying a similar mixed-method approach, our study broadens the potential for more accurate gender classification, addressing some of the constraints noted in automated-only systems. While anti-bias training for reviewers could mitigate the discriminatory effects of gender explicitness in peer review, the decentralized nature of this process limits enforceability and uniform implementation. As a result, institutions and publishers must adopt complementary strategies, such as strengthening blind review processes, promoting gender equity policies and leveraging bibliometric tools to ensure fair representation without adding unnecessary burden on authors.

Furthermore, [Piwowar *et al.* (2018)](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/) emphasized the importance of accessible and standardized open data for gender and bibliometric studies, noting that data limitations often hinder comprehensive gender analyses. This supports our finding that integrating open-access and linked open data could significantly improve both manual and automated gender identification processes by providing a more diverse and representative data set for bibliometric analyses.

A limitation of this study is the time-intensive nature of the process, as it requires reviewing multiple webpages. Not all authors include pronouns, which complicates gender identification. In addition, languages that do not grammatically distinguish gender, such as English, pose further challenges. These manual limitations necessitate thorough and ongoing checks to ensure accuracy in determining the gender from bibliographic files. Consequently, the results may be less reliable for certain data sets, especially those involving authors from diverse linguistic backgrounds.

One of the critical limitations of Wikidata is that the property “gender” (P21) is labeled as “sex or gender” and includes seven values that mix gender identity, sex and even information about sexual orientation. Another limitation is that in Wikidata, not all scientific authors are registered, and not all have the same data in their records. For example, they may not have declared gender or other IDs such as the Scopus ID or VIAF ID. Another important issue which is at the same time an advantage is that the Wikidata records can be manually edited which can produce an enrichment of the records on adding data to the author records, data missing on removing or changing data by any cause. However, majorly they have ORCID in their records, a unique Wikidata ID which facilitates performing queries with the API.

When a researcher is not found by an identifier such as ORCID, performing search by names is challenging because scientific names are not normalized, and, as we make the effort of collecting all possible names in Scopus and in ORCID, is possible to have not retrieved a small part of them.

In the context of Wikidata, it is essential to consider that, apart from inputting the value for gender identity, it is imperative to provide a secondary source of information explicitly verifying the gender identity in question. This practice ensures the ethical utilization of what can be deemed sensitive information in subsequent contexts. It is worth noting that in certain countries, self-identifying with specific genders can potentially lead to complications. Nevertheless, it is important to acknowledge that Wikidata, whereas a valuable resource is not without limitations from a gender perspective.

In addition, the WDQS imposes constraints on query duration, result volume, memory consumption and query frequency to guarantee stability and equitable resource allocation amongst users. All these limitations have already been identified by the administrators of the SPARQL-based search system, and are in the process of being solved through a participatory process. This process will end with selection and implementation of a new, promising, WDQS backend.

There are three main limitations in VIAF. First, it is not possible to search by ORCID that would be beneficial for any user which is interested in an author. Second, one author may have different VIAF IDS. This is because of a variety of reasons in the researcher life-cycle. Different publishers might generate new records without considering that the author exists. Also because during their researchers, life cycle researchers use different names, for example, women who are married and change their surname to adopt their husband’s surname. It also can happen that researchers do not use the same normalized name in all their publications. Besides, VIAF does not perform strict control of author identifications. The result is that in many cases, the same person can have more than one identifier. This can be corrected if there is a deeper exploration into interoperability with other identification systems. Finally, redundancies arose in our search within VIAF, owing to the use of a comprehensive sample. We identified a discrepancy wherein a researcher was listed as male in VIAF but as non-binary in Wikidata.

Since obtaining the ORCID ID of the authors, different affiliations and other possible names used in scientific papers, ChatGPT has limitations on obtaining the Wikidata ID of the authors because it does use the Wikidata API. It does use through exhaustive searchers which cause in most cases timeout requests in the same prompt of ChatGPT.

The method outlined in this study provides a systematic framework for identifying the gender of authors, primarily within the scientific domain. However, to strengthen future research, it is crucial to expand these methodologies to encompass authors from other fields, such as the humanities, social sciences, journalism and medicine. These fields may necessitate distinct identifiers or alternative data sources to accurately determine gender, given the different professional contexts. Enhancing automated gender identification across various disciplines is an essential next step.

The preeminent technique for discerning the gender of academic authors resides in the automated process facilitated by the Wikidata API, which attains a 42% identification rate. This level of attainment remains unmodifiable due to the sporadic availability of ORCID identification on Wikidata and the inconsistent declaration of gender property (P21) in Wikidata. A further complicating factor, as stated previously, is the ongoing debate and consensus-seeking within the community of volunteers on the labeling of the property (P21), erroneously conflating the terms “sex” and “gender” as interchangeable.

Envisioning the potential of Wikidata as a central hub for identifiers from diverse databases, linked open data and Wikidata ontologies, it could serve as a pivotal platform for gender identification and scientific authorship in general. To surmount the current limitations of Wikidata, several initiatives are underway to standardize the description of entity categories, prescribing obligatory properties for each instance. Notably, Entity Schemas, a prominent initiative, offer guidance for editing specific entity categories, specifying the types, properties and values to be assigned. Expansion of this initiative to encompass researchers, including identification systems as mandatory properties, is a viable enhancement.

In addition, a significant avenue for enhancing the efficiency of the automated process revolves around encouraging authors to enhance their profiles in Scopus by linking their ORCID with their respective profiles. This practice also holds relevance within the WoS ecosystem. It is noteworthy, however, that to the best of our knowledge, WoS does not currently provide a Researcher WoS ID when downloading bibliographic records. Authors with profiles in Wikidata can contribute to this improvement initiative by ensuring the accuracy of the data contained within their profiles. During testing, we identified cases where authors had incorrectly linked their ORCID identifiers, highlighting the importance of accurate data integration. Improving the accuracy of ORCID profiles and encouraging researchers to maintain up-to-date links to databases like Scopus and WoS are crucial for enhancing gender identification accuracy. Collaborative efforts, such as those led by VIAF to maintain authority catalogues in libraries and ORCID’s focus on the research community, are essential. Future research could explore strategies to incentivize these practices, ensuring that researchers regularly update their profiles, thereby improving the overall reliability of gender identification processes.

Notwithstanding, the methodology presented herein embodies a comprehensive and pragmatic approach to data enrichment for gender identification, exemplifying the effectiveness of an integrated approach that harnesses multiple authoritative data sources. Through scrupulous open data handling and robust querying strategies, this methodology substantially enhances the data set’s utility for gender-based bibliometric analysis, thereby establishing a robust foundation for subsequent analytical endeavors. By identifying and addressing biases in automated gender identification practices, this study contributes to reducing systemic inequities and promoting more accurate and inclusive bibliometric analyses in academia.

Another critical consideration is the potential impact of stereotype threat on authors, particularly those from underrepresented or marginalized genders. If authors are required to specify their gender before submission, this could introduce a cognitive burden, potentially affecting performance and perpetuating existing disparities ([Steele and Aronson, 1995](https://www-emerald-com.sire.ub.edu/dlp/article/41/2/346/1246541/)). Future research should explore ways to integrate gender data collection without inadvertently contributing to such negative outcomes, perhaps through voluntary and anonymized reporting systems.

The dual-method approach outlined in this study provides a scalable model for enhancing gender identification accuracy in bibliometric databases, supporting more reliable gender-based analyses. Improved data, particularly through the inclusion of non-binary classifications, enables a clearer picture of gender diversity across disciplines, which can guide equity initiatives, especially in fields with significant disparities like STEM. Databases such as Wikidata hold potential as central resources for linking author data across platforms, especially if terms like “sex” and “gender” are clarified and standardized. Such advancements in data accuracy not only benefit research but also contribute to a fairer academic environment by fostering inclusivity and supporting equitable practices in hiring, funding and promotion.

The proposed gender identification methods primarily aim to enhance bibliometric analyses and information retrieval processes by improving metadata accuracy and inclusivity. Although these methods are not directly tied to the peer review process, they hold the potential to inform broader discussions on equity in academia. By ensuring transparent and ethical practices in gender identification, this approach contributes to the integrity of both metadata storage systems and scholarly evaluation frameworks, promoting fairness and inclusivity in academic publishing.

Future studies could integrate additional data sources into Wikidata, like national and institutional databases, and develop sophisticated algorithms that better handle gender nuances, especially for non-binary individuals. Clarifying the distinction between “sex” and “gender” in Wikidata is also important. Standardizing these terms will improve gender data accuracy, aiding in monitoring disparities in publishing and career advancement, especially in STEM. Accurate gender data supports the development of institutional policies that promote fair resource allocation, fostering an inclusive academic environment. This contributes to broader efforts toward gender equity in academia, ensuring diversity and fairness for all researchers.

This work was supported by the Spanish Ministerio de Innovación, Ciencia y Universidades, project Women and Wikipedia \[grant ref. PID2020-116936RA-I00\].

Agapoff

,

J.A.

and

Van Schalkwyk

,

G.I.

(

2023

), “”,

Medical Education Online

, Vol.

28

No.

1

, p.

2169921

, doi:

[https://doi-org.sire.ub.edu/10.1080/10872981.2023.2169921](https://doi-org.sire.ub.edu/10.1080/10872981.2023.2169921)

.

Binns

,

R.

(

2018

), “”,

Proceedings of Machine Learning Research, 81. Conference on Fairness, Accountability and Transparency

, pp.

1

\-

11

,

available at: [https://proceedings.mlr.press/v81/binns18a/binns18a.pdf](https://proceedings.mlr.press/v81/binns18a/binns18a.pdf)

Boté Vericad

,

J.-J.

(

2022

), “”, \[Doctoral Dissertation\].

Stiftung Universität Hildesheim

, doi:

[https://doi-org.sire.ub.edu/10.25528/141](https://doi-org.sire.ub.edu/10.25528/141)

.

Boté-Vericad

,

J.-J.

(

2024

), “”, doi:

[https://doi-org.sire.ub.edu/10.5281/zenodo.13685921](https://doi-org.sire.ub.edu/10.5281/zenodo.13685921)

.

Boté-Vericad

,

J.-J.

,

Adilović

,

E.

and

Afonso-Mendonça

,

H.-S.

(

2024

), “”,

Documentación de Las Ciencias de la Información

, Vol.

47

, pp.

5

\-

13

, doi:

[https://doi-org.sire.ub.edu/10.5209/dcin.90547](https://doi-org.sire.ub.edu/10.5209/dcin.90547)

.

Budden

,

A.E.

,

Tregenza

,

T.

,

Aarssen

,

L.W.

,

Koricheva

,

J.

,

Leimu

,

R.

and

Lortie

,

C.J.

(

2008

), “”,

Trends in Ecology and Evolution

, Vol.

23

No.

1

, pp.

4

\-

6

, doi:

[https://doi-org.sire.ub.edu/10.1016/j.tree.2007.07.008](https://doi-org.sire.ub.edu/10.1016/j.tree.2007.07.008)

.

Burgwal

,

A.

,

Gvianishvili

,

N.

,

Hård

,

V.

,

Kata

,

J.

,

García Nieto

,

I.

,

Orre

,

C.

,

Smiley

,

A.

,

Vidić

,

J.

and

Motmans

,

J.

(

2019

), “”,

International Journal of Transgenderism

, Vol.

20

Nos

2/3

, pp.

218

\-

229

, doi:

[https://doi-org.sire.ub.edu/10.1080/15532739.2019.1629370](https://doi-org.sire.ub.edu/10.1080/15532739.2019.1629370)

.

Carter

,

D.F.

,

Razo Dueñas

,

J.E.

and

Mendoza

,

R.

(

2019

), “”, in

Paulsen

,

M.B.

and

Perna

,

L.W.

(Eds),

Higher Education: Handbook of Theory and Research

,

Springer International Publishing

,

Cham

, Vol.

34

, pp.

39

\-

97

, doi:

[https://doi-org.sire.ub.edu/10.1007/978-3-030-03457-3\_2](https://doi-org.sire.ub.edu/10.1007/978-3-030-03457-3_2)

.

Casad

,

B.J.

,

Franks

,

J.E.

,

Garasky

,

C.E.

,

Kittleman

,

M.M.

,

Roesler

,

A.C.

,

Hall

,

D.Y.

and

Petzel

,

Z.W.

(

2021

), “”,

Journal of Neuroscience Research

, Vol.

99

No.

1

, pp.

13

\-

23

, doi:

[https://doi-org.sire.ub.edu/10.1002/jnr.24631](https://doi-org.sire.ub.edu/10.1002/jnr.24631)

.

Ceci

,

S.J.

,

Ginther

,

D.K.

,

Kahn

,

S.

and

Williams

,

W.M.

(

2014

), “”,

Psychological Science in the Public Interest

,

SAGE Publications

, Vol.

15

No.

3

, pp.

75

\-

141

, doi:

[https://doi-org.sire.ub.edu/10.1177/1529100614541236](https://doi-org.sire.ub.edu/10.1177/1529100614541236)

.

Chisholm-Burns

,

M.A.

,

Spivey

,

C.A.

,

Hagemann

,

T.

and

Josephson

,

M.A.

(

2017

), “”,

American Journal of Health-System Pharmacy

, Vol.

74

No.

5

, pp.

312

\-

324

, doi:

[https://doi-org.sire.ub.edu/10.2146/ajhp160930](https://doi-org.sire.ub.edu/10.2146/ajhp160930)

.

Cimpian

,

J.R.

,

Kim

,

T.H.

and

McDermott

,

Z.T.

(

2020

), “”,

Science

, Vol.

368

No.

6497

, pp.

1317

\-

1319

, doi:

[https://doi-org.sire.ub.edu/10.1126/science.aba7377](https://doi-org.sire.ub.edu/10.1126/science.aba7377)

.

Cruz-Castro

,

L.

and

Sanz-Menendez

,

L.

(

2021

), “”,

Journal of Informetrics

, Vol.

15

No.

3

, p.

101196

, doi:

[https://doi-org.sire.ub.edu/10.1016/j.joi.2021.101196](https://doi-org.sire.ub.edu/10.1016/j.joi.2021.101196)

.

Daitch

,

V.

,

Turjeman

,

A.

,

Poran

,

I.

,

Tau

,

N.

,

Ayalon-Dangur

,

I.

,

Nashashibi

,

J.

,

Yahav

,

D.

,

Paul

,

M.

and

Leibovic

,

L.

(

2022

), “”,

Trials

, Vol.

23

No.

1

, p.

1038

, doi:

[https://doi-org.sire.ub.edu/10.1186/s13063-022-07004-2](https://doi-org.sire.ub.edu/10.1186/s13063-022-07004-2)

.

Dewidar

,

O.

,

Elmestekawy

,

N.

and

Welch

,

V.

(

2022

), “”,

Research Integrity and Peer Review

, Vol.

7

No.

1

, p.

4

, doi:

[https://doi-org.sire.ub.edu/10.1186/s41073-022-00123-z](https://doi-org.sire.ub.edu/10.1186/s41073-022-00123-z)

.

Ferran-Ferrer

,

N.

,

Boté Vericad

,

J.J.

and

Minguillón I Alfonso

,

J.

(

2024

), “”,

\[Object Object\]

, doi:

[https://doi-org.sire.ub.edu/10.34810/DATA980](https://doi-org.sire.ub.edu/10.34810/DATA980)

.

Ferran-Ferrer

,

N.

,

Boté-Vericad

,

J.-J.

and

Minguillón

,

J.

(

2023

), “”,

El Profesional de La Información

, p.

e320617

, doi:

[https://doi-org.sire.ub.edu/10.3145/epi.2023.nov.17](https://doi-org.sire.ub.edu/10.3145/epi.2023.nov.17)

.

Ferran-Ferrer

,

N.

,

Castellanos-Pineda

,

P.

,

Minguillón

,

J.

and

Meneses

,

J.

(

2021

), “”,

El Profesional de la Información

, Vol.

30

No.

5

, p.

e300516

, doi:

[https://doi-org.sire.ub.edu/10.3145/epi.2021.sep.16](https://doi-org.sire.ub.edu/10.3145/epi.2021.sep.16)

.

Foley

,

M.

and

Williamson

,

S.

(

2018

), “”,

Gender in Management: An International Journal

, Vol.

33

No.

8

, pp.

623

\-

635

, doi:

[https://doi-org.sire.ub.edu/10.1108/GM-03-2018-0037](https://doi-org.sire.ub.edu/10.1108/GM-03-2018-0037)

.

Fox

,

C.W.

and

Paine

,

C.E.T.

(

2019

), “”,

Ecology and Evolution

, Vol.

9

No.

6

, pp.

3599

\-

3619

, doi:

[https://doi-org.sire.ub.edu/10.1002/ece3.4993](https://doi-org.sire.ub.edu/10.1002/ece3.4993)

.

González-Salmón

,

E.

and

Robinson-García

,

N.

(

2024

), “”,

Infonomy

, Vol.

2

No.

1

, doi:

[https://doi-org.sire.ub.edu/10.3145/infonomy.24.010](https://doi-org.sire.ub.edu/10.3145/infonomy.24.010)

.

Hofstra

,

B.

,

Kulkarni

,

V.V.

,

Munoz-Najar Galvez

,

S.

,

He

,

B.

,

Jurafsky

,

D.

and

McFarland

,

D.A.

(

2020

), “”,

Proceedings of the National Academy of Sciences

, Vol.

117

No.

17

, pp.

9284

\-

9291

, doi:

[https://doi-org.sire.ub.edu/10.1073/pnas.1915378117](https://doi-org.sire.ub.edu/10.1073/pnas.1915378117)

.

Ikae

,

C.

and

Savoy

,

J.

(

2022

), “”,

Journal of the Association for Information Science and Technology

, Vol.

73

No.

1

, pp.

58

\-

69

, doi:

[https://doi-org.sire.ub.edu/10.1002/asi.24541](https://doi-org.sire.ub.edu/10.1002/asi.24541)

.

Kaatz

,

A.

,

Gutierrez

,

B.

and

Carnes

,

M.

(

2014

), “”,

Trends in Pharmacological Sciences

, Vol.

35

No.

8

, pp.

371

\-

373

, doi:

[https://doi-org.sire.ub.edu/10.1016/j.tips.2014.06.005](https://doi-org.sire.ub.edu/10.1016/j.tips.2014.06.005)

.

Kaminski

,

D.

and

Geisler

,

C.

(

2012

), “”,

Science

, Vol.

335

No.

6070

, pp.

864

\-

866

, doi:

[https://doi-org.sire.ub.edu/10.1126/science.1214844](https://doi-org.sire.ub.edu/10.1126/science.1214844)

.

Karimi

,

F.

,

Wagner

,

C.

,

Lemmerich

,

F.

,

Jadidi

,

M.

and

Strohmaier

,

M.

(

2016

), “”,

Proceedings of the 25th International Conference Companion on World Wide Web – WWW ’16 Companion

,

ACM Press

,

Montreal

, pp.

53

\-

54

, doi:

[https://doi-org.sire.ub.edu/10.1145/2872518.2889385](https://doi-org.sire.ub.edu/10.1145/2872518.2889385)

.

Keyes

,

O.

(

2018

), “”,

Proceedings of the Acm on Human-Computer Interaction

, Vol.

2

, pp.

88:1

\-

88:22

, doi:

[https://doi-org.sire.ub.edu/10.1145/3274357](https://doi-org.sire.ub.edu/10.1145/3274357)

.

Larivière

,

V.

,

Ni

,

C.

,

Gingras

,

Y.

,

Cronin

,

B.

and

Sugimoto

,

C.R.

(

2013

), “”,

Nature

, Vol.

504

No.

7479

, pp.

211

\-

213

, doi:

[https://doi-org.sire.ub.edu/10.1038/504211a](https://doi-org.sire.ub.edu/10.1038/504211a)

.

Leuner

,

K.

(

2021

), “”,

Huntington Library Quarterly

, Vol.

84

No.

1

, pp.

13

\-

26

.

Llorens

,

A.

,

Tzovara

,

A.

,

Bellier

,

L.

,

Bhaya-Grossman

,

I.

,

Bidet-Caulet

,

A.

,

Chang

,

W.K.

,

Cross

,

Z.R.

, et al. (

2021

), “”,

Neuron

, Vol.

109

No.

13

, pp.

2047

\-

2074

, doi:

[https://doi-org.sire.ub.edu/10.1016/j.neuron.2021.06.002](https://doi-org.sire.ub.edu/10.1016/j.neuron.2021.06.002)

.

Maes

,

K.

,

Gvozdanovic

,

J.

,

Buitendijk

,

S.

,

Hallberg

,

I.R.

and

Mantilleri

,

B.

(

2012

),

Women, Research and Universities: Excellence without Gender Bias

,

LERU, League of European Research Universities

.

Mihaljević-Brandt

,

H.

,

Santamaría

,

L.

and

Tullney

,

M.

(

2016

), “”,

Plos One

, Vol.

11

No.

10

, p.

e0165367

, doi:

[https://doi-org.sire.ub.edu/10.1371/journal.pone.0165367](https://doi-org.sire.ub.edu/10.1371/journal.pone.0165367)

.

Minguillón

,

J.

,

Meneses

,

J.

,

Aibar

,

E.

,

Ferran-Ferrer

,

N.

and

Fàbregues

,

S.

(

2021

), “”,

PLoS One

, Vol.

16

No.

2

, p.

e0246702

, doi:

[https://doi-org.sire.ub.edu/10.1371/journal.pone.0246702](https://doi-org.sire.ub.edu/10.1371/journal.pone.0246702)

.

Monroe

,

K.

,

Ozyurt

,

S.

,

Wrigley

,

T.

and

Alexander

,

A.

(

2008

), “”,

Perspectives on Politics

, Vol.

6

No.

2

, pp.

215

\-

233

, doi:

[https://doi-org.sire.ub.edu/10.1017/S1537592708080572](https://doi-org.sire.ub.edu/10.1017/S1537592708080572)

.

Moss-Racusin

,

C.A.

,

Dovidio

,

J.F.

,

Brescoll

,

V.L.

,

Graham

,

M.J.

and

Handelsman

,

J.

(

2012

), “”,

Proceedings of the National Academy of Sciences

, Vol.

109

No.

41

, pp.

16474

\-

16479

, doi:

[https://doi-org.sire.ub.edu/10.1073/pnas.1211286109](https://doi-org.sire.ub.edu/10.1073/pnas.1211286109)

.

Nguyen

,

M.

,

Gonzalez

,

L.

,

Chaudhry

,

S.I.

,

Ahuja

,

N.

,

Pomahac

,

B.

,

Newman

,

A.

,

Cannon

,

A.

,

Zarebski

,

S.A.

and

Dardik

,

A.

(

2023

), “”,

JAMA Network Open

, Vol.

6

No.

3

, p.

e233630

, doi:

[https://doi-org.sire.ub.edu/10.1001/jamanetworkopen.2023.3630](https://doi-org.sire.ub.edu/10.1001/jamanetworkopen.2023.3630)

.

Ni

,

C.

,

Smith

,

E.

,

Yuan

,

H.

,

Larivière

,

V.

and

Sugimoto

,

C.R.

(

2021

), “”,

Science Advances

, Vol.

7

No.

36

, p.

eabe4639

, doi:

[https://doi-org.sire.ub.edu/10.1126/sciadv.abe4639](https://doi-org.sire.ub.edu/10.1126/sciadv.abe4639)

.

Patel

,

S.R.

,

Riano

,

I.

,

Geiger

,

G.

,

Pimienta

,

J.

,

Abuali

,

I.

,

Ai

,

A.

,

Ramirez Roggio

,

A.

,

Dhawan

,

N.

,

Dizman

,

N.

,

Salina

,

A.L.

and

Duma

,

N.

(

2021

), “”,

Journal of Clinical Oncology

, Vol.

39

No.

15\_suppl

, p.

11007

, doi:

[https://doi-org.sire.ub.edu/10.1200/JCO.2021.39.15\_suppl.11007](https://doi-org.sire.ub.edu/10.1200/JCO.2021.39.15_suppl.11007)

.

Piscopo

,

A.

and

Simperl

,

E.

(

2018

), “”,

Proceedings of the Acm on Human-Computer Interaction

, Vol.

2

, pp.

141:1

\-

141:18

, doi:

[https://doi-org.sire.ub.edu/10.1145/3274410](https://doi-org.sire.ub.edu/10.1145/3274410)

.

Piwowar

,

H.

,

Priem

,

J.

,

Larivière

,

V.

,

Alperin

,

J.P.

,

Matthias

,

L.

,

Norlander

,

B.

,

Farley

,

A.

,

West

,

J.

and

Haustein

,

S.

(

2018

), “”,

PeerJ

, Vol.

6

, p.

e4375

, doi:

[https://doi-org.sire.ub.edu/10.7717/peerj.4375](https://doi-org.sire.ub.edu/10.7717/peerj.4375)

.

Robinson-Garcia

,

N.

,

Costas

,

R.

,

Sugimoto

,

C.R.

,

Larivière

,

V.

and

Nane

,

G.F.

(

2020

), “”, in

Rodgers

,

P.

and

Morgan

,

A.

(Eds),

eLife

, Vol.

9

, p.

e60586

, doi:

[https://doi-org.sire.ub.edu/10.7554/eLife.60586](https://doi-org.sire.ub.edu/10.7554/eLife.60586)

.

Santamaría

,

L.

and

Mihaljević

,

H.

(

2018

), “”,

PeerJ Computer Science

, Vol.

4

, p.

e156

, doi:

[https://doi-org.sire.ub.edu/10.7717/peerj-cs.156](https://doi-org.sire.ub.edu/10.7717/peerj-cs.156)

.

Schmaling

,

K.B.

and

Gallo

,

S.A.

(

2023

), “”,

Research Integrity and Peer Review

, Vol.

8

No.

1

, p.

2

, doi:

[https://doi-org.sire.ub.edu/10.1186/s41073-023-00127-3](https://doi-org.sire.ub.edu/10.1186/s41073-023-00127-3)

.

Sebo

,

P.

(

2021

), “”,

Journal of the Medical Library Association

, Vol.

109

No.

4

, doi:

[https://doi-org.sire.ub.edu/10.5195/jmla.2021.1252](https://doi-org.sire.ub.edu/10.5195/jmla.2021.1252)

.

Shen

,

H.

(

2013

), “”,

Nature News

, Vol.

495

No.

7439

, p.

22

, doi:

[https://doi-org.sire.ub.edu/10.1038/495022a](https://doi-org.sire.ub.edu/10.1038/495022a)

.

Trepte

,

S.

and

Loths

,

L.

(

2020

), “”,

Annals of the International Communication Association

, Vol.

44

No.

4

, pp.

289

\-

311

, doi:

[https://doi-org.sire.ub.edu/10.1080/23808985.2020.1804434](https://doi-org.sire.ub.edu/10.1080/23808985.2020.1804434)

.

VanHelene

,

A.D.

,

Khatri

,

I.

,

Hilton

,

C.B.

,

Mishra

,

S.

,

Uzun

,

E.D.G.

and

Warner

,

J.L.

(

2024

), “”,

medRxiv, 31 January

, doi:

[https://doi-org.sire.ub.edu/10.1101/2024.01.30.24302027](https://doi-org.sire.ub.edu/10.1101/2024.01.30.24302027)

.

West

,

J.D.

,

Jacquet

,

J.

,

King

,

M.M.

,

Correll

,

S.J.

and

Bergstrom

,

C.T.

(

2013

), “”, in

Hadany

,

L.

(Ed.),

PLoS ONE

, Vol.

8

No.

7

, p.

e66212

, doi:

[https://doi-org.sire.ub.edu/10.1371/journal.pone.0066212](https://doi-org.sire.ub.edu/10.1371/journal.pone.0066212)

.