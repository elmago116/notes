---
title: "The use of Semantic Technologies in Computer Science Curriculum: A Systematic Review"
year: "2022"
tags:
  - Tech/SemanticWeb
  - research_method/ScopingReview
---
![[The use of Semantic Technologies in Computer Science Curriculum A Systematic Review.pdf]]

## PDF text extraction

The use of Semantic Technologies in Computer
Science Curriculum: A Systematic Review
Yixin Cheng
Yixin.Cheng@anu.edu.au
The Australian National University
Canberra, Australia
Bernardo Pereira Nunes
Bernardo.Nunes@anu.edu.au
The Australian National University
Canberra, Australia
Abstract
Semantic technologies are evolving and being applied in sev-
eral research areas, including the education domain. This
paper presents the outcomes of a systematic review carried
out to provide an overview of the application of semantic
technologies in the context of the Computer Science curricu-
lum and discuss the limitations in this field whilst offering
insights for future research. A total of 4,510 studies were
reviewed, and 37 were analysed and reported. As a result,
while semantic technologies have been increasingly used to
develop Computer Science curricula, the alignment of on-
tologies and accurate curricula assessment appears to be the
most significant limitations to the widespread adoption of
such technologies.
CCS Concepts:• General and reference→Surveys and
overviews; • Social and professional topics→Model
curricula; • Computing methodologies→Ontology en-
gineering.
Keywords: Semantic Technologies, Computer Science Cur-
riculum, Systematic Review
1 Introduction
The Semantic Web (SW) is a decentralised global information
space for sharing machine-readable data with minimal inter-
operability and integration costs [18, 49]. It aims at enabling
machines to understand and answer the requests of people
and machines through several standards and technologies1.
For instance, the Resource Description Framework (RDF)
is the standard data model to represent information 2 [21]
whereas the Web Ontology Language (OWL) is the stan-
dard language for defining vocabularies/ontologies on the
Web [3].
Ontologies — a formal representation of the shared knowl-
edge of a domain [38] — are one of the core technologies
of the Semantic Web. Analogous to the concept of ontolo-
gies is the concept of curriculum in the educational domain.
Cox [8], for example, defines a curriculum as a selection
and organisation of knowledge for educational purposes
used to represent the shared agreement on what learners
should know in different stages of life. Another definition is
provided by Chung and Kim in [7] where they state that a
1https://www.w3.org/standards/semanticweb/
2https://www.w3.org/TR/rdf-concepts/
curriculum is a course blueprint designed to guide students’
learning [7] through a planned sequence of subjects [31]. As
a technology, ontologies can support curriculum design by
representing domain knowledge for educational purposes.
Cassel et al. [6], for instance, proposed the ontology of com-
puting to support the development of a Computer Science
curriculum while Wang et al. [47] proposed the computer
course architectural ontology system.
This paper presents a systematic review on the use of
semantic technologies in the context of Computer Science
Education. We review existing initiatives using semantic
technologies for curriculum design as well as the key chal-
lenges for their widespread adoption. The following research
question guided the development of this work:
•What are the semantic technologies used in the context
of Computer Science curriculum?
A total of 4,510 papers were retrieved from mainstream
digital libraries and, after detailed analysis, 37 papers were
found to be relevant. The reviewed articles focus on the use of
ontologies and semantic technologies for curriculum design,
curriculum interoperability and analysis. Here, we report
on the tools/frameworks, datasets, vocabularies/ontologies,
as well as the challenges of using and adopting semantic
technologies in curriculum design in Computer Science to
leverage new research opportunities.
The remainder of this paper is structured as follows: Sec-
tion 2 reviews closely related surveys to semantic technolo-
gies in Education. Section 3 describes the research method-
ology used to carry out this systematic review. Section 4
provides an overview of employing semantic technologies
in Computer Science curriculum. Section 5 discusses the
challenges and, finally, Section 6 concludes the paper.
2 Related Work
Krieger and Rösner [ 22] present a comprehensive review
of the effects and applications of semantic technologies in
e-learning. They discuss the construction of models with
educational ontologies where they provide an ontology-wise
overview in a Web-based educational environment. Accord-
ing to their work, the educational semantic web services
include adaptive learning and e-assessment. Finally, they
raise a few issues of adopting semantic technologies for data
integration such as trust and credibility in data from multiple
sources.
1
arXiv:2205.00462v2  [cs.CY]  25 Aug 2022

Another relevant survey was conducted by Pereira et
al. [37], where they reviewed various applications of Linked
Data in the context of Education, including datasets, tools
and common vocabularies/ontologies. They also identified
the challenges in each stage of the process and provided an
overview of the development in that area.
In another survey, Navarrete and Lujan-Mora [28] focused
on the use of Linked Data to enrich Open Educational Re-
sources (OER). Their study described how OER Web sites
can adopt the Linked Data principles through the 5-star de-
ployment scheme to enhance discovery, retrieval, reuse and
remix of OERs.
Regarding ontology-related studies, Stancin et al. [43] sur-
veyed ontologies used in educational contexts. Their survey
is a valuable contribution to curriculum modelling and man-
agement describing learning domains, educational data and
e-learning services using ontologies. They also provide a
clear definition of the term ontology along with traditional
methodologies for their creation in the field of Education.
Likewise, Tapia-Leon et al. [45] surveyed the application of
ontologies in Higher Education institutions and proposed
guidelines for ontology creation.
Despite the contributions presented in previous studies,
semantic technologies in Curriculum Design, specifically
applied to Computer Science, have not yet been thoroughly
investigated. This paper fills the gap in the literature by
systematically reviewing the usage of semantic technologies
applied to Computer Science Curriculum Design.
3 Research Methodology
This systematic review was conducted following the method-
ology defined by Kitchenham and Charters [4]. The method
is composed of three main steps: planning, conducting and
reporting. The planning stage helps to identify existing re-
search in the area of interest as well as build the research
question. Our research question was created based on the
PICOC method [4] and used to identify keywords and corre-
sponding synonyms to build the search string to find relevant
related works. The resulting search string is given below.
("computer science" OR "computer engineering" OR "infor-
matics") AND ("curriculum" OR "course description" OR "learn-
ing outcomes" OR "curricula" OR "learning objects") AND ("se-
mantic" OR "ontology" OR "linked data" OR "linked open data")
To include a paper in this systematic review, we defined
the following inclusion criteria: (1) papers must have been
written in English; (2) papers must be exclusively related to
semantic technologies, Computer Science and curriculum;
(3) papers must have four or more pages (i.e., full research
papers); (4) papers must be accessible online; and, finally, (5)
papers must be scientifically sound, present a clear method-
ology and conduct a proper evaluation for the proposed
method, tool or model.
Figure 1.Paper Selection Process
Figure 1 shows the paper selection process in detail. Ini-
tially, 4,510 papers were retrieved using the ACM Digital
Library3, IEEE Xplore Digital Library4, Springer5, Scopus6,
ScienceDirect7 and Web of Science8 as digital libraries. The
Springer digital library returned a total of 3,549 studies. The
large number of papers returned by the Springer search
mechanism led us to develop a simple crawling tool to help
us in the process of including/rejecting papers in our system-
atic review. All the information returned by Springer was
collected and stored in a relational database. After that, we
were able to correctly query the Springer database and select
the relevant papers for this systematic review.
We also applied the forward and backward snowballing
method to this systematic review to identify relevant papers
that were not retrieved by our query string. The backward
snowballing method was used to collect relevant papers from
the references of the final list of papers in Phase 1, whereas
3https://dl.acm.org/
4https://ieeexplore.ieee.org/
5https://www.springer.com/
6https://www.scopus.com/
7https://www.sciencedirect.com/
8https://www.webofscience.com/
2

the forward snowballing method was used to collect the
papers that cited these papers [48]. Google Scholar9 was used
in the forward snowballing method. In total, 37 studies were
identified as relevant; most of the studies were published
in the last few years, although no relevant paper has been
published in 2022.
4 Semantic Technologies in Computer
Science Curriculum Design
4.1 Tools/Frameworks
Protégé10[18] is a popular open-source editor and frame-
work for ontology construction, which several researchers
have adopted to design curricula in Computer Science [16,
19, 25, 32, 41, 44, 46, 47]. Despite its wide adoption, Pro-
tégé still presents limitations in terms of the manipulation
of ontological knowledge [44]. As an attempt to overcome
this shortcoming, Asoke et al. [19] developed a curriculum
design plug-in called OntoCD, allowing curriculum design-
ers to customise curricula by loading a skeleton curriculum
and a benchmark domain ontology. OntoCD is evaluated by
designing a Computer Science degree curriculum using a
benchmark domain ontology proposed by ACM and IEEE
[1]. Moreover, Adelina and Jason [ 44] used Protégé to de-
velop the Sunway University Computing Ontology (SUCO),
an ontology-specific Application Programming Interface for
curricula management system. They claim that, in response
to the shortcoming with using the Protégé platform, the
SUCO tool shows a higher level of ability to manipulate and
extract knowledge in addition to functioning effectively if
the ontology is processed as an eXtensible Markup Language
(XML) format document.
Other specific ontology-based tools in curriculum man-
agement have also been developed, e.g., the CDIO frame-
work [24]. CDIO was created to automatically adapt a given
curriculum according to teaching objectives and content.
Similarly, Maffei et al. [ 25] utilised CONALI ontology as
a tool for representing the semantics behind the construc-
tive alignment activities to design, synthesise and evaluate
courses in different domains. Likewise, in Mandić’s study,
the author presented a software platform11 for comparing
informatics teacher education curricula [26]. In Hedayati’s
work, the authors used the curriculum Capability Maturity
Model (CMM), which is a taxonomical model used for de-
scribing the organisation’s level of capability in the domain
of software engineering [35], as the reference model to dis-
cuss an ontology-driven modelling to the culturally sensitive
curriculum development process in the context of vocational
ICT education in Afghanistan [16].
Finally, Vaquero et al. [ 46] used an experience-sharing
tool to transform information into knowledge to improve
9https://scholar.google.com/
10https://protege.stanford.edu/
11http://www.pef.uns.ac.rs/InformaticsTeacherEducationCurriculum
curriculum design called the “Set of Experience Knowledge
Structure” (SOEKS) [40]. SOEKS is used as part of a process
to collect, infer and manage explicit knowledge using ontolo-
gies and semantic reasoning to provide curriculum designers
with different expert perspectives for curriculum design.
4.2 Datasets
One of the most popular datasets used to build ontologies or
as benchmarks between Computer Science curricula is the
open-access CS201312 [1]. This dataset results from the joint
development sponsored by the ACM and IEEE Computer
Society of a computing curriculum [ 38]. CS2013 has been
widely adopted [2, 12, 16, 19, 31, 32] due to its international
reach and curricula and pedagogical guidelines.
Similar to CS2013, the Thailand Qualification Framework
for Higher Education (TQF: HEd) was developed by the Of-
fice of the Thailand Higher Education Commission to be used
by all Higher Education Institutions (HEIs) in Thailand as a
framework to enhance the quality of course curricula and en-
able academic mobility. The TQF: HEd guidelines have been
used in terms of ontology development in several studies for
Computer Science curriculum design [15, 31–33].
Other studies use self-created datasets [ 12, 16, 25, 47].
Specifically, in Wang’s work, the Ontology System for the
Computer Course Architecture (OSCCA) was proposed based
on a dataset created using course catalogues from top univer-
sities in China and network education Web sites [47]. In Maf-
fei’s study, the authors experiment and evaluate the proposal
based on the Engineering program at KTH Royal Institute
of Technology in Stockholm, Sweden [25]. In Gubervic et
al. ’s work, the dataset used for comparing courses comes
from the Faculty of Electrical Engineering and Computing
at the University of Zagreb in Croatia and all universities
from United States of America [14]. In Fiallos’s study, not
only did the authors adopt CS2013 for domain ontologies
modelling, but also the core Computational Sciences courses
from the Escuela Superior Politécnica del Litoral (ESPOL13)
in Ecuador were collected to compare semantic similarity
between curricula. [12].
4.3 Knowledge Representation
RDF is used as the design standard for data interchange in
the following studies [32, 38, 41]. In particular, Saquicela et
al. [41] generated curriculum data in RDF format, creating
and storing data in a repository when the ontological model
has been defined and created.
Built on RDF and extended with additional vocabulary and
semantics [27], OWL14 is a vocabulary used in many studies
for representing and sharing knowledge on the Web [5, 25,
12https://cs2013.org/
13https://www.espol.edu.ec/
14https://www.w3.org/OWL/
3

26, 38, 46, 47]. Apart from OWL, two studies used XML15 due
to implementation requirements of their researches [15, 44].
Body of Knowledge (BoK) is another method for repre-
senting knowledge, often using OWL. It offers a complete set
of concepts, terms and activities for a professional domain
[38]. BoK has been used in many studies [7, 15, 19, 31, 33, 45]
for curriculum design, including Piedra and Caro [38] who
used it based on the IEEE/ACM CS2013 ontology as “a spec-
ification of the content to be covered and a curriculum as
an implementation”; Numtawong et al. [32] who used it to
map different ontologies based on the ontology of TQF: HEd;
and, Barb and Kilicay-Ergin [ 5] who used BoK based on
the Library of Congress Subject Headings16 to propose and
evaluate an ontology for an Information Science curriculum.
4.4 Use of Semantic Technologies in Computer
Science Curriculum Design
Semantic technologies have been found helpful in the con-
text of curriculum design to (i) extract and analyse the re-
lationship between concepts from learning materials; (ii)
measure the similarity between courses/disciplines and their
pre-requisites; and, (iii) create ontologies to enable course /
curriculum analysis. These approaches mainly aim to enable
academic mobility and curriculum interoperability across
institutions [38].
Most approaches and tools use natural language process-
ing techniques (e.g., NLTK17) to generate semantic descrip-
tions for ontology creation [38, 45] based on extracted con-
cepts and their relationships [47], find patterns in curricula
[34] and compare them [20]. Analysis and comparison of con-
cepts extracted are performed based on word [34], sentence
[2, 12, 36] and concept network level [17, 31–33].
Lexical database of semantic relations such as WordNet18
[36] and Latent Semantic Analysis [10, 14] are also used to
measure the similarity of courses/disciplines or define ontol-
ogy mapping rules to establish dependency relationships be-
tween curricula. For performance reasons, these approaches
are often combined with clustering [41], statistical methods
[5, 34, 41], and established taxonomies, such as the Bloom
Taxonomy, [23, 26] to measure course similarity.
5 Discussion
Semantic technologies have the potential to facilitate aca-
demic mobility, curriculum interoperability, program and
course benchmarking, and the design of new curricula. How-
ever, despite its potential benefits, several challenges hamper
its broad adoption in Computer Science and in other do-
mains.
15https://www.w3.org/standards/xml/
16https://www.loc.gov/aba/cataloging/subject/
17https://www.nltk.org/
18https://wordnet.princeton.edu/
One of the challenges is to create domain-specific ontolo-
gies to represent all the areas of computing, as mentioned
in [13]. The main challenges are that the existing ontolo-
gies for CS represent different structures for CS programs
and courses as well as represent concepts in different depths
and contexts. Ontology Alignment (OA) techniques to ad-
dress these issues have been extensively proposed [15, 38],
however, OA is still a research problem [9, 30]. Further in-
vestigation is required to understand the difference in CS
curricula in different universities and how these differences
can be used to enhance existing CS programs and curricula.
Although Sekiya et al. [ 42] present a study where the top
ten universities in the USA in 2015 uniformly covered topics
in Computer Science using the CS2013 curriculum guide-
lines, “there is no single correct ontology for any domain " [29].
Therefore, multiple ontologies are required to account for
the diversity and local needs of each CS program and course,
HEI and country. We note, however, that reuse and modu-
larity are important factors to be considered when building
ontologies [39] and, although a list of Good Ontologies 19
are available to assist ontology creators, many of the studies
reviewed do not reuse them.
Other aspects to consider when building ontologies are
maintainability and correctness [39]. An ontology must take
into account changes and the correct interpretation of domain-
specific concepts to avoid erroneous inferences and, there-
fore, impact the use of that ontology in a specific domain,
e.g., in our context, hinder academic mobility and curricular
interoperability. We recognise that this might be a difficult
problem to solve as curriculum design are often based on
cultural background and ideology.
Domain-specific semantic tools for curriculum design are
lacking, while the use of multipurpose semantic tools can
introduce errors into the process of creation (and alignment)
of curriculum design, requiring manual verification [ 34],
which makes the process less attractive and, therefore, less
adoptable by HEIs. To exemplify this problem, consider the
common Learning Outcomes creation/alignment task. Many
curriculum creators rely on the hierarchical structure of
Bloom’s Taxonomy (Remembering, Understanding, Apply-
ing, Analysing, Evaluating and Creating) [23], but represent-
ing or capturing each of these levels from textual descrip-
tions by multipurpose semantic tools is hard [26, 36]. Future
research on semantic reasoners is promising, as seen in [46].
For ontology creation, Protégé seems to be the standard
tool (see Section 4.1). However, as it is not a tool for creating
curricula, many studies have created extensions (and other
tools) to facilitate the creation of curricula [19, 44]. Future
research on ontology creation tools and curriculum design is
required to elicit the requirements for an ontology creation
tool for curriculum design.
19https://www.w3.org/wiki/Good_Ontologies
4

Another issue is related to the reproducibility of the pro-
posed ontologies for CS curricula. Several studies [11, 24, 44,
46, 47] do not make their datasets available nor validate their
approaches. We finalise this discussion with a call for repro-
ducible research in this field. Ontologies and datasets must
be available to take advantage of the benefits of semantic
technologies.
6 Conclusion
This study presented a systematic review on semantic tech-
nologies applied in the context of Computer Science and
Curriculum Design.
This paper addressed the most common topics covered
in the literature, such as tools and frameworks used for cur-
riculum design; datasets used to evaluate and propose Com-
puter Science curricula; knowledge representation models
to manage curriculum data; and the many uses of semantic
technologies in the context of curriculum design.
Although there are common challenges faced in curricu-
lum design using semantic technologies such as the effi-
ciency of data processing and the evaluation and alignment
of ontologies, the use of semantic technologies facilitates
numerous improvements in academic activities (such as cur-
ricula design, mobility, interoperability and benchmarking).
The literature reviewed are an initial but important step
to allow the construction of CS curricula. However, to en-
able further adoption of semantic technologies, HEIs need
to make their curricula available using semantic standards
using frameworks and languages such as RDF and OWL.
References
[1] ACM/IEEE-CS Joint Task Force on Computing Curricula. 2013. Com-
puter Science Curricula 2013 . Technical Report. ACM Press and IEEE
Computer Society Press. https://doi.org/10.1145/2534860
[2] Eiman Aeiad and Farid Meziane. 2016. Validating learning outcomes
of an E-Learning system using NLP. Lecture Notes in Computer Science
(including subseries Lecture Notes in Artificial Intelligence and Lecture
Notes in Bioinformatics) 9612 (2016), 292–300. https://doi.org/10.1007/
978-3-319-41754-7_27
[3] Pierre Allard and Sébastien Ferré. 2008. Dynamic Taxonomies for the
Semantic Web. 382 – 386. https://doi.org/10.1109/DEXA.2008.71
[4] Kitchenham BA and Stuart Charters. 2007. Guidelines for performing
Systematic Literature Reviews in Software Engineering. 2 (01 2007).
[5] Adrian S. Barb and Nil Kilicay-Ergin. 2020. Applications of Natural
Language Techniques to Enhance Curricular Coherence.Procedia Com-
puter Science 168 (2020), 88–96. https://doi.org/10.1016/j.procs.2020.
02.263 “Complex Adaptive Systems”Malvern, PennsylvaniaNovember
13-15, 2019.
[6] Lillian N. Cassel, Gordon Davies, William Fone, Anneke Hacque-
bard, John Impagliazzo, Richard LeBlanc, Joyce Currie Little, Andrew
McGettrick, and Michela Pedrona. 2007. The Computing Ontology:
Application in Education. SIGCSE Bull. 39, 4 (Dec. 2007), 171–183.
https://doi.org/10.1145/1345375.1345439
[7] Hyun Sook Chung and Jung Min Kim. 2014. Semantic model of syl-
labus and learning ontology for intelligent learning system. Lecture
Notes in Computer Science (including subseries Lecture Notes in Artificial
Intelligence and Lecture Notes in Bioinformatics) 8733 (2014), 175–183.
https://doi.org/10.1007/978-3-319-11289-3_18
[8] Cristián Cox. 2005. Cecilia Braslavsky and the Curriculum.PROSPECTS
35, 4 (2005), 415–427. https://doi.org/10.1007/s11125-006-7258-9
[9] Jairo Francisco de Souza, Sean Wolfgand Matsui Siqueira, and
Bernardo Pereira Nunes. 2020. A framework to aggregate multi-
ple ontology matchers. Int. J. Web Inf. Syst. 16, 2 (2020), 151–169.
https://doi.org/10.1108/IJWIS-05-2019-0023
[10] Scott Deerwester, Susan T. Dumais, George W. Furnas, Thomas K.
Landauer, and Richard Harshman. 1990. Indexing by Latent Semantic
Analysis. JOURNAL OF THE AMERICAN SOCIETY FOR INFORMATION
SCIENCE 41 (1990), 391–407.
[11] Hilary Dexter and Ioan Davies. 2009. An ontology-based curriculum
knowledgebase for managing complexity and. Proceedings - 2009
9th IEEE International Conference on Advanced Learning Technologies,
ICALT 2009 June (2009), 136–140. https://doi.org/10.1109/ICALT.2009.
85
[12] Angel Fiallos. 2018. Assisted curricula design based on generation
of domain ontologies and the use of NLP techniques. 2017 IEEE 2nd
Ecuador Technical Chapters Meeting, ETCM 2017 2017-Janua (2018),
1–6. https://doi.org/10.1109/ETCM.2017.8247474
[13] CC2020 Task Force. 2020. Computing Curricula 2020: Paradigms for
Global Computing Education . Association for Computing Machinery,
New York, NY, USA.
[14] E. Guberovic, F. Turcinovic, Z. Relja, and I. Bosnic. 2018. In search of a
syllabus: Comparing computer science courses. 2018 41st International
Convention on Information and Communication Technology, Electronics
and Microelectronics, MIPRO 2018 - Proceedings (2018), 588–592. https:
//doi.org/10.23919/MIPRO.2018.8400111
[15] Xingwei Hao, Xiangxu Meng, and Xu Cui. 2008. Knowledge Point
Based Curriculum Developing and Learning Object Reusing. Knowl-
edge Creation Diffusion Utilization (2008), 126–137.
[16] Mohammad Hadi Hedayati and Laanpere Mart. 2016. Ontology-driven
modeling for the culturally-sensitive curriculum development: A case
study in the context of vocational ICT education in Afghanistan. Pro-
ceedings of the 10th INDIACom; 2016 3rd International Conference on
Computing for Sustainable Global Development, INDIACom 2016 Ontol-
ogy 101 (2016), 928–932.
[17] Wael H.Gomaa and Aly A. Fahmy. 2013. A Survey of Text Similarity
Approaches. International Journal of Computer Applications 68, 13
(2013), 13–18. https://doi.org/10.5120/11638-7118
[18] Muhammad Imran and R. I.M. Young. 2016. Reference ontologies
for interoperability across multiple assembly systems. International
Journal of Production Research 54, 18 (2016), 5381–5403. https://doi.
org/10.1080/00207543.2015.1087654
[19] Asoka S. Karunananda, Gihan M. Rajakaruna, and Shantha Jayalal.
2012. OntoCD - Ontological solution for curriculum development.
International Conference on Advances in ICT for Emerging Regions,
ICTer 2012 - Conference Proceedings (2012), 137–144. https://doi.org/
10.1109/ICTer.2012.6421412
[20] Kornraphop Kawintiranon, Peerapon Vateekul, Atiwong Suchato, and
Proadpran Punyabukkana. 2016. Understanding knowledge areas
in curriculum through text mining from course materials. In 2016
IEEE International Conference on Teaching, Assessment, and Learning
for Engineering (TALE) . 161–168. https://doi.org/10.1109/TALE.2016.
7851788
[21] Graham Klyne and Jeremy Carroll. 2006. Resource Description Frame-
work (RDF): Concepts and Abstract Syntax. World Wide Web Consor-
tium 10 (01 2006).
[22] Katrin Krieger and Dietmar Rösner. 2011. Linked Data in E-Learning:
A Survey. Semantic Web 0 0 (2011), 1–9. http://semantic-web-journal.
org/sites/default/files/swj184.pdf
[23] Thomas J. Lasley. 2013. Bloom’s Taxonomy. https://doi.org/10.4135/
9781412957403.n51
[24] Ye Liang and Xiaojun Ma. 2012. Teaching reform of software engi-
neering course. ICCSE 2012 - Proceedings of 2012 7th International
5

Conference on Computer Science and Education Iccse (2012), 1936–1939.
https://doi.org/10.1109/ICCSE.2012.6295452
[25] Antonio Maffei, Lorenzo Daghini, Andreas Archenti, and Niels Lohse.
2016. CONALI Ontology. A Framework for Design and Evaluation
of Constructively Aligned Courses in Higher Education: Putting in
Focus the Educational Goal Verbs. Procedia CIRP 50 (2016), 765–772.
https://doi.org/10.1016/j.procir.2016.06.004
[26] Milinko Mandić. 2018. Semantic web based software platform for
curriculum harmonization*. ACM International Conference Proceeding
Series (2018). https://doi.org/10.1145/3227609.3227654
[27] Deborah L McGuinness and Frank van Harmelen. 2004. OWL Web
Ontology Language Overview. W3C recommendation 10, February
(2004). http://www.w3.org/TR/owl-features/
[28] Rosa Navarrete and Sergio Lujan-Mora. 2015. Use of Linked Data to
enhance Open Educational Resources. 2015 International Conference
on Information Technology Based Higher Education and Training, ITHET
2015 (2015). https://doi.org/10.1109/ITHET.2015.7218017
[29] N. Noy and Deborah Mcguinness. 2001. Ontology Development 101: A
Guide to Creating Your First Ontology. Knowledge Systems Laboratory
32 (01 2001).
[30] Bernardo Pereira Nunes, Alexander Arturo Mera Caraballo, Marco An-
tonio Casanova, Besnik Fetahu, Luiz André P. Paes Leme, and Stefan
Dietze. 2013. Complex Matching of RDF Datatype Properties. In Data-
base and Expert Systems Applications - 24th International Conference,
DEXA 2013, Prague, Czech Republic, August 26-29, 2013. Proceedings,
Part I (Lecture Notes in Computer Science, Vol. 8055) , Hendrik Decker,
Lenka Lhotská, Sebastian Link, Josef Basl, and A Min Tjoa (Eds.).
Springer, 195–208. https://doi.org/10.1007/978-3-642-40285-2_18
[31] Chayan Nuntawong, Chakkrit Snae Namahoot, and Michael Brück-
ner. 2016. A web based cooperation tool for evaluating standardized
curricula using ontology mapping. Lecture Notes in Computer Sci-
ence (including subseries Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics) 9929 LNCS (2016), 172–180. https:
//doi.org/10.1007/978-3-319-46771-9_23
[32] Chayan Nuntawong, Chakkrit Snae Namahoot, and Michael Brückner.
2017. HOME: Hybrid ontology mapping evaluation tool for computer
science curricula. Journal of Telecommunication, Electronic and Com-
puter Engineering 9, 2-3 (2017), 61–65.
[33] Chayan Nuntawong, Chakkrit Snae, and Michael Brückner. 2015. A
Semantic Similarity Assessment Tool for Computer Science Subjects
Using Extended Wu & Palmer’s Algorithm and Ontology. Lecture
Notes in Electrical Engineering 339 (02 2015), 989–996. https://doi.org/
10.1007/978-3-662-46578-3_118
[34] Gerardo Orellana, Marcos Orellana, Victor Saquicela, Fernando Bac-
ulima, and Nelson Piedra. 2018. A text mining methodology to dis-
cover syllabi similarities among higher education institutions. Pro-
ceedings - 3rd International Conference on Information Systems and
Computer Science, INCISCOS 2018 2018-Decem (2018), 261–268. https:
//doi.org/10.1109/INCISCOS.2018.00045
[35] Mark Paulk, Bill Curtis, Mary Chrissis, and Charles Weber. 1993. Ca-
pability Maturity Model for Software, Version 1.1 .
[36] Atish Pawar and Vijay Mago. 2018. Similarity between learning out-
comes from course objectives using semantic analysis, bloom’s taxon-
omy and corpus statistics. arXiv (2018). arXiv:1804.06333
[37] Crystiam Kelle Pereira, Sean Wolfgand Matsui Siqueira,
Bernardo Pereira Nunes, and Stefan Dietze. 2018. Linked Data
in Education: A Survey and a Synthesis of Actual Research and Future
Challenges. IEEE Transactions on Learning Technologies 11, 3 (2018),
400–412. https://doi.org/10.1109/TLT.2017.2787659
[38] Nelson Piedra and Edmundo Tovar Caro. 2018. LOD-CS2013: Multi-
leaming through a semantic representation of IEEE computer science
curricula. IEEE Global Engineering Education Conference, EDUCON
2018-April (2018), 1939–1948. https://doi.org/10.1109/EDUCON.2018.
8363473
[39] Alan L. Rector. 2002. Normalisation of ontology implementations :
Towards modularity , re-use , and maintainability.
[40] Cesar Sanín and Edward Szczerbicki. 2005. Set of experience: a knowl-
edge structure for formal decision events. Foundations of Control and
Management Sciences (2005), 95–113.
[41] Víctor Saquicela, Fernando Baculima, G. Orellana, Nelson Piedra, Mar-
cos Orellana, and M. Espinoza. 2018. Similarity Detection among
Academic Contents through Semantic Technologies and Text Mining.
In IWSW.
[42] Takayuki Sekiya, Yoshitatsu Matsuda, and Kazunori Yamaguchi. 2015.
Curriculum Analysis of CS Departments Based on CS2013 by Simpli-
fied, Supervised LDA. In Proceedings of the Fifth International Confer-
ence on Learning Analytics And Knowledge (Poughkeepsie, New York)
(LAK ’15) . Association for Computing Machinery, New York, NY, USA,
330–339. https://doi.org/10.1145/2723576.2723594
[43] Kristian Stancin, Patrizia Poscic, and Danijela Jaksic. 2020. Ontologies
in education – state of the art. Education and Information Technologies
25, 6 (2020), 5301–5320. https://doi.org/10.1007/s10639-020-10226-z
[44] Adelina Tang and Jason Hoh. 2013. Ontology-specific API for a cur-
ricula management system. 2013 2nd International Conference on E-
Learning and E-Technologies in Education, ICEEE 2013 (2013), 294–297.
https://doi.org/10.1109/ICeLeTE.2013.6644391
[45] Mariela Tapia-Leon, Abdón Carrera Rivera, Janneth Chicaiza, and Ser-
gio Luján-Mora. 2018. Application of ontologies in higher education: A
systematic mapping study. In 2018 IEEE Global Engineering Education
Conference (EDUCON) . 1344–1353. https://doi.org/10.1109/EDUCON.
2018.8363385
[46] Javier Vaquero, Carlos Toro, Juantxu Martín, and Andoni Aregita. 2009.
Semantic Enhancement of the Course Curriculum Design Process. In
Proceedings of the 13th International Conference on Knowledge-Based
and Intelligent Information and Engineering Systems: Part I (Santiago,
Chile) (KES ’09) . Springer-Verlag, Berlin, Heidelberg, 269–276. https:
//doi.org/10.1007/978-3-642-04595-0_33
[47] Yan Wang, Zhao Wang, Xuemei Hu, Tian Bai, Sen Yang, and Lan
Huang. 2019. A Courses Ontology System for Computer Science
Education. 2019 IEEE International Conference on Computer Science
and Educational Informatization, CSEI 2019 3 (2019), 251–254. https:
//doi.org/10.1109/CSEI47661.2019.8938930
[48] Claes Wohlin. 2014. Guidelines for snowballing in systematic literature
studies and a replication in software engineering. ACM International
Conference Proceeding Series (2014). https://doi.org/10.1145/2601248.
2601268
[49] Xiaoyan Yu, Manas Tungare, Weiguo Fan, Manuel Pérez-Quiñones,
Edward A. Fox, William Cameron, and Lillian Cassel. 2007. Using
automatic metadata extraction to build a structured syllabus repository.
Lecture Notes in Computer Science (including subseries Lecture Notes in
Artificial Intelligence and Lecture Notes in Bioinformatics) 4822 LNCS
(2007), 337–346. https://doi.org/10.1007/978-3-540-77094-7_43
6
