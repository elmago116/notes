---
title: Bias and fairness in machine learning and artificial intelligence
source: https://www-sciencedirect-com.sire.ub.edu/science/chapter/edited-volume/pii/B9780128213926000066
authors: "[[AbstractSex and gender biases can be entrenched in the life cycle of Artificial Intelligence (AI) development]],[[from data acquisition to technological design and deployment. AI systems that fail to account for the contribution of sex and gender to health generate suboptimal results and discriminatory outcomes. Assessing sex and gender biases in these resources enables to acquire insights and awareness on the pressing need of an ethically informed science]],[[paving the way to robust]],[[trustworthy]],[[and intelligible applications of AI accounting for sex and gender equity. Nevertheless]],[[sex and gender biases are not the only types of biases that can manifest in AI systems. In this chapter]],[[we provide an overview on the pervasiveness of several types of biases in AI development and a categorization of the main types of biases as well as bias metrics and available implementations for AI fairness evaluation]],[[with special emphasis on sex and gender categories.]],[[Google Scholar]]"
published:
created: 2026-02-17
description: Sex and gender biases can be entrenched in the life cycle of Artificial Intelligence (AI) development, from data acquisition to technological design a…
tags:
  - themes/bias/algorithmic
  - themes/gender
  - themes/health
DOI:
Type:
year:
---
[[Bias and fairness in machine learning and artificial intelligence.pdf]]

- [View **PDF**](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000066/pdfft?md5=9d9f18f634c90e8f5f6808de621af561&pid=3-s2.0-B9780128213926000066-main.pdf)![Academic Press](https://ars-els-cdn-com.sire.ub.edu/content/image/Dacadpr.gif)

Academic Press

## Sex and Gender Bias in Technology and Artificial Intelligence

Biomedicine and Healthcare Applications

2022, Pages 57-75

## Chapter 3 - Bias and fairness in machine learning and artificial intelligence

[https://doi-org.sire.ub.edu/10.1016/B978-0-12-821392-6.00006-6](https://doi-org.sire.ub.edu/10.1016/B978-0-12-821392-6.00006-6 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=B9780128213926000066&orderBeanReset=true)

Complimentary access

- [Next chapter in book](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000078)

## Keywords

Bias

Fairness

Model development

Artificial intelligence

## Acknowledgments

The authors are grateful to Dr. Michele Loi for reviewing the manuscript meticulously and providing extremely valuable feedback.

## Chapter points

- •
	Bias in humans as well as in AI prevents impartial judgment, leading to decisions that are not based on objective criteria or free from external influences.
- •
	Several categorizations of bias have been proposed, including desirable and undesirable biases, cognitive and statistical biases, explicit and implicit biases, and algorithmic biases.
- •
	We identify in the life cycle of AI development that require specific actions to ensure the realization of bias-free AI models.
- •
	Creating awareness about bias in AI is a fundamental endeavor to fight against discrimination and prejudice in the scientific and technological communities as well as in the society.

## 1\. Introduction

Bias is a word of unknown origin, but its most plausible etymology provides a metaphorically appropriate description. Indeed, the term probably came to French from Old Provençal *biais*, possibly via Vulgar Latin *(e)bigassius* from Greek *epikarsios*, which translates to “a slant, an oblique,” a line going diagonally across the grain of a fabric .

Contemporarily, the term bias has acquired many definitions. From a statistical point of view, it refers to any type of error or distortion that is found with the use of statistical analysis . For instance, a statistical bias can emerge due to improper analytical procedures, such as an inaccurate estimation, an unfair sampling, or a testing error, that systematically hold with some outcomes over others. From a cognitive point of view, it can refer to an innate or learned tendency in favor of or against an individual, a group, or a belief . For instance, preconceived convictions, preferences, and inclinations may guide views on social questions, despite being formed with a small amount of evidence or even without factual knowledge.

Overall, bias prevents impartial judgment, leading to decisions that are not based on objective criteria or free from external influences. This concept is of paramount importance in science as it is intimately linked to testability and reproducibility of observations, which represent basic tools for our collective knowledge and understanding of the world . This problem of scientific objectivity has been largely scrutinized by countless authors and thinkers throughout the history of mankind (see Section 3, [Chapter 11](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000029 "Persistent link using publisher item identifier"), “Societal and Ethical Impact of technologies for Health and Biomedicine”).

The existence of statistical and cognitive biases can have a deep impact in all the aspects of scientific practices and technical developments, from experimental design to the implementations of models in all disciplines, with special emphasis on the intersection of medicine and computational sciences. For instance, algorithms for , which are to automatically perform tasks, such as executing arithmetic or logical operations or performing analytical and modeling procedures, can produce outcomes that exhibit systematic errors. The origin of such errors include but are not limited to the design of the algorithm itself or the data that it utilizes or generates. Nevertheless, algorithmic bias is one type of bias among many others that can coexist in the same system and all of its parts. The outline of a comprehensive taxonomy of biases represents a challenging endeavor aggravated by the absence of a definitive consensus about an accepted classification and unequivocal arrangement of bias categories. In this chapter, we identify the most commonly recognized classes of bias and shed light on both their relationship with and research, with special attention to sex and gender biases, and existing solutions to ensure a of algorithms and the data they feed on.

## 2\. A complex landscape of intersecting biases

Functional and well-crafted algorithms display a great potential to generate outcomes that can be equally or even more impartial than human decisions. Nevertheless, with the growing complexity in algorithm design, algorithmic biases are being increasingly difficult to be assessed and addressed . Such complexity is mirrored by the massive volume of data that humanity generates, which is estimated to amount to 2.5 quintillion bytes (2.3 trillion gigabytes) each day . A significant share of this data is related to personal information or protected characteristics, which is used to feed into algorithms for detecting patterns to predict behaviors and classify individuals for several purposes, such as assisting and shaping interaction with products and services (see Section 2, [Chapter 4](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000078 "Persistent link using publisher item identifier"), “Big Data in healthcare from a perspective”). For instance, a popular video streaming platform uses a to predict future watches based on users’ preferences .

Recently, bias in Artificial Intelligence (AI) has taken center stage in the public debate and scientific circles, resulting in a progressive acquaintance of our community with concepts such as bias, fairness, and related ones. For instance, it is now widely accepted the so-called “black box” metaphor, which dates back to the early days of , and refers to systems where only the input and output can be observed or interpreted but not the internal mechanisms. The “black box” metaphor is especially used in the context of deep learning applications, a debate that is being recently fueled by positions about the reasonable use of black boxes and the dedicated explainable approaches .

Although it is acknowledged that AI tends to reflect the biases of the data it feeds on, many other sources of biases should be recognized and addressed. Indeed, as bias in AI can reflect human cognitive biases, the best way to understand algorithmic bias is to understand first. For instance, a recent study found that less than 20% of the researchers applying to prestigious AI conferences are women , exposing the risk of predominantly male perspective in AI design. The reduced female participation can potentially lead to inaccuracies and selective avoidance of specific aspects, such as the adequate representation of disease manifestations in women in the data used for training for health. An example of the complexity of intersecting biases is in , where the gender bias in medical imaging datasets used to train AI systems is accompanied by a marked gender discrimination in radiology resident selection , , ().

![Illustration of two people with laptops and two doctors with X-ray images of shoulder and knee.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000066-f03-01-9780128213926.jpg)

Download: Download full-size image

As increasing the inclusion of women in can have a positive impact in the prevention of bias generation in AI development, several activities in this area are being promoted, such as inclusive STEM (Science, Technology, Engineering, and Mathematics) programs embraced by universities and colleges as well as dedicated initiatives in academia, such as Bioinfo4Women (B4W) ([http://bioinfo4women.bsc.es/](http://bioinfo4women.bsc.es/)), and industry, such as STEM for Girls by IBM ([https://www.ibm.org/initiatives/stemforgirls](https://www.ibm.org/initiatives/stemforgirls)). Our society needs a higher representation of women and girls in science to devise actionable solutions for containing and eventually ceasing the feedback of stereotypes and inequalities generated by the design and application of biased AI. Creating awareness about these themes is a fundamental endeavor to fight against discrimination and prejudice in the scientific and technological communities and society at large.

## 3\. Taxonomies of bias

Several categorizations of bias have been proposed in different areas of research, ranging from psychology to machine learning. Such a variety of categorizations of bias arises naturally as new problems are identified over time, thus ambiguities in bias taxonomies are expected . Nevertheless, initiatives to identify comprehensive lists of biases exist, such as The Catalogue of Bias ([https://catalogofbias.org/biases/](https://catalogofbias.org/biases/)). Based on the value of the resulting outcome, we have recently proposed a categorization of biases into desirable and undesirable . A desirable bias is a differentiation between categories that achieves socially and morally valuable outcomes as well as their fair distribution (e.g., considering sex and gender differences in disease manifestation or drug response to design new therapies that are equally effective across the different sexes and genders), while an undesirable bias is a differentiation between categories that magnifies inequalities (e.g., prejudicial sex and gender discrimination). Such formulation of bias acknowledges the current view on the complexities that characterize this area of research , .

### 3.1. Cognitive and statistical biases

The most simple and intuitive categorization of bias distinguishes between cognitive bias and statistical bias. Cognitive bias is a systematic deviation from some aspects of objective reality and its emergence is tightly linked to the evolution of (see : “Human cognition, generalization, and machine learning”). More than 200 types of cognitive biases have been described, such as confirmation bias, cultural bias, historical bias, emotional bias (a comprehensive list can be found at Ref. ). Some of these biases are particularly relevant in , such as the reporting bias, which occurs due to the conscious or unconscious omission of information. An example of reporting bias is that of a discrepancy between the adverse event data in a trial sponsor's database and the published data .

Box 3.1

Human cognition, generalization, and machine learning.

Human inherent cognitive capacity of learning is central to solving problems in our , endowing us with the ability to make quick and adaptive decisions in complex situations. In general terms, the human learning process supports *generalization*, which is based on accumulated knowledge obtained from the interaction with the environment . Generalization is often supported by the reduction of complex concepts to simple categories that can ultimately be considered as “stereotypical” representations of our reality that enable survival advantages . Generalization is also what most machine learning algorithms that underlie AI technologies are designed to support, often aiming toward providing effective , especially in complex situations with actionable implications, ranging from fraudulent credit card transactions to pharmacological strategies targeting cancer. In machine learning, generalization is impossible without assumptions (i.e., bias-free learning is futile), as asserted by the ugly duckling theorem , the , and many others. Indeed, arguments asserting the impossibility of bias-free learning stretches back to David Hume's *A Treatise of* (1738–40) where the empiricist philosopher pointed out that “we have no reason to draw any inference concerning any object beyond those of which we have had experience.”

Statistical bias is the systematic deviation of the result of an analytical procedure from its true value, excluding the contribution of randomness (a.k.a. precision). For example, a systematic error in a sample statistic used, for instance, to estimate a quantitative parameter of a population, may cause that the measured value differs from its true value:$measured value=true value+systematic error+random error$

There are several types of statistical bias (). Additional biases that can be found in the literature are forms of other major statistical or cognitive biases; for instance, attrition bias is a type of selection bias that manifests when samples are lost from the population under study (e.g., participants dropping out of a clinical trial). Moreover, some cognitive biases can lead to statistical biases, such as the observer bias, consisting of unreliable reported information (e.g., patients knowing that they are being examined), which can lead to several forms of detection bias.

Table 3.1. Main types of statistical bias.

| Type of bias | Description | Example |
| --- | --- | --- |
| Selection bias | It occurs when the group under study is not representative of the entire population. | Genomic databases display an unbalanced representation of men and women . |
| Detection bias | It occurs when an event is more likely to be observed in a specific group of the population. | Biological factors and gender norms lead to an inflation of women diagnosed with depression . |
| Measurement bias | It occurs when the same procedure measures different features in different groups of the population. | Conventional cardiac troponin assays thresholds underdiagnose acute myocardial infarction in women . |
| Evaluation bias | It occurs when one conclusion is favored instead of other equally valid alternatives. | Older adults with intellectual disability are more prone to experience inappropriate drug prescribing . |
| Aggregation bias | It occurs when assumptions about the population are believed to apply or not to a specific group. | Women with early breast cancer receive unnecessary imaging tests for metastasis . |

### 3.2. Explicit and implicit biases

A more widespread categorization of bias distinguishes between explicit bias (alt. conscious or aware bias) and implicit bias (alt. unconscious, unaware, or hidden bias). Some authors define implicit bias as a latent mental construct (e.g., a personal attitude) that causes specific behaviors, while other authors define it as a behavior itself that is influenced by sociocultural cues .

Implicit bias has been addressed in the context of several forms of gender inequity and biased modes of human-machine interactions . Interestingly, despite being able to seep into AI development, AI-aided interventions on implicit bias exist and are collectively called “equitech” , that is, AI systems aimed at improving equity.

Implicit bias can be measured in both humans and machines. For instance, a human subject can report attitudes in an explicit way, but the same attitudes can also be implicitly inferred from other behaviors. In the case of AI systems, such as in the area of , implicit bias can be detected by measuring word associations through the Word-Embedding Association Test (WEAT) (see Section 2, [Chapter 6](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000091 "Persistent link using publisher item identifier"), “Sex and gender bias in Natural Language Processing”).

### 3.3. Algorithmic bias

Algorithmic bias is a peculiar type of bias as it is specifically related to and particularly relevant in the area of machine learning and AI. Algorithmic bias can be classified into preexisting, technical, and emergent . Preexisting algorithmic bias emerges from social and institutional ideologies that may affect directly or indirectly a programmer or a developer. Technical algorithmic bias derives from the limitation of the system under development, such as computational power, design, and internal mechanisms. Emergent algorithmic bias occurs due to the use of an algorithm in a novel and unknown context. Unexpected emergent biases can occur in self-learning systems or during the course of a simulation . A form of emergent bias is correlation bias, which manifests as unexpected correlations between sensitive and nonsensitive data, such as race and postal codes . Moreover, emergent bias can create harmful feedback loops if the outcome of the algorithm results in responses that are to it, for instance, for retraining. The outcome of an algorithm that feeds on biased data from the real world can lead to biased decisions and create new inequalities, which will be reflected in new data used by the algorithm to produce new biased outcomes, and so forth. Such AI-powered feedback loops propagating have been observed in several areas, such as recommender systems as well as predictive policing and , . As an example of this kind of feedback loop in the , a study has recently found evidence of racial bias in an algorithm, widely used in hospitals, to predict the need of follow-up care from insurance claims . As the algorithm was trained on health costs rather than on the actual health needs, it was inappropriately inferring illness from the unequal access to care between Black and White patients. When the algorithm was retrained using the actual physiological variables, the racial bias was completely removed.

## 4\. From ideation to deployment: The life cycle of AI development

Many domain-specific concepts of efficiency exist. For instance, in economics efficiency can be defined in terms of maximum feasible output given the available resources (technical efficiency) or in terms of use of the most productive combination of those (allocative efficiency) . As for computer science and AI, efficiency is defined in terms of speed and requirements, information storage and communication, and energy . Although optimizing efficiency has been a priority in the life cycle of AI development, available computational resources are often limited and exclusive. As an example, the of parameters trained in the state-of-the-art models for requires computational and economic costs that are inaccessible to small enterprises and most public institutions (see Section 2, [Chapter 6](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000091 "Persistent link using publisher item identifier"), “Sex and gender bias in Natural Language Processing”). Efficiency alone may prevent us from achieving the fair and equitable outcomes that we care to reflect our values, which is particularly evident in the case of forms of efficiency that can be used for healthcare. For instance, adjusting health resource investments based solely upon the maximization of the overall quality-adjusted life year (QALY) could potentially conflict with fairness due to the complexity of the care needs and costs of diverse groups of patients , , .

We are currently witnessing a progressive paradigm shift in the process of AI design, from concept ideation to solution implementation and resource estimation. Critical issues related to ethics and specific to the scope and goals of each AI project are being increasingly taken into consideration in the production pipeline, including privacy and data ownership, trustworthiness and accountability, transparency, and, naturally, bias and fairness. Concerning this revolution in AI development, the change should be complemented by the responsibility to inform the consumers of the AI systems, such as policy makers, business owners or the general population, about the concepts and metrics used in the field. Indeed, such awareness enables, in turn, to implement better audit models for different types of bias and help identify better measures of impact and strategies for their reduction and/or removal.

We identified four in the life cycle of AI development that require specific actions from engineers, data scientists and managers to ensure the realization of a fair AI model ():
- 1
	Collected data should be examined to detect dataset imbalance and different types of biases. In the case of AI systems, special emphasis should be given to statistical, implicit, and algorithmic biases (see , “Taxonomies of bias”).
- 2
	The model should be explainable and interpretable in all its components. and are fundamental elements to equip an AI system with transparency, fairness, and accountability (see Section 3, [Chapter 9](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000042 "Persistent link using publisher item identifier"), “A unified framework for the management of sex and gender biases in AI models for Healthcare”).
- 3
- 4
	The impact of model deployment should be evaluated based on real-world data and end-users experience. Importantly, estimations of the socioeconomic impact of an AI system is a crucial evaluation that should be accounted for before and after its deployment (see Section 1, [Chapter 2](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000054 "Persistent link using publisher item identifier"), “Sex and in Precision Medicine: Socioeconomic Determinants of Health”).

![Circular diagram of machine learning lifecycle with five stages labelled 1 to 5.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000066-f03-02-9780128213926.jpg)

Download: Download full-size image

These four points highlight how pervasive biases can be throughout all the stages of AI development, which can exhibit several layers of biased elements including not only biased data and results but also, more subtly, biased purposes and biased human views on the entire process. In this regard, postmodeling aspects are equally important. AI can be used to take decisions resulting in actions with distinct outcomes. However, as the same decisions could be taken by any human alone or following some preestablished rules, the question on how to evaluate an improvement compared to such a baseline emerges, considering that the world itself, in terms of the human historical framework, is inherently biased (see : “Human cognition, generalization, and machine learning”). How to mitigate inherent bias and avoid distortions in AI benchmarking is still an open field of investigation with novel implementations such as Dynabench , a dynamic benchmarking platform created by Facebook that proposes a model error evaluation based on the interaction with humans.

## 5\. Bias metrics

A crucial aspect of measuring bias impact is to have a working definition of “fairness.” Despite the growing trend in appealing to fairness within the domain of machine learning and AI, the definition of this concept is neither well understood nor agreed upon. As the debate in the public sphere makes it evident, questions of fairness often give rise to disagreement. As a matter of fact, what we regard as a benefit or a burden determines our judgments of unfairness, which might entail a reasonable disagreement by parties with different goals and views than ours . This variety of conceptions has a great impact in the current efforts to devise an of fairness in the area of machine learning and AI.

For instance, if we collect data that capture an unequal baseline condition, such as a difference in the incidence of a disease in male and female individuals, this difference can be learned by a system capable of statistical generalization, such as a machine learning model, and hence be reflected in the resulting decision or outcome. Without knowing if the observed diversity underpins a genuine , it is actually difficult to agree whether that decision is biased or not. Likewise, it is difficult to agree if removing this alleged bias from the model makes the decision fairer.

This dilemma is at the heart of the current research on machine learning fairness and a large body of work has been carried out to better understand and prevent discrimination in AI , . For instance, it has been shown that, in the case of a disease risk predictor trained under different base rates across two groups, three fairness conditions can be attained: (a) the model estimates should be systematically distorted for at least one group; (b) a higher risk should be assigned to healthy individuals of one group; and (c) a higher risk should be assigned to the diseased individuals of one group. Since these three notions of fairness are incompatible, a trade-off between them must be determined .

These conceptions of fairness and nondiscrimination have various equivalent and alternative formalizations in the scientific literature. Indeed, algorithms used for assuring fairness are still being improved and an established methodology for avoiding discrimination of protected classes or attributes (e.g., gender, race, religion, disability, and social status) is currently lacking. Nevertheless, three of the most common notions of algorithmic fairness can be defined , ():
- •
	**Demographic parity** (a.k.a. statistical parity): the predictor should assign a positive outcome to each group of a protected class at equal rates. In the case of a binary decision $Yˆ∈01$ and a binary protected class sex *S* ∈{ *male*,*female* }, this constraint is formalized as follows:
$PYˆ=1S=male=PYˆ=1S=female$
- •
	**Equal opportunity**: the predictor should assign a positive outcome across groups at equal rates, assuming that the individuals in the group qualify for it. In other words, the predictor should ensure the same True Positive Rate (TPR) across the groups:
$PYˆ=1S=maleY=1=PYˆ=1S=femaleY=1$
- •
	**Equalized odds**: the predictor should ensure equal opportunity but also misclassification at equal rates across groups. In other words, the predictor should ensure TPR and (FPR) across the groups:
$PYˆ=1S=maleY=y=PYˆ=1S=femaleY=y,y∈01$

![Diagram comparing statistical metrics with figures labelled A, B, and C.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000066-f03-03-9780128213926.jpg)

Download: Download full-size image

These three definitions range from the less restrictive (demographic parity) to the more restrictive (equalized odds) and should be applied under specific conditions. Nevertheless, the use of a particular definition of fairness in different contexts requires in-depth evaluations and it currently represents a matter of intense scientific research due to the complexity of the problem. For instance, enforcing demographic parity would not be deemed appropriate in situations such as assigning a treatment with harmful side effects to individuals who do not benefit from it .

While considering the use of existing fairness notions could potentially improve machine learning equity under specific circumstances, just ignoring the protected attributes is not effective due to the possible existence of redundant encodings and proxy variables that can indirectly relate to them (see , “Algorithmic bias”). In this regard, several other approaches and definitions of fairness exist. For instance, predictive parity ensures that the precision rates, or positive predictive value (PPV), are equivalent across groups, that is, the proportion of predicted positives that are true positives. Other fairness metrics, such as counterfactual fairness, which ensures equal outcomes of identical individuals of different groups of a protected attribute , are not always applicable to every context.

Additional fairness metrics are private to specific problems. For instance, *maxmin* fairness is used in for network optimization with several applications in real-world scenarios, such as patient matching for or donor-recipient matching for . Algorithms to guarantee the maximum satisfactory matching possible to all individuals, with no exclusion, have been recently proposed . In such a composite landscape of fairness notions, several resources in this area of research are available, including online books (e.g., [https://fairmlbook.org/](https://fairmlbook.org/)) as well as open source toolkits and several software implementations ().

Table 3.2. Selection of GitHub repositories of software for machine learning fairness (the complete list is available at ).

| Name | Developed by | Code repository | Description | Reference |
| --- | --- | --- | --- | --- |
| Fairness Measures | Universitat Pompeu Fabra & Technische Universität Berlin | [https://github.com/FairnessMeasures/fairness-measures-code](https://github.com/FairnessMeasures/fairness-measures-code) | Python software for detecting algorithmic discrimination. |  |
| Fairness Comparison | University of Arizona, University of Utah & Haverford College | [https://github.com/algofairness/fairness-comparison](https://github.com/algofairness/fairness-comparison) | Python software for fairness benchmarking of machine learning algorithms. |  |
| Themis-ML | Arena | [https://github.com/cosmicBboy/themis-ml](https://github.com/cosmicBboy/themis-ml) | Python fairness-aware machine learning interface. |  |
| FairML | Massachusetts Institute of Technology | [https://github.com/adebayoj/fairml](https://github.com/adebayoj/fairml) | Python toolbox for auditing predictive models for bias. |  |
| Aequitas | University of Chicago | [https://github.com/dssg/aequitas](https://github.com/dssg/aequitas) | Python bias audit toolkit. |  |
| FairTest | EPFL, Columbia University, Cornell Tech & Saarland University | [https://github.com/columbia/fairtest](https://github.com/columbia/fairtest) | Python software to discover unwarranted associations in an algorithm's outputs. |  |
| Themis | University of Massachusetts Amherst | [https://github.com/LASER-UMASS/Themis](https://github.com/LASER-UMASS/Themis) | Python software to measure group and causal discrimination. |  |
| Audit-AI | Pymetrics | [https://github.com/pymetrics/audit-ai](https://github.com/pymetrics/audit-ai) | Python library for bias testing in generalized machine learning applications. |  |
| AIF360 | IBM | [https://github.com/Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) | Python and R packages to detect and mitigate bias in machine learning models. |  |
| FairLearn | Microsoft | [https://github.com/fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) | Python package to assess AI fairness and mitigate unfairness observations. |  |
| FairSight | University of Pittsburgh | [https://github.com/ayong8/FairSight](https://github.com/ayong8/FairSight) | JavaScript visual analytic system to address fairness in ranking decisions. |  |
| ML Fairness Gym | Google | [https://github.com/google/ml-fairness-gym](https://github.com/google/ml-fairness-gym) | Python toolkit for long-term impact assessment of machine learning systems. |  |
| Fairness Indicators | Tensorflow | [https://github.com/tensorflow/fairness-indicators](https://github.com/tensorflow/fairness-indicators) | Tensorflow toolkit for evaluating, improving, and comparing models for fairness. |  |
| Fairness | University of Copenhagen & Humboldt University of Berlin | [https://github.com/kozodoi/fairness](https://github.com/kozodoi/fairness) | R package to calculate metrics of algorithmic fairness across different sensitive groups. |  |
| Fairness in Classification | Max Planck Institute for Software Systems | [https://github.com/mbilalzafar/fair-classification](https://github.com/mbilalzafar/fair-classification) | Python implementation of fair logistic regression classifiers. |  |
| LiFT | LinkedIn | [https://github.com/linkedin/LiFT](https://github.com/linkedin/LiFT) | Scala/Spark library to measure fairness in large scale machine learning workflows. |  |
| Fair Distributor | Hackathonners | [https://github.com/Hackathonners/vania](https://github.com/Hackathonners/vania) | Python module to fairly distribute a list of arbitrary objects through a set of targets. |  |
| FAT Forensic | University of Bristol & Thales | [https://github.com/fat-forensics/fat-forensics](https://github.com/fat-forensics/fat-forensics) | Python toolbox for evaluating fairness, accountability and transparency of predictive systems. |  |
| CQR | Stanford University | [https://github.com/yromano/cqr](https://github.com/yromano/cqr) | Python package to construct unbiased predictive intervals for data-driven recommendation systems. |  |
| Responsibly | Boston University | [https://github.com/ResponsiblyAI/responsibly](https://github.com/ResponsiblyAI/responsibly) | Python toolkit for auditing and mitigating bias and fairness of machine learning systems. |  |
| FairModels | Warsaw University of Technology | [https://github.com/ModelOriented/fairmodels](https://github.com/ModelOriented/fairmodels) | R package for bias detection, visualization, and mitigation in machine learning models. | , |
| LaundryML | Université du Québec à Montréal | [https://github.com/aivodji/LaundryML](https://github.com/aivodji/LaundryML) | Python implementation of a regularized rule list enumeration algorithm for black-box models. |  |
| Wasserstein Fairness | DeepMind | [https://github.com/deepmind/wasserstein\_fairness](https://github.com/deepmind/wasserstein_fairness) | Python implementation of fair classification based on Wasserstein distance. |  |

a

Affiliation of the corresponding developer.

## 6\. Conclusions

The development of AI systems that are designed for healthcare and medicine is a striking achievement of of our times. Nevertheless, such systems learn to perform specific tasks, such as diagnosing diseases and recommending treatments, by processing large amounts of data that is produced through and practice or fetched from large databases of medical information. The quality and content of this data have an immense impact on what and how AI learns. If the data contains biases, such as artifacts and missing or wrong information, the application of AI can lead to discriminatory outcomes and propagate such biases into the society. For instance, an AI system for that has been trained using only medical images of one sex will fail to perform with equal accuracy in both sexes. In the long term, the application of such a tool in the clinical domain would create a disparity in the quality of medical care between the two sexes with negative implications for .

Discrimination in AI can be prevented by ensuring fairness and trustworthiness throughout all the steps of the life cycle of AI development. This includes addressing biases when gathering and preprocessing the data, as well as during the stages of model building, training, and evaluation, and finally at deployment phase and impact assessment of the AI application to the end-users in real-world settings. Recommendations to achieve this goal are to increase awareness of all these different types of biases in the scientific community, technology industry, among policymakers, and the general public; to implement AI with explainable components validated with appropriate benchmarks; and to incorporate key ethical considerations in the AI implementation, ensuring that the systems maximize wellbeing and health of the entire population. These recommendations have been recently outlined by the Women's Project and collaborators .

Awareness about the need for unbiased AI systems to pursue precision medicine and advance health and wellbeing is an obligation of the scientific community toward society, including both the layman and the professional. Moreover, ensuring fair opportunities and just treatment for all is the basis to eradicate discrimination of minorities and marginalized groups and, in the long term, remove any kind of underrepresentation in the data used in AI. Finally, perfecting policies and procedures to address equality, diversity and inclusion in science and technology can have a radical impact in ensuring multiplicity of views and innovative ideas for research and industry, leading to actions and procedures aimed at enhancing the quality of AI design and efficacy.

## References

- ### Achieving trust in health-behavior-change artificial intelligence apps (HBC-AIApp) development: A multi-perspective guide
	2023, Journal of Biomedical Informatics
	Citation Excerpt:
	This paper cited many important works, including \[2,8,10\]. We relied and cited additional papers that draw from our professional knowledge and extended the state of the art on trust building in HBC-AIApps, considering the perspectives of: medical informatics (\[13–18,34,36–38,40,60,68–70,72–79,82,87–89\]), human-centered design (\[4,5,20–28,31–33,55,62–63,67,80,86,90,91,96–117\]), and holistic health accompanied by occupational therapy (\[7,11,12,28–30,35,39,41–54,56–59,61,64–66,71,81,83–85,118\]). Our multidisciplinary background allowed us to synthesize our findings by considering different building blocks for building trust in HBC-AIApps (Fig. 2).

[View Abstract](https://www-sciencedirect-com.sire.ub.edu/science/chapter/edited-volume/abs/pii/B9780128213926000066)