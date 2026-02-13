---
title: Techniques and Methods to Evaluate Human-Centered Symbiotic AI Systems | Companion Proceedings of the 30th International Conference on Intelligent User Interfaces
source: https://dl-acm-org.sire.ub.edu/doi/10.1145/3708557.3716153
author:
  - "[[Miriana Calvano]]"
published:
created: 2025-12-04
description:
tags:
  - tech/hybrid
  - design/evaluation
  - design/UCD/
  - op/acc/download
DOI: 10.1145/3708557.3716153
year: "2025"
apa_citation: Calvano, M 2025
apa_long: Calvano, Miriana. 2025
journal: "IUI '25: Companion Proceedings of the 30th International Conference on Intelligent User Interfaces"
---
[[Techniques and Methods to Evaluate Human-Centered Symbiotic AI Systems 1]]

## Abstract

Artificial Intelligence (AI) is transforming many fields, enabling enhanced automated decision-making processes and the development of autonomous systems. To design high-quality AI systems, Human-Computer Interaction (HCI) and AI contaminate each other, creating a symbiosis between humans and AI. I am a second-year PhD student in Computer Science with a fellowship in the Future AI Research (FAIR) project. My research project concerns the evaluation of the quality of Symbiotic AI (SAI) systems and, consequently, the definition of an evaluation framework and metrics to evaluate both the human’s and AI system’s performance. This contribution presents a first set of results considering the main opportunities and challenges in this new scenario.

## 1 Introduction

The research area of this project concerns Symbiotic Artificial Intelligence (SAI). In this scenario, Human-Computer Interaction (HCI) and AI are not separate disciplines, but they contaminate each other to empower humans during interaction. In this regard, it is possible to introduce the concept of Symbiotic AI (SAI), which refers to a collaborative relationship between humans and AI systems in which humans are empowered and not replaced \[[5](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0005)\]. The focus is shifted towards enhancing human behaviors and cognitive abilities while guaranteeing the right balance between the automation of the system and the intervention of the human \[[9](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0009)\]. The following sections describe the main aspects of this research work.

## 2 Research Motivations

It is important to design high-quality AI systems that empower people in ways that make systems reliable, safe, and trustworthy and fully in human control \[[9](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0009)\]. Human-centered techniques should be applied while designing and developing SAI systems to reach this goal.

In this field of study, researchers face many challenges, such as low-level explainability, data privacy, biased data and ethical issues. Since they can represent a potential risk to humans, the ethical and moral challenges associated with AI must be addressed \[[1](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0001)\]. Starting from the learning phase of the AI model its behavior can be influenced by biased data therefore it is necessary to reduce them as much as possible to avoid non-fair and discriminatory decisions. To achieve this objective, regulations (e.g., the European AI Act) should be considered while designing and developing SAI systems to safeguard human rights during interaction. The AI Act is a regulatory framework enacted by the EU to govern the usage of AI, categorizing specific systems in the associated level of risks (i.e., minimal, limited, high, and unacceptable) \[[3](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0003)\]. Another challenge is represented by the black-box nature of AI models, which do not allow users to intervene in the system’s performance and to understand the outputs. To involve humans in the decision process and to foster symbiosis, the emphasis has moved toward explainable models that allow users to understand, manage, and trust AI decisions \[[6](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0006)\]. Ultimately, it is important to find a way to assess the quality of human-AI symbiosis according to how it benefits humans. Achieving this objective requires human-centered design methods and techniques, fostering a multidisciplinary setting where AI and HCI researchers work together. Figure [1](https://dl-acm-org.sire.ub.edu/doi/10.1145/#fig1) represents the final objective of this research work in which the human and AI sides are considered together to evaluate SAI systems.

![](https://dl-acm-org.sire.ub.edu/cms/10.1145/3708557.3716153/asset/b40ae5dd-e740-4989-9a53-7b961751200a/assets/images/large/iuicompanion25-10-fig1.jpg)

UX and AI metrics’ role for the definition of SAI metrics

## 3 Objectives and Research Questions

The research work focuses primarily on improving the human-AI symbiotic relationship by suggesting solutions to evaluate the quality of SAI systems and the scientific validity of design techniques and interaction mechanisms. Specifically:

- define an evaluation framework and novel metrics to evaluate the symbiosis between humans and AI.
- define new interaction mechanisms and user interfaces that align with these new needs.
- define transparency mechanisms to enforce SAI system’s behaviors; users must be allowed to easily comprehend the decisions of the system, even if they are not AI experts.

The research questions (RQs) being investigated to achieve the previously presented objectives are as follows.

- *(RQ1) What are the existing challenges resulting from the intersection among Human-Computer Interaction (HCI) and Artificial Intelligence (AI)? How can these challenges be addressed?* The first step of this work is to comprehend the well-established concepts and methodologies necessary to define instruments (e.g., guidelines, metrics, frameworks) to create high-quality SAI systems. A systematic literature review (SLR) was conducted to have an overall vision of the study context. Based on the results obtained, the specific characteristics of SAI are defined.
- *(RQ2) What are the limitations in existing metrics to evaluate the human-AI symbiosis?* As a starting point, the existing literature was analysed to have an overall vision of how the well-known User Experience (UX) and AI metrics can be employed to assess AI and human performance. The collected information can be helpful in understanding how the existing elements can be integrated to define novel SAI metrics.
- *(RQ 3) How can the human-AI symbiotic relationship be evaluated?* Novel metrics and evaluation framework will be defined to evaluate the quality of the human-AI symbiotic relationship properly.

## 4 Related Work

Due to the definition of a new perspective in which HCI and AI are strictly connected, a new discipline was born: Human-Centered Artificial Intelligence (HCAI), which combines user experiences with embedded AI methods while balancing AI automation and human intervention \[[9](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0009)\]. This is ensured by SAI, which is a specialization of HCAI that aims to boost human-machine collaboration by enhancing human cognitive abilities through the interaction process \[[4](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0004)\]. One of the first times that the term *symbiosis* was used was in 1960, when Licklider J. stated that “Man (human)-computer symbiosis is an expected development in cooperative interaction between men (humans) and electronic computers” \[[8](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0008)\]. The symbiosis can be seen as the integration of two approaches: Augmented Intelligence, which aims to enhance the effectiveness of the decision-making process, and Human Intelligence for Artificial Intelligence (HI4AI), in which human intelligence serves as information feedback or as inspiration \[[7](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0007)\]. Symbiosis can be considered also as a consequence of the human-AI partnership, where human intelligence serves to improve AI processes and functionality and vice versa: it is a bidirectional relationship of continuous exchange, similar to HI4AI \[[10](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0010)\]. In accordance with SAI philosophy, AI systems should be designed according to a human-centered approach, as developed within the HCI community, to foster the human-AI symbiotic relationship \[[5](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0005)\]. In this scenario, humans are considered in all of their dimensions, in terms of dignity, environment, needs, and ethics, to safeguard humans’ rights during the interaction process. For this reason, the AI Act proposed a *human-centric* approach, which ensures that human values are central to how AI systems are developed, deployed and used \[[3](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0003)\].

In the end, to reach the human-AI symbiosis, humans should trust and properly comprehend the AI model’s decisions, making trustworthiness one of the main properties to consider when dealing with such systems. Trustworthiness can be seen as the umbrella property to ensure a human-centric approach to AI \[[2](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0002)\].

## 5 Research Approach

To design and develop high-quality SAI systems, the user must be included in all the phases of the creation process. In this section, the approaches it is intended to adopt to reach the objectives of this research project are described below. An approach to adopt refers to considering the user’s characteristics starting from the training phase of the AI model. By fully considering users from the beginning of the SAI system design, the system’s behavior can be easily adapted to their needs. User studies will be conducted to assess the validity of the proposed approach and gather additional information. It is necessary to define novel metrics concerning the SAI system’s properties. To reach this goal, the starting point of this research work is an SLR to understand whether and how humans are considered in the regulations that have to be referred to when creating SAI systems (i.e. the European AI Act). In the end, proper evaluation techniques will be applied to verify the validity of the gathered results (i.e., metrics and evaluation framework). In particular, the defined solutions will be assessed by performing studies with users; SAI systems’ user interfaces will be evaluated by performing usability studies and in-field studies to understand if these can be considered applicable and valid in real-world scenarios.

## 6 Current State of the Work and Expected Results

To have an overall understanding of the context of the study, an investigation of the literature was conducted. In this way, the basic concepts were acquired to represent a starting point for the research project.

Due to the coming force of the European AI Act, an SLR was conducted to understand how humans are considered in this new scenario and what characteristics SAI systems should have to be legally compliant. Considering the obtained results, principles and properties that characterize SAI systems were defined. It emerged that aspects concerning the level of automation, protection of users from potential harms, transparency and fairness of AI decisions must be considered together with aspects concerning trustworthiness, robustness and sustainability of AI. To validate these principles and properties, a user study performed on a web application employed in the medical field is being planned. In the end, to delineate the specific characteristics to consider when evaluating SAI systems, an SLR is being carried out. The obtained results will define a first set of metrics and framework to follow during the evaluation phase.

In the end, the work plan of the research project encompassing the 3-years program is the following: *Phase 1* concerns the activities related to studying the state of the art concerning SAI and related topics. In particular, it is important to study definitions and basic concepts, identify and analyze existing case studies, and evaluate solutions. *Phase 2* concerns the activities related to the design and evaluation of symbiotic AI systems. The following activities will be performed: elicitation of users’ needs and definition of the technical methodology to follow; design of interaction paradigms that align with SAI systems’ characteristics; evaluation of SAI systems’ performance through the defined metrics in order to assess their validity. *Phase 3* concerns the activities related to the validity assessment of the proposed solutions and the writing of the PhD thesis.

In the end, this contribution presents the main challenges and opportunities of this research project. Currently, I am at the beginning of the second phase described in the work plan. Based on the gathered results, it is possible to state that humans are not widely considered regarding AI aspects. Therefore, the focus is on understanding how to fully consider the human during the entire life-cycle of SAI systems, from the definition of requirements to their evaluation.

## Acknowledgments

The research Miriana Calvano is supported by the co-funding of the European Union - Next Generation EU: NRRP Initiative, Mission 4, Component 2, Investment 1.3 – Partnerships extended to universities, research centers, companies, and research D.D. MUR n. 341 del 15.03.2022 – Next Generation EU (PE0000013 – “Future Artificial Intelligence Research – FAIR” - CUP: H97G22000210007).

[View full text](https://dl-acm-org.sire.ub.edu/doi/full/10.1145/3708557.3716153) | [Download PDF](https://dl-acm-org.sire.ub.edu/doi/pdf/10.1145/3708557.3716153?download=true)

## PDF text extraction

Techniques and Methods to Evaluate Human-Centered Symbiotic 
AI Systems 
Miriana Calvano 
Department of Computer Science 
University of Bari Aldo Moro 
Bari, BA, Italy 
miriana.calvano@uniba.it 
Abstract 
Artificial Intelligence (AI) is transforming many fields, enabling 
enhanced automated decision-making processes and the develop-
ment of autonomous systems. To design high-quality AI systems, 
Human-Computer Interaction (HCI) and AI contaminate each other, 
creating a symbiosis between humans and AI. I am a second-year 
PhD student in Computer Science with a fellowship in the Future AI 
Research (FAIR) project. My research project concerns the evalua-
tion of the quality of Symbiotic AI (SAI) systems and, consequently, 
the definition of an evaluation framework and metrics to evaluate 
both the human’s and AI system’s performance. This contribution 
presents a first set of results considering the main opportunities 
and challenges in this new scenario. 
CCS Concepts 
• Human-centered computing → HCI design and evaluation 
methods. 
Keywords 
Symbiotic Artificial Intelligence (SAI), Human-Centered Design, 
Metrics, Evaluation 
ACM Reference Format: 
Miriana Calvano. 2025. Techniques and Methods to Evaluate Human-Centered 
Symbiotic AI Systems. In 30th International Conference on Intelligent User 
Interfaces Companion (IUI Companion ’25), March 24–27, 2025, Cagliari, Italy. 
ACM, New York, NY, USA, 3 pages. https://doi.org/10.1145/3708557.3716153 
1 Introduction 
The research area of this project concerns Symbiotic Artificial Intel-
ligence (SAI). In this scenario, Human-Computer Interaction (HCI) 
and AI are not separate disciplines, but they contaminate each other 
to empower humans during interaction. In this regard, it is possible 
to introduce the concept of Symbiotic AI (SAI), which refers to 
a collaborative relationship between humans and AI systems in 
which humans are empowered and not replaced [5]. The focus is 
shifted towards enhancing human behaviors and cognitive abilities 
while guaranteeing the right balance between the automation of 
Permission to make digital or hard copies of all or part of this work for personal or 
classroom use is granted without fee provided that copies are not made or distributed 
for profit or commercial advantage and that copies bear this notice and the full citation 
on the first page. Copyrights for third-party components of this work must be honored. 
For all other uses, contact the owner/author(s). 
IUI Companion ’25, Cagliari, Italy 
© 2025 Copyright held by the owner/author(s). 
ACM ISBN 979-8-4007-1409-2/25/03 
https://doi.org/10.1145/3708557.3716153 
the system and the intervention of the human [9]. The following 
sections describe the main aspects of this research work. 
2 Research Motivations 
It is important to design high-quality AI systems that empower 
people in ways that make systems reliable, safe, and trustworthy 
and fully in human control [9]. Human-centered techniques should 
be applied while designing and developing SAI systems to reach 
this goal. 
In this field of study, researchers face many challenges, such 
as low-level explainability, data privacy, biased data and ethical 
issues. Since they can represent a potential risk to humans, the 
ethical and moral challenges associated with AI must be addressed 
[1]. Starting from the learning phase of the AI model its behavior 
can be influenced by biased data therefore it is necessary to reduce 
them as much as possible to avoid non-fair and discriminatory de-
cisions. To achieve this objective, regulations (e.g., the European 
AI Act) should be considered while designing and developing SAI 
systems to safeguard human rights during interaction. The AI Act 
is a regulatory framework enacted by the EU to govern the usage of 
AI, categorizing specific systems in the associated level of risks (i.e., 
minimal, limited, high, and unacceptable) [3]. Another challenge 
is represented by the black-box nature of AI models, which do not 
allow users to intervene in the system’s performance and to under-
stand the outputs. To involve humans in the decision process and to 
foster symbiosis, the emphasis has moved toward explainable mod-
els that allow users to understand, manage, and trust AI decisions 
[6]. Ultimately, it is important to find a way to assess the quality of 
human-AI symbiosis according to how it benefits humans. Achiev-
ing this objective requires human-centered design methods and 
techniques, fostering a multidisciplinary setting where AI and HCI 
researchers work together. Figure 1 represents the final objective of 
this research work in which the human and AI sides are considered 
together to evaluate SAI systems. 
3 Objectives and Research Questions 
The research work focuses primarily on improving the human-AI 
symbiotic relationship by suggesting solutions to evaluate the qual-
ity of SAI systems and the scientific validity of design techniques 
and interaction mechanisms. Specifically: 
• define an evaluation framework and novel metrics to evalu-
ate the symbiosis between humans and AI. 
• define new interaction mechanisms and user interfaces that 
align with these new needs. 
232


IUI Companion ’25, March 24–27, 2025, Cagliari, Italy Miriana Calvano 
Figure 1: UX and AI metrics’ role for the definition of SAI metrics 
• define transparency mechanisms to enforce SAI system’s 
behaviors; users must be allowed to easily comprehend the 
decisions of the system, even if they are not AI experts. 
The research questions (RQs) being investigated to achieve the 
previously presented objectives are as follows. 
• (RQ1) What are the existing challenges resulting from the 
intersection among Human-Computer Interaction (HCI) and 
Artificial Intelligence (AI)? How can these challenges be ad-
dressed? The first step of this work is to comprehend the 
well-established concepts and methodologies necessary to 
define instruments (e.g., guidelines, metrics, frameworks) 
to create high-quality SAI systems. A systematic literature 
review (SLR) was conducted to have an overall vision of the 
study context. Based on the results obtained, the specific 
characteristics of SAI are defined. 
• (RQ2) What are the limitations in existing metrics to evaluate 
the human-AI symbiosis? As a starting point, the existing 
literature was analysed to have an overall vision of how the 
well-known User Experience (UX) and AI metrics can be em-
ployed to assess AI and human performance. The collected 
information can be helpful in understanding how the exist-
ing elements can be integrated to define novel SAI metrics. 
• (RQ 3) How can the human-AI symbiotic relationship be eval-
uated? Novel metrics and evaluation framework will be de-
fined to evaluate the quality of the human-AI symbiotic 
relationship properly. 
4 Related Work 
Due to the definition of a new perspective in which HCI and AI are 
strictly connected, a new discipline was born: Human-Centered Ar-
tificial Intelligence (HCAI), which combines user experiences with 
embedded AI methods while balancing AI automation and human 
intervention [9]. This is ensured by SAI, which is a specialization of 
HCAI that aims to boost human-machine collaboration by enhanc-
ing human cognitive abilities through the interaction process [4]. 
One of the first times that the term symbiosis was used was in 1960, 
when Licklider J. stated that “Man (human)-computer symbiosis 
is an expected development in cooperative interaction between 
men (humans) and electronic computers” [8]. The symbiosis can be 
seen as the integration of two approaches: Augmented Intelligence, 
which aims to enhance the effectiveness of the decision-making 
process, and Human Intelligence for Artificial Intelligence (HI4AI), 
in which human intelligence serves as information feedback or as 
inspiration [7]. Symbiosis can be considered also as a consequence 
of the human-AI partnership, where human intelligence serves to 
improve AI processes and functionality and vice versa: it is a bidi-
rectional relationship of continuous exchange, similar to HI4AI [10]. 
In accordance with SAI philosophy, AI systems should be designed 
according to a human-centered approach, as developed within the 
HCI community, to foster the human-AI symbiotic relationship [5]. 
In this scenario, humans are considered in all of their dimensions, 
in terms of dignity, environment, needs, and ethics, to safeguard 
humans’ rights during the interaction process. For this reason, the 
AI Act proposed a human-centric approach, which ensures that hu-
man values are central to how AI systems are developed, deployed 
and used [3]. 
In the end, to reach the human-AI symbiosis, humans should 
trust and properly comprehend the AI model’s decisions, making 
trustworthiness one of the main properties to consider when dealing 
with such systems. Trustworthiness can be seen as the umbrella 
property to ensure a human-centric approach to AI [2]. 
5 Research Approach 
To design and develop high-quality SAI systems, the user must be 
included in all the phases of the creation process. In this section, 
the approaches it is intended to adopt to reach the objectives of 
this research project are described below. An approach to adopt 
refers to considering the user’s characteristics starting from the 
training phase of the AI model. By fully considering users from 
the beginning of the SAI system design, the system’s behavior can 
be easily adapted to their needs. User studies will be conducted to 
assess the validity of the proposed approach and gather additional 
information. It is necessary to define novel metrics concerning 
the SAI system’s properties. To reach this goal, the starting point 
of this research work is an SLR to understand whether and how 
humans are considered in the regulations that have to be referred 
to when creating SAI systems (i.e. the European AI Act). In the end, 
proper evaluation techniques will be applied to verify the validity 
of the gathered results (i.e., metrics and evaluation framework). In 
particular, the defined solutions will be assessed by performing 
studies with users; SAI systems’ user interfaces will be evaluated 
by performing usability studies and in-field studies to understand if 
these can be considered applicable and valid in real-world scenarios. 
233

Techniques and Methods to Evaluate Human-Centered Symbiotic AI Systems IUI Companion ’25, March 24–27, 2025, Cagliari, Italy 
6 Current State of the Work and Expected 
Results 
To have an overall understanding of the context of the study, an 
investigation of the literature was conducted. In this way, the basic 
concepts were acquired to represent a starting point for the research 
project. 
Due to the coming force of the European AI Act, an SLR was 
conducted to understand how humans are considered in this new 
scenario and what characteristics SAI systems should have to be 
legally compliant. Considering the obtained results, principles and 
properties that characterize SAI systems were defined. It emerged 
that aspects concerning the level of automation, protection of users 
from potential harms, transparency and fairness of AI decisions 
must be considered together with aspects concerning trustworthi-
ness, robustness and sustainability of AI. To validate these principles 
and properties, a user study performed on a web application em-
ployed in the medical field is being planned. In the end, to delineate 
the specific characteristics to consider when evaluating SAI sys-
tems, an SLR is being carried out. The obtained results will define a 
first set of metrics and framework to follow during the evaluation 
phase. 
In the end, the work plan of the research project encompassing 
the 3-years program is the following: Phase 1 concerns the activities 
related to studying the state of the art concerning SAI and related 
topics. In particular, it is important to study definitions and basic 
concepts, identify and analyze existing case studies, and evaluate 
solutions. Phase 2 concerns the activities related to the design and 
evaluation of symbiotic AI systems. The following activities will be 
performed: elicitation of users’ needs and definition of the technical 
methodology to follow; design of interaction paradigms that align 
with SAI systems’ characteristics; evaluation of SAI systems’ perfor-
mance through the defined metrics in order to assess their validity. 
Phase 3 concerns the activities related to the validity assessment of 
the proposed solutions and the writing of the PhD thesis. 
In the end, this contribution presents the main challenges and 
opportunities of this research project. Currently, I am at the be-
ginning of the second phase described in the work plan. Based 
on the gathered results, it is possible to state that humans are not 
widely considered regarding AI aspects. Therefore, the focus is on 
understanding how to fully consider the human during the entire 
life-cycle of SAI systems, from the definition of requirements to 
their evaluation. 
Acknowledgments 
The research Miriana Calvano is supported by the co-funding of the Euro-
pean Union - Next Generation EU: NRRP Initiative, Mission 4, Component 
2, Investment 1.3 – Partnerships extended to universities, research centers, 
companies, and research D.D. MUR n. 341 del 15.03.2022 – Next Generation 
EU (PE0000013 – “Future Artificial Intelligence Research – FAIR” - CUP: 
H97G22000210007). 
References 
[1] 2020. Artificial Intelligence (AI) Ethics: Ethics of AI and Ethical AI. 74-87 pages. 
doi:10.4018/JDM.2020040105 
[2] European Commission. 2021. European Commission - Ethics Guidelines for 
Trustworthy AI. https://ec.europa.eu/futurium/en/ai-alliance-consultation.1. 
html 
[3] The European Commission. 2024. Proposal for a Regulation Of The European 
Parliament And Of The Council Laying Down Harmonised Rules On Asrtificial 
Intelligence (Artificial Intelligence Act) And Amending Certain Union Legislative 
Acts. http://thomas.loc.gov/cgi-bin/query/z?c102:H.CON.RES.1.IH 
[4] Giuseppe Desolda, Andrea Esposito, Rosa Lanzilotti, Antonio Piccinno, and 
Maria F. Costabile. 2024. From human-centered to symbiotic artificial intel-
ligence: a focus on medical applications. Multimedia Tools and Applications (Nov. 
2024). doi:10.1007/s11042-024-20414-5 
[5] Scott S. Grigsby. 2018. Artificial Intelligence for Advanced Human-Machine 
Symbiosis. In Augmented Cognition: Intelligent Technologies, Dylan D. Schmorrow 
and Cali M. Fidopiastis (Eds.). Springer International Publishing, Cham, 255–266. 
[6] David Gunning and David W. Aha. 2019. DARPA’s Explainable Artificial Intelli-
gence Program. AI Magazine 40, 2 (2019), 44–58. doi:10.1609/aimag.v40i2.2850 
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1609/aimag.v40i2.2850 
[7] Davor Horvatić and Tomislav Lipic. 2021. Human-Centric AI: The Symbiosis of 
Human and Artificial Intelligence. Entropy 23, 3 (2021). doi:10.3390/e23030332 
[8] J. C. R. Licklider. 1960. Man-Computer Symbiosis. IRE Transactions on Human 
Factors in Electronics HFE-1, 1 (1960), 4–11. doi:10.1109/THFE2.1960.4503259 
[9] Ben Shneiderman. 2022. Human-Centered AI (1 ed.). Oxford University PressOx-
ford. doi:10.1093/oso/9780192845290.001.0001 
[10] Lina Zhou, Souren Paul, Haluk Demirkan, Lingyao Yuan, Jim Spohrer, and Julie 
Zhou, Michelle Basu. 2021. Intelligence Augmentation: Towards Building Human-
machine Symbiotic Relationship. AIS Transactions on Human-Computer Interac-
tion 13, 2 (2021), 243–264. doi:10.17705/1thci.00149 
234
