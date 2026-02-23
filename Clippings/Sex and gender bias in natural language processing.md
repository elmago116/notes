---
title: "Sex and gender bias in natural language processing"
source: "https://www-sciencedirect-com.sire.ub.edu/science/chapter/edited-volume/pii/B9780128213926000091"
authors: "[[AbstractNatural language processing (NLP) is increasingly applied to a broad range of sensitive tasks]],[[such as human resources]],[[biomedicine]],[[and healthcare. Accordingly]],[[a growing body of research is investigating the impact of sex and gender bias in the models and the data on which such models are trained. As NLP systems become more pervasive in our societies]],[[the vulnerability to sex and gender bias may cause the perpetuation of prejudice and discriminatory decisions. To address this challenge]],[[a widespread awareness of bias needs to be created in the NLP community and more robust learning algorithms and fair solutions are required for the development and evaluation of NLP methods. In this chapter]],[[we survey the state-of-the-art NLP models and some popular applications to biomedicine and health]],[[with special emphasis on chatbots for mental health. Moreover]],[[we discuss sources and implications of bias in this area and show examples of notable debiasing methods.]]"
published:
created: 2026-02-17
description: "Natural language processing (NLP) is increasingly applied to a broad range of sensitive tasks, such as human resources, biomedicine, and healthcare. A…"
tags:
  - "themes/bias/algorithmic"
  - "Humanities/historicalMemory"
DOI:
Type: "Chapter"
year: "2022"
---

> ([[Sex and gender bias in natural language processing.pdf#page=12&annotation=730R|Sex and gender bias in natural language processing, p.124]])
> Notably, research in machine translation is investing great efforts in finding solutions to sex and gender bias in this specific NLP task, and we can find examples of bias detection [118,119], bias evaluation [120], and debiasing methods [107]. #op/acc/buscar 

[114] Zitelny H, Shalom M, Bar-Anan Y. What is the implicit gender-science stereotype? Exploring correlations between the gender-science IAT and self-report measures. Soc Psychol Personal Sci 2017;8:719–35. https://doi.org/10.1177/1948550616683017. #op/acc/buscar 


![[Sex and gender bias in natural language processing.pdf#page=7&rect=82,53,479,255|Sex and gender bias in natural language processing, p.119]]
![[Sex and gender bias in natural language processing.pdf#page=11&rect=149,127,408,305|Sex and gender bias in natural language processing, p.123]]




![[Sex and gender bias in natural language processing.pdf]]

- [View **PDF**](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000091/pdfft?md5=4409ce62b4a71d1b1a1689d44649a157&pid=3-s2.0-B9780128213926000091-main.pdf)![Academic Press](https://ars-els-cdn-com.sire.ub.edu/content/image/Dacadpr.gif)

Academic Press

## Sex and Gender Bias in Technology and Artificial Intelligence

Biomedicine and Healthcare Applications

2022, Pages 113-132

## Chapter 6 - Sex and gender bias in natural language processing

[https://doi-org.sire.ub.edu/10.1016/B978-0-12-821392-6.00009-1](https://doi-org.sire.ub.edu/10.1016/B978-0-12-821392-6.00009-1 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=B9780128213926000091&orderBeanReset=true)

Full text access

- [Next chapter in book](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B978012821392600008X)

## Keywords

Natural language processing

Language models

Debiasing methods

Machine translation

Sex and gender bias

## Acknowledgments

This work has received funding from “Future of Computing Center, a Barcelona Supercomputing Center and IBM initiative (2020).” The authors are grateful to Dr. Lynette Hirschman for reviewing the manuscript meticulously and providing extremely valuable feedback, and Dr. Martin Krallinger for the support and encouragement.

## Chapter points

- •
	The performances of have greatly improved, approaching human-like levels, and expanding the range of feasible applications in health.
- •
	Evidence of sex and gender biases in NLP methods is making the development of debiasing approaches of crucial importance for the application of these technologies in the biomedical domain.
- •
	Challenges and limitations of computational and data requirements for the implementation of fair NLP methods for health highlight the need to promote further research in this area especially focusing on the relation among sex and gender, language, and society.

## 1\. Introduction

(NLP) is an area of research and application focused on computational systems designed to understand, manipulate, and generate written and spoken human language for the purpose of performing a desired task . The term “natural” distinguishes human speech and writing from more formal languages, such as programming languages and mathematical notations. In recent years, have become so powerful that the performance on many tasks, such as speech recognition and , along with many others, has greatly improved. In some cases, such performances approach human-like levels, therefore expanding the range of feasible NLP applications especially in the health domain, where written and spoken material is largely abundant. To achieve such performances, vast amounts of textual data are used to train complex NLP models with huge numbers of parameters. Both the computational and data requirements impose several limits and challenges, including our ability to accurately detect and remove biases that can be present in the data used for training the models and ensure fair outcomes . Among these, sex and gender biases are some of the most frequently embedded biases that have been found in NLP, posing serious concerns on the impact of this technology in the society and especially the health domain .

In this chapter, we discuss how sex and gender bias can seep into NLP models for health-related applications, as well as possible and crucial areas for future research and development. The chapter is divided into several sections in which we discuss sex and gender bias in relation to the state-of-the-art in neural language models (), the application of such models to the health domain (), with special emphasis on (), and the effect of biased corpora on model outcomes () as well as prominent debiasing methods (). The chapter concludes with a discussion and an examination of future research perspectives in NLP ().

## 2\. NLP today: Breakthroughs and new challenges

NLP permeates the vast majority of digital tools that we use every day, and it involves direct real-world applications, such as machine translation, speech recognition, automated , and question answering as well as classification, summarization, and recommendation of text. Approaches to NLP are being addressed through rule-based and statistical techniques, as well as through and, most recently, . Indeed, recent advances in NLP have seen a shift from statistical language models , traditionally based on the utilization of words as labels (e.g., *n* -grams), to neural language models , which encode the distributional semantics of the terms, accounting for the context and the long-distance dependencies in either a static or a dynamic way. The theoretical foundations of such a modeling approach are based on the so-called distributional hypothesis, which states that words that occur in the same contexts tend to have similar meanings . Clear examples of this paradigm shift in NLP are visible in the approaches to language modeling, namely the task of predicting a word given its textual context consisting of preceding and/or following words ().

![Two diagrams showing language models predicting word probabilities.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000091-f06-01-9780128213926.jpg)

Download: Download full-size image

Deep learning is an area of machine learning that employs a large number of layers of , which collectively are able to learn rich with remarkable performance gains. Deep learning has proven extremely effective in NLP, especially thanks to its recent application to language modeling, and the employment, through one-/few-shot learning or fine tuning , of the resulting pretrained language models to a broad range of language-related tasks, such as , generation, translation, conversation, and others. State-of-the-art neural language models can use , recursive (RNN) , long-short term memory (LSTM) networks , and more recently Transformers .

In recent years, we have witnessed an outstanding number of breakthroughs in deep learning applied to NLP. This revolution is enabling a large range of applications but also unprecedented research directions. Some of these new challenges stem from pressing concerns in the NLP area, such as the recent trend toward big models that optimize massive amounts of parameters during the training process. Indeed, NLP is noticeably marked by a steady increase in model sizes, so much so that a model with over 1-billion parameters is perceived as the norm in the state-of-the-art (). of such large models are higher computational, economic and environmental costs as well as narrower competition opportunities for smaller entities in the field . For instance, a single GPU, even with 32GB of memory, cannot accommodate any model with more than 1.3 billion parameters . As a reaction, new approaches are bringing forward the creation of smaller models that are faster but comparable in performance with the bigger ones, such as , a method to pretrain an efficient language model with reduced size and faster performance.

Table 6.1. Number of parameters and training datasets size of notable pretrained language models that have been recently released.

| Model name | Institution or company name | Number of parameters | Training datasets size | Release year | References |
| --- | --- | --- | --- | --- | --- |
| ELMo | Ai2 | 93.6M | 1B WordBenchmark (11GB) | 2018 | , |
| GPT | OpenAI | 110M | BooksCourpus (5GB) | 2018 |  |
| BERT-Large | Google | 340M | BooksCorpus & English Wikipedia (13GB) | 2018 |  |
| MT-DNN | Microsoft | 330M | See BERT-Large | 2019 |  |
| ALBERT-xxlarge | Google | 233M | BooksCorpus & English Wikipedia (16GB) | 2019 |  |
| XLNet-Large | Carnegie Mellon University | 340M | BooksCorpus & English Wikipedia (13GB), Giga5 (16GB) , ClueWeb 2012-B (19GB) , Common Crawl (110GB) | 2019 |  |
| ERNIE-Gen-Large | Baidu Inc. | 340M | BooksCorpus & English Wikipedia (16GB) | 2019 |  |
| RoBERTa-Large | Facebook | 355M | Five English-language corpora (161GB) | 2019 |  |
| BART-Large | Facebook | 400M | See RoBERTa-Large | 2019 |  |
| Transformer ELMo | Ai2 | 465M | See ELMo | 2019 |  |
| XLM-R | Facebook | 550M | CommonCrawl (2.5TB) | 2019 |  |
| XLM (English model) | Facebook | 665M | See BERT-Large | 2019 |  |
| DistillBERT | HuggingFace | 66M | See BERT-Large | 2019 |  |
| GPT-2 | OpenAI | 1.5B | WebText (40GB) | 2019 |  |
| Grover-Mega | University of Washington | 1.5B | RealNews (120GB) | 2019 |  |
| CTRL | Salesforce Research | 1.63B | Several datasets (140GB) | 2019 |  |
| MegatronLM | nVIDIA | 8.3B | Several datasets (174GB) | 2019 |  |
| Meena | Google | 2.6B | Public domain social media conversations (341GB) | 2020 |  |
| T5-11B | Google | 11B | C4 (745GB) | 2020 |  |
| T-NLG | Microsoft | 17B | C4 (174GB) | 2020 |  |
| BST 9.4 | Facebook | 9.4B | Pushshift Reddit dataset (several terabytes) | 2020 |  |
| GPT-3 | OpenAI | 175B | CommonCrawl (570GB) and others of smaller sizes | 2020 |  |
| GShard | Google | 600B | In-house web-mined multilingual corpus | 2020 |  |
| Switch-C | Google | 1571B | C4 (745GB) | 2020 |  |

*M*, millions (10 <sup>6</sup>); *B*, billions (10 <sup>9</sup>).

a

Source: [https://www.stateof.ai/](https://www.stateof.ai/).

Even so, large models can be beneficial for low resources languages with limited , such as Hansa and , by the use of transferring learning for NLP . is a modeling approach that applies the knowledge learned in a problem to a different one, thus reducing the need for additional training data and resources.

In such a varied landscape of models and applications, need to be evaluated through appropriate human benchmarks, which should account for the fairness of the decisions, ensuring that no bias, including bias, is actually occurring. For instance, the creation of training and validation corpora with unfair representation of categories might introduce biases in both the performance evaluation and selection practices of NLP models. Critical to this aim is the inclusion of sex and gender bias assessment in the performance evaluation of the state-of-the-art in NLP for biomedicine. Performance evaluation in NLP is being addressed by dedicated initiatives, such as Microsoft Project Hanover , focusing on automated annotation for machine reading, and assessment campaigns, such as BioCreative , . These community-wide efforts are enhancing the evaluation of text-mining and information extraction systems applied to biomedicine, including document triage and relation extraction , chemical entities detection , and web servers . Although we are not aware of NLP performance evaluation campaigns that are specifically focused on sex and gender bias, several efforts to create corpora and datasets for sex and gender bias evaluation have been recently attempted , , .

## 3\. NLP for biomedicine and health

Although the underlying have been sparsely studied, differences have been documented in both written and spoken human language. Indeed, it has been shown that they can reflect cognitive differences interacting with speech and , . Thus, unbiased NLP models with medical applications have the potential to achieve better targeted predictions. For instance, models for text and speech analysis not only can be beneficial for , such as and stuttering, but also disorders with symptoms in the language domain, such as , depression, anxiety, and schizophrenia.

NLP has a wide range of in the biomedical and healthcare domains, especially for gender medicine. It provides new tools and methods to both research and healthcare that can analyze large amounts of textual data in scientific articles and patient clinical records to uncover differences and improve personalized medicine. In this regard, NLP-based applications in health have recently demonstrated their potential to improve efficiency in time consuming tasks such as medical coding and information extraction for database curation, which represent crucial steps toward the actionable incorporation of the sex and gender dimension in and practice ().

![Diagram of data interaction highlighting implicit and explicit knowledge conversion paths.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000091-f06-02-9780128213926.jpg)

Download: Download full-size image

Medical coding is a common NLP technique aimed at identifying clinical statements in patients’ clinical records and assigns standard codes using a . Standard codes are generally assigned according to the International of Diseases and Related Health Problems (ICD), which is the main medical classification standard for diseases, signs, and symptoms. Although this coding was originally intended for the billing of medical services, it is also widely used for research purposes, such as the processing of (EHRs) . In the context of gender, it is important to highlight that the recent 11th edition of ICD, officially approved in 2019, has redefined gender identity-related health, for instance, replacing such as “transsexualism” with “gender incongruence of adolescence and adulthood” .

Examples of biomedical include applications of information extraction systems to that have made it possible to identify relevant biomedical concepts, such as radiology reports, discharge summaries, problem lists, nursing documentation, among others . Moreover, a plethora of NLP tools have been developed to extract events and clinical concepts from EHRs, including MedLEE , KnowledgeMap , cTAKES , MetaMap , and MedTagger . Other applications of clinical NLP include patient cohort retrieval using EHRs , speech-to-text dictation to improve clinical documentation , the use of NLP for large-sample , and chatbots as clinicians, and also for clinical practice .

## 4\. A case in study: Chatbots for mental health

An example of NLP models are chatbots, which include general or goal-oriented digital voice-assistants. Popular chatbots, such as Apple's Siri, Alexa, Microsoft's Cortana, combine sophisticated NLP algorithms for speech recognition and with web-based search, and other capabilities (see : “Chatbots and robots”). Chatbots are also used in and healthcare. Besides such complex systems, even simple neural network-based techniques can effectively model dialog in certain contexts . Such can be augmented with available metadata to adjust features of the replier in terms of gender, age, and . For instance, the model of a speaker with specific attributes, such as dialect, age, and gender, can be trained from vectorial representations of conversational content. If this conversational content for training comes from different speakers who produce similar responses, their vectorial representations will be similar, thus increasing the generalization of the final speaker model. For instance, models trained using conversation content from a specific group of patients can account for factors such as incomplete sentences, speech difficulties, and emotional aspects among others. In this view, in order to accurately account for in disorders that may affect speech, the conversational datasets used for training such models should exhibit a fair representation of female and male patients.

Box 6.1

Chatbots and robots

In contrast to pure input-output linguistic chatbots, situated , such as robots (see Section 2, [Chapter 8](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000108 "Persistent link using publisher item identifier") “ How gender is intertwined with robots and affective technologies: A short review”), can additionally sense or act upon the physical world. In this regard, determining how the connections between words and objects are established represents a for AI. This problem is known as the symbol grounding problem and it concerns the question “how does a word get its meaning?” Rich semantic models interconnecting words to nonlinguistic entities such as sensory data, actions, and representations of plans and goals, often have to be constructed and/or empirically derived through data-driven methods , . For example, a robot can learn to describe the texture of a surface in natural language by touching it, while training a pure linguistic chatbot does not need perceptual symbol grounding and is limited to the content of the corpora used for training. This aspect highlights the difficulties of achieving human-like performances in automated systems that are challenged with tasks that, for us humans, appear to be natural and innate.

In the context of healthcare, chatbots are used to deliver real-time symptom assessment like in the case of Babylon Health and Ada Health . A flourishing area of development of medical chatbots is .

Psychiatric or compose a large array of conditions, including such as anxiety, depression, schizophrenia, and others. With the wide use of , chatbots of support for mental health are being developed, providing privacy and as well as scalable access, and aiming at improving users’ through chat interfaces and recommendation systems. Mental health organizations and health app evaluation agencies, such as ORCHA , periodically review technologies targeted at alleviating these disorders. With a growing number of users, popular mental care conversational agents are largely based on (CBT) and (DBT) and developed in collaboration with mental health professionals. Examples include Woebot , which proved to relieve from feelings of anxiety and depression a in ; Joy , which measures , geospatial patterns, and social interactions, analyzing habits that may affect the user's wellbeing; Moodkit , which recommends activities such as chatting and journaling through text and voice notes, and proved effective in clinical trials ; and Wysa , which has recently gained momentum as successful app for COVID-19 stress and anxiety.

Despite the beneficial values of such technology, most chatbots are designed with female characteristics. Moving from a recent report by UNESCO on the gendered design of most commercial voice-based chatbots , a recent work analyzed 1375 text-based chatbots and identified gender-specific cues implemented in their design, such as name, avatar, and description . The gendered design was found to be particularly prominent in , such as branded conversations, customer service, and sales, and biased toward female characteristics. Moreover, the authors found that the users tend to manifest traditional gender stereotypes toward the chatbots whenever they display specific social cues, thus potentially reinforcing negative generalizations.

## 5\. Sex and gender bias in the training corpora

Advances in and in have largely influenced NLP applications to biomedicine and health. These technologies were made possible by the availability of both high-performance and massive amounts of data, which we generally refer to as . Starting from the adoption of , the role of Big Data in healthcare has become crucial for building models from textual information.

Text corpora may contain imprints of documented human biases, such as sex and gender biases, and cultural stereotypes. Thus, their use has the potential to propagate these biases to the systems using NLP. This long-standing issue in is believed to be closely related to language evolution itself . Indeed, while some authors support a view of language specialization where communication improvement leads to enhanced fitness , others reckon a dependence on the cultural pressure of transmission to new learners and use . Recent efforts aim to reconcile the two views and even new theories on how to formulate and address the problem from a holistic perspective are arising .

Given the easy accessibility of massive text corpora (see ), sex and gender bias in NLP for health has received substantial attention in recent years . It has been shown that AI technologies, including NLP, as well as the biomedical, clinical, and data that they use, are largely exposed to sex and gender biases. As a consequence, algorithms can magnify health inequalities by integrating such biases, dramatically reducing their ability to achieve accurate and and treatment. The scientific community should incorporate regulations and ethical considerations to increase awareness of sex and gender differences and biases and advocate for trustworthy AI development . In this regard, an active research area in NLP is focused on studying what information language models are able to capture, paving the way to in this field . Furthermore, the flourishing birth of for measuring and mitigating bias in NLP models has led to the creation of guidelines and recommendations for analyzing bias in .

## 6\. Debiasing methods

All the components of an NLP system, from the data used for training its models to the context of its downstream applications, can potentially exhibit sex and gender biases. This condition exposes NLP systems to a high risk of producing socially biased outcomes and thus perpetuate preferences or prejudices in the society. It has been largely reported that NLP systems can propagate and amplify societal biases and stereotypes found in text corpora , in particular, in the health domain. For instance, the language used in may reflect a biased perception about patients, perpetuating negative stereotypes and even casting doubt or blame on the patient's experience (e.g., using stigmatizing expressions to highlight nonadherence to treatment) .

In particular, sex and gender bias can be found in many areas with dedicated NLP tasks, including caption generation from images based on a person's appearance , speech recognition of dialects , of abusive language , general language models , machine translation such as English-Spanish , and word embeddings , which we discuss further in the following.

In a seminal work, Bolukbasi and colleagues defined gender bias in word embeddings by the projection of a word vector on a predefined gender direction, such that vectors projected on the male direction are considered male-biased and vice versa. In the same work, they propose a novel method for debiasing word embeddings, by removing the projection component from the vector, which zeros the bias by definition ().

![Scatterplot graph with axes 'NEUTRALITY' and 'GENDER'. Points labelled as 'secretary', 'doctor', 'woman', 'man'.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000091-f06-03-9780128213926.jpg)

Download: Download full-size image

In a follow-up work, Zhao and colleagues presented a debiasing method, used during the training phase, which was also based on that same definition of bias by projection.

However, these methods were detected as problematic, since most of the bias information remained in the representations even after using them. Gonen and Goldberg showed that gender bias in word embeddings was more systematic, and deeply ingrained in the representations, which makes debiasing more challenging than previously perceived. This triggered a series of works about debiasing with different techniques, such as Manifold Dimensionality Retention (MDR) , among others (reviewed in Refs. , ).

Bias detection in NLP can leverage . Indeed, subconscious sex and gender bias in humans can be detected through the implicit-association test (IAT) , a popular and effective indirect measure of automatic associations, able to reveal implicit cognitive biases such as and stereotypes . IAT measures reaction times as an indicator of bias when subjects are asked to pair concepts they find similar as well as concepts they find different. By adapting the IAT measure of concepts’ association strength, Caliskan and colleagues have demonstrated how pervasively stereotyped biases can be absorbed by popular word , such as GloVe and Word2Vec. By using this technique, which they named the Word Embedding Association Test (WEAT), the authors also accurately predicted employment trends based only on the semantic closeness of the occupation word (“doctor,” “teacher,” “engineer”) to feminine words. Similarly, bias in word embeddings has been used to measure the change in female participation in the labor force . An extension of WEAT, called Sentence Encoder Association Test (SEAT) , tests sentence encoders, such as ELMo, for human biases measured through IAT.

Notably, research in machine translation is investing great efforts in finding solutions to sex and gender bias in this specific NLP task, and we can find examples of bias detection , , bias evaluation , and debiasing methods . Indeed, subtle nuances in language make it difficult to achieve a direct and accurate translation between many languages. One main challenge in this setting is underspecification of gender in the target language, which needs to be determined during translation, thus exposing undesired underlying biases. For instance, gender neutral nouns in English, such as “child,” will be translated into gender specific nouns in Spanish, such as “niño” (masculine) or “niña” (feminine). Translation can be very ambiguous in the case of heavily gender neutral languages, such as Turkish. For instance, the sentence in Turkish “o bir doktor” translates to English as “he/she is a doctor.” Indeed, Turkish to English translation poses major challenges to any machine or human aiming at a word or sentence without further context. In the case of machine translation, a system trained on texts expressing historical sex and gender bias will translate “o bir doktor” into “he is a doctor,” as doctors are more likely to be male.

Google Translate implemented a solution to this issue by explicitly specifying the desired gender for the translation of . First, a classifier identifies queries that can be translated into multiple genders. The classifier is a (CNN) trained on a large volume of human labeled examples of gender-neutral and gender-specific queries. Second, a rewriter introduces an extra token to the neutral queries expressing the gender to be translated to. Thus, the rewritten queries “< MALE> o bir doktor” and “<FEMALE \> o bir doktor” will be translated to English into “he is a doctor” and “she is a doctor,” respectively. This feature is currently implemented in the Google Translate system and led to a bias reduction of 95% when from Turkish to English, with a precision of 97% in the translation of both genders (). The solution adopted by Google Translate is one of the many examples of recent attempts in detection and mitigation of bias in NLP systems. Indeed, detection and mitigation of bias in NLP tasks, from machine translation to coreference resolution, is an active and promising area of investigation (see Section 3, [Chapter 9](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/B9780128213926000042 "Persistent link using publisher item identifier") “A unified framework for managing sex and gender bias in AI models for healthcare”).

![Translation of 'O bir doktor' with gender options.](https://ars-els-cdn-com.sire.ub.edu/content/image/3-s2.0-B9780128213926000091-f06-04-9780128213926.jpg)

Download: Download full-size image

## 7\. Discussion

In the history of our society, the concepts of sex and gender have been regrettably fraught with stereotypes and discriminatory attitudes. The magnitude of this fault is particularly evident in the accumulated volumes of textual data that have been historically produced and consumed in any human activity of communication and information exchange. Despite such preexisting biases, nowadays, the available large amounts of textual data can be efficiently harnessed to train complex NLP models that enable unprecedented applications with a significant impact in the progress of technology for the processing of , which has voluminous unstructured content. Indeed, for instance, the vast majority of clinical information in EHRs is presented in an unstructured form and needs to be mined with NLP systems for and interpretation in order to be ultimately translated into research applications and improved patient care.

If this data is not precisely curated and annotated by experts, training large NLP models by automatically digesting massive amounts of biased information can lead to the propagation of such bias into NLP systems, consequently feeding back inequalities in our society with their deployment. Examples of bias in NLP range from stereotyped translations to inaccurate sex-specific speech recognition, among others. The pervasiveness of bias in NLP has been recently demonstrated, for example, by unveiling the that exists between the employment numbers of specific occupations with the feminine gender as captured in word embeddings .

The increasing awareness on the extent to which sex and gender equality can be directly affected by the application of biased NLP models have spawned several research initiatives aimed at finding actionable solutions and avoiding the perfusion of bias into NLP systems. For instance, debiasing methods for word embeddings tailored to specific scenarios , and methods to properly declare the circumstances of a dataset creation have been recently proposed as solutions to mitigate preexisting bias and emergent bias, respectively. Despite the growing awareness of this issue, the research revolving around bias in NLP models is still in its infancy and needs significant improvements and further investigation before being fully and routinely embraced in the technological . For instance, research studies on NLP aspects related to trans- and nonbinary genders have scarcely been undertaken, and in written and spoken language are still under examination in several areas of inquiry. Moreover, the emergence of sex and gender bias in NLP applications, such as machine translation, is tightly linked to the linguistic defaults found in the languages associated with many human cultures. In such cases, the default (or “unmarked”) option is the general form (e.g., “actor” or “man”) and the “marked” form is the less general one (e.g., “actress” or “woman”). The acquisition of such linguistic defaults is currently a matter of intense research , .

Ethical foundations for the use of gender as a variable in NLP have recently been proposed , including the requirement of its definition and annotation in the modeling process as well as the fair utilization of this information in the datasets. To mitigate the threats to sex and gender equality, research in NLP modeling needs to commit to both making unfairness and bias visible as well as helping eradicate the discriminatory use of language in our society.

## References

[View Abstract](https://www-sciencedirect-com.sire.ub.edu/science/chapter/edited-volume/abs/pii/B9780128213926000091)