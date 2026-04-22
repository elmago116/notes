---
title: Is Neuro Symbolic AI Meeting its Promise in Natural Language Processing? A Structured Review
authors:
  - Kyle Hamilton
  - Aparna Nayak
  - Bojan Božić
  - Luca Longo
year: "2022"
journal: Semantic Web
doi: 10.3233/sw-223228
type: document
source: Manual
base: clippings
last_enrichment_run: 2025-08-20
updated: 2025-08-20
tags:
  - research_method/ScopingReview
  - Tech/NeSyAI
  - tech/NeSyAI/hybrid
apa_citation: Kyle Hamilton et al., 2022
---
[[Is Neuro-Symbolic AI Meeting its Promise in Natural Language Processing? A Structured Review.pdf]]

![[Is Neuro-Symbolic AI Meeting its Promise in Natural Language Processing? A Structured Review.pdf#page=6&rect=59,557,537,734|Is Neuro-Symbolic AI Meeting its Promise in Natural Language Processing? A Structured Review, p.6]]


## PDF text extraction

arXiv:2202.12205v2  [cs.AI]  30 Jun 2022
Is Neuro-Symbolic AI Meeting its Promise in
Natural Language Processing? A Structured
Review
Kyle Hamilton *, Aparna Nayak, Bojan Boži ´c and Luca Longo
SFI Centre for Research T raining in Machine Learning, Schoo l of Computer Science, T echnological University
Dublin, Republic of Ireland
E-mails: kyle.i.hamilton@mytudublin.ie, aparna.nayak@ tudublin.ie , bojan.bozic@tudublin.ie,
luca.longo@tudublin.ie
Abstract. Advocates for Neuro-Symbolic Artiﬁcial Intelligence (NeS y) assert that combining deep learning with symbolic
reasoning will lead to stronger AI than either paradigm on it s own. As successful as deep learning has been, it is generall y
accepted that even our best deep learning systems are not ver y good at abstract reasoning. And since reasoning is inextri cably
linked to language, it makes intuitive sense that Natural La nguage Processing (NLP), would be a particularly well-suit ed
candidate for NeSy . W e conduct a structured review of studie s implementing NeSy for NLP , with the aim of answering the
question of whether NeSy is indeed meeting its promises: rea soning, out-of-distribution generalization, interpreta bility , learning
and reasoning from small data, and transferability to new do mains. W e examine the impact of knowledge representation, s uch as
rules and semantic networks, language structure and relati onal structure, and whether implicit or explicit reasoning contributes to
higher promise scores. W e ﬁnd that systems where logic is com piled into the neural network lead to the most NeSy goals bein g
satisﬁed, while other factors such as knowledge representa tion, or type of neural architecture do not exhibit a clear co rrelation
with goals being met. W e ﬁnd many discrepancies in how reason ing is deﬁned, speciﬁcally in relation to human level reason ing,
which impact decisions about model architectures and drive conclusions which are not always consistent across studies . Hence
we advocate for a more methodical approach to the applicatio n of theories of human reasoning as well as the development of
appropriate benchmarks, which we hope can lead to a better un derstanding of progress in the ﬁeld. W e make our data and code
available on github for further analysis. 1
Keywords: Neuro-Symbolic Artiﬁcial Intelligence, Natura l Language Processing, Deep Learning, Knowledge Represent ation &
Reasoning, Structured Review
1. Introduction
At its core, Neuro-Symbolic AI (NeSy) is “the combination of deep learning and symbolic reasoning” [1]. The
goal of NeSy is to address the weaknesses of each of symbolic a nd sub-symbolic (neural, connectionist) approaches
while preserving their strengths (see ﬁgure 1). Thus NeSy pr omises to deliver a best-of-both-worlds approach which
embodies the “two most fundamental aspects of intelligent c ognitive behavior: the ability to learn from experience,
and the ability to reason from what has been learned” [1, 2].
* Corresponding author . E-mail: kyle.i.hamilton@mytudubl in.ie .
1 https://github.com/kyleiwaniec/neuro- symbolic-ai- systematic-review

Fig. 1. Symbolic vs Sub-Symbolic strengths and weaknesses. Based on the work of [8]
Remarkable progress has been made on the learning side, espe cially in the area of Natural Language Processing
(NLP) and in particular with deep learning architectures su ch as the Transformer [3, 4]. However, these systems
display certain intrinsic weaknesses which some researche rs [5, 6] argue cannot be addressed by deep learning alone
and that in order to do even the most basic reasoning, we need r ich representations which enable precise, human
interpretable inference via mathematical logic. 2
Recently, a discussion between Gary Marcus and Y oshua Bengi o at the 2019 Montreal AI Debate prompted
some passionate exchanges in AI circles, with Marcus arguin g that “expecting a monolithic architecture to handle
abstraction and reasoning is unrealistic”, while Bengio de fended the stance that “sequential reasoning can be
performed while staying in a deep learning framework” [9]. S purred by this discussion, and almost ironically, by the
success of deep learning (and ergo, the clarity into its limi tations), research into hybrid solutions has seen a dramati c
increase (see ﬁgure 2). At the same time, discussion in the AI community has culminated in “violent agreement” [10]
that the next phase of AI research will be about “combining ne ural and symbolic approaches in the sense of NeSy
AI [which] is at least a path forward to much stronger AI syste ms” [11]. Much of this discussion centers around
the ability (or inability) of deep learning to reason, and in particular, to reason outside of the training distribution .
Indeed, at IJCAI 2021, Y oshua Bengio afﬁrms that “we need a ne w learning theory to deal with Out-of-Distribution
generalization” [12]. Bengio’s talk is titled “System 2 Dee p Learning: Higher-Level Cognition, Agency, Out-of-
Distribution Generalization and Causality.” Here, System 2 refers to the System 1/System 2 dual process theory of
human reasoning explicated by psychologist and Nobel laure ate Daniel Kahneman in his 2011 book “Thinking, Fast
and Slow” [13]. AI researchers [1, 6, 14–18] have drawn many p arallels between the characteristics of sub-symbolic
and symbolic AI systems and human reasoning with System 1/Sy stem 2. Broadly speaking, sub-symbolic (neural,
deep-learning) architectures are said to be akin to the fast , intuitive, often biased and/or logically ﬂawed System 1.
And the more deliberative, slow , sequential System 2 can be t hought of as symbolic or logical. But this is not the
only theory of human reasoning as we will discuss later in thi s paper. It should also be noted that Kahneman himself
has cautioned against the over reliance on the System 1/Syst em 2 analogy in a followup discussion at the Montreal
AI Debate 2 the following year, stating, “I think that this id ea of two systems may have been adopted more than it
should have been.” 3
1.1. Reasoning & Language
“Language understanding in the broadest sense of the term, i ncluding question answering that requires
commonsense reasoning, offers probably the most complete a pplication area of neurosymbolic AI” [1]. This makes
a lot of intuitive sense from a linguistic perspective. If we accept that language is compositional, with rules and
structure, then it should be possible to obtain its meaning v ia logical reasoning. Compositionality in language was
formalized by Richard Montague in the 1970s, in what is now re ferred to as Montague grammar : “The key idea
2 See also Besold et al. [7], p.17-18 for additional context.
3 https://youtu.be/2zNd69ZGZ8o?t=161

Fig. 2. Number of Neuro Symbolic articles published since 20 10, normalized by the total number of all Computer Science ar ticles published
each year . The ﬁgure represents the unﬁltered results from S copus given the search keywords described in section 5.2.
is that compositionality requires the existence of a homomo rphism between the expressions of a language and
the meanings of those expressions.” 4 In other words, there is a direct relationship between synta x and semantics
(meaning). This is in line with Noam Chomsky’s Universal grammar 5 which states that there is a structure to natural
language which is innate and universal to all humans, and is g overned by precise mathematical rules. While an
analysis of the study of linguistics is beyond the scope of th is paper, the key takeaway is this: what makes such
theories so attractive to computational linguists is that m eaning can be derived from syntactic structures which can
be translated into computer programs. T oday, industrial st rength tools for extracting these structures (i.e., part-o f-
speech tagging, constituency parsing, dependency parsing ) are readily available, such as for example NL TK 6 or
SpaCy7. The challenge lies in representing and utilizing these str uctures in a way that both captures the semantics
and is computationally efﬁcient.
On the one hand, distributed representations are desirable because they can be efﬁciently processed by gradient
descent (the backbone of deep learning). The downside is tha t the meaning embedded in a distributed representation
is difﬁcult if not impossible to decompose. So while a Large L anguage Model (LLM), a deep learning language
model based on the principle of distributional semantics, m ay be very good at making certain types of predictions,
it cannot be queried for answers not present in the training d ata by way of analogy or logic. W e have also seen that
even as these models get infeasibly large - the larger the mod el, the better the predictions [19] - they still fail on
tasks requiring basic commonsense. The example in Figure 3, given by Marcus and Davis in [20] is a case in point.
Y ou are having a small dinner party . Y ou want to serve dinner i n the living room. The dining room table is wider than the
doorway , so to get it into the living room, you will have to remove the door . Y ou have a table saw , so you cut the door in half
and remove the top half.
Fig. 3. Third Generation Generative Pre-trained Transform er (GPT3) [21] text completion example. The prompt is render ed in regular font, while
the GPT3 response is shown in bold. It is clear that GPT3 is inc apable of commonsense.
On the other hand, traditional symbolic approaches have als o failed to capture the essence of human reasoning.
While we may not yet understand exactly how people reason, it is generally accepted that human reasoning is
nothing like the rigorous mathematical logic where the goal is validity. Though not for lack of ambition - Socrates
got himself killed trying to get people to reason with logic [ 22]. In the Dictionary of Cognitive Science [23], Pascal
4 https://plato.stanford.edu/entries/compositionality/#FormStat
5 https://www .britannica.com/topic/universal-grammar
6 https://www .nltk.org/
7 https://spacy .io/

Engel describes reasoning in a natural setting as “ridden wi th errors and paralogisms.” Engel refers to Daniel
Kahneman, Amos Tversky, Philip W ason, among others, who hav e conducted numerous experiments and written
extensively showing how logical fallacies and “noise” can l ead to those errors [13, 24]. But even when the objective
is not to emulate human thinking, but rather the execution of tasks which require precise, deterministic answers
such as expert reasoning or planning, traditional symbolic reasoners are slow , cumbersome, and computationally
intractable at scale, “typically subject to combinatorial explosions that limit both the number of axioms, the number
of individuals and relations described by these axioms, and the depth of reasoning that is possible” [18]. For example,
Description Logics (DLs) such as OWL 8 are used to reason over ontologies and knowledge graphs (KGs ). However,
one must accept a harsh trade-off between expressivity and c omplexity when choosing a DL ﬂavor. Improving the
performance of reasoning over ontologies and knowledge gra phs that power search and information retrieval across
the web is particularly relevant to the Semantic W eb communi ty. Hitzler et al. [25] report on recent research on
neuro-symbolic integration in relation to the Semantic W eb ﬁeld, with a focus on the promises and possible beneﬁts
for both.
The remainder of this manuscript is structured as follows. S ection 2 offers a brief history of NLP in the context of
reasoning. Several recent surveys and their contributions to NeSy are discussed in section 3, and are intended as an
introduction to the ﬁeld. Our contribution is given in secti on 4, which also details the goals of NeSy selected for this
survey. Section 5 describes the research methods employed f or searching and analysing relevant studies. In Section
6 we analyze the results of the data extraction, how the studi es reviewed ﬁt into Henry Kautz’s NeSy taxonomy
[10], and we propose a simpliﬁed nomenclature for describin g Kautz’s NeSy categories. Section 7 discusses the
limitations and challenges of the reviewed implementation s. Section 8 presents limitations of this work and future
directions for NeSy in NLP , followed by the conclusion in Sec tion 9.
2. A Brief History of NLP
The study of language and reasoning goes back thousands of ye ars, but it was not until the 1960’s that the
ﬁrst computational models were realized. The Association f or Computational Linguistics (ACL) 9 was founded in
1962 for people working on computational problems involvin g human language, a ﬁeld often referred to as either
computational linguistics or Natural Language Processing (NLP). Common NLP tasks are illustrated in Figure 4.
Named Entity Recognition 
(NER)
Part-of-Speech Tagging 
(POS)
Text Categorization/ 
Classification
Automatic Tpeech
Recognition (ASR)
Text-to-Speech (TTS) 
Syntactic Parsing
Coreference Resolution
Machine Translation 
Relation Extraction
Question Answering (QA)
Sentiment Analysis
Semantic Parsing
Paraphrase & Natural 
Language Inference
Dialog Agents
Summarization
NLP 
Fig. 4. Common Natural Language Processing tasks [26].
One of the ﬁrst NLP projects was a chat-bot named ELIZA [27], w ritten by Joseph W eizenbaum around 1965.
Given a small hand crafted set of rules, ELIZA was able to hold an, albeit superﬁcial, conversation, gaining
8 https://www .w3.org/2007/OWL/wiki/Direct_Semantics
9 https://www .aclweb.org/portal/

tremendous popularity. Curiously, despite the program’s s implicity those who interacted with it, attributed to it
human-like emotions. These early systems were based on patt ern matching and small rule-sets, and were very
limited for obvious reasons. In the 1970s and 80s linguistic ally rich, logic-driven, grounded systems, largely
inﬂuenced by Noam Chomsky’s Universal Grammar 10 were developed. The 1990s and early 2000s saw the
‘statistical revolution’ and the rise of machine learning, and work on NLP tasks focused on semantics, such as
Natural Language Understanding (NLU), diminished for the n ext decade or so 11 . NLU returns to center stage,
mixing techniques from previous years sometime around 2010 . As a case in point, in 2011 IBM’s W atson DeepQA
computer system won ﬁrst place on Jeopardy! for a prize of $1 m illion, competing against champions Brad Rutter
and Ken Jennings. 12 DeepQA is a large ensemble of techniques and models, the vast majority of which was
focused on general Information Retrieval (IR), NLP/NLU, Kn owledge Representation & Reasoning (KRR), and
Machine Learning (ML) [28]. Broadly speaking, DeepQA is a la rge neuro-symbolic question answering software
pipeline. In the last decade, and especially in the last few y ears, the emphasis on deep learning has somewhat
overshadowed traditional NLP approaches. The Long Short T e rm Memory (LSTM) [29] architecture paved the way
for the Transformer, which has generated a huge amount of opt imism leading some people to believe that “deep
learning is going to be able to do everything.” 13 However, as already mentioned, the success of the Transform er
and Large Language Models (LLMs) has also served to highligh t their inherent shortcomings. This brings us to
the present, or the “3rd W ave” [1], which seeks to overcome th ose shortcomings by combining deep learning with
symbolic reasoning and knowledge, and by integrating and ex panding on the work of previous decades.
Areas of NLP which are said to beneﬁt from this approach are on es which require some form of reasoning or logic.
In particular, Natural Language Understanding (NLU), Natu ral Language Inference (NLI), and Natural Language
Generation (NLG).
Natural Language Understanding (NLU) is a large subset of NLP containing topics particularly focu sed on
semantics and meaning. The boundaries between NLP and NLU ar e not always clear and open to debate, and even
when they are agreed upon, they’re somewhat arbitrary, as it ’s a matter of convention and a reﬂection of history
[26].
Natural Language Inference (NLI) enables tasks like semantic search, information retrieval , information
extraction, machine translation, paraphrase acquisition , reading comprehension, and question answering. It is the
problem of determining whether a natural language hypothes is h can reasonably be inferred from a given premise
p [30]. For example, the premise “Hazel is an Australian Cattl e Dog”, entails the hypothesis “Hazel is a dog”, and
can be expressed in First Order Logic (FOL) by: p |= h.
Natural Language Generation (NLG) is the task of generating text or speech from non-linguistic (structured)
input [31]. It can be seen as orthogonal to NLU, where the inpu t is natural language. An end-to-end system can be
made up of both NLU and NLG components. When that is the case, w hat happens in the middle is not always that
clear-cut. A neural language model such as GPT3 [21] has no st ructured component, however, whether it performs
“understanding” is subject to debate - Figure 5.
3. Related W ork
Several recent surveys [1, 7, 8, 11, 15–18, 32] cover neuro-s ymbolic architectures in detail. Our aim is not
to produce another NeSy survey, but rather to examine whethe r the promises of NeSy in NLP are materializing.
However, for completeness, and by way of introduction to the subject, we brieﬂy summarize each of these surveys
and provide references for the architectures under review .
In response to recent discussions in the AI community and the resurgence of interest in NeSy AI, Garcez et al. [1]
synthesize the last 20 years of research in the ﬁeld in the con text of the aforementioned debate. The authors highlight
the need for trustworthiness, interpretability, and accou ntability in AI systems, which ostensibly, NeSy is most
10 https://www .cs.bham.ac.uk/~pjh/sem1a5/pt1/pt1_history .html
11 https://nlp.stanford.edu/~wcmac/papers/20140716-UNLU.pdf
12 https://www .youtube.com/watch?v=lI-M7O_bRNg
13 https://www .technologyreview .com/2020/11/03/1011616/ai-godfather-geoffrey-hinton-deep-learning- will-do -everything/

Natural Language 
Understanding
Natural Language 
Generation
(a) Symbolic view - reasoning is performed
explicitly via rules and logic
Natural Language 
Understanding
Natural Language 
Generation
(b) Connectionist view - reasoning is performed
implicitly inside the neural network
Fig. 5. NLU takes as input unstructured text and produces out put which can be reasoned over . NLG takes as input structured data and outputs a
response in natural language.
suited to, in particular when it comes to natural language un derstanding. The authors also emphasize the distinction
between commonsense knowledge and expert knowledge, and su ggest that these two goals may ultimately lead
to two distinct research directions: “those who seek to unde rstand and model the brain, and those who seek to
achieve or improve AI.” Garcez at al. conclude that “Neurosy mbolic AI is in need of standard benchmarks and
associated comprehensibility tests which could in a princi pled way offer a fair comparative evaluation with other
approaches” with a focus on the following goals: learning fr om fewer data, reasoning about extrapolation, reducing
computational complexity, and reducing energy consumptio n14 - Figure 6.
Reasoning
about extrapolation
Learning
from fewer data
Reducing 
computational complexity
Reducing 
energy consumption
Fig. 6. Neuro-Symbolic Artiﬁcial Intelligence promise are as [1]
Sarker et al. [11] survey recent work in the proceedings of le ading AI conferences. The authors review a total of
43 papers and classify them according to Henry Kautz’s categ ories15, as well as an earlier categorisation scheme
from 2005 [33]. Comparing the earlier research to the curren t trends, the authors conﬁrm advancements on both the
neural side, as well as the logic side, with a tendency toward s more expressive logics being explored today than was
thought tractable in the past, and the inﬂuence of the succes s of neural networks on the rise in interest in NeSy in
general. Sarker et al. identify four areas of AI that can bene ﬁt from NeSy approaches: Learning from small data,
Out of distribution handling, Intepretability, and Error r ecovery - Figure 7.
Out of distribution
handling
Learning
from small data
Interpretability Error recovery
?
Fig. 7. Neuro-Symbolic Artiﬁcial Intelligence promise are as [11]
14 Energy consumption is particularly signiﬁcant when traini ng Large Language Models which can cost in the thousands if no t millions of
dollars in electricity [19].
15 Henry Kautz introduced a taxonomy of NeSy types at the Third A AAI Conference on AI [10]. W e rely on this taxonomy to classif y the
studies under review , and discuss each type in detail in sect ion 6.2.3

The authors conclude that “more emphasis is needed, in the im mediate future, on deepening the logical aspects
in NeSy research even further, and to work towards a systemat ic understanding and toolbox for utilizing complex
logics in this context.” Based on the studies in our review , w e come to a similar conclusion.
Garcez et al. [8] survey recent accomplishments for integra ted machine learning and reasoning motivated by
the need for interpretability and accountability in AI syst ems. According to [8], there are three main important
features of a NeSy system: Representation, Extraction, and Reasoning & Learning. Symbolic knowledge can also
be categorized into three groups: rule-based, formula-bas ed, and embedding-based. The authors categorize and
describe the following neuro-symbolic architectures.
Early systems such as KBANN [34] and CILP [35] embed propositional logic in a neural network by constraining
the model parameters - Figure 8.
Fig. 8. Knowledge representation of φ= {A ← B ∧C, B ← C ∧¬ D ∧E, D ← E}using KBANN and CILP . [8]
T ensorizationis a process that embeds ﬁrst order logic (FOL) symbols into r eal-valued tensors. Reasoning is
performed through matrix computation. Examples include Lo gic T ensor Networks (L TNs) [36] and Neural T ensor
Networks (NTLs) [37] - Figure 9.
Fig. 9. Logic T ensor Network (L TN) for P(x, y) → A(y) with G(x) = v and G(y) = u; G are grounding (vector representation) for symbols in
ﬁrst-order language. [8]
In Neural-Symbolic Learning the primary goal is learning, with the assistance of rules an d logic. Different
architectures are characterized by how the logic is incorpo rated into the network, and how it is translated into
differentiable form.
– Inductive Logic Programming (ILP) [38] is a set of techniques for learning logic programs from examples:
* Neural Logic Programming (NLP) [39]
* Differentiable Inductive Logic Programming ( ∂ILP) [40]
* Neural Theorem Prover (NTP) [41]
* Neural Logic Machines (NLMs) [42]

– Horizontal Hybrid Learning combines expert knowledge in the form of rules/logic with da ta, thus are suitable
to knowledge transfer learning (horizontally across domai ns).
– V ertical Hybrid Learning combines symbolic and sub-symbolic modules which take insp iration from
neuroscience in that certain areas of the brain are responsi ble for processing input signals, while other areas
perform logical thinking and reasoning (vertically for a si ngle domain).
Neural-Symbolic Reasoning concerns itself with logical reasoning, as the name suggest s, powered by neural
computation. These consist of model-based, and theorem pro ving approaches. In early theorem proving systems
such as SHRUTI [43] learning capability was limited. On the o ther hand, model-based approaches inside neural
networks have been shown to demonstrate nonmonotonic, intu itionistic, abductive, and other forms of human
reasoning capability. Hence, rather than attempting to per form both learning and reasoning in a single architecture,
more recent designs tend to contain separate learning and re asoning modules which communicate with each other.
The authors conclude that combining symbolic and sub-symbo lic modules, in other words, the compositionality of
neuro-symbolic systems, contributes to the development of explainable and accountable AI [44].
Y u et al. [32] divide neuro-symbolic systems into two types: heavy-reasoning light-learning and heavy-learning
light-reasoning (Figure 10). These are similar to the Neura l-Symbolic Reasoning and Neural-Symbolic Learning
categorization in [8] above. Heavy-reasoning light-learn ing mainly adopts the methods of the symbolic system
heavy reasoning light learning heavy learning light reasoning
Fig. 10. T wo types of neuro-symbolic systems: heavy reasoni ng light learning, and heavy learning light reasoning [32]
to solve the problem in machine reasoning, and introduces ne ural networks to assist in solving those problems,
while heavy-learning light-reasoning mainly applies meth ods of the neural system to solve the problem in machine
learning, and introduces symbolic knowledge in the trainin g process.
– Heavy reasoning light learning (based on Statistical Relat ional Learning (SRL) [45])
* Probabilistic Logic Programming (ProbLog) [46]
* Markov Logic Network (MLN) [47]
* Inductive Logic Programming (ILP) [38]
– Heavy learning light reasoning
* Regularization models add symbols in the form of regular terms to the objective func tion as a kind of prior
knowledge to guide training.
* Knowledge transfer models integrate the knowledge graph that represents semantic inf ormation into the
neural network model, making up for the lack of data by transf erring semantic knowledge. Knowledge
transfer models are mainly used to solve zero-shot learning and few-shot learning [48] tasks.
Besold et al. [7] examine neuro-symbolic learning and reaso ning through the lens of cognitive science, cognitive
neuro-science, and human-level artiﬁcial intelligence. T his is a much more theoretical approach. The authors ﬁrst
describe some early systems such as CILP [35] and ﬁbring, int roduced by Garcez & Gabby [49]. Fibred networks
work on the principle of recursion, where multiple neural ne tworks are connected together, such that a ﬁbring
function in a network A, determines which neurons should be a ctivated in a network B. A key characteristic of
neuro-symbolic systems is modularity, where each network i n the ensemble is responsible for a speciﬁc logic or

task, increasing expressivity and allowing for non-classi cal logics to be represented such as connectionist modal,
intuitionistic, temporal, nonmonotonic, epistemic and re lational logic. Neuro-symbolic computation encompasses
the integration of cognitive abilities - induction, deduct ion, abduction - and the study of mental models. The study
of mental models has a long history, and the authors referenc e research from the ﬁeld of neuro science and cognitive
science, including the “binding” problem, dual process the ory (System 1/System 2), and theories of affect; with
the goal of formulating these in a neuro-symbolic system. Of particular interest to our work are the two sections
on Syntactic Structures, and Compositionality, as they bot h deal with modeling language. Psycho-linguists have
different theories of language morphology (study of the int ernal construction of words 16), with some arguing for
association based explanations (McClelland [50]), while o thers argue for a rule-based one (Pinker [51]) - the
question being whether it is better to model language throug h a connectionist approach, per McClelland, or a
symbolic one, as per Pinker. Whether to model language in a co nnectionist or symbolic manner hinges also on its
inherent compositionality 17.
V on Rueden et al. [17] propose a taxonomy for integrating pri or knowledge into learning systems. This
is an extensive work covering types of knowledge and knowled ge representations, neuro-symbolic integration
approaches, motivations for each approach, challenges and future directions. The authors categorize knowledge into
three types: scientiﬁc knowledge, world knowledge, and exp ert knowledge. Furthermore, knowledge representations
are classiﬁed into eight types - Figure 11.
Fig. 11. T ypes of knowledge representation [17]. Given that our work deals with natural language as input, we are only con cerned with Logic
Rules (which we subdivide into rules and logic) and Knowledg e Graphs (which we subdivide into frames and semantic networ ks) - see section
6.2.2
Zhang et al. [15] survey the area of neuro-symbolic reasonin g on Knowledge Graphs (KGs). The authors
contribute a uniﬁed reasoning framework for Knowledge Grap h Completion (KGC) and Knowledge Graph Question
Answering (KGQA). Among future directions, the authors adv ocate for taking inspiration from human cognition for
neural-symbolic reasoning in KGs, alluding to the dual mode l of human reasoning (System 1/System 2). Additional
future directions include:
– F ew-shot Reasoning which addresses the issue of few labeled examples.
– Reasoning upon Multi-sources which incorporates additional information from unstructu red text.
– Dynamic Reasoning which deals with inferring new facts evolving over time.
– Analogical Reasoning (AR) which involves the use of past experiences to solve problems that are similar to
problems solved before. Case Based Reasoning (CBR) is an exa mple of AR [52].
– Knowledge Graph Pre-training which enables transfer learning for domain adaptation.
Lamb et al. [16] review the state of the art on the use of Graph N eural Networks (GNNs) in NeSy (Figure 12).
Similar to [1] and our work, this survey is motivated by the AI Debate in Montreal. Henry Kautz’s NeSy taxonomy
16 https://www .britannica.com/topic/morphology-linguistics
17 According to Noam Chomsky theory of language, language is co mpositional, in the sense that a sentence is composed of
phrases, which are in turn composed of sub-phrases, and so on , in a recursive manner . This idea enables the construction o f
inﬁnite possibilities from ﬁnite means. This seems particu larly well suited to a symbolic system which, given a ﬁnite se t of rules
should be capable of constructing/deconstructing (reason ing over) all possibilities. In contrast, a sub-symbolic, o r distributional, system
can never see the inﬁnite amount of the data in the universe to learn from. For learning in inﬁnite domains, see also [18].
https://www .britannica.com/biography/Noam-Chomsky/Rule-systems-in-Chomskyan- theories-of- language
18 Tutorial slides associated with [53]: http://snap.stanfo rd.edu/proj/embeddings-www/ﬁles/nrltutorial- part2-g nns.pdf

(a) 
(b) 
Fig. 12. Graph Neural Network (GNN) intuition: generate nod e embeddings based on local neighborhoods, where nodes aggr egate information
from their neighbors using neural networks (a). The network neighborhood deﬁnes a computation graph such that every nod e corresponds to a
unique computation graph (b). The key distinctions are in ho w different approaches aggregate information across the la yers [53]. 18
is used as a foundation for describing NeSy systems. A high le vel overview of state of the art neural architectures
(convolutional layers, recurrent layers, and attention) i s given, followed by a discussion of each of the following:
– Logic T ensor Networks (L TNs) [36] (Figure 9).
– Pointer Networks [54]. Pointer networks are based on the enc oder/decoder with attention (ie. transformer)
architecture, with the modiﬁcation that the input length ca n vary. This architecture lends itself to combinatorial
optimization problems such as the Traveling Salesperson Pr oblem (TSP).
– Graph Convolutional Networks (GCNs) [55] can be thought of a s a generalization of Convolutional Neural
Networks (CNNs) for non-grid topologies.
– Graph Neural Network Model [56] - early GNN architecture sim ilar to GCN.
– Message-passing Neural Networks - similar to GNN with a slig htly modiﬁed update function [16].
– Graph Attention Networks (GA Ts) [57] - implement an attenti on mechanism enabling vertices to weigh
neighbor representations during their aggregation. GA Ts a re known to outperform typical GCN architectures
for graph classiﬁcation tasks.
According to the authors, GNNs endowed with attention mecha nisms “are a promising direction of research towards
the provision of rich reasoning and learning in [Kautz’s] ty pe 6 neuralsymbolic systems.” In NLP , GA Ts have
enabled substantial improvements in several tasks through transfer learning over pretrained transformer language
models, 19 while GCNs have been shown to improve upon the state-of-the- art for seq2seq models [58]. GNN models
have also been successfully applied to relational tasks ove r knowledge bases, such as link prediction [59]. 20 The
authors posit that the application of GNNs in NeSy will bring the following beneﬁts:
– Extrapolation of a learned classiﬁcation of graphs as Hamil tonian, to graphs of arbitrary size.
– Reasoning about a learned graph structure to generalise bey ond the distribution of the training data.
– Reasoning about the partO f (X; Y ) relation (e.g., to make sense of handwritten MNIST digits an d non-digits).
– Using an adequate self-attention mechanism to make combina torial reasoning computationally efﬁcient.
Belle [18] aims to disabuse the reader of the “common misconc eption that logic is for discrete properties, whereas
probability theory and machine learning, more generally, i s for continuous properties.” The author advocates for
tackling problems that symbolic logic and machine learning might struggle to address individually such as time,
space, abstraction, causality, quantiﬁed generalization s, relational abstractions, unknown domains, and unforese en
examples.
19 References to relevant works are not provided.
20 While a detailed review of GNNs in NLP is beyond the scope of th is work, we point the interested reader to an online resource dedicated to
this topic: https://github.com/naganandy/graph- based- deep-learning-literature#computational-linguistics- conferences .

Harmelen & T eije [60] present a conceptual framework to cate gorize the techniques for combining learning
and reasoning via a set of design patterns. “Broadly recogni zed advantages of such design patterns are they distill
previous experience in a reusable form for future design act ivities, they encourage re-use of code, they allow
composition of such patterns into more complex systems, and they provide a common language in a community.” A
graphical notation is introduced where boxes with labels re present symbolic, and sub-symbolic modules, connected
with arrows. Harmelen & T eije’s boxology representation of AlphaGo is given in ﬁgure 13.
data ML sym KR sym
Fig. 13. Schematic diagram using the boxology graphical not ation of the AlphaGo system. Ovals denote algorithmic compo nents (i.e. objects
that perform some computation), and boxes denote their inpu t and output (i.e. data structures) [60].
Earlier surveys [33, 61–64] tend to focus more on logic and lo gic programming, and less on learning, which
is not surprising given that the ground breaking successes i n deep learning are relatively recent. Several themes
run through the above listed works, namely, the inherent str engths and weaknesses of symbolic and sub-symbolic
techniques when taken in isolation, the types of problems wh ich NeSy promises to solve, and the development of
approaches over time.
T wo future directions of particular interest to our work eme rge: building systems which take inspiration from
human cognition and reasoning, and the integration of unstr uctured data. T o our knowledge there is no survey
speciﬁcally covering the application of NeSy computing for Natural Language Processing (NLP) where the input
data is both unstructured and replete with the ambiguities a nd inconsistencies of human reasoning.
4. Contributions
Our aim is to analyze recent work implementing NeSy in the lan guage domain, to verify if the goals of NeSy are
being realized, and to identify the challenges and future di rections. W e brieﬂy describe each of the goals illustrated
in ﬁgure 14, which we have identiﬁed based on our synthesis of the related work outlined above.
Out-of-distribution
Generalization Interpretability Reduced DataTransferability Reasoning
?
Fig. 14. Neuro-Symbolic Artiﬁcial Intelligence Goals
4.1. Out-of-distribution (OOD) Generalization
OOD generalization [65] refers to the ability of a model to ex trapolate to phenomena not previously seen
in the training data. The lack of OOD generalization in LLMs i s often demonstrated by their inability perform
commonsense reasoning, as in the example in Figure 3.
4.2. Interpretability
As Machine Learning (ML) and AI become increasingly embedde d in daily life, the need to hold ML/AI
accountable is also growing. This is particularly true in se nsitive domains such as healthcare, legal, and some
business applications such as lending, where bias mitigati on and fairness are critical. “ An interpretable model is
constrained, following a domain-speciﬁc set of constraint s that make reasoning processes understandable” [66].

4.3. Reduced size of training data
State-of-the-Art (SOT A) language models utilize massive a mounts of data for training. This can cost in the
thousands or even millions of dollars [19], take a very long t ime, and is neither environmentally friendly nor
accessible to most researchers or businesses. The ability t o learn from less data brings obvious beneﬁts. But apart
from the practical implications, there is something innate ly disappointing in LLMs’ ‘bigger hammer’ approach.
Science rewards parsimony and elegance, and NeSy promises t o deliver results without the need for such massive
scale. While this issue can be partially solved by ﬁne tuning a pre-trained LLM using only a small amount labeled
data, these techniques come with their own limitations. For example, Jiang et al. [67] discuss issues such as over-
ﬁtting the data of downstream tasks and forgetting the knowl edge of the pre-trained model.
4.4. T ransferability
Transferability is the ability of a model which was trained o n one domain, to perform similarly well in a different
domain. This can be particularly valuable, when the new doma in has very few examples available for training. In
such cases we might rely on knowledge transfer similar to the way a person might rely on abstract reasoning when
faced with an unfamiliar situation [68].
4.5. Reasoning
According to Encyclopedia Britannica, “T o reason is to draw inferences appropriate to the situation” [69].
Reasoning is not only a goal in its own right, but also the mean s by which the other above mentioned goals can be
achieved. Not only is it one of the most difﬁcult problems in A I21 , it is one of the most contested. Also, a distinction
must be made between human-level reasoning, or what is somet imes referred to as commonsense reasoning, and
formal reasoning. While human-level reasoning can be ambig uous, error-prone, and difﬁcult to specify, formal
reasoning, or logic, follows strict rules and aims to be as pr ecise as possible. The challenge lies in determining
when it is appropriate to deploy one or the other or both, and h ow . In section 7.1 we examine the uses of the term
reasoning in more depth.
5. Methods
Our review methodology is guided by the principles describe d in [70–72]. The data, queries, code, and additional
details can be found in our github repository. 22
5.1. Research Questions
– Is Neuro-symbolic AI meeting its promises in NLP?
1. What are the existing studies on neurosymbolic AI (NeSy) i n natural language processing (NLP)?
2. What are the current applications of NeSy in NLP?
3. How are symbolic and sub-symbolic techniques integrated and what are the advantages/disadvantages?
5.2. Search Process
W e chose Scopus to perform our initial search, as Scopus inde xes most of the top journals and conferences we
were interested in. In addition to Scopus, we searched the AC L Anthology database and the proceedings from
conferences speciﬁc to Neuro-symbolic AI. It is possible we missed some relevant studies, but as our aim is to
21 As expressed by Luis Lamb at https://video.ibm.com/record ed/131288165
22 https://github.com/kyleiwaniec/neuro- symbolic-ai- systematic-review

shed light on the ﬁeld generally, our assumption is that thes e journals and proceedings are a good representation
of the area as a whole. The included sources are listed in Appe ndix C. Since we were looking for studies which
combine neural and symbolic approaches, our query consists of combinations of neural and symbolic terms as well
as variations thereof, listed in table 1. The keywords are de liberately broad, as it would be impossible to come up
with a complete list of all possible keywords relevant to NeS y in NLP . More importantly, the focus of the work is
not on speciﬁc subﬁelds, each of which may warrant a review of its own, but rather on the explicit use of neuro-
symbolic approaches regardless of subﬁeld. Strictly speak ing the only keywords that would cover this would be
neuro-symbolic and its syntactic variants, but we relaxed t his slightly on the basis that works which explore both
symbolic reasoning and deep learning in combination (as per the deﬁnition in section 1) may not necessarily have
used the term neuro-symbolic.
T able 1
Search Keywords
Neural T erms Symbolic T erms Neuro-Symbolic T erms
sub-symbolic symbolic neuro-symbolic
machine learning reasoning neural-symbolic
deep learning logic neuro symbolic
neural symbolic
neurosymbolic
The initial query was restricted to peer-reviewed English l anguage journal articles and conference papers from
the last 3 years, which produced a total of 21,462 results.
5.3. Study selection process
W e further limit the Scopus articles to those published by th e top 20 publishers as ranked by Scopus’s CiteScore,
which is based on number of citations normalized by the docum ent count over a 4 year window 23, and SJR (SCImago
Journal Rank), a measure of prestige inspired by the PageRan k algorithm over the citation network 24, the union
of which resulted in 29 publishers, and eliminated 19,560 st udies, for a total of 1,519 journal articles and 383
conference papers for screening. T wo researchers independ ently screened a sample of each of the 1,902 studies
(articles and conference papers), based on the inclusion/e xclusion criteria in T able 2. The selection process is
illustrated in Figure 15.
The inclusion criteria at this stage was intentionally broa d, as the process itself was meant to be exploratory,
and to inform the researchers of relevant topics within NeSy . As per best practices, this ﬁrst round is also designed
to understand and address inter-annotator disagreement. T his unsurprisingly led to some researcher disagreement
on inclusion, especially since studies need not have been ex plicitly labeled as neuro-symbolic to be classiﬁed as
such. Agreement between researchers can be measured using t he Cohen Kappa statistic, with values ranging from
[-1,1], where 0 represents the expected kappa score had the l abels been assigned randomly, -1 indicates complete
disagreement, and 1 indicates perfect agreement. Our score at this stage came to a modest 0.33. W e observed that it
was not always clear from the abstract alone whether the sub- symbolic and symbolic methods were integrated in a
way that meets the inclusion criteria.
T o attain inter-annotator agreement and facilitate the nex t round of review , we kept a shared glossary of symbolic
and sub-symbolic concepts as they presented themselves in t he literature. W e each reviewed all of the 1,902 studies,
this time by way of a shallow reading of the full text of each st udy. Any disagreement at this stage was discussed in
person with respect to the shared glossary. This process led to 75 journal articles and 106 conference papers marked
for the ﬁnal round of inclusion/exclusion.
23 https://service.elsevier.com/app/answers/detail/a_id/14880/kw/citescore/supporthub/scopus/
24 https://service.elsevier.com/app/answers/detail/a_id/14883/supporthub/scopus/related/1/

T able 2
Inclusion/Exclusion Criteria
Inclusion Exclusion
Input format: unstructured or semi structured text Input fo rmat: structured query , images, speech, tabular
data, categorical data, or any other data type which is not
natural language text.
Output format: Any Application: Theoretical Papers, Position Papers,
Surveys, implementations of software pipelines from
existing models
Application: Implementation of a novel architecture The se arch keywords match, but the actual content does
not
Language: English Full text not available (Authors were contacted in these
cases)
Total studies identified by 
Scopus, ACL, NeSy 
searches:
Journal articles = 2,456
Conference Papers = 
19,006
Studies screened by title 
and abstract
Journal articles = 1,519
Conference papers = 383
Studies screened for 
accessibility
Journal articles = 80
Conference papers = 119 
Studies assessed for 
eligibility based on full 
reading
Journal articles = 75
Conference papers = 106
Studies included in 
analysis
Journal articles = 15
Conference papers = 44
Excluded based on 
automation tools:
Journal articles = 937
Conference papers = 
18,623
Excluded based on 
title and abstract
Journal articles = 1,439
Conference papers = 264
Excluded based on 
inaccessibility
Journal articles = 5
Conference papers = 13
Excluded based on 
inclusion/exclusion criteria
and study quality
Journal articles = 60
Conference papers = 62
Fig. 15. Selection Process Diagram
5.4. Quality Assessment
During the ﬁnal round of inclusion/exclusion, the quality o f each study was determined through the use of a
nine-item questionnaire. Each of the following questions w as answered with a binary value, and the study’s quality
was determined by calculating the ratio of positive answers . Less than a handful of studies were excluded due to a
quality score of less than 50%.
1. Is there a clear and measurable research question?
2. Is the study put into context of other studies and research , and design decisions justiﬁed accordingly (number
of references in the literature review/ introduction)?
3. Is it clearly stated in the study which other algorithms th e study’s algorithm(s) have been compared with?
4. Are the performance metrics used in the study explained an d justiﬁed?
5. Is the analysis of the results relevant to the research que stion?
6. Does the test evidence support the ﬁndings presented?
7. Is the study algorithm sufﬁciently documented to be repro ducible (independent researchers arriving at the
same results using their own data and methods)?
8. Is code provided?
9. Are performance metrics provided (hardware, training ti me, inference time)?

32 
12 
5
7
3
Fig. 16. Study quality
More than 85% of the studies satisfy the requirements listed from Q1 to Q6. However, over 80% of the studies fail to
provide source code or details related to the computing envi ronment which makes the system difﬁcult to reproduce.
This leads to an overall reduction of the average quality sco re to 76.5% - Figure 16.
Finally, a deep reading of each of the eligible studies led to 59 studies selected for inclusion. Data extraction was
performed for each of the features outlined in T able 3. For ac ceptable values of individual features see Appendix B.
The lists of neural and symbolic terms referenced in the tabl e constitute the glossary items learned from conducting
the selection process. Figure 17(a) shows the breakdown of c onference papers vs journal articles, and Figure 17(b)
shows the number of studies published each year.
(a) Publication type
20 
26 
2
11 
(b) Published year
Fig. 17. Publications selected for inclusion
6. Results, Data Analysis, T axonomies
W e perform quantitative data analysis based on the extracte d features in T able 3. Each study was labeled with
terms from the aforementioned glossary, and each term in the glossary was classiﬁed as either symbolic, or neural. A
bi-product of this process are two taxonomies built bottom- up of concepts relevant to the set of studies under review .
The two taxonomies are a reﬂection of the deﬁnition of NeSy pr ovided earlier: “the combination of deep learning
and symbolic reasoning.” T o make this deﬁnition more precis e, we limit the type of combination that qualiﬁes as
neuro-symbolic. Speciﬁcally, the sub-symbolic and symbol ic components must be integrated in a way such that
one informs the other. By way of counter example, a system whi ch is made up of two independent symbolic and
sub-symbolic components would not be considered NeSy if the re is no interaction between them. For example,
while a system where one component is used to process one type of data, and the other is used to process another
type of data may be an effective software pipeline design, we do not consider this type of solution neuro-symbolic
as the two components do not interact in any way. Thus the deﬁn ition becomes “the integration of deep learning
and symbolic reasoning.” It should be noted, that these term s are not always consistently deﬁned in the literature.

T able 3
Data extraction features
Feature Description
Business application The stated objective or application o f the proposed study . Often
this is an NLP task, but this is not a requirement (i.e., “Medi cal
decision support”)
T echnical application T ype of model output
T ype of learning Indicates learning method (supervised, un supervised, etc.)
Knowledge representation One of four categories: Rules, Lo gic, Frames, and Semantic
networks
T ype of reasoning Indicates whether knowledge is represent ed implicitly (embedded)
or explicitly (symbolic)
Language structure Indicates whether linguistic structur e is leveraged to facilitate
reasoning
Relational structure Indicates whether relational struct ure is leveraged to facilitate
reasoning (e.g., part-of-speech tags, named entities, etc .)
Symbolic terms List of symbolic techniques used by the model s
Neural terms List of neural architectures used by the models
Datasets List of all datasets used for evaluation
Model description Describes model architecture schematic ally
Evaluation Metrics Evaluation metrics reported by the auth ors
Reported score Model performance reported by the authors
Contribution Novel contribution reported by the authors
Key-intake Short description of the study
isNeSy Indicates whether the authors label their study as Ne uro-Symbolic
NeSy goals For each of the goals listed in Section 1, indicate s whether the goal
is met as reported by the authors
Kautz category List of categories from Kautz’ s taxonomy
NeSy category List of categories from the proposed nomencla ture
Study quality Percentage of positive answers in the quality assessment
questionnaire
For example, in a much earlier survey, [33] split the interre lation (type of combination) of neuro-symbolic systems
into hybrid and integrated, whereas we use the term integrated to cover both.
On the learning side, we have neural architectures (describ ed in Section 6.2.1), and on the symbolic reasoning
side we have knowledge representation (described in Sectio n 6.2.2). These results are rendered in T able 4, with the
addition of color representing a simple metric, or promise score , for each study. The promise score is simply the
number of goals reported to have been satisﬁed by the solutio n in the study.
6.1. Exploratory Data Analysis
W e plot the relationships between the features extracted fr om the studies, and the goals from section 4 in an effort
to identify any correlations between them, and ultimately t o identify patterns leading to higher promise scores.
6.1.1. Business and T echnical Applications
The business application is the stated application, or objective, of a given study. It is often but not always an NLP
task, such as text classiﬁcation , or sentiment analysis . It should be noted that in this example, sentiment analysis is

a type of text classiﬁcation, but while one author’s stated o bjective is speciﬁc to sentiment, another author may be
interested in solving for text classiﬁcation in general. As such there is no particular hierarchy or taxonomy associate d
with business applications. The relationship between all t asks, or business applications, and NeSy goals is shown in
Figure 18.
Emotion Recognition
Sentiment Analysis
Text Games 
Dialog System
N2F
Kg Completion / Link Prediction
Entity Linking
Relation Extraction
Image Captioning
Opnion Extraction
Annotation
Reading Comprehension
Text Classification 
Causal Reasoning
Question Answering
Decision Support
Argumentation Mining
Language Modeling
Information Extraction
Entity Resolution
Text Summarization 
Reasoning
OOD
Interpretability
Reduced Data
Transferability 
None
Fig. 18. Relationship between Business Applications and Ne Sy Goals. Question answering is the most frequently occurri ng task, and is associated
mainly with reasoning, reduced data, and to a lesser degree, interpretability .
The business application largely determines the type of mod el output, or what we term technical application .
Most business applications are associated with a single (or at most two) technical applications. The exceptions
being question answering and reading comprehension , which have been tackled as both inference and classiﬁcatio n
problems, or with the goal of information extraction or text generation. Question answering is the most frequently
occurring task, and is associated mainly with reasoning, re duced data, and to a lesser degree, interpretability. On a
philosophical level this seems somewhat disappointing, as one would hope that in receiving an answer, one could
expect to understand why such an answer was given.
For completeness, the number of studies representing the te chnical applications and most frequently occurring
business application is given in Figure 19, while Figure 20 i llustrates the relationship between business application s,
technical applications, and goals.
Question answering
Text classification
Reading comprehension
Sentiment analysis
KG Completion / link prediction
10
7
5
5
5
(a) T op Business Applications (b) T echnical Applications (model output)
Fig. 19. Number of studies in each application category
6.1.2. T ype of learning
Machine learning algorithms are classiﬁed as supervised, u nsupervised, semi-supervised, curriculum or
reinforcement learning, depending on the amount and type of supervision required during training [73–75]. Figure
21 demonstrates that the supervised method outnumbers all o ther approaches.

Emotion Recognition
Sentiment Analysis
Text Games 
Dialog System
N2F
Kg Completion / Link Prediction
Entity Linking
Relation Extraction
Image Captioning
Opnion Extraction
Annotation
Reading Comprehension
Text Classification 
Causal Reasoning
Question Answering
Decision Support
Argumentation Mining
Language Modeling
Information Extraction
Entity Resolution
Text Summarization 
Similarity
Classification
Generative
Inference
Information 
Extraction
Reasoning
OOD
Interpretability
Reduced Data
Transferability 
Generative
SimilaritySimilaritySimilarity
None
Fig. 20. Relationship between Business Applications, T ech nical Applications, and NeSy Goals
Similarity
Classification
Type of Learning 
Technical Application 
(Model Output) NeSy Goals
Generative
Inference
Information 
Extraction
Semi-supervised
Unsupervised
Supervised
Reinforcement
Reasoning
OOD
Interpretability
Reduced Data
Transferability 
None
Fig. 21. Relationship between Learning T ype, T echnical App lication, and NeSy Goals. It is clear that supervised approa ches dominate the ﬁeld,
are applied across a variety of technical applications, and there is no clear winner when it comes to goals.
6.1.3. Implicit vs Explicit Reasoning
The subset of tasks belonging to Natural Language Understan ding (NLU) and Natural Language Generation
(NLG) are often regarded as more difﬁcult, and presumed to re quire reasoning. Given that reasoning was one of the
keywords used for search, it is not surprising that many stud ies report reasoning as a characteristic of their model(s).
How reasoning is performed often depends on the underlying r epresentation and what it facilitates. Sometimes
the representations are obtained via explicit rules or logi c, but are subsequently transformed into non-decomposable
embeddings for learning. As such, we can say that any reasoni ng during the learning process is done implicitly.
Studies utilizing Graph Neural Networks (GNNs) [76–82] wou ld also be considered to be doing reasoning implicitly.
The majority of the studies doing implicit reasoning levera ge linguistic and/or relational structure to generate thos e
internal representations. These studies meet 53 out of a pos sible 180 NeSy goals, where 180 = #delete/goals * #delete/studies,
or 29.4%. For reasoning to be considered explicit, rules or l ogic must be applied during or after training. Studies
which implement explicit reasoning perform slightly bette r, meeting 51 out of 135 goals, or 37.8% and generally
require less training data. Additionally, 4 studies implem ent both implicit and explicit reasoning, at a NeSy promise
rate of 40%. Of particular interest in this grouping is Bianc hi et al. [83]’s implementation of Logic T ensor Networks
(L TNs), originally proposed by Seraﬁni and Garcez in [84]. “ L TNs can be be used to do after-training reasoning
over combinations of axioms which it was not trained on. Sinc e L TNs are based on Neural Networks, they reach
similar results while also achieving high explainability d ue to the fact that they ground ﬁrst-order logic” [83]. Also

in this grouping, Jiang et al. [85] propose a model where embe ddings are learned by following the logic expressions
encoded in huffman trees to represent deep ﬁrst-order logic knowledge. Each node of the tree is a logic expression,
thus hidden layers are interpretable.
Figure 22 shows the relationship between implicit & explici t reasoning and goals, while the relationship between
knowledge representation, type of reasoning, and goals is s hown in Figure 23.
Both
Implicit
Explicit
Reasoning
OOD
Interpretability
Reduced Data
Transferability 
None
Fig. 22. T ype of Reasoning and Goals. Around half, 48%, of stu dies where reasoning is performed explicitly mention inter pretability as a feature.
While nearly a third of studies performing reasoning implic itly do not meet any of the NeSy promises identiﬁed for this re view .
Semantic Network
Frames
Rules
Logic
Both
Implicit
Explicit
Reasoning
Reasoning NeSy GoalsKnowledge Representation
OOD
Interpretability
Reduced Data
Transferability 
None
Fig. 23. Knowledge Representation, T ype of Reasoning, and G oals. What is noteworthy , is that when Semantic Networks are utilized, reasoning
is almost always done implicitly . The two exception are [83] , and [77]. However, [83] utilizes FOL for explicit reasonin g rather than its network
component. On the other hand, [77] generate a novel interpre table reasoning graph as the output of their model.
6.1.4. Linguistic and Relational Structure
In the previous section we described how linguistic and rela tional structures can be leveraged to generate internal
representations for the purpose of implicit reasoning. Her e we plot the relationships between these structures and
other extracted features and their interactions - Figure 24 . Perhaps the most telling chart is the mapping between
structures and goals, where many the studies leveraging lin guistic structure do not meet any of the goals. This runs
counter to the intuition that language is a natural ﬁt for NeS y.

Emotion Recognition 
Sentiment Analysis 
Text Games 
Dialog System 
N2F
KG Completion / Link Prediction 
Relation Extraction 
Image Captioning 
Opnion Extraction 
Annotation 
Reading Comprehension 
Text Classiﬁcation 
Causal Reasoning 
Question Answering 
Decision Support 
Argumentation Mining 
Language Modeling 
Information Extraction 
Entity Resolution 
Text Summarization 
Reasoning 
OOD
Interpretability 
Reduced Data 
Transferability 
None 
Semantic Network 
Frames 
Rules 
Logic
Both 
Implicit 
Explicit 
Reasoning 
OOD
Interpretability 
Reduced Data 
Transferability 
None 
Classiﬁcation
Generative 
Inference 
Information Extraction 
Similarity
Classiﬁcation 
Generative 
Inference 
Information 
Extraction 
Reasoning 
OOD
Interpretability 
Reduced Data 
Transferability 
None 
Emotion recognition 
Sentiment analysis 
Text games 
Dialog system 
N2f
Kg completion / link prediction 
Entity linking
Relation extraction 
Image captioning 
Opnion extraction 
Annotation 
Reading comprehension 
Text classiﬁcation 
Causal reasoning 
Question answering 
Decision support 
Argumentation mining 
Language modeling 
Information extraction 
Entity resolution 
Text summarization 
Semi-supervised
Unsupervised 
Supervised
Reinforcement 
Compiled
Cooperative 
Nested 
Sequential
Linguistic Structure (LS) 
Relational Structure (RS) 
LS 
LS 
LS 
LS 
LS 
LS 
LS 
LS 
RS 
RS 
RS 
RS RS 
RS 
RS 
RS 
a) NeSy Goal b) NeSy Category
c) Technical Application d) Knowledge Representation
e) Reasoning Type -> NeSy Goal f) Technical Application -> NeSy Goal 
g) Business Use Case h) Business Use Case -> Learning Type 
Fig. 24. Relationships between leveraged structures and ex tracted features. As can be seen in a), e), and f), studies lev eraging linguistic structures
often do not meet any NeSy goals, which runs counter to our ori ginal hypothesis. Further investigation into this phenome non may be warranted.
Note: studies which do no leverage either structure are not s hown

6.1.5. Datasets and Benchmarks
Each study in our survey is based on a unique dataset, and a var iety of metrics. Given that there are nearly as
many business applications, or tasks, as there are studies, this is not surprising. As such it is not possible to compare
the performance of the models reviewed. However, this bring s up an interesting question, and that is how one might
design a benchmark for NeSy in the ﬁrst place. A discussion ab out benchmarks at the IBM Neuro-Symbolic AI
W orkshop 202225 resulted in general agreement that the most important chara cteristic of a good benchmark for NeSy
is in the diversity of tasks tackled. Gary Marcus pointed out that current benchmarks can be solved extensionally,
meaning they can be “gamed”. 26 In other words, with enough attempts, a model can become very good at a speciﬁc
task without solving the fundamental reasoning challenge. In essence, this akin to over-ﬁtting on the test set. The
phenomenon can be exposed when adversarial examples are int roduced such as described in [86], or through the
observation that spurious correlations can be introduced i n the annotation process as per [87]. This leads to models
which are not able to generalize out of the training distribu tion. In contrast, to solve a task intensionally is to
demonstrate “understanding” which is transferable to diff erent tasks. This view is controversial with advocates of
purely connectionist approaches arguing that “understand ing” is not only ill deﬁned, but also a moving target [1] -
every time we solve for the current deﬁnition of understandi ng, the deﬁnition is revised to have to meet a higher bar.
So instead of worrying about the semantics of “understandin g”, the panelists agreed that to make the benchmarks
robust to gaming is to build in enormous variance in the types of tasks they tackle. T aking this a step further, Luis
Lamb27 proposed that instead of designing benchmarks for testing m odels, we should be designing challenges which
encourage people to work on important real world problems. F or a deeper dive, see the ACL-2021 W orkshop on
Benchmarking: Past, Present and Future (BPPF) 28 , where some of the same issues pertaining speciﬁcally to NLP
and NLU were discussed, as well as the challenges in interpre ting performances across datasets, models, and with
the evolution of language and context over time.
6.2. T axonomies: Neural, Symbolic, & Neuro-Symbolic
6.2.1. Neural
In the main, the extracted neural terms refer to the neural ar chitecture implemented in a given study. W e group
these into higher level categories such as Linear models, Ea rly generation (which includes CNNs), Graphical
models, Sequence-to-Sequence - Figure 25. W e have included Transformers in the Sequence-to-Sequence category
as the original architecture was an encoder/decoder with at tention. It should be noted that not all Transformers
since then employ both an encoder and decoder, or generate se quences. What they have in common is the attention
mechanism described in the seminal paper Attention Is All Y o u Need, by V aswami et al. [3] which dramatically
advanced NLP research. W e also include here Neuro-Symbolic architectures such as Logic T ensor Networks (L TN),
Recursive Neural Knowledge Networks (RNKN), T ensor Produc t Representations (TPRs), and Logical Neural
Networks (LNN) because they are suitable to optimization vi a gradient descent - Figure 26. W e include one study
[88] which does not implement gradient descent, but rather N euroevolution (NE). Neuroevolution involves genetic
algorithms for learning neural network weights, topologie s, or ensembles of networks by taking inspiration from
biological nervous systems [89, 90]. Neuroevolution is oft en employed in the service of Reinforcement Learning
(RL). Studies which do not specify a particular architectur e are categorised as Multilayer Perceptron (MLP).
6.2.2. Symbolic
The deﬁnition we adopted states that NeSy is the integration of deep learning and symbolic reasoning . Our neural
taxonomy described above reﬂects the deep learning component. For the symbolic reasoning component we utilize
four common Knowledge Representation (KR) categories: 1) p roduction rules, 2) logical representation, 3) frames,
and 4) semantic networks [91–96]. The following deﬁnitions are merely a glimpse at each of these topics, in order
to provide a basic intuition.
25 https://video.ibm.com/recorded/131288165
26 https://video.ibm.com/recorded/131288165 time-marker 43:00
27 https://video.ibm.com/recorded/131288165 time-marker 50:00
28 https://github.com/kwchurch/Benchmarking_past_present_future#S1

Convolutional Neural Network (CNN) 
input
convolution
pooling
fully
connected output
 Multilayer Perceptron (MLP) 
input output hidden layers
Neuroevolution (NE) 
evaluation selection
crossovermutation
Graph Neural Network (GNN) 
neural network
input graph
neighborhood aggregation
Sequence-to-Sequence (Seq2Seq) 
encoder
decoderinput
output
x1 x2 xn-1 xn
encoder state 
RNN RNN RNN RNN RNN RNN RNN RNN 
Transformer (e.g. BERT) 
encoder
decoder
output
y1 y2 yn-1 yn
y1 y2 yn-1 
input
attention
x1 x2 xn-1 xn
h1
h0
h2 hn-1 hn s1 s2 sn-1 sn
RNN RNN RNN RNN Z
W
RNN RNN RNN RNN 
WX+b WX+b WX+b WX+b 
Fig. 25. Neural architectures represented in T able 4
Logic Tensor Networks(LTN) Recursive Neural Knowledge Networks (RNKN) 
Tensor Product Representation (TPR) Logic Neural Networks (LNN)
u = ⟨ u1, . . . .,u n⟩
G(P(v,u) → A(u)) 
v = ⟨ v1, . . . .,v n⟩
1-/u1D70E
uP
th th 
++
W 1
P W 2
P V 1
P V 2
P B 1
P B 2
P
1-/u1D70E
th th 
+
+ =
+
W 1
A W 2
A V 1
A V 2
A B 1
A B 2
A
uA
max
p(3)
1 p(2)
2&
p(2)
1 p(1)
3&
p(3)
1
p(2)
1
p(1)
1
p(1) layer
p(2) layer
p(3) layer
Root layer
Input layer
p(1)
2 p(1)
3 p(1)
4 p(1)
5
p(1)
1 p(1)
2&
limb weakness
⇒ heart failure
nausea
⇒ heart failure
checst congestion
⇒ heart failure
palpitations
⇒ hyperthiroid ... 
chest congestion
⇒ hyperthiroid ... 
p(2)
2
p(1)
1 p(1)
2&
limb weakness nausea heart failure chest congestion palitations heart failure
Whiskers Tail Cat Dog
Pet
Laser pointer Chases
→
→ →
⊗ ⊗
(Whiskers ⊗ Tail ⊗ (Laser pointer → Chases)) → Cat
(Cat ⊗ Dog) → Pet  Dog) 
LOVER 
John Mary John loves Mary 
BELOVED 
Fig. 26. Neuro-symbolic architectures represented in T abl e 4
1. Production rules - A production rule is a two-part structure comprising an ant ecedent set of conditions and a
consequent set of actions [94]. W e usually write a rule in thi s form:
I F conditions T H E N actions ex ) I F Bird T H E N f ly
2. Logical representation - Logic is the study of entailment relations—languages, tru th conditions, and rules of
inference. [94, 97]. A logic includes:

– Syntax : speciﬁes the symbols in the language and how they can be comb ined to form sentences. Hence
facts about the world are represented as sentences in logic.
– Semantics : speciﬁes what facts in the world a sentence refers to. Hence , also speciﬁes how you assign a
truth value to a sentence based on its meaning in the world. A f act is a claim about the world, and may be
true or false.
– Inference Procedure (reasoning) : mechanical method for computing (deriving) new (true) sen tences from
existing sentences.
The sentence "Not all birds can ﬂy" in First Order Logic (FOL) looks like:
¬ (∀xBird (x) → F ly(x))
FOL is by no means the only choice, but as per [94] it is a simple and convenient one for the sake of illustration.
Natural Logic (NL) for example, is a formal proof theory buil t on the syntax of human language, which can be
traced to the syllogisms of Aristotle [98]. “For better or wo rse, most of the reasoning that is done in the world
is done in natural language. And correspondingly, most uses of natural language involve reasoning of some
sort. Thus it should not be too surprising to ﬁnd that the logi cal structure that is necessary for natural language
to be used as a tool for reasoning should correspond in some de ep way to the grammatical structure of natural
language” [99]. Implementations and extensions include [3 0, 100–102]. Real-valued logics are often utilized
in machine learning because they can be made differentiable and/or probabilistic [36] - ﬁrst introduced by
Łukasiewicz at the turn of the 20th century [103, 104]). Othe r, logic-based cognitive modelling approaches
such as non-monotonic logic, attempt to deal with the comple xities of human reasoning, epistemology, and
defeasible inference [105].
3. Frames - Frames are objects which hold entities, their properties a nd methods. An individual frame schema
looks like this:
(F rame − name
< slot − name1 f iller 1 >
< slot − name2 f iller 2 >
... )
(Penguin
canF ly : 0
isA : ′′Bird′′
... )
The frame and slot names are atomic symbols; the ﬁllers are ei ther atomic values (like numbers or strings) or
the names of other individual frames [94]. This is similar to Object Oriented Programming (OOP), where the
frame is analogous to the object, and slots and ﬁllers are pro perties and values respectively.
4. Semantic networks - A semantic network is a structure for representing knowled ge as a pattern of
interconnected nodes and edges [96]. A Frame network is a kin d of semantic network where nodes are frames,
and edges are the relationships between nodes. An example of a semantic network often used in NLU systems
is W ordNet 29 - a lexical database of English - Figure 27. T oday semantic ne tworks are more often referred to
as Knowledge Graphs (KGs). 30
T able 4 shows which studies combine which of the above neural (6.2.1) and symbolic (6.2.2) categories as well
as the number of NeSy goals satisﬁed.
6.2.3. Neuro-Symbolic
NeSy systems can be categorized according to the nature of th e combination of neural and symbolic techniques.
At AAAI-20, Henry Kautz presented a taxonomy of 6 types of Neu ro-Symbolic architectures with a brief example of
each [10]. While Kautz has not provided any additional infor mation beyond his talk at AAAI-20, several researchers
29 https://wordnet.princeton.edu/
30 This term was popularized after Google introduced contextu al information to search results from their semantic networ k under the brand
name Knowledge Graph https://blog.google/products/search/introducing-knowledge-graph-things-not/ .

hypernym
attribute
similar
temperature
antonym
hot
cold
body temperature,
blood heat
coldness, cold, low
temperature, frigidity,
frigidness
arctic, frigind, gelid,
glacial, icy, polsr
Fig. 27. English W ordNet subgraph [106]
have formed their own interpretations [1, 11, 16]. W e have ca tegorized all the reviewed studies according to Kautz’s
taxonomy as well as our proposed nomenclature - Figure 28. T a ble 7 in Appendix A lists all the studies by category.
Neuro-Symbolic Categories 
SequentialEnsemble
Fibring
Integrated
Nested
1. symbolic Neuro symbolic
2. Symbolic[Neuro] 
6. Neuro[Symbolic] 
3. Neuro; Symbolic 
4. Neuro: Symbolic → Neuro 
5. Neuro_Symbolic 
Cooperative
Compiled
Fig. 28. Proposed Neuro-Symbolic Artiﬁcial Intelligence c ategories. Adapted from Henry Kautz.
T ype 1 symbolic Neuro symbolic is a special case where symbolic knowledge (such as words) is transformed into
continuous vector space and thus encoded in the feature embe ddings of an otherwise “standard” ML model. W e
opted to include these studies if the derived input features belong to the set of symbolic knowledge representations
described in Section 6.2 - Figure 29. One could still argue th at this is simply a case of good old fashioned feature
engineering, and not particularly special, but we want to ex plore the idea that deep learning can perform reasoning,
albeit implicitly, if provided with a rich knowledge repres entation in the pre-processing phase. W e classify these
studies as Sequential. Evaluating these studies as a group was particularly chall enging as they have very little in
common including different datasets, benchmarks and busin ess applications. Half of the studies do not mention
reasoning at all, and the ones that do are mainly executing ru les on candidate solutions output by the neural models
post hoc. In aggregate, only 26 out of a total of 115 (23 studie s * 5 goals), or 22.6%, possible NeSy goals were met.
T ype 2 Symbolic[Neuro] is what we describe as a Nested architecture, where a symbolic reasoning system is the
primary system with neural components driving certain inte rnal decisions. AlphaGo is the example given by Kautz,

T able 4
Neural & Symbolic Combinations
1 2 3 4 5 Number of NeSy goals satisﬁed out of the 5 described in Sectio n 4.
Note: some studies use multiple techniques.
Knowledge Representation
Frames Logic Rules Semantic
network
Linear Models SVM [107] [108] [88]
Early
Generation
MLP [109]
[110, 111]
[112, 113]
[114]
[115]
[116] [81]
CNN [117] [113] [118] [119] [120]
Graphical
Models
DBN
[118]
GNN [80] [76] [82] [78, 81]
[79] [77]
Sequence-
to-Sequence
RNN [117, 121]
[122] [123]
[124], [125], [126]
[127] [118, 128]
[129]
[130] [131] [132]
[133] [134] [135]
[136] [137]
[120, 138]
[139]
[140]
[141]
RcNN [85] [142]
Transformer [143, 144]
[145] [146]
[147, 148]
[129, 149]
[150], [134]
[151] [152]
[138] [153]
[78, 154]
[81]
Neuro-
Symbolic
L TN
[83]
RNKN [85]
LNN [155] [152]
TPR [123] [142]
Neuroevolution [88]
S
N
V
D N
NP 
VP 
+
WSD, POS, NER, Generalization 
Symbolic knowledge extraction 
with WordNet and linguistic structures 
Skipgram 
model 
(Word2Vec, 
Fasttext) 
Seq2Seq 
generative 
Neural 
Network
Real valued 
vector 
representation 
OUTPUT:
summary
INPUT:
Unstructured 
text document 
Fig. 29. T ype 1 Sequential. A symbolic knowledge representation module is used to gene rate rich embeddings for downstream machine learning
[138].

where the symbolic system is a Monte Carlo Tree Search with ne ural state estimators nominating next states. W e
found four studies that ﬁt this architecture. W e use [115] fo r the purposes of illustration - Figure 30.
+
NeSy Program Synthesizer 
DSL (Domain Specific Language) 
with internal neural components 
Transductive Learning 
module
Unlabeled webpages 
OUTPUT:
answers for 
each webpage 
Natural language 
query 
x
x
x
x
x
x
x
x
GetLeaves( 
    GetDescendents( 
 /u1D45F , /u1D706/u1D467 .matchKeyword(/u1D467, /u1D43E )))
Labeled webpages 
Fig. 30. T ype 2 Nested. Given a natural language query and a set of web pages, the sys tem outputs answers for each page. A symbolic reasoner,
which uses a custom Domain Speciﬁc Language (DSL) to travers e the HTML, interacts with internal neural modules such as BE R T which
perform a number of Natural Language Processing tasks. What is learned is a DSL program, using only a few labeled examples , which can
generalize to a large number of heterogeneous web pages. The authors report large improvements in precision and recall s cores over state-of-the
art, in some cases over 50 points [115].
T ype 3 Neuro; Symbolic is what we call Cooperative. Here, a neural network focuses on one task (e.g. object
detection) and interacts via input/output with a symbolic r easoner specializing in a complementary task (e.g. query
answering). Unstructured input is converted into symbolic representations which can be solved by a symbolic
reasoner, which in turn informs the neural component which l earns from the errors of the symbolic component. This
process is iterated until convergence or a satisfactory out put is produced. There are nine studies in this category, all
but one of which utilize rules and/or logic for knowledge rep resentation. A common theme among the cooperative
architectures is the business application of question answ ering. The Neuro-Symbolic Concept Learner (NS-CL)
[137] - Figure 31 - is an example of T ype 3, meeting 4 out of the 5 NeSy goals. Its ability to perform well with
reduced data is particularly impressive: “Using only 10% of the training images, our model is able to achieve
comparable results with the baselines trained on the full da taset.” Similarly, [116] report perfect performance on
small datasets which they also attribute to the use of explic it and precise reasoning. Both studies display similar
limitations, the use of synthetic datasets, and the need for handcrafted logic, a DSL (Domain Speciﬁc Language)
in the case of [137], and Image Schemas in [116]. Six out of the nine studies leverage linguistic structures in
some fashion, and in particular, [146] utilize natural logic , for a model which is both interpretable, and achieves
state-of-the-art performance on two QA datasets. This work builds on [30, 101].
T ypes 4 and 5, Neuro: Symbolic → Neuro and Neuro_Symbolic respectively, were originally presented by Kautz
under one heading. After his presentation, Kautz modiﬁed th e slide deck 31 separating these two types into systems
where knowledge is compiled into the network weights, and wh ere knowledge is compiled into the loss function. In
T ypes 4 and 5, reasoning can be performed both implicitly and explicitly, in that it is calculated via gradient descent,
but can also be performed post hoc. W e have grouped studies be longing to these two categories under the moniker
of Compiled systems, of which there are sixteen and seven respectively.
Deep Learning For Mathematics [156] is the canonical exampl e of T ype 4, where the input and output to the
model are mathematical expressions. The model performs sym bolic differentiation or integration, for example, given
x2 as input, the model outputs 2x. The model exploits the tree structure of mathematical expr essions, which are
fed into a sequence-to-sequence architecture. This seems l ike a particularly ﬁtting paradigm for natural language
applications on the basis that structures such as parse tree s can be similarly leveraged to output other meaningful
structures such as for example: cause and effect relationsh ips as exempliﬁed in [134] and [150], or the generation
of argument schemes as per [76]. The downside of many of these types of systems is the need for hand-crafted
31 https://henrykautz.com/talks/index.html

Visual Representation 
Obj 1 
Obj 2 
Obj 3 
Obj 4 
Concept Embeddings
Semantic Parsing (Candidate Interpretations)
Back-propagation
Symbolic Reasoning
Answer: Cylinder
Groundtruth: Box
REINFORCE
Back-propagation
Sphere 
Query(Shape, Filter(Red, Relate(Left, Filter(Sphere)))) 
Query(Shape, Filter(Sphere, Relate(Left, Filter(Red)))) 
Exist(AERelate(Shape, Filter(Red, Relate(Left, Filter(Sphere))))) 
Q: What is the shape of 
the red object left of the 
sphere?
✓
ᅜ
ᅜ
/u1D6AF v
/u1D6AF s
Fig. 31. T ype 3 Cooperative. The Neuro-Symbolic Concept Learner (NS-CL) jointly learn s visual concepts, words, and semantic parsing of
sentences without any explicit annotations. Given an input image, the visual perception module detects objects in the s cene and extracts a deep,
latent representation for each of them. The semantic parsin g module translates an input question in natural language in to an executable program
given a domain speciﬁc language (DSL). The generated progra ms have a hierarchical structure of symbolic, functional mo dules, each fulﬁlling
a speciﬁc operation over the scene representation. The expl icit program semantics enjoys compositionality , interpre tability , and generalizability
[137].
rules and logic [125, 133, 150, 152]. In contrast, [155] lear n rules from data (rule induction) by combining Logical
Neural Networks (LNN) with text-based Reinforcement Learn ing (RL). One could argue that this is a combination
of T ype 4, compiled (logic embedded in the network), and T ype 3, cooperative (symbolic and sub-symbolic modules
learning from each other in an iterative fashion). [155] is t he only work we found which meets all ﬁve promises, and,
it outperforms previous SOT A approaches - Figure 32. Anothe r example of a T ype 4 system in our set of studies is
Observation: You find yourself in a bedroom. An usual one. I guess you better just go 
and list everything you see here. There is an exit to the north. Don’t worry, it is 
unguarded. There is an exit to the south. Don’t worry, it is unblocked. You don’t like 
doors? Why not try going west, that entranceway is unguarded.
Symbolic facts: hasExit(bedroom, north), hasExit(bedroom, south), 
hasExit(dedroom, west), hasVisited(bedroom, south) 
Posible actions: go(x, west), go(x, north) 
Final sampled output action: go west 
go(x, y) ← hasExit(x, y)∧¬ hasVisited(x, y)∧¬ hasCoin(x) take(x) ← hasCoin(x)
hasExit(x, y)  ¬hasExit(x, y)  hasVisited(x, y)  ¬hasVisited(x, y)  hasCoin(x, y)  ¬hasCoin(x, y)
∧ ∧
∧ ∧Logic: go(x,y) 
Logic: take(x) 
0.5 0.5
0.83
0.17
0.99
0.99
0.99
Fig. 32. T ype 4 Compiled. SymboLic Action policy for Textual Environments ( SLA TE) learns interpretable action policy for each action verb,
go and take, from ﬁrst-order symbolic states. The goal is to learn symbo lic rules as logical connectives for generating action comm ands by
gradient-based training [155].
proposed by [85]. Here, knowledge is encoded in the form of hu ffman trees made of triples and logic expressions,
in order to jointly learn embeddings and model weights - Figu re 33. The model is intended for medical diagnosis
decision support, where a requisite characteristic is inte rpretability, and this model meets that goal.
T ype 5 comprises T ensor Product Representations (TPRs) [15 7], Logic T ensor Networks (L TNs) [36], Neural
T ensor Networks (NTN) [37] and more broadly is referred to as tensorization, where logic acts as a constraint.
LT N EE [83] is an example of a compiled T ype 5 system - Figure 34.
T ype 6 Neuro[Symbolic] is the most tightly integrated but perhaps the most elusive a s there do not appear to be
any recent implementations in existence. According to Kaut z, this is the ultimate NeSy system which should be
capable of efﬁcient combinatorial reasoning at the level of super-intelligence, if not human intelligence.

p(3)
1 p(2)
2&
p(2)
1 p(1)
3&
p(3)
1
p(2)
1
p(1)
1
p(1) layer
p(2) layer
p(3) layer
Root layer
Input layer
p(1)
2 p(1)
3 p(1)
4 p(1)
5
p(1)
1 p(1)
2&
limb weakness
⇒ heart failure
nausea
⇒ heart failure
checst congestion
⇒ heart failure
palpitations
⇒ hyperthiroid ... 
chest congestion
⇒ hyperthiroid ... 
p(2)
2
p(1)
1 p(1)
2&
limb weakness nausea heart failure chest congestion palitations heart failure
Fig. 33. T ype 4 Compiled. Huffman tree of the Recursive Neural Knowledge Network (RN KN), representing deep ﬁrst-order logic knowledge.
The ﬁrst layer of the tree consists of entities, the second la yer consists of relations (x → y). Higher layers compute logic rules. The root node
is the ﬁnal embedding representing a document (in this case a single health record). Back propagation is used for optimiz ation with softmax for
calculating class probabilities [85].
Commonsense Knowledge Axiomatic Knowledge
•  Text annotated with entity linking 
•  Entities dbr:cat and dbr:tiger 
    appear in similar contexts. 
•  Entity Embeddings:
•  v(dbr:cat) ≈ v(dbr:tiger) 
species( dbr:cat )
mammal( dbr:tiger )
bird( dbr:penguin )
[...]
∀x (mammal( x) → animal( x)) 
Instantiated atoms
dbr:cat 
dbr:tiger 
dbr:penguin 
Universaly quantified formuls 
dbr:cat 
dbr:tiger 
dbr:penguin 
embedding
Sub-symbolic commonsense knowledge Sub-symbolic commonsense knowledge with learned predicates
LTN 
After Training Inferences:
animal( dbr:cat ) ?
∀x (species( x) → animal( x)) 
mammal
animal
species
learning predicates with
commonsnse and 
axiomatic knowledge
Fig. 34. T ype 5 Compiled. LT N E E - Using Logic T ensor Networks (L TNs) it is possible to integr ate axioms and facts (using ﬁrst-order fuzzy
logic to represent terms, functions, and predicates in a vec tor space) with commonsense knowledge represented in a sub- symbolic form (based
on the principle of distributional semantics and implement ed with W ord2V ec) in one single model performing well in reas oning tasks. The major
contribution of this work is to show that combining commonse nse knowledge under the form of text-based entity embedding s with L TNs is not
only simple, but it is also promising. L TNs can also be used to do after-training reasoning over combinations of axioms on which it was not
trained [83].
Figure 35 shows the number of studies per category, and Figur e 36 illustrates the relationship between categories
and goals. T able 5 shows the number of studies in each categor y per goal.
7. Discussion
All studies report performance either on par or above benchm arks, but we cannot compare studies based on
performance as nearly every study uses a different dataset a nd benchmark as discussed in Section 6.1.5. Our focus
is instead on whether the goals of NeSy are being met. Our Promise Score metric is not necessarily what the studies’
authors were optimizing for or even reporting, especially s tudies which have not labeled themselves as NeSy per se.
So we want to make it very clear that our analysis is not a judge ment of the success of any particular study, but rather
we seek to understand if the hypotheses about NeSy are materi alizing, namely that the combination of symbolic
and sub-symbolic techniques will fulﬁll the goals describe d in Section 4: Out-of-distribution (OOD) Generalization,
interpretability, tranferability, reduced data, and reas oning. And the short answer is we are not there yet, as can be
seen in Figure 37. For a detailed breakdown of each goal and st udy see T able 6.
In Section 4.5 we put forward the hypothesis that reasoning i s the means by which the other goals can be achieved.
This is not evidenced in the studies we reviewed. Some possib le explanations for this ﬁnding are: 1) The kind of

(a) NeSy category (b) Kautz category
Fig. 35. Number of studies per category
4. neuro: symbolic → neuro
5. neuro_symbolic
3. neuro; symbolic
2. symbolic[neuro]
1. symbolic neuro symbolic
Compiled
Cooperative
Nested
Sequential Reasoning
OOD
Interpretability
Reduced data
Transferability 
None
Fig. 36. NeSy categories to NeSy Goals. There is no obvious pa ttern with respect to what types of goals are met within each o f the NeSy
categories.
T able 5
Number of studies meeting each goal. The Promise Ratio represents the percentage of goals reported to have been met out of the total number of
possible goals (# of studies * 5 goals) in each category .
Compiled Cooperative Nested Sequential
Reasoning 12 5 3 14
OOD 9 3 1 2
Interpretability 8 4 2 6
Reduced data 6 4 2 3
Transferability 7 2 1 2
Promise Ratio 29.5% 40% 45% 21.6%
reasoning required to fulﬁll the other goals is not the kind b eing implemented; 2) The approaches are theoretically
promising, but the technical solutions need further develo pment. Next we look at each of these possibilities.
7.1. Reasoning Challenges
Thirty four out of the ﬁfty nine studies mention reasoning as a characteristic of their solution. But there is a lot
of variation in how reasoning is described and implemented. Given the overwhelming evidence of the fallibility of
human reasoning, to understand language, AI researchers ha ve sought guidance from disciplines such as psychology,
cognitive linguistics, neuroscience, and philosophy. The challenge is that there are multiple competing theories of
human reasoning and logic both across and within these disci plines. What we have discovered in our review , is
a blurring of the lines between various types of logic, human reasoning, and mathematical reasoning, as well as
counter-productive assumptions about which theory to adop t. For example, drawing inspiration from “how people

(a) All studies (b) NeSy studies only
Fig. 37. Proportion of studies which have met one or more of th e 5 goals
think”, accepting that how people think is ﬂawed, and subseq uently attempting to build a model with a logical
component, which by deﬁnition, is rooted in validity, seems counter productive to us. Although this does depend
somewhat on the business application. For problems like MWP (Math W ord Problems ) [77, 123, 135], where
answers are precise and unambiguous, less assumptions are n eeded. Additionally, the justiﬁcation of “because that’s
how people think” is inconsistent. Some examples from the st udies we reviewed include:
– [83] describe human reasoning in terms of a dual process of “s ubsymbolic commonsense” (strongly correlated
with associative learning), and “axiomatic” knowledge (pr edicates and logic formulas) for structured inference.
– In [108] humans reason by way of analogy, and commonsense kno wledge is represented in ConceptNet, a
graphical representation of common concepts and their rela tionships.
– For [116] human reasoning can be modeled by Image Schemas (IS ). Schemas are made up of logical rules on
(Entity1,Relation,Entity2) tuples, such as transitivity , or inversion.
– [113] explain their choice of fuzzy logic for “its resemblan ce to human reasoning and natural language.” This
is a probabilistic approach which attempts to deal with unce rtainty.
– [119] propose that human thought constructs can be modelled as cause-effect pairs. Commonsense is often
described as the ability to draw causal conclusions from bas ic knowledge, for example: If I drop the glass, it
will break .
– And [123] state that “when people perform explicit reasonin g, they can typically describe the way to the
conclusion step by step via relational descriptions.”
But the most plausible hypothesis in our view is that of Schon et al. [128]: in order to emulate human reasoning,
systems need to be ﬂexible, be able to deal with contradictin g evidence, evolving evidence, have access to enormous
amounts of background knowledge, and include a combination of different techniques and logics. Most notably,
no particular theory of reasoning is given. The argument put forward by Leslie Kaelbling at IBM Neuro-Symbolic
AI W orkshop 2022 32 is similarly appealing. Kaelbling points to the over-relia nce on the System1/System2 analogy,
and advocates for a much more diverse and dynamic approach. W e posit that the type of reasoning employed should
not be based solely on how we think people think, but on the att endant objective. This is in line with the “goal
oriented” theory from neuroscience, in that reasoning invo lves many sub-systems: perception, information retrieval ,
decision making, planning, controlling, and executing, ut ilizing working memory, calculation, and pragmatics. But
here the irony is not lost on us, and we acknowledge that by res orting to neuroscience for inspiration, we have
just committed the same mischief for which we have been decry ing our peers! But if we must resort to analogies
with human reasoning then it is imperative to be as rigorous a s possible. In their recent book, A F ormal Theory of
Commonsense Psychology, How P eople Think P eople Think [158], Gordon and Hobbs present a “large-scale logical
formalization of commonsense psychology in support of huma nlike artiﬁcial intelligence” to act as a baseline for
researchers building intelligent AI systems. Santos et al. [159] take this a step in the direction we are advocating,
32 https://researcher .watson.ibm.com/researcher/view_group.php?id=10897

T able 6
NeSy Promises reported as having been met ( y = yes, n = no)
Ref. Score Reasoning OOD
Generalization Interpretability Reduced
Data Transferability isNeSy
[155] 5 y y y y y y
[137, 143] 4 y y y y n y
[144] 4 y y y n y y
[77] 4 y n y y y n
[88, 152] 4 n y y y y y
[83, 136] 3 y y y n n y
[116] 3 y n y y n n
[123] 3 y n y n y n
[82] 3 n y n y y n
[133] 2 y y n n n y
[129, 132] 2 y n y n n y
[79, 85, 114, 128] 2 y n y n n n
[130, 141] 2 y n n y n n
[134, 135] 2 y n n n y y
[118] 2 y n n n y n
[131] 2 n y n y n y
[149, 151] 2 n y n y n n
[111] 2 n y n n y n
[110] 2 n n y n y n
[80, 147] 1 y n n n n y
[76, 78, 108, 122]
[112, 113, 119, 140]
[81, 107, 127]
1 y n n n n n
[154] 1 n y n n n y
[146] 1 n n y n n y
[153] 1 n n y n n n
[115, 148] 1 n n n y n y
[125, 139, 145, 150] 0 n n n n n y
[121, 124, 126, 138]
[109, 117, 120, 142]
0 n n n n n n
by testing whether there is human annotator agreement when c ategorizing texts into Gordon and Hobbs’ theories.
“Our end-goal is to advocate for better design of commonsens e benchmarks [and to] support the development of a
formal logic for commonsense reasoning” [159]. It is difﬁcu lt to imagine a single formal logic which would afford
all of Gordon and Hobbs’ 48 categories of reasoning tasks. Be sold et al. [7] dedicate several pages to this topic
under the heading of Neural-Symbolic Integration in and for Cognitive Science: Building Mental Models. In short,
computational modelling of cognitive tasks and especially language processing is still considered a hard challenge.
7.2. T echnical challenges
There is strong agreement that a successful NeSy system will be characterized by compositionality [1, 7, 8, 18,
160–163]. Compositionality allows for the construction of new meaning from learned building blocks thus enabling
extrapolation beyond the training data distribution. T o pa raphrase Garcez et al., one should be able to query the
trained network using a rich description language at an adeq uate level of abstraction [1]. The challenge is to come up
with dense/compact differentialble representations whil e preserving the ability to decompose, or unbind, the learne d
representations for downstream reasoning tasks.

One such system, proposed by Bianchi et al. [83] is the LT N EE - Figure 34 - an extention of Logic T ensor
Networks (L TNs), in which pre-trained embeddings are fed in to the L TN. They show promising results on small
datasets which have the important characteristic of being c apable of after-training logical inferences. However,
LT N EE is limited by heavy computational requirements as the logic becomes more expressive, for example by the
use of quantiﬁers.
Other studies [116, 137] introduce logical inference withi n their solutions, but all require manually designed rules,
and are limited by the domain expertise of the designer. Lear ning rules from data, or structure learning [164] is an
ongoing research topic as pointed out by [17]. In [118] Chatu rvedi et al. use fuzzy logic for emotion classiﬁcation
where explicit membership functions are learned. However, as stated by the authors, the classiﬁer becomes very
slow with the number of functions.
Other ( compiled) approaches involve translating logic into differentialb le functions, which are either directly
included as network nodes as in [85], or added as a constraint to the loss function, as in [165]. T o achieve this, First
Order Logic (FOL) can be operationalized using t-norms for e xample. T o address the many types of reasoning as
discussed in the previous section, we need to be able to incor porate other types of logic, such as temporal, modal,
epistemic, non-monotonic, probabilistic, and more, which , presumably, are better able to model human reasoning.
In summary, formulating logic, or more broadly reasoning, i n a differentiable fashion remains challenging.
8. Limitations & Future W ork
W e organized our analysis according to the characteristics extracted from the studies to test whether there were
any patterns leading to NeSy goals. Another approach would b e to reverse this perspective, and look at each goal
separately to understand the characteristics leading to it s fulﬁllment. However, each goal is really an entire ﬁeld of
study in and of itself, and we do not think we could have done ju stice to any of them by taking this approach. W e
spent a lot of time looking for signal in a very noisy environm ent where the studies we reviewed had very little in
common. More can be said about what we did not ﬁnd, than what we did. Another approach might be to narrow
the criteria for the type of NLP task, while expanding the tec hnical domain. In particular, a subset of tasks from the
NLU domain could be a good starting point, as these tasks are o ften said to require reasoning.
W e tried to be comprehensive in respect to the selected studi es which led to the trade-off of less space dedicated
to technical details or additional context from the neuro-s ymbolic discussion. There are a lot of ideas and concepts
which we did not cover, such as, and in no particular order, Re lational Statistical Learning (RSL), Inductive
Logic Programming (ILP), DeepProbLog [166], Connectionis t Modal Logics (CML), Extreme Learning Machines
(ELM), Genetic Programming, grounding and proposinalizat ion, Case Based Reasoning (CBR), Abstract Meaning
Representation (AMR), to name but a few , some of which are cov ered in detail in other surveys [7, 8].
Furthermore, we argued that we need differentiable forms of different types of logic, but we did not discuss how
they might be implemented. A comprehensive point of referen ce such as this would be a very valuable contribution
to the NeSy community, especially if the implementations we re anchored in cognitive science and linguistics as
discussed in 7.1.
Finally, the need for common datasets and benchmarks cannot be overstated.
9. Conclusion
W e analyzed recent studies implementing NeSy for NLP in orde r to test whether the promises of NeSy are
materializing in NLP . W e attempted to ﬁnd a pattern in a small and widely variable set of studies, and ultimately we
do not believe there are enough results to draw deﬁnitive con clusions. Only 59 studies met the criteria for our review ,
and many of them (in the Sequential category) we would not consider truly integrated NeSy syste ms. The one thing
studies which meet the most goals [77, 88, 137, 143, 144, 152, 155] have in common is that they all belong to the
tightly integrated set of NeSy categories, Cooperative and Compiled which is good news for NeSy. T wo out of these
seven report lower computational cost than baselines, and p erformance on par or slightly above baselines, though
we must reiterate that performance comparisons are not poss ible as discussed in Section 6.1.5. On the down side,

we have seen that some studies suffer from high computationa l cost, and that explicit reasoning still often requires
hand crafted domain speciﬁc rules and logic which makes them difﬁcult to scale or generalize to other applications.
Indeed, of the ﬁve goals, transferability to new domains was the least frequently satisﬁed.
Our view is that the lack of consensus around theories of reas oning and appropriate benchmarks is hindering
our ability to evaluate progress. Hence we advocate for the d evelopment of robust reasoning theories and formal
logics as well as the development of challenging benchmarks which not only measure the performance of speciﬁc
implementations, but have the potential to address real wor ld problems. Systems capable of capturing the nuances
of natural language (ie., ones that “understand” human reas oning) while returning sound conclusions (ie., perform
logical reasoning) could help combat some of the most conseq uential issues of our times such as mis- and dis-
information, corporate propaganda such as climate change d enialism, divisive political speech, and other harmful
rhetoric in the social discourse.
Acknowledgements
This publication has emanated from research supported in pa rt by a grant from Science Foundation Ireland under
Grant number 18/CR T/6183. For the purpose of Open Access, th e author has applied a CC BY public copyright
licence to any Author Accepted Manuscript version arising f rom this submission.
References
[1] A.d. Garcez and L.C. Lamb, Neurosymbolic AI: The 3rd W ave , arXiv , 2020. doi:10.48550/ARXIV .2012.05876.
[2] L.G. V aliant, Three Problems in Computer Science, Journal of the ACM 50(1) (2003), 96–99. doi:10.1145/602382.602410.
[3] A. V aswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones , A.N. Gomez, Ł. Kaiser and I. Polosukhin, Attention is all yo u need, in:
Advances in neural information processing systems , V ol. 30, 2017, pp. 5998–6008.
[4] J. Devlin, M.-W . Chang, K. Lee and K. T outanova, BER T: Pre -training of Deep Bidirectional Transformers for Language Understanding,
in: Proceedings of the 2019 Conference of the North American Cha pter of the Association for Computational Linguistics: Hum an
Language T echnologies, V olume 1 (Long and Short P apers) , Association for Computational Linguistics, Minneapolis , Minnesota, 2019,
pp. 4171–4186. doi:10.18653/v1/N19-1423.
[5] J. Pearl, Theoretical Impediments to Machine Learning W ith Seven Sparks from the Causal Revolution, arXiv , 2018.
doi:10.48550/ARXIV .1801.04016.
[6] G. Marcus, Deep Learning: A Critical Appraisal, arXiv , 2 018. doi:10.48550/ARXIV .1801.00631.
[7] T .R. Besold, A.d. Garcez, S. Bader, H. Bowman, P . Domingo s, P . Hitzler, K.-U. Kuehnberger, L.C. Lamb, D. Lowd, P .M.V . Lima,
L. de Penning, G. Pinkas, H. Poon and G. Zaverucha, Neural-Sy mbolic Learning and Reasoning: A Survey and Interpretation , arXiv ,
2017. doi:10.48550/ARXIV .1711.03902.
[8] A.d. Garcez, M. Gori, L.C. Lamb, L. Seraﬁni, M. Spranger a nd S.N. Tran, Neural-Symbolic Computing: An Effective
Methodology for Principled Integration of Machine Learnin g and Reasoning, arXiv , 2019. doi:10.48550/ARXIV .1905.06 088.
https://arxiv .org/abs/1905.06088 .
[9] Y . Bengio, G. Marcus and V . Boucher, AI DEBA TE! Y oshua Ben gio vs Gary Marcus, Montreal.AI.
https://montrealartiﬁcialintelligence.com/aidebate/ .
[10] H. Kautz, The Third AI Summer, AAAI Robert S. Engelmore M emorial Lecture, Thirty-fourth AAAI Conference on Artiﬁci al
Intelligence, New Y ork, NY . https://henrykautz.com/talk s/index.html .
[11] M.K. Sarker, L. Zhou, A. Eberhart and P . Hitzler, Neuro- Symbolic Artiﬁcial Intelligence: Current Trends, arXiv , 2 021.
doi:10.48550/ARXIV .2105.05330.
[12] Y . Bengio, System 2 Deep Learning: Higher-Level Cognit ion, Agency , Out-of-Distribution Generalization and Caus ality , 30th
International Joint Conference on Artiﬁcial Intelligence . https://ijcai-21.org/invited- talks/ .
[13] D. Kahneman, Thinking, fast and slow , Farrar, Straus and Giroux, New Y ork, 2011. ISBN 9780374275 631 0374275637.
[14] Z. Liu, Z. W ang, Y . Lin and H. Li, A Neural-Symbolic Appro ach to Natural Language Understanding (2022), arXiv:2203. 10557 [cs].
[15] J. Zhang, B. Chen, L. Zhang, X. Ke and H. Ding, Neural, sym bolic and neural-symbolic reasoning on knowledge graphs, AI Open 2
(2021), 14–35. doi:10.1016/j.aiopen.2021.03.001.
[16] L.C. Lamb, A.d. Garcez, M. Gori, M.O.R. Prates, P .H.C. A velar and M.Y . V ardi, Graph Neural Networks Meet Neural-
Symbolic Computing: A Survey and Perspective, in: Proceedings of the T wenty-Ninth International Joint Confe rence on Artiﬁcial
Intelligence, International Joint Conferences on Artiﬁcial Intelligen ce Organization, 2020, pp. 4877–4884. ISBN 978-0-9992411- 6-5.
doi:10.24963/ijcai.2020/679.

[17] L. von Rueden, S. Mayer, K. Beckh, B. Georgiev, S. Giesse lbach, R. Heese, B. Kirsch, M. W alczak, J. Pfrommer, A. Pick, R. Ramamurthy,
J. Garcke, C. Bauckhage and J. Schuecker, Informed Machine L earning - A T axonomy and Survey of Integrating Prior Knowled ge into
Learning Systems, IEEE Transactions on Knowledge and Data Engineering (2021), 1–1. doi:10.1109/TKDE.2021.3079836.
[18] V . Belle, Symbolic Logic Meets Machine Learning: A Brie f Survey in Inﬁnite Domains, in: Scalable Uncertainty Management , Springer
International Publishing, 2020, pp. 3–16. ISBN 978-3-030- 58449-8.
[19] O. Sharir, B. Peleg and Y . Shoham, The Cost of Training NL P Models: A Concise Overview, ArXiv (2020).
doi:10.48550/arXiv .2004.08900.
[20] G. Marcus and E. Davis, GPT -3, Bloviator: OpenAI’ s lang uage generator has no idea what it’ s talking about | MIT T echn ology Review .
https://www .technologyreview .com/2020/08/22/1007539/gpt3- openai-language-generator-artiﬁcial-intellige nce- ai- opinion/ .
[21] T .B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P . D hariwal, A. Neelakantan, P . Shyam, G. Sastry, A. Askell, S. A garwal,
A. Herbert-V oss, G. Krueger, T . Henighan, R. Child, A. Rames h, D.M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler , M. Litwin,
S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radf ord, I. Sutskever and D. Amodei, Language Models are Few-Sho t Learners
(2020). doi:10.48550/ARXIV .2005.14165.
[22] W . Farnsworth, The socratic method: A practitioner’s handbook , David R. Godine Publisher Inc, 2021.
[23] P . Engel, Reasoning and Rationality , in: Dictionary of cognitive science neuroscience, psychology , Artiﬁcial Intelligence, linguistics, and
philosophy, T aylor and Francis, 2003, pp. 315–316. doi:https://doi.o rg/10.4324/9780203486030.
[24] D. Kahneman, O. Sibony and C.R. Sunstein, Noise: A Flaw in Human Judgment , HarperCollins Publishers Limited, 2021. ISBN 978-0-
00-830900-8.
[25] P . Hitzler, F . Bianchi, M. Ebrahimi and M.K. Sarker, Neu ral-symbolic integration and the Semantic W eb, Semantic W eb 11(1) (2020),
3–11. doi:10.3233/SW-190368.
[26] B. MacCartney, Understanding Natural Language Unders tanding, ACM SIGAI Bay Area Chapter Inaugural Meeting, San M ateo, CA.
https://www .youtube.com/watch?v=vcPd0V4VSNU .
[27] J. W eizenbaum, ELIZA—a computer program for the study o f natural language communication between man and machine,
Communications of the ACM 9(1) (1966), 36–45.
[28] D.A. Ferrucci, Introduction to “This is W atson”, IBM Journal of Research and Development 56(3.4) (2012), 1:1–1:15.
doi:10.1147/JRD.2012.2184356.
[29] S. Hochreiter and J. Schmidhuber, Long Short-T erm Memo ry , Neural Computation 9(8) (1997), 1735–1780.
doi:10.1162/neco.1997.9.8.1735.
[30] B. MacCartney and C.D. Manning, An extended model of nat ural logic, in: Proceedings of the Eight International Conference on
Computational Semantics , Association for Computational Linguistics, Tilburg, The Netherlands, 2009, pp. 140–156.
[31] A. Gatt and E. Krahmer, Survey of the State of the Art in Na tural Language Generation: Core tasks, applications and ev aluation, Journal
of Artiﬁcial Intelligence Research 61 (2018), 65–170. doi:10.1613/jair .5477.
[32] D. Y u, B. Y ang, D. Liu and H. W ang, A Survey on Neural-symb olic Systems, arXiv , 2021. doi:10.48550/ARXIV .2111.0816 4.
[33] S. Bader and P . Hitzler, Dimensions of Neural-symbolic Integration – A Structured S urvey , in: W e W ill Show Them! Essays in Honour of
Dov Gabbay , V olume One, S.N , College Publications, 2005.
[34] G.G. T owell and J.W . Shavlik, Knowledge-based artiﬁci al neural networks, Artiﬁcial intelligence 70(1–2) (1994), 119–165.
[35] A.S.d. Garcez, K. Broda, D.M. Gabbay et al., Neural-symbolic learning systems: foundations and applic ations, Springer Science &
Business Media, 2002.
[36] L. Seraﬁni and A.S. d’A vila Garcez, Learning and Reason ing with Logic T ensor Networks, in: AI*IA 2016 Advances in Artiﬁcial
Intelligence, G. Adorni, S. Cagnoni, M. Gori and M. Maratea, eds, Lecture N otes in Computer Science, Springer International Publishi ng,
2016, pp. 334–348. ISBN 978-3-319-49130-1. doi:10.1007/9 78-3-319-49130-1_25.
[37] R. Socher, D. Chen, C.D. Manning and A. Ng, Reasoning Wit h Neural T ensor Networks for Knowledge Base Completion, in: Advances
in Neural Information Processing Systems , V ol. 26, Curran Associates, Inc., 2013.
[38] S. Muggleton, Inductive logic programming, New Generation Computing 8(4) (1991), 295–318. doi:10.1007/BF03037089.
[39] F . Y ang, Z. Y ang and W .W . Cohen, Differentiable learnin g of logical rules for knowledge base reasoning, Advances in neural information
processing systems 30 (2017).
[40] R. Evans and E. Grefenstette, Learning explanatory rul es from noisy data, Journal of Artiﬁcial Intelligence Research 61 (2018), 1–64.
[41] T . Rocktäschel and S. Riedel, Learning knowledge base i nference with neural theorem provers, in: Proceedings of the 5th workshop on
automated knowledge base construction , 2016, pp. 45–50.
[42] H. Dong, J. Mao, T . Lin, C. W ang, L. Li and D. Zhou, Neural L ogic Machines, arXiv , 2019. doi:10.48550/ARXIV .1904.116 94.
[43] C. W endelken and L. Shastri, Multiple instantiation an d rule mediation in SHRUTI, Connection Science 16(3) (2004), 211–217.
[44] G. V ilone and L. Longo, Notions of explainability and ev aluation approaches for explainable artiﬁcial intelligen ce, Information Fusion 76
(2021), 89–106.
[45] D. Koller, N. Friedman, S. Džeroski, C. Sutton, A. McCal lum, A. Pfeffer, P . Abbeel, M.-F . W ong, C. Meek, J. Neville et al., Introduction
to statistical relational learning , MIT press, 2007.
[46] L. De Raedt, A. Kimmig and H. T oivonen, ProbLog: A Probab ilistic Prolog and Its Application in Link Discovery ., in: IJCAI, V ol. 7,
Hyderabad, 2007, pp. 2462–2467.
[47] M. Richardson and P . Domingos, Markov logic networks, Machine Learning 62(1) (2006), 107–136. doi:10.1007/s10994-006-5833-1.
[48] Y . W ang, Q. Y ao, J.T . Kwok and L.M. Ni, Generalizing from a few examples: A survey on few-shot learning, ACM computing surveys
(csur) 53(3) (2020), 1–34.

[49] A.S.d. Garcez and D.M. Gabbay, Fibring neural networks , in: Proceedings of 19th National Conference on Artiﬁcial Intel ligence - AAAI-
2004, AAAI Press, 2004, pp. 342–347.
[50] M.F . Joanisse and J.L. McClelland, Connectionist pers pectives on language learning, representation and process ing, W iley
Interdisciplinary Reviews: Cognitive Science 6(3) (2015), 235–247.
[51] S. Pinker, W ords and rules, Lingua 106(1–4) (1998), 219–242.
[52] R.D. Sriram, Analogical and Case-Based Reasoning , in: Intelligent Systems for Engineering: A Knowledge-based Ap proach, Springer
London, London, 1997, pp. 285–334. ISBN 978-1-4471-0631-9 . doi:10.1007/978-1-4471-0631-9_6.
[53] W .L. Hamilton, R. Y ing and J. Leskovec, Representation Learning on Graphs: Methods and Applications (2017).
doi:10.48550/ARXIV .1709.05584.
[54] O. V inyals, M. Fortunato and N. Jaitly, Pointer network s, Advances in neural information processing systems 28 (2015).
[55] T .N. Kipf and M. W elling, Semi-supervised classiﬁcati on with graph convolutional networks. 2017, ArXiv abs/1609.02907 (2017).
[56] F . Scarselli, M. Gori, A.C. Tsoi, M. Hagenbuchner and G. Monfardini, The graph neural network model, IEEE transactions on neural
networks 20(1) (2008), 61–80.
[57] P . V elickovic, G. Cucurull, A. Casanova, A. Romero, P . L iò and Y . Bengio, Graph Attention Networks, CoRR abs/1710.10903 (2017).
[58] L. Y ao, C. Mao and Y . Luo, Graph convolutional networks f or text classiﬁcation, in: Proceedings of the AAAI conference on artiﬁcial
intelligence, V ol. 33, 2019, pp. 7370–7377.
[59] M. Schlichtkrull, T .N. Kipf, P . Bloem, R.v .d. Berg, I. T itov and M. W elling, Modeling relational data with graph con volutional networks,
in: European semantic web conference , Springer, 2018, pp. 593–607.
[60] F . V an Harmelen and A.t. T eije, A boxology of design patt erns for hybrid learning and reasoning systems, arXiv preprint arXiv:1905.12389
(2019).
[61] B. Hammer and P . Hitzler (eds), P erspectives of Neural-Symbolic Integration , V ol. 77, Springer, 2007. ISBN 978-3-540-73953-1.
[62] A.S. Garcez, L.C. Lamb and D.M. Gabbay, Neural-Symbolic Cognitive Reasoning, Cognitive T echnolo gies, Springer, 2009. ISBN 978-3-
540-73245-7. doi:10.1007/978-3-540-73246-4..
[63] E. Gabrilovich, R. Guha, A. McCallum and K. Murphy, Know ledge Representation and Reasoning: Integrating Symbolic and Neural
Approaches, The AAAI Press, Palo Alto, California., 2015. I SBN 978-1-57735-707-0.
[64] T .R. Besold and K.-U. Kühnberger, T owards integrated n eural–symbolic systems for human-level AI: T wo research pr ograms helping to
bridge the gaps, Biologically Inspired Cognitive Architectures 14 (2015), 97–110. doi:10.1016/j.bica.2015.09.003.
[65] Z. Shen, J. Liu, Y . He, X. Zhang, R. Xu, H. Y u and P . Cui, T ow ards Out-Of-Distribution Generalization: A Survey (2021) .
doi:10.48550/ARXIV .2108.13624.
[66] C. Rudin, C. Chen, Z. Chen, H. Huang, L. Semenova and C. Zh ong, Interpretable machine learning: Fundamental princip les and 10 grand
challenges, Statistics Surveys 16 (2022), 1–85.
[67] H. Jiang, P . He, W . Chen, X. Liu, J. Gao and T . Zhao, SMAR T: Robust and Efﬁcient Fine-Tuning for Pre-trained Natural La nguage
Models through Principled Regularized Optimization, in: Proceedings of the 58th Annual Meeting of the Association fo r Computational
Linguistics, Association for Computational Linguistics, Online, 2020 , pp. 2177–2190. doi:10.18653/v1/2020.acl-main.197.
[68] F . Zhuang, Z. Qi, K. Duan, D. Xi, Y . Zhu, H. Zhu, H. Xiong an d Q. He, A Comprehensive Survey on Transfer Learning, Proceedings of
the IEEE 109(1) (2021), 43–76. doi:10.1109/JPROC.2020.3004555.
[69] Reasoning, Encyclopædia Britannica, inc. https://ww w .britannica.com/technology/artiﬁcial- intelligence/ Reasoning .
[70] B. Kitchenham, Procedures for performing systematic r eviews, Keele, UK, Keele University 33(2004) (2004), 1–26.
[71] G. Paré, M.-C. Trudel, M. Jaana and S. Kitsiou, Synthesi zing information systems knowledge: A typology of literatu re reviews,
Information & Management 52(2) (2015), 183–199. doi:https://doi.org/10.1016/j.im. 2014.08.008.
[72] M.J. Page, J.E. McKenzie, P .M. Bossuyt, I. Boutron, T .C . Hoffmann, C.D. Mulrow, L. Shamseer, J.M. T etzlaff, E.A. Ak l, S.E. Brennan,
R. Chou, J. Glanville, J.M. Grimshaw, A. Hróbjartsson, M.M. Lalu, T . Li, E.W . Loder, E. Mayo-Wilson, S. McDonald, L.A. Mc Guinness,
L.A. Stewart, J. Thomas, A.C. Tricco, V .A. W elch, P . Whiting and D. Moher, The PRISMA 2020 statement: an updated guidelin e for
reporting systematic reviews, Systematic Reviews 10(1) (2021), 89. doi:10.1186/s13643-021-01626-4.
[73] M. Kang and N.J. Jameson, Machine Learning: Fundamenta ls, Prognostics and Health Management of Electronics: Fundame ntals,
Machine Learning, and the Internet of Things (2018), 85–109.
[74] G. Bonaccorso, Machine learning algorithms , Packt Publishing Ltd, 2017.
[75] Y . Bengio, J. Louradour, R. Collobert and J. W eston, Cur riculum learning, in: Proceedings of the 26th annual international conference on
machine learning , 2009, pp. 41–48.
[76] E. Saveleva, V . Petukhova, M. Mosbach and D. Klakow, Gra ph-based Argument Quality Assessment, in: Proceedings of the International
Conference on Recent Advances in Natural Language Processi ng (RANLP 2021) , INCOMA Ltd., Held Online, 2021, pp. 1268–1280.
[77] Q. Zhang, L. W ang, S. Y u, S. W ang, Y . W ang, J. Jiang and E.- P . Lim, NOAHQA: Numerical Reasoning with Interpretable Gra ph
Question Answering Dataset, in: Findings of the Association for Computational Linguistics : EMNLP 2021 , Association for Computational
Linguistics, Punta Cana, Dominican Republic, 2021, pp. 414 7–4161. doi:10.18653/v1/2021.ﬁndings-emnlp.350.
[78] K. Chen, W . Xu, X. Cheng, Z. Xiaochuan, Y . Zhang, L. Song, T . W ang, Y . Qi and W . Chu, Question Directed Graph Attention N etwork
for Numerical Reasoning over T ext, in: Proceedings of the 2020 Conference on Empirical Methods in N atural Language Processing
(EMNLP), Association for Computational Linguistics, Online, 2020 , pp. 6759–6768. doi:10.18653/v1/2020.emnlp-main.549.
[79] Y . Gu, J.Z. Pan, G. Cheng, H. Paulheim and G. Stoilos, Loc al ABox consistency prediction with transparent TBoxes usi ng gated graph
neural networks, in: Proc. 14th International W orkshop on Neural-Symbolic Lear ning and Reasoning (NeSy) , 2019.

[80] H. Lemos, P . A velar, M. Prates, A. Garcez and L. Lamb, Neu ral-Symbolic Relational Reasoning on Graph Models: Effect ive Link
Inference and Computation from Knowledge Bases, Lecture Notes in Computer Science 12396 LNCS (2020), 647–659. doi:10.1007/978-
3-030-61609-0_51.
[81] M. Zhou, D. Ji and F . Li, Relation Extraction in Dialogue s: A Deep Learning Model Based on the Generality and Specialt y of Dialogue
T ext, IEEE/ACM Transactions on Audio Speech and Language Process ing 29 (2021), 2015–2026. doi:10.1109/T ASLP .2021.3082295.
[82] S. Huo, T . Ma, J. Chen, M. Chang, L. Wu and M. Witbrock, Gra ph Enhanced Cross-Domain T ext-to-SQL Generation, in: Proceedings of
the Thirteenth W orkshop on Graph-Based Methods for Natural Language Processing, T extGraphs@EMNLP 2019, Hong Kong, No vember
4, 2019 , Association for Computational Linguistics, 2019, pp. 159 –163. doi:10.18653/v1/D19-5319.
[83] F . Bianchi, M. Palmonari, P . Hitzler and L. Seraﬁni, Com plementing logical reasoning with sub-symbolic commonsen se, Lecture Notes
in Computer Science 11784 LNCS (2019), 161–170. doi:10.1007/978-3-030-31095-0_11.
[84] L. Seraﬁni and A.d. Garcez, Logic T ensor Networks: Deep Learning and Logical Reasoning from Data and Knowledge, arXiv:1606.04422
[cs] (2016).
[85] J. Jiang, H. W ang, J. Xie, X. Guo, Y . Guan and Q. Y u, Medica l knowledge embedding based on recursive neural network for multi-disease
diagnosis, Artiﬁcial Intelligence in Medicine 103 (2020). doi:10.1016/j.artmed.2019.101772.
[86] R. Jia and P . Liang, Adversarial Examples for Evaluatin g Reading Comprehension Systems, in: Proceedings of the 2017 Conference on
Empirical Methods in Natural Language Processing , Association for Computational Linguistics, Copenhagen, Denmark, 2017, pp. 2021–
2031. doi:10.18653/v1/D17-1215.
[87] S. Gururangan, S. Swayamdipta, O. Levy, R. Schwartz, S. Bowman and N.A. Smith, Annotation Artifacts in Natural Lang uage Inference
Data, in: Proceedings of the 2018 Conference of the North American Cha pter of the Association for Computational Linguistics: Hum an
Language T echnologies, V olume 2 (Short P apers) , Association for Computational Linguistics, New Orleans, Louisiana, 2018, pp. 107–112.
doi:10.18653/v1/N18-2017.
[88] B. Škrlj, M. Martinc, N. Lavra ˇc and S. Pollak, autoBOT: evolving neuro-symbolic represen tations for explainable low resource text
classiﬁcation, Machine Learning 110(5) (2021), 989–1028. doi:10.1007/s10994-021-05968-x.
[89] R. Miikkulainen, Neuroevolution, in: Encyclopedia of Machine Learning , Springer, New Y ork, 2010.
[90] J. Lehman and R. Miikkulainen, Neuroevolution, Scholarpedia 8(6) (2013), 30977. doi:10.4249/scholarpedia.30977.
[91] R. Davis, H. Shrobe and P . Szolovits, What is a knowledge representation?, AI magazine 14(1) (1993), 17–17.
[92] T .J. Bench-Capon, Knowledge representation: An approach to artiﬁcial intell igence, V ol. 32, Elsevier, 2014.
[93] H.J. Levesque, Knowledge representation and reasonin g, Annual review of computer science 1(1) (1986), 255–287.
[94] R. Brachman and H. Levesque, Knowledge representation and reasoning , Elsevier, 2004.
[95] I.L. Travis, Knowledge Representation in Artiﬁcial In telligence, Clinic on Library Applications of Data Processing (27th: 19 90) (1990).
[96] J.F . Sowa, Principles of Semantic Networks , Morgan Kaufmann, 1991. ISBN 978-1-4832-0771-1. doi:10.1 016/C2013-0-08297-7.
[97] C.R. Dyer, CS 540 Lecture Notes: Logic, University of Wi sconsin - Madison. https://pages.cs.wisc.edu/~dyer/cs5 40/notes/logic.html .
[98] J. Byszuk, M. W o´ zniak, M. Kestemont, A. Le ´sniak, W . Lukasik, A. Šel , a and M. Eder, Detecting Direct Speech in Multilingual Colle ction
of 19th-century Novels, in: Proceedings of LT4HALA 2020 - 1st W orkshop on Language T echn ologies for Historical and Ancient
Languages, European Language Resources Association (ELRA), Marseil le, France, 2020, pp. 100–104. ISBN 979-10-95546-53-5.
[99] G. Lakoff, Linguistics and natural logic, Synthese 22(1) (1970), 151–271. doi:10.1007/BF00413602.
[100] B. MacCartney and C.D. Manning, Natural logic for text ual inference, in: Proceedings of the ACL-P ASCAL W orkshop on T extual
Entailment and P araphrasing , 2007, pp. 193–200.
[101] G. Angeli and C.D. Manning, NaturalLI: Natural Logic I nference for Common Sense Reasoning, in: Proceedings of the 2014 Conference
on Empirical Methods in Natural Language Processing (EMNLP ), Association for Computational Linguistics, Doha, Qatar, 2014,
pp. 534–545. doi:10.3115/v1/D14-1059.
[102] C. Manning, M. Surdeanu, J. Bauer, J. Finkel, S. Bethar d and D. McClosky , The Stanford CoreNLP Natural Language Pro cessing T oolkit,
in: Proceedings of 52nd Annual Meeting of the Association for Co mputational Linguistics: System Demonstrations , Association for
Computational Linguistics, Baltimore, Maryland, 2014, pp . 55–60. doi:10.3115/v1/P14-5010. https://aclanthology .org/P14-5010 .
[103] S. McCall, Review of Selected W orks, Synthese 26(1) (1973), 165–171.
[104] F . Harder and T .R. Besold, Learning Łukasiewicz logic , Cognitive Systems Research 47 (2018), 42–67. doi:10.1016/j.cogsys.2017.07.004.
[105] C. Strasser and G.A. Antonelli, Non-monotonic Logic, in: The Stanford Encyclopedia of Philosophy , Summer 2019 edn, Metaphysics
Research Lab, Stanford University, 2019.
[106] J.P . McCrae, E. Rudnicka and F . Bond, English W ordNet: A new open-source wordnet for English, 2021.
https://lexicala.com/review/2020/mccrae- rudnicka-bond-english- wordnet/ .
[107] J. D’Souza, I.O. Mulang’ and S. Auer, T eam SVMrank: Lev eraging Feature-rich Support V ector Machines for Ranking E xplanations
to Elementary Science Questions, in: Proceedings of the Thirteenth W orkshop on Graph-Based Meth ods for Natural Language
Processing, T extGraphs@EMNLP 2019, Hong Kong, November 4, 2019, Association for Computational Linguistics, 2019, pp. 90– 100.
doi:10.18653/v1/D19-5312.
[108] A. Hussain and E. Cambria, Semi-supervised learning f or big social data analysis, Neurocomputing 275 (2018), 1662–1673.
doi:10.1016/j.neucom.2017.10.010.
[109] Q. Cui, Y . Zhou and M. Zheng, Sememes-Based Framework f or Knowledge Graph Embedding with Comprehensive-Informat ion, Lecture
Notes in Computer Science 12816 LNAI (2021), 419–426. doi:10.1007/978-3-030-82147-0_34.
[110] C. Xu and R. Li, Relation Embedding with Dihedral Group in Knowledge Graph, in: Proceedings of the 57th Annual Meeting
of the Association for Computational Linguistics , Association for Computational Linguistics, Florence, It aly, 2019, pp. 263–272.
doi:10.18653/v1/P19-1026.

[111] A.I. Cowen-Rivers, P . Minervini, T . Rocktaschel, M. B osnjak, S. Riedel and J. W ang, Neural V ariational Inference For Estimating
Uncertainty in Knowledge Graph Embeddings (2019).
[112] M. Bounabi, K. Elmoutaouakil and K. Satori, A new neutr osophic TF-IDF term weighting for text mining tasks: text cl assiﬁcation use
case, International Journal of W eb Information Systems 17(3) (2021), 229–249. doi:10.1108/IJWIS-11-2020-0067.
[113] F . Es-Sabery, A. Hair, J. Qadir, B. Sainz-De-Abajo, B. Garcia-Zapirain and I. T orre-DIez, Sentence-Level Classi ﬁcation Using Parallel
Fuzzy Deep Learning Classiﬁer, IEEE Access 9 (2021), 17943–17985. doi:10.1109/ACCESS.2021.3053917.
[114] R. Lima, B. Espinasse and F . Freitas, The Impact of Sema ntic Linguistic Features in Relation Extraction: A Logical Relational Learning
Approach, in: Proceedings of the International Conference on Recent Adva nces in Natural Language Processing (RANLP 2019) ,
INCOMA Ltd., V arna, Bulgaria, 2019, pp. 648–654. doi:10.26 615/978-954-452-056-4_076.
[115] Q. Chen, A. Lamoreaux, X. W ang, G. Durrett, O. Bastani a nd I. Dillig, W eb Question Answering with Neurosymbolic
Program Synthesis , in: Proceedings of the 42nd ACM SIGPLAN International Conferen ce on Programming Language Design
and Implementation , Association for Computing Machinery , New Y ork, NY , USA, 20 21, pp. 328–343–. ISBN 9781450383912.
https://doi.org/10.1145/3453483.3454047 .
[116] Y . Y ao, J. Xu, J. Shi and B. Xu, Learning to activate logi c rules for textual reasoning, Neural Networks 106 (2018), 42–49.
doi:10.1016/j.neunet.2018.06.012.
[117] A.A.N. T ato, R. Nkambou and A. Dufresne, Hybrid Deep Ne ural Networks to Predict Socio-Moral Reasoning Skills, in: Proceedings of
the 12th International Conference on Educational Data Mini ng, EDM 2019, Montréal, Canada, July 2-5, 2019 , International Educational
Data Mining Society (IEDMS), 2019. https://drive.google. com/ﬁle/d/1aCXyukLqV euShQSGA TRzEeDAk_Al7bVz .
[118] I. Chaturvedi, R. Satapathy, S. Cavallari and E. Cambr ia, Fuzzy commonsense reasoning for multimodal sentiment a nalysis, P attern
Recognition Letters 125 (2019), 264–270. doi:10.1016/j.patrec.2019.04.024.
[119] R. A yyanar, G. Koomullil and H. Ramasangu, Causal rela tion classiﬁcation using convolutional neural networks an d grammar tags, 2019.
doi:10.1109/INDICON47234.2019.9028985.
[120] J. Gong, H. Ma, Z. T eng, Q. T eng, H. Zhang, L. Du, S. Chen, M.Z.A. Bhuiyan, J. Li and M. Liu, Hierarchical Graph
Transformer-Based Deep Learning Model for Large-Scale Mul ti-Label T ext Classiﬁcation, IEEE Access 8 (2020), 30885–30896.
doi:10.1109/ACCESS.2020.2972751.
[121] A.M.P . Bra¸ soveanu and R. Andonie, Semantic Fake News Detection: A Machine Learning Perspective, Lecture Notes in Computer Science
11506 LNCS (2019), 656–667. doi:10.1007/978-3-030-20521-8_54.
[122] D. Hu, L. W ei and X. Huai, DialogueCRN: Contextual Reas oning Networks for Emotion Recognition in Conversations, i n: Proceedings
of the 59th Annual Meeting of the Association for Computatio nal Linguistics and the 11th International Joint Conferenc e on
Natural Language Processing (V olume 1: Long P apers) , Association for Computational Linguistics, Online, 2021 , pp. 7042–7052.
doi:10.18653/v1/2021.acl-long.547.
[123] K. Chen, Q. Huang, H. Palangi, P . Smolensky , K.D. Forbu s and J. Gao, Mapping Natural-Language Problems to F ormal-Language
Solutions Using Structured Neural Representations , in: Proceedings of the 37th International Conference on Machin e Learning ,
JMLR.org, 2020.
[124] L. Graziani, S. Melacci and M. Gori, Jointly Learning t o Detect Emotions and Predict Facebook Reactions, Lecture Notes in Computer
Science 11730 LNCS (2019), 185–197. doi:10.1007/978-3-030-30490-4_16.
[125] K. Gupta, T . Ghosal and A. Ekbal, A Neuro-Symbolic Appr oach for Question Answering on Research Articles, in: Proceedings of the
35th P aciﬁc Asia Conference on Language, Information and Co mputation, Association for Computational Lingustics, Shanghai, Chi na,
2021, pp. 40–49.
[126] J. Langton and K. Srihasam, Applied Medical Code Mappi ng with Character-based Deep Learning Models and W ord-base d Logic,
in: Proceedings of the 1st and 2nd W orkshops on Natural Logic Mee ts Machine Learning (NALOMA) , Association for Computational
Linguistics, Groningen, the Netherlands (online), 2021, p p. 7–11.
[127] L.B. Fazlic, A. Hallawa, A. Schmeink, A. Peine, L. Mart in and G. Dartmann, A Novel NLP-FUZZY System Prototype for In formation
Extraction from Medical Guidelines, in: 2019 42nd International Convention on Information and Comm unication T echnology , Electronics
and Microelectronics (MIPRO) , 2019, pp. 1025–1030. doi:10.23919/MIPRO.2019.8756929.
[128] C. Schon, S. Siebert and F . Stolzenburg, The CoRg Proje ct: Cognitive Reasoning, KI - Kunstliche Intelligenz 33(3) (2019), 293–299.
doi:10.1007/s13218-019-00601-5.
[129] M.L. Pacheco and D. Goldwasser, Modeling Content and C ontext with Deep Relational Learning, Transactions of the Association for
Computational Linguistics 9 (2021), 100–119. doi:10.1162/tacl_a_00357.
[130] K. Amin, Cases without Borders: Automating Knowledge Acquisition Approach using Deep Autoencoders and Siamese N etworks in
Case-Based Reasoning, in: 2019 IEEE 31st International Conference on T ools with Artiﬁ cial Intelligence (ICTAI) , 2019, pp. 133–140.
doi:10.1109/ICT AI.2019.00027.
[131] E. Altszyler, P . Brusco, N. Basiou, J. Byrnes and D. V er gyri, Zero-shot Multi-Domain Dialog State Tracking Using P rescriptive Rules,
in: Proceedings of the 15th International W orkshop on Neural-S ymbolic Learning and Reasoning as part of the 1st Internatio nal Joint
Conference on Learning & Reasoning (IJCLR 2021), V irtual co nference, October 25-27, 2021 , CEUR W orkshop Proceedings, V ol. 2986,
CEUR-WS.org, 2021, pp. 57–66.
[132] A. Sutherland, S. Magg and S. W ermter, Leveraging Recu rsive Processing for Neural-Symbolic Affect-T arget Assoc iations, in: 2019
International Joint Conference on Neural Networks (IJCNN) , 2019, pp. 1–6. doi:10.1109/IJCNN.2019.8851875.

[133] D. Demeter and D. Downey, Just Add Functions: A Neural- Symbolic Language Model, in: The Thirty-F ourth AAAI Conference on
Artiﬁcial Intelligence, AAAI 2020, The Thirty-Second Inno vative Applications of Artiﬁcial Intelligence Conference , IAAI 2020, The T enth
AAAI Symposium on Educational Advances in Artiﬁcial Intell igence, EAAI 2020, New Y ork, NY , USA, F ebruary 7-12, 2020 , AAAI Press,
2020, pp. 7634–7642.
[134] B. Zhou, K. Richardson, Q. Ning, T . Khot, A. Sabharwal a nd D. Roth, T emporal Reasoning on Implicit Events from Dista nt
Supervision, in: Proceedings of the 2021 Conference of the North American Cha pter of the Association for Computational Linguistics:
Human Language T echnologies , Association for Computational Linguistics, Online, 2021 , pp. 1361–1371. doi:10.18653/v1/2021.naacl-
main.107.
[135] J. Qin, X. Liang, Y . Hong, J. T ang and L. Lin, Neural-Sym bolic Solver for Math W ord Problems with Auxiliary T asks, in : Proceedings
of the 59th Annual Meeting of the Association for Computatio nal Linguistics and the 11th International Joint Conferenc e on
Natural Language Processing (V olume 1: Long P apers) , Association for Computational Linguistics, Online, 2021 , pp. 5870–5881.
doi:10.18653/v1/2021.acl-long.456.
[136] P . Sen, M. Danilevsky, Y . Li, S. Brahma, M. Boehm, L. Chi ticariu and R. Krishnamurthy , Learning Explainable Lingui stic Expressions
with Neural Inductive Logic Programming for Sentence Class iﬁcation, in: Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP) , Association for Computational Linguistics, Online, 2020 , pp. 4211–4221.
doi:10.18653/v1/2020.emnlp-main.345.
[137] J. Mao, C. Gan, P . Kohli, J.B. T enenbaum and J. Wu, The Ne uro-Symbolic Concept Learner: Interpreting Scenes, W ords , and Sentences
From Natural Supervision, in: 7th International Conference on Learning Representations , ICLR 2019, New Orleans, LA, USA, May 6-9,
2019, OpenReview .net, 2019.
[138] P . Kouris, G. Alexandridis and A. Stafylopatis, Abstr active T ext Summarization: Enhancing Sequence-to-Sequen ce Models
Using W ord Sense Disambiguation and Semantic Content Gener alization, Computational Linguistics 47(4) (2021), 813–859.
doi:10.1162/coli_a_00417.
[139] C.S. Pinhanez, P .R. Cavalin, V .H.A. Ribeiro, A.P . App el, H. Candello, J. Nogima, M. Pichiliani, M.A. Guerra, M. de Bayser, G.L. Malfatti
and H. Ferreira, Using Meta-Knowledge Mined from Identiﬁer s to Improve Intent Recognition in Conversational Systems, in: Proceedings
of the 59th Annual Meeting of the Association for Computatio nal Linguistics and the 11th International Joint Conferenc e on Natural
Language Processing, ACL/IJCNLP 2021, (V olume 1: Long P ape rs), V irtual Event, August 1-6, 2021 , C. Zong, F . Xia, W . Li and
R. Navigli, eds, Association for Computational Linguistic s, 2021, pp. 7014–7027. doi:10.18653/v1/2021.acl-long.5 45.
[140] W . Liu, J. T ang, X. Liang and Q. Cai, Heterogeneous grap h reasoning for knowledge-grounded medical dialogue syste m, Neurocomputing
442 (2021), 260–268. doi:10.1016/j.neucom.2021.02.021.
[141] P . Manda, S. SayedAhmed and S.D. Mohanty, Automated On tology-Based Annotation of Scientiﬁc Literature Using Dee p Learning, in:
Proceedings of The International W orkshop on Semantic Big D ata, SBD ’20, Association for Computing Machinery, New Y ork, NY ,
USA, 2020. ISBN 9781450379748. doi:10.1145/3391274.3393 636.
[142] Q. Huang, L. Deng, D. Wu, C. Liu and X. He, Attentive T ens or Product Learning, Proceedings of the AAAI Conference on Artiﬁcial
Intelligence 33(01) (2019), 1344–1351. doi:10.1609/aaai.v33i01.330113 44.
[143] Z. Chen, Q. Gao and L.S. Moss, NeuralLog: Natural Langu age Inference with Joint Neural and Logical Reasoning, in: Proceedings of
*SEM 2021: The T enth Joint Conference on Lexical and Computa tional Semantics , Association for Computational Linguistics, Online,
2021, pp. 78–88. doi:10.18653/v1/2021.starsem-1.7.
[144] K. Kogkalidis, M. Moortgat and R. Moot, Neural Proof Ne ts, in: Proceedings of the 24th Conference on Computational Natura l Language
Learning, Association for Computational Linguistics, Online, 2020 , pp. 26–40. doi:10.18653/v1/2020.conll-1.3.
[145] M. Wu, W . W ang and S.J. Pan, Deep W eighted MaxSA T for Asp ect-based Opinion Extraction, in: Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing (EMNLP) , Association for Computational Linguistics, Online, 2020 , pp. 5618–5628.
doi:10.18653/v1/2020.emnlp-main.453.
[146] J. Shi, X. Ding, L. Du, T . Liu and B. Qin, Neural Natural L ogic Inference for Interpretable Question Answering, in: Proceedings of the
2021 Conference on Empirical Methods in Natural Language Pr ocessing, Association for Computational Linguistics, Online and Pu nta
Cana, Dominican Republic, 2021, pp. 3673–3684. doi:10.186 53/v1/2021.emnlp-main.298.
[147] W . W ang and S.J. Pan, V ariational Deep Logic Network fo r Joint Inference of Entities and Relations, Computational Linguistics 47(4)
(2021), 775–812. doi:10.1162/coli_a_00415.
[148] T . Li and V . Srikumar, Augmenting Neural Networks with First-order Logic, in: Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics , Association for Computational Linguistics, Florence, It aly, 2019, pp. 292–302. doi:10.18653/v1/P19-
1028.
[149] H. Honda and M. Hagiwara, Question Answering Systems w ith Deep Learning-Based Symbolic Processing, IEEE Access 7 (2019),
152368–152378. doi:10.1109/ACCESS.2019.2948081.
[150] L. Y abloko, ETHAN at SemEval-2020 T ask 5: Modelling Ca usal Reasoning in Language Using Neuro-symbolic Cloud Comp uting, in:
Proceedings of the F ourteenth W orkshop on Semantic Evaluat ion, International Committee for Computational Linguistics, Barcelona
(online), 2020, pp. 645–652. doi:10.18653/v1/2020.semev al-1.83.
[151] R. Das, M. Zaheer, D. Thai, A. Godbole, E. Perez, J.Y . Le e, L. T an, L. Polymenakos and A. McCallum, Case-based Reason ing
for Natural Language Queries over Knowledge Bases, in: Proceedings of the 2021 Conference on Empirical Methods in N atural
Language Processing , Association for Computational Linguistics, Online and Pu nta Cana, Dominican Republic, 2021, pp. 9594–9611.
doi:10.18653/v1/2021.emnlp-main.755.

[152] H. Jiang, S. Gurajada, Q. Lu, S. Neelam, L. Popa, P . Sen, Y . Li and A. Gray, LNN-EL: A Neuro-Symbolic Approach to Short -text
Entity Linking, in: Proceedings of the 59th Annual Meeting of the Association fo r Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing (V olume 1: Long P apers) , Association for Computational Linguistics, Online, 2021 ,
pp. 775–787. doi:10.18653/v1/2021.acl-long.64.
[153] C. Dehua, Z. Keting and H. Jianrong, BDCN: Semantic Emb edding Self-explanatory Breast Diagnostic Capsules Netwo rk, in: Proceedings
of the 20th Chinese National Conference on Computational Li nguistics, Chinese Information Processing Society of China, Huhhot, China,
2021, pp. 1178–1189.
[154] P . V erga, H. Sun, L. Baldini Soares and W . Cohen, Adapta ble and Interpretable Neural MemoryOver Symbolic Knowledg e, in: Proceedings
of the 2021 Conference of the North American Chapter of the As sociation for Computational Linguistics: Human Language T echnologies,
Association for Computational Linguistics, Online, 2021, pp. 3678–3691. doi:10.18653/v1/2021.naacl-main.288.
[155] S. Chaudhury , P . Sen, M. Ono, D. Kimura, M. T atsubori an d A. Munawar, Neuro-Symbolic Approaches for T ext-Based Pol icy Learning, in:
Proceedings of the 2021 Conference on Empirical Methods in N atural Language Processing , Association for Computational Linguistics,
Online and Punta Cana, Dominican Republic, 2021, pp. 3073–3 078. doi:10.18653/v1/2021.emnlp-main.245.
[156] G. Lample and F . Charton, Deep Learning for Symbolic Ma thematics, arXiv preprint arXiv:1912.01412 (2019).
doi:10.48550/ARXIV .1912.01412.
[157] P . Smolensky , T ensor product variable binding and the representation of symbolic structures in connectionist sy stems, Artiﬁcial
Intelligence 46(1) (1990), 159–216. doi:https://doi.org/10.1016/0004- 3702(90)90007-M.
[158] A.S. Gordon and J.R. Hobbs, A F ormal Theory of Commonsense Psychology: How P eople Think P eople Think , Cambridge University
Press, 2017. doi:10.1017/9781316584705.
[159] H. Santos, M. Kejriwal, A.M. Mulvehill, G. Forbush and D.L. McGuinness, An experimental study measuring human ann otator
categorization agreement on commonsense sentences, Experimental Results 2 (2021), e19. doi:10.1017/exp.2021.9.
[160] R. Cartuyvels, G. Spinks and M.-F . Moens, Discrete and continuous representations and processing in deep learnin g: Looking forward,
AI Open 2 (2021), 143–159. doi:10.1016/j.aiopen.2021.07.002.
[161] E. Tsamoura, T . Hospedales and L. Michael, Neural-Sym bolic Integration: A Compositional Perspective, Proceedings of the AAAI
Conference on Artiﬁcial Intelligence 35(66) (2021), 5051–5060.
[162] G. Boleda, Distributional Semantics and Linguistic T heory, Annual Review of Linguistics 6(1) (2020), 213–234. doi:10.1146/annurev-
linguistics-011619-030303.
[163] X. Chen, C. Liang, A.W . Y u, D. Song and D. Zhou, Composit ional Generalization via Neural-Symbolic Stack Machines, in: Proceedings
of the 34th International Conference on Neural Information Processing Systems , NIPS’20, 2020. ISBN 9781713829546.
[164] V . Embar, D. Sridhar, G. Farnadi and L. Getoor, Scalabl e Structure Learning for Probabilistic Soft Logic, arXiv:1807.00973 [cs, stat]
(2018).
[165] M. Diligenti, M. Gori and C. Saccà, Semantic-based reg ularization for learning and inference, Artiﬁcial Intelligence 244 (2017), 143–165.
doi:10.1016/j.artint.2015.08.011.
[166] R. Manhaeve, S. Dumancic, A. Kimmig, T . Demeester and L . De Raedt, DeepProbLog: Neural Probabilistic Logic Progra mming,
Advances in Neural Information Processing Systems 31 (2018).
Appendix A. NeSy and Kautz Categories
T able 7
NeSy and Kautz Categories
NeSy (Ours) Kautz Refs.
Sequential 1. symbolic Neuro symbolic [78, 79, 109–114, 120–122, 126, 128, 130, 132, 138, 149]
[81, 107, 117, 119, 127, 139, 141, 153]
Nested 2. Symbolic[Neuro] [115, 118, 129, 143]
Cooperative 3. Neuro; Symbolic [80, 88, 116, 135, 137, 145–1 47, 151]
Compiled 4. Neuro: Symbolic → Neuro [76, 77, 82, 85, 125, 133, 134, 136, 140, 144, 150, 152, 1 54, 155]
5. Neuro_Symbolic [83, 108, 123, 124, 131, 142, 148]

Appendix B. Allowed V alues
T able 8
Allowed values
Feature Allowed values
Business application
Annotation, Argumentation mining, Causal Reasoning, Deci sion support, Dialog system, Emotion recognition,
Entity Linking, Entity Resolution, Image captioning, Info rmation extraction, KG Completion / link prediction,
Language modeling, N2F , Opinion extraction, Question answ ering, Reading comprehension, Relation extraction,
Sentiment analysis, T ext classiﬁcation, T ext games, T ext s ummarization
T echnical application Clustering, Generative, Inference , Classiﬁcation, Information extraction, Similarity
T ype of learning Supervised, Unsupervised, Semi-supervis ed, Reinforcement, Curriculum
T ype of reasoning Implicit, Explicit, Both
Language structure Y es, No
Relational structure Y es, No
NeSy goals Reasoning, OOD Generalization, Interpretabili ty , Reduced data, Transferability
Kautz category 1. symbolic Neuro symbolic, 2. Symbolic[Neuro], 3. Neuro; S ymbolic,
4. Neuro: Symbolic → Neuro, 5. Neuro_Symbolic, 6. Neuro[Symbolic]
NeSy category Sequential, Nested, Cooperative, Compiled

Appendix C. V enues
T able 9
V enues referred in the study
American Association for the Advancement of Science
American Chemical Society
American Institute of Physics
American Society for Microbiology
Association for Computing Machinery (ACM)
Association for Computational Linguistics (ACL)
Cairo University
Chongqing University of Posts and T elecommunications
Elsevier
Emerald
IEEE
IOS Press
Institute for Operations Research and the Management Scien ces
King Saud University
MIT Press
Mary Ann Liebert
Morgan & Claypool Publishers
Now Publishers Inc
Optical Society of America
Oxford University Press
Public Library of Science
SAGE
Society for Industrial and Applied Mathematics
Springer Nature
T aylor & Francis
University of California Press
University of Minnesota
Wiley-Blackwell

Appendix D. Acronyms
T able 10
Acronyms and Abbreviations
AAAI Association for the Advancement of Artiﬁcial Intellig ence
ACL Association for Computational Linguistics
AI Artiﬁcial Intelligence
AR Analogical Reasoning
CBR Case based reasoning
CNN Convolutional Neural Network
DBN Deep Belief Network
DL Deep Learning
DLs Description Logic
GA T Graph Attention Network
GCN Graph Convolutional Network
GNN Graph Neural Network
GPT3 Third generation Generative Pre-trained Transformer
IJCAI International Joint Conference on Artiﬁcial Intelli gence
ILP Inductive Logic Programming
KG Knowledge Graphs
KGC Knowledge Graph Completion
KGQA Knowledge Graph Question Answering
KR Knowledge Representation
KRR Knowledge Representation & Reasoning
LNN Logical Neural Networks
LLM Large Language Models
LSTM Long Short T erm Memory
L TN Logic T enson Network
ML Machine Learning
MLN Markov Logic Network
MLP Multilayer Perceptron
MWP Math W ord Problem
NE Neuroevolution
NeSy Neuro-Symbolic AI
NL Natural Logic
NLI Natural Language Inference
NLG Natural Language Generation
NLM Neural Logic Machine
NLP Natural Language Processing
NLU Natural Language Understanding
NS-CL Neuro-Symbolic Concept Learner
NTP Neural Theorem Prover
NN Neural Network
OOD Out-of-distribution
OOP Object-oriented programming(paradigm)
OWL W eb Ontology Language
ProbLog Probabilistic Logic Programming
RcNN Recursive Neural Network
RL Reinforcement Learning
RNKN Recursive Neural Knowledge Network
RNN Recurrent Neural Network
SOT A State of the Art
SVM Support V ector Machine
TPR T ensor Product Representation
TSP Traveling Salesperson Problem
(∂ILP) Differentiable Inductive Logic Programming

This figure "iospress.png" is available in "png"
 format from:
http://arxiv.org/ps/2202.12205v2
