---
title: "The screening phase in systematic reviews: Can we speed up the process?"
source: "https://www-sciencedirect-com.sire.ub.edu/science/article/abs/pii/S0065245821000310"
author:
published:
created: 2025-05-07
description: "The aim of a systematic reviews (SRs) is to gain a better understanding of a certain aspect of selected research field using the principle of classifi…"
tags:
  - "research_method"
---
## Chapter Three - The screening phase in systematic reviews: Can we speed up the process?

[https://doi.org/10.1016/bs.adcom.2021.01.006](https://doi.org/10.1016/bs.adcom.2021.01.006 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S0065245821000310&orderBeanReset=true)

## Introduction

The first phase of research work in any field is to get insight into the state of the art by reviewing the existing knowledge \[1\]. Diverse types of evidence-based research exist and one of them is systematic review (SR). A specific form of SR, namely systematic literature review (SLR) is performed over a large number of carefully selected articles in a field to achieve this aim \[2\]. An alternative is to conduct a systematic mapping study (SMS), which only classifies studies into a set of predefined clusters. As such it tends to give less specific answers but involves an even larger set of selected articles \[3\]. Both types of reviews have to follow a strictly defined protocol to be valid. This protocol is suitable when it is consistent with the guidelines for performing SR \[4\]. One of the most important steps is performed after the collection of a large number of approximately suitable articles from different sources when a set of suitable articles is selected by screening using defined inclusion/exclusion criteria. The screening is usually performed by a quick manual reading of each article's title and abstract \[5, 6\]. Then, the article is included or excluded from the set of suitable articles. Unfortunately, the amount of collected articles is usually very large (more than 5000) and demands a lot of effort \[7\]. Syriani reportedz that screening of 11,173 articles in total demanded more than 558 h \[8\], while Kosar screened 1636 articles in 81 h \[9\]. Even in case of a smaller initial set of articles, the manual screening consumes a large amount of effort (time) \[10\]. As a consequence, the SR performers tend to diminish the initial set of articles by limiting the initial search or performing it in a fast, not enough detailed way. This practice may lead to exclusion of valuable evidence. By suitable automation of screening several important advantages can be achieved \[11, 12\]. Most importantly, the shorter performance time with less manual effort enables the researcher to actually screen a larger set of collected articles. The difficult part is how to efficiently perform such an automated screening in a correct, yet appropriate way. Additional issues involve the usability concerns (e.g., the availability of a tool).

The main objective of this work is to propose an approach for a faster, but still affordable screening of a large number of articles, which is compatible with the strict rules of SR protocol. The approach is supported by a tool, which can be configured to better meet the expected level of screening results correctness. It enables adaptable configuration of screening, iterative optimization of screening by using it on small pilot sets, screening execution and the assessment of the outcomes. Additionally, an experiment to demonstrate the suitability of such an approach is presented. The experiment compares the effect of the manual and several executions of the automated screening with an emphasis on the size of the pilot set and on the definition of decision rules. It is conducted on the collection of articles for an SMS on examining different processes while developing a domain-specific language (DSL) or domain-specific modeling language (DSML). Finally, the concluding remarks concisely points out the main benefits of the tool usage.

The proper management of an SLR or SMS must follow a rigorous protocol, thus a detailed insight into various aspects of both types of research are given first. Next, the problem of the most time-consuming parts of SR process is explored to find out possible points where time could be saved. Focusing on the step of the article's screening, a solution for the automation of this step is proposed. The solution is configurable and it is based on the principle of the statistical analysis of the article's contents. The automated screening approach is implemented by a tool. To demonstrate its value, an experiment is performed, too. The actual context of the experiment (i.e., the SMS on examining the different processes while developing DS(M)L) is explained first. The experiment compares the results of the manual vs automated screening execution. Several variants of tool's improvement strategies are explored in the experiment discussing four issues: the necessary size of the pilot set to be manually screened, the improvement strategy, the number and type of keywords, and the structure of decision rules. The presentation of results is accompanied by a short discussion. Finally, the related work is presented to compare our approach with similar solutions.

First, the definition of an approach for the automated screening demonstrates its compatibility with SR protocol. Second, the custom-made tool we developed to support the approach proves its practical applicability. The tool is configurable and enables different levels of classification accuracy. Third, the results of an experiment demonstrate the practical level up to which screening step can be automated, and the required manual effort. The final part of the experiment shortly points out the main achievements of its use.

In the next section, the principles of the evidence-based research with the emphasis on the details of SR (SLR and SMS) are explained. In Section 3, the problem of screening automation and its configurable solution is presented in detail. Especially, an automatic screening approach is explained. In Section 4, the presentation of solution's implementation with a custom-made tool is explained. Section 5 describe a demonstration experiment we performed. Its context is given in the first part, while the core of this section presents four parts of the experiment with the discussion of corresponding results. The related work is presented in Section 6. The last section concludes and presents future work.

## Section snippets

## Evidence-based research in software engineering

The results of research work can contribute to several types of achievements \[13\], but they must clearly base on a solid foundation of previous experience. The term *evidence-based research* is implicated from *evidence-based practice (EBP)* in the field of medicine, which defines an up-to-date research evidence to inform clinical decisions \[14\]. In the field of medicine, this approach is enforced by a large corpus of predominantly well structured (experience and research) work. Unfortunately, this

## Effective article screening: The problem and the solution

The following part presents the core of this article. First, the actual problem is systematically presented. Second, the solution is described in a sequence of subsections addressing topics from basic idea to solution specifics (i.e., decision principles, statistical analysis, and automatic assessment).

## The implementation of the automatic screening

Two artifacts are developed to implement the before mentioned solution. First, a rigorous process to efficiently perform the automatic screening is defined. Second, a specific tool to support the process execution is developed as well.

## The experiment description

An experiment is presented to evaluate the proposed solution and demonstrate its usability on a practical example. The experiment is conducted on an actual SMS we are currently performing. The aim of this SMS is to review the available evidence on examining different processes while developing a DSL or DSML. Actually, the idea for automatic screening is based on some actual issues and experience from this SMS.

At the beginning of the section, we provide a short insight into the contents of our

## Conclusion

The aim of our work is to propose, implement, and demonstrate a solution which speeds up the screening phase of the SR process. The main idea is to appropriately substitute manually performed screening with a screening, which is (at least) partly performed automatically while carefully assesses the quality of the outcome. The presented approach is described in detail and integrated into the rigorous SLR or SMS process. It is implemented by an easy-to-use tool, which is able to organize and

**Igor Rožanc** received the MSc and PhD degrees in Computer Science from the University of Ljubljana in 1996 and 2003, respectively. He is currently a senior lecturer at the University of Ljubljana, Faculty of Computer and Information Science. His research interests are in the area of Software Engineering, especially software quality, model-driven development, and domain-specific (modeling) languages. He is a member of the IEEE. More information about him is available at [//www.fri.uni-lj.si/en/employees/igor-rozanc](https://www.fri.uni-lj.si/en/employees/igor-rozanc)

- *et al.*
	### Guidelines for conducting systematic mapping studies in software engineering: an update
	### Inf. Softw. Technol.
	(2015)
- *et al.*
	### On the reliability of mapping studies in software engineering
	### J. Syst. Softw.
	(2013)
- *et al.*
	### Lessons from applying the systematic literature review process within the software engineering domain
	### J. Syst. Softw.
	(2007)
- *et al.*
	### A systematic mapping study driven by the margin of error
	### J. Syst. Softw.
	(2018)
- *et al.*
	### Systematic mapping study of template-based code generation
	### Comput. Lang. Syst. Struct.
	(2018)
- *et al.*
	### Domain-specific languages: a systematic mapping study
	### Inf. Softw. Technol.
	(2016)
- *et al.*
	### A systematic mapping study of software reliability modeling
	### Inf. Softw. Technol.
	(2014)
- *et al.*
	### Chapter One—a systematic approach to generation of new ideas for PhD research in computing
- *et al.*
	### Experimental validation in software engineering
	### Inf. Softw. Technol.
	(1997)
- ### Empirical research methods for technology validation: scaling up to practice
	### J. Syst. Softw.
	(2014)

- *et al.*
	### Aspect-oriented model-driven code generation: a systematic mapping study
	### Inf. Softw. Technol.
	(2013)
- *et al.*
	### A systematic mapping study of web application testing
	### Inf. Softw. Technol.
	(2013)
- *et al.*
	### Software product line testing—a systematic mapping study
	### Inf. Softw. Technol.
	(2011)
- *et al.*
	### Using mapping studies as the basis for further research: a participant-observer case study
	### Inf. Softw. Technol.
	(2011)
- *et al.*
	### Systematic literature reviews in software engineering—a systematic literature review
	### Inf. Softw. Technol.
	(2009)
- *et al.*
	### Reducing workload in systematic review preparation using automated citation classification
	### J. Am. Med. Inform. Assoc.
	(2006)
- *et al.*
	### Using ontology-based semantic similarity to facilitate the article screening process for systematic reviews
	### J. Biomed. Informatics
	(2017)
- *et al.*
	### Special issue on the programming Languages track at the 28th ACM symposium on applied computing
	### Comput. Lang. Syst. Struct.
	(2014)
- *et al.*
	### Definitions and approaches to model quality in model-based software development—a review of literature
	### Inf. Softw. Technol.
	(2009)
- *et al.*
	### Design and implementation of domain-specific language easytime
	### Comput. Lang. Syst. Struct.
	(2011)
- *et al.*
	### Debugging measurement systems using a domain-specific modeling language
	### Comput. Ind.
	(2014)
- *et al.*
	### Usability driven DSL development with USE-ME
	### Comput. Lang. Syst. Struct.
	(2018)
- *et al.*
	### Leveraging software product lines engineering in the development of external DSLs: a systematic literature review
	### Comput. Lang. Syst. Struct.
	(2016)
- *et al.*
	### Evidence-based software engineering
- ### Procedures for Performing Systematic Reviews
	(2004)
- *et al.*
	### Guidelines for performing systematic literature reviews in software engineering version 2.3
	### Engineering
	(2007)
- *et al.*
	### A visual analysis approach to update systematic reviews
- *et al.*
	### A visual text mining approach for systematic reviews

- ### Screening articles for systematic reviews with ChatGPT
	2024, Journal of Computer Languages
	Citation Excerpt:
	For instance, Kosar et al. \[16\] propose a variation of the Kitchenham protocol \[5\] by reducing the number of articles to screen within a certain margin of error. Rozanc and Mernik \[17\] propose automating the screening task of systematic mapping studies through text analysis, employing text statistic analysis to count the occurrence of important works, and enabling the user to define rules to decide how the screening process should interpret these occurrences. In particular, users state which words are required, have a positive or negative effect towards the decision outcome.

![](https://ars-els-cdn-com.sire.ub.edu/content/image/1-s2.0-S0065245821000310-u03-01-9780128241219.jpg)

**Igor Rožanc** received the MSc and PhD degrees in Computer Science from the University of Ljubljana in 1996 and 2003, respectively. He is currently a senior lecturer at the University of Ljubljana, Faculty of Computer and Information Science. His research interests are in the area of Software Engineering, especially software quality, model-driven development, and domain-specific (modeling) languages. He is a member of the IEEE. More information about him is available at [https://www.fri.uni-lj.si/en/employees/igor-rozanc](https://www.fri.uni-lj.si/en/employees/igor-rozanc).

![](https://ars-els-cdn-com.sire.ub.edu/content/image/1-s2.0-S0065245821000310-u03-02-9780128241219.jpg)

**Marjan Mernik** received the MSc and PhD degrees in Computer Science from the University of Maribor in 1994 and 1998, respectively. He is currently a professor at the University of Maribor, Faculty of Electrical Engineering and Computer Science. He was a visiting professor at the University of Alabama at Birmingham, Department of Computer and Information Sciences. His research interests include programming languages, compilers, domain-specific (modeling) languages, grammar-based systems, grammatical inference, and evolutionary computations. He is a member of the IEEE, ACM, and EAPLS. He is the Editor-in-Chief of the Journal of Computer Languages, as well as Associate Editors of the Applied Soft Computing Journal, Information Sciences Journal, and Swarm and Evolutionary Computation Journal. He is being named a Highly Cited Researcher for years 2017 and 2018. More information about his work is available at [https://lpm.feri.um.si/en/members/mernik/](https://lpm.feri.um.si/en/members/mernik/).

[View full text](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/S0065245821000310)