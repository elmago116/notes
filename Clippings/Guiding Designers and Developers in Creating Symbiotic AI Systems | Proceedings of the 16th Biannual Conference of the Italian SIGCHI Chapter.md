---
title: Guiding Designers and Developers in Creating Symbiotic AI Systems | Proceedings of the 16th Biannual Conference of the Italian SIGCHI Chapter
source: https://dl-acm-org.sire.ub.edu/doi/10.1145/3750069.3750095
author:
  - "[[Miriana Calvano]]"
  - "[[Antonio Curci]]"
  - "[[Rosa Lanzilotti]]"
published:
created: 2025-12-04
description:
tags:
  - design/hybrid-symbiosis
  - design/UX/Method
  - op/acc/leer
DOI: https://doi.org/10.1145/3750069.3750095
year: "2025"
apa_citation: Calvano, M. et. al. 2025
---
![[Guiding Designers and Developers in Creating Symbiotic AI Systems.pdf]]
## Abstract

AI is spreading in many fields influencing the way humans carry out activities. In this scenario, humans and AI collaborate fostering a bidirectional relationship where both parties are improved learning form each other. Thus, there is the need to create HCAI systems that consider humans not as mere users but in all of their dimensions to safeguard their fundamental rights while considering their needs, preferences and characteristics. SAI, which is a specialization of HCAI, refers to the creation of AI systems that empower and support humans rather than replacing them. Nevertheless, due to the influence of AI in contexts that can impact human lives and the environment surrounding them, it is important to create systems compliant with law (i.e., the European AI Act). This work, presents a set of guidelines that can guide practitioners to create high-quality and AI Act compliant SAI systems.

## 1 Introduction

The spread of Artificial Intelligence is having a huge impact of individuals’ daily lives changing the way we conduct activities and communicate with technology. AI is being integrated in many contexts—e.g., medicine, finance, agriculture—raising the need for more sophisticated systems that also enable individuals to understand the reasoning that lies behind their functioning, allowing them make informed decisions \[[4](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0004), [19](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0019)\]. Therefore, a new perspective, where Human Computer Interaction (HCI) and AI contaminate each other, should be adopted to create Human-Centered Artificial Intelligence (HCAI) systems that align with users’ needs and characteristics \[[27](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0027)\]. In this context, humans and AI collaborate to reach shared objectives fostering a bidirectional relationship in which they learn from each other while being empowered. These aspects are embodied in a branch of HCAI, called Symbiotic Artificial Intelligence, which refers to AI systems that are not perceived as mere tools, but support rather than replace humans allowing a mutual and continuous exchange to improve both parties over time \[[10](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0010)\]. To create high-quality Symbiotic Artificial Intelligence (SAI) systems, the Human-Centered Design (HCD) approach must be adopted complementing the techniques and methods belonging to the more technical and mathematical discipline of AI \[[17](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0017)\]. Due to the close relationship among AI and humans, when creating SAI systems, it is important to include their compliance with the current legal standards, ensuring the preservation of fundamental rights and environment surrounding them. In this regard, the European Union (EU) has released the AI Act, which is a legal framework that regulates the design, development, and use of AI across the EU to ensure safety, transparency, accountability, and ethicity of AI systems \[[13](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0013), [24](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0024)\]. It adopts a risk-based approach classifying AI systems according to their level of risk—high, limited, low, and minimal—which dictates requirements and obligations \[[13](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0013), [29](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0029)\].

The objective of this work is to present a set of guidelines to support practitioners in the creation of high-quality SAI systems that comply with legal standards. The guidelines were defined to provide an appropriate level of detail, while maintaining generality, to enable their application to a wide range of domains \[[11](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0011)\]. To better frame the context of this research, the guidelines are part of a three-layer framework that adopts a top-down approach to guide practitioners in the creation of law-compliant SAI systems. The three layers of the framework are: *Principles*, *Guidelines*, and *Success Criteria*, which become increasingly practical and pragmatic indications. Besides presenting a set of guidelines for each principle that characterize SAI, we explore the insights gathered from a preliminary validation study conducted to verify the comprehensibility and relevance of each guideline, and the protocol of a future extensive study.

The article is structured as follows: Section [3](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-3) provides an overview of the framework and details the guidelines for each principle; Section [4](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-4) reports the protocol for the user study to evaluate the comprehensibility, relevance, and feasibility of each guideline; Section [5](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-5) discusses the results of a preliminary validation that was performed with two experts; Section [6](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-6) draws the conclusions of the research and investigates its future work.

## 2 Related Work

The field of SAI has been gaining interest in the last few years, but the first time that the term “symbiosis” was used in the literature dates back to the 1960’s with Licklider. In this perspective, humans and AI are conceived as two parties that can collaborate and evolve together \[[22](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0022)\]. Thus, the design and development of SAI systems must be a collaborative effort among various disciplines that curate different aspects, all equal in relevance, of the same object \[[7](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0007), [10](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0010)\]. Ensuring that humans and AI can cooperate towards a common goal implies the establishment of specific interaction mechanisms that ensure that one can understand the other and make actions based off of the context \[[27](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0027)\]. At the same time, following the *human-centric* approach undertaken by the AI Act, it is important that humans remain at the core of the decision-making process. They must be able to intervene in the behavior of the system and exercise their agency \[[2](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0002)\]. Apart from the AI Act, there have been efforts to standardize these practices also by other regulatory bodies. Some examples are the “Ethical There are commonly known techniques in the literature that allow to reach these objectives \[[26](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0026)\]—e.g., Reinforcement Learning (RL) \[[28](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0028)\], Interactive Machine Learning (IML) \[[30](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0030)\]—, which provide strong technical support but if they are not inserted in the appropriate interaction mechanism that enables users to understand and exploit the full potential of the system, this might result in failures and wrong outcomes \[[32](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0032)\]. The HCAI domain, pioneered by Ben Shneiderman, highlights these aspects; it provides the theoretical foundations and the overall approach to undertake but without appropriate technical guidance with respect to the establishment of a symbiotic relationship \[[27](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0027)\]. In fact, as mentioned earlier, SAI is a subset of HCAI systems \[[10](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0010)\]. Thus, in order to move on from the system-centric perspective, the gap that this research aims at filling consists in standardizing and systematizing the approach that can guide designers and developers towards a *Symbiotic-by-design* system.

## 3 Guidelines to Create AI Act compliant SAI systems

This section presents the set of guidelines that will be integrated in the framework; they derive from four of the principles that characterize SAI—i.e., *Automation Level*, *Fairness*, *Protection*, and *Transparency* —which emerged from an on-going parallel study involving a Systematic Literature Review (SLR) performed following the Kitchenham’s protocol \[[21](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0021)\]. The latter had the objective of determining the principles of SAI systems that safeguard humans, avoiding risks, and complying with the AI Act.

The guidelines provide practitioners with a higher granularity with respect to functionalities and expected behaviors, considering humans in the interaction process \[[18](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0018), [25](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0025)\]. The guidelines were defined starting from principles, which aspects were detailed and further specialized to provide more concrete and specific instructions. Specifically, the description of principles was “transformed” into atomic sentences that can consider a more detailed description of each aspect covered by the principles, which are described as follows. *Transparency* aims to guarantee that AI systems can be overseen by humans, allowing them to interpret AI’s behavior and to receive explanations \[[16](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0016), [25](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0025)\]. *Fairness* concerns equality and inclusiveness in the AI system’s performance, avoiding discriminatory behaviors and ensuring that both humans and AI access rightful information \[[1](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0001), [31](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0031)\]. *Protection* highlights that humans must be protected from dangerous and misleading AI behaviors, guaranteeing privacy, security, and safety \[[23](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0023), [25](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0025)\]. *Automation Level* It refers to the implementation of appropriate human oversight or control, which allows humans to be either *on-* or *in-the-loop* \[[6](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0006), [20](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0020)\].

The specific guidelines are reported in the following paragraphs, appearing in the form: <Subject> must <obligation> <action> \[<motivation>\], and being grouped by principle. They are the final result of the preliminary validation study performed with two experts as described in [4](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-4). Some guidelines overlap among principles highlighting the multidisciplinary nature of symbiosis. In order to provide a more sound set of guidelines, they were written by two researchers and refined through a preliminary study in which other two researchers, with expertise in HCI and AI, were involved. This represents an initial activity that it is needed to conduct to prevent issue before applying these guidelines to a real-context scenario to assess the symbiosis of an artifact.  #themes/ethics 

- The human must be able to check, monitor, and supervise the AI system’s behavior, taking into account how it functions and the decisions it makes. (*Automation Level*, *Transparency*)
- The human must be enabled to assign proper meaning to the AI model’s outputs, whose presentation varies depending on task, processes, and structure to eventually modify its behavior. (*Transparency*, *Automation Level*)
- The human must be enabled to control the AI system’s behavior and functioning through proper interaction mechanisms. (*Transparency*, *Automation Level*)
- The human must be guided towards ethical behaviors when reconfiguring the AI model to avoid harms to both parties. (*Transparency*, *Fairness*, *Protection*)
- The human must not be manipulated by the AI system through persuasive behaviors unless they must be dissuaded against unethical intentions. (Protection, Fairness)
- The human must be allowed to retrieve accurate and reliable information from the AI system. (*Fairness*, *Automation Level*)
- The human must be aware that outputs generated by the AI system are not influenced by biases in the training data. (*Fairness*)
- The AI model must not discriminate humans based on their own characteristics unless necessary for specific, legitimate, and authorized tasks, oriented to the well-being of both all human beings and the environment surrounding them. (*Fairness*)
- The human must be informed about the AI processes and manages their data. (*Protection*)
- The AI system must fulfill its intended function without causing harm to living beings or the environment. (*Protection*)
- The AI system must preserve sensitive information, ensuring the accuracy of its data and operations, remaining available and resilient to attacks and capable of recovering from them. (*Protection*)

## 4 Evaluation Protocol

Assessing the guidelines is crucial to determine their validity in real-world scenarios and the extent to which they can be used by their target audience (i.e., specialists in HCI and AI). The evaluation and validation of the guidelines is divided in the two steps: the first has been completed, being necessary for an initial high-level refinement of the guidelines (see Section [5](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-5)) and the second, whose protocol is reported below, is more comprehensive and yet to be performed [4.2](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-4-2).

### 4.1 Preliminary Validation

The initial set of guidelines are submitted to the judgment of two experts in HCI and AI to filter out high-level flaws and ambiguities. These experts are part of the research team, but they do not intervene in the process of either writing or refining the guidelines. Thus, after the definition of a stable set, this preliminary validation aims to determining the comprehensibility and relevance of the guidelines to detect problems that could distract the participants of the future comprehensive study, potentially interfering with its results. This evaluation is performed through a form with three questions per guideline concerning the following aspects: *Comprehensibility*, *Relevance*, and *Comments*. The first two questions have Likert-scale answers and the third gave them the possibility of providing comments to improve parts of the guidelines’ statements. The first two criteria will also be part of the extensive study and are better detailed in Section [4.2](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-4-2). Afterwards, their answers and comments are analyzed and the guidelines refined, grounding the observations in the literature.

### 4.2 Extensive Study

This part of the evaluation protocol has the objective of gaining more broad and comprehensive insights that are more vertical for each guideline. The entire set of guidelines is tested in terms of comprehensibility, relevance, and feasibility with respect to the target audience of the framework. Since SAI is a result from the convergence of different disciplines, especially HCI and AI, the participants of the study will be required to possess expertise in these two fields. This study is designed to include a number of participants that ranges from 20 to 30, gathering an appropriate amount of feedback and perspectives to obtain rich insights with respect to the validity of the proposed solution. The guidelines are assessed through a questionnaire, explored below, which investigates three main criteria:

- **Comprehensibility**: the extent to which individuals can easily understand the meaning of the guideline.
- **Relevance**: the extent to which it is important to consider the specific guideline with respect to the establishment of a symbiotic relationship while not undermining the system’s functionalities.
- **Feasibility**: the extent to which the guideline can be applied to an system’s User Interface (UI) and functionalities.

To assess their applicability and provide more context to the participants, examples are provided in terms of use cases, scenarios, or UIs. They will not be mere screenshots of UIs that belong to SAI systems, but they can also be exemplary interaction paradigms, or architectures. The three criteria will appear to the participant as a question with a Likert-scale answer. After these three steps, it will be possible to provide extra suggestions for each guideline and/or for the group of guidelines for each principle through a *Comments* section. An example of question is illustrated in Figure [1](https://dl-acm-org.sire.ub.edu/doi/10.1145/#fig1), which shows the three criteria and the exemplary UI given for the guideline (G1.3). We highlight that the examples provided to the participants will belong to the set of SAI, being grounded in the literature and/or tested with end-users, in order to ensure soundness. In Figure [1](https://dl-acm-org.sire.ub.edu/doi/10.1145/#fig1), we used an AI system for the medical field—rhinocytology \[[14](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0014)\]—to support professionals in classifying cells and detecting abnormalities \[[9](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0009)\].

![](https://dl-acm-org.sire.ub.edu/cms/10.1145/3750069.3750095/asset/24c0e488-339d-4ecc-8274-cd7ce9a0a49b/assets/images/large/chitaly2025-26-fig1.jpg)

Example of the structure of the questionnaire to evaluate each guideline with respect to the three criteria and an example \[ 9 \]

## 5 Discussions and Preliminary Findings

This section presents the insights that emerged from the preliminary evaluation for the refinement of the initial set of guidelines reported in [3](https://dl-acm-org.sire.ub.edu/doi/10.1145/#sec-3). The two researchers, named *R1* and *R2* for anonymity reasons, raised important issues and highlighted interesting points with respect to the clarity of the sentences, the contents of the guidelines, and their utility. After grounding them in the literature, these insights brought to the refinement and modification of 4 guidelines out of 16, as explored below. Although not particularly statistically relevant because of the limited sample, the average scores for the two questions are reported for completeness: *Comprehensibility* scored an average of 4.68/5 and *Relevance* scored 4.58/5.

The original version of (G5) stated *“The human must not be manipulated by the AI system through persuasive or deceptive behaviors”*, which raised a strong ethical/philosophical issue that lies in the fact that “persuasion may be useful when humans want to act unethically and the AI needs to “dissuade” them”, as stated by R2 \[[3](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0003)\]. The same researcher also added that mentioning persuasion with deception in this case could lead to confusion or lack of clarity. Thus, recognizing that such situations could occur, the guideline was modified accordingly.

Similar considerations were made for (G9), which stated as follows in its previous version *“The human must not be subjected to discriminatory behavior based on their own characteristics (e.g. ethnicity, gender, age) by the AI system”*. R2 highlighted that there can be situations in which such characteristics could be important for the completion of tasks, for example, with the detection of illnesses that affect people who live in specific areas of the world because of the environment in which they live in or because of their genetic background. It was also noted that the structure of this guideline could come across as confusing since, in this case, “humans” were the object of the sentence and not its subject, bringing the need for its modification.

Referring to (G12), which originally stated that *“The AI system must preserve the Confidentiality, Integrity, and Availability, being resilient against attacks, enabling recovery from them”*, R2 stated that “The CIA triad (i.e., Confidentiality, Integrity, and Availability) may not be known and these concepts are not defined in the guideline, making it impossible to understand to other people”. Considering this comment, the guideline, was modified by including the concepts of the CIA Triad and not the mere extended acronym.

There was an additional guideline for the *Protection* principle which stated: *“The AI model must be trained on data that designers and developers have permission to elaborate”*. It was removed from the set of guidelines because it is not relevant for the human-AI symbiosis, but it is more centered on a legal perspective. Specifically, R1 commented “I think the guideline is very important. Certainly, the user will appreciate knowing that the developers had permission to work with the data, but in my opinion the guidelines do not affect the symbiotic relationship”, and R2 “This does not feel important for the relationship with its users. This is more shifted towards just pure "legality" of the deployment, and is not a concern for the end-users like other guidelines”.

## 6 Conclusions and Future Work

Building SAI is a complex task which requires a multidisciplinary approach, considering humans in all of their dimensions \[[10](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0010), [12](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0012)\]. This research proposes a set of guidelines to create SAI systems following the main characteristics that allow the achievement of human-AI symbiosis. The guidelines, which possess a high-level of generality, have the goal of supporting designers and developers in establishing proper interaction mechanisms while considering the obligations that the AI Act sets. The guidelines are planned to be extensively tested and evaluated in terms of comprehensibility, relevance, and feasibility. In this manuscript, we present the results of a preliminary validation study was performed on the first stable set of guidelines, performed with two experts in HCI and AI, which highlighted the importance of clear statements that are self-explanatory and that reflect the multidisciplinary of symbiosis, bringing to the modification of some guidelines. This research lays the groundwork for the construction of a framework to provide more concrete and detailed guidance to designers and developers, expanding the guidelines to success criteria and design patterns. Although the latter is the final objective, the next steps will concern the execution of the comprehensive study, whose protocol was presented in this manuscript, and refining the guidelines based on its result. In order to refine the guidelines, they are being applied to some case studies that are ongoing, concerning the use of the framework to build AI systems for the field of medicine \[[5](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0005), [8](https://dl-acm-org.sire.ub.edu/doi/10.1145/#core-collateral-Bib0008)\]

## Acknowledgments

The research of Rosa Lanzilotti, Miriana Calvano, and Antonio Curci is supported by the co-funding of the European Union - Next Generation EU: NRRP Initiative, Mission 4, Component 2, Investment 1.3 – Partnerships extended to universities, research centers, companies, and research D.D. MUR n. 341 del 15.03.2022 – Next Generation EU (PE0000013 – “Future Artificial Intelligence Research – FAIR” - CUP: H97G22000210007).

[View full text](https://dl-acm-org.sire.ub.edu/doi/full/10.1145/3750069.3750095) | [Download PDF](https://dl-acm-org.sire.ub.edu/doi/pdf/10.1145/3750069.3750095?download=true)

## PDF text extraction

Guiding Designers and Developers in Creating Symbiotic AI 
Systems 
Miriana Calvano 
Department of Computer Science 
University of Bari Aldo Moro 
Bari, Italy 
miriana.calvano@uniba.it 
Rosa Lanzilotti 
Department of Computer Science 
University of Bari Aldo Moro 
Bari, Italy 
rosa.lanzilotti@uniba.it 
Abstract 
AI is spreading in many felds infuencing the way humans carry 
out activities. In this scenario, humans and AI collaborate foster-
ing a bidirectional relationship where both parties are improved 
learning form each other. Thus, there is the need to create HCAI 
systems that consider humans not as mere users but in all of their 
dimensions to safeguard their fundamental rights while consider-
ing their needs, preferences and characteristics. SAI, which is a 
specialization of HCAI, refers to the creation of AI systems that 
empower and support humans rather than replacing them. Nev-
ertheless, due to the infuence of AI in contexts that can impact 
human lives and the environment surrounding them, it is important 
to create systems compliant with law (i.e., the European AI Act). 
This work, presents a set of guidelines that can guide practitioners 
to create high-quality and AI Act compliant SAI systems. 
CCS Concepts 
• Human-centered computing → HCI design and evaluation 
methods. 
Keywords 
Symbiotic Artifcial Intelligence (SAI), Artifcial Intelligence (AI) 
Act, Guidelines, User Study 
ACM Reference Format: 
Miriana Calvano, Antonio Curci, Rosa Lanzilotti, and Antonio Piccinno. 
2025. Guiding Designers and Developers in Creating Symbiotic AI Systems. 
In CHItaly 2025: 16th Biannual Conference of the Italian SIGCHI Chapter 
(CHItaly 2025), October 06–10, 2025, Salerno, Italy. ACM, New York, NY, USA, 
5 pages. https://doi.org/10.1145/3750069.3750095 
This work is licensed under a Creative Commons Attribution 4.0 International License. 
CHItaly 2025, Salerno, Italy 
© 2025 Copyright held by the owner/author(s). 
ACM ISBN 979-8-4007-2102-1/25/10 
https://doi.org/10.1145/3750069.3750095 
Antonio Curci 
Department of Computer Science 
University of Bari Aldo Moro 
Bari, Italy 
Department of Computer Science 
University of Pisa 
Pisa, Italy 
antonio.curci@uniba.it 
Antonio Piccinno 
Department of Computer Science 
University of Bari Aldo Moro 
Bari, Italy 
antonio.piccinno@uniba.it 
1 Introduction 
The spread of Artifcial Intelligence is having a huge impact of 
individuals’ daily lives changing the way we conduct activities 
and communicate with technology. AI is being integrated in many 
contexts—e.g., medicine, fnance, agriculture—raising the need for 
more sophisticated systems that also enable individuals to under-
stand the reasoning that lies behind their functioning, allowing 
them make informed decisions [4, 19]. Therefore, a new perspec-
tive, where Human Computer Interaction (HCI) and AI contaminate 
each other, should be adopted to create Human-Centered Artif-
cial Intelligence (HCAI) systems that align with users’ needs and 
characteristics [27]. In this context, humans and AI collaborate to 
reach shared objectives fostering a bidirectional relationship in 
which they learn from each other while being empowered. These 
aspects are embodied in a branch of HCAI, called Symbiotic Artif-
cial Intelligence, which refers to AI systems that are not perceived 
as mere tools, but support rather than replace humans allowing a 
mutual and continuous exchange to improve both parties over time 
[10]. To create high-quality Symbiotic Artifcial Intelligence (SAI) 
systems, the Human-Centered Design (HCD) approach must be 
adopted complementing the techniques and methods belonging to 
the more technical and mathematical discipline of AI [17]. Due to 
the close relationship among AI and humans, when creating SAI 
systems, it is important to include their compliance with the current 
legal standards, ensuring the preservation of fundamental rights 
and environment surrounding them. In this regard, the European 
Union (EU) has released the AI Act, which is a legal framework 
that regulates the design, development, and use of AI across the 
EU to ensure safety, transparency, accountability, and ethicity of 
AI systems [13, 24]. It adopts a risk-based approach classifying AI 
systems according to their level of risk—high, limited, low, and 
minimal—which dictates requirements and obligations [13, 29]. 
The objective of this work is to present a set of guidelines to 
support practitioners in the creation of high-quality SAI systems 
that comply with legal standards. The guidelines were defned to 
provide an appropriate level of detail, while maintaining generality, 


CHItaly 2025, October 06–10, 2025, Salerno, Italy Miriana Calvano, Antonio Curci, Rosa Lanziloti, and Antonio Piccinno 
to enable their application to a wide range of domains [11]. To 
better frame the context of this research, the guidelines are part 
of a three-layer framework that adopts a top-down approach to 
guide practitioners in the creation of law-compliant SAI systems. 
The three layers of the framework are: Principles, Guidelines, and 
Success Criteria, which become increasingly practical and pragmatic 
indications. Besides presenting a set of guidelines for each princi-
ple that characterize SAI, we explore the insights gathered from a 
preliminary validation study conducted to verify the comprehensi-
bility and relevance of each guideline, and the protocol of a future 
extensive study. 
The article is structured as follows: Section 3 provides an overview 
of the framework and details the guidelines for each principle; Sec-
tion 4 reports the protocol for the user study to evaluate the com-
prehensibility, relevance, and feasibility of each guideline; Section 5 
discusses the results of a preliminary validation that was performed 
with two experts; Section 6 draws the conclusions of the research 
and investigates its future work. 
2 Related Work 
The feld of SAI has been gaining interest in the last few years, but 
the frst time that the term “symbiosis” was used in the literature 
dates back to the 1960’s with Licklider. In this perspective, humans 
and AI are conceived as two parties that can collaborate and evolve 
together [22]. Thus, the design and development of SAI systems 
must be a collaborative efort among various disciplines that curate 
diferent aspects, all equal in relevance, of the same object [7, 10]. 
Ensuring that humans and AI can cooperate towards a common goal 
implies the establishment of specifc interaction mechanisms that 
ensure that one can understand the other and make actions based 
of of the context [27]. At the same time, following the human-
centric approach undertaken by the AI Act, it is important that 
humans remain at the core of the decision-making process. They 
must be able to intervene in the behavior of the system and exercise 
their agency [2]. Apart from the AI Act, there have been eforts to 
standardize these practices also by other regulatory bodies. Some 
examples are the “Ethical There are commonly known techniques 
in the literature that allow to reach these objectives [26]—e.g., Rein-
forcement Learning (RL) [28], Interactive Machine Learning (IML) 
[30]—, which provide strong technical support but if they are not 
inserted in the appropriate interaction mechanism that enables 
users to understand and exploit the full potential of the system, 
this might result in failures and wrong outcomes [32]. The HCAI 
domain, pioneered by Ben Shneiderman, highlights these aspects; 
it provides the theoretical foundations and the overall approach to 
undertake but without appropriate technical guidance with respect 
to the establishment of a symbiotic relationship [27]. In fact, as men-
tioned earlier, SAI is a subset of HCAI systems [10]. Thus, in order 
to move on from the system-centric perspective, the gap that this 
research aims at flling consists in standardizing and systematizing 
the approach that can guide designers and developers towards a 
Symbiotic-by-design system. 
3 Guidelines to Create AI Act compliant SAI 
systems 
This section presents the set of guidelines that will be integrated 
in the framework; they derive from four of the principles that 
characterize SAI—i.e., Automation Level, Fairness, Protection, and 
Transparency—which emerged from an on-going parallel study in-
volving a Systematic Literature Review (SLR) performed following 
the Kitchenham’s protocol [21]. The latter had the objective of 
determining the principles of SAI systems that safeguard humans, 
avoiding risks, and complying with the AI Act. 
The guidelines provide practitioners with a higher granularity 
with respect to functionalities and expected behaviors, considering 
humans in the interaction process [18, 25]. The guidelines were 
defned starting from principles, which aspects were detailed and 
further specialized to provide more concrete and specifc instruc-
tions. Specifcally, the description of principles was “transformed” 
into atomic sentences that can consider a more detailed description 
of each aspect covered by the principles, which are described as 
follows. Transparency aims to guarantee that AI systems can be 
overseen by humans, allowing them to interpret AI’s behavior and 
to receive explanations [16, 25]. Fairness concerns equality and 
inclusiveness in the AI system’s performance, avoiding discrimi-
natory behaviors and ensuring that both humans and AI access 
rightful information [1, 31]. Protection highlights that humans must 
be protected from dangerous and misleading AI behaviors, guar-
anteeing privacy, security, and safety [23, 25]. Automation Level It 
refers to the implementation of appropriate human oversight or 
control, which allows humans to be either on- or in-the-loop [6, 20]. 
The specifc guidelines are reported in the following paragraphs, 
appearing in the form: <Subject> must <obligation> <action> [<mo-
tivation>], and being grouped by principle. They are the fnal result 
of the preliminary validation study performed with two experts as 
described in 4. Some guidelines overlap among principles highlight-
ing the multidisciplinary nature of symbiosis. In order to provide a 
more sound set of guidelines, they were written by two researchers 
and refned through a preliminary study in which other two re-
searchers, with expertise in HCI and AI, were involved. This rep-
resents an initial activity that it is needed to conduct to prevent 
issue before applying these guidelines to a real-context scenario to 
assess the symbiosis of an artifact. 
G1 The human must be able to check, monitor, and supervise the 
AI system’s behavior, taking into account how it functions 
and the decisions it makes. (Automation Level, Transparency) 
G2 The human must be enabled to assign proper meaning to the 
AI model’s outputs, whose presentation varies depending 
on task, processes, and structure to eventually modify its 
behavior. (Transparency, Automation Level) 
G3 The human must be enabled to control the AI system’s behav-
ior and functioning through proper interaction mechanisms. 
(Transparency, Automation Level) 
G4 The human must be guided towards ethical behaviors when 
reconfguring the AI model to avoid harms to both parties. 
(Transparency, Fairness, Protection) 
G5 The human must not be manipulated by the AI system through 
persuasive behaviors unless they must be dissuaded against 
unethical intentions. (Protection, Fairness) 

Guiding Designers and Developers in Creating Symbiotic AI Systems CHItaly 2025, October 06–10, 2025, Salerno, Italy 
G6 The human must be guaranteed privacy by the AI system, 
safeguarding sensitive data from improper access, theft, or 
loss. (Protection) 
G7 The human must be allowed to retrieve accurate and reliable 
information from the AI system. (Fairness, Automation Level) 
G8 The human must be aware that outputs generated by the 
AI system are not infuenced by biases in the training data. 
(Fairness) 
G9 The AI model must not discriminate humans based on their 
own characteristics unless necessary for specifc, legitimate, 
and authorized tasks, oriented to the well-being of both 
all human beings and the environment surrounding them. 
(Fairness) 
G10 The human must be informed about the AI processes and 
manages their data. (Protection) 
G11 The AI system must fulfll its intended function without caus-
ing harm to living beings or the environment. (Protection) 
G12 The AI system must preserve sensitive information, ensuring 
the accuracy of its data and operations, remaining available 
and resilient to attacks and capable of recovering from them. 
(Protection) 
4 Evaluation Protocol 
Assessing the guidelines is crucial to determine their validity in real-
world scenarios and the extent to which they can be used by their 
target audience (i.e., specialists in HCI and AI). The evaluation and 
validation of the guidelines is divided in the two steps: the frst has 
been completed, being necessary for an initial high-level refnement 
of the guidelines (see Section 5) and the second, whose protocol is 
reported below, is more comprehensive and yet to be performed 
4.2. 
4.1 Preliminary Validation 
The initial set of guidelines are submitted to the judgment of two 
experts in HCI and AI to flter out high-level faws and ambigui-
ties. These experts are part of the research team, but they do not 
intervene in the process of either writing or refning the guidelines. 
Thus, after the defnition of a stable set, this preliminary validation 
aims to determining the comprehensibility and relevance of the 
guidelines to detect problems that could distract the participants 
of the future comprehensive study, potentially interfering with its 
results. This evaluation is performed through a form with three 
questions per guideline concerning the following aspects: Com-
prehensibility, Relevance, and Comments. The frst two questions 
have Likert-scale answers and the third gave them the possibility of 
providing comments to improve parts of the guidelines’ statements. 
The frst two criteria will also be part of the extensive study and 
are better detailed in Section 4.2. Afterwards, their answers and 
comments are analyzed and the guidelines refned, grounding the 
observations in the literature. 
4.2 Extensive Study 
This part of the evaluation protocol has the objective of gaining 
more broad and comprehensive insights that are more vertical for 
each guideline. The entire set of guidelines is tested in terms of 
comprehensibility, relevance, and feasibility with respect to the 
target audience of the framework. Since SAI is a result from the 
convergence of diferent disciplines, especially HCI and AI, the par-
ticipants of the study will be required to possess expertise in these 
two felds. This study is designed to include a number of partici-
pants that ranges from 20 to 30, gathering an appropriate amount 
of feedback and perspectives to obtain rich insights with respect to 
the validity of the proposed solution. The guidelines are assessed 
through a questionnaire, explored below, which investigates three 
main criteria: 
(1) Comprehensibility: the extent to which individuals can 
easily understand the meaning of the guideline. 
(2) Relevance: the extent to which it is important to consider 
the specifc guideline with respect to the establishment of a 
symbiotic relationship while not undermining the system’s 
functionalities. 
(3) Feasibility: the extent to which the guideline can be applied 
to an system’s User Interface (UI) and functionalities. 
To assess their applicability and provide more context to the 
participants, examples are provided in terms of use cases, scenarios, 
or UIs. They will not be mere screenshots of UIs that belong to 
SAI systems, but they can also be exemplary interaction paradigms, 
or architectures. The three criteria will appear to the participant 
as a question with a Likert-scale answer. After these three steps, 
it will be possible to provide extra suggestions for each guideline 
and/or for the group of guidelines for each principle through a 
Comments section. An example of question is illustrated in Fig-
ure 1, which shows the three criteria and the exemplary UI given 
for the guideline (G1.3). We highlight that the examples provided 
to the participants will belong to the set of SAI, being grounded 
in the literature and/or tested with end-users, in order to ensure 
soundness. In Figure 1, we used an AI system for the medical feld— 
rhinocytology [14]—to support professionals in classifying cells 
and detecting abnormalities [9]. 
5 Discussions and Preliminary Findings 
This section presents the insights that emerged from the prelimi-
nary evaluation for the refnement of the initial set of guidelines 
reported in 3. The two researchers, named R1 and R2 for anonymity 
reasons, raised important issues and highlighted interesting points 
with respect to the clarity of the sentences, the contents of the guide-
lines, and their utility. After grounding them in the literature, these 
insights brought to the refnement and modifcation of 4 guidelines 
out of 16, as explored below. Although not particularly statistically 
relevant because of the limited sample, the average scores for the 
two questions are reported for completeness: Comprehensibility 
scored an average of 4.68/5 and Relevance scored 4.58/5. 
(G2) previously stated that “The human must be enabled to assign 
proper meaning to the AI model’s outputs, processes, and structure to 
eventually modify its behavior”. In this regard, R2 commented that 
the it was unclear whether the word “output” referred to the actual 
presentation of the AI response or something more profound. The 
guideline was modifed accordingly, specifying that the word refers 
to the presentation of the AI response [15]. There are terms that 
could be interpreted in diferent ways, depending on the expertise 
and technical background of those who read them. 

CHItaly 2025, October 06–10, 2025, Salerno, Italy Miriana Calvano, Antonio Curci, Rosa Lanziloti, and Antonio Piccinno 
Figure 1: Example of the structure of the questionnaire to evaluate each guideline with respect to the three criteria and an 
example [9] 
The original version of (G5) stated “The human must not be ma-
nipulated by the AI system through persuasive or deceptive behaviors”, 
which raised a strong ethical/philosophical issue that lies in the 
fact that “persuasion may be useful when humans want to act un-
ethically and the AI needs to “dissuade” them”, as stated by R2 [3]. 
The same researcher also added that mentioning persuasion with 
deception in this case could lead to confusion or lack of clarity. 
Thus, recognizing that such situations could occur, the guideline 
was modifed accordingly. 
Similar considerations were made for (G9), which stated as fol-
lows in its previous version “The human must not be subjected to 
discriminatory behavior based on their own characteristics (e.g. eth-
nicity, gender, age) by the AI system”. R2 highlighted that there can 
be situations in which such characteristics could be important for 
the completion of tasks, for example, with the detection of illnesses 
that afect people who live in specifc areas of the world because of 
the environment in which they live in or because of their genetic 
background. It was also noted that the structure of this guideline 
could come across as confusing since, in this case, “humans” were 
the object of the sentence and not its subject, bringing the need for 
its modifcation. 
Referring to (G12), which originally stated that “The AI system 
must preserve the Confdentiality, Integrity, and Availability, being 
resilient against attacks, enabling recovery from them”, R2 stated that 
“The CIA triad (i.e., Confdentiality, Integrity, and Availability) may 
not be known and these concepts are not defned in the guideline, 
making it impossible to understand to other people”. Considering 
this comment, the guideline, was modifed by including the concepts 
of the CIA Triad and not the mere extended acronym. 
There was an additional guideline for the Protection principle 
which stated: “The AI model must be trained on data that designers 
and developers have permission to elaborate”. It was removed from 
the set of guidelines because it is not relevant for the human-AI 
symbiosis, but it is more centered on a legal perspective. Specifcally, 
R1 commented “I think the guideline is very important. Certainly, 
the user will appreciate knowing that the developers had permission 
to work with the data, but in my opinion the guidelines do not afect 
the symbiotic relationship”, and R2 “This does not feel important 
for the relationship with its users. This is more shifted towards 
just pure "legality" of the deployment, and is not a concern for the 
end-users like other guidelines”. 
6 Conclusions and Future Work 
Building SAI is a complex task which requires a multidisciplinary 
approach, considering humans in all of their dimensions [10, 12]. 
This research proposes a set of guidelines to create SAI systems 
following the main characteristics that allow the achievement of 
human-AI symbiosis. The guidelines, which possess a high-level of 
generality, have the goal of supporting designers and developers 
in establishing proper interaction mechanisms while considering 
the obligations that the AI Act sets. The guidelines are planned 
to be extensively tested and evaluated in terms of comprehensibil-
ity, relevance, and feasibility. In this manuscript, we present the 
results of a preliminary validation study was performed on the frst 
stable set of guidelines, performed with two experts in HCI and 
AI, which highlighted the importance of clear statements that are 
self-explanatory and that refect the multidisciplinary of symbiosis, 
bringing to the modifcation of some guidelines. This research lays 
the groundwork for the construction of a framework to provide 
more concrete and detailed guidance to designers and developers, 
expanding the guidelines to success criteria and design patterns. 
Although the latter is the fnal objective, the next steps will concern 
the execution of the comprehensive study, whose protocol was 
presented in this manuscript, and refning the guidelines based on 
its result. In order to refne the guidelines, they are being applied 
to some case studies that are ongoing, concerning the use of the 
framework to build AI systems for the feld of medicine [5, 8] 
Acknowledgments 
The research of Rosa Lanzilotti, Miriana Calvano, and Antonio 
Curci is supported by the co-funding of the European Union - Next 
Generation EU: NRRP Initiative, Mission 4, Component 2, Invest-
ment 1.3 – Partnerships extended to universities, research centers, 

Guiding Designers and Developers in Creating Symbiotic AI Systems 
companies, and research D.D. MUR n. 341 del 15.03.2022 – Next Gen-
eration EU (PE0000013 – “Future Artifcial Intelligence Research – 
FAIR” - CUP: H97G22000210007). 
References 
[1] Sebastian Biewer, Kevin Baum, Sarah Sterz, Holger Hermanns, Sven Hetmank, 
Markus Langer, Anne Lauber-Rönsberg, and Franz Lehr. 2024. Software Doping 
Analysis for Human Oversight. Formal Methods in System Design (April 2024). 
doi:10.1007/s10703-024-00445-2 
[2] Federico Bomba, María Menéndez-Blanco, Paolo Grigis, Michele Cremaschi, 
and Antonella De Angeli. 2024. The Choreographer-Performer Continuum: A 
Difraction Tool to Illuminate Authorship in More Than Human Co-Performances. 
ACM Transactions on Computer-Human Interaction 31, 6 (Dec. 2024), 1–23. doi:10. 
1145/3689040 Publisher: Association for Computing Machinery (ACM). 
[3] Marietjie Botes. 2023. Autonomy and the social dilemma of online manipulative 
behavior. AI and Ethics 3, 1 (Feb. 2023), 315–323. doi:10.1007/s43681-022-00157-5 
[4] Francisco Maria Calisto, João Fernandes, Margarida Morais, Carlos Santi-
ago, João Maria Abrantes, Nuno Nunes, and Jacinto C. Nascimento. 2023. 
Assertiveness-based agent communication for a personalized medicine on medi-
cal imaging diagnosis. In Proceedings of the 2023 CHI conference on human factors 
in computing systems (Chi ’23). Association for Computing Machinery, New York, 
NY, USA. doi:10.1145/3544548.3580682 Number of pages: 20 Place: Hamburg, 
Germany tex.articleno: 13. 
[5] Miriana Calvano, Antonio Curci, Andrea Esposito, Rosa Lanzillotti, Antonio 
Piccinno, and Alfonso Pio Pretorino. 2025. Leveraging Emotion Recognition to 
Power Adaptability for More Efective Speech Therapies. In Joint Proceedings of 
IS-EUD 2025: 10th International Symposium on End-User Development, Vol. Vol-
3978. CEUR Workshop Proceedings, Munich, Germany. https://ceur-ws.org/Vol-
3978/short-s2-05.pdf 
[6] Joana Covelo De Abreu. 2024. The “Artifcial Intelligence Act” Proposal on 
European e-Justice Domains Through the Lens of User-Focused, User-Friendly 
and Efective Judicial Protection Principles. In Multidisciplinary Perspectives 
on Artifcial Intelligence and the Law, Henrique Sousa Antunes, Pedro Miguel 
Freitas, Arlindo L. Oliveira, Clara Martins Pereira, Elsa Vaz De Sequeira, and Luís 
Barreto Xavier (Eds.). Vol. 58. Springer International Publishing, Cham, 397–414. 
doi:10.1007/978-3-031-41264-6_21 
[7] Antonio Curci. 2024. A Comprehensive Framework Proposal to Design Symbiotic 
AI Systems. In Proceedings of the 28th International Conference on Evaluation and 
Assessment in Software Engineering. ACM, Salerno Italy, 460–465. doi:10.1145/ 
3661167.3661219 
[8] Antonio Curci and Andrea Esposito. 2024. Detecting Brain Tumors Through Mul-
timodal Neural Networks. In 13th International Conference on Pattern Recognition 
Applications and Methods. SCITEPRESS – Science and Technology Publications, 
Lda., Rome, Italy, 995–1000. doi:10.5220/0012608600003654 
[9] Giuseppe Desolda, Giovanni Dimauro, Andrea Esposito, Rosa Lanzilotti, Maris-
tella Matera, and Massimo Zancanaro. 2024. A Human–AI interaction paradigm 
and its application to rhinocytology. Artifcial Intelligence in Medicine 155 (Sept. 
2024), 102933. doi:10.1016/j.artmed.2024.102933 
[10] Giuseppe Desolda, Andrea Esposito, Rosa Lanzilotti, Antonio Piccinno, and 
Maria F. Costabile. 2024. From human-centered to symbiotic artifcial intel-
ligence: a focus on medical applications. Multimedia Tools and Applications (Nov. 
2024). doi:10.1007/s11042-024-20414-5 
[11] Alan Dix (Ed.). 2004. Human-computer interaction (3rd ed ed.). Pearson/Prentice-
Hall, Harlow, England ; New York. 
[12] Alan Dix, Matt Roach, Tommaso Turchi, Alessio Malizia, and Ben Wilson. 
2024. Designing and building hybrid human-AI systems (SYNERGY 2024). 
In Proceedings of the 2024 international conference on advanced visual inter-
faces (Avi ’24). Association for Computing Machinery, New York, NY, USA. 
doi:10.1145/3656650.3660537 Number of pages: 4 Place: Arenzano, Genoa, Italy 
tex.articleno: 122. 
[13] European Parliament and Council of the European Union. 2024. Regulation of 
the European Parliament and of the Council Laying down Harmonised Rules 
on Artifcial Intelligence and Amending Regulations (EC) No 300/2008, (EU) No 
167/2013, (EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and 
Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828 (Artifcial Intelligence 
Act). 
[14] Matteo Gelardi and John F. Pallanch. 2012. Atlas of nasal cytology for the dif-
ferential diagnosis of nasal diseases (2nd ed ed.). Edi. Ermes, New York. OCLC: 
932224272. 
[15] Riccardo Guidotti, Anna Monreale, Dino Pedreschi, and Fosca Giannotti. 2021. 
Principles of Explainable Artifcial Intelligence. In Explainable AI Within the 
Digital Transformation and Cyber Physical Systems, Moamar Sayed-Mouchaweh 
(Ed.). Springer International Publishing, Cham, 9–31. doi:10.1007/978-3-030-
76409-8_2 
[16] Balint Gyevnar, Nick Ferguson, and Burkhard Schafer. 2023. Bridging the Trans-
parency Gap: What Can Explainable AI Learn from the AI Act? In Frontiers in 
CHItaly 2025, October 06–10, 2025, Salerno, Italy 
Artifcial Intelligence and Applications, Kobi Gal, Ann Nowé, Grzegorz J. Nalepa, 
Roy Fairstein, and Roxana Rădulescu (Eds.). IOS Press. doi:10.3233/FAIA230367 
[17] Maria Hartikainen, Kaisa Väänänen, Anu Lehtiö, Saara Ala-Luopa, and Thomas 
Olsson. 2022. Human-Centered AI Design in Reality: A Study of Developer 
Companies’ Practices: A study of Developer Companies’ Practices. In Nordic 
Human-Computer Interaction Conference. ACM, Aarhus Denmark, 1–11. doi:10. 
1145/3546155.3546677 
[18] High Level Expert Group on Artifcial Intelligence. 2020. Assessment List for 
Trustworthy Artifcial Intelligence (ALTAI) for Self-Assessment. 
[19] Mohammad Hossein Jarrahi. 2018. Artifcial intelligence and the future of work: 
Human-AI symbiosis in organizational decision making. Business Horizons 61, 4 
(July 2018), 577–586. doi:10.1016/j.bushor.2018.03.007 
[20] Peter Kieseberg, Edgar Weippl, A. Min Tjoa, Federico Cabitza, Andrea Campagner, 
and Andreas Holzinger. 2023. Controllable AI - An Alternative to Trustworthiness 
in Complex AI Systems? In Machine Learning and Knowledge Extraction, Andreas 
Holzinger, Peter Kieseberg, Federico Cabitza, Andrea Campagner, A Min Tjoa, 
and Edgar Weippl (Eds.). Vol. 14065. Springer Nature Switzerland, Cham, 1–12. 
doi:10.1007/978-3-031-40837-3_1 
[21] Barbara Kitchenham. 2004. Procedures for Performing Systematic Reviews. 
[22] Joseph Carl Robnett Licklider. 1960. Man-Computer Symbiosis. IRE Transactions 
on Human Factors in Electronics HFE-1, 1 (1960), 4–11. doi:10.1109/THFE2.1960. 
4503259 
[23] Rostam J. Neuwirth. 2023. Prohibited Artifcial Intelligence Practices in the 
Proposed EU Artifcial Intelligence Act (AIA). Computer Law & Security Review 
48 (April 2023), 105798. doi:10.1016/j.clsr.2023.105798 
[24] Rostam J. Neuwirth. 2024. Law, artifcial intelligence, and synaesthesia. AI & 
SOCIETY 39, 3 (June 2024), 901–912. doi:10.1007/s00146-022-01615-8 
[25] Georgios Pavlidis. 2024. Unlocking the Black Box: Analysing the EU Artifcial 
Intelligence Act’s Framework for Explainability in AI. Law, Innovation and 
Technology 16, 1 (Jan. 2024), 293–308. doi:10.1080/17579961.2024.2313795 
[26] Sven Peldszus, Henriette Knopp, Yorick Sens, and Thorsten Berger. 2025. Towards 
ML-Integration and Training Patterns for AI-Enabled Systems. In Lecture Notes in 
Computer Science. Springer Nature Switzerland, Cham, 434–452. doi:10.1007/978-
3-031-73741-1_26 ISSN: 0302-9743, 1611-3349. 
[27] Ben Shneiderman. 2022. Human-Centered AI (1 ed.). Oxford University PressOx-
ford. doi:10.1093/oso/9780192845290.001.0001 
[28] Richard S. Sutton and Andrew G. Barto. 2018. Reinforcement learning: an intro-
duction (second edition ed.). The MIT Press, Cambridge, Massachusetts. 
[29] Matthias Wagner, Markus Borg, and Per Runeson. 2024. Navigating the Upcoming 
European Union AI Act. IEEE Software 41, 1 (Jan. 2024), 19–24. doi:10.1109/MS. 
2023.3322913 
[30] Natnael A. Wondimu, Cédric Buche, and Ubbo Visser. 2022. Interactive Ma-
chine Learning: A State of the Art Review. doi:10.48550/arXiv.2207.06196 
arXiv:2207.06196 [cs]. 
[31] Manuel Wörsdörfer. 2023. Mitigating the Adverse Efects of AI with the Euro-
pean Union’s Artifcial Intelligence Act: Hype or Hope? Global Business and 
Organizational Excellence (Nov. 2023), joe.22238. doi:10.1002/joe.22238 
[32] Wei Xu, Marvin J. Dainof, Liezhong Ge, and Zaifeng Gao. 2023. Transitioning 
to Human Interaction with AI Systems: New Challenges and Opportunities 
for HCI Professionals to Enable Human-Centered AI. International Journal of 
Human–Computer Interaction 39, 3 (Feb. 2023), 494–518. doi:10.1080/10447318. 
2022.2041900
