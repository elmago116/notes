---
title: "Neuro-symbolic artificial intelligence- a survey"
type: article
base: clippings
source: pdf
tags:
  - Tech/NeuroSymbolic
---

Linked PDF file(s) for **Neuro-symbolic artificial intelligence- a survey**:

- [[PDF/Neuro-symbolic artificial intelligence- a survey.pdf]]

## PDF text extraction

REVIEW
Neuro-symbolic artificial intelligence: a survey
Bikram Pratim Bhuyan1,2 • Amar Ramdane-Cherif 1 • Ravi Tomar 3 • T. P. Singh4
Received: 8 May 2023 / Accepted: 3 May 2024 / Published online: 6 June 2024
/C211The Author(s), under exclusive licence to Springer-Verlag London Ltd., part of Springer Nature 2024
Abstract
The goal of the growing discipline of neuro-symbolic artiﬁcial intelligence (AI) is to develop AI systems with more
human-like reasoning capabilities by combining symbolic reasoning with connectionist learning. We survey the literature
on neuro-symbolic AI during the last two decades, including books, monographs, review papers, contribution pieces,
opinion articles, foundational workshops/talks, and related PhD theses. Four main features of neuro-symbolic AI are
discussed, including representation, learning, reasoning, and decision-making. Finally, we discuss the many applications of
neuro-symbolic AI, including question answering, robotics, computer vision, healthcare, and more. Scalability, explain-
ability, and ethical considerations are also covered, as well as other difﬁculties and limits of neuro-symbolic AI. This study
summarizes the current state of the art in neuro-symbolic artiﬁcial intelligence.
Keywords Neuro-symbolic artiﬁcial intelligence /C1 Machine learning /C1 Knowledge representation and reasoning /C1
Spatial-temporal data /C1 Neural networks /C1 Artiﬁcial intelligence
1 Introduction
There have been several breakthroughs and innovations in
the areas of artiﬁcial intelligence (AI) and deep learning
(connectionist artiﬁcial intelligence) during the last decade
[1]. The widespread use of AI and deep learning as cutting-
edge technologies has been a signiﬁcant recent develop-
ment. Several industries, including healthcare, banking,
transportation, agriculture, and arts, have proﬁted from
recent artiﬁcial intelligence and deep learning develop-
ments [2–4].
New technologies have advanced deep learning models
in computer vision and natural language processing. Con-
volutional neural networks (CNNs) and transformers have
improved sectors like image recognition and language
translation [ 5]. Generative adversarial networks (GANs)
and variational autoencoders (VAEs) may produce new
data, images, and sounds [ 6]. Music production and design
might leverage these models. Edge computing, another
decade-old breakthrough, allows AI model installation on
low-resource devices. Thus, AI and deep learning models
may be applied on edge, closer to the data source, which is
beneﬁcial in constructing Internet of Things (IoT) devices
[7].
Yet, connectionist AI is not without its caveats. One
drawback is that training models properly usually require a
lot of data (typically involving highly unstructured, per-
ceptual data). These AI models may also lack the trans-
parency and explainability of other forms of AI due to the
complexity involved in understanding how they arrive at
their predictions or choices [ 8].
Symbolic AI, commonly known as ‘‘good old-fashioned
AI’’, emerged as the foundation of AI research during the
mid-twentieth century with notable ﬁgures such as Allen
Newell and Herbert A. Simon [ 9–11]. Referred to as rule-
based or expert systems, they were designed and imple-
mented with a predeﬁned set of explicit rules and logical
reasoning mechanisms to address and resolve various
problems. Ontologies were conceived as a means of rep-
resenting and sharing knowledge [ 12]. Although symbolic
& Bikram Pratim Bhuyan
bikram-pratim.bhuyan@universite-paris-saclay.fr
1 LISV Laboratory, University of Paris Saclay, 10-12 Avenue
of Europe, 78140 Velizy, France
2 School of Computer Science, University of Petroleum and
Energy Studies, Bidholi, Dehradun, Uttarakhand 248006,
India
3 Persistent Systems, Pune, Mumbai 411016, India
4 School of Computer Science Engineering and Technology,
Bennett University, Greater Noida 201306, India
123
Neural Computing and Applications (2024) 36:12809–12844
https://doi.org/10.1007/s00521-024-09960-z(0123456789().,-volV)(0123456789().,-volV)

AI demonstrated proﬁciency in problem domains charac-
terized by explicit rules and clear boundaries, they
encountered difﬁculties when confronted with incomplete
information [ 13]. Thus, the efﬁciency of these systems is
hugely dependent on the completeness of the knowledge.
The drawbacks of both the ﬁelds individually in terms of
‘Explainability’, ‘Efﬁciency’, and ‘Generalization’ could
be seen through Fig. 1. The efﬁciency of connectionist AI
is typically considered high due to its ability to process vast
amounts of data and learn complex patterns through neural
networks. This efﬁciency stems from the processing
capabilities of neural networks, which can handle and learn
from high-dimensional data, making them particularly
adept at tasks like image and speech recognition, where
they can directly learn from raw inputs to outputs.
On the other hand, the efﬁciency of symbolic AI is often
viewed as lower, particularly in the context of processing
large datasets or handling perceptual tasks. Symbolic AI
operates on explicit rules and logic, which can be com-
putationally intensive and less ﬂexible when dealing with
nuanced or ambiguous data that does not ﬁt neatly into
predeﬁned categories or rules. While symbolic AI excels in
tasks that require clear, logical reasoning and inter-
pretability, its rule-based nature can limit its efﬁciency in
scenarios where learning from data or scaling to large
problem spaces is essential.
However, it’s crucial to contextualize these efﬁciency
considerations within the speciﬁc domains and tasks to
which each AI approach is applied. While connectionist AI
may show higher efﬁciency in data-driven, pattern recog-
nition tasks, symbolic AI can be more efﬁcient in domains
where clear reasoning, interpretability, and adherence to
explicit knowledge or rules are paramount. This distinction
underscores the complementary nature of these approaches,
highlighting the potential of neuro-symbolic AI to leverage
the strengths of both to achieve higher overall efﬁciency
across a broader range of tasks.
The roots of neuro-symbolic (NeSy) AI may be traced
all the way back to the 1950s and 1960s when the ﬁeld of
AI was getting its start [ 14]. In the past, artiﬁcial intelli-
gence studies focused on creating rule- and symbol-based
problem-solving machines. In the 1980s, however,
Fig. 1 The drawbacks of both the ﬁelds individually in terms of ‘Explainability’, ‘Efﬁciency’, and ‘Generalization’, when the ﬁelds merge
together to form neuro-symbolic artiﬁcial intelligence, all three characteristics are high
12810 Neural Computing and Applications (2024) 36:12809–12844
123

scientists started to see the method’s ﬂaws. For example,
natural language processing and vision were shown to be
areas where symbolic AI systems faltered. Researchers
began implementing neuroscientiﬁc principles into AI
systems to address these shortcomings. In the early twenty-
ﬁrst century, scientists started looking at ways to combine
the best features of the two methods. They came up with a
new branch of AI, neuro-symbolic AI, which combines
symbolic reasoning and representation with neural net-
works. It has been used in disparate ﬁelds such as health-
care, robotics, and natural language processing. One of the
most exciting directions in artiﬁcial intelligence research
today is neuro-symbolic AI, which aims to create intelli-
gent systems that can learn and reason like humans. The
growing interest in the ﬁeld could be seen through the
amount of literature published, as shown in Fig. 2. The
literature contains books, monographs, thesis [ 15–23],
review papers [ 20, 24–33], contributory articles [ 34–95],
commentary articles [25, 39, 93, 96–143], and foundational
workshops/talks [ 144–167]. It’s worth noting that neuro-
synthetic AI is a hot topic in both academia and industry
because of its immense potential for artiﬁcial general
intelligence.
Neuro-symbolic AI is a kind of AI that takes cues from
the way the human brain processes information while also
relying on symbolic logic to solve issues. The study of the
brain and its functions serves as inspiration for the ‘‘neuro’’
component of neuro-symbolic AI [ 33]. The ‘‘neuro’’
component of this AI makes use of neural networks to learn
from data and enhance its grasp of the environment, much
like the way human brains process information and learn
from experience. The ‘‘symbolic’’ component of neuro-
symbolic AI uses symbolic representations and logical
reasoning to accomplish its goals. This suggests that the AI
can think logically and grasp notions like ‘‘if-then’’
statements. Knowledge may also be represented in a
human-understandable form, for as via the use of words
and symbols to stand in for real-world entities and abstract
concepts.
Recent research on neural-symbolic integration, which
seeks to combine the capabilities of symbolic AI with
neural networks to produce more powerful and adapt-
able intelligent systems, is surveyed in the articles as
shown in Table 1, and we base our classiﬁcation method
based on this with the objective of harnessing the com-
plementing capabilities of the two paradigms [ 168]. The
criteria for classiﬁcation are taken from the Kautz’s talk
[169], which is even regarded as the turning point of the
ﬁeld [ 33].
All of the major developments over the last two decades
are summarized in this survey article. It delves into the
numerous aspects that have led to the hybridization of
connectionist AI and symbolic AI. Its applications in many
ﬁelds are also examined. The challenges are also being
considered. Figure 3 depicts a conceptual map of the arti-
cle. The organization of the survey is shown in Fig. 4.
2 Background and related work
2.1 Neuro-symbolic properties
We delve into the core components that deﬁne neuro-
symbolic AI, encompassing representation, learning, rea-
soning, decision-making, knowledge, and logic. This
exploration provides insight into how neuro-symbolic AI
seeks to amalgamate the strengths of symbolic and neural
approaches to overcome their limitations.
Fig. 2 Peer reviewed papers in
the ﬁeld of neuro-symbolic AI
with keywords, ‘neuro-
symbolic’, ‘neural-symbolic’,
‘neuro symbolic’, ‘neural
symbolic’ and ‘neurosymbolic’
Neural Computing and Applications (2024) 36:12809–12844 12811
123

2.1.1 Representations
When discussing symbolic AI, ‘‘localist representations’’
refer to using isolated symbols to stand in for abstract ideas
or concrete objects [ 170]. Expert systems and rule-based
systems are two examples of symbolic AI that extensively
use localist representations [171]. As each sign represents a
distinct idea that humans can readily grasp, they beneﬁt
from being interpretable and transparent.
In contrast to localist representations, distributed repre-
sentations [170] have gained traction in recent years, par-
ticularly in the context of deep learning. Distinct
dimensions of a vector of real-valued integers in distributed
representations represent different features or aspects of a
topic. This paves the way for more versatile and potent
representations that encapsulate subtle but signiﬁcant data
linkages and patterns. The difference can be seen in Fig. 5.
Localist and distributed representation has their own
beneﬁts and drawbacks, as shown in Table 2.
Attention systems, graph neural networks, differentiable
programming, variable grounding, symbol manipulation,
and foundation model representation techniques make
neuro-symbolic AI integration unique in the ﬁeld.
Attention mechanisms in neuro-symbolic AI improve
the model’s focus on relevant parts of the input data or
internal representations. This is particularly used in tasks
requiring sequential data processing, like natural language
understanding by [ 91, 172], where the model needs to
focus on relevant parts of the input sequence to make
decisions or predictions.
Graph neural networks (GNNs) are pivotal in repre-
senting and processing data in graph form, which is
inherently symbolic. GNNs can capture the complex
relationships and structures within data, making them ideal
for tasks that involve relational reasoning, knowledge
graphs, and structured prediction. [173] surveys around this
integration for encoding both entity attributes and the
relationships between entities in a way that is amenable to
neural network processing.
Differentiable programming extends the capabilities of
neural networks by making them more ﬂexible and capable
of incorporating symbolic computation within the learning
process. [ 174, 175] uses this approach to enable the inte-
gration of symbolic reasoning directly into the neural net-
work’s architecture, allowing for the optimization of
symbolic operations alongside standard neural network
parameters, facilitating a tighter integration of symbolic
and sub-symbolic AI components.
Variable grounding refers to the process of linking
abstract symbols or concepts to concrete instances in data.
In the context of neuro-symbolic AI, [ 176, 177] involves
the identiﬁcation and association of symbolic variables
with relevant features or patterns learned by the neural
network, enabling the system to reason about abstract
concepts in a grounded, data-driven context.
Symbol manipulation in neuro-symbolic systems
involves the use of operations on symbols that represent
abstract concepts, akin to traditional symbolic AI.
[178, 179] integrated these operations within a neural
framework. Neuro-symbolic AI systems can perform
symbolic reasoning, such as logical deduction and infer-
ence, while also beneﬁting from the adaptive learning
capabilities of neural networks.
Finally, leveraging foundation models for representation
can enhance performance in neuro-symbolic tasks, reduce
data labeling, and minimize manual engineering, as
Table 1 Review papers with the discussion upon the domain, properties, type of neural architecture and neuro-symbolic types represented by NS
Properties
Paper Year Domain Representation Learning Reasoning Decision making Logic Neural type NS
Corchado et al. [ 24] 2002 Oceanography – – – – – U –
Hatzilygeroudis et al. [ 25] 2004 Expert Systems – – – – – – –
O¨ ztu¨ rk et al. [ 26] 2014 CBR – – – – – – –
Besold et al. [ 27] 2017 General – – – – UU –
Garnelo et al. [ 28] 2019 General U –– – – – –
Garcez et al. [ 29] 2019 General – UU – U ––
De et al. [ 30] 2020 General – – – – UU –
Sarker et al. [ 31] 2021 General – UU - U – U
Hitzler et al. [ 20] 2022 General – – – – – – –
Wang et al. [ 32] 2022 General – UU U U ––
Garcez et al. [ 33] 2023 General U – U –- – U
Our survey 2024 General UU U U U U U
12812 Neural Computing and Applications (2024) 36:12809–12844
123

demonstrated by the introduction of architectures like
NeSyGPT [180].
2.1.2 Learning
Neuro-symbolic AI introduces a paradigm shift in how
machines learn, blending the deductive, rule-based learning
of symbolic AI with the inductive, pattern-recognizing
capabilities of neural networks. This hybrid approach
leverages the strengths of both domains to facilitate a more
comprehensive learning methodology.
Traditional symbolic AI learns through logical deduc-
tion, inducing general rules from speciﬁc instances. Tech-
niques like decision tree induction [ 181] and explanation-
based learning [182] exemplify this, where new knowledge
is systematically derived from existing rules and examples.
However, this method’s reliance on extensive manual
curation of knowledge bases and datasets is a notable lim-
itation [183].
In contrast, connectionist AI, particularly through deep
learning, excels at learning representations from raw,
unstructured data [ 184]. It employs various techniques
(e.g., supervised, unsupervised, and reinforcement learning
[185]) to adjust neural connections, enabling pattern
recognition and decision-making. While powerful, this
approach often lacks transparency and interoperability.
Neuro-symbolic AI (NeSy) aims to transcend these
limitations by integrating the structured knowledge repre-
sentation of symbolic AI with the adaptive learning
mechanisms of neural networks. This integration enables
Neuro-Symbolic AI
Domain
Robotics
[8–13]
Question
Answering
[14–21]
Medical
applications
[22–29]
Computer
Vision
[30–43]
Programming
and Opti-
mization
[21, 44–53]
Other
Sciences
[54–80]
Properties
Representation
Learning
Reasoning
Decision
Making
Logic
Contribution
Type
Books/
Mono-
graphs
/ Thesis
[46, 81–88]
Review
Papers
[85, 89–98]
Contributory
Articles [ 21,
21, 45, 65,
76, 99–156]
Commentary
Articles [ 90,
104, 154,
157–204]
Foundational
Workshops
/ talks
[205–228]
Type
Type 1 [ 8,
9, 14, 15,
30, 54, 55,
229, 230]
Type 2 [ 22,
31, 56–69]Type 3
[10–13,
32–36, 70]
Type 4
[23–28,
44, 71–76]
Type 5 [ 16–
18, 29, 37–
43, 77, 78,
231–233]
Type 6
[19, 79, 80,
234–236]
Fig. 3 A conceptual map of the survey, depicting the wide range of neuro-symbolic AI implementations, their respective type of integration,
contribution kinds, and properties
Neural Computing and Applications (2024) 36:12809–12844 12813
123

NeSy systems to: (a) learn from fewer examples by
leveraging pre-existing symbolic knowledge, thus
addressing the data-hungry nature of pure neural approa-
ches; (b) enhance interpretability by grounding neural
network outputs in symbolic representations, making the
learning process and outcomes more understandable;
(c) facilitate adaptable reasoning that combines the
robustness of neural pattern recognition with the precision
of symbolic logic; and (d) incorporate feedback loops
where symbolic reasoning can guide neural learning and
vice versa, enabling dynamic adaptation to new informa-
tion or tasks. The comparison is shown in Table 3.
2.1.3 Reasoning
Reasoning, a fundamental aspect of intelligence, has been
approached differently across the AI spectrum. The trade-
off between learning and reasoning in symbolic AI and
connectionist AI can be shown in Table 4. Symbolic AI,
with its roots in formal logic and knowledge representation,
traditionally employs deductive, inductive, and abductive
reasoning [ 186]. These methods allow for deriving con-
clusions from known premises, generalizations from
speciﬁc instances, and formulating plausible explanations
from observations [186, 187]. While powerful in structured
environments, symbolic reasoning struggles with ambigu-
ity and the inherent uncertainty of real-world data.
In contrast, connectionist models, particularly neural
networks, excel in pattern recognition and inference from
vast datasets but cannot traditionally perform explicit, rule-
based reasoning. However, there has been some recent
work on developing reasoning tasks based on neural net-
works. For example, some researchers have explored using
neural networks to understand natural language and answer
questions [188]. Other researchers have looked into neural-
symbolic integration, in which neural networks are used to
learn representations of complex data, which are fed into
symbolic reasoning systems to make logical inferences
[189]. Even with all these efforts, making neural network-
based approaches to reasoning tasks work well is still
tough, especially when explicit rules or logic are needed.
These challenges include how hard it is to encode symbolic
information in a distributed representation, how fragile
neural networks are when dealing with new inputs, and
how little they can do abstract reasoning or ﬁgure out what
information is missing.
Another important discussion is on combinatorial and
common-sense reasoning [33]. Common-sense reasoning is
a type of approximate reasoning that involves making
assumptions or inferences based on general knowledge and
experience rather than on explicit rules or algorithms.
Problems in mathematics, computer science, and engi-
neering are typically solved with the use of combinatorial
reasoning methods, including counting principles, permu-
tations, and combinations. The emergence of neuro-sym-
bolic AI represents a paradigm shift, aiming to meld the
structured reasoning capabilities of symbolic AI with the
adaptive learning process of neural networks [ 136]. The
various types of reasoning used are shown in Fig. 6.
Fig. 4 Organization of the article as a ﬂowchart
12814 Neural Computing and Applications (2024) 36:12809–12844
123

Under NeSy, CTLK (Temporal-Epistemic Reasoning)
[39, 40] exempliﬁes the application of deductive reasoning
in neuro-symbolic systems, showcasing how neural
networks can be employed to interpret and defend trans-
lations of non-classical logics, including temporal logic.
CIL2P [36, 37] (Connectionist Inductive Learning and
Fig. 5 Difference between localist and distributed representations
Table 2 Comparison of localist and distributed representations and integration in neuro-symbolic AI
Aspect Localist representation Distributed representation
Deﬁnition Represents concepts with dedicated units or nodes in the
network, where each unit represents a single concept or
category
Represents concepts across many units, with each unit
participating in the representation of multiple concepts,
allowing for more nuanced representations
Beneﬁts High interpretability and transparency
Easier manipulation of individual concepts
Simpliﬁes mapping of symbolic knowledge
Greater capacity for generalization
Efﬁcient use of network capacity
Facilitates learning of complex patterns
Drawbacks Limited scalability with the number of concepts
Less efﬁcient in capturing complex patterns
Reduced interpretability of individual units
Integration of explicit symbolic knowledge can be challenging
Neuro-
symbolic AI
integration
Neuro-symbolic AI leverages both approaches, utilizing localist representations for symbolic components and distributed
methods for neural processing, enabling efﬁcient integration of symbolic reasoning with neural learning
Neural Computing and Applications (2024) 36:12809–12844 12815
123

Logic Programming) serves as a prime example of induc-
tive reasoning in neuro-symbolic AI, where a neural net-
work is trained using propositional logic and then used to
derive logical programs from the learned representations.
MicroPsi [ 58, 59], CORGI (COmmonsense Reasoning by
Instruction) and COMET (COMmonsense Transformers)
[81, 82] stand out as a signiﬁcant contribution toward
modeling common-sense reasoning within a neuro-sym-
bolic framework, focusing on cognitive architecture and
autonomous motivation, which are essential for common-
sense understanding and decision-making. DeepProbLog
[75–77] integrates probabilistic logic programming with
neural networks, offering a powerful approach to combi-
natorial reasoning where the system can reason over
complex, structured data and learn from uncertain infor-
mation, making it relevant for tasks that require combina-
torial reasoning capabilities.
2.1.4 Decisions
Neuro-symbolic AI advances decision-making by inte-
grating the rapid, intuitive processing akin to Kahneman’s
System 1 with the deliberate, logical reasoning of System 2
[190]. Table 5 summarizes the two types of decision-
making in ‘‘Thinking, Fast and Slow’’ and their relation-
ship to neuro-symbolic AI.
Neuro-symbolic models incorporate neural network
components that mimic System 1 thinking by processing
sensory data rapidly to produce intuitive responses. These
components are adept at recognizing patterns and making
quick predictions, similar to the fast and subconscious
decision-making observed in humans. For instance, neural
learning within NeSy can be trained on large datasets to
swiftly identify patterns, akin to how humans rely on
heuristics and past experiences for immediate decision-
making.
Symbolic components within NeSy frameworks reﬂect
System 2 thinking, employing logical rules and knowledge
representation for reasoned analysis and decision-making.
This aspect allows NeSy systems to handle complex,
structured problems that require careful deliberation and
logic. Techniques such as rule-based inference and sym-
bolic manipulation enable NeSy models to perform tasks
that necessitate a deep understanding of relationships and
concepts, mirroring humans’ slow, conscious decision-
making process.
The logical neural networks (LNNs) developed by IBM
Research [ 86] embody aspects of System 2 thinking by
Table 3 Comparison of learning paradigms in neuro-symbolic AI
Learning
paradigm
Characteristics Neuro-symbolic integration
Symbolic
learning
Involves logical deduction and induction to generate rules
from data. Highly interpretable but requires extensive
knowledge engineering
NeSy integrates symbolic rules with neural learning, allowing
for the derivation of symbolic knowledge from neural
representations, enhancing interpretability and leveraging
pre-existing knowledge
Connectionist
learning
Utilizes neural networks to learn patterns from large
datasets. Excels in generalization but lacks transparency
NeSy harnesses neural networks for pattern recognition and
generalization, while grounding the learned patterns in
symbolic representations for improved transparency and
reasoning
Hybrid
learning
Aims to combine the strengths of symbolic and connectionist
approaches, often using separate components for each
NeSy embodies true hybrid learning by deeply integrating
symbolic and neural processes within a uniﬁed framework,
enabling dynamic, bidirectional interaction between
symbolic reasoning and neural learning
Reinforcement
learning
Involves learning through interaction with an environment
and receiving feedback in the form of rewards
NeSy applies reinforcement learning principles to both
symbolic and neural components, enabling the system to
reﬁne its strategies and knowledge through experience
Unsupervised
learning
Focuses on discovering hidden patterns or structures in
unlabeled data
In NeSy, unsupervised learning techniques can be used to
uncover latent symbolic structures within data, which can
then be explicitly represented and manipulated
Table 4 Trade-off between learning and reasoning in symbolic AI
and neural networks
Quantiﬁcation Symbolic AI Neural network
Reasoning Learning Reasoning Learning
Universal (8) Easy Hard
Existential (9) Hard Easy
12816 Neural Computing and Applications (2024) 36:12809–12844
123

supporting ﬁrst-order logic, allowing for the representation
of more complex kinds of knowledge in a way that’s
understandable and can represent uncertainty. LNNs
improve predictive accuracy by representing the strengths
of relationships between logical clauses via neural weights.
They are tolerant of incomplete knowledge, unlike many
AI approaches that make closed-world assumptions. This
feature enables LNNs to operate under more realistic,
open-world assumptions, accommodating incomplete
knowledge robustly.
The Neuro-Symbolic Question Answering (NSQA)
system [191] is another example where IBM Research has
applied NeSy for knowledge-based question answering,
requiring advanced reasoning such as multi-hop, quantita-
tive, geographic, and temporal reasoning. The NSQA
approach translates natural language questions into an
abstract form that captures the conceptual meaning,
allowing reasoning over existing knowledge to answer
complex questions. This method provides interpretability,
Fig. 6 Different types of reasoning which are not mutually exclusive and can often be used in combination with one another
Table 5 A table summarizing the two types of decision-making in ‘‘Thinking, Fast and Slow’’ and their relationship to neuro-symbolic AI
Type of
decision-
making
Description Relationship to neuro-symbolic AI
System 1 Fast, automatic, subconscious decision-
making based on heuristics and intuition
Similar to neural learning, where the system is trained on large amounts of data
to quickly recognize patterns and make predictions.
System 2 Slow, deliberate, conscious decision-making
based on reasoning, analysis, and logic
Similar to symbolic learning, where the system is provided with explicit logical
rules and knowledge representation to reason about concepts and
relationships.
Neural Computing and Applications (2024) 36:12809–12844 12817
123

generalizability, and robustness, which are critical in
enterprise natural language processing settings.
Implementations like Scallop [ 192], which supports
differentiable logical and relational reasoning, and Deep-
ProbLog [ 75–77], which combines neural networks with
probabilistic reasoning, further illustrate the versatility and
depth of NeSy approaches in bridging the gap between
neural and symbolic architectures. These implementations
showcase how NeSy can leverage large-scale learning and
symbol manipulation for robust intelligence.
2.1.5 Knowledge and logic
Neuro-symbolic AI synergizes the structured expressive-
ness of logic with the adaptive learning capabilities of
neural networks, fostering systems that excel in reasoning
and knowledge representation. Figure 7 gives a pictorial
view of such a framework’s various kinds of logic.
NeSy architectures frequently employ propositional
logic for its simplicity in representing binary relationships
and decision processes. First-order logic (FOL), with its
ability to quantify individuals, extends this capacity,
allowing for more intricate representations of real-world
scenarios. Integrating FOL in NeSy facilitates reasoning
about entities and their relations, enhancing the system’s
ability to generalize from speciﬁc instances to broader
concepts [20, 193].
Higher-order logic (HOL) further expands the expres-
sive power of NeSy systems by enabling quantiﬁcation
over predicates and functions. This allows for the modeling
of complex abstractions and relationships, which is pivotal
for tasks requiring deep semantic understanding. However,
the increased expressiveness of HOL comes with chal-
lenges in decidability and computational efﬁciency,
necessitating innovative solutions within NeSy frameworks
to harness its potential effectively [ 29, 194].
Logic is a foundational pillar for knowledge represen-
tation in NeSy, providing a formal structure for encoding
domain-speciﬁc rules and relationships. By mapping logi-
cal constructs to neural representations, NeSy systems can
leverage the robustness of neural learning while adhering
to the precision of logical reasoning. This dual approach
not only enhances the system’s interpretability but also its
adaptability to complex reasoning tasks [ 31, 195].
Knowledge graphs represent a pivotal component of
NeSy, offering a structured and interconnected framework
for representing complex knowledge bases. By encapsu-
lating entities, concepts, and their relationships in a graph
structure, knowledge graphs enable NeSy systems to per-
form sophisticated reasoning and inference, drawing on the
rich semantic connections encoded within the graph
[196, 197].
2.2 Neuro-symbolic: best of both worlds
Neuro-symbolic AI can build more powerful reasoning and
learning systems by combining the strengths of deep
learning-based methods and symbolic reasoning tech-
niques. However, the key research questions (included in
Wikipedia) asked [ 198] were:
A. What is the best way to integrate neural and symbolic
architectures?
B. How should symbolic structures be represented within
neural networks and extracted from them?
C. How should common-sense knowledge be learned and
reasoned about?
D. How can abstract knowledge that is hard to encode
logically be handled?
We now try to ﬁnd the solutions to these questions in the
major algorithms/paradigms/language/frameworks devel-
oped for neuro-symbolic artiﬁcial intelligence integration
Fig. 7 Various disciplines of logic: a. Symbolic expressions—delving
into the language of mathematics and logic, symbolic expressions use
variables and operations to represent complex ideas succinctly. For
example, ‘a ?b?2cosA’ and ‘1 ?5/(6*10)?15’ demonstrate how
mathematical symbols and functions can encapsulate calculations or
relationships. b. Propositional logic—this discipline focuses on
forming and analyzing statements that can be either true or false. c.
First-order logic—extends propositional logic by incorporating
quantiﬁers and variables that can represent objects in a domain. d.
Higher-order logic—builds on ﬁrst-order logic by allowing functions
and predicates to be inputs to other functions and predicates,
facilitating more complex expressions of ideas. e. Knowledge
graphs—representing complex networks of real-world information,
knowledge graphs connect entities (such as individuals, places, and
objects) through edges that represent their interrelations
12818 Neural Computing and Applications (2024) 36:12809–12844
123

during the last two decades. The summary of these
frameworks is in Table 6. From Table 6, we can now cover
some discussions based on the four questions posed.
The integration of neural and symbolic architectures has
been approached in various innovative ways. Early meth-
ods like KBANN [34] and Penalty Logic [ 35] laid the
groundwork by mapping propositional logic and penalty
systems onto neural networks, respectively. As the ﬁeld
evolved, more sophisticated frameworks like LTN
[62, 66–68] and Tensor Networks [ 62] emerged, offering
richer representations and interactions within neural net-
works through tensors and differentiable logical languages.
More recent advancements like DeepLogic [ 92] and HRI
[93] have focused on simultaneous learning of perception
and reasoning, and hierarchical rule induction, showcasing
the continuous evolution toward more seamless and efﬁ-
cient integration methods.
The representation and extraction of symbolic structures
within neural networks have seen signiﬁcant advance-
ments. Early models like NSL [ 38] and CTLK [ 39, 40]
introduced context-free languages and the capability to
interpret non-classical logics, respectively. Over time,
models like NTP [ 65] and DeepProbLog [ 75–77] have
enhanced the representation of complex logical structures
and probabilistic logic programming within neural net-
works. These developments highlight a trend toward more
expressive and interpretable neuro-symbolic systems cap-
able of embedding and reasoning with intricate symbolic
information.
Learning and reasoning about common-sense knowl-
edge have been central to neuro-symbolic AI’s evolution.
Initial approaches like CIL
2P [36] and SATyrus [ 41]
focused on inductive learning and constraint processing.
Later, models like NLM [ 78] and NSPS [62] demonstrated
scalable learning from small to larger tasks and program
synthesis, respectively, indicating a growing capability in
common-sense reasoning. The introduction of models like
CORGI [ 89] and NSFR [ 90], which engage in conversa-
tional reasoning and forward-chaining reasoning, respec-
tively, showcases the ﬁeld’s progression toward more
dynamic and interactive common-sense reasoning systems.
The handling of abstract knowledge has evolved from
simpler logic mapping and penalty systems in models like
K
BANN [34] and Penalty Logic [ 35] to more complex
hierarchical and adaptive systems seen in HRI [ 93] and
DeepLogic [92]. These recent developments demonstrate a
signiﬁcant advancement in neuro-symbolic AI’s ability to
process, reason, and learn from abstract concepts, moving
closer to human-like reasoning capabilities.
2.3 Neuro-symbolic types
2.3.1 Type 1: symbolic neuro-symbolic
In the domain of type 1 neuro-symbolic AI, the interplay
between neural networks and symbolic reasoning forms the
cornerstone of representation, inference, and learning pro-
cesses. Here, neural networks are harnessed for their
powerful representational learning capabilities, enabling
the extraction of nuanced patterns and features from
complex data. This is particularly evident in natural lan-
guage processing, where neural network-based vector
embeddings, such as those developed by [ 199, 200],
transform input symbols into rich, continuous vector
spaces. These embeddings capture semantic and syntactic
relationships inherent in the data, facilitating a broad
spectrum of neural network-driven tasks like classiﬁcation,
prediction, and sequence generation.
Conversely, symbolic reasoning within type 1 systems is
deployed to imbue these neural representations with
structured, logical frameworks. This symbolic layer is
pivotal for encoding knowledge, performing deductive
reasoning, and ensuring the interpretability of the AI sys-
tem’s operations. It leverages symbols and formal logic to
articulate rules and constraints, thereby guiding the deci-
sion-making processes in a transparent and explainable
manner.
The fusion of neural networks and symbolic reasoning
in type 1 neuro-symbolic AI endeavors to marry the
adaptive, data-driven insights of neural networks with the
clarity and rigor of symbolic logic. This hybrid approach
not only enhances the system’s ability to process and
interpret complex, real-world data but also ensures that its
operations remain grounded in logical principles that are
comprehensible to human operators.
Figure 8 illustrates this synergistic relationship between
neural representation and symbolic logic, highlighting how
each contributes to the system’s overall functionality.
Sequential methodologies within this category, such as
language translation or graph categorization, exemplify the
application of neural networks for symbolic processing.
However, as outlined in Table 7, despite their advance-
ments, these integrations highlight the ongoing challenges
in achieving the full potential of neuro-symbolic
integration.
2.3.2 Type 2: symbolic [neuro]
Systems of type 2 neuro-symbolic AI employ neural net-
works as subroutines inside a broader symbolic problem
solver; these systems are hybrid but are predominantly
symbolic. Loose coupling between the symbolic and neural
Neural Computing and Applications (2024) 36:12809–12844 12819
123

Table 6 Major algorithms/paradigms/language/frameworks developed for neuro-symbolic artiﬁcial intelligence integration during the last two
decades
Authors/Work
(Ref)
Year Question A: Best way to
integrate
Question B:
Representation and
extraction of symbolic
structures
Question C: Learning and
reasoning about common-
sense knowledge
Question D: Handling
abstract knowledge
K
BANN [34] 1994 Hybrid learning system
mapping domain theories
onto neural networks
Propositional logic
encoded within neural
architectures
Utilizes past knowledge
for generalization, aiding
common-sense reasoning
Demonstrates superior
generalization in
molecular biology,
indicating effective
handling of abstract
concepts
Penalty Logic
[35]
1995 Penalty Logic as an
alternative connectionist
paradigm for integration
Embeds symbolic
structures as penalties
within neural networks
Addresses nonmonotonic
reasoning and
inconsistent beliefs,
relevant to common-
sense knowledge
Penalty system allows for
approximation and
reasoning about abstract
knowledge
CIL
2P [36] 1999 CIL2P model based on
feed-forward ANN and
logic programming
Utilizes a translational
technique for embedding
propositional logic
Inductive learning from
examples and past
knowledge supports
common-sense reasoning
Logic programming aspect
aids in handling abstract
knowledge that is
logically hard to encode
NSL [38] 2002 Integrates neural and
symbolic systems via a
context-free language
embedded in neural
networks
Employs weighted-sum
nonlinear thresholded
elements for symbolic
representation
Facilitates common-sense
reasoning through
inductive learning and
formal language
structure
Addresses abstract
knowledge using BNF
formalism within a
neural framework
CTLK [39, 40] 2003 Demonstrates artiﬁcial
neural networks’
capability to interpret
and apply non-classical
logics, including
propositional temporal
logic, showcasing an
advanced integration
method
Neural networks are
employed to solve
problems like the
muddy-children puzzle,
indicating a method for
embedding and
extracting complex
logical structures
The ability to reason about
new information suggests
a pathway for learning
and applying common-
sense knowledge within
neural frameworks
Addresses the challenge of
encoding and processing
abstract knowledge
through the application
of temporal-epistemic
reasoning within neural
networks
SATyrus [41] 2005 SATyrus showcases a
neuro-symbolic approach
for constraint processing
by translating problems
into energy functions,
indicating a novel
integration method
The architecture employs
energy functions to
represent symbolic
constraints within neural
networks, facilitating
their extraction through
global minima solutions
The model’s ability to
solve complex problems
like the traveling
salesman problem hints
at its capacity for
common-sense reasoning
and problem-solving
Its approach to expressing
problems as energy
functions offers a unique
way to handle abstract
knowledge that is
typically challenging to
encode logically
NSBL [42] 2005 Neuro-symbolic language
for robotics behavior
modeling
Action-selection and
inference mechanisms
for symbolic
representation
Adaptive behavior for
common-sense reasoning
in robotics
Modeling complex
behaviors and navigation
in robotics
Sathasivam et al.
[44–46]
2010 Introduces the Pseudo
inverse learning rule for
enhancing Hopﬁeld
neural network logic
programming
Demonstrates an effective
method for representing
logical functions within
neural networks
Enhances the network’s
capability for inductive
learning, relevant for
common-sense reasoning
Compares with Hebb Rule
and Direct learning rule,
showcasing efﬁciency in
handling complex logical
constructs
Velik et al. [ 47] 2010 Introduces a neuro-
symbolic network
bridging neurological
and symbolic levels,
offering a uniﬁed
approach to integration
Proposes neuro-symbolic
coding to represent and
process multimodal
sensory information,
facilitating the extraction
of symbolic structures
from neural data
Explores perceptual
learning processes,
suggesting a framework
for common-sense
knowledge acquisition
and reasoning based on
sensory inputs
Addresses the binding
problem in perception,
providing insights into
handling abstract
knowledge through
neuro-symbolic
interactions
12820 Neural Computing and Applications (2024) 36:12809–12844
123

Table 6 (continued)
Authors/Work
(Ref)
Year Question A: Best way to
integrate
Question B:
Representation and
extraction of symbolic
structures
Question C: Learning and
reasoning about common-
sense knowledge
Question D: Handling
abstract knowledge
Komendantskaya
et al. [ 48]
2010 Introduced neural
networks capable of
performing induction,
presenting a novel
approach to neuro-
symbolic computation
Utilized symbol
recognizers and recurrent
connections for
embedding and
processing symbolic
structures
Explored recursive
computing for enhancing
common-sense reasoning
in neural networks
Demonstrated the neural
network’s ability to
handle complex
dependencies,
contributing to the
management of abstract
knowledge
Neurule [49] 2011 Employs neurules derived
from training examples
or symbolic rule bases,
showcasing a method for
dynamic integration
Neurules enable efﬁcient
updates and interactive
inference, illustrating
advanced symbolic
structure handling within
neural frameworks
Enhances reasoning with
case-based integration,
indicating an approach
for incorporating
common-sense
knowledge
Facilitates adaptive
reasoning with diverse
knowledge sources,
addressing the challenge
of managing abstract
knowledge
SCTL [55] 2011 Utilizes sequences and
counter-examples to
integrate temporal logic
rules into neural
networks, offering a
novel approach to neuro-
symbolic integration
Employs a nonlinear
recurrent network model
to represent and extract
temporal logic structures,
enhancing symbolic
representation within
neural frameworks
The learning from
sequences and system
properties facilitates
reasoning about
common-sense
knowledge, particularly
in temporal domains
The adaptation of temporal
logic rules and model
checking into the neural
network aids in
managing abstract
knowledge related to
time and system
behaviors
NTN [56] 2013 Introduces a method for
entity vectors to interact
through tensors,
enhancing the integration
of knowledge bases with
neural networks
Employs tensors for rich
representation and
interaction of entity
vectors, enabling the
extraction of complex
relational information
Utilizes knowledge base
reasoning for predicting
new entity relationships,
indicating a capability
for common-sense
knowledge inference
Demonstrates high
accuracy in classifying
unseen relationships,
showcasing the model’s
ability to manage
abstract knowledge
Riveret et al. [ 57] 2015 Integrates probabilistic
abstract argumentation
with Boltzmann
machines, offering a
unique approach to
neuro-symbolic
reasoning
Enables alternative
labeling within neural
networks, facilitating the
representation and
extraction of
argumentative structures
The probabilistic setup
suggests a method for
common-sense reasoning
through argumentation
Demonstrates the handling
of complex argument
structures, contributing
to the abstraction of
knowledge within neural
networks
MicroPsi [58] 2015 Explores neuro-symbolic
cognitive architecture
with a focus on
autonomous motivation,
bridging cognitive
processes with symbolic
reasoning
Models complex human-
like behaviors and
emotions, providing a
framework for
representing and
extracting symbolic
structures related to
affective states
Utilizes polycyclic
motivation and social
demands to simulate
common-sense reasoning
and social interactions
Applies parameters and
modulators to capture
individual variance and
personality traits,
offering insights into
abstract knowledge
representation
Conﬁdence Rules
[63]
2016 Introduces a novel method
for embedding
quantitative ideas in
neural networks using
conﬁdence criteria
Enhances the
representation of deep
networks through
conﬁdence-based
layerwise extraction
Demonstrates the
incorporation of
historical data into
training, suggesting a
potential for abstract
knowledge handling
Hu et al. [ 64] 2016 Provides a framework for
enhancing neural
networks with ﬁrst-order
logic, offering a novel
integration approach
Utilizes iterative
distillation to embed
logic rules into network
weights, improving
symbolic structure
representation
The technique’s ability to
infuse structured logical
information into neural
networks suggests a
potential for handling
abstract knowledge
Neural Computing and Applications (2024) 36:12809–12844 12821
123

Table 6 (continued)
Authors/Work
(Ref)
Year Question A: Best way to
integrate
Question B:
Representation and
extraction of symbolic
structures
Question C: Learning and
reasoning about common-
sense knowledge
Question D: Handling
abstract knowledge
NTP [65] 2016 Utilizes differentiable
backward chaining to
integrate logical
reasoning within neural
networks
Enables the representation
and learning of complex
logical structures through
replacement
representations
The application of domain
knowledge and canonical
rules suggests a method
for common-sense
reasoning
Facilitates the handling of
abstract knowledge by
learning logical linkages
from minimal data
LTN [66] 2016 Presents LTN as a
framework combining
neural networks with
ﬁrst-order logic for
querying, learning, and
reasoning
Utilizes Real Logic, a
differentiable logical
language, for
representing and
processing data and
knowledge within neural
networks
The framework’s ability to
handle rich data and
abstract world
knowledge suggests
potential for common-
sense reasoning
applications
LTN’s integration of ﬁrst-
order logic and neural
computation offers a
novel approach to
managing abstract
knowledge in AI tasks
Tensor networks
[62]
2016 Introduces a Neuro-
Symbolic Program
Synthesis method,
enabling autonomous
code generation for
replicating input–output
pairs
Features two novel neural
modules: a cross-
correlation I/O network
and R3NN for program
synthesis
Demonstrates program
synthesis capability,
potentially applicable in
learning common-sense
reasoning patterns
Leverages context-free
grammar rules for
constructing parse trees,
highlighting a novel
approach to abstract
knowledge
representation
Wang et al. [ 69] 2017 Introduces DGCC,
blending human
cognition methods with
machine learning for
cognitive computing
Employs a multi-
granularity approach to
represent and process
information, enhancing
symbolic representation
in neural networks
Proposes ‘ ‘hierarchical
structuralism’’ as a new
paradigm, potentially
advancing the handling
of abstract and complex
knowledge
Tran et al. [ 70] 2017 Proposes a method to
represent propositional
formulas in Restricted
Boltzmann Machines
(RBMs), simplifying
logical implications and
Horn clauses
representation
Enhances RBMs to handle
symbolic structures
through a new
representation approach
Offers a less complex
framework for
integrating symbolic
knowledge, suggesting
potential in handling
abstract knowledge
TPRN [72] 2018 Introduces TPRN for
interpretable question
answering using
grammatical concepts
without prior linguistic
knowledge
Embeds discrete symbol
structures within neural
networks to represent
and process linguistic
information
Demonstrates learning of
syntax/semantics through
task performance,
aligning with natural
language acquisition
theories
Enables deep learning
systems to create
representations encoding
abstract grammatical
concepts, bridging the
gap between continuous
numerical operations and
discrete conceptual
categories
dILP [73] 2018 Introduces dILP
framework for robust
logic programming
against noisy data,
extending beyond
traditional ILP
capabilities
Embeds logical structures
within neural networks to
enhance interpretability
and reasoning
capabilities
Facilitates learning from
ambiguous data,
suggesting an approach
for common-sense
knowledge acquisition
Supports data efﬁciency
and generalization,
addressing the challenge
of encoding abstract
knowledge that is hard to
encode logically
DeepProbLog
[75]
2018 Proposes DeepProbLog,
integrating neural
networks with
probabilistic logic
programming for
enhanced reasoning
Combines symbolic and
sub-symbolic
representations, enabling
complex logical
reasoning within neural
architectures
Aids in learning and
reasoning with
probabilistic models,
contributing to the
understanding of
common-sense
knowledge
Showcases the integration
of logical reasoning and
probabilistic modeling,
offering new
perspectives on handling
abstract knowledge
12822 Neural Computing and Applications (2024) 36:12809–12844
123

Table 6 (continued)
Authors/Work
(Ref)
Year Question A: Best way to
integrate
Question B:
Representation and
extraction of symbolic
structures
Question C: Learning and
reasoning about common-
sense knowledge
Question D: Handling
abstract knowledge
NLM [78] 2019 Introduces NLM for
inductive reasoning and
learning, employing
logic programming
alongside neural
networks
Processes objects,
attributes, and relations
using logic programming
within neural
frameworks
Demonstrates scalability
from small-scale tasks to
larger applications,
indicating potential for
common-sense
knowledge learning
Illustrates how neural
networks can
approximate complex
functions, enhancing the
handling of abstract
knowledge
SGM [79] 2019 Combines deep generative
models with neuro-
symbolic programs,
introducing a
programmatic framework
for structure expression
Enhances generative
models by incorporating
global structural
expressions
Offers a new perspective
on integrating
programmatic
frameworks with neural
models, potentially
advancing abstract
knowledge
representation
KENN [80] 2019 Develops KENN, adding
logical constraints to
neural network
predictions through a
Knowledge Enhancer
layer
Integrates logical
restrictions within neural
networks to reﬁne
predictions
Facilitates the
incorporation of
learnable logical
constraints, contributing
to the discussion on
abstract knowledge
encoding
COMET [81] 2019 Adapts language models to
generate new common-
sense knowledge,
validated against
ATOMIC and
ConceptNet databases
Enhances language models
with common-sense
reasoning capabilities
Demonstrates the
generation of accurate
common-sense
knowledge
Addresses the integration
of dynamic, contextually
relevant common-sense
knowledge into language
models
PLANS [83] 2020 Applies hybrid systems to
decode decision-making
logic from visual
narratives, introducing
adaptive ﬁltering for
neurally inferred
speciﬁcations
Integrates neural and rule-
based reasoning for
decision-making logic
analysis
Reduces human oversight
in understanding
decision-making
processes in complex
scenarios
Innovates in combining
neural and symbolic
components efﬁciently
for decision-making
analysis
r-FOL [84] 2020 Evaluates VQA models’
reasoning using a
differentiable ﬁrst-order
logic framework,
independent of
perception
Incorporates ﬁrst-order
logic for interpretability
in reasoning processes
Facilitates the separation
of reasoning from
perception in VQA
models, enhancing
interpretability and
analytical capabilities
MWS [85] 2020 Explores neuro-symbolic
generative models using
neural networks for both
inference and symbolic
data generation,
capturing compositional
structures
Introduces the MWS
algorithm to enhance
program induction within
learning processes
Utilizes MWS to learn
models in complex
domains, suggesting an
approach for acquiring
common-sense
knowledge
Focuses on explainability
and compositional
structure in generative
modeling, contributing to
abstract knowledge
representation
LNN [86] 2020 Presents LNNs that
evaluate logical
equations, integrating
predicate logic within
neural frameworks
Enables neural networks to
process logical
predicates and equations,
enhancing symbolic
representation
Could facilitate logical
reasoning and common-
sense knowledge
application through
neural computation
Advances the ﬁeld by
embedding weighted
logical systems within
neural networks,
addressing abstract
reasoning challenges
Neural Computing and Applications (2024) 36:12809–12844 12823
123

Table 6 (continued)
Authors/Work
(Ref)
Year Question A: Best way to
integrate
Question B:
Representation and
extraction of symbolic
structures
Question C: Learning and
reasoning about common-
sense knowledge
Question D: Handling
abstract knowledge
DLM [88] 2021 Proposes DLM for tackling
ILP and RL problems
using a neural-logic
architecture
Utilizes predicates as
weights, enabling a
continuous
representation of ﬁrst-
order logic programs
within neural networks
Demonstrates the
application in solving
complex problems,
implying potential for
common-sense reasoning
Introduces a novel method
for encoding and
processing abstract
logical knowledge
through gradient descent,
enhancing the neuro-
symbolic AI domain
CORGI [89] 2021 Introduces a
conversational approach
for common-sense
reasoning using a neuro-
symbolic theorem prover
Engages in dialogue using
a common-sense
knowledge base,
enhancing user
interaction with AI
Demonstrates the
evocation of common-
sense knowledge through
human speech,
suggesting advancements
in natural language
understanding
Highlights the practical
application of neuro-
symbolic models in
conversational AI,
contributing to the ﬁeld
of common-sense
reasoning
NSFR [90] 2021 Proposes a novel reasoning
method using
differentiable forward-
chaining based on ﬁrst-
order logic
Transforms raw inputs into
probabilistic ground
atoms for reasoning,
advancing symbolic
representation in neural
networks
Facilitates seamless
deduction of new facts
from existing knowledge,
aligning with common-
sense reasoning
paradigms
Enhances the
interpretability and
ﬂexibility of neuro-
symbolic reasoning,
pushing the boundaries
of abstract knowledge
handling
autoBOT [91] 2021 Explores autonomous
development of text
representations for
explainable and efﬁcient
AI models
Evolves representations
rather than learning
them, offering a novel
approach to handling
symbolic structures
Contributes to the
advancement of low-
resource, explainable AI
models, potentially
impacting the
representation of abstract
knowledge
DeepLogic [92] 2022 Integrates neural
perception and logical
reasoning in a uniﬁed
learning process
Utilizes a tree structure and
logic operators for
sophisticated logical
formulations within
neural networks
Optimizes mutual
supervision signals for
simultaneous learning of
perception and reasoning
Describes ﬁrst-order
logical formulations,
enhancing abstract
knowledge handling
HRI [93] 2022 Solves ILP issues with a
hierarchical rule
induction approach,
efﬁciently integrating
neural and symbolic
methods
Matches meta-rule facts
with body predicates
through learned
embeddings,
representing symbolic
structures
Uses a set of generic meta-
rules for common-sense
knowledge reasoning
Employs controlled noise
and interpretability-
regularization for
abstract knowledge
SenticNet 7 [ 94] 2022 Utilizes auto-regressive
models and kernel
methods for generating
symbolic representations
from text
Transforms real language
into a proto-language for
symbolic processing
Enhances sentiment
analysis with
unsupervised, repeatable,
and interpretable models
Provides a trustworthy and
explainable framework
for abstract knowledge
representation
ASL [95] 2023 Combines deep learning
with abductive logical
reasoning for subconcept
learning and reasoning
Induces logical hypotheses
for subconcept
representation and
detection in neural
networks
Applies meta-interpretive
learning for common-
sense knowledge
acquisition and reasoning
Reduces inconsistency in
model outputs,
advancing abstract
knowledge handling
through integrated
learning
12824 Neural Computing and Applications (2024) 36:12809–12844
123

components is a hallmark of this integrated model type
(Fig. 9). System types 2 include models, which use a
symbolic stack machine to support recursion and sequence
manipulation and a neural network to generate the execu-
tion trace. A notable instance of this hybrid approach is
AlphaGo [208], which integrates Monte Carlo Tree Search
(MCTS) [ 209] for problem-solving and a neural network
for heuristic evaluations, thereby showcasing the potential
of combining strategic decision-making processes with
neural network-based insights. It’s crucial to clarify that
while AlphaGo exempliﬁes the innovative use of neural
networks within a decision-making framework, its conﬁg-
uration primarily enhances decision strategies and may not
fully encapsulate the traditional neural-symbolic integra-
tion aimed at combining deep semantic reasoning with
neural computation. Another case in point is a rule-based
system that leverages abstract notions recorded by a neural
perception module as I/O requirements and is introduced
for program synthesis from raw visual observations. The
usefulness of combining the skills of symbolic thinking
with brain processing for complicated problem-solving
tasks is brought to light by type 2 systems. Table 8 shows
the properties of some contributions.
2.3.3 Type 3: neuro | symbolic
Type 3 neuro-symbolic AI systems combine neural and
symbolic components to improve both aspects’ perfor-
mance. In this setup, the relationship between the neuro-
logical and symbolic layers is more cooperative than
strictly functional (Fig. 10). Some program synthesis
algorithms, for instance, make use of deep learning to
produce symbolic programs and rule systems that fulﬁll
high-level task speciﬁcations; the interaction between the
neural and symbolic components aids in the model’s per-
formance. To improve decision-making, symbolic planning
is also included in RL in neural-symbolic RL. Similarly,
NLProlog [188] and DeepProbLog [ 75–77] employ neural
networks to calculate the probabilities of probabilistic facts
and the inference mechanism of ProbLog to compute the
required loss gradient, all of which are instances of type 3
systems. In general, type 3 neuro-symbolic AI systems
combine the beneﬁts of neural and symbolic techniques to
solve difﬁcult problems, as shown in Table 9.
2.3.4 Type 4: neuro-symbolic /C0! neuro
Systems of this fourth kind of integration include symbolic
rules and information into the design or training of neural
networks (Fig. 11). With the goal of seamlessly integrating
symbolic domain information into connectionist architec-
tures, this method has lately acquired traction. They also
include tightly coupled but localist neuro-symbolic systems
[237–242]. To teach a system in mathematics, for instance,
one may use tree representations of equations and mean-
ingful mathematical expressions [243]. Symbolic programs
are produced and run by the neural network as completely
differentiable operations in Visual Question Answering
models [ 84]. Graph neural networks (GNNs) [ 244] are
being used more recently to include external knowledge
bases with entities and relationships. Though some critics
claim GNNs’ reasoning power is lacking, Kautz classiﬁes
such approaches as Type 4. Table 10 shows the properties
of some contributions.
2.3.5 Type 5: neuro
Symbolic
In order to train a neural network, type 5 neuro-symbolic
AI systems include symbolic information as soft restric-
tions into the loss function (tensors) (Fig. 12). The neural
network is given the ability to reason with the information
thanks to the incorporation of symbolic knowledge into the
network weights. Logic tensor networks (LTNs)
[62, 66–68] are an example of this method; they use fuzzy
relations on real numbers to represent ﬁrst-order logic
equations in neural computing, enabling gradient-based
sub-symbolic learning. To cope with approximate rather
than accurate reasoning, LTNs soften Boolean ﬁrst-order
logic as soft fuzzy logic. End-to-end training of networks
using symbolic knowledge is made possible by LTNs by
including logic rules in the network learning aim. When
designing classiﬁers, class hierarchies are used as both the
classiﬁcation targets and the background knowledge. The
Fig. 8 Neuro-symbolic AI process ﬂow in type 1 systems. Symbols
are translated into vector representations, processed through neural
networks to capture intricate patterns, and then converted back into
symbolic outputs, integrating the adaptability of neural embeddings
with the precision of symbolic logic
Neural Computing and Applications (2024) 36:12809–12844 12825
123

purpose of objective functions in training is to encourage
consistency between predictions and the existing class
structure. Additional training targets for hierarchical scene
parsing are compositional relations over semantic hierar-
chies. Table 11 shows the properties of some contributions.
2.3.6 Type 6: neuro[symbolic]
Most experts agree that type 6 neuro-symbolic AI has the
most promise for bringing together the best features of
traditional symbolic AI with modern neural-based AI. A
symbolic thinking engine is embedded directly into a
neural engine, making this a completely integrated system
(Fig. 13). Type 6 methods include a family of algorithms
that mimics the logic of tensor calculus to train neural
networks to carry out symbolic operations. Their capacity
for logical thinking, however, remains low. Kautz argues
that type 6 techniques should be able to do combinatorial
reasoning since they are computer models of Kahneman’s
System 1 and System 2, although such a fully ﬂedged
system does not exist yet. According to Kautz, no current
proper integration method comes close to matching the
quality of a Type 6 system. Nevertheless, Type 6 systems
could signiﬁcantly advance AI by bringing together sym-
bolic reasoning and neural networks. Table 12 shows the
properties of some contributions claiming to be in type 6.
3 Applications
The rapid advancement of neuro-symbolic integration in
recent years has paved the way for the emergence of a
plethora of new applications. Here, we showcase several
widely used applications in an effort to spark future inno-
vation across a wider range of use cases.
3.1 Neuro-symbolic AI in robotics
Neuro-symbolic AI is signiﬁcantly advancing robotics by
enabling robots to perform complex tasks previously
deemed unattainable, leveraging the fusion of neural net-
work adaptability with the structured logic of symbolic AI.
This synergy enhances robots’ capabilities to perceive,
reason, and act in intricate and unpredictable environments.
Notable implementations include robots learning new skills
from human demonstrations, translating these into sym-
bolic plans, and reasoning about objects’ physical proper-
ties and their environmental interactions.
Table 7 Collection of papers with neuro-symbolic type 1 and their properties
Paper Year Domain Properties
Rep. Learn. Reason. Dec. Mak. Logic Neural Typ.
Burattini et al. [ 201] 2001 Expert Sys. Loc. /C2 Comm. /C2/C2 /C2
Hitzler et al. [ 202] 2003 Logic Prog. Dist. Ded. /C2/C2 /C2 FF NN
Coraggio et al. [ 203] 2008 Robotics Dist. Ded. /C2/C2 /C2 FF NN
Staffa et al. [ 204] 2011 Robotics Dist. Diff. Evol. [ 205] /C2/C2 /C2 FF NN
Hasoon et al. [ 206] 2013 Op. Sys. Dist. Ded. /C2 Rule B. /C2 ANN
word2vec [199] 2013 QA Dist. Grad. Desc. /C2/C2 /C2 RNN
Glove [200] 2014 QA Dist. Grad. Desc. /C2/C2 /C2 RNN
Golovko et al. [ 207] 2020 Comp. Vis. Dist. Ded. /C2 Rule B. /C2 ANN
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Logic Logic Type, Neural Typ. Neural Type, Ded.
Deductive, Dist. Distributed, Loc. Localist, FF NN Feed Forward Neural Network, ANN Artiﬁcial Neural Network, RNN Recurrent Neural
Network, Comm. Common-sense, Rule B. Rule Based, Grad. Desc. Gradient Descent
Fig. 9 Integration framework of type 2 neuro-symbolic AI. The
diagram illustrates a neural network acting as an intermediary
between input/output ﬂows and a symbolic AI system. The neural
components provide insight-driven inputs to the symbolic problem
solver, characterizing the loosely coupled but predominantly sym-
bolic nature of these systems
12826 Neural Computing and Applications (2024) 36:12809–12844
123

Coraggio et al. [ 203] devised a neuro-symbolic system
for robot self-localization in minimally sensor-equipped
environments, utilizing natural environmental features as
landmarks for navigation. This approach blends neural
networks’ perceptual strengths with symbolic AI’s logical
reasoning, enabling sophisticated decision-making pro-
cesses based on landmark detection and encoding.
Staffa et al. [ 204] explored robotic control by tuning
thresholds within a neuro-symbolic network, demonstrating
enhanced adaptability and decision-making in behavior-
based robotics. The dynamic adjustment of behavior in
response to environmental changes showcases the potential
of neuro-symbolic approaches in improving robotic
autonomy and efﬁciency.
Coraggio and De Gregorio [ 229] developed a neuro-
symbolic hybrid method for landmark recognition and
robot localization, improving landmark detection robust-
ness and robot navigation accuracy in complex settings.
This method exempliﬁes the signiﬁcant contributions of
neuro-symbolic integration to the ﬁeld of robotics, partic-
ularly in spatial awareness and adaptability applications.
An innovative approach to active video surveillance was
presented in [ 230], integrating virtual neural sensors with
BDI agents for enhanced system intelligence and reactivity.
This integration yields a highly adaptive surveillance sys-
tem capable of autonomous operation in dynamic envi-
ronments, highlighting the beneﬁts of combining neural
networks’ perceptual abilities with symbolic AI’s reason-
ing capabilities.
Kraetzschmar et al. [ 226] utilized neuro-symbolic inte-
gration for environmental modeling in mobile robotics,
enabling dynamic and efﬁcient environment representation
crucial for navigation and interaction. This approach
underscores the importance of combining neural
Table 8 Collection of papers with neuro-symbolic type 2 and their properties
Paper Year Domain Properties Neural Typ.
Rep. Learn. Reason. Dec. Mak. Logic
Neuro-Data-Mine [210] 2000 Medical applications Dist. Unsup. /C2/C2 /C2 /C2
Corchado et al. [ 211] 2001 Oceanography Dist. Sup. Case-B. /C2 Prop. Belief network
Riverola et al. [ 212] 2002 Oceanography Dist. Sup. Case-B. /C2 Prop. RBF ANN
Neagu et al. [ 213] 2002 Air Quality Dist. Sup. /C2/C2 /C2 Basic ANN
Corchado et al. [ 214] 2003 Oceanography Dist. Sup. Case-B. /C2/C2 Basic ANN
Fsfrt [215] 2003 Oceanography Dist. Sup. Case-B. /C2 Prop. RBF ANN
Policastro et al. [ 216] 2003 Mechanics Dist. Sup. Case-B. /C2 Prop. MLP
Fernandez et al. [ 217] 2004 Biology Dist. Unsup. Case-B. /C2 Fuzzy /C2
Corchado et al. [ 218] 2005 Business Dist. Sup. Case-B. /C2/C2 Basic ANN
Prentzas et al. [ 50, 219] 2008 UCI [ 220] Dist. Sup. Case-B. /C2/C2 Basic ANN
Borrajo et al. [ 221] 2008 Business Loc. Sup. Case-B. Rule B. Prop. /C2
Hatzilygeroudis et al. [ 222, 223] 2011 Business Loc. Sup. Case-B. Rule B. Prop. /C2
Bach et al. [ 224] 2015 Minecraft Dist. Sup. /C2 Rule B. Prop. /C2
Bologna et al. [ 225] 2017 Computer Vision Dist. Sup. /C2 Rule B. Prop. Deep MLP
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Logic Logic Type, Neural Typ. Neural Type, Sup.
Supervised, Unsup. Unsupervised, Case-B. Case-Based, Rule B. Rule Based, Prop. Propositional, Basic ANN Basic Artiﬁcial Neural Network,
RBF ANN Radial Basis Function Artiﬁcial Neural Network, MLP Multilayer Perceptron, Deep MLP Deep Multilayer Perceptron
Fig. 10 Dynamic interplay in type 3 neuro-symbolic AI systems. The
illustration depicts a cyclical interaction where a neural network and a
symbolic AI system operate in a feedback loop, allowing for both
procedural learning and logical inference. This structure supports
complex tasks like program synthesis, as seen in systems that interpret
visual data through neural perception and apply symbolic reasoning
for output generation
Neural Computing and Applications (2024) 36:12809–12844 12827
123

adaptability with symbolic reasoning in enhancing robots’
real-world operational effectiveness.
The research [ 131] conducted by Google Inc., Byte-
Dance Inc., and Tsinghua University on the neuro-sym-
bolic Neural Logic Machine (NLM) [ 78] has demonstrated
state-of-the-art methods for solving general application
tasks like array sorting, critical path ﬁnding, and more
intricate tasks such as Blocks World. This approach allows
for the application of generalized rules to achieve target
results from randomized layouts, showcasing the potential
of NeSy in enhancing robotic capabilities.
Moreover, the Neuro-Symbolic Concept Learner (NS-
CL) model, designed for the CLEVR dataset [ 179],
represents a signiﬁcant advancement in the ﬁeld. It adopts a
quasi-symbolic approach, utilizing neural networks for
inference and symbolic data for generating logical actions.
This method provides a framework for common-sense
knowledge acquisition and reasoning based on sensory
inputs, thereby offering insights into handling abstract
knowledge through neuro-symbolic interactions.
Furthermore, the development of the Neuro-Symbolic
Dynamic Reasoning (NS-DR) model, tailored for the
CLEVRER video reasoning dataset [ 280], introduces a
neural dynamics predictor. This learned physics engine is
crucial for accounting for causal relations in dynamic
environments, making it particularly relevant for robotics
applications where understanding and predicting physical
interactions are key.
These are just a handful of the ways that neuro-symbolic
AI is revolutionizing robotics. Several key viewpoints and
limitations emerge that future researchers in the ﬁeld of
neuro-symbolic AI in robotics can address:
a. Environmental complexity and dynamic adaptation
While neuro-symbolic systems like those developed by
Coraggio et al. [ 203] and Staffa et al. [ 204] have shown
promise in navigating and making decisions based on
environmental features, the adaptability of these systems to
rapidly changing or highly complex environments remains
a challenge. Future research could focus on enhancing the
robustness and ﬂexibility of neuro-symbolic systems to
better cope with unpredictable changes in the environment.
b. Perception and landmark recognition The work by
Coraggio and De Gregorio [ 229] on landmark recognition
for robot localization points to the need for improved
perceptual accuracy and the ability to distinguish between
similar features in the environment. Enhancing the per-
ceptual capabilities of neuro-symbolic systems, possibly
Table 9 Collection of papers with neuro-symbolic type 3 and their properties
Paper Year Domain Properties Neural Typ.
Rep. Learn. Reason. Dec. Mak. Logic
Kraetzschmar et al.[ 226] 2000 Mobile Robotics Dist. Sup. /C2/C2 Prop. Voronoi
WiSARD [227, 228] 2003 Computer Vision Dist. Sup. /C2/C2 F.O. Basic ANN
Coraggio et al. [ 229] 2007 Robotics Dist. Sup. /C2/C2 F.O. Basic ANN
De Gregorio et al. [ 230] 2008 Robotics Dist. Sup. Ded. /C2 F.O. Basic ANN
Qadeer et al. [ 231] 2009 Home Care Loc. Sup. Ded. Ontology Prop. Basic ANN
Dietrich et al. [ 232] 2009 Robotics Loc. Sup. Ded. Ontology Prop. Basic ANN
Barbosa et al. [ 233, 234] 2017 Computer Vision Dist. Sup. /C2/C2 F.O. Basic ANN
Yi et al. [ 235] 2018 Computer Vision Dist. Sup. /C2/C2 Symbolic CNN
NLProlog [188] 2019 Question Answering Dist. ILP [ 236] /C2 Rule B. Symbolic MLP
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Neural Typ. Neural Type, Sup. Supervised, Ded.
Deductive, Prop. Propositional, F.O. First Order, ILP Inductive Logic Programming, CNN Convolutional Neural Network, MLP Multilayer
Perceptron
Fig. 11 Type 4 neuro-symbolic AI system with explicit mapping.
This ﬁgure shows a structure where a distinct mapping layer explicitly
connects the symbolic AI component with the neural network. This
setup allows for direct translation of symbolic reasoning into neural
operations and vice versa, facilitating complex tasks that require tight
integration of both symbolic and sub-symbolic processes
12828 Neural Computing and Applications (2024) 36:12809–12844
123

through more advanced neural network architectures or
more sophisticated symbolic reasoning mechanisms, could
be a valuable area of exploration.
c. Autonomy in surveillance systems The integration of
virtual neural sensors with BDI agents as explored in [ 230]
highlights the potential for autonomous operation in
surveillance systems. However, ensuring these systems can
operate with minimal human intervention while making
contextually appropriate decisions in dynamic scenarios is
an ongoing challenge. Research could delve into optimiz-
ing the balance between neural network-driven perception
and symbolic agent-driven decision-making to improve
autonomy.
d. Environmental modeling and interaction Kraet-
zschmar et al.’s [ 226] work on environmental modeling
underscores the importance of efﬁcient and dynamic
environment representation. Future efforts could focus on
developing more sophisticated models that account for a
wider range of environmental variables and enable more
complex interactions between robots and their
surroundings.
e. Generalization and application of rules The successes
of the Neural Logic Machine (NLM) [ 78] and the Neuro-
Symbolic Concept Learner (NS-CL) [ 179] in applying
generalized rules to speciﬁc tasks suggest an area for fur-
ther research in the generalization capabilities of neuro-
symbolic systems. Investigating how these systems can
learn and apply rules across a broader range of scenarios
without signiﬁcant retraining could enhance their applica-
bility in robotics.
f. Causal reasoning and physical interactions The
development of the Neuro-Symbolic Dynamic Reasoning
(NS-DR) model [280] addresses the need for understanding
causal relationships in dynamic environments, which is
crucial for robotics. Expanding on this work to include
more complex physical interactions and causal mecha-
nisms could improve the predictive and reasoning capa-
bilities of robotic systems.
Table 10 Collection of papers with neuro-symbolic type 4 and their properties
Paper Year Domain Properties Neural Typ.
Rep. Learn. Reason. Dec. Mak. Logic
NEURULES [237] 2000 Medical applications Loc. LMS /C2 Rule B. Prop. /C2
INSS [238] 2001 Monk’s Problem [ 243] Loc. Incr. /C2 Rule B. Prop. Cascade correlation
Garcez et al. [ 239] 2001 Molecular Biology Loc. Ded. /C2 Rule B. Prop. Basic NN
Prentzas et al. [ 240] 2002 Intelligent Tutoring Loc. Ded. /C2 Rule B. Prop. Basic NN
Salgado et al. [ 241] 2003 Neurobiology Loc. Ded. /C2 Rule B. Prop. Basic NN
Omlin et al. [ 245] 2003 Medical diagnosis Dist. Ind. /C2 Rule B. Prop. Basic NN
Bologna et al. [ 246] 2003 Medical diagnosis Dist. Ind. /C2 Rule B. Prop. MLP
Obot et al. [ 247] 2009 Medical diagnosis Dist. Sup. C-B. Rule B. Prop. MLP
Boulahia et al. [ 248] 2015 UCI [ 220] Dist. Sup. C-B. Rule B. Prop. Basic NN
Prentzas et al. [ 52] 2016 Life Insurance Dist. Sup. Neurule Rule B. Prop. Basic NN
Ghosh et al. [ 249] 2018 Medical applications Dist. Sup. /C2 Rule B. Prop. Basic NN
Bhatia et al. [ 250] 2018 Code Correction Dist. Sup. Constr.-based Rule B. /C2 RNN
Prentzas et al. [ 242] 2019 Medical diagnosis Loc. Ded. /C2 Rule B. Prop. Basic NN
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Logic Logic Type, Neural Typ. Neural Type, Sup.
Supervised, Unsup. Unsupervised, Case-B. Case-Based, Rule B. Rule Based, Prop. Propositional, Basic ANN Basic Artiﬁcial Neural Network,
RBF ANN Radial Basis Function Artiﬁcial Neural Network, MLP Multilayer Perceptron, RNN Recurrent Neural Network, LMS Least Mean
Square, Incr. Incremental, C-B. Case-Based, Constr.-based Constraint-based
Fig. 12 Type 5 neuro-symbolic AI with tensor-based transformation.
This visualization presents the conversion of symbolic ﬁrst-order
logic (FoL) into tensors, processed by a neural network, and then re-
converted into symbolic FoL, highlighting a system where symbolic
logic is seamlessly integrated with tensorial neural computation
Neural Computing and Applications (2024) 36:12809–12844 12829
123

Addressing these limitations and exploring these view-
points could signiﬁcantly advance the ﬁeld of neuro-sym-
bolic AI in robotics, leading to more capable, adaptable,
and intelligent robotic systems.
3.2 Neuro-symbolic AI in question answering
The ﬁeld of question answering (QA) has seen remarkable
advancements through the integration of neuro-symbolic
AI, blending the strengths of neural networks’ data pro-
cessing with symbolic AI’s logical reasoning. Notably,
models like Word2Vec and GloVe have revolutionized
word representation, enabling AI systems to understand
and process natural language queries more effectively.
Mikolov et al.’s work on efﬁcient word representations
[199] and Pennington et al.’s development of GloVe [ 200]
have set signiﬁcant milestones in semantic understanding,
essential for interpreting complex questions.
Table 11 Collection of papers with neuro-symbolic type 5 and their properties
Paper Year Domain Properties Neural Typ.
Rep. Learn. Reason. Dec. Mak. Logic
Souici et al. [ 251] 2004 Text Recognition Dist. Ded. Case-B. Rule B. Prop. Basic ANN
Perrier et al. [ 252] 2005 Autonomous vehicles Dist. Sup. Case-B. Rule B. Prop. Basic ANN
Sanchez et al. [ 253] 2008 Textiles Dist. Incr. Case-B. Rule B. - Basic ANN
Velik et al. [ 254] 2010 Computer Vision Dist. Incr. Ded. /C2 Prop. Basic ANN
SHERLOCK [255] 2011 /C2 Dist. Ind. Ded. /C2 F.O. Basic ANN
Saikia et al. [ 256] 2016 Optimization Dist. ILP Ded. /C2 F.O. DBN
k-il [257] 2019 Medical Dist. Ind. Knowledge Graph Rule B. F.O. LSTM
Khan et al. [ 258] 2020 Computer Vision Dist. Sup. Knowledge Graph Rule B. F.O. DNN
Kapanipathi et al. [ 259] 2020 Question Answering Dist. Sup. Knowledge Graph Rule B. F.O. LNN
Neurasp [260] 2020 Computer Vision Dist. Unsup. Common Sense Rule B. F.O. Basic ANN
NSSE [261] 2021 Aircraft Maintenance Dist. Sup. Knowledge Graph Rule B. F.O. LSTM
Stammer et al. [ 262] 2021 Computer Vision Dist. Unsup. Ded. Rule B. F.O. CNN
Kimura et al. [ 263] 2021 Question Answering Dist. Sup. Knowledge Graph Rule B. F.O. LNN
Evans et al. [ 264] 2021 Computer Vision Dist. Unsup. /C2 Rule B. Prop. LSTM
PIGLeT [177] 2021 Question Answering Dist. Unsup. Common Sense Rule B. Prop. LSTM
DUA [265] 2022 Optimization Dist. ILP Inductive Rule B. F.O. /C2
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Logic Logic Type, Neural Typ. Neural Type, Sup.
Supervised, Ded. Deductive, Incr. Incremental, Case-B. Case-Based, Rule B. Rule Based, Prop. Propositional, Basic ANN Basic Artiﬁcial
Neural Network, RBF ANN Radial Basis Function Artiﬁcial Neural Network, MLP Multilayer Perceptron, RNN Recurrent Neural Network, LMS
Least Mean Square, ILP Inductive Logic Programming, DBN Deep Belief Network, LSTM Long Short-Term Memory, DNN Deep Neural
Network, LNN Logical Neural Network
Fig. 13 Type 6 neuro-symbolic AI integration model. The process
begins with a neural unit that feeds into a series of logical units,
symbolizing the transition from sub-symbolic neural processing to
higher-level logical reasoning. This represents an advanced form of
integration where the neural network output is not just interpreted but
also informs and shapes logical unit operations. This illustration
conceptualizes the ideal of a fully integrated system, embedding a
symbolic reasoning engine within a neural framework. As proposed
by Kautz, it symbolizes the aspiration for a comprehensive AI model
capable of both Kahneman’s intuitive (System 1) and deliberate
(System 2) thinking processes
12830 Neural Computing and Applications (2024) 36:12809–12844
123

Further enhancing QA systems, the Neuro-Symbolic
Program Synthesis (NSPS) approach [ 62] exempliﬁes the
seamless integration of symbolic knowledge into neural
frameworks, enabling the execution of symbolic programs
for query resolution. This method stands out for its per-
formance on benchmark datasets like WikiTableQuestions
and Spider, highlighting its efﬁcacy in deriving accurate
answers from structured data.
Innovations such as the PIGLeT model by Zellers et al.
[177] introduce a novel dimension to QA by grounding
language in a 3D world, merging physical common-sense
with linguistic understanding. This dual approach, com-
bining a physical dynamics model with a language model,
allows for the prediction and verbalization of object
interactions, showcasing the model’s proﬁciency in neuro-
symbolic interaction.
Research by Weber et al. [ 188], which integrates Pro-
log’s reasoning with natural language processing, and the
comparative study by Ma et al. [ 281] on common-sense
QA, further illustrate the diversity of strategies employed
to enhance question understanding and answer generation.
These studies underscore the importance of knowledge
base compatibility and the integration techniques’ role in
model performance, advocating for a hybrid approach that
leverages both data-driven and knowledge-driven pro-
cesses for superior reasoning and explainability in AI
systems.
Through these pioneering works, the QA domain con-
tinues to evolve, with neuro-symbolic AI playing a pivotal
role in developing more nuanced, context-aware systems
capable of tackling the intricacies of human language and
cognition. This fusion has led to more sophisticated natural
language understanding and processing, essential for
interpreting and responding to complex queries. Some key
viewpoints in this domain can be:
a. Semantic understanding and word representation The
development of models like Word2Vec and GloVe by
Mikolov et al. [ 199] and Pennington et al. [ 200], respec-
tively, has been instrumental in enhancing semantic
understanding in QA systems. Future research could delve
into further improving word representation models to
capture nuanced linguistic features and contextual mean-
ings, potentially through more advanced and higher
dimensional integration of symbolic knowledge.
b. Symbolic program execution for query resolution The
Neuro-Symbolic Program Synthesis (NSPS) approach
introduced by Parisotto et al. [ 62] exempliﬁes the suc-
cessful incorporation of symbolic knowledge into neural
frameworks for query resolution. However, extending the
applicability of such models to a broader range of natural
language queries and diverse datasets remains a challenge,
inviting further exploration into adaptable and scalable
neuro-symbolic integration techniques.
c. Grounding language in physical reality The PIGLeT
model by Zellers et al. [ 177] merges physical common-
sense with linguistic understanding, a novel approach in
QA. Expanding on this, future work could focus on
enhancing the integration of physical dynamics models
with language models to improve the prediction and ver-
balization of complex object interactions, moving toward
more holistic neuro-symbolic systems that can reason
about both the physical and linguistic aspects of queries.
d. Knowledge base compatibility and reasoning Studies
such as those by Weber et al. [ 188] highlight the impor-
tance of integrating reasoning capabilities, like those in
Prolog, with natural language processing for QA.
Enhancing knowledge base compatibility and the tech-
niques for integrating symbolic reasoning into neural
models could lead to more accurate and explainable QA
systems. Research could explore advanced methods for
seamlessly merging data-driven insights with structured
knowledge bases to improve reasoning and context-
awareness in responses.
Table 12 Collection of papers with neuro-symbolic type 6 and their properties
Paper Year Domain Properties Neural Typ.
Rep. Learn. Reason. Dec. Mak. Logic
Alshahrani et al. [ 266] 2017 Biology Dist. Unsup. K. Graph Rule B. F.O. G. Embed. [ 267]
Agibetov et al. [ 268] 2018 Biology Dist. Unsup. K. Graph Rule B. F.O. G. Embed. [ 269]
Bianchi et al. [ 270] 2019 DBpedia Dist. Unsup. K. Graph Rule B. F.O. G. Embed. [ 271]
Oltramari et al. [ 272] 2019 Question Answering [ 273] Dist. Unsup. K. Graph Rule B. F.O. G. Embed. [ 274]
Doldy et al. [ 275] 2021 Edge Computing Dist. Unsup. K. Graph Rule B. F.O. G. Embed. [ 276]
Sun et al. [ 277] 2021 Table Understanding Dist. Unsup. PSL [ 278] Rule B. F.O. G. Embed. [ 279]
Rep. Representation, Learn. Learning, Reason. Reasoning, Dec. Mak. Decision Making, Logic Logic Type, Neural Typ. Neural Type, Unsup.
Unsupervised, K. Graph Knowledge Graph, Rule B. Rule Based, F.O. First Order, G. Embed. Graph Embedding
Neural Computing and Applications (2024) 36:12809–12844 12831
123

e. Hybrid approaches for enhanced reasoning and
explainability The diversity of strategies employed in the
QA domain underscores the potential of hybrid approaches
that combine data-driven and knowledge-driven processes.
Future research could investigate new methods for lever-
aging both neural network capabilities and symbolic AI’s
structured reasoning to create QA systems with superior
reasoning, adaptability, and explainability.
Addressing these viewpoints and limitations could sig-
niﬁcantly advance the ﬁeld of QA, leading to the devel-
opment of AI systems that are not only more capable of
handling complex queries but also more intuitive and
aligned with human cognitive processes.
3.3 Neuro-symbolic AI in medical applications
The medical industry presents a promising landscape for
the integration of neuro-symbolic AI, signiﬁcantly
advancing clinical decision support systems. By blending
the analytical precision of symbolic AI with the adapt-
ability of neural networks, neuro-symbolic reasoning
(NSR) has been effectively employed for more accurate
and personalized diagnoses. Research has demonstrated
NSR’s capability in accurately identifying acute abdominal
pain, showcasing its potential in improving diagnostic
accuracy [282].
Further, neuro-symbolic integration (NSI) has been
applied to electronic health records analysis, combining
deep learning with symbolic reasoning to extract actionable
insights, potentially enhancing patient care [ 283]. The
Neuro-Data-Mine framework by Ultsch [210] is notable for
its efﬁcient transformation of sub-symbolic to symbolic
data, crucial for making high-dimensional medical data
interpretable. This approach underlines the utility of neuro-
symbolic methods in complex tasks like cerebrospinal ﬂuid
analysis, emphasizing their role in advancing precision
medicine through improved data analysis and
intelligibility.
Hybrid formalisms, such as those proposed by Hatzi-
lygeroudis and Prentzas [ 237], integrate production rules
with neural units to streamline knowledge bases, demon-
strating improved inference efﬁciency in medical contexts
like bone inﬂammation diagnosis. This approach highlights
the effectiveness of neuro-symbolic systems in managing
complex decision-making and pattern recognition tasks,
offering superior performance compared to traditional
methods.
Omlin and Snyders’ work [ 245] on inductive bias in
neural networks, tailored by prior knowledge, showcases
the potential of neuro-symbolic approaches in medical
analysis, such as breast tissue characterization from mag-
netic resonance spectroscopy. Bologna’s development of
the discretized interpretable multi-layer perceptron
(DIMLP) [ 246] furthers the transparency of neural net-
works in medical diagnostics, enabling rule extraction that
aligns with neural network responses and uncovering sig-
niﬁcant biomarkers for disease classiﬁcation.
The framework by Obot and Uzoka [ 247] represents a
comprehensive integration of case-based, rule-based, and
neural network methodologies, overcoming individual
limitations and providing a robust diagnostic tool. This
hybrid system has shown strong correlations with con-
ventional neural network results while offering additional
explanatory insights, marking a signiﬁcant step toward
explainable and reliable medical AI applications.
The application of neuro-symbolic AI in the medical
domain offers promising advancements, particularly in
enhancing clinical decision support systems by merging the
precision of symbolic AI with the adaptability of neural
networks. This integration facilitates more accurate and
personalized diagnoses, improving patient care through
more insightful analyses of complex medical data. Some
key viewpoint might be:
a. Diagnostic accuracy and personalization: The capa-
bility of neuro-symbolic reasoning (NSR) in precise med-
ical diagnosis, such as the identiﬁcation of acute abdominal
pain, illustrates its potential in reﬁning diagnostic processes
[282]. Future research could focus on expanding the range
of medical conditions NSR can accurately diagnose,
ensuring broader applicability and personalization in
patient care.
b. Interpretability of high-dimensional data The Neuro-
Data-Mine framework by Ultsch [ 210] emphasizes the
importance of transforming sub-symbolic data into a
symbolic format to make complex medical data more
interpretable. Enhancing these transformation techniques
could further improve the clarity and usability of medical
data, aiding in more nuanced data analysis and decision-
making in healthcare.
c. Efﬁciency in knowledge base management The inte-
gration of production rules with neural units, as demon-
strated by Hatzilygeroudis and Prentzas [ 237], showcases
the potential for neuro-symbolic systems to streamline
knowledge bases and improve inference efﬁciency in
medical diagnostics. Research could explore advanced
hybrid formalisms that further optimize knowledge base
management and inference processes in medical
applications.
d. Transparency in medical diagnostics The develop-
ment of models like the discretized interpretable multi-
layer perceptron (DIMLP) by Bologna [ 246] highlights the
need for transparency in neural network-based medical
diagnostics. Future efforts could aim at enhancing rule
extraction techniques to align more closely with neural
network responses, facilitating the identiﬁcation of critical
12832 Neural Computing and Applications (2024) 36:12809–12844
123

biomarkers and disease classiﬁcations with greater accu-
racy and interpretability.
e. Comprehensive diagnostic tools The comprehensive
framework by Obot and Uzoka [ 247], which combines
case-based, rule-based, and neural network methodologies,
overcomes the limitations of individual approaches and
offers a more robust diagnostic tool. Expanding this inte-
gration to incorporate the latest advancements in neural
network architectures and symbolic reasoning methods
could yield even more powerful and explainable medical
diagnostic systems.
Addressing these aspects could signiﬁcantly advance
neuro-symbolic AI’s contribution to the medical ﬁeld,
leading to the development of highly effective, transparent,
and patient-centric clinical decision support systems.
3.4 Neuro-symbolic AI in computer vision
In the evolving landscape of computer vision, neuro-sym-
bolic AI has emerged as a pivotal force, driving innova-
tions across various domains including object recognition,
scene interpretation, and image categorization. The inte-
gration of symbolic reasoning with deep learning models,
facilitated by approaches like graph neural networks
(GNNs) [ 244], has enabled the embedding of items and
relations within external knowledge bases, such as
ontologies or knowledge graphs, enhancing the interpretive
capabilities of AI systems in understanding complex visual
content.
A notable advancement in this ﬁeld is the Neuro-Sym-
bolic Concept Learner (NS-CL) framework [ 179], which
leverages GNNs to encode the relationships between visual
features and their corresponding concepts within a
knowledge graph, thereby predicting potential concepts in
new images. This framework exempliﬁes the fusion of sub-
symbolic learning with symbolic knowledge, where logical
principles are rendered into fuzzy relations using logic
tensor networks (LTNs) [ 62, 66–68], offering a robust
mechanism for interpreting visual scenes and reasoning
about abstract ideas.
The application of neuro-symbolic AI in computer
vision is vividly illustrated in the work of Golovko et al.
[207], who developed an intelligent decision support sys-
tem (IDSS) for enhancing product labeling quality control.
This system epitomizes the synergy between deep neural
networks, for image localization and recognition, and
semantic networks, for intelligent data processing,
demonstrating the efﬁcacy of neuro-symbolic approaches
in real-world manufacturing environments.
Further enriching the discourse, Bologna and Hayashi
[225] explored the transparency of deep learning systems
by characterizing symbolic rules within deep discretized
interpretable multi-layer perceptrons (DIMLPs). Their
work underscores the potential of deep learning models to
maintain a balance between accuracy and interpretability, a
crucial aspect in the application of AI in sensitive ﬁelds
such as medical diagnostics.
In the realm of multimedia and language integration,
Burattini et al. [ 227] and Grieco et al. [ 228] have con-
tributed signiﬁcantly by exploring the synergy between
verbal and visual information and the concept of generating
pattern examples from ‘‘mental’’ images, respectively.
These studies highlight the multifaceted nature of neuro-
symbolic AI in bridging the gap between cognitive rea-
soning and sensory perception, offering novel insights into
pattern recognition and generation.
The neuro-symbolic approach has also been pivotal in
spatial-temporal pattern analysis, as demonstrated by Bar-
bosa et al. [ 233, 234] in their work on GPS trajectory
classiﬁcation. Their methodology exempliﬁes the integra-
tion of neural network adaptability with symbolic AI’s
structured logic, enhancing the interpretability and com-
putational efﬁciency of trajectory analysis.
Moreover, the exploration of reasoning, vision, and
language understanding by Yi et al. [ 235] through Neural-
Symbolic Visual Question Answering (VQA) and the
advancements in multimedia event processing by Khan and
Curry [258] further underscore the breadth of neuro-sym-
bolic AI’s application in computer vision and beyond.
As the ﬁeld continues to evolve, the focus on developing
sophisticated neuro-symbolic architectures that seamlessly
combine the learning process of neural networks with the
structured knowledge representation of symbolic systems
remains paramount. The future of computer vision lies in
creating more adaptable and generalized models that not
only mimic human visual capabilities but also encapsulate
transparent and comprehensible reasoning processes,
bridging the chasm between artiﬁcial intelligence and
human cognition. Some key viewpoints in this domain can
be:
a. Enhancing interpretive capabilities The integration of
graph neural networks (GNNs) with symbolic reasoning
has facilitated the embedding of visual elements and their
relationships within external knowledge bases, improving
AI systems’ ability to understand intricate visual scenes.
Future research could focus on reﬁning these integrations
to handle more complex, abstract visual concepts and their
interrelations.
b. Predicting concepts in images The Neuro-Symbolic
Concept Learner (NS-CL) framework represents a leap in
encoding relationships between visual features and con-
cepts within knowledge graphs. Expanding this framework
to encompass a broader array of concepts and visual fea-
tures could further enhance the predictive accuracy and
applicability of neuro-symbolic systems in computer
vision.
Neural Computing and Applications (2024) 36:12809–12844 12833
123

c. Real-world application in manufacturing The intelli-
gent decision support system developed by Golovko et al.
[207] exempliﬁes the practical application of neuro-sym-
bolic AI in enhancing product labeling quality control.
Research aimed at extending such systems to other man-
ufacturing domains could revolutionize quality assurance
processes across various industries.
d. Balancing accuracy and interpretability The work by
Bologna and Hayashi [ 225] on characterizing symbolic
rules within deep learning models highlights the impor-
tance of maintaining a balance between model accuracy
and interpretability. Future efforts could explore novel
methodologies to enhance the transparency and explain-
ability of deep learning models without compromising their
performance.
e. Bridging cognitive reasoning and sensory perception
Studies by Burattini et al. [ 227] and Grieco et al. [ 228]
underline the potential of neuro-symbolic AI in integrating
verbal and visual information and generating pattern
examples from ‘‘mental’’ images. Advancing these
approaches could offer deeper insights into cognitive pro-
cesses and sensory perception, facilitating more intuitive
human-AI interactions.
f. Spatial-temporal pattern analysis The methodology
employed by Barbosa et al. [ 233, 234] for GPS trajectory
classiﬁcation demonstrates the effectiveness of combining
neural network adaptability with symbolic logic. Further
research in this area could enhance the interpretability and
efﬁciency of analyzing spatial-temporal patterns, with
broad implications for navigation, urban planning, and
environmental monitoring.
g. Integrating reasoning, vision, and language The
exploration of neuro-symbolic approaches in tasks like
Visual Question Answering (VQA) by Yi et al. [ 235] and
multimedia event processing by Khan and Curry [ 258]
showcases the vast potential of neuro-symbolic AI beyond
traditional computer vision tasks. Expanding these
methodologies to more complex, multimodal interactions
could signiﬁcantly advance AI’s cognitive capabilities.
Addressing these aspects could propel the ﬁeld of
computer vision forward, leading to the development of AI
systems that not only emulate human visual and cognitive
abilities but also offer transparent and understandable
reasoning processes, narrowing the gap between artiﬁcial
intelligence and human-like cognition.
3.5 Neuro-symbolic AI in programming
and optimization
The science of computer programming and optimization
has greatly beneﬁted from the integration of neuro-sym-
bolic AI. The objective of program synthesis is to generate
programs that fulﬁll a speciﬁed task, a challenge that
remains to be fully automated. Neuro-symbolic AI tech-
niques, which combine symbolic reasoning with neural
network models, have shown promise in overcoming this
challenge, enabling effective program synthesis for tasks
such as sorting or searching algorithms [ 62]. Moreover,
neuro-symbolic AI extends to enhancing software efﬁ-
ciency, where optimizations are discovered by blending
symbolic reasoning with insights derived from neural net-
work training on program execution patterns.
In the domain of programming and optimization, Bhatia,
Kohli, and Singh [250] introduced a groundbreaking neuro-
symbolic program corrector tailored for introductory pro-
gramming assignments. This tool harnesses both neural
networks and symbolic AI to identify and rectify errors in
student-submitted code, providing an automated and
intelligent feedback system that enhances the learning
experience for programming novices. The neuro-symbolic
approach not only detects syntactic errors but also grasps
the semantic intent behind the code, ensuring corrections
are accurate and contextually relevant.
Sen et al. [ 87] present a novel approach to inductive
logic programming (ILP) by integrating it with logical
neural networks (LNNs), offering a neuro-symbolic ILP
framework that merges ILP’s structured reasoning with the
adaptability of LNNs. This combination facilitates the
extraction and reﬁnement of logical rules from data,
marking a signiﬁcant advancement in AI, particularly in
programming and optimization.
Chaudhuri et al. [ 19] delve into neuro-symbolic pro-
gramming, highlighting the fusion of neural networks with
symbolic programming paradigms to address the limita-
tions of purely data-driven or rule-based systems. This
synthesis represents a pivotal shift toward creating more
adaptable, interpretable, and robust AI systems in the
programming and optimization domain.
Yin and Neubig [ 284] introduce a syntactic neural
model for general-purpose code generation, leveraging
structural patterns in programming languages to generate
code from natural language descriptions. This advancement
holds signiﬁcant promise for automating coding tasks and
bridging the gap between natural language processing and
software engineering.
Ritchie et al. [ 285] explore the application of neuro-
symbolic models in computer graphics, addressing the
challenges of generating, rendering, and manipulating
graphical content. This novel integration promises to rev-
olutionize computer graphics by introducing more intelli-
gent and adaptable systems.
Reddy and Balasubramanian [ 286] explore estimating
treatment effects using Neuro-Symbolic Program Synthe-
sis, offering a nuanced understanding of treatment efﬁcacy
and potentially transforming ﬁelds such as healthcare and
policy analysis.
12834 Neural Computing and Applications (2024) 36:12809–12844
123

Li, Huang, and Naik [ 287] introduce ‘‘Scallop,’’ a lan-
guage designed for neuro-symbolic programming, aiming
to bridge the gap between neural and symbolic computing
paradigms and facilitate the development of neuro-sym-
bolic applications.
Varela’s doctoral dissertation [ 288] investigates the
impact of hybrid neural networks on meta-learning objec-
tives, shedding light on the potential of hybrid networks to
enhance the efﬁciency and effectiveness of meta-learning
processes.
Mundhenk et al. [ 289] explore symbolic regression via
neural-guided genetic programming, aiming to enhance the
efﬁciency and accuracy of symbolic regression tasks by
leveraging the strengths of neural networks.
Chen et al. [ 290] embark on the symbolic discovery of
optimization algorithms, signifying a pivotal shift toward
automating the design of optimization algorithms and
potentially accelerating the advancement of AI and com-
putational sciences.
The infusion of neuro-symbolic AI into programming
and optimization heralds a promising horizon, marked by
enhanced learning tools, innovative problem-solving
methodologies, and a deeper understanding of complex
systems. While strides have been made, the journey toward
fully realizing the potential of neuro-symbolic AI contin-
ues, with future research poised to tackle the remaining
challenges of scalability, interpretability, and the seamless
integration of neural and symbolic systems. The key points
from the programming and optimization domain can be
consolidated into broader themes to capture the essence of
current achievements and future directions:
a. Advancements in program synthesis and software
optimization The progress in automating program synthe-
sis, exempliﬁed by neuro-symbolic techniques [62], and the
strides in enhancing software efﬁciency underscore the
potential of neuro-symbolic AI in transforming software
development practices. Future research could aim to extend
these methodologies to more complex and diverse pro-
gramming tasks, further automating and optimizing soft-
ware development processes.
b. Improving programming education and software
development Innovations such as the neuro-symbolic pro-
gram corrector [ 250] highlight the potential for AI to sig-
niﬁcantly impact programming education by providing
more nuanced error detection and correction. Extending
these tools to accommodate a wider range of programming
languages and complexities could revolutionize learning
experiences and software development workﬂows.
c. Expanding the scope of neuro-symbolic integration
The work in inductive logic programming [ 87], neuro-
symbolic programming paradigms [ 19], and dedicated
neuro-symbolic programming languages [ 287] demon-
strates the evolving landscape of neuro-symbolic AI.
Future efforts could focus on developing sophisticated
frameworks and languages that ease the integration of
neural and symbolic components, enhancing AI’s adapt-
ability and interpretability across various applications.
d. Cross-disciplinary applications and innovations The
exploration of neuro-symbolic AI in ﬁelds such as com-
puter graphics [ 285] and healthcare [ 286] illustrates its
versatile applicability. Research aimed at exploring and
expanding neuro-symbolic AI’s capabilities in diverse
domains could unlock new possibilities for innovative
applications, from digital media to precision medicine.
e. Automating the design of optimization algorithms The
initiative to automate the discovery of optimization algo-
rithms [290] opens up new research avenues in making AI
systems more efﬁcient and autonomous. Investigating
autonomous methods for identifying and implementing
optimizations could lead to breakthroughs in computational
efﬁciency and AI model performance.
By focusing on these consolidated themes, future
research in neuro-symbolic AI within the programming and
optimization domain can address existing challenges and
unlock new potentials, paving the way for more intelligent,
efﬁcient, and user-friendly AI systems.
4 Challenges
The subject of neuro-symbolic AI is expanding quickly,
thanks to its ability to integrate deep learning methods with
symbolic reasoning to produce more robust and versatile
AI systems. There are, however, obstacles that must be
overcome before its full potential may be tapped. The
following are some of the major obstacles facing neuro-
symbolic AI:
Integration of deep learning and symbolic reasoning A
critical challenge lies in the effective amalgamation of
neural and symbolic components, a task that requires
innovative architectural designs and learning paradigms.
The question of how to seamlessly integrate these com-
ponents without diluting their respective strengths remains
open. Works like the Neuro-Symbolic Concept Learner
(NS-CL) and Logical Tensor Networks (LTNs) offer
promising directions, yet the quest for a universally efﬁ-
cient integration strategy continues. This challenge is
compounded by the need for sophisticated representation
schemes that can encapsulate symbolic structures within
the ﬂuidity of neural architectures, ensuring that the
extracted symbolic knowledge retains its logical integrity
and is amenable to rigorous reasoning processes.
Need of a spatial-temporal explainable learning and
reasoning framework Developing frameworks that can
interpret and reason about spatial-temporal data with
transparency, as highlighted by the need for explainable
Neural Computing and Applications (2024) 36:12809–12844 12835
123

neuro-symbolic AI in applications like smart city man-
agement and environmental monitoring, is paramount.
Innovations such as CIL2P [36] and NSL [ 38] showcase
strides toward this goal, yet the quest for fully explainable
and generalizable systems persists. The integration of
graph neural networks (GNNs) with symbolic reasoning
mechanisms offers a pathway to imbue AI systems with an
enhanced understanding of spatial-temporal dynamics,
pertinent to domains such as environmental modeling and
autonomous navigation. The endeavor to reﬁne these
frameworks, extending their applicability and accuracy,
stands as a crucial frontier in neuro-symbolic AI research.
Data quality and bias The quality and representative-
ness of training data are crucial across domains. Biases
inherent in the data can lead to skewed AI models, making
the development of comprehensive and unbiased datasets,
as well as algorithms capable of identifying and correcting
for bias, a universal challenge.
Human–machine collaboration Enhancing interfaces
and methodologies to foster effective human-AI collabo-
ration is vital. While frameworks like NSBL [42] and NTN
[56] have made progress, creating systems that intuitively
integrate human insights and AI capabilities remains a
broad challenge.
Representation and handling of abstract knowledge The
ability to represent and reason about abstract knowledge, a
theme recurrent in works from neuro-symbolic cognitive
architectures like MicroPsi [ 58] to logic-enhanced models
like LTN [66], is a critical hurdle. Expanding AI’s capacity
to manage abstract concepts through novel neuro-symbolic
integrations is essential for advancing AI’s cognitive
capabilities.
Ethical considerations As neuro-symbolic AI continues
to evolve, it is imperative to address the ethical challenges
that accompany its development and application. The
integration of neural networks with symbolic reasoning
introduces complex ethical dimensions that warrant careful
consideration.
Neuro-symbolic AI systems, by leveraging the strengths
of both neural networks and symbolic AI, have the
potential to address complex problems with a high degree
of interpretability and adaptability. However, the integra-
tion of these two paradigms introduces complexities in
identifying and mitigating biases. Neural networks, known
for their capacity to learn from vast datasets, may inad-
vertently encode and amplify existing biases within the
data, leading to decisions that can perpetuate societal
inequalities. Symbolic AI, while providing a framework for
logical reasoning and interpretability, relies on the pre-
mises and rules deﬁned by humans, which can also be a
source of bias [ 291, 292].
The literature emphasizes the importance of trans-
parency, fairness, and accountability in AI systems to
address these challenges. For instance, the concept of
‘‘algorithmic auditing’’ has been proposed as a means to
scrutinize and evaluate the ethical implications of AI
algorithms, including those used in neuro-symbolic sys-
tems. This process involves a thorough examination of the
algorithms’ decision-making processes, data sources, and
outcomes to identify potential biases and ensure that the
systems operate within ethical boundaries [ 293].
Moreover, the development of interpretable models is
advocated to enhance the transparency of AI systems,
making it easier to understand how decisions are made and
on what basis. This is particularly relevant for neuro-
symbolic AI, where the rationale behind decisions should
be accessible and understandable to users, especially in
high-stakes domains such as healthcare, criminal justice,
and public policy [ 292].
Addressing the ethical challenges of bias and fairness in
neuro-symbolic AI also involves considering the broader
societal impacts of these technologies. The potential for
reinforcement of existing social inequalities through biased
decision-making underscores the need for ethical frame-
works that prioritize inclusivity, equity, and justice.
Engaging with diverse perspectives and disciplines can
provide a more comprehensive understanding of the social
implications of neuro-symbolic AI and guide the devel-
opment of more ethical and fair AI systems [ 294, 295].
Finally, the effects of neuro-symbolic AI on the labor
market are a source of worry. Ethical concerns regarding
the social effect and the necessity for retraining and edu-
cation is raised as technology develops and threatens
human jobs in speciﬁc sectors. Concerns about the morality
of developing and deploying neuro-symbolic AI must be
addressed if the technology is to be utilized for the greater
good of society. ‘‘Neuro-symbolic AI should ensure
transparency by making decision-making processes
understandable, uphold accountability through clear
delineation of responsibility for decisions, maintain fair-
ness by actively mitigating biases in data and algorithms,
protect privacy by safeguarding personal data, and adhere
to non-maleﬁcence by preventing harm and ensuring the
beneﬁts of AI applications outweigh potential risks.’’
As we navigate the future of neuro-symbolic AI, a
multidisciplinary approach that amalgamates insights from
cognitive science, computer science, and ethics is para-
mount. The exploration of novel integration strategies,
advanced representation techniques, and ethical frame-
works will be instrumental in realizing the full potential of
neuro-symbolic AI across its diverse applications. The
journey ahead, while fraught with challenges, holds the
promise of transformative breakthroughs that could
12836 Neural Computing and Applications (2024) 36:12809–12844
123

redeﬁne the paradigms of artiﬁcial intelligence in an array
of domains.
5 Conclusion
As this article has shown, neuro-symbolic AI is gaining
traction in the area of AI as it seeks to integrate the best
features of both symbolic reasoning and connectionist
learning. Throughout this study, we have covered the
representation, learning, reasoning, and decision-making
aspects of neuro-symbolic AI. Robotics, question answer-
ing, healthcare, computer vision, and programming are just
a few of the areas where neuro-symbolic AI has found
success. The limits and difﬁculties of neuro-symbolic AI,
including its scalability, explainability, and ethical impli-
cations, have also been examined. There is still a long way
to go, but neuro-symbolic AI shows promise for creating
AI systems with human-level intelligence and resemblance.
Acknowledgments This work is supported by the ‘‘ADI 2022’’ pro-
ject funded by the IDEX Paris-Saclay, ANR-11-IDEX-0003-02.
Author contributions Conceptualisation, B.P.B., A.R.C., T.P.S. and
R.T.; methodology, B.P.B., A.R.C. and R.T.; software, B.P.B., A.R.C.
and R.T.; validation, B.P.B., A.R.C., T.P.S. and R.T.; formal analysis,
B.P.B., A.R.C. and R.T.; investigation, B.P.B., A.R.C. and R.T.;
resources, B.P.B., A.R.C. and R.T.; data curation, B.P.B., A.R.C. and
R.T.; writing—original draft preparation, B.P.B.; writing—review
and editing, B.P.B., T.P.S., A.R.C. and R.T.; visualisation, B.P.B.;
supervision, A.R.C. and R.T.; project administration, B.P.B., A.R.C.,
T.P.S. and R.T.; funding acquisition, R.T. All authors have read and
agreed to the published version of the manuscript.
Funding This research received no external funding.
Availability of data and materials Data sharing is not applicable to
this article as no datasets were generated or analyzed during the
current study.
Code availability Not applicable.
Declarations
Conflict of interest The authors declare no conflict of interest
Ethics approval Not applicable.
Consent to participate Not applicable.
Consent for publication The authors consent to the publication of this
work.
References
1. Helm JM, Swiergosz AM, Haeberle HS, Karnuta JM, Schaffer
JL, Krebs VE, Spitzer AI, Ramkumar PN (2020) Machine
learning and artiﬁcial intelligence: deﬁnitions, applications, and
future directions. Curr Rev Musculoskelet Med 13:69–76
2. Hassan AM, Rajesh A, Asaad M, Nelson JA, Coert JH, Mehrara
BJ, Butler CE (2023) Artiﬁcial intelligence and machine
learning in prediction of surgical complications: current state,
applications, and implications. Am Surg 89(1):25–30
3. Novakovsky G, Dexter N, Libbrecht MW, Wasserman WW,
Mostafavi S (2023) Obtaining genetics insights from deep
learning via explainable artiﬁcial intelligence. Nat Rev Genet
24(2):125–137
4. Jebamikyous H, Li M, Suhas Y, Kashef R (2023) Leveraging
machine learning and blockchain in e-commerce and beyond:
beneﬁts, models, and application. Discov Artif Intell 3(1):3
5. Rawat W, Wang Z (2017) Deep convolutional neural networks
for image classiﬁcation: a comprehensive review. Neural
Comput 29(9):2352–2449
6. Bond-Taylor S, Leach A, Long Y, Willcocks CG (2021) Deep
generative modelling: a comparative review of vaes, gans,
normalizing ﬂows, energy-based and autoregressive models.
IEEE Trans Pattern Anal Mach Intell
7. Shakarami A, Ghobaei-Arani M, Shahidinejad A (2020) A
survey on the computation ofﬂoading approaches in mobile edge
computing: a machine learning-based perspective. Comput
Netw 182:107496
8. Li B, Qi P, Liu B, Di S, Liu J, Pei J, Yi J, Zhou B (2023)
Trustworthy ai: From principles to practices. ACM Comput
Surv 55(9):1–46
9. Augusto LM (2021) From symbols to knowledge systems: A.
Newell and Ha Simon’s contribution to symbolic ai
10. Newell A (1980) Physical symbol systems. Cogn Sci
4(2):135–183
11. Newell A (1982) The knowledge level. Artif Intell 18(1):87–127
12. Uschold M, Gruninger M (1996) Ontologies: principles, meth-
ods and applications. knowl Eng Rev 11(2):93–136
13. Reed SK, Pease A (2017) Reasoning from imperfect knowledge.
Cogn Syst Res 41:56–72
14. Youheng Z (2023) A historical review and philosophical
examination of the two paradigms in artiﬁcial intelligence
research. Eur J Artif Intell Mach Learn 2(2):24–32
15. Wermter S, Sun R An overview of hybrid neural systems.
Subseries of Lecture Notes in Computer Science Edited by JG
Carbonell and J. Siekmann, 1
16. Garcez ASd, Broda KB, Gabbay DM Neural-symbolic learning
systems foundations and applications
17. Hammer B, Hitzler P (2007) Perspectives of neural-symbolic
integration vol 77
18. Sun R, Alexandre F (2013) Connectionist-symbolic integration:
from uniﬁed to hybrid approaches
19. Chaudhuri S, Ellis K, Polozov O, Singh R, Solar-Lezama A,
Yue Y (2021) Neurosymbolic programming. Found Trends /C210
Program Lang 7(3):158–243
20. Hitzler P, Eberhart A, Ebrahimi M, Sarker MK, Zhou L (2022)
Neuro-symbolic approaches in artiﬁcial intelligence. Natl Sci
Rev 9(6):035
21. Velik R (2008) A bionic model for human-like machine
perception
22. Gallagher K (2018) Request conﬁrmation networks: a cortically
inspired approach to neuro-symbolic script execution. PhD
thesis, Harvard University
23. Martin LJ (2021) Neurosymbolic automated story generation.
PhD thesis, Georgia Institute of Technology
24. Corchado JM, Aiken J (2002) Hybrid artiﬁcial intelligence
methods in oceanographic forecast models. IEEE Trans Syst
Man Cybern Part C (Appl Rev) 32(4):307–313
25. Hatzilygeroudis I, Prentzas J (2004) Neuro-symbolic approaches
for knowledge representation in expert systems. Int J Hybrid
Intell Syst 1(3–4):111–126
Neural Computing and Applications (2024) 36:12809–12844 12837
123

26. O¨ ztu¨ rk P, Tidemann A (2014) A review of case-based reasoning
in cognition-action continuum: a step toward bridging symbolic
and non-symbolic artiﬁcial intelligence. Knowl Eng Rev
29(1):51–77
27. Besold TR, Garcez Ad, Bader S, Bowman H, Domingos P,
Hitzler P, Ku¨ hnberger K-U, Lamb LC, Lowd D, Lima PMV et al
(2017) Neural-symbolic learning and reasoning: a survey and
interpretation. arXiv preprint arXiv:1711.03902
28. Garnelo M, Shanahan M (2019) Reconciling deep learning with
symbolic artiﬁcial intelligence: representing objects and rela-
tions. Curr Opin Behav Sci 29:17–23
29. Garcez Ad, Gori M, Lamb LC, Seraﬁni L, Spranger M, Tran SN
(2019) Neural-symbolic computing: an effective methodology
for principled integration of machine learning and reasoning.
arXiv preprint arXiv:1905.06088
30. De Raedt L, Dumancˇic´ S, Manhaeve R, Marra G (2020) From
statistical relational to neuro-symbolic artiﬁcial intelligence.
arXiv preprint arXiv:2003.08316
31. Sarker MK, Zhou L, Eberhart A, Hitzler P (2021) Neuro-sym-
bolic artiﬁcial intelligence. AI Commun 34(3):197–209
32. Wang W, Yang Y (2022) Towards data-and knowledge-driven
artiﬁcial intelligence: a survey on neuro-symbolic computing.
arXiv preprint arXiv:2210.15889
33. Garcez Ad, Lamb LC (2023) Neurosymbolic ai: the 3rd wave.
Artif Intell Rev 56:1–20
34. Towell GG, Shavlik JW (1994) Knowledge-based artiﬁcial
neural networks. Artif intell 70(1–2):119–165
35. Pinkas G (1995) Reasoning, nonmonotonicity and learning in
connectionist networks that capture propositional knowledge.
Artif Intell 77(2):203–247
36. Avila Garcez AS, Zaverucha G (1999) The connectionist
inductive learning and logic programming system. Appl Intell
11:59–77
37. Franc¸a MV, Zaverucha G, Garcez AS (2014) Fast relational
learning using bottom clause propositionalization with artiﬁcial
neural networks. Mach Learn 94:81–104
38. Burattini E, De Gregorio M, Francesco A (2002) Nsl: a neuro-
symbolic language for monotonic and non-monotonic logical
inferences. In: SBRN, pp 256–261
39. Garcez A, Lamb L (2003) Reasoning about time and knowledge
in neural symbolic learning systems. In: Advances in neural
information processing systems, vol 16
40. Garcez ASd, Lamb LC (2006) A connectionist computational
model for epistemic and temporal reasoning. Neural Comput
18(7):1711–1738
41. Lima PMV, Morveli-Espinoza MM, Pereira GC, Franga F
(2005) Satyrus: a sat-based neuro-symbolic architecture for
constraint processing. In: Fifth international conference on
hybrid intelligent systems (HIS’05). IEEE, p 6
42. Burattini E, Datteri E, Tamburrini G (2005) Neuro-symbolic
programs for robots. In: Proceedings of NeSy, vol 5
43. Burattini E, De Gregorio M, Rossi S (2010) An adaptive
oscillatory neural architecture for controlling behavior based
robotic systems. Neurocomputing 73(16–18):2829–2836
44. Sathasivam S, Velavan M (2010) Neuro symbolic integration
using pseudo inverse rule. In: Annual international conference
on advance topics in artiﬁcial intelligence, Phuket, Thailand
45. Sathasivam S (2011) Learning rules comparison in neuro-sym-
bolicintegration. Int J Appl Phys Math 1(2):129
46. Sathasivam S (2012) Applying different learning rules in neuro-
symbolic integration. In: Advanced materials research, vol 433.
Trans Tech Publ, pp 716–720
47. Velik R (2010) The neuro-symbolic code of perception. J Cogn
Sci 11(2):161–180
48. Komendantskaya E, Broda K, Garcez A (2010) Using inductive
types for ensuring correctness of neuro-symbolic computations
49. Prentzas J, Hatzilygeroudis I (2011) Neurules-a type of neuro-
symbolic rules: an overview. Springer, Berlin, pp 145–165
50. Prentzas J, Hatzilygeroudis I (2011) Efﬁciently merging sym-
bolic rules into integrated rules
51. Hatzilygeroudis I, Prentzas J (2015) Symbolic-neural rule based
reasoning and explanation. Expert Syst Appl 42(9):4595–4609
52. Prentzas J, Hatzilygeroudis I (2016) Assessment of life insur-
ance applications: an approach integrating neuro-symbolic rule-
based with case-based reasoning. Expert Syst 33(2):145–160
53. Sreelekha S (2018) Neurosymbolic integration with uncertainty.
Ann Math Artif Intell 84(3–4):201–220
54. Prentzas J, Hatzilygeroudis I (2018) Using clustering algorithms
to improve the production of symbolic-neural rule bases from
empirical data. Int J Artif Intell Tools 27(02):1850002
55. Borges RV, Garcez Ad, Lamb LC (2011) Learning and repre-
senting temporal knowledge in recurrent networks. IEEE Trans
Neural Netw 22(12):2409–2421
56. Socher R, Chen D, Manning CD, Ng A (2013) Reasoning with
neural tensor networks for knowledge base completion. In:
Advances in neural information processing systems, vol 26
57. Riveret R, Pitt JV, Korkinof D, Draief M (2015) Neuro-sym-
bolic agents: Boltzmann machines and probabilistic abstract
argumentation with sub-arguments. In: AAMAS, pp 1481–1489
58. Bach J (2015) Modeling motivation in micropsi 2. In: Artiﬁcial
general intelligence: 8th international conference, AGI 2015,
AGI 2015, Berlin, Germany, July 22-25, 2015, Proceedings 8.
Springer, pp 3–13
59. Bach J (2009) Principles of synthetic intelligence psi: an
architecture of motivated cognition, vol 4
60. Varadarajan KM, Vincze M (2015) Affordance and k-tr aug-
mented alphabet based neuro-symbolic language-af-ktraans-a
human-robot interaction meta-language. In: 2015 20th interna-
tional conference on methods and models in automation and
robotics (MMAR). IEEE, pp 394–399
61. Abubakar H, Masanawa SA, Yusuf S (2020) Neuro-symbolic
integration of hopﬁeld neural network for optimal maximum
random ksatisﬁability (maxrksat) representation. J Reliab Stat
Stud 13:199–220
62. Parisotto E, Mohamed A-r, Singh R, Li L, Zhou D, Kohli P
(2016) Neuro-symbolic program synthesis. arXiv preprint arXiv:
1611.01855
63. Tran SN, Garcez ASd (2016) Deep logic networks: Inserting and
extracting knowledge from deep belief networks. IEEE Trans
Neural Netw Learn Syst 29(2):246–258
64. Hu Z, Ma X, Liu Z, Hovy E, Xing E (2016) Harnessing deep
neural networks with logic rules. arXiv preprint arXiv:1603.
06318
65. Rockta¨ schel T, Riedel S (2016) Learning knowledge base
inference with neural theorem provers. In: Proceedings of the
5th workshop on automated knowledge base construction,
pp 45–50
66. Seraﬁni L, Garcez AS (2016) Learning and reasoning with logic
tensor networks. In: AI* IA 2016 advances in artiﬁcial intelli-
gence: XVth international conference of the Italian association
for artiﬁcial intelligence, Genova, Italy, November 29–Decem-
ber 1, 2016, Proceedings XV. Springer, pp 334–348
67. Manigrasso F, Miro FD, Morra L, Lamberti F (2021) Faster-ltn:
a neuro-symbolic, end-to-end object detection architecture. In:
Artiﬁcial neural networks and machine learning–ICANN 2021:
30th international conference on artiﬁcial neural networks,
Bratislava, Slovakia, September 14–17, 2021, Proceedings, Part
II 30. Springer, pp 40–52
68. Badreddine S, Garcez Ad, Seraﬁni L, Spranger M (2022) Logic
tensor networks. Artif Intell 303:103649
69. Wang G (2017) Dgcc: data-driven granular cognitive comput-
ing. Granular Comput 2(4):343–355
12838 Neural Computing and Applications (2024) 36:12809–12844
123

70. Tran SN (2017) Propositional knowledge representation and
reasoning in restricted boltzmann machines. arXiv preprint
arXiv:1705.10899
71. Cohen WW, Yang F, Mazaitis KR (2017) Tensorlog: Deep
learning meets probabilistic dbs. arXiv preprint arXiv:1707.
05390
72. Palangi H, Smolensky P, He X, Deng L (2018) Question-an-
swering with grammatically-interpretable representations. In:
Proceedings of the AAAI conference on artiﬁcial intelligence,
vol 32
73. Evans R, Grefenstette E (2018) Learning explanatory rules from
noisy data. J Artif Intell Res 61:1–64
74. Minervini P, Bosˇnjak M, Rockta¨ schel T, Riedel S, Grefenstette
E (2020) Differentiable reasoning on large knowledge bases and
natural language. In: Proceedings of the AAAI conference on
artiﬁcial intelligence, vol 34, pp 5182–5190
75. Manhaeve R, Dumancic S, Kimmig A, Demeester T, De Raedt,
L (2018) Deepproblog: neural probabilistic logic programming.
In: Advances in neural information processing systems, vol 31
76. De Raedt L, Manhaeve R, Dumancic S, Demeester T, Kimmig
A (2019) Neuro-symbolic= neural ? logical? probabilistic. In:
NeSy’19@ IJCAI, the 14th international workshop on neural-
symbolic learning and reasoning
77. Manhaeve R, De Raedt L, Kimmig A, Dumancic S, Demeester
T (2019) Deepproblog: integrating logic and learning through
algebraic model counting. In: KR2ML Workshop@ Neurips’19,
Vancouver, Canada
78. Dong H, Mao J, Lin T, Wang C, Li L, Zhou D (2019) Neural
logic machines. arXiv preprint arXiv:1904.11694
79. Young H, Bastani O, Naik M (2019) Learning neurosymbolic
generative models via program synthesis. In: International
conference on machine learning. PMLR, pp 7144–7153
80. Daniele A, Seraﬁni L (2019) Knowledge enhanced neural net-
works. In: PRICAI 2019: trends in artiﬁcial intelligence: 16th
Paciﬁc Rim international conference on artiﬁcial intelligence,
Cuvu, Yanuca Island, Fiji, August 26–30, 2019, Proceedings,
Part I 16. Springer, pp 542–554
81. Bosselut A, Rashkin H, Sap M, Malaviya C, Celikyilmaz A,
Choi Y (2019) Comet: Commonsense transformers for auto-
matic knowledge graph construction. arXiv preprint arXiv:1906.
05317
82. Bosselut A, Le Bras R, Choi Y (2021) Dynamic neuro-symbolic
knowledge graph construction for zero-shot commonsense
question answering. In: Proceedings of the AAAI conference on
artiﬁcial intelligence, vol 35, pp 4923–4931
83. Dang-Nhu R (2020) Plans: Neuro-symbolic program learning
from videos. Adv Neural Inf Process Syst 33:22445–22455
84. Amizadeh S, Palangi H, Polozov A, Huang Y, Koishida K
(2020) Neuro-symbolic visual reasoning: Disentangling. In:
International conference on machine learning. PMLR,
pp 279–290
85. Hewitt L, Le TA, Tenenbaum J (2020) Learning to learn gen-
erative programs with memoised wake-sleep. In: Conference on
uncertainty in artiﬁcial intelligence. PMLR, pp 1278–1287
86. Riegel R, Gray A, Luus F, Khan N, Makondo N, Akhalwaya IY,
Qian H, Fagin R, Barahona F, Sharma U, et al (2020) Logical
neural networks. arXiv preprint arXiv:2006.13155
87. Sen P, Carvalho BW, Riegel R, Gray A (2022) Neuro-symbolic
inductive logic programming with logical neural networks. In:
Proceedings of the AAAI conference on artiﬁcial intelligence,
vol. 36, pp 8212–8219
88. Zimmer M, Feng X, Glanois C, Jiang Z, Zhang J, Weng P, Dong
L, Jianye H, Wulong L (2021) Differentiable logic machines.
arXiv preprint arXiv:2102.11529
89. Arabshahi F, Lee J, Gawarecki M, Mazaitis K, Azaria A,
Mitchell T (2021) Conversational neuro-symbolic commonsense
reasoning. In: Proceedings of the AAAI conference on artiﬁcial
intelligence, vol 35, pp 4902–4911
90. Shindo H, Dhami DS, Kersting K (2021) Neuro-symbolic for-
ward reasoning. arXiv preprint arXiv:2110.09383
91. Sˇkrlj B, Martinc M, Lavracˇ N, Pollak S (2021) autobot: evolving
neuro-symbolic representations for explainable low resource
text classiﬁcation. Mach Learn 110:989–1028
92. Duan X, Wang X, Zhao P, Shen G, Zhu W (2022) Deeplogic:
Joint learning of neural perception and logical reasoning. IEEE
Trans Pattern Anal Mach Intell
93. Glanois C, Jiang Z, Feng X, Weng P, Zimmer M, Li D, Liu W,
Hao J (2022) Neuro-symbolic hierarchical rule induction. In:
International conference on machine learning, PMLR,
pp 7583–7615
94. Cambria E, Liu Q, Decherchi S, Xing F, Kwok K (2022) Sen-
ticnet 7: A commonsense-based neurosymbolic ai framework for
explainable sentiment analysis. In: Proceedings of the thirteenth
language resources and evaluation conference, pp 3829–3839
95. Han Z, Cai L-W, Dai W-Z, Huang Y-X, Wei B, Wang W, Yin Y
(2023) Abductive subconcept learning. Sci China Inf Sci
66(2):1–13
96. Wermter S, Sun R (2001) The present and the future of hybrid
neural symbolic systems some reﬂections from the nips work-
shop. AI Mag 22(1):123–123
97. Kelley TD (2003) Symbolic and sub-symbolic representations in
computational models of human cognition: what can be learned
from biology? Theory Psychol 13(6):847–860
98. Rapaport WJ (2003) How to pass a turing test: Syntactic
semantics, natural-language understanding, and ﬁrst-person
cognition. The Turing test: the elusive standard of artiﬁcial
intelligence, 161–184
99. Bader S, Hitzler P, Ho ¨ lldobler S (2004) The integration of
connectionism and ﬁrst-order knowledge representation and
reasoning as a challenge for artiﬁcial intelligence. arXiv preprint
cs/0408069
100. Pugeda TGS III (2005) Artiﬁcial intelligence and ethical
reﬂections from the catholic church. Intelligence 26(4):53
101. Ray O, Garcez AS (2006) Towards the integration of abduction
and induction in artiﬁcial neural networks. In: Proceedings of
the ECAI, vol 6. Citeseer, pp 41–46
102. Rawbone P, Paor P, Ware JA, Barrett J (2006) Interactive
causation: a neurosymbolic agent. In: IC-AI. Citeseer, pp 51–55
103. Velik R, Bruckner D (2008) euro-symbolic networks: intro-
duction to a new information processing principle. In: 2008 6th
IEEE international conference on industrial informatics. IEEE,
pp 1042–1047
104. Ku¨ hnberger K-U, Gust H, Geibel P (2008) erspectives of neuro–
symbolic integration–extended abstract–. In: Dagstuhl Seminar
Proceedings. Schloss Dagstuhl-Leibniz-Zentrum fu¨ r Informatik
105. Ku¨ hnberger K-U, Geibel P, Gust H, Krumnack U, Ovchinnikova
E, Schwering A, Wandmacher T (2008) Learning from incon-
sistencies in an integrated cognitive architecture. Front Artif
Intell Appl 171:212
106. Haikonen PO (2009) The role of associative processing in
cognitive computing. Cogn Comput 1:42–49
107. Prentzas J, Hatzilygeroudis I (2009) Combinations of case-based
reasoning with other intelligent methods. Int J Hybrid Intell Syst
6(4):189–209
108. Garcez AS (2010) eurons and symbols: a manifesto. In: Dag-
stuhl Seminar Proceedings. Schloss Dagstuhl-Leibniz-Zentrum
fA˜1=4r Informatik
109. Velik R (2010) Why machines cannot feel. Mind Mach
20(1):1–18
110. Bruckner D, Velik R, Penya Y (2011) Machine perception in
automation: a call to arms. EURASIP J Embed Syst 2011:1–9
Neural Computing and Applications (2024) 36:12809–12844 12839
123

111. POli R (2012) Discovery of symbolic, neuro-symbolic and
neural networks with parallel. In: Artiﬁcial neural nets and
genetic algorithms: proceedings of the international conference
in Norwich, UK, 1997. Springer, p 419
112. Velik R (2013) Brain-like artiﬁcial intelligence for automation–
foundations, concepts and implementation examples. BRAIN
4(1–4):26–54
113. Achler T (2013) Neural networks that perform recognition using
generative error may help ﬁll the ‘ ‘neuro-symbolic gap’’. Biol
Inspired Cogn Archit 3:6–12
114. Lima PM (2017) Q-satyrus: Mapping neuro-symbolic reasoning
into an adiabatic quantum computer. In: NeSy
115. Shen S, Ramesh S, Shinde S, Roychoudhury A, Saxena P (2018)
Neuro-symbolic execution: The feasibility of an inductive
approach to symbolic execution. arXiv preprint arXiv:1807.
00575
116. Lieto A, Lebiere C, Oltramari A (2018) The knowledge level in
cognitive architectures: current limitations and possible devel-
opments. Cogn Syst Res 48:39–55
117. Wang P (2004) Toward a uniﬁed artiﬁcial intelligence. In:
AAAI Technical Report (1), p 83
118. Hammer P (2019) Adaptive neuro-symbolic network agent.
Springer, Berlin, pp 80–90
119. Sitto´n I, Alonso RS, Herna´ndez-Nieves E, Rodrı´guez-Gonzalez
S, Rivas A (2019) Neuro-symbolic hybrid systems for industry
4.0: a systematic mapping study. In: Knowledge management in
organizations: 14th international conference, KMO 2019,
Zamora, Spain, July 15–18, 2019, Proceedings 14. Springer,
pp 455–465
120. Marcus G (2020) The next decade in ai: four steps towards
robust artiﬁcial intelligence. arXiv preprint arXiv:2002.06177
121. Hameed HA (2020) Artiﬁcial intelligence: What it was, and
what it should be? Int J Adv Comput Sci Appl 11(6)
122. Belle V (2020) Symbolic logic meets machine learning: a brief
survey in inﬁnite domains. In: Scalable uncertainty manage-
ment: 14th international conference, SUM 2020, Bozen-Bol-
zano, Italy, September 23–25, 2020, Proceedings 14. Springer,
pp 3–16
123. Tiddi I (2020) Directions for explainable knowledge-enabled
systems. Knowledge Graphs for eXplainable Artiﬁcial intelli-
gence: Foundations Applications and Challenges 47:245
124. Hanson D, Imran A, Vellanki A, Kanagaraj S (2020) A neuro-
symbolic humanlike arm controller for sophia the robot. arXiv
preprint arXiv:2010.13983
125. Franklin NT, Norman KA, Ranganath C, Zacks JM, Gershman
SJ (2020) Structured event memory: a neuro-symbolic model of
event cognition. Psychol Rev 127(3):327
126. Di Maio P (2020) Neurosymbolic knowledge representation for
explainable and trustworthy ai
127. Anderson G, Verma A, Dillig I, Chaudhuri S (2020) Neu-
rosymbolic reinforcement learning with formally veriﬁed
exploration. Adv Neural Inf Process Syst 33:6172–6183
128. Gaur M, Kursuncu U, Sheth A, Wickramarachchi R, Yadav S
(2020) Knowledge-infused deep learning. In: Proceedings of the
31st ACM conference on hypertext and social media,
pp 309–310
129. Santoro A, Lampinen A, Mathewson K, Lillicrap T, Raposo D
(2021) Symbolic behaviour in artiﬁcial intelligence. arXiv pre-
print arXiv:2102.03406
130. Ebrahimi M, Eberhart A, Bianchi F, Hitzler P (2021) Towards
bridging the neuro-symbolic gap: deep deductive reasoners.
Appl Intell 51:6326–6348
131. Susskind Z, Arden B, John LK, Stockton P, John EB (2021)
Neuro-symbolic ai: An emerging class of ai workloads and their
characterization. arXiv preprint arXiv:2109.06133
132. Alonso RS (2021) Deep symbolic learning and semantics for an
explainable and ethical artiﬁcial intelligence. In: Ambient
intelligence–software and applications: 11th international sym-
posium on ambient intelligence. Springer, pp 272–278
133. Park K-W, Bu S-J, Cho S-B (2021) Evolutionary optimization of
neuro-symbolic integration for phishing url detection. In: Hybrid
artiﬁcial intelligent systems: 16th international conference,
HAIS 2021, Bilbao, Spain, September 22–24, 2021, Proceedings
16. Springer, pp 88–100
134. Oltramari A, Francis J, Ilievski F, Ma K, Mirzaee R (2021)
Generalizable neuro-symbolic systems for commonsense ques-
tion answering, 294–310
135. Calvaresi D, Ciatto G, Najjar A, Aydog ˘an R, Torre L, Omicini
A, Schumacher M (2021) Expectation: personalized explainable
artiﬁcial intelligence for decentralized agents with heteroge-
neous knowledge. In: Explainable and transparent AI and multi-
agent systems: third international workshop, EXTRAAMAS
2021, Virtual Event, May 3–7, 2021, Revised Selected Papers 3.
Springer, pp 331–343
136. Nye M, Tessler M, Tenenbaum J, Lake BM (2021) Improving
coherence and consistency in neural sequence models with dual-
system, neuro-symbolic reasoning. Adv Neural Inf Process Syst
34:25192–25204
137. Gaur M, Gunaratna K, Bhatt S, Sheth A (2022) Knowledge-
infused learning: a sweet spot in neuro-symbolic ai. IEEE
Internet Comput 26(4):5–11
138. Samsonovich AV (2022) One possibility of a neuro-symbolic
integration. In: Biologically inspired cognitive architectures
2021: proceedings of the 12th annual meeting of the BICA
Society. Springer, pp 428–437
139. Dold D, Soler Garrido J, Caceres Chian V, Hildebrandt M,
Runkler T (2022) Neuro-symbolic computing with spiking
neural networks. In: Proceedings of the international conference
on neuromorphic systems 2022, pp 1–4
140. Chitnis R, Silver T, Tenenbaum JB, Lozano-Perez T, Kaelbling
LP (2022) Learning neuro-symbolic relational transition models
for bilevel planning. In: 2022 IEEE/RSJ international confer-
ence on intelligent robots and systems (IROS). IEEE,
pp 4166–4173
141. Kocon´ J, Baran J, Gruza M, Janz A, Kajstura M, Kazienko P,
Korczyn´ski W, Miłkowski P, Piasecki M, Szołomicka J (2022)
Neuro-symbolic models for sentiment analysis. In: Computa-
tional science–ICCS 2022: 22nd international conference, Lon-
don, UK, June 21–23, 2022, Proceedings, Part II. Springer,
pp 667–681
142. Alon U, Xu F, He J, Sengupta S, Roth D, Neubig G (2022)
Neuro-symbolic language modeling with automaton-augmented
retrieval. In: International conference on machine learning.
PMLR, pp 468–485
143. Amado LR, Pereira RF, Meneguzzi FR (2023) Robust neuro-
symbolic goal and plan recognition. In: Proceedings of the 37th
AAAI conference on artiﬁcial intelligence (AAAI), 2023,
Estados Unidos
144. Hitzler P, Roth-Berghofer T, Rudolph S (2007) Foundations of
artiﬁcial intelligence faint-07 workshop at ki 2007. In: Work-
shop at KI, vol 2007. Citeseer
145. Garcez AS, Lamb LC, Gabbay DM (2008) Neural-symbolic
cognitive reasoning
146. Komendantskaya E, Broda K, Garcez ASd (2010) Neuro-sym-
bolic representation of logic programs deﬁning inﬁnite sets.
ICANN (1) 6352:301–304
147. Andreasik J, Ciebiera A, Umpirowicz S, Speretta M, Gauch S,
Lakkaraju P, Alessandrelli D, Pagano P, Nastasi C, Petracca M
et al (2010) Hsi 2010 conference programme may 13
148. Barcelona CS, Garcez Ad, Lamb L Seventh international
workshop on neural-symbolic learning and reasoning
12840 Neural Computing and Applications (2024) 36:12809–12844
123

149. Hatzilygeroudis I, Prentzas J (2011) Combinations of intelligent
methods and applications. Springer, Berlin
150. Achler T (2012) Towards bridging the gap between pattern
recognition and symbolic representation within neural networks.
In: Workshop on neural-symbolic learning and reasoning,
AAAI-2012. Citeseer
151. Garcez A, Gori M, Hitzler P, Lamb LC (2015) Neural-symbolic
learning and reasoning (dagstuhl seminar 14381). In: Dagstuhl
Reports, vol. 4. Schloss Dagstuhl-Leibniz-Zentrum fuer
Informatik
152. Hatzilygeroudis I, Palade V (2016) 6thinternational workshop
on combinations of intelligent methods and applications (cima
2016)
153. Hatzilygeroudis I, Palade V, Prentzas J (2017) Advances in
combining intelligent methods
154. Hatzilygeroudis I, Palade V (2018) Advances in hybridization of
intelligent methods
155. Hammer P, Agrawal P, Goertzel B, Ikle ´ M (2019) Artiﬁcial
general intelligence: 12th international conference, AGI 2019,
Shenzhen, China, August 6–9, 2019, Proceedings, vol 11654.
Springer
156. Shen S, Shinde S, Ramesh S, Roychoudhury A, Saxena P (2019)
Neuro-symbolic execution: Augmenting symbolic execution
with neural constraints. In: NDSS
157. Averkin A (2019) Hybrid intelligent systems based on fuzzy
logic and deep learning. Artiﬁcial Intelligence: 5th RAAI
Summer School, Dolgoprudny, Russia, July 4–7, 2019, Tutorial
Lectures, 3–12
158. Pisano G, Ciatto G, Calegari R, Omicini A (2020) Neuro-sym-
bolic computation for xai: Towards a uniﬁed model. In: WOA,
vol 1613, p 101
159. Alam M, Groth P, Hitzler P, Paulheim H, Sack H, Tresp V
(2020) Cssa’20: workshop on combining symbolic and sub-
symbolic methods and their applications. In: Proceedings of the
29th ACM international conference on information & knowl-
edge management, pp 3523–3524
160. Benzmu¨ ller C, Lomfeld B (2020) Reasonable machines: a
research manifesto. In: KI 2020: advances in artiﬁcial intelli-
gence: 43rd German conference on AI, Bamberg, Germany,
September 21–25, 2020, Proceedings 43. Springer, pp 251–258
161. Ilkou E, Koutraki M (2020) Symbolic vs sub-symbolic ai
methods: Friends or enemies? In: CIKM (Workshops)
162. Singh G, Mondal S, Bhatia S, Mutharaju R (2021) Neuro-
symbolic techniques for description logic reasoning (student
abstract). In: Proceedings of the AAAI conference on artiﬁcial
intelligence, vol 35, pp 15891–15892
163. Branco R, Branco A, Silva JM, Rodrigues J (2021) Common-
sense reasoning: how do neuro-symbolic and neuro-only
approaches compare? In: CIKM Workshops
164. Basu K, Murugesan K, Atzeni M, Kapanipathi P, Talamadupula
K, Klinger T, Campbell M, Sachan M, Gupta G (2021) A hybrid
neuro-symbolic approach for text-based games using inductive
logic programming. Combining learning and reasoning: pro-
gramming languages, formalisms, and representations
165. Garcez Ad, Jime ´nez-Ruiz E (2021) Neural-symbolic learning
and reasoning (nesy)
166. Saha A, Joty S, Hoi SC (2022) Weakly supervised neuro-sym-
bolic module networks for numerical reasoning over text. In:
Proceedings of the AAAI conference on artiﬁcial intelligence,
vol 36, pp 11238–11247
167. Ahmed K, Teso S, Chang K-W, Broeck G, Vergari A (2022)
Semantic probabilistic layers for neuro-symbolic learning. Adv
Neural Inf Process Syst 35:29944–29959
168. Bader S, Hitzler P (2005) Dimensions of neural-symbolic inte-
gration—a structured survey. arXiv preprint arXiv:cs/0511042
169. Kautz H (2022) The third ai summer: Aaai Robert S. Engelmore
memorial lecture. AI Mag 43(1):105–125
170. Browne A, Sun R (2001) Connectionist inference models.
Neural Netw 14(10):1331–1355
171. Cloete I, Zurada JM (2000) Knowledge-based neurocomputing
172. Hamilton K, Nayak A, Boz ˇic´ B, Longo L (2022) Is neuro-
symbolic ai meeting its promises in natural language process-
ing? a structured review. Semantic Web (Preprint), 1–42
173. Yu D, Yang B, Liu D, Wang H, Pan S (2023) A survey on
neural-symbolic learning systems. Neural Netw
174. Yang C, Chaudhuri S (2022) Safe neurosymbolic learning with
differentiable symbolic execution. arXiv preprint arXiv:2203.
07671
175. Shah A, Zhan E, Sun J, Verma A, Yue Y, Chaudhuri S (2020)
Learning differentiable programs with admissible neural
heuristics. Adv Neural Inf Process Syst 33:4940–4952
176. Barbin A, Cerutti F, Gerevini AE (2022) Addressing the symbol
grounding problem with constraints in neuro-symbolic planning
177. Zellers R, Holtzman A, Peters M, Mottaghi R, Kembhavi A,
Farhadi A, Choi Y (2021) Piglet: language grounding through
neuro-symbolic interaction in a 3d world. arXiv preprint arXiv:
2106.00188
178. Borghesani V, Piazza M (2017) The neuro-cognitive represen-
tations of symbols: the case of concrete words. Neuropsy-
chologia 105:4–17
179. Mao J, Gan C, Kohli P, Tenenbaum JB, Wu J (2019) The neuro-
symbolic concept learner: Interpreting scenes, words, and sen-
tences from natural supervision. arXiv preprint arXiv:1904.
12584
180. Cunnington D, Law M, Lobo J, Russo A (2024) The role of
foundation models in neuro-symbolic learning and reasoning.
arXiv preprint arXiv:2402.01889
181. De Ma´ntaras RL (1991) A distance-based attribute selection
measure for decision tree induction. Mach Learn 6:81–92
182. Valiant LG (1984) Deductive learning. Philos Trans R Soc Lond
Ser A Math Phys Sci 312(1522):441–446
183. Tiddi I, Schlobach S (2022) Knowledge graphs as tools for
explainable machine learning: a survey. Artif Intell 302:103627
184. Arulkumaran K, Deisenroth MP, Brundage M, Bharath AA
(2017) Deep reinforcement learning: a brief survey. IEEE Signal
Process Mag 34(6):26–38
185. Sutton RS, Barto AG (2018) Reinforcement learning: an
introduction
186. Sætre AS, Ven A (2021) Generating theory by abduction. Acad
Manag Rev 46(4):684–701
187. Al-Ajlan A (2015) The comparison between forward and
backward chaining. Int J Mach Learn Comput 5(2):106
188. Weber L, Minervini P, Mu¨ nchmeyer J, Leser U, Rockta¨ schel T
(2019) Nlprolog: reasoning with weak uniﬁcation for question
answering in natural language. arXiv preprint arXiv:1906.06187
189. Zhang B, Zhu J, Su H (2023) Toward the third generation
artiﬁcial intelligence. Sci China Inf Sci 66(2):1–19
190. SKahneman D (2013) Thinking, fast and slow
191. Kapanipathi P, Abdelaziz I, Ravishankar S, Roukos S, Gray A,
Astudillo R, Chang M, Cornelio C, Dana S, Fokoue A, et al
(2020) Leveraging abstract meaning representation for knowl-
edge base question answering. arXiv preprint arXiv:2012.01707
192. Huang J, Li Z, Chen B, Samel K, Naik M, Song L, Si X (2021)
Scallop: From probabilistic deductive databases to scalable
differentiable reasoning. Adv Neural Inf Process Syst
34:25134–25145
193. Smullyan RM (1995) First-order logic
194. Andrews PB (2013) An introduction to mathematical logic and
type theory: to truth through proof, vol 27
195. Garcez Ad, Bader S, Bowman H, Lamb LC, Penning L, Illu-
minoo B, Poon H, Zaverucha CG (2022) Neural-symbolic
Neural Computing and Applications (2024) 36:12809–12844 12841
123

learning and reasoning: a survey and interpretation. Neuro-
Symb Artif Intell State Art 342(1):327
196. Ehrlinger L, Wo¨ ß W (2016) Towards a deﬁnition of knowledge
graphs. SEMANTiCS (Posters, Demos, SuCCESS) 48(1–4):2
197. Ji S, Pan S, Cambria E, Marttinen P, Philip SY (2021) A survey
on knowledge graphs: representation, acquisition, and applica-
tions. IEEE Trans Neural Netw Learn Syst 33(2):494–514
198. Sun R (2002) Hybrid systems and connectionist implementa-
tionalism. Encyclop Cogn Sci 1:697–703
199. Mikolov T, Chen K, Corrado G, Dean J (2013) Efﬁcient esti-
mation of word representations in vector space. arXiv preprint
arXiv:1301.3781
200. Pennington J, Socher R, Manning CD (2014) Glove: Global
vectors for word representation. In: Proceedings of the 2014
conference on empirical methods in natural language processing
(EMNLP), pp 1532–1543
201. Burattini E, De Gregorio M, Tamburrin G (1999) Pictorial and
verbal components in artiﬁcial intelligence explanations. In:
Vision: the approach of biophysics and neurosciences: pro-
ceedings of the international school of biophysics, Casamicciola,
Napoli, Italy, 11-16 October 1999, vol 11, p 471
202. Hitzler P, Seda AK (2003) Continuity of semantic operators in
logic programming and their approximation by artiﬁcial neural
networks. In: KI 2003: advances in artiﬁcial intelligence: 26th
annual German conference on AI, KI 2003, Hamburg, Germany,
September 15-18, 2003. Proceedings 26. Springer, pp 355–369
203. Coraggio P, De Gregorio M, Forastiere M (2008) Robot navi-
gation based on neurosymbolic reasoning over landmarks. Int J
Pattern Recognit Artif Intell 22(05):1001–1014
204. Staffa M, Rossi S, De Gregorio M, Burattini E (2011) Thresh-
olds tuning of a neuro-symbolic net controlling a behavior-based
robotic system. In: ESANN
205. Price KV (2013) Differential evolution. Handbook of Opti-
mization: From Classical to Modern Approach, 187–214
206. Hasoon SO, Jasim YA (2013) Diagnosis windows problems
based on hybrid intelligence systems. J Eng Sci Technol
8(5):566–578
207. Golovko V, Kroshchanka A, Kovalev M, Taberko V, Ivaniuk D
(2020) Neuro-symbolic artiﬁcial intelligence: application for
control the quality of product labeling. In: Open semantic
technologies for intelligent system: 10th international confer-
ence, OSTIS 2020, Minsk, Belarus, February 19–22, 2020,
Revised Selected Papers. Springer, pp 81–101
208. Wang F-Y, Zhang JJ, Zheng X, Wang X, Yuan Y, Dai X, Zhang
J, Yang L (2016) Where does alphago go: from church-turing
thesis to alphago thesis and beyond. IEEE/CAA J Autom Sin
3(2):113–120
209. S´wiechowski M, Godlewski K, Sawicki B, Man ´dziuk J (2023)
Monte Carlo tree search: a review of recent modiﬁcations and
applications. Artif Intell Rev 56(3):2497–2562
210. Ultsch A (2000) The neuro-data-mine. In: Symposia on neural
computation (NC’2000), Berlin, Germany
211. Corchado JM, Lees B (2001) Adaptation of cases for case based
forecasting with neural network support. In: Soft computing in
case based reasoning, pp 293–319
212. Fdez-Riverola F, Corchado JM, Torres JM (2002) Neuro-sym-
bolic system for forecasting red tides. In: Artiﬁcial intelligence
and cognitive science: 13th Irish conference, AICS 2002 Lim-
erick, Ireland, September 12–13, 2002 Proceedings. Springer,
pp 45–52
213. Neagu C-D, Avouris N, Kalapanidas E, Palade V (2002) Neural
and neuro-fuzzy integration in a knowledge-based system for air
quality prediction. Appl Intell 17(2):141
214. Corchado Rodrı´guez JM, Aiken J, Rees N et al (2003) Neuro-
symbolic reasoning system for modeling complex behaviours
215. Fdez-Riverola F, Corchado JM (2003) Fsfrt: Forecasting system
for red tides: a hybrid autonomous ai model. Appl Artif Intell
17(10):955–982
216. Policastro CA, Carvalho AC, Delbem AC (2003) Hybrid
approaches for case retrieval and adaptation. In: KI 2003:
Advances in Artiﬁcial Intelligence: 26th Annual German Con-
ference on AI, KI 2003, Hamburg, Germany, September 15-18,
2003. Proceedings 26. Springer, pp 297–311
217. Ferna´ndez-Riverola F, Corchado JM (2004) Employing tsk
fuzzy models to automate the revision stage of a cbr system. In:
Current topics in artiﬁcial intelligence: 10th conference of the
Spanish association for artiﬁcial intelligence, CAEPIA 2003,
and 5th Conference on Technology Transfer, TTIA 2003, San
Sebastian, Spain, November 12-14, 2003. Revised Selected
Papers. Springer, pp 302–311
218. Corchado JM, Borrajo ML, Pellicer MA, Ya ´n˜ez JC (2005)
Neuro-symbolic system for business internal control. In:
Advances in data mining: applications in image mining, medi-
cine and biotechnology, management and environmental con-
trol, and telecommunications; 4th industrial conference on data
mining, ICDM 2004, Leipzig, Germany, July 4-7, 2004, Revised
Selected Papers 4. Springer, pp 1–10
219. Prentzas J, Hatzilygeroudis I, Michail O (2008) Improving the
accuracy of neuro-symbolic rules with case-based reasoning. In:
Proceedings of the ﬁrst international workshop on combinations
of intelligent methods and applications in conjunction with 18th
European conference on artiﬁcial intelligence, pp 49–54
220. Newman CBD (1998) Uci repository of machine learning
databases. http://www.ics.uci.edu/mlearn/MLRepository.html
221. Borrajo ML, Laza R, Corchado JM (2008) A complex case-
based advisor. Appl Artif Intell 22(5):377–406
222. Prentzas J, Hatzilygeroudis I (2011) Case-based reasoning
integrations: Approaches and applications. Case-based reason-
ing: processes, suitability and applications, 1–28
223. Hatzilygeroudis I, Prentzas J (2013) Fuzzy and neuro-symbolic
approaches in personal credit scoring: assessment of bank loan
applicants. In: Innovations in Intelligent Machines-4, p 319
224. Bach J, Herger P (2015) Request conﬁrmation networks for
neuro-symbolic script execution. In: CoCo@ NIPS
225. Bologna G, Hayashi Y (2017) Characterization of symbolic
rules embedded in deep dimlp networks: a challenge to trans-
parency of deep learning. J Artif Intell Soft Comput Res
7(4):265–286
226. Kraetzschmar G, Sablatno ¨
g S, Enderle S, Palm G (2000)
Application of neurosymbolic integration for environment
modelling in mobile robots. In: Hybrid neural systems. Springer,
pp 387–401
227. Burattini E, Coraggio P, De Gregorio M, Ripa B (2003) Agent
wisard: go and catch that image. In: Proc. First IAPR TC3
Workshop, Florence, Italy, vol 89, p 95
228. Grieco BP, Lima PM, De Gregorio M, Franc ¸a FM (2010) Pro-
ducing pattern examples from ‘‘mental’’ images. Neurocom-
puting 73(7–9):1057–1064
229. Coraggio P, De Gregorio M (2007) A neurosymbolic hybrid
approach for landmark recognition and robot localization. In:
Advances in brain, vision, and artiﬁcial intelligence: second
international symposium, BVAI 2007, Naples, Italy, October
10-12, 2007. Proceedings 2. Springer, pp 566–575
230. De Gregorio M (2008) An intelligent active video surveillance
system based on the integration of virtual neural sensors and bdi
agents. IEICE Trans Inf Syst 91(7):1914–1921
231. Qadeer N, Velik R, Zucker G, Boley H (2009) Knowledge
representation for a neuro-symbolic network in home care risk
identiﬁcation. In: 2009 7th IEEE international conference on
industrial informatics. IEEE, pp 277–282
12842 Neural Computing and Applications (2024) 36:12809–12844
123

232. Dietrich D, Bruckner D, Zucker G, Muller B, Tmej A (2009)
Psychoanalytical model for automation and robotics. In:
AFRICON 2009. IEEE, pp 1–8
233. Barbosa R, Cardoso DO, Carvalho D, Franc ¸a FM (2017) A
neuro-symbolic approach to gps trajectory classiﬁcation.
ESANN
234. Barbosa R, Cardoso DO, Carvalho D, Franca FM (2018)
Weightless neuro-symbolic gps trajectory classiﬁcation. Neu-
rocomputing 298:100–108
235. Yi K, Wu J, Gan C, Torralba A, Kohli P, Tenenbaum J (2018)
Neural-symbolic vqa: Disentangling reasoning from vision and
language understanding. In: Advances in neural information
processing systems, vol 31
236. Lavrac N, Dzeroski S (1994) Inductive logic programming. In:
WLP. Springer, pp 146–160
237. Hatzilygeroudis I, Prentzas J (2000) Neurules: improving the
performance of symbolic rules. Int J Artif Intell Tools
9(01):113–130
238. Oso´rio F, Amy B, Cechin A (2001) Hybrid machine learning
tools: Inss-a neuro-symbolic system for constructive machine
learning. Deep fusion of computational and symbolic process-
ing, 121–144
239. Garcez Ad, Broda K, Gabbay DM (2001) Symbolic knowledge
extraction from trained neural networks: a sound approach. Artif
Intell 125(1–2):155–207
240. Prentzas J, Hatzilygeroudis I, Garofalakis J (2002) A web-based
intelligent tutoring system using hybrid rules as its representa-
tional basis. In: Intelligent tutoring systems: 6th international
conference, ITS 2002 Biarritz, France and San Sebastian, Spain,
June 2–7, 2002 Proceedings 6. Springer, pp 119–128
241. Salgado GR, Amy B (2003) Neuro-symbolic hybrid system for
treatment of gradual rules. Neural Information Processing—
Letters and Reviews 1(2)
242. Prentzas N, Nicolaides A, Kyriacou E, Kakas A, Pattichis C
(2019) Integrating machine learning with symbolic reasoning to
build an explainable ai model for stroke prediction. In: 2019
IEEE 19th international conference on bioinformatics and bio-
engineering (BIBE). IEEE, pp 817–821
243. Thrun SB, Bala JW, Bloedorn E, Bratko I, Cestnik B, Cheng J,
De Jong KA, Dzeroski S, Fisher DH, Fahlman SE, et al (1991)
The monk’s problems: A performance comparison of different
learning algorithms. Technical report
244. Zhou J, Cui G, Hu S, Zhang Z, Yang C, Liu Z, Wang L, Li C,
Sun M (2020) Graph neural networks: a review of methods and
applications. AI Open 1:57–81
245. Omlin CW, Snyders S (2003) Inductive bias strength in
knowledge-based neural networks: application to magnetic res-
onance spectroscopy of breast tissues. Artif Intell Med
28(2):121–140
246. Bologna G (2003) A model for single and multiple knowledge
based networks. Artif Intell Med 28(2):141–163
247. Obot OU, Uzoka F-ME (2009) A framework for application of
neuro-case-rule base hybridization in medical diagnosis. Appl
Soft Comput 9(1):245–253
248. Boulahia J, Smirani L, KSA MA (2015) Experiments of a neuro
symbolic hybrid learning system with incomplete data
249. Ghosh J, Taha I (2018) A neuro-symbolic hybrid intelligent
architecture with. In: Recent advances in artiﬁcial neural net-
works, 1
250. Bhatia S, Kohli P, Singh R (2018) Neuro-symbolic program
corrector for introductory programming assignments. In: Pro-
ceedings of the 40th international conference on software
engineering, pp 60–70
251. Souici-Meslati L, Sellami M (2004) A hybrid approach for
arabic literal amounts recognition. Arab J Sci Eng 29
252. Perrier M, Kalwa J (2005) Intelligent diagnosis for autonomous
underwater vehicles using a neuro-symbolic system in a dis-
tributed architecture. In: Europe Oceans 2005, vol 1. IEEE,
pp 350–355
253. Sa´nchez VGC, Villegas OOV, Salgado GR, Dominguez H
(2008) Quality inspection of textile artiﬁcial textures using a
neuro-symbolic hybrid system methodology. WSEAS Trans
Comput 12:1899–1905
254. Velik R, Boley H (2010) Neurosymbolic alerting rules. IEEE
Trans Ind Electron 57(11):3661–3668
255. Komendantskaya E, Zhang Q (2011) Sherlock-a neural network
software for automated problem solving. In: Proceedings of
seventh international workshop on neural-symbolic learning and
reasoning
256. Saikia S, Vig L, Srinivasan A, Shroff G, Agarwal P, Rawat R
(2016) Neuro-symbolic eda-based optimisation using ilp-en-
hanced dbns. arXiv preprint arXiv:1612.06528
257. Kursuncu U, Gaur M, Sheth A (2019) Knowledge infused
learning (k-il): Towards deep incorporation of knowledge in
deep learning. arXiv preprint arXiv:1912.00512
258. Khan MJ, Curry E (2020) Neuro-symbolic visual reasoning for
multimedia event processing: Overview, prospects and chal-
lenges. In: CIKM (Workshops)
259. Kapanipathi P, Abdelaziz I, Ravishankar S, Roukos S, Gray A,
Astudillo R, Chang M, Cornelio C, Dana S, Fokoue A, et al
(2020) Question answering over knowledge bases by leveraging
semantic parsing and neuro-symbolic reasoning. arXiv preprint
arXiv:2012.01707
260. Yang Z, Ishay A, Lee J (2020) Neurasp: embracing neural
networks into answer set programming. In: 29th international
joint conference on artiﬁcial intelligence (IJCAI 2020)
261. Siyaev A, Jo G-S (2021) Neuro-symbolic speech understanding
in aircraft maintenance metaverse. IEEE Access
9:154484–154499
262. Stammer W, Schramowski P, Kersting K (2021) Right for the
right concept: revising neuro-symbolic concepts by interacting
with their explanations. In: Proceedings of the IEEE/CVF con-
ference on computer vision and pattern recognition,
pp 3619–3629
263. Kimura D, Ono M, Chaudhury S, Kohita R, Wachi A, Agravante
DJ, Tatsubori M, Munawar A, Gray A (2021) Neuro-symbolic
reinforcement learning with ﬁrst-order logic. arXiv preprint
arXiv:2110.10963
264. Evans R, Bos ˇnjak M, Buesing L, Ellis K, Pfau D, Kohli P,
Sergot M (2021) Making sense of raw input. Artif Intell
299:103521
265. Mitchener L, Tuckey D, Crosby M, Russo A (2022) Detect,
understand, act: a neuro-symbolic hierarchical reinforcement
learning framework. Mach Learn 111(4):1523–1549
266. Alshahrani M, Khan MA, Maddouri O, Kinjo AR, Queralt-
Rosinach N, Hoehndorf R (2017) Neuro-symbolic representa-
tion learning on biological knowledge graphs. Bioinformatics
33(17):2723–2730
267. Perozzi B, Al-Rfou R, Skiena S (2014) Deepwalk: Online
learning of social representations. In: Proceedings of the 20th
ACM SIGKDD international conference on knowledge discov-
ery and data mining, pp 701–710
268. Agibetov A, Samwald M (2018) Fast and scalable learning of
neuro-symbolic representations of biomedical knowledge. arXiv
preprint arXiv:1804.11105
269. Wu L, Fisch A, Chopra S, Adams K, Bordes A, Weston J (2018)
Starspace: Embed all the things! In: Proceedings of the AAAI
conference on artiﬁcial intelligence, vol 32
270. Bianchi F, Palmonari M, Hitzler P, Seraﬁni L (2019) Comple-
menting logical reasoning with sub-symbolic commonsense. In:
Rules and reasoning: third international joint conference,
Neural Computing and Applications (2024) 36:12809–12844 12843
123

RuleML? RR 2019, Bolzano, Italy, September 16–19, 2019,
Proceedings 3. Springer, pp 161–170
271. Bianchi F, Palmonari M, Nozza D (2018) Towards encoding
time in text-based entity embeddings. In: The semantic web–
ISWC 2018: 17th international semantic web conference,
Monterey, CA, USA, October 8–12, 2018, Proceedings, Part I
17. Springer, pp 56–71
272. Oltramari A, Francis J, Henson C, Ma K, Wickramarachchi R
(2020) Neuro-symbolic architectures for context understanding.
arXiv preprint arXiv:2003.04707
273. Singh P, Lin T, Mueller ET, Lim G, Perkins T, Li Zhu W (2002)
Open mind common sense: knowledge acquisition from the
general public. In: On the move to meaningful internet systems
2002: CoopIS, DOA, and ODBASE: confederated international
conferences CoopIS, DOA, and ODBASE 2002 Proceedings.
Springer, pp 1223–1237
274. Wang Q, Mao Z, Wang B, Guo L (2017) Knowledge graph
embedding: a survey of approaches and applications. IEEE
Trans Knowl Data Eng 29(12):2724–2743
275. Doldy D, Garridoy JS (2021) An energy-based model for neuro-
symbolic reasoning on knowledge graphs. In: 2021 20th IEEE
international conference on machine learning and applications
(ICMLA). IEEE, pp 916–921
276. Nickel M, Tresp V, Kriegel H-P (2011) A three-way model for
collective learning on multi-relational data. In: Icml, vol 11,
pp 3104482–3104584
277. Sun K, Rayudu H, Pujara J (2021) A hybrid probabilistic
approach for table understanding. In: Proceedings of the AAAI
conference on artiﬁcial intelligence, vol 35, pp 4366–4374
278. Kimmig A, Bach S, Broecheler M, Huang B, Getoor L (2012) A
short introduction to probabilistic soft logic. In: Proceedings of
the NIPS workshop on probabilistic programming: foundations
and applications, pp 1–4
279. Gol MG, Pujara J, Szekely P (2019) Tabular cell classiﬁcation
using pre-trained cell embeddings. In: 2019 IEEE international
conference on data mining (ICDM). IEEE, pp 230–239
280. Ding M, Chen Z, Du T, Luo P, Tenenbaum J, Gan C (2021)
Dynamic visual reasoning by learning differentiable physics
models from video and language. Adv Neural Inf Process Syst
34:887–899
281. Ma K, Francis J, Lu Q, Nyberg E, Oltramari A (2019) Towards
generalizable neuro-symbolic systems for commonsense ques-
tion answering. arXiv preprint arXiv:1910.14087
282. Sundar LKS, Muzik O, Buvat I, Bidaut L, Beyer T (2021)
Potentials and caveats of ai in hybrid imaging. Methods
188:4–19
283. Kang T, Turfah A, Kim J, Perotte A, Weng C (2021) A neuro-
symbolic method for understanding free-text medical evidence.
J Am Med Inform Assoc 28(8):1703–1711
284. Yin P, Neubig G (2017) A syntactic neural model for general-
purpose code generation. arXiv preprint arXiv:1704.01696
285. Ritchie D, Guerrero P, Jones RK, Mitra NJ, Schulz A, Willis
KD, Wu J (2023) Neurosymbolic models for computer graphics.
In: Computer graphics forum, vol 42. Wiley Online Library,
pp 545–568
286. Reddy AG, Balasubramanian VN (2022) Estimating treatment
effects using neurosymbolic program synthesis. arXiv preprint
arXiv:2211.04370
287. Li Z, Huang J, Naik M (2023) Scallop: A language for neu-
rosymbolic programming. Proceedings of the ACM on Pro-
gramming Languages 7(PLDI):1463–1487
288. Varela FA (2022) The effects of hybrid neural networks on
meta-learning objectives. PhD thesis
289. Mundhenk TN, Landajuela M, Glatt R, Santiago CP, Faissol
DM, Petersen BK (2021) Symbolic regression via neural-guided
genetic programming population seeding. arXiv preprint arXiv:
2111.00053
290. Chen X, Liang C, Huang D, Real E, Wang K, Pham H, Dong X,
Luong T, Hsieh C-J, Lu Y et al (2024) Symbolic discovery of
optimization algorithms. In: Advances in neural information
processing systems, vol 36
291. Mittelstadt BD, Allo P, Taddeo M, Wachter S, Floridi L (2016)
The ethics of algorithms: mapping the debate. Big Data Soc
3(2):2053951716679679
292. Rudin C (2019) Stop explaining black box machine learning
models for high stakes decisions and use interpretable models
instead. Nature Mach Intell 1(5):206–215
293. Kazim E, Denny DMT, Koshiyama A (2021) Ai auditing and
impact assessment: according to the UK information commis-
sioner’s ofﬁce. AI Ethics 1:301–310
294. Jobin A, Ienca M, Vayena E (2019) The global landscape of ai
ethics guidelines. Nat Mach Intell 1(9):389–399
295. Tamang MD, Shukla VK, Anwar S, Punhani R (2021)
Improving business intelligence through machine learning
algorithms. In: 2021 2nd International conference on intelligent
engineering and management (ICIEM). IEEE, pp 63–68
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Springer Nature or its licensor (e.g. a society or other partner) holds
exclusive rights to this article under a publishing agreement with the
author(s) or other rightsholder(s); author self-archiving of the
accepted manuscript version of this article is solely governed by the
terms of such publishing agreement and applicable law.
12844 Neural Computing and Applications (2024) 36:12809–12844
123
