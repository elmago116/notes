---
year: "2025"
doi: https://doi.org/10.1145/3715275.3732136
tags:
  - humanities/coproduction
  - tech/Ai
  - themes/ethics
  - design/community_Design
  - humanities/coproduction
title: Distributive Epistemic Injustice in AI Ethics A Co-productionist Account of Global North-South Politics in Knowledge Production
journal: Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency
publisher: ACM
type: article
source: Manual
ORCID: //orcid.org/0000-0002-0053-4657
base: clippings
authors:
  - Kerry McInerney Leverhulme,
  - Abdullah Hasan Safir
  - Alan F. Blackwell
  - Ramit Debnath
apa_citation: Kerry McInerney Leverhulme, et al., 2025
---
[[Distributive Epistemic Injustice in AI Ethics A Co-productionist Account of Global North-South Politics in Knowledge Production.pdf]]

[[Distributive Epistemic Injustice in AI Ethics A Co-productionist Account of Global North-South Politics in Knowledge Production.pdf]]

## PDF text extraction

Distributive Epistemic Injustice in AI Ethics: A Co-productionist
Account of Global North-South Politics in Knowledge Production
Abdullah Hasan Safir
Collective Intelligence & Design Group
University of Cambridge
Cambridge, United Kingdom
sa2168@cam.ac.uk
Kerry McInerney
Leverhulme Centre for the Future of Intelligence
University of Cambridge
Cambridge, United Kingdom
kam83@cam.ac.uk
Alan F. Blackwell
Department of Computer Science and Technology
University of Cambridge
Cambridge, United Kingdom
afb21@cam.ac.uk
Ramit Debnath
Collective Intelligence & Design Group
University of Cambridge
Cambridge, United Kingdom
rd545@cam.ac.uk
Abstract
In this study, we analyse a comprehensive database (from 1960 to
June 2024) of scientific publications in AI Ethics (n= 5755) using
Web of Science (WoS) as a data source, to generate quantitative in-
sights around the research trends within the field. We systematically
curate the initial data to conduct a co-authorship and co-citation
analysis with highly cited research outputs (n = 500) and a co-word
analysis with most relevant research outputs (n = 1000). These
bibliometric analyses result in multiple networked visualisations
that map the status quo and the nature of current citational and
collaborative practices among the experts, institutions and coun-
tries involved in global AI Ethics research. Using Sheila Jasanoff’s
co-production theory as a conceptual lens, we analyse these find-
ings and show that the experts from the Global North currently
legitimise their expertise in AI Ethics through dynamic citational
and collaborative practices in knowledge production within the
field. Collectively, they shape the discourses and institutional ways
of understanding around the ethical development of AI technolo-
gies worldwide. This techno-politics of knowledge-making in AI
Ethics culminates in creating epistemic injustice for the Global
South. Drawing from Miranda Fricker and prominent feminist and
postcolonial theorists, we explain how such injustice is produced
and distributed through patterned pathways of co-production of
AI Ethics. Thus, we show that the global project of AI Ethics fails
to deliver its promise to be universally useful by keeping the global
majority populations in the Southern regions marginalized as ‘oth-
ers’.
CCS Concepts
• Human-centered computing →HCI theory, concepts and
models; • Social and professional topics →Geographic char-
acteristics.
This work is licensed under a Creative Commons Attribution 4.0 International License.
FAccT ’25, Athens, Greece
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1482-5/25/06
https://doi.org/10.1145/3715275.3732136
Keywords
Artificial Intelligence, Ethics, Knowledge Production, Epistemic
Justice, Global South
ACM Reference Format:
Abdullah Hasan Safir, Kerry McInerney, Alan F. Blackwell, and Ramit Deb-
nath. 2025. Distributive Epistemic Injustice in AI Ethics: A Co-productionist
Account of Global North-South Politics in Knowledge Production. In The
2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT
’25), June 23–26, 2025, Athens, Greece. ACM, New York, NY, USA, 16 pages.
https://doi.org/10.1145/3715275.3732136
1 Introduction
AI Ethics has emerged as a scholarly discipline to address the moral
implications and societal impacts of artificial intelligence (AI) tech-
nologies [55]. The field seeks to ensure that AI systems are de-
signed and used in ways that are more ethical [ 73, 99, 109] and
‘human–centred’ [93, 110] by promoting fairness [68], accountabil-
ity [31], transparency [61] and their alignment with international
standards of human rights [ 6]. In this article, we argue that AI
Ethics as a global scientific enterprise is co-producing a new techno-
political order. This techno-politics reconfigures political relations
and power dynamics among actors, including experts, institutions,
and nation states, by using knowledge production as political in-
struments (see [59]). In our study, we try to unfold the geopolitical
power dynamics of AI Ethics as a global project, one that promotes
knowledge and values from the Global North at the expense of the
Global South.
Despite its promise of inclusivity and diversity, AI Ethics falls
short in challenging the epistemological, socio-economic, and cul-
tural frameworks of the Global North [8, 12, 69, 86]. Only a small
percentage of publications in prestigious AI Ethics conferences
and journals discuss the ethical issues raised by AI in non-Western
countries, and even fewer of those appropriately address such cir-
cumstances (for systematic literature reviews of articles published
in conferences: [2, 77]; and for journals, see [49, 75]). This body of
literature uses data and ontologies from the West, presents AI Ethics
as a project to mitigate social injustices prevalent in Western con-
texts, and implicitly presents Western ideals as universal standard
to develop ethical frameworks for AI for the rest of the world [91].
2009


FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
But such Global North-centric ethical approaches are often consid-
ered ineffective, if not harmful, in the Global South, because there
exist various socio-economic and contextual differences between
the North and South and the extent of the ethical risks of AI in these
regions are also very contrasting [79]. Here, we acknowledge the
problems associated with the rhetoric of Global North and South,
stereotypes, assumed homogeneity, and contested definitions of the
terms; but scholars who work on power asymmetries and inequality
in AI continue to use such binary categories as a ‘useful unifier for
building solidarity’ for non-Western or Global South countries [79].
In this article, we follow the tradition and use the term Global South
to broadly indicate the economically underdeveloped and develop-
ing countries that are geographically located on continents other
than Europe and North America. We use this common identity,
as it was built on ‘shared historical experiences of exclusion and
oppression’ [83] and reflect it through knowledge-making politics.
Although the racial and colonial harm of AI has been pointed out
by critical and decolonial AI scholars [3, 7, 15, 74, 75], there is less
literature on how exclusion from the key academic and intellectual
discourse in AI Ethics harms and marginalises populations in the
Global South. Some recent academic conversations highlight how
epistemic injustice shapes or is shaped by AI (see [54, 57, 92, 96]),
but epistemic injustice in the academic field of AI Ethics remains
under-researched to date [10].
To this end, we conducted one of the first holistic assessments of
the current academic practices in AI Ethics. Our contribution adds
to the literature by bridging philosophical concepts and data-driven
analysis, revealing how injustice is evident in citation and collab-
oration patterns within AI Ethics. Using bibliometric approaches,
our empirical study explores the ‘intellectual structure’ (see [39])
of the field. We analysed a comprehensive database (from 1960 to
June 2024) of scientific publications on AI Ethics (n = 5755) using
Web of Science (WoS) as a data source to generate quantitative
insights about research trends within the field. We systematically
curated the initial data to perform a co-authorship and co-citation
analysis with highly cited research results (n = 500) and a co-word
analysis with the most relevant research outputs (n = 1000). These
bibliometric analyses resulted in multiple network visualisations
that map the status quo and the nature of current citational and
collaborative practices among the experts, institutions, and coun-
tries involved in global AI Ethics research. Using Sheila Jasanoff’s
[51, 52] co-production theory as a conceptual lens, we analyse these
findings and show that experts from the Global North currently le-
gitimise their expertise in AI Ethics through dynamic citational and
collaborative practices. Collectively, they shape the discourses and
institutional ways of understanding around the ethical development
of AI technologies worldwide. This techno-politics of knowledge-
making in AI Ethics culminates in creating epistemic injustice for
the Global South stakeholders. Drawing from Miranda Fricker [37]
and prominent feminist and postcolonial theorists, we explain how
such injustices are produced and disseminated through patterned
pathways of AI Ethics’ co-production. We discuss these injustices
as distributive in nature, with disproportionate funding, resources,
expertise, and academic prestige in the field owned by a select num-
ber of institutions in the Global North. Thus, through the lens of
distributive epistemic injustice, we argue that the global AI Ethics
project fails to fulfil its promise to be universally useful by keeping
global majority populations in the southern regions marginalised
as ‘others’.
2 Theoretical Framework
2.1 Co-production as a conceptual lens
We use co-production as a conceptual lens in our work to navi-
gate the complexities of global knowledge-making practices in AI
Ethics. Co-production is a seminal concept in Science and Technol-
ogy Studies (STS), largely theorised by Sheila Jasanoff, who posits
that scientific knowledge and techno-political orders in society are
produced together through interconnected processes. This theori-
sation extends the post-structuralist insight that social structures
are rarely stable, universal, or immutable but are fluid, contingent,
and subject to change. Jasanoff [51] argues that, while science and
society constitute themselves simultaneously, they also interact
with each other. There is a continual negotiation of boundaries
between two, each influencing and stabilising the other. Such ne-
gotiations are political and determine what counts as scientific
knowledge, who is considered and represented as experts, and how
scientific knowledge should be integrated into institutional decision
making [52].
At the same time, societies have collective visions of ‘desirable
futures’, which shape the development and acceptance of sociotech-
nical innovations [52, 53] and guide the direction of scientific fields
through research and development [9]. Diverse actors, including
scientists, policymakers, and the public, come together at shared
spaces or sites to discuss issues that have both techno-scientific
and sociopolitical dimensions and articulate these desirable futures.
Jasanoff suggests four of such crucial sites of co-production in her
framework: identities, institutions, discourses, and representations.
The interaction of science and societies at these sites works as ‘order-
ing instruments’ [52] of co-production. Therefore, examining these
four sites provides critical insights around how knowledge-making
and social or political forces are ordered as well as co-produced:
(1) identities may illuminate how individuals and group of re-
searchers form their identities as experts and how their per-
ceived identities enable them to influence the agendas and
research practices of their scientific fields (see [64])
(2) institutions reveal how scientific knowledge creation is inter-
twined with functional social institutions, such as universi-
ties, and how these institutions and their norms are in turn
shaped by the knowledge they produce (see [48])
(3) discourses illuminate how scientific discourses influence pub-
lic understanding and policy debates, and how their up-
take may impact scientific research agendas within a field
(see [100])
(4) representations show how scientific knowledge development
can be embodied through the presence of large entities such
as countries or states in global politics and their ability to
shape the direction of research agenda through such pres-
ence (see [71])
Jasannoff’s co-production theory perfectly helps us to explore
the interactions that take place at these four sites in the field of AI
Ethics to understand the intricate and dynamic relationships be-
tween knowledge production and the current techno-political order
of the field. However, Jasanoff [51] herself prescribes co-production
2010

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
as an interpretative framework and warns that applying it as a rigid
methodological template will not serve its purpose. Rather, this lens
blends the ‘descriptive richness’ with the ‘explanatory power’ of
scholars by helping them avoid deterministic and straightforward
causal explanations of sociotechnical phenomena. Therefore, co-
production as a non-reductionist approach continues to be applied
in various disciplines beyond STS [13, 47, 80, 98].
2.2 Distributive epistemic injustice as derivative
of co-production of AI Ethics
Miranda Fricker [37] defines epistemic injustice as the wrong done
to someone specifically in their capacity as a knower. She identified
two main forms of epistemic injustice: testimonial and hermeneuti-
cal injustice. Testimonial injustice occurs when the credibility of a
speaker is unfairly deflated and their testimony is wrongly discred-
ited, undervalued, or even dismissed due to prejudice. Hermeneu-
tical injustice occurs when the collective interpretative frame-
works available to society are insufficient to understand certain
marginalised experiences, making it difficult for individuals in such
marginalised groups to comprehend and communicate their own
experiences. While these two are characterised as discriminatory
injustices [20], later she added a third layer, distributive epistemic
injustice, to her conceptualisation, suggesting that it occurs when
epistemic goods (such as education or information) are unfairly
distributed in a society [38]. We particularly find this distributive
aspect crucial in AI Ethics for exploring the extent in which this aca-
demic field is capable of contributing to or mitigating the systemic
and structure inequalities in knowledge production and provid-
ing some tangible entry points for the scientific community and
policymakers to collectively imagine practical solutions to these
issues.
Central to Fricker’s analysis is the relationship between power
and identity. This relationship influences epistemic interactions, of-
ten reinforcing existing power structures that define who is consid-
ered a credible knower and whose knowledge is valued or dismissed
[36]. However, the limit of this theorisation is ironically its inherent
Whiteness. Fricker does not acknowledge the body of work on the
politics of knowledge-making by cultural theorists (such as Stuart
Hall), Black feminist thinkers (such as Patricia Hill Collins) or post-
colonial scholars (such as Frantz Fanon, Edward Said, or Gayatri
Spivak) who critically engaged with the ways in which knowl-
edge production and representation perpetuate power imbalances
and marginalise certain racial groups, colonised subjects, or more
broadly non-Western and Global South populations. They highlight
that the processes in which knowledge is produced, validated, and
disseminated may involve the silencing, misrepresentation, and
marginalisation of knowledge systems, experiences, and identities
of vulnerable groups. These standpoints carry much importance in
relation to epistemic injustice facilitated by the co-production of
AI Ethics.
Drawing from Fricker and other thinkers discussed above, it is
possible to map how epistemic injustice operates across Jasanoff’s
four sites of co-production:
(1) injustice through identities: identities are constructed within
power-laden contexts, meaning that certain groups are con-
sistently discredited or excluded from contributing to col-
lective knowledge [37]; colonial alienation can shape self-
perception and identity, develop inferiority by imposing
coloniser’s language [ 32, 33]; Western intellectuals often
speak for marginalised groups in the Global South rather
than enabling them to speak for themselves [94]
(2) injustice through institutions: epistemic injustice is often in-
stitutional; structural and institutional conditions facilitate
inequitable epistemic practices [37]; Western academic insti-
tutions produce knowledge about other parts of the world
(such as the ‘Orient’ and its stereotyping as exotic, backward,
and irrational) [89]
(3) injustice through discourses: exclusion or ‘outsider within’
status of intellectuals from marginalised communities in
mainstream academic and intellectual discourse can invali-
date their knowledges [24]; voices of marginalised groups
cannot be heard within the structures of power and knowl-
edge [94]
(4) injustice through representations: those who control the
means of representation have significant power in shaping
knowledge; lack of representation can lead to the silencing
of marginalised voices [43] or invalidating and suppressing
non-Western ways of knowing [90]; colonial powers often
represented colonised peoples in ways that justified their
subjugation and denied their agency and knowledge systems
[94]
We thus combine these insights with Jasanoff’s account of co-
production to examine how the field of AI Ethics facilitates epis-
temic injustice.
3 Methods
To map the intellectual structure [ 39] of AI Ethics as a research
domain, we have applied bibliometric methods [21, 22] in this study.
Bibliometrics is a set of statistical methods to study and measure
various aspects of academic publications and other forms of schol-
arly literature [82]. Over the years, this quantitative analysis of
empirical data around scientific publications has become increas-
ingly popular as a means of examining knowledge trends within
a specific field and has been used across a wide range of disci-
plines [29]. Among various bibliometric methods [104], we have
combined institutional and country-wise citational analysis[ 95],
co-authorship analysis [103], co-citation analysis [41, 106] and co-
word analysis [46] to capture the state of academic discourses and
prevailing norms such as citational and co-authorship practices
among the experts, institutions, and countries involved in AI Ethics,
and at the same time, to understand the politics embedded within
such practices.
We collected our data from Web of Science (WoS) which re-
mains reliable bibliometric research as one of the oldest and most
authoritative database of research publications and citations met-
rics [11, 103]. To search within this database, we used ‘AI Ethics’
as the primary keyword to find indexed scholarly outputs in the
field and navigate the citation network between all authors and
their affiliations. In addition, we used secondary keywords such as
2011

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
‘Machine Ethics’, ‘Responsible AI’ and ‘AI Governance’ to broaden
the search, ensuring a thorough exploration of articles, proceeding
articles, review articles, early access articles, editorial materials,
book chapters, book reviews, books, and discussions. Our dataset
covered publications from journals such as AI and Society, Ethics of
Engineering Technology, IEEE Access, Big Data and Society, Nature
Machine Intelligence, Mind and Machines, and other applied fields
such as BMJ Open and Journal of Medical Ethics, and AAAI/ ACM
conferences such as AIES, FAccT, CHI, DIS, ACL, EAAMO, as well
as IEEE and other relevant conferences. The search option in this
platform is automated, comprehensive and selection bias or control
free, primary and secondary keywords are used simultaneously.
The search initially resulted in 5767 research outputs published
within the period spanning from 1960 to 2024 (last search date: 9
June 2024). Later, duplicate records were removed to avoid redun-
dancy, and other inconsistencies of data such as unrelated research
output were removed from search results by carefully checking the
titles and abstracts. This produced a final dataset (dataset one) of
5755 records.
We have used a network visualiser software named VOSviewer
[101] for our analysis. Since the academic publications in the initial
sample were cited more than 68,000 times in total (11.85 average
per item), it was not possible to perform bibliometric analysis and
produce meaningful results using VOSviewer with such a large
dataset. As a cut-off point [67], the top 500 research outputs (dataset
two) were sorted in descending order according to the number of
times they were cited first from the highest. They carried more than
40 percent of total citations of the original dataset. Similarly, for
consistent results in co-word analysis, dataset three was prepared
with the top 1000 research outputs using the ‘relevance’ feature of
the WoS platform. ‘Relevance’ sorts the records in an order based on
a ranking system that considers how many search terms are found
in the titles, abstracts and keywords of the research results [ 19].
Dataset two [88] and Dataset three [87] are available online.
Using dataset two, we constructed networks of research organi-
sations and countries contributing to AI Ethics academic literature.
The analysis focused on citational practice, with 30 organisations
and 31 countries crossing the minimum common citation threshold1
of six documents. We created a network visualisation map showing
how these organisations are connected through mutual citation
practices. Our co-authorship analysis revealed that 49 organisations
had researchers who co-authored at least five AI Ethics-related re-
search outputs, and 21 countries had researchers who produced a
minimum of 10 documents in collaboration. Next, we performed
a co-citation analysis that involves examining how often two doc-
uments are cited together by other subsequent documents [ 95].
We selected ‘cited authors’ as the unit of co-citation analysis in
VOSviewer, with 66 authors crossing the 20 citation threshold. The
authors with the highest total link strengths were visible in the
mapping. Finally, we applied co-word analysis to examine the rela-
tionships between keywords or phrases in AI Ethics [46]. Co-word
analysis measures the strength of the co-occurrence [ 18] of the
terms existing in the dataset. For the current analysis, a minimum
number of occurrences of a particular term within the abstracts of
1For careful threshold selection and understanding the algorithmic approaches behind
clustering in VOSviewer, we consulted existing key literature of bibliometrics [78, 101,
102] and applied those insights in our analysis
the research documents was selected 30 and 166 words crossed this
threshold. The Top 100 terms with high co-occurrence relevance
score were selected for network visualisation. The mapping show-
cases the interconnected thematic composition of the academic
field of AI Ethics. All visualisations were adjusted in terms of their
scale and size to increase clarity of the embedded texts, and later
analysed. The next section highlights these insights.
4 Findings
The following four subsections summarise the findings of our study.
Through the site of identities, institutions, discourses, and rep-
resentations, we examine the patterned pathways by which co-
production of AI Ethics occurs.
4.1 Making identities in AI Ethics: whose
expertise counts?
Jasanoff argues that individual and collective identities are fre-
quently created, contested, or renegotiated through knowledge pro-
duction within a scientific field, while such productions of knowl-
edge contribute to shaping and sustaining these roles of experts,
providing them with epistemic power and significance (see [65]).
Academic practices in AI Ethics, such as co-citation, contribute to
defining who is recognised as an expert and what is considered ex-
pertise in this interdisciplinary field ([58]). Such knowledge-making
practices also stabilise the field by bringing order, standardisation,
and legitimacy to produced knowledge, in this case ethical ap-
proaches to AI.
Figure 1(a) visualises the relationships between highly cited
authors in the field of AI Ethics. Lines connecting the authors rep-
resent co-citations, showing how frequently these authors are cited
together. It displays four clusters, each represented by different
colours (blue, green, red, and yellow), indicating groups of recur-
rently co-cited authors. The connections between authors reflect
shared citations. The density of interconnections is higher within a
cluster, indicating strong intellectual ties and joint research themes.
The high centrality of some of the authors located in the dense,
central parts of each cluster indicates their significant influence.
In general, the presence of multiple clusters in this representative
mapping of academic literature reflects the diverse expertise and
orientations of the scholars to different schools of thought within
the field of AI Ethics.
The presence of such diverse frontiers of knowledge within AI
Ethics is consistent with the interdisciplinary nature of this emerg-
ing interdisciplinary field. This diversity in knowledge-making
practice plays a pivotal role in the formation of identities, defining
who are considered experts and what constitutes their expertise
— linking the individuals or groups to the field’s establishment as
authorities in specific domains. The identities of AI Ethics experts
are co-produced through the recognition of their academic insights
and meaningful contributions to the field by peer acknowledgment
and trust manifested through high counts of citations (see [23]).
The cross-cluster connections visible from the graph indicate
these sub-fields also influence each other, leading to a richer and
more integrated field of study of AI Ethics as a response to mul-
tifaceted problems introduced by AI in society. However, there
2012

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
(a) Network visualisation of co-citation analysis of cited authors
in AI Ethics (generated in VOSviewer), see Fig. 5 in appendix for
full size image
(b) A table showing four frontiers in AI Ethics emerged from the
co-citation analysis
Figure 1: Co-citation practices and emerging frontiers in AI
Ethics
are disconnections on the map as well. We realise there are inher-
ent disagreements over key definitions within the field, although
scholars from diverse disciplines are contributing to knowledge
around the ethical implications of AI from different angles. For
example, computer scientist Margaret Mitchell and philosopher
Nick Bostrom remain very distant from each other, which may
reflect their conflicting opinions in their respective scholarship
on the ethical implications of AI and influencing citation patterns
(for details of these conflicts within the field, see [40]). However,
authors such as Luciano Floridi appear prominently in the centre
and show strong connections with researchers in every cluster,
suggesting a central influence through his foundational work on
the philosophy of information and ethics of AI (for example, [35]).
Thus, experts from different domains play crucial roles in bringing
cohesion in the intellectual landscape of AI Ethics through their
endorsements, critiques, and validations which eventually legit-
imise the knowledge-making process and maintain the stability
and integrity of the academic field.
While this co-citation analysis and mapping helps identify the
key authors and their collaborative networks in AI Ethics, it also
shows the overwhelming presence of Western scholars (findings
in the following sections highlight the institutional and country
affiliations of the researchers). None of the scholars in the map
(Figure 1 (a)) is based in the Global South, including those who are
critical of the Global North-centric establishments in AI. It would be
wrong to assume that AI Ethics as a field should or does not cover
Global South issues and contexts (be it philosophical, computing,
social or legal), or there is a lack of expertise or knowledge-making
capacity in these fields in the Global South; such assumptions, as
seen in Section 2.2, highlight, are rather constructed [90]. Instead,
it implies that it is difficult for scholars in the Global South to be
recognised as experts and achieve legitimacy of their expertise by
navigating through the co-production mechanism of the emerging
field as discussed above. Previous studies in different fields show
that the intrinsic value of an academic work is not the sole factor
determining its citation, as Matthew Effect [ 60] and preferential
attachment [1] add additional value to the published papers that
include prestige of researchers’ institutional affiliations and publi-
cation venues. At the same time, there exists asymmetry in citation
expectations among the academics in the Global North and the
South. Global South scholars are expected to cite Western scholars
to avoid marginalisation and rejection in top journals/venues in the
field, while Global North scholars have no comparable expectation
to engage with Global South scholarship [25].
The following subsections will build on and advance these criti-
cal insights, connecting these experts with institutions (for example,
influential scholars such as Floridi are based in prominent Western
universities such as Oxford) and the prevalence of funding oppor-
tunities in the Global North. In general, this lack of recognition of
scholars from the Global South in the field results in their weaker
identity formation as well as a lack of authority to make decisions
and judgments in shaping the direction of research agendas in AI
Ethics. As Western experts continue to validate and organise the
epistemic structure of the field, it creates an environment in which
the knowledge they produce becomes reliable and replicable. Break-
ing the boundaries of expertise or redefine it becomes impossible
for the Global South scholars (similar politics highlighted in a close
field, HCI: [4]). Thus, the field progresses in a coherent manner, but
by systematically erasing Global South expertise.
4.2 Institutionalisation of AI Ethics
To better understand the mechanisms through which the legitimacy
of new knowledge is established, the lens of institutionalisation is
powerful. A quick analysis of our data shows the distribution of
research outputs in AI Ethics published by institutions worldwide.
We find an unbalanced ratio: among the top 50, four are in Aus-
tralia (Monash University, University of Melbourne, UNSW, and
Australian National University), and two institutions are in Asia
(National University of Singapore and IIT, India). The remaining 44
institutions are either in Europe or in North America and include
universities, the research wings of tech companies such as Microsoft
and IBM, and public research organisations such as the Alan Turing
Institute. There are no institutions in Latin or Central America,
sub-Saharan Africa, or the region of the Middle East and North
Africa (MENA). Although the dominance of Western institutions
in AI Ethics literature shows that these institutions are funding
and prioritising ethics research in AI, reflecting their commitment
to address responsible ways of AI development and deployment,
they are also contributing to structuring ‘institutionalised ways
2013

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
of understanding’ [50]. A subsequent citation analysis (Figure 2
(a)) and a co-authorship analysis (Figure 2 (b)) further clarify the
mechanisms of their intellectual influence.
(a) Network visualisation of citational practices in AI Ethics
among Global Institutions (generated in VOSviewer), see Fig. 6
in appendix for full size image
(b) Network visualisation of co-authorship practices in AI Ethics
among Global Institutions (generated in VOSviewer), see Fig. 7
in appendix for full size image
Figure 2: Citational and co-authorship practices in AI Ethics
is overwhelmingly situated in the Global North
Each node of the network visualisation in Figure 2(a) represents
a different institution, and the size of the node in the map indi-
cates the number of citations that institution has received, with
larger nodes (such as the University of Oxford, the University of
Cambridge, the Alan Turing Institute, Harvard, MIT, and Stanford)
representing institutions that are more frequently cited in the AI
Ethics literature. The lines connecting the nodes represent the cita-
tion relationships between institutions. For example, the University
of Oxford and Alan Turing Institute have the thickest and darkest
lines, which means that researchers at these institutions frequently
refer to each other’s work. Similarly, MIT-Harvard-British Columbia
have stronger citation ties between their AI Ethics research. The
mapping also shows different colours (purple, blue, red, green, and
yellow) representing clusters of institutions that are closely related
in terms of their citation practices. For example, British institutions
including Oxford, Cambridge, Turing and the British Library have
a strong collaborative network through frequent citational inter-
actions, as the map indicates. Institutions with central positions
and extensive connections in each cluster have a broader impact;
for example, within the red cluster, MIT and Harvard researchers
are influencing other institutions. Peripheral institutions (such as
the German Aerospace Centre or Vrije Universiteit Amsterdam)
with fewer connections may have more specialised but less widely
recognised contributions. The network also shows significant in-
terconnections between institutions across different clusters (such
as Oxford-MIT), suggesting cross-Atlantic academic engagement
in AI Ethics.
Figure 2(b), on the other hand, visualises the co-authorship net-
work of institutions involved in global AI Ethics research. Each
node represents an institution like the previous one, but the size of
the node here indicates the volume of co-authored publications in
AI Ethics. The lines connecting the nodes represent co-authorship
links between institutions, with the thickness of the lines indicating
the strength or frequency of collaboration. For example, the map
indicates that researchers from Oxford, Stanford and MIT produce
more collaborative works, and they are also highly interconnected
with multiple other institutions in their efforts. This visualisation,
like the previous one, shows several clusters of nodes, typically
represented by a distinct colour (blue, green, red, yellow, orange,
purple), indicating groups of institutions that frequently collaborate
with each other. This can be due to geographical proximity, similar
research interests, or existing academic partnerships.
However, there is no presence of Global South institutions in
these mappings, and there is only one Asian institution represented:
the National University of Singapore. The distribution of AI Ethics-
related publications, as well as collective citational and collabora-
tive practice across the institutions in the Global North suggest a
significant concentration of contributions from their side to the
field, by showing preferred forms of expertise through citations and
academic collaborations. As repositories of knowledge and power,
Western institutions are bringing order in AI Ethics research, but
at the same time their institutional hegemony reinforces their sta-
tus and influence within the field. Logically, to a Global South
researcher wanting to do cutting-edge research in AI Ethics, in-
stitutions in the Global North regions will seem better equipped
(which can be true), and these institutions inevitably attract top
talents from the South with those researchers having opportunities
to build their identities benefiting from the institutional credibility
and endorsement. This pattern results in ‘brain-drain’ phenomenon
as previously discussed in literature [30] and remain as an structural
barriers towards equity in knowledge production. Even if scholars
are able to do research on Global South issues, their processes of
inquiry are shaped, and the outputs owned by the Global North
institutions — weakening Southern stakes in the institutionalisation
of AI Ethics. As a result, established epistemic norms centred on
the Global North in the field continue to be replicated.
4.3 Discursive space of AI Ethics
In their effort to institutionalise a research field, scientific authori-
ties establish new structures of power through the formulation of
discourses [52], and therefore, this study next looks at the discursive
practices of the AI Ethics academic community.
Figure 3(a) depicts the co-word analysis of academic literature
in AI Ethics which is produced by examining the frequency and
2014

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
(a) Network visualisation of co-word Analysis of academic litera-
ture in AI Ethics (generated in VOSviewer), see Fig. 8 in appendix
for full size image
(b) Different dynamics of discourses in AI Ethics emerged from
the co-word analysis
Figure 3: Co-word analysis in AI Ethics literature and domi-
nant discourses of the field
patterns of co-occurrence of keywords in the paper abstracts. Each
node represents a keyword or term, and the size of the node in
the map indicates the frequency of the term in the literature, with
larger nodes (for example, transparency, fairness, human/ humanity,
future, guideline, governance, participant experience, etc.) repre-
senting more frequently occurring keywords. The lines connecting
the nodes represent co-occurrences of keywords within the research
outputs in the field, while thicker and darker lines indicate stronger
co-occurrence relationships. For example, keywords like fairness,
transparency, lack, and trust are well connected, meaning these
terms are frequently mentioned together. Different colours in the
visualisation represent clusters of terms that are closely related in
the literature; by analysing these clusters, it is possible to construct
some distinct thematic areas within AI Ethics academic discourse.
Figure 3(b) highlights these emerging themes. These discourses
are also consistent with four frontiers in AI Ethics that emerged
from the co-citation analysis: ethical/philosophical, legal, design
and long-term issues. It indicates that experts from their respective
fields repurpose discourses that were already prevalent in their
domain and incorporated them into AI Ethics, thus shaping the
direction of the field.
The visualisation (Figure 3 (a)) also shows interconnections be-
tween different clusters, indicating that these discourses in AI Ethics
developed in highly interrelated ways. For example, governance and
policy discussions (green cluster) are closely linked with fairness
and transparency issues (blue cluster), linking technical knowledge
to practise or action in the field. Terms like machine learning, ethi-
cal principle, trust, science, and researcher appear at the centre of
the map, indicating their cross-cutting roles in shaping the dynamic
nature of the evolving discourses in AI Ethics.
While the co-word analysis visualisation provides an overview
of the key thematic discourses and their interconnections within
AI Ethics literature, they also show that there is no strong presence
of issues that are particularly or uniquely relevant to the Global
South in this discursive landscape. Drawing from findings in the
previous subsections, the absence can be explained by the fact that
these current discourses are heavily influenced by the Global North
stakeholders through their preference for expertise and institutional
mechanisms. Important critical AI issues relevant to Global South
regions, such as data and AI colonialism [26, 44], imperialism [97],
data sovereignty [85], extractivism [27], labour exploitation [108],
AI’s detrimental environmental impact [62], AI for low resource lan-
guages [76] and/or culturally sensitive design [72, 86] are currently
under-represented or overlooked as ethical blind spots in the global
discursive space of AI Ethics. Conducting occasional research on
these issues will not be enough; they need to be mainstreamed to
shift the direction of the current dominant Global North-centric
discourses.
4.4 Crisis of representation in AI Ethics
Although representation has varied meanings, in this case, the
lens is specifically used to explore the interplay between national
contexts of different countries and the production of academic
knowledge in AI Ethics and to understand how it contributes to
global scientific progress of the field as well as international poli-
tics. National priorities, economic interests, political environments,
and cultural values shape scientific research [34], while scientific
achievements, collaborations, and contributions to knowledge mak-
ing influence national identities and international standing [28]. In
linking to the findings in the previous subsections, countries are
represented in the global network of AI Ethics research through
their knowledge contributions facilitated by expert researchers and
institutions. The participation and visibility of countries are further
explored in the following two network visualisations in terms of
their influence on global academic agendas of the field.
The visualisation of the network in Figure 4 (a) helps to under-
stand the relationships and influence patterns between different
countries of the world in AI Ethics literature based on their cita-
tional interactions. Each node on the map represents a country,
while the size of the node indicates the number of citations the
researcher in that country has received, with the largest nodes rep-
resenting countries with the highest total citation counts. For ex-
ample, countries such as England, Germany, and the United States
have large nodes and numerous connections, highlighting their
substantial influence in knowledge-making in the field. The lines
connecting the nodes represent the citation relationships between
countries. Thicker and darker lines (for example, England-Germany
and USA-Canada) indicate stronger citation ties, meaning that re-
searchers from these countries frequently cite each other’s work.
Like previous visualisations, this mapping also shows different re-
gional clusters of countries who are highly interactive through their
citational practices. However, strong inter-cluster interconnections
2015

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
(a) Network visualisation of citational practices in AI Ethics
among countries worldwide (generated in VOSviewer), see Fig. 9
in appendix for full size image
(b) Network visualisation of co-authorship practices in AI Ethics
among countries worldwide (generated in VOSviewer), see Fig. 10
in appendix for full size image
Figure 4: Global North countries remain at the centre within
citational and co-authorship practices in AI Ethics
are visible between the USA, Australia, England, and other Euro-
pean countries, indicating the central roles of the researchers of
these countries in shaping the field of AI Ethics.
Similarly, Figure 4 (b) visualises the collaborative relationships
in AI Ethics among countries worldwide through co-authorship
practices. In this case, the size of the node indicates the number
of co-authored publications from that country, with larger nodes
(such as USA, England, Germany, etc.) representing countries with
a higher number of co-authorship in AI Ethics literature. Thicker
and darker lines (for example, England-Germany) indicate stronger
co-authorship ties, meaning that researchers from these countries
frequently collaborate on their publications in the field. From the
clustering feature, it is also visible that European countries (red
cluster) that include England, Germany, Netherlands, Belgium, and
Switzerland are showing strong interconnections, suggesting fre-
quent co-authorship and collaboration among these countries.
However, unlike other visualisations in this study, some non-
Western countries are visible in these two networks, but in almost
all cases they remain in the periphery, indicating their weaker
positions both in terms of citational and co-authorship practices.
Figure 4(a) shows that while the works of Chinese researchers are
somewhat frequently cited by others in the field, researchers from
countries such as India and Brazil cite European or North Ameri-
can researchers in their publications without strong reciprocation.
Similarly, these two countries are also present as small nodes in
the periphery of Figure 4 (b), indicating that collaborations are of-
fered to them from the central, leading countries of the map, which
are located in the Global North. Weaker representations of Global
South countries in the international collaborative network of AI
Ethics reflect their compromised capacities and participation in
shaping the field’s direction and knowledge production. Countries
in the Global North, on the other hand, leverage stronger scientific
collaborations by pooling resources and sharing expertise from
all over the world. Such scientific efforts cultivate a global com-
munity of practice and international cooperation to facilitate the
harmonisation of standards and practices for AI, thus preventing
regulatory arbitrage and ensuring consistent protection of rights
across borders [105]. The Northern actors gain an upper hand in
scientific diplomacy that enhances the soft power to regulate AI on
a global scale [56].
The findings outlined in these four subsections discuss the cur-
rent directions in AI Ethics research and demonstrate that top
names, institutions and countries in the Global North become the
centre of knowledge production by gaining more citations in the
field. Thus, the experts from these regions gain credibility and
recognition for the knowledge they produce in the field, and their
institutional and national representations influence the dominant
discourses of the field. The patterned pathways of co-production of
global AI Ethics project results in epistemic injustice for the Global
South. The nature of such epistemic injustice and its implications
will be discussed in the next section.
5 Discussion
5.1 Distributive epistemic injustice in/of AI
Ethics
Our study demonstrates the politics of knowledge-making in AI
Ethics in four sites: identities, institutions, discourses, and represen-
tations. It shows that the Global North actors currently bring order,
stabilise and control the trajectories, and thereby, own the means
of co-production of AI Ethics. Our citational, co-citational, and
co-authorship analysis of the field reveals that prominent Global
North figures are shaping the intellectual landscape of AI Ethics by
establishing themselves as authoritative knowers, with academic
institutions in Europe and North America setting the standards and
norms for ethical AI research and practice, often directly shaping
national or global policies (see [5]). We also show that AI Ethics
is being shaped through discursive practices with interrelated and
mutually reinforcing technical, legal, and philosophical themes.
However, the dominance of Global North-based experts and in-
stitutions reinforces their epistemic power, peer influence, and
institutional hegemony in the field [107]. These mechanisms con-
tribute to disproportionate country-level representations in the
global collaborative network of knowledge-making in AI Ethics,
making the field geographically concentrated in the Global North,
leading to an uneven distribution of knowledge production, and
creating epistemic injustice by perpetuating the existing power
2016

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
imbalances around knowledge and expertise between the Global
North and South.
Global South scholarship on AI Ethics is often sidelined in favour
of Global North alternatives on similar ethical and societal impli-
cations around AI. Researchers from these regions, with current
their ‘outsider within’ [24] status, struggle to meaningfully partici-
pate in the mainstream academic and intellectual discourses of AI
Ethics as credible knowers due to a lack of funding, recognition,
and collaboration with institutions and researchers in the Global
North. The field continues to overlook critical ethical concerns per-
tinent to the Global South, such as community-centric values [84],
local notions of privacy [ 8], and indigenous knowledge systems
[63]. If institutional and expertise gaps are not addressed, this cycle
of under-representation in discourse making will continue. The
implications of this are double-layered for the Global South’s AI
futures. First, Global South stakeholders may end up receiving ill-
suited AI technologies that can exacerbate existing techno-political
inequalities [17]. Second, global policy and governance frameworks
predominantly informed by Northern AI Ethics scholarship may
establish standards that could be irrelevant or difficult to implement
within Southern societies, creating regulatory gaps and leading to
poor ethical oversight of such technologies in these regions [79].
In addition, when Southern countries adopt Global North-centric
AI Ethics policies, it can lead to social resistance, mistrust in AI,
and political tensions [66]. Here, we would also like to highlight
Frickerian hermeneutic injustice alongside distributive nature of
such patterns. The collective interpretive frameworks developed
in the Global North can appear insufficient in the Global South in
many cases, as Southern researchers highlights, making it difficult
for marginalised groups to comprehend and communicate their ex-
periences. As community of practitioners of ethics, they often end
up questioning AI policies or applications, but become unable to
express their concerns due to geopolitical and cultural hegemony.
Thus, the Global South as an inferior ‘other’, marginalised within
the knowledge-making project of AI Ethics, is forced to accept the
knowledge of the West (see [32, 94]). While ‘othering’ by techno-
scientific knowledge systems (see [14]) is not new, it is even more
problematic in the field of AI Ethics, given that the field is explicitly
packaged as ‘ethical’. Western dominant experts and institutions
often produce distorted representations for their Southern ‘others’
— by excluding them, and in addition, determining what is ethical
for them or not — to justify their dominance (see [43]), and in doing
so, marginalise the epistemologies of these groups (see [24]) and
their ‘non-Western ways of knowing’ (see [90]). AI Ethics, therefore,
is not ethical enough, unless it takes care of its problem of epistemic
injustice.
5.2 Aligning academic practices in AI Ethics
towards Justice for the Global South
Our study shows that inequitable epistemic practices in AI Ethics
are facilitated by structural and institutional conditions [37]. The
systemic lack of researchers in the field representing Global South
countries is power-laden, since Global North actors control the
means of representation [43]. Addressing the disparities around
the contributions from the institutions in the Global South could
be addressed by concerted efforts to support and empower those
institutions [42, 81, 107]. For example, institutions in the Global
North could support Global South institutions by fostering cross-
regional collaborations. However, the current global co-authorship
network mapping in our study fails to visualise convincing pres-
ence of academic institutions beyond Western countries. Similarly,
the peripheral positions of Global South countries such as India
and Brazil in country-level mapping indicate the weaker roles of re-
searchers from these countries in the global collaborative academic
network in AI Ethics.
Southern actors’ low participation in citational practices is often
attributed to weaker institutional capacity and inequitable resource
allocation in global knowledge production, hindering their ability
to produce quality academic works and eventually contribute to
ethical AI efforts. One quick analysis in our study shows that the
majority of top funding agencies for AI Ethics research are located
in the Global North, particularly in North America and Europe (We
found only one Chinese organisation among the ten top funders
contributing to the high number of publications in the field). This
concentration co-relates to the availability of resources, infrastruc-
ture, and established research institutions in these regions, and
contrarily, can lead to an imbalance in research contributions from
the Southern institutions in AI Ethics literature.
Some decolonial AI scholars question whether AI as a field can
ever be decolonised because it depends on and was made possi-
ble by the logics of coloniality [ 3]. Others, however, continue to
demand non-Western perspectives from the margins, edges, or pe-
ripheries of the racial global system (see [7, 70, 74]). In this article,
we extend these viewpoints, but for the field of AI Ethics — for
bringing more knowledge and power from ‘below’ (see [ 16, 45])
and promote greater inclusivity and equity — integrating under-
represented perspectives into the mainstream ethical discourses
around AI, particularly those from the Global South. Plural epis-
temologies, unique sociotechnical contexts and political realities
can inform more context-sensitive and effective ethical guidelines
for AI. Such efforts have profound implications, especially for the
design, development and deployment of AI technologies in a non-
exclusionary way in the near and longer term.
While we understand the necessity of more empirical, on-the-
ground studies examining the specific ethical issues faced by differ-
ent regions and communities in the world, our research captures
the structural and systemic hurdles for it. These, in turn, show
some key entry-points for equitable and global collaborative efforts
to decentralise the AI Ethics academic project: making identities,
institutions, discourses, and representations for the Global South
in the field. We should not explicitly assume that Global South
approaches in AI Ethics will be inherently pro-justice, the political
realities may not enable the Global South actors to challenge and
dismantle prejudices that undermine the credibility and desirable
recognition of their knowledge systems and experiences. Rather,
investment in building epistemic capacities of Southern experts and
research institutions through funding and infrastructural support,
promoting equity in cross-regional collaborations in the field, and
creating platforms that amplify their diverse voices can be a practi-
cal way forward. Future research can focus on the mechanisms of
such equitable approaches to AI Ethics, by deeply looking at the
instruments highlighted in this research.
2017

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
6 Limitations
Our data for this study were collected from the WoS platform. While
this is one of the most comprehensive databases available, it might
exclude some venues and journals in the field (for top categories of
academic fields and venues represented in our dataset, see figure 11
and 12 in the appendix). In most cases, the excluded journals in WoS
are not indexed, where researchers from the Global South countries
may publish their research. However, not being indexed reduces the
chances of papers to be cited, which itself is part of the citational pol-
itics. Co-citation and co-word analysis was conducted with subsets
(respectively dataset two: highly cited research outputs, n = 500 and
dataset three most relevant research outputs, n = 1000) of the main
dataset. These Ns are kept different for meaningful visualisations in
VOSviewer based on the statistical parameters such as modularity
co-efficient and relevance score. While the methods used in the
empirical study are helpful to generate quantitative insights on
research trends, influential authors etc. based on the number of
publications, citations, and co-authorships etc., they only become
meaningful if properly analysed. In many cases, bibliometric meth-
ods are used by generalists or method experts, who can only discuss
an academic field’s publishing patterns and general understandings,
without critical and extensive engagements of the very field ([111].
With these limitations in mind, in this research such methods have
been used carefully and in a complementary way, by focusing on
the qualitative depth of the analysis, for example, not looking at
what, who, or what percentage, rather emphasising on why, how,
and so what. The interpretations of the quantitative results were
also offered carefully. For example, while institutional mapping can
indicate high presence of Global North institutions, there can be
researchers from the Global South producing research within such
institutions, but this movement of researchers away from the South
is part of what contributes to the Southern research institutions
being under-represented (we discuss this on section 4.2). In this
context, we realise a necessity of a positionality statement indicat-
ing how our own positionalities as researchers have informed this
research. All four researchers of this study are currently based at an
elite university in the United Kingdom, although they come from
different countries such as Bangladesh, India and New Zealand.
7 Conclusion
Drawing from a comprehensive empirical study, in this paper, we
show that the actors in the Global North currently own the means
of knowledge production with their dominant representations in
AI Ethics. The Northern experts interact collaboratively, institution-
alise knowledge practices, and by doing so, they bring an apparent
stability to the field, but end up shaping the discourses and even-
tually the global ways of understanding around what ethical AI
could and should look like. Since the control of the trajectories of
AI Ethics belong to the West, we contend that this global project
facilitates and distributes epistemic injustice through the patterned
pathways of its co-production. We also discuss the implications, ar-
guing that such epistemic injustice perpetuates the existing power
disparity among the Northern and Southern actors, and so the po-
litical purpose of AI Ethics to ensure universal social good through
harmonious human-AI coexistence fails to deliver. The Global South
remains as an inferior ‘other’ of the AI Ethics project with their
weaker representation and influence. We suggest that identities,
institutions, discourses and representations can be critical site of
interventions to ensure Global South voices and concerns to be
meaningfully heard and valued within this unequal power dynam-
ics.
Acknowledgments
This work builds on the MPhil Dissertation work of the first author.
He acknowledges the generous funding he received from his college
Trinity Hall that made his MPhil in Ethics of AI, Data and Algorithm
possible at the Leverhulme Centre for the Future of Intelligence,
University of Cambridge.
References
[1] Alireza Abbasi, Liaquat Hossain, and Loet Leydesdorff. 2012. Betweenness
centrality as a driver of preferential attachment in the evolution of research
collaboration networks. Journal of informetrics 6, 3 (2012), 403–412.
[2] Amina A Abdu, Irene V Pasquetto, and Abigail Z Jacobs. 2023. An empirical
analysis of racial categories in the algorithmic fairness literature. In Proceedings
of the 2023 ACM Conference on Fairness, Accountability, and Transparency . 1324–
1333.
[3] Rachel Adams. 2021. Can artificial intelligence be decolonized? Interdisciplinary
Science Reviews 46, 1-2 (2021), 176–197.
[4] Syed Ishtiaque Ahmed, Sareeta Amrute, Jeffrey Bardzell, Shaowen Bardzell,
Nicola Bidwell, Tawanna Dillahunt, Sane Gaytán, Naveena Karusala, Neha
Kumar, Rigoberto Lara Guzmán, et al. 2022. Citational justice and the politics
of knowledge production. interactions 29, 5 (2022), 78–82.
[5] Mhairi Aitken, David Leslie, Florian Ostmann, Jacob Pratt, Helen Margetts, and
Cosmina Dorobantu. 2022. Common regulatory capacity for AI.The Alan Turing
Institute (2022).
[6] Evgeni Aizenberg and Jeroen Van Den Hoven. 2020. Designing for human rights
in AI. Big Data & Society 7, 2 (2020), 2053951720949566.
[7] M. Ali. 2014. Towards a decolonial computing. In Ambiguous Technologies:
Philosophical Issues, Practical Solutions, Human Nature . International Society of
Ethics and Information Technology, 28–35.
[8] Payal Arora. 2019. Decolonizing privacy studies. Television & New Media 20, 4
(2019), 366–378.
[9] Silke Beck, Sheila Jasanoff, Andy Stirling, and Christine Polzin. 2021. The
governance of sociotechnical transformations to sustainability. Current Opinion
in Environmental Sustainability 49 (2021), 143–152.
[10] Abeba Birhane, Elayne Ruane, Thomas Laurent, Matthew S. Brown, Johnathan
Flowers, Anthony Ventresque, and Christopher L. Dancy. 2022. The forgotten
margins of AI ethics. In Proceedings of the 2022 ACM Conference on Fairness,
Accountability, and Transparency . 948–958.
[11] Caroline Birkle, David A Pendlebury, Joshua Schnell, and Jonathan Adams. 2020.
Web of Science as a data source for research on scientific and scholarly activity.
Quantitative Science Studies 1, 1 (2020), 363–376.
[12] Alan F Blackwell, Addisu Damena, and Tesfa Tegegne. 2021. Inventing artificial
intelligence in Ethiopia. Interdisciplinary Science Reviews 46, 3 (2021), 363–385.
[13] Scott Bremer and Simon Meisch. 2017. Co-production in climate change re-
search: reviewing different perspectives.Wiley Interdisciplinary Reviews: Climate
Change 8, 6 (2017), e482.
[14] Santiago Castro-Gómez. 2019. The Social Sciences, Epistemic Violence, and the
Problem of the" Invention of the Other". In Unbecoming Modern . Routledge,
211–227.
[15] Stephen Cave. 2020. The problem with intelligence: its value-laden history and
the future of AI. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and
Society. 29–35.
[16] Dipesh Chakrabarty. 2000. Subaltern studies and postcolonial historiography.
Nepantla: views from South 1, 1 (2000), 9–32.
[17] Alan Chan, Chinasa T Okolo, Zachary Terner, and Angelina Wang. 2021. The
limits of global inclusion in AI development. arXiv preprint arXiv:2102.01265
(2021).
[18] Xiuwen Chen, Jianming Chen, Dengsheng Wu, Yongjia Xie, and Jing Li. 2016.
Mapping the research trends by co-word analysis based on keywords from
funded project. Procedia computer science 91 (2016), 547–555.
[19] Clarivate. 2022. Web of Science: Sort options for search results. https://
clarivate.com/web-of-science-sort-options Accessed: 2025-01-11.
[20] David Coady. 2017. Epistemic injustice as distributive injustice 1. In The
Routledge handbook of epistemic injustice . Routledge, 61–68.
[21] Manuel J Cobo, Antonio Gabriel López-Herrera, Enrique Herrera-Viedma, and
Francisco Herrera. 2011. An approach for detecting, quantifying, and visualizing
2018

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
the evolution of a research field: A practical application to the Fuzzy Sets Theory
field. Journal of informetrics 5, 1 (2011), 146–166.
[22] Manuel J Cobo, Maria Angeles Martínez, María Gutiérrez-Salcedo, Hamido
Fujita, and Enrique Herrera-Viedma. 2015. 25 years at knowledge-based systems:
a bibliometric analysis. Knowledge-based systems 80 (2015), 3–13.
[23] Citational Justice Collective, Gabriela Molina León, Lynn Kirabo, Marisol Wong-
Villacres, Naveena Karusala, Neha Kumar, Nicola Bidwell, Pedro Reynolds-
Cuéllar, Pranjal Protim Borah, Radhika Garg, et al. 2021. Following the trail
of citational justice: critically examining knowledge production in HCI. In
Companion Publication of the 2021 Conference on Computer Supported Cooperative
Work and Social Computing . 360–363.
[24] Patricia Hill Collins. 2022. Black Feminist Thought: Knowledge, Consciousness,
and the Politics of Empowerment . Routledge.
[25] Fran M Collyer. 2018. Global patterns in the publishing of academic knowledge:
Global North, global South. Current Sociology 66, 1 (2018), 56–73.
[26] Nick Couldry and Ulises A Mejias. 2019. Data colonialism: Rethinking big
data’s relation to the contemporary subject. Television & New Media 20, 4 (2019),
336–349.
[27] Kate Crawford. 2021. The Atlas of AI: Power, Politics, and the Planetary Costs
of Artificial Intelligence.
[28] Sarah R Davies and Maja Horst. 2016. Science communication: Culture, identity
and citizenship . Springer.
[29] Nicola De Bellis. 2009.Bibliometrics and citation analysis: from the science citation
index to cybermetrics . scarecrow press.
[30] Frédéric Docquier. 2006. Brain drain and inequality across nations.International
Journal on Multicultural Societies (2006).
[31] Finale Doshi-Velez, Mason Kortz, Ryan Budish, Chris Bavitz, Sam Gershman,
David O’Brien, Kate Scott, Stuart Schieber, James Waldo, David Weinberger,
et al. 2017. Accountability of AI under the law: The role of explanation. arXiv
preprint arXiv:1711.01134 (2017).
[32] Frantz Fanon. 1952. Black Skin, White Masks . Grove Press.
[33] Frantz Fanon. 1963. The Wretched of the Earth . Grove Press.
[34] Martha Finnemore. 1996. National interests in international society . Cornell
University Press.
[35] Luciano Floridi and Massimo Chiriatti. 2020. GPT-3: Its nature, scope, limits,
and consequences. Minds and Machines 30 (2020), 681–694.
[36] Miranda Fricker. 1998. Rational authority and social power: Towards a truly
social epistemology. In Proceedings of the Aristotelian Society . JSTOR, 159–177.
[37] Miranda Fricker. 2007. Epistemic injustice: Power and the ethics of knowing .
Oxford University Press.
[38] Miranda Fricker. 2013. Epistemic justice as a condition of political freedom?
Synthese 190 (2013), 1317–1332.
[39] Floriana Fusco, Marta Marsilio, and Chiara Guglielmetti. 2020. Co-production
in health policy and management: a comprehensive bibliometric review. BMC
health services research 20 (2020), 1–16.
[40] Timnit Gebru and Émile P Torres. 2024. The TESCREAL bundle: Eugenics
and the promise of utopia through artificial general intelligence. First Monday
(2024).
[41] Jonathan Grant, Robert Cottrell, Françoise Cluzeau, and Gail Fawcett. 2000. Eval-
uating “payback” on biomedical research from papers cited in clinical guidelines:
applied bibliometric study. Bmj 320, 7242 (2000), 1107–1111.
[42] Carolina Guzmán-Valenzuela. 2019. Values and the international collaborative
research in higher education: Negotiating epistemic power between the Global
South and the Global North. Values of the University in a Time of Uncertainty
(2019), 137–153.
[43] Stuart Hall et al . 1997. The spectacle of the other. Representation: Cultural
representations and signifying practices 7 (1997).
[44] Karen Hao. 2022. Artificial intelligence is creating a new colonial world order.
MIT Technology Review (April 19 2022). https://www .technologyreview.com/
2022/04/19/1049592/artificial-intelligence-colonialism/ Accessed: 2025-01-11.
[45] Sandra Harding. 2008. Sciences from below: Feminisms, postcolonialities, and
modernities. Duke University Press.
[46] Qin He. 1999. Knowledge discovery through co-word analysis. (1999).
[47] Vaughan Higgins, Melanie Bryant, Andrea Howell, and Jane Battersby. 2017. Or-
dering adoption: Materiality, knowledge and farmer engagement with precision
agriculture technologies. Journal of Rural Studies 55 (2017), 193–202.
[48] Stephen Hilgartner. 2004. Mapping systems and moral order: Constituting
property in genome laboratories. In States of Knowledge . Routledge, 131–141.
[49] Soraj Hongladarom and Jerd Bandasak. 2024. Non-Western AI ethics guidelines:
Implications for intercultural ethics of technology. Ai & Society 39, 4 (2024),
2019–2032.
[50] Sheila Jasanoff. 2001. Image and Imagination: The Emergence of Global Envi-
ronmental Consciousness. In Changing the Atmosphere: Expert Knowledge and
Global Environmental Governance , Clark A. Miller and Paul N. Edwards (Eds.).
MIT Press, Cambridge, MA.
[51] Sheila Jasanoff. 2004. The idiom of co-production. In States of knowledge .
Routledge, 1–12.
[52] Sheila Jasanoff. 2004. Ordering knowledge, ordering society. In States of knowl-
edge. Routledge, 13–45.
[53] Sheila Jasanoff. 2015. Future imperfect: Science, technology, and the imagina-
tions of modernity. Dreamscapes of modernity: Sociotechnical imaginaries and
the fabrication of power (2015), 1–33.
[54] Jackie Kay, Atoosa Kasirzadeh, and Shakir Mohamed. 2024. Epistemic injustice
in generative ai. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and
Society, Vol. 7. 684–697.
[55] Emre Kazim and Adriano Soares Koshiyama. 2021. A high-level overview of AI
ethics. Patterns 2, 9 (2021).
[56] Jane Knight. 2022. Analysing Knowledge Diplomacy and Differentiating It from
Soft Power and Cultural, Science, Education and Public Diplomacies. The Hague
Journal of Diplomacy 18, 4 (2022), 654–686.
[57] Angelie Kraft and Eloïse Soulier. 2024. Knowledge-Enhanced Language Mod-
els Are Not Bias-Proof: Situated Knowledge and Epistemic Injustice in AI. In
Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Trans-
parency. 1433–1445.
[58] Neha Kumar and Naveena Karusala. 2021. Braving citational justice in human-
computer interaction. InExtended Abstracts of the 2021 CHI Conference on Human
Factors in Computing Systems . 1–9.
[59] Can Kurban, Ismael Peña-López, and María Haberer. 2017. What is technopol-
itics? A conceptual schema for understanding politics in the digital age. IDP.
Revista de Internet, Derecho y Política 24 (2017), 3–20.
[60] Vincent Larivière and Yves Gingras. 2010. The impact factor’s Matthew Effect:
A natural experiment in bibliometrics. Journal of the American society for
information science and technology 61, 2 (2010), 424–427.
[61] Stefan Larsson and Fredrik Heintz. 2020. Transparency in artificial intelligence.
Internet policy review 9, 2 (2020), 1–16.
[62] Sebastián Lehuedé. 2024. An elemental ethics for artificial intelligence: water
as resistance within AI’s value chain. AI & SOCIETY (2024), 1–14.
[63] Jason Edward Lewis, Angie Abdilla, Noelani Arista, Kaipulaumakaniolono Baker,
Scott Benesiinaabandan, Michelle Brown, Melanie Cheung, Meredith Coleman,
Ashley Cordes, Joel Davison, et al . 2020. Indigenous protocol and artificial
intelligence position paper. (2020).
[64] Michael Lynch. 2004. Circumscribing Expertise: membership categories in
courtroom testimony. In States of Knowledge . Routledge, 161–180.
[65] Bruce Macfarlane. 2011. Professors as intellectual leaders: Formation, identity
and role. Studies in Higher Education 36, 1 (2011), 57–73.
[66] Mirca Madianou. 2021. Nonhuman humanitarianism: when’AI for good’can be
harmful. Information, Communication & Society 24, 6 (2021), 850–868.
[67] Katherine W McCain. 1990. Mapping authors in intellectual space: A technical
overview. Journal of the American Society for Information Science (1986-1998) 41,
6 (1990), 433.
[68] Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram
Galstyan. 2021. A survey on bias and fairness in machine learning. ACM
computing surveys (CSUR) 54, 6 (2021), 1–35.
[69] Milagros Miceli, Martin Schuessler, and Tianling Yang. 2020. Between subjec-
tivity and imposition: Power dynamics in data annotation for computer vision.
Proceedings of the ACM on Human-Computer Interaction 4, CSCW2 (2020), 1–25.
[70] Stefania Milan and Emiliano Treré. 2019. Big data from the South (s): Beyond
data universalism. Television & New Media 20, 4 (2019), 319–335.
[71] Clark A Miller. 2004. Climate science and the making of a global political order.
In States of knowledge . Routledge, 46–66.
[72] Nusrat Jahan Mim, Dipannita Nandi, Sadaf Sumyia Khan, Arundhuti Dey, and
Syed Ishtiaque Ahmed. 2024. In-Between Visuals and Visible: The Impacts
of Text-to-Image Generative AI Tools on Digital Image-making Practices in
the Global South. In Proceedings of the CHI Conference on Human Factors in
Computing Systems . 1–18.
[73] Brent Mittelstadt. 2019. Principles alone cannot guarantee ethical AI. Nature
machine intelligence 1, 11 (2019), 501–507.
[74] Shakir Mohamed, Marie-Therese Png, and William Isaac. 2020. Decolonial AI:
Decolonial theory as sociotechnical foresight in artificial intelligence.Philosophy
& Technology 33 (2020), 659–684.
[75] James Muldoon and Boxi A Wu. 2023. Artificial intelligence in the colonial
matrix of power. Philosophy & Technology 36, 4 (2023), 80.
[76] Tolúlopé Ògúnrèmí, Wilhelmina Onyothi Nekoto, and Saron Samuel. 2023. De-
colonizing nlp for “low-resource languages”: Applying abebe birhane’s relational
ethics. GRACE: Global Review of AI Community Ethics 1, 1 (2023).
[77] Anaelia Ovalle, Arjun Subramonian, Vagrant Gautam, Gilbert Gee, and Kai-Wei
Chang. 2023. Factoring the matrix of domination: A critical review and reimagi-
nation of intersectionality in ai fairness. In Proceedings of the 2023 AAAI/ACM
Conference on AI, Ethics, and Society . 496–511.
[78] Antonio Perianes-Rodriguez, Ludo Waltman, and Nees Jan Van Eck. 2016. Con-
structing bibliometric networks: A comparison between full and fractional
counting. Journal of informetrics 10, 4 (2016), 1178–1195.
[79] Marie-Therese Png. 2022. At the tensions of south and north: Critical roles of
global south stakeholders in AI governance. In Proceedings of the 2022 ACM
2019

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Conference on Fairness, Accountability, and Transparency . 1434–1445.
[80] Christian Pohl, Stephan Rist, Anne Zimmermann, Patricia Fry, Ghana S Gurung,
Flurina Schneider, Chinwe Ifejika Speranza, Boniface Kiteme, Sébastian Boillat,
Elvira Serrano, et al . 2010. Researchers’ roles in knowledge co-production:
experience from sustainability research in Kenya, Switzerland, Bolivia and
Nepal. Science and public policy 37, 4 (2010), 267–281.
[81] Bridget Pratt and Jantina De Vries. 2023. Where is knowledge from the global
South? An account of epistemic justice for a global bioethics. Journal of medical
ethics 49, 5 (2023), 325–334.
[82] Alan Pritchard. 1969. Statistical bibliography or bibliometrics. Journal of
documentation 25 (1969), 348.
[83] Miriam Prys-Hansen. 2023. The global south: a problematic term. Internationale
Politik Quarterly (2023).
[84] Rida Qadri, Renee Shelby, Cynthia L Bennett, and Emily Denton. 2023. AI’s
regimes of representation: A community-centered study of text-to-image models
in South Asia. In Proceedings of the 2023 ACM Conference on Fairness, Account-
ability, and Transparency . 506–517.
[85] Stephanie Carroll Rainie, Tahu Kukutai, Maggie Walter, Oscar Luis Figueroa-
Rodríguez, Jennifer Walker, and Per Axelsson. 2019. Indigenous data sovereignty.
(2019).
[86] Mohammad Rashidujjaman Rifat, Abdullah Hasan Safir, Sourav Saha, Ja-
hedul Alam Junaed, Maryam Saleki, Mohammad Ruhul Amin, and Syed Ishtiaque
Ahmed. 2024. Data, Annotation, and Meaning-Making: The Politics of Cate-
gorization in Annotating a Dataset of Faith-based Communal Violence. In The
2024 ACM Conference on Fairness, Accountability, and Transparency . 2148–2156.
[87] Abdullah Hasan Safir. 2025. Dataset three. https://doi .org/10.6084/
m9.figshare.29045321. Accessed: 2025-05-13.
[88] Abdullah Hasan Safir. 2025. Dataset two. https://doi .org/10.6084/
m9.figshare.29045270. Accessed: 2025-05-13.
[89] Edward Said. 1978. Orientalism. Pantheon Books.
[90] Edward Said. 1993. Culture and Imperialism . Chatto & Windus.
[91] Nithya Sambasivan, Shivani Kapania, Hannah Highfill, Diana Akrong, Praveen
Paritosh, and Lora M Aroyo. 2021. “Everyone wants to do the model work, not
the data work”: Data Cascades in High-Stakes AI. In proceedings of the 2021 CHI
Conference on Human Factors in Computing Systems . 1–15.
[92] Martina Sardelli. 2022. Epistemic Injustice in the Age of AI. Aporia 22 (2022),
44–53.
[93] Ben Shneiderman. 2022. Human-centered AI . Oxford University Press.
[94] Gayatri Chakravorty Spivak. 1988. Can the Subaltern Speak? In Marxism
and the Interpretation of Culture , Cary Nelson and Lawrence Grossberg (Eds.).
Macmillan, Basingstoke, 271–313.
[95] Ganesh Surwase, Anil Sagar, BS Kademani, and K Bhanumurthy. 2011. Co-
citation analysis: An overview. (2011).
[96] John Symons and Ramón Alvarado. 2022. Epistemic injustice and data science
technologies. Synthese 200, 2 (2022), 87.
[97] Jasmina Tacheva and Srividya Ramasubramanian. 2023. AI Empire: Unraveling
the interlocking systems of oppression in generative AI’s global order. Big Data
& Society 10, 2 (2023), 20539517231219241.
[98] Doreen Tembo, Gary Hickey, Cristian Montenegro, David Chandler, Erica
Nelson, Katie Porter, Lisa Dikomitis, Mary Chambers, Moses Chimbari, Noni
Mumba, et al. 2021. Effective engagement and involvement with community
stakeholders in the co-production of global health research. bmj 372 (2021).
[99] Andreas Theodorou and Virginia Dignum. 2020. Towards ethical and socio-legal
governance in AI. Nature Machine Intelligence 2, 1 (2020), 10–12.
[100] Charis Thompson. 2004. Co-producing CITES and the African elephant. In
States of Knowledge . Routledge, 67–86.
[101] Nees Van Eck and Ludo Waltman. 2010. Software survey: VOSviewer, a computer
program for bibliometric mapping. scientometrics 84, 2 (2010), 523–538.
[102] Nees Jan Van Eck and Ludo Waltman. 2007. Bibliometric mapping of the
computational intelligence field. International Journal of Uncertainty, Fuzziness
and Knowledge-Based Systems 15, 05 (2007), 625–645.
[103] Nees Jan Van Eck and Ludo Waltman. 2014. Visualizing bibliometric networks.
In Measuring scholarly impact: Methods and practice . Springer, 285–320.
[104] Anthony FJ Van Raan. 2005. For your citations only? Hot topics in bibliometric
analysis. Measurement: interdisciplinary research and perspectives 3, 1 (2005),
50–62.
[105] Michael Veale, Kira Matus, and Robert Gorwa. 2023. AI and global governance:
modalities, rationales, tensions. Annual Review of Law and Social Science 19, 1
(2023), 255–275.
[106] Rick Vogel and Wolfgang H Güttel. 2013. The dynamic capability view in strate-
gic management: A bibliometric review. International Journal of Management
Reviews 15, 4 (2013), 426–446.
[107] Melanie Walker and Carmen Martinez-Vargas. 2022. Epistemic governance and
the colonial epistemic structure: Towards epistemic humility and transformed
South-North relations. Critical Studies in Education 63, 5 (2022), 556–571.
[108] Adrienne Williams, Milagros Miceli, and Timnit Gebru. 2022. The exploited
labor behind artificial intelligence. Noema Magazine 22 (2022).
[109] Alan Winfield. 2019. Ethical standards in robotics and AI. Nature Electronics 2,
2 (2019), 46–48.
[110] Wei Xu. 2019. Toward human-centered AI: a perspective from human-computer
interaction. interactions 26, 4 (2019), 42–46.
[111] Yi Zhang, Mengjia Wu, George Yijun Tian, Guangquan Zhang, and Jie Lu. 2021.
Ethics and privacy of artificial intelligence: Understandings from bibliometrics.
Knowledge-Based Systems 222 (2021), 106994.
A Appendix: Full-size images of 1 (a), 2 (a), 2(b),
3(a), 4(a) and 4(b) and top categories of
academic fields and venues represented in
our dataset
2020

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
Figure 5: Network visualisation of co-citation analysis of cited authors in AI Ethics (full size image of Fig. 1a)
Figure 6: Network visualisation of citational practices in AI Ethics among Global Institutions (full size image of Fig. 2a)
2021

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Figure 7: Network visualisation of co-authorship practices in AI Ethics among Global Institutions (full size image of Fig. 2b)
Figure 8: Network visualisation of co-word Analysis of academic literature in AI Ethics (full size image of Fig. 3a)
2022

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
Figure 9: Network visualisation of citational practices in AI Ethics among countries worldwide (full size image of Fig. 4a)
Figure 10: Network visualisation of co-authorship practices in AI Ethics among countries worldwide (full size image of Fig. 4b)
2023

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Figure 11: Top categories of academic fields represented in our dataset (from WoS)
Figure 12: Top categories of academic venues represented in our dataset (from WoS)
2024


## PDF text extraction

Distributive Epistemic Injustice in AI Ethics: A Co-productionist
Account of Global North-South Politics in Knowledge Production
Abdullah Hasan Safir
Collective Intelligence & Design Group
University of Cambridge
Cambridge, United Kingdom
sa2168@cam.ac.uk
Kerry McInerney
Leverhulme Centre for the Future of Intelligence
University of Cambridge
Cambridge, United Kingdom
kam83@cam.ac.uk
Alan F. Blackwell
Department of Computer Science and Technology
University of Cambridge
Cambridge, United Kingdom
afb21@cam.ac.uk
Ramit Debnath
Collective Intelligence & Design Group
University of Cambridge
Cambridge, United Kingdom
rd545@cam.ac.uk
Abstract
In this study, we analyse a comprehensive database (from 1960 to
June 2024) of scientific publications in AI Ethics (n= 5755) using
Web of Science (WoS) as a data source, to generate quantitative in-
sights around the research trends within the field. We systematically
curate the initial data to conduct a co-authorship and co-citation
analysis with highly cited research outputs (n = 500) and a co-word
analysis with most relevant research outputs (n = 1000). These
bibliometric analyses result in multiple networked visualisations
that map the status quo and the nature of current citational and
collaborative practices among the experts, institutions and coun-
tries involved in global AI Ethics research. Using Sheila Jasanoff’s
co-production theory as a conceptual lens, we analyse these find-
ings and show that the experts from the Global North currently
legitimise their expertise in AI Ethics through dynamic citational
and collaborative practices in knowledge production within the
field. Collectively, they shape the discourses and institutional ways
of understanding around the ethical development of AI technolo-
gies worldwide. This techno-politics of knowledge-making in AI
Ethics culminates in creating epistemic injustice for the Global
South. Drawing from Miranda Fricker and prominent feminist and
postcolonial theorists, we explain how such injustice is produced
and distributed through patterned pathways of co-production of
AI Ethics. Thus, we show that the global project of AI Ethics fails
to deliver its promise to be universally useful by keeping the global
majority populations in the Southern regions marginalized as ‘oth-
ers’.
CCS Concepts
• Human-centered computing →HCI theory, concepts and
models; • Social and professional topics →Geographic char-
acteristics.
This work is licensed under a Creative Commons Attribution 4.0 International License.
FAccT ’25, Athens, Greece
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1482-5/25/06
https://doi.org/10.1145/3715275.3732136
Keywords
Artificial Intelligence, Ethics, Knowledge Production, Epistemic
Justice, Global South
ACM Reference Format:
Abdullah Hasan Safir, Kerry McInerney, Alan F. Blackwell, and Ramit Deb-
nath. 2025. Distributive Epistemic Injustice in AI Ethics: A Co-productionist
Account of Global North-South Politics in Knowledge Production. In The
2025 ACM Conference on Fairness, Accountability, and Transparency (FAccT
’25), June 23–26, 2025, Athens, Greece. ACM, New York, NY, USA, 16 pages.
https://doi.org/10.1145/3715275.3732136
1 Introduction
AI Ethics has emerged as a scholarly discipline to address the moral
implications and societal impacts of artificial intelligence (AI) tech-
nologies [55]. The field seeks to ensure that AI systems are de-
signed and used in ways that are more ethical [ 73, 99, 109] and
‘human–centred’ [93, 110] by promoting fairness [68], accountabil-
ity [31], transparency [61] and their alignment with international
standards of human rights [ 6]. In this article, we argue that AI
Ethics as a global scientific enterprise is co-producing a new techno-
political order. This techno-politics reconfigures political relations
and power dynamics among actors, including experts, institutions,
and nation states, by using knowledge production as political in-
struments (see [59]). In our study, we try to unfold the geopolitical
power dynamics of AI Ethics as a global project, one that promotes
knowledge and values from the Global North at the expense of the
Global South.
Despite its promise of inclusivity and diversity, AI Ethics falls
short in challenging the epistemological, socio-economic, and cul-
tural frameworks of the Global North [8, 12, 69, 86]. Only a small
percentage of publications in prestigious AI Ethics conferences
and journals discuss the ethical issues raised by AI in non-Western
countries, and even fewer of those appropriately address such cir-
cumstances (for systematic literature reviews of articles published
in conferences: [2, 77]; and for journals, see [49, 75]). This body of
literature uses data and ontologies from the West, presents AI Ethics
as a project to mitigate social injustices prevalent in Western con-
texts, and implicitly presents Western ideals as universal standard
to develop ethical frameworks for AI for the rest of the world [91].
2009


FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
But such Global North-centric ethical approaches are often consid-
ered ineffective, if not harmful, in the Global South, because there
exist various socio-economic and contextual differences between
the North and South and the extent of the ethical risks of AI in these
regions are also very contrasting [79]. Here, we acknowledge the
problems associated with the rhetoric of Global North and South,
stereotypes, assumed homogeneity, and contested definitions of the
terms; but scholars who work on power asymmetries and inequality
in AI continue to use such binary categories as a ‘useful unifier for
building solidarity’ for non-Western or Global South countries [79].
In this article, we follow the tradition and use the term Global South
to broadly indicate the economically underdeveloped and develop-
ing countries that are geographically located on continents other
than Europe and North America. We use this common identity,
as it was built on ‘shared historical experiences of exclusion and
oppression’ [83] and reflect it through knowledge-making politics.
Although the racial and colonial harm of AI has been pointed out
by critical and decolonial AI scholars [3, 7, 15, 74, 75], there is less
literature on how exclusion from the key academic and intellectual
discourse in AI Ethics harms and marginalises populations in the
Global South. Some recent academic conversations highlight how
epistemic injustice shapes or is shaped by AI (see [54, 57, 92, 96]),
but epistemic injustice in the academic field of AI Ethics remains
under-researched to date [10].
To this end, we conducted one of the first holistic assessments of
the current academic practices in AI Ethics. Our contribution adds
to the literature by bridging philosophical concepts and data-driven
analysis, revealing how injustice is evident in citation and collab-
oration patterns within AI Ethics. Using bibliometric approaches,
our empirical study explores the ‘intellectual structure’ (see [39])
of the field. We analysed a comprehensive database (from 1960 to
June 2024) of scientific publications on AI Ethics (n = 5755) using
Web of Science (WoS) as a data source to generate quantitative
insights about research trends within the field. We systematically
curated the initial data to perform a co-authorship and co-citation
analysis with highly cited research results (n = 500) and a co-word
analysis with the most relevant research outputs (n = 1000). These
bibliometric analyses resulted in multiple network visualisations
that map the status quo and the nature of current citational and
collaborative practices among the experts, institutions, and coun-
tries involved in global AI Ethics research. Using Sheila Jasanoff’s
[51, 52] co-production theory as a conceptual lens, we analyse these
findings and show that experts from the Global North currently le-
gitimise their expertise in AI Ethics through dynamic citational and
collaborative practices. Collectively, they shape the discourses and
institutional ways of understanding around the ethical development
of AI technologies worldwide. This techno-politics of knowledge-
making in AI Ethics culminates in creating epistemic injustice for
the Global South stakeholders. Drawing from Miranda Fricker [37]
and prominent feminist and postcolonial theorists, we explain how
such injustices are produced and disseminated through patterned
pathways of AI Ethics’ co-production. We discuss these injustices
as distributive in nature, with disproportionate funding, resources,
expertise, and academic prestige in the field owned by a select num-
ber of institutions in the Global North. Thus, through the lens of
distributive epistemic injustice, we argue that the global AI Ethics
project fails to fulfil its promise to be universally useful by keeping
global majority populations in the southern regions marginalised
as ‘others’.
2 Theoretical Framework
2.1 Co-production as a conceptual lens
We use co-production as a conceptual lens in our work to navi-
gate the complexities of global knowledge-making practices in AI
Ethics. Co-production is a seminal concept in Science and Technol-
ogy Studies (STS), largely theorised by Sheila Jasanoff, who posits
that scientific knowledge and techno-political orders in society are
produced together through interconnected processes. This theori-
sation extends the post-structuralist insight that social structures
are rarely stable, universal, or immutable but are fluid, contingent,
and subject to change. Jasanoff [51] argues that, while science and
society constitute themselves simultaneously, they also interact
with each other. There is a continual negotiation of boundaries
between two, each influencing and stabilising the other. Such ne-
gotiations are political and determine what counts as scientific
knowledge, who is considered and represented as experts, and how
scientific knowledge should be integrated into institutional decision
making [52].
At the same time, societies have collective visions of ‘desirable
futures’, which shape the development and acceptance of sociotech-
nical innovations [52, 53] and guide the direction of scientific fields
through research and development [9]. Diverse actors, including
scientists, policymakers, and the public, come together at shared
spaces or sites to discuss issues that have both techno-scientific
and sociopolitical dimensions and articulate these desirable futures.
Jasanoff suggests four of such crucial sites of co-production in her
framework: identities, institutions, discourses, and representations.
The interaction of science and societies at these sites works as ‘order-
ing instruments’ [52] of co-production. Therefore, examining these
four sites provides critical insights around how knowledge-making
and social or political forces are ordered as well as co-produced:
(1) identities may illuminate how individuals and group of re-
searchers form their identities as experts and how their per-
ceived identities enable them to influence the agendas and
research practices of their scientific fields (see [64])
(2) institutions reveal how scientific knowledge creation is inter-
twined with functional social institutions, such as universi-
ties, and how these institutions and their norms are in turn
shaped by the knowledge they produce (see [48])
(3) discourses illuminate how scientific discourses influence pub-
lic understanding and policy debates, and how their up-
take may impact scientific research agendas within a field
(see [100])
(4) representations show how scientific knowledge development
can be embodied through the presence of large entities such
as countries or states in global politics and their ability to
shape the direction of research agenda through such pres-
ence (see [71])
Jasannoff’s co-production theory perfectly helps us to explore
the interactions that take place at these four sites in the field of AI
Ethics to understand the intricate and dynamic relationships be-
tween knowledge production and the current techno-political order
of the field. However, Jasanoff [51] herself prescribes co-production
2010

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
as an interpretative framework and warns that applying it as a rigid
methodological template will not serve its purpose. Rather, this lens
blends the ‘descriptive richness’ with the ‘explanatory power’ of
scholars by helping them avoid deterministic and straightforward
causal explanations of sociotechnical phenomena. Therefore, co-
production as a non-reductionist approach continues to be applied
in various disciplines beyond STS [13, 47, 80, 98].
2.2 Distributive epistemic injustice as derivative
of co-production of AI Ethics
Miranda Fricker [37] defines epistemic injustice as the wrong done
to someone specifically in their capacity as a knower. She identified
two main forms of epistemic injustice: testimonial and hermeneuti-
cal injustice. Testimonial injustice occurs when the credibility of a
speaker is unfairly deflated and their testimony is wrongly discred-
ited, undervalued, or even dismissed due to prejudice. Hermeneu-
tical injustice occurs when the collective interpretative frame-
works available to society are insufficient to understand certain
marginalised experiences, making it difficult for individuals in such
marginalised groups to comprehend and communicate their own
experiences. While these two are characterised as discriminatory
injustices [20], later she added a third layer, distributive epistemic
injustice, to her conceptualisation, suggesting that it occurs when
epistemic goods (such as education or information) are unfairly
distributed in a society [38]. We particularly find this distributive
aspect crucial in AI Ethics for exploring the extent in which this aca-
demic field is capable of contributing to or mitigating the systemic
and structure inequalities in knowledge production and provid-
ing some tangible entry points for the scientific community and
policymakers to collectively imagine practical solutions to these
issues.
Central to Fricker’s analysis is the relationship between power
and identity. This relationship influences epistemic interactions, of-
ten reinforcing existing power structures that define who is consid-
ered a credible knower and whose knowledge is valued or dismissed
[36]. However, the limit of this theorisation is ironically its inherent
Whiteness. Fricker does not acknowledge the body of work on the
politics of knowledge-making by cultural theorists (such as Stuart
Hall), Black feminist thinkers (such as Patricia Hill Collins) or post-
colonial scholars (such as Frantz Fanon, Edward Said, or Gayatri
Spivak) who critically engaged with the ways in which knowl-
edge production and representation perpetuate power imbalances
and marginalise certain racial groups, colonised subjects, or more
broadly non-Western and Global South populations. They highlight
that the processes in which knowledge is produced, validated, and
disseminated may involve the silencing, misrepresentation, and
marginalisation of knowledge systems, experiences, and identities
of vulnerable groups. These standpoints carry much importance in
relation to epistemic injustice facilitated by the co-production of
AI Ethics.
Drawing from Fricker and other thinkers discussed above, it is
possible to map how epistemic injustice operates across Jasanoff’s
four sites of co-production:
(1) injustice through identities: identities are constructed within
power-laden contexts, meaning that certain groups are con-
sistently discredited or excluded from contributing to col-
lective knowledge [37]; colonial alienation can shape self-
perception and identity, develop inferiority by imposing
coloniser’s language [ 32, 33]; Western intellectuals often
speak for marginalised groups in the Global South rather
than enabling them to speak for themselves [94]
(2) injustice through institutions: epistemic injustice is often in-
stitutional; structural and institutional conditions facilitate
inequitable epistemic practices [37]; Western academic insti-
tutions produce knowledge about other parts of the world
(such as the ‘Orient’ and its stereotyping as exotic, backward,
and irrational) [89]
(3) injustice through discourses: exclusion or ‘outsider within’
status of intellectuals from marginalised communities in
mainstream academic and intellectual discourse can invali-
date their knowledges [24]; voices of marginalised groups
cannot be heard within the structures of power and knowl-
edge [94]
(4) injustice through representations: those who control the
means of representation have significant power in shaping
knowledge; lack of representation can lead to the silencing
of marginalised voices [43] or invalidating and suppressing
non-Western ways of knowing [90]; colonial powers often
represented colonised peoples in ways that justified their
subjugation and denied their agency and knowledge systems
[94]
We thus combine these insights with Jasanoff’s account of co-
production to examine how the field of AI Ethics facilitates epis-
temic injustice.
3 Methods
To map the intellectual structure [ 39] of AI Ethics as a research
domain, we have applied bibliometric methods [21, 22] in this study.
Bibliometrics is a set of statistical methods to study and measure
various aspects of academic publications and other forms of schol-
arly literature [82]. Over the years, this quantitative analysis of
empirical data around scientific publications has become increas-
ingly popular as a means of examining knowledge trends within
a specific field and has been used across a wide range of disci-
plines [29]. Among various bibliometric methods [104], we have
combined institutional and country-wise citational analysis[ 95],
co-authorship analysis [103], co-citation analysis [41, 106] and co-
word analysis [46] to capture the state of academic discourses and
prevailing norms such as citational and co-authorship practices
among the experts, institutions, and countries involved in AI Ethics,
and at the same time, to understand the politics embedded within
such practices.
We collected our data from Web of Science (WoS) which re-
mains reliable bibliometric research as one of the oldest and most
authoritative database of research publications and citations met-
rics [11, 103]. To search within this database, we used ‘AI Ethics’
as the primary keyword to find indexed scholarly outputs in the
field and navigate the citation network between all authors and
their affiliations. In addition, we used secondary keywords such as
2011

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
‘Machine Ethics’, ‘Responsible AI’ and ‘AI Governance’ to broaden
the search, ensuring a thorough exploration of articles, proceeding
articles, review articles, early access articles, editorial materials,
book chapters, book reviews, books, and discussions. Our dataset
covered publications from journals such as AI and Society, Ethics of
Engineering Technology, IEEE Access, Big Data and Society, Nature
Machine Intelligence, Mind and Machines, and other applied fields
such as BMJ Open and Journal of Medical Ethics, and AAAI/ ACM
conferences such as AIES, FAccT, CHI, DIS, ACL, EAAMO, as well
as IEEE and other relevant conferences. The search option in this
platform is automated, comprehensive and selection bias or control
free, primary and secondary keywords are used simultaneously.
The search initially resulted in 5767 research outputs published
within the period spanning from 1960 to 2024 (last search date: 9
June 2024). Later, duplicate records were removed to avoid redun-
dancy, and other inconsistencies of data such as unrelated research
output were removed from search results by carefully checking the
titles and abstracts. This produced a final dataset (dataset one) of
5755 records.
We have used a network visualiser software named VOSviewer
[101] for our analysis. Since the academic publications in the initial
sample were cited more than 68,000 times in total (11.85 average
per item), it was not possible to perform bibliometric analysis and
produce meaningful results using VOSviewer with such a large
dataset. As a cut-off point [67], the top 500 research outputs (dataset
two) were sorted in descending order according to the number of
times they were cited first from the highest. They carried more than
40 percent of total citations of the original dataset. Similarly, for
consistent results in co-word analysis, dataset three was prepared
with the top 1000 research outputs using the ‘relevance’ feature of
the WoS platform. ‘Relevance’ sorts the records in an order based on
a ranking system that considers how many search terms are found
in the titles, abstracts and keywords of the research results [ 19].
Dataset two [88] and Dataset three [87] are available online.
Using dataset two, we constructed networks of research organi-
sations and countries contributing to AI Ethics academic literature.
The analysis focused on citational practice, with 30 organisations
and 31 countries crossing the minimum common citation threshold1
of six documents. We created a network visualisation map showing
how these organisations are connected through mutual citation
practices. Our co-authorship analysis revealed that 49 organisations
had researchers who co-authored at least five AI Ethics-related re-
search outputs, and 21 countries had researchers who produced a
minimum of 10 documents in collaboration. Next, we performed
a co-citation analysis that involves examining how often two doc-
uments are cited together by other subsequent documents [ 95].
We selected ‘cited authors’ as the unit of co-citation analysis in
VOSviewer, with 66 authors crossing the 20 citation threshold. The
authors with the highest total link strengths were visible in the
mapping. Finally, we applied co-word analysis to examine the rela-
tionships between keywords or phrases in AI Ethics [46]. Co-word
analysis measures the strength of the co-occurrence [ 18] of the
terms existing in the dataset. For the current analysis, a minimum
number of occurrences of a particular term within the abstracts of
1For careful threshold selection and understanding the algorithmic approaches behind
clustering in VOSviewer, we consulted existing key literature of bibliometrics [78, 101,
102] and applied those insights in our analysis
the research documents was selected 30 and 166 words crossed this
threshold. The Top 100 terms with high co-occurrence relevance
score were selected for network visualisation. The mapping show-
cases the interconnected thematic composition of the academic
field of AI Ethics. All visualisations were adjusted in terms of their
scale and size to increase clarity of the embedded texts, and later
analysed. The next section highlights these insights.
4 Findings
The following four subsections summarise the findings of our study.
Through the site of identities, institutions, discourses, and rep-
resentations, we examine the patterned pathways by which co-
production of AI Ethics occurs.
4.1 Making identities in AI Ethics: whose
expertise counts?
Jasanoff argues that individual and collective identities are fre-
quently created, contested, or renegotiated through knowledge pro-
duction within a scientific field, while such productions of knowl-
edge contribute to shaping and sustaining these roles of experts,
providing them with epistemic power and significance (see [65]).
Academic practices in AI Ethics, such as co-citation, contribute to
defining who is recognised as an expert and what is considered ex-
pertise in this interdisciplinary field ([58]). Such knowledge-making
practices also stabilise the field by bringing order, standardisation,
and legitimacy to produced knowledge, in this case ethical ap-
proaches to AI.
Figure 1(a) visualises the relationships between highly cited
authors in the field of AI Ethics. Lines connecting the authors rep-
resent co-citations, showing how frequently these authors are cited
together. It displays four clusters, each represented by different
colours (blue, green, red, and yellow), indicating groups of recur-
rently co-cited authors. The connections between authors reflect
shared citations. The density of interconnections is higher within a
cluster, indicating strong intellectual ties and joint research themes.
The high centrality of some of the authors located in the dense,
central parts of each cluster indicates their significant influence.
In general, the presence of multiple clusters in this representative
mapping of academic literature reflects the diverse expertise and
orientations of the scholars to different schools of thought within
the field of AI Ethics.
The presence of such diverse frontiers of knowledge within AI
Ethics is consistent with the interdisciplinary nature of this emerg-
ing interdisciplinary field. This diversity in knowledge-making
practice plays a pivotal role in the formation of identities, defining
who are considered experts and what constitutes their expertise
— linking the individuals or groups to the field’s establishment as
authorities in specific domains. The identities of AI Ethics experts
are co-produced through the recognition of their academic insights
and meaningful contributions to the field by peer acknowledgment
and trust manifested through high counts of citations (see [23]).
The cross-cluster connections visible from the graph indicate
these sub-fields also influence each other, leading to a richer and
more integrated field of study of AI Ethics as a response to mul-
tifaceted problems introduced by AI in society. However, there
2012

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
(a) Network visualisation of co-citation analysis of cited authors
in AI Ethics (generated in VOSviewer), see Fig. 5 in appendix for
full size image
(b) A table showing four frontiers in AI Ethics emerged from the
co-citation analysis
Figure 1: Co-citation practices and emerging frontiers in AI
Ethics
are disconnections on the map as well. We realise there are inher-
ent disagreements over key definitions within the field, although
scholars from diverse disciplines are contributing to knowledge
around the ethical implications of AI from different angles. For
example, computer scientist Margaret Mitchell and philosopher
Nick Bostrom remain very distant from each other, which may
reflect their conflicting opinions in their respective scholarship
on the ethical implications of AI and influencing citation patterns
(for details of these conflicts within the field, see [40]). However,
authors such as Luciano Floridi appear prominently in the centre
and show strong connections with researchers in every cluster,
suggesting a central influence through his foundational work on
the philosophy of information and ethics of AI (for example, [35]).
Thus, experts from different domains play crucial roles in bringing
cohesion in the intellectual landscape of AI Ethics through their
endorsements, critiques, and validations which eventually legit-
imise the knowledge-making process and maintain the stability
and integrity of the academic field.
While this co-citation analysis and mapping helps identify the
key authors and their collaborative networks in AI Ethics, it also
shows the overwhelming presence of Western scholars (findings
in the following sections highlight the institutional and country
affiliations of the researchers). None of the scholars in the map
(Figure 1 (a)) is based in the Global South, including those who are
critical of the Global North-centric establishments in AI. It would be
wrong to assume that AI Ethics as a field should or does not cover
Global South issues and contexts (be it philosophical, computing,
social or legal), or there is a lack of expertise or knowledge-making
capacity in these fields in the Global South; such assumptions, as
seen in Section 2.2, highlight, are rather constructed [90]. Instead,
it implies that it is difficult for scholars in the Global South to be
recognised as experts and achieve legitimacy of their expertise by
navigating through the co-production mechanism of the emerging
field as discussed above. Previous studies in different fields show
that the intrinsic value of an academic work is not the sole factor
determining its citation, as Matthew Effect [ 60] and preferential
attachment [1] add additional value to the published papers that
include prestige of researchers’ institutional affiliations and publi-
cation venues. At the same time, there exists asymmetry in citation
expectations among the academics in the Global North and the
South. Global South scholars are expected to cite Western scholars
to avoid marginalisation and rejection in top journals/venues in the
field, while Global North scholars have no comparable expectation
to engage with Global South scholarship [25].
The following subsections will build on and advance these criti-
cal insights, connecting these experts with institutions (for example,
influential scholars such as Floridi are based in prominent Western
universities such as Oxford) and the prevalence of funding oppor-
tunities in the Global North. In general, this lack of recognition of
scholars from the Global South in the field results in their weaker
identity formation as well as a lack of authority to make decisions
and judgments in shaping the direction of research agendas in AI
Ethics. As Western experts continue to validate and organise the
epistemic structure of the field, it creates an environment in which
the knowledge they produce becomes reliable and replicable. Break-
ing the boundaries of expertise or redefine it becomes impossible
for the Global South scholars (similar politics highlighted in a close
field, HCI: [4]). Thus, the field progresses in a coherent manner, but
by systematically erasing Global South expertise.
4.2 Institutionalisation of AI Ethics
To better understand the mechanisms through which the legitimacy
of new knowledge is established, the lens of institutionalisation is
powerful. A quick analysis of our data shows the distribution of
research outputs in AI Ethics published by institutions worldwide.
We find an unbalanced ratio: among the top 50, four are in Aus-
tralia (Monash University, University of Melbourne, UNSW, and
Australian National University), and two institutions are in Asia
(National University of Singapore and IIT, India). The remaining 44
institutions are either in Europe or in North America and include
universities, the research wings of tech companies such as Microsoft
and IBM, and public research organisations such as the Alan Turing
Institute. There are no institutions in Latin or Central America,
sub-Saharan Africa, or the region of the Middle East and North
Africa (MENA). Although the dominance of Western institutions
in AI Ethics literature shows that these institutions are funding
and prioritising ethics research in AI, reflecting their commitment
to address responsible ways of AI development and deployment,
they are also contributing to structuring ‘institutionalised ways
2013

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
of understanding’ [50]. A subsequent citation analysis (Figure 2
(a)) and a co-authorship analysis (Figure 2 (b)) further clarify the
mechanisms of their intellectual influence.
(a) Network visualisation of citational practices in AI Ethics
among Global Institutions (generated in VOSviewer), see Fig. 6
in appendix for full size image
(b) Network visualisation of co-authorship practices in AI Ethics
among Global Institutions (generated in VOSviewer), see Fig. 7
in appendix for full size image
Figure 2: Citational and co-authorship practices in AI Ethics
is overwhelmingly situated in the Global North
Each node of the network visualisation in Figure 2(a) represents
a different institution, and the size of the node in the map indi-
cates the number of citations that institution has received, with
larger nodes (such as the University of Oxford, the University of
Cambridge, the Alan Turing Institute, Harvard, MIT, and Stanford)
representing institutions that are more frequently cited in the AI
Ethics literature. The lines connecting the nodes represent the cita-
tion relationships between institutions. For example, the University
of Oxford and Alan Turing Institute have the thickest and darkest
lines, which means that researchers at these institutions frequently
refer to each other’s work. Similarly, MIT-Harvard-British Columbia
have stronger citation ties between their AI Ethics research. The
mapping also shows different colours (purple, blue, red, green, and
yellow) representing clusters of institutions that are closely related
in terms of their citation practices. For example, British institutions
including Oxford, Cambridge, Turing and the British Library have
a strong collaborative network through frequent citational inter-
actions, as the map indicates. Institutions with central positions
and extensive connections in each cluster have a broader impact;
for example, within the red cluster, MIT and Harvard researchers
are influencing other institutions. Peripheral institutions (such as
the German Aerospace Centre or Vrije Universiteit Amsterdam)
with fewer connections may have more specialised but less widely
recognised contributions. The network also shows significant in-
terconnections between institutions across different clusters (such
as Oxford-MIT), suggesting cross-Atlantic academic engagement
in AI Ethics.
Figure 2(b), on the other hand, visualises the co-authorship net-
work of institutions involved in global AI Ethics research. Each
node represents an institution like the previous one, but the size of
the node here indicates the volume of co-authored publications in
AI Ethics. The lines connecting the nodes represent co-authorship
links between institutions, with the thickness of the lines indicating
the strength or frequency of collaboration. For example, the map
indicates that researchers from Oxford, Stanford and MIT produce
more collaborative works, and they are also highly interconnected
with multiple other institutions in their efforts. This visualisation,
like the previous one, shows several clusters of nodes, typically
represented by a distinct colour (blue, green, red, yellow, orange,
purple), indicating groups of institutions that frequently collaborate
with each other. This can be due to geographical proximity, similar
research interests, or existing academic partnerships.
However, there is no presence of Global South institutions in
these mappings, and there is only one Asian institution represented:
the National University of Singapore. The distribution of AI Ethics-
related publications, as well as collective citational and collabora-
tive practice across the institutions in the Global North suggest a
significant concentration of contributions from their side to the
field, by showing preferred forms of expertise through citations and
academic collaborations. As repositories of knowledge and power,
Western institutions are bringing order in AI Ethics research, but
at the same time their institutional hegemony reinforces their sta-
tus and influence within the field. Logically, to a Global South
researcher wanting to do cutting-edge research in AI Ethics, in-
stitutions in the Global North regions will seem better equipped
(which can be true), and these institutions inevitably attract top
talents from the South with those researchers having opportunities
to build their identities benefiting from the institutional credibility
and endorsement. This pattern results in ‘brain-drain’ phenomenon
as previously discussed in literature [30] and remain as an structural
barriers towards equity in knowledge production. Even if scholars
are able to do research on Global South issues, their processes of
inquiry are shaped, and the outputs owned by the Global North
institutions — weakening Southern stakes in the institutionalisation
of AI Ethics. As a result, established epistemic norms centred on
the Global North in the field continue to be replicated.
4.3 Discursive space of AI Ethics
In their effort to institutionalise a research field, scientific authori-
ties establish new structures of power through the formulation of
discourses [52], and therefore, this study next looks at the discursive
practices of the AI Ethics academic community.
Figure 3(a) depicts the co-word analysis of academic literature
in AI Ethics which is produced by examining the frequency and
2014

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
(a) Network visualisation of co-word Analysis of academic litera-
ture in AI Ethics (generated in VOSviewer), see Fig. 8 in appendix
for full size image
(b) Different dynamics of discourses in AI Ethics emerged from
the co-word analysis
Figure 3: Co-word analysis in AI Ethics literature and domi-
nant discourses of the field
patterns of co-occurrence of keywords in the paper abstracts. Each
node represents a keyword or term, and the size of the node in
the map indicates the frequency of the term in the literature, with
larger nodes (for example, transparency, fairness, human/ humanity,
future, guideline, governance, participant experience, etc.) repre-
senting more frequently occurring keywords. The lines connecting
the nodes represent co-occurrences of keywords within the research
outputs in the field, while thicker and darker lines indicate stronger
co-occurrence relationships. For example, keywords like fairness,
transparency, lack, and trust are well connected, meaning these
terms are frequently mentioned together. Different colours in the
visualisation represent clusters of terms that are closely related in
the literature; by analysing these clusters, it is possible to construct
some distinct thematic areas within AI Ethics academic discourse.
Figure 3(b) highlights these emerging themes. These discourses
are also consistent with four frontiers in AI Ethics that emerged
from the co-citation analysis: ethical/philosophical, legal, design
and long-term issues. It indicates that experts from their respective
fields repurpose discourses that were already prevalent in their
domain and incorporated them into AI Ethics, thus shaping the
direction of the field.
The visualisation (Figure 3 (a)) also shows interconnections be-
tween different clusters, indicating that these discourses in AI Ethics
developed in highly interrelated ways. For example, governance and
policy discussions (green cluster) are closely linked with fairness
and transparency issues (blue cluster), linking technical knowledge
to practise or action in the field. Terms like machine learning, ethi-
cal principle, trust, science, and researcher appear at the centre of
the map, indicating their cross-cutting roles in shaping the dynamic
nature of the evolving discourses in AI Ethics.
While the co-word analysis visualisation provides an overview
of the key thematic discourses and their interconnections within
AI Ethics literature, they also show that there is no strong presence
of issues that are particularly or uniquely relevant to the Global
South in this discursive landscape. Drawing from findings in the
previous subsections, the absence can be explained by the fact that
these current discourses are heavily influenced by the Global North
stakeholders through their preference for expertise and institutional
mechanisms. Important critical AI issues relevant to Global South
regions, such as data and AI colonialism [26, 44], imperialism [97],
data sovereignty [85], extractivism [27], labour exploitation [108],
AI’s detrimental environmental impact [62], AI for low resource lan-
guages [76] and/or culturally sensitive design [72, 86] are currently
under-represented or overlooked as ethical blind spots in the global
discursive space of AI Ethics. Conducting occasional research on
these issues will not be enough; they need to be mainstreamed to
shift the direction of the current dominant Global North-centric
discourses.
4.4 Crisis of representation in AI Ethics
Although representation has varied meanings, in this case, the
lens is specifically used to explore the interplay between national
contexts of different countries and the production of academic
knowledge in AI Ethics and to understand how it contributes to
global scientific progress of the field as well as international poli-
tics. National priorities, economic interests, political environments,
and cultural values shape scientific research [34], while scientific
achievements, collaborations, and contributions to knowledge mak-
ing influence national identities and international standing [28]. In
linking to the findings in the previous subsections, countries are
represented in the global network of AI Ethics research through
their knowledge contributions facilitated by expert researchers and
institutions. The participation and visibility of countries are further
explored in the following two network visualisations in terms of
their influence on global academic agendas of the field.
The visualisation of the network in Figure 4 (a) helps to under-
stand the relationships and influence patterns between different
countries of the world in AI Ethics literature based on their cita-
tional interactions. Each node on the map represents a country,
while the size of the node indicates the number of citations the
researcher in that country has received, with the largest nodes rep-
resenting countries with the highest total citation counts. For ex-
ample, countries such as England, Germany, and the United States
have large nodes and numerous connections, highlighting their
substantial influence in knowledge-making in the field. The lines
connecting the nodes represent the citation relationships between
countries. Thicker and darker lines (for example, England-Germany
and USA-Canada) indicate stronger citation ties, meaning that re-
searchers from these countries frequently cite each other’s work.
Like previous visualisations, this mapping also shows different re-
gional clusters of countries who are highly interactive through their
citational practices. However, strong inter-cluster interconnections
2015

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
(a) Network visualisation of citational practices in AI Ethics
among countries worldwide (generated in VOSviewer), see Fig. 9
in appendix for full size image
(b) Network visualisation of co-authorship practices in AI Ethics
among countries worldwide (generated in VOSviewer), see Fig. 10
in appendix for full size image
Figure 4: Global North countries remain at the centre within
citational and co-authorship practices in AI Ethics
are visible between the USA, Australia, England, and other Euro-
pean countries, indicating the central roles of the researchers of
these countries in shaping the field of AI Ethics.
Similarly, Figure 4 (b) visualises the collaborative relationships
in AI Ethics among countries worldwide through co-authorship
practices. In this case, the size of the node indicates the number
of co-authored publications from that country, with larger nodes
(such as USA, England, Germany, etc.) representing countries with
a higher number of co-authorship in AI Ethics literature. Thicker
and darker lines (for example, England-Germany) indicate stronger
co-authorship ties, meaning that researchers from these countries
frequently collaborate on their publications in the field. From the
clustering feature, it is also visible that European countries (red
cluster) that include England, Germany, Netherlands, Belgium, and
Switzerland are showing strong interconnections, suggesting fre-
quent co-authorship and collaboration among these countries.
However, unlike other visualisations in this study, some non-
Western countries are visible in these two networks, but in almost
all cases they remain in the periphery, indicating their weaker
positions both in terms of citational and co-authorship practices.
Figure 4(a) shows that while the works of Chinese researchers are
somewhat frequently cited by others in the field, researchers from
countries such as India and Brazil cite European or North Ameri-
can researchers in their publications without strong reciprocation.
Similarly, these two countries are also present as small nodes in
the periphery of Figure 4 (b), indicating that collaborations are of-
fered to them from the central, leading countries of the map, which
are located in the Global North. Weaker representations of Global
South countries in the international collaborative network of AI
Ethics reflect their compromised capacities and participation in
shaping the field’s direction and knowledge production. Countries
in the Global North, on the other hand, leverage stronger scientific
collaborations by pooling resources and sharing expertise from
all over the world. Such scientific efforts cultivate a global com-
munity of practice and international cooperation to facilitate the
harmonisation of standards and practices for AI, thus preventing
regulatory arbitrage and ensuring consistent protection of rights
across borders [105]. The Northern actors gain an upper hand in
scientific diplomacy that enhances the soft power to regulate AI on
a global scale [56].
The findings outlined in these four subsections discuss the cur-
rent directions in AI Ethics research and demonstrate that top
names, institutions and countries in the Global North become the
centre of knowledge production by gaining more citations in the
field. Thus, the experts from these regions gain credibility and
recognition for the knowledge they produce in the field, and their
institutional and national representations influence the dominant
discourses of the field. The patterned pathways of co-production of
global AI Ethics project results in epistemic injustice for the Global
South. The nature of such epistemic injustice and its implications
will be discussed in the next section.
5 Discussion
5.1 Distributive epistemic injustice in/of AI
Ethics
Our study demonstrates the politics of knowledge-making in AI
Ethics in four sites: identities, institutions, discourses, and represen-
tations. It shows that the Global North actors currently bring order,
stabilise and control the trajectories, and thereby, own the means
of co-production of AI Ethics. Our citational, co-citational, and
co-authorship analysis of the field reveals that prominent Global
North figures are shaping the intellectual landscape of AI Ethics by
establishing themselves as authoritative knowers, with academic
institutions in Europe and North America setting the standards and
norms for ethical AI research and practice, often directly shaping
national or global policies (see [5]). We also show that AI Ethics
is being shaped through discursive practices with interrelated and
mutually reinforcing technical, legal, and philosophical themes.
However, the dominance of Global North-based experts and in-
stitutions reinforces their epistemic power, peer influence, and
institutional hegemony in the field [107]. These mechanisms con-
tribute to disproportionate country-level representations in the
global collaborative network of knowledge-making in AI Ethics,
making the field geographically concentrated in the Global North,
leading to an uneven distribution of knowledge production, and
creating epistemic injustice by perpetuating the existing power
2016

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
imbalances around knowledge and expertise between the Global
North and South.
Global South scholarship on AI Ethics is often sidelined in favour
of Global North alternatives on similar ethical and societal impli-
cations around AI. Researchers from these regions, with current
their ‘outsider within’ [24] status, struggle to meaningfully partici-
pate in the mainstream academic and intellectual discourses of AI
Ethics as credible knowers due to a lack of funding, recognition,
and collaboration with institutions and researchers in the Global
North. The field continues to overlook critical ethical concerns per-
tinent to the Global South, such as community-centric values [84],
local notions of privacy [ 8], and indigenous knowledge systems
[63]. If institutional and expertise gaps are not addressed, this cycle
of under-representation in discourse making will continue. The
implications of this are double-layered for the Global South’s AI
futures. First, Global South stakeholders may end up receiving ill-
suited AI technologies that can exacerbate existing techno-political
inequalities [17]. Second, global policy and governance frameworks
predominantly informed by Northern AI Ethics scholarship may
establish standards that could be irrelevant or difficult to implement
within Southern societies, creating regulatory gaps and leading to
poor ethical oversight of such technologies in these regions [79].
In addition, when Southern countries adopt Global North-centric
AI Ethics policies, it can lead to social resistance, mistrust in AI,
and political tensions [66]. Here, we would also like to highlight
Frickerian hermeneutic injustice alongside distributive nature of
such patterns. The collective interpretive frameworks developed
in the Global North can appear insufficient in the Global South in
many cases, as Southern researchers highlights, making it difficult
for marginalised groups to comprehend and communicate their ex-
periences. As community of practitioners of ethics, they often end
up questioning AI policies or applications, but become unable to
express their concerns due to geopolitical and cultural hegemony.
Thus, the Global South as an inferior ‘other’, marginalised within
the knowledge-making project of AI Ethics, is forced to accept the
knowledge of the West (see [32, 94]). While ‘othering’ by techno-
scientific knowledge systems (see [14]) is not new, it is even more
problematic in the field of AI Ethics, given that the field is explicitly
packaged as ‘ethical’. Western dominant experts and institutions
often produce distorted representations for their Southern ‘others’
— by excluding them, and in addition, determining what is ethical
for them or not — to justify their dominance (see [43]), and in doing
so, marginalise the epistemologies of these groups (see [24]) and
their ‘non-Western ways of knowing’ (see [90]). AI Ethics, therefore,
is not ethical enough, unless it takes care of its problem of epistemic
injustice.
5.2 Aligning academic practices in AI Ethics
towards Justice for the Global South
Our study shows that inequitable epistemic practices in AI Ethics
are facilitated by structural and institutional conditions [37]. The
systemic lack of researchers in the field representing Global South
countries is power-laden, since Global North actors control the
means of representation [43]. Addressing the disparities around
the contributions from the institutions in the Global South could
be addressed by concerted efforts to support and empower those
institutions [42, 81, 107]. For example, institutions in the Global
North could support Global South institutions by fostering cross-
regional collaborations. However, the current global co-authorship
network mapping in our study fails to visualise convincing pres-
ence of academic institutions beyond Western countries. Similarly,
the peripheral positions of Global South countries such as India
and Brazil in country-level mapping indicate the weaker roles of re-
searchers from these countries in the global collaborative academic
network in AI Ethics.
Southern actors’ low participation in citational practices is often
attributed to weaker institutional capacity and inequitable resource
allocation in global knowledge production, hindering their ability
to produce quality academic works and eventually contribute to
ethical AI efforts. One quick analysis in our study shows that the
majority of top funding agencies for AI Ethics research are located
in the Global North, particularly in North America and Europe (We
found only one Chinese organisation among the ten top funders
contributing to the high number of publications in the field). This
concentration co-relates to the availability of resources, infrastruc-
ture, and established research institutions in these regions, and
contrarily, can lead to an imbalance in research contributions from
the Southern institutions in AI Ethics literature.
Some decolonial AI scholars question whether AI as a field can
ever be decolonised because it depends on and was made possi-
ble by the logics of coloniality [ 3]. Others, however, continue to
demand non-Western perspectives from the margins, edges, or pe-
ripheries of the racial global system (see [7, 70, 74]). In this article,
we extend these viewpoints, but for the field of AI Ethics — for
bringing more knowledge and power from ‘below’ (see [ 16, 45])
and promote greater inclusivity and equity — integrating under-
represented perspectives into the mainstream ethical discourses
around AI, particularly those from the Global South. Plural epis-
temologies, unique sociotechnical contexts and political realities
can inform more context-sensitive and effective ethical guidelines
for AI. Such efforts have profound implications, especially for the
design, development and deployment of AI technologies in a non-
exclusionary way in the near and longer term.
While we understand the necessity of more empirical, on-the-
ground studies examining the specific ethical issues faced by differ-
ent regions and communities in the world, our research captures
the structural and systemic hurdles for it. These, in turn, show
some key entry-points for equitable and global collaborative efforts
to decentralise the AI Ethics academic project: making identities,
institutions, discourses, and representations for the Global South
in the field. We should not explicitly assume that Global South
approaches in AI Ethics will be inherently pro-justice, the political
realities may not enable the Global South actors to challenge and
dismantle prejudices that undermine the credibility and desirable
recognition of their knowledge systems and experiences. Rather,
investment in building epistemic capacities of Southern experts and
research institutions through funding and infrastructural support,
promoting equity in cross-regional collaborations in the field, and
creating platforms that amplify their diverse voices can be a practi-
cal way forward. Future research can focus on the mechanisms of
such equitable approaches to AI Ethics, by deeply looking at the
instruments highlighted in this research.
2017

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
6 Limitations
Our data for this study were collected from the WoS platform. While
this is one of the most comprehensive databases available, it might
exclude some venues and journals in the field (for top categories of
academic fields and venues represented in our dataset, see figure 11
and 12 in the appendix). In most cases, the excluded journals in WoS
are not indexed, where researchers from the Global South countries
may publish their research. However, not being indexed reduces the
chances of papers to be cited, which itself is part of the citational pol-
itics. Co-citation and co-word analysis was conducted with subsets
(respectively dataset two: highly cited research outputs, n = 500 and
dataset three most relevant research outputs, n = 1000) of the main
dataset. These Ns are kept different for meaningful visualisations in
VOSviewer based on the statistical parameters such as modularity
co-efficient and relevance score. While the methods used in the
empirical study are helpful to generate quantitative insights on
research trends, influential authors etc. based on the number of
publications, citations, and co-authorships etc., they only become
meaningful if properly analysed. In many cases, bibliometric meth-
ods are used by generalists or method experts, who can only discuss
an academic field’s publishing patterns and general understandings,
without critical and extensive engagements of the very field ([111].
With these limitations in mind, in this research such methods have
been used carefully and in a complementary way, by focusing on
the qualitative depth of the analysis, for example, not looking at
what, who, or what percentage, rather emphasising on why, how,
and so what. The interpretations of the quantitative results were
also offered carefully. For example, while institutional mapping can
indicate high presence of Global North institutions, there can be
researchers from the Global South producing research within such
institutions, but this movement of researchers away from the South
is part of what contributes to the Southern research institutions
being under-represented (we discuss this on section 4.2). In this
context, we realise a necessity of a positionality statement indicat-
ing how our own positionalities as researchers have informed this
research. All four researchers of this study are currently based at an
elite university in the United Kingdom, although they come from
different countries such as Bangladesh, India and New Zealand.
7 Conclusion
Drawing from a comprehensive empirical study, in this paper, we
show that the actors in the Global North currently own the means
of knowledge production with their dominant representations in
AI Ethics. The Northern experts interact collaboratively, institution-
alise knowledge practices, and by doing so, they bring an apparent
stability to the field, but end up shaping the discourses and even-
tually the global ways of understanding around what ethical AI
could and should look like. Since the control of the trajectories of
AI Ethics belong to the West, we contend that this global project
facilitates and distributes epistemic injustice through the patterned
pathways of its co-production. We also discuss the implications, ar-
guing that such epistemic injustice perpetuates the existing power
disparity among the Northern and Southern actors, and so the po-
litical purpose of AI Ethics to ensure universal social good through
harmonious human-AI coexistence fails to deliver. The Global South
remains as an inferior ‘other’ of the AI Ethics project with their
weaker representation and influence. We suggest that identities,
institutions, discourses and representations can be critical site of
interventions to ensure Global South voices and concerns to be
meaningfully heard and valued within this unequal power dynam-
ics.
Acknowledgments
This work builds on the MPhil Dissertation work of the first author.
He acknowledges the generous funding he received from his college
Trinity Hall that made his MPhil in Ethics of AI, Data and Algorithm
possible at the Leverhulme Centre for the Future of Intelligence,
University of Cambridge.
References
[1] Alireza Abbasi, Liaquat Hossain, and Loet Leydesdorff. 2012. Betweenness
centrality as a driver of preferential attachment in the evolution of research
collaboration networks. Journal of informetrics 6, 3 (2012), 403–412.
[2] Amina A Abdu, Irene V Pasquetto, and Abigail Z Jacobs. 2023. An empirical
analysis of racial categories in the algorithmic fairness literature. In Proceedings
of the 2023 ACM Conference on Fairness, Accountability, and Transparency . 1324–
1333.
[3] Rachel Adams. 2021. Can artificial intelligence be decolonized? Interdisciplinary
Science Reviews 46, 1-2 (2021), 176–197.
[4] Syed Ishtiaque Ahmed, Sareeta Amrute, Jeffrey Bardzell, Shaowen Bardzell,
Nicola Bidwell, Tawanna Dillahunt, Sane Gaytán, Naveena Karusala, Neha
Kumar, Rigoberto Lara Guzmán, et al. 2022. Citational justice and the politics
of knowledge production. interactions 29, 5 (2022), 78–82.
[5] Mhairi Aitken, David Leslie, Florian Ostmann, Jacob Pratt, Helen Margetts, and
Cosmina Dorobantu. 2022. Common regulatory capacity for AI.The Alan Turing
Institute (2022).
[6] Evgeni Aizenberg and Jeroen Van Den Hoven. 2020. Designing for human rights
in AI. Big Data & Society 7, 2 (2020), 2053951720949566.
[7] M. Ali. 2014. Towards a decolonial computing. In Ambiguous Technologies:
Philosophical Issues, Practical Solutions, Human Nature . International Society of
Ethics and Information Technology, 28–35.
[8] Payal Arora. 2019. Decolonizing privacy studies. Television & New Media 20, 4
(2019), 366–378.
[9] Silke Beck, Sheila Jasanoff, Andy Stirling, and Christine Polzin. 2021. The
governance of sociotechnical transformations to sustainability. Current Opinion
in Environmental Sustainability 49 (2021), 143–152.
[10] Abeba Birhane, Elayne Ruane, Thomas Laurent, Matthew S. Brown, Johnathan
Flowers, Anthony Ventresque, and Christopher L. Dancy. 2022. The forgotten
margins of AI ethics. In Proceedings of the 2022 ACM Conference on Fairness,
Accountability, and Transparency . 948–958.
[11] Caroline Birkle, David A Pendlebury, Joshua Schnell, and Jonathan Adams. 2020.
Web of Science as a data source for research on scientific and scholarly activity.
Quantitative Science Studies 1, 1 (2020), 363–376.
[12] Alan F Blackwell, Addisu Damena, and Tesfa Tegegne. 2021. Inventing artificial
intelligence in Ethiopia. Interdisciplinary Science Reviews 46, 3 (2021), 363–385.
[13] Scott Bremer and Simon Meisch. 2017. Co-production in climate change re-
search: reviewing different perspectives.Wiley Interdisciplinary Reviews: Climate
Change 8, 6 (2017), e482.
[14] Santiago Castro-Gómez. 2019. The Social Sciences, Epistemic Violence, and the
Problem of the" Invention of the Other". In Unbecoming Modern . Routledge,
211–227.
[15] Stephen Cave. 2020. The problem with intelligence: its value-laden history and
the future of AI. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and
Society. 29–35.
[16] Dipesh Chakrabarty. 2000. Subaltern studies and postcolonial historiography.
Nepantla: views from South 1, 1 (2000), 9–32.
[17] Alan Chan, Chinasa T Okolo, Zachary Terner, and Angelina Wang. 2021. The
limits of global inclusion in AI development. arXiv preprint arXiv:2102.01265
(2021).
[18] Xiuwen Chen, Jianming Chen, Dengsheng Wu, Yongjia Xie, and Jing Li. 2016.
Mapping the research trends by co-word analysis based on keywords from
funded project. Procedia computer science 91 (2016), 547–555.
[19] Clarivate. 2022. Web of Science: Sort options for search results. https://
clarivate.com/web-of-science-sort-options Accessed: 2025-01-11.
[20] David Coady. 2017. Epistemic injustice as distributive injustice 1. In The
Routledge handbook of epistemic injustice . Routledge, 61–68.
[21] Manuel J Cobo, Antonio Gabriel López-Herrera, Enrique Herrera-Viedma, and
Francisco Herrera. 2011. An approach for detecting, quantifying, and visualizing
2018

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
the evolution of a research field: A practical application to the Fuzzy Sets Theory
field. Journal of informetrics 5, 1 (2011), 146–166.
[22] Manuel J Cobo, Maria Angeles Martínez, María Gutiérrez-Salcedo, Hamido
Fujita, and Enrique Herrera-Viedma. 2015. 25 years at knowledge-based systems:
a bibliometric analysis. Knowledge-based systems 80 (2015), 3–13.
[23] Citational Justice Collective, Gabriela Molina León, Lynn Kirabo, Marisol Wong-
Villacres, Naveena Karusala, Neha Kumar, Nicola Bidwell, Pedro Reynolds-
Cuéllar, Pranjal Protim Borah, Radhika Garg, et al. 2021. Following the trail
of citational justice: critically examining knowledge production in HCI. In
Companion Publication of the 2021 Conference on Computer Supported Cooperative
Work and Social Computing . 360–363.
[24] Patricia Hill Collins. 2022. Black Feminist Thought: Knowledge, Consciousness,
and the Politics of Empowerment . Routledge.
[25] Fran M Collyer. 2018. Global patterns in the publishing of academic knowledge:
Global North, global South. Current Sociology 66, 1 (2018), 56–73.
[26] Nick Couldry and Ulises A Mejias. 2019. Data colonialism: Rethinking big
data’s relation to the contemporary subject. Television & New Media 20, 4 (2019),
336–349.
[27] Kate Crawford. 2021. The Atlas of AI: Power, Politics, and the Planetary Costs
of Artificial Intelligence.
[28] Sarah R Davies and Maja Horst. 2016. Science communication: Culture, identity
and citizenship . Springer.
[29] Nicola De Bellis. 2009.Bibliometrics and citation analysis: from the science citation
index to cybermetrics . scarecrow press.
[30] Frédéric Docquier. 2006. Brain drain and inequality across nations.International
Journal on Multicultural Societies (2006).
[31] Finale Doshi-Velez, Mason Kortz, Ryan Budish, Chris Bavitz, Sam Gershman,
David O’Brien, Kate Scott, Stuart Schieber, James Waldo, David Weinberger,
et al. 2017. Accountability of AI under the law: The role of explanation. arXiv
preprint arXiv:1711.01134 (2017).
[32] Frantz Fanon. 1952. Black Skin, White Masks . Grove Press.
[33] Frantz Fanon. 1963. The Wretched of the Earth . Grove Press.
[34] Martha Finnemore. 1996. National interests in international society . Cornell
University Press.
[35] Luciano Floridi and Massimo Chiriatti. 2020. GPT-3: Its nature, scope, limits,
and consequences. Minds and Machines 30 (2020), 681–694.
[36] Miranda Fricker. 1998. Rational authority and social power: Towards a truly
social epistemology. In Proceedings of the Aristotelian Society . JSTOR, 159–177.
[37] Miranda Fricker. 2007. Epistemic injustice: Power and the ethics of knowing .
Oxford University Press.
[38] Miranda Fricker. 2013. Epistemic justice as a condition of political freedom?
Synthese 190 (2013), 1317–1332.
[39] Floriana Fusco, Marta Marsilio, and Chiara Guglielmetti. 2020. Co-production
in health policy and management: a comprehensive bibliometric review. BMC
health services research 20 (2020), 1–16.
[40] Timnit Gebru and Émile P Torres. 2024. The TESCREAL bundle: Eugenics
and the promise of utopia through artificial general intelligence. First Monday
(2024).
[41] Jonathan Grant, Robert Cottrell, Françoise Cluzeau, and Gail Fawcett. 2000. Eval-
uating “payback” on biomedical research from papers cited in clinical guidelines:
applied bibliometric study. Bmj 320, 7242 (2000), 1107–1111.
[42] Carolina Guzmán-Valenzuela. 2019. Values and the international collaborative
research in higher education: Negotiating epistemic power between the Global
South and the Global North. Values of the University in a Time of Uncertainty
(2019), 137–153.
[43] Stuart Hall et al . 1997. The spectacle of the other. Representation: Cultural
representations and signifying practices 7 (1997).
[44] Karen Hao. 2022. Artificial intelligence is creating a new colonial world order.
MIT Technology Review (April 19 2022). https://www .technologyreview.com/
2022/04/19/1049592/artificial-intelligence-colonialism/ Accessed: 2025-01-11.
[45] Sandra Harding. 2008. Sciences from below: Feminisms, postcolonialities, and
modernities. Duke University Press.
[46] Qin He. 1999. Knowledge discovery through co-word analysis. (1999).
[47] Vaughan Higgins, Melanie Bryant, Andrea Howell, and Jane Battersby. 2017. Or-
dering adoption: Materiality, knowledge and farmer engagement with precision
agriculture technologies. Journal of Rural Studies 55 (2017), 193–202.
[48] Stephen Hilgartner. 2004. Mapping systems and moral order: Constituting
property in genome laboratories. In States of Knowledge . Routledge, 131–141.
[49] Soraj Hongladarom and Jerd Bandasak. 2024. Non-Western AI ethics guidelines:
Implications for intercultural ethics of technology. Ai & Society 39, 4 (2024),
2019–2032.
[50] Sheila Jasanoff. 2001. Image and Imagination: The Emergence of Global Envi-
ronmental Consciousness. In Changing the Atmosphere: Expert Knowledge and
Global Environmental Governance , Clark A. Miller and Paul N. Edwards (Eds.).
MIT Press, Cambridge, MA.
[51] Sheila Jasanoff. 2004. The idiom of co-production. In States of knowledge .
Routledge, 1–12.
[52] Sheila Jasanoff. 2004. Ordering knowledge, ordering society. In States of knowl-
edge. Routledge, 13–45.
[53] Sheila Jasanoff. 2015. Future imperfect: Science, technology, and the imagina-
tions of modernity. Dreamscapes of modernity: Sociotechnical imaginaries and
the fabrication of power (2015), 1–33.
[54] Jackie Kay, Atoosa Kasirzadeh, and Shakir Mohamed. 2024. Epistemic injustice
in generative ai. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and
Society, Vol. 7. 684–697.
[55] Emre Kazim and Adriano Soares Koshiyama. 2021. A high-level overview of AI
ethics. Patterns 2, 9 (2021).
[56] Jane Knight. 2022. Analysing Knowledge Diplomacy and Differentiating It from
Soft Power and Cultural, Science, Education and Public Diplomacies. The Hague
Journal of Diplomacy 18, 4 (2022), 654–686.
[57] Angelie Kraft and Eloïse Soulier. 2024. Knowledge-Enhanced Language Mod-
els Are Not Bias-Proof: Situated Knowledge and Epistemic Injustice in AI. In
Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Trans-
parency. 1433–1445.
[58] Neha Kumar and Naveena Karusala. 2021. Braving citational justice in human-
computer interaction. InExtended Abstracts of the 2021 CHI Conference on Human
Factors in Computing Systems . 1–9.
[59] Can Kurban, Ismael Peña-López, and María Haberer. 2017. What is technopol-
itics? A conceptual schema for understanding politics in the digital age. IDP.
Revista de Internet, Derecho y Política 24 (2017), 3–20.
[60] Vincent Larivière and Yves Gingras. 2010. The impact factor’s Matthew Effect:
A natural experiment in bibliometrics. Journal of the American society for
information science and technology 61, 2 (2010), 424–427.
[61] Stefan Larsson and Fredrik Heintz. 2020. Transparency in artificial intelligence.
Internet policy review 9, 2 (2020), 1–16.
[62] Sebastián Lehuedé. 2024. An elemental ethics for artificial intelligence: water
as resistance within AI’s value chain. AI & SOCIETY (2024), 1–14.
[63] Jason Edward Lewis, Angie Abdilla, Noelani Arista, Kaipulaumakaniolono Baker,
Scott Benesiinaabandan, Michelle Brown, Melanie Cheung, Meredith Coleman,
Ashley Cordes, Joel Davison, et al . 2020. Indigenous protocol and artificial
intelligence position paper. (2020).
[64] Michael Lynch. 2004. Circumscribing Expertise: membership categories in
courtroom testimony. In States of Knowledge . Routledge, 161–180.
[65] Bruce Macfarlane. 2011. Professors as intellectual leaders: Formation, identity
and role. Studies in Higher Education 36, 1 (2011), 57–73.
[66] Mirca Madianou. 2021. Nonhuman humanitarianism: when’AI for good’can be
harmful. Information, Communication & Society 24, 6 (2021), 850–868.
[67] Katherine W McCain. 1990. Mapping authors in intellectual space: A technical
overview. Journal of the American Society for Information Science (1986-1998) 41,
6 (1990), 433.
[68] Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram
Galstyan. 2021. A survey on bias and fairness in machine learning. ACM
computing surveys (CSUR) 54, 6 (2021), 1–35.
[69] Milagros Miceli, Martin Schuessler, and Tianling Yang. 2020. Between subjec-
tivity and imposition: Power dynamics in data annotation for computer vision.
Proceedings of the ACM on Human-Computer Interaction 4, CSCW2 (2020), 1–25.
[70] Stefania Milan and Emiliano Treré. 2019. Big data from the South (s): Beyond
data universalism. Television & New Media 20, 4 (2019), 319–335.
[71] Clark A Miller. 2004. Climate science and the making of a global political order.
In States of knowledge . Routledge, 46–66.
[72] Nusrat Jahan Mim, Dipannita Nandi, Sadaf Sumyia Khan, Arundhuti Dey, and
Syed Ishtiaque Ahmed. 2024. In-Between Visuals and Visible: The Impacts
of Text-to-Image Generative AI Tools on Digital Image-making Practices in
the Global South. In Proceedings of the CHI Conference on Human Factors in
Computing Systems . 1–18.
[73] Brent Mittelstadt. 2019. Principles alone cannot guarantee ethical AI. Nature
machine intelligence 1, 11 (2019), 501–507.
[74] Shakir Mohamed, Marie-Therese Png, and William Isaac. 2020. Decolonial AI:
Decolonial theory as sociotechnical foresight in artificial intelligence.Philosophy
& Technology 33 (2020), 659–684.
[75] James Muldoon and Boxi A Wu. 2023. Artificial intelligence in the colonial
matrix of power. Philosophy & Technology 36, 4 (2023), 80.
[76] Tolúlopé Ògúnrèmí, Wilhelmina Onyothi Nekoto, and Saron Samuel. 2023. De-
colonizing nlp for “low-resource languages”: Applying abebe birhane’s relational
ethics. GRACE: Global Review of AI Community Ethics 1, 1 (2023).
[77] Anaelia Ovalle, Arjun Subramonian, Vagrant Gautam, Gilbert Gee, and Kai-Wei
Chang. 2023. Factoring the matrix of domination: A critical review and reimagi-
nation of intersectionality in ai fairness. In Proceedings of the 2023 AAAI/ACM
Conference on AI, Ethics, and Society . 496–511.
[78] Antonio Perianes-Rodriguez, Ludo Waltman, and Nees Jan Van Eck. 2016. Con-
structing bibliometric networks: A comparison between full and fractional
counting. Journal of informetrics 10, 4 (2016), 1178–1195.
[79] Marie-Therese Png. 2022. At the tensions of south and north: Critical roles of
global south stakeholders in AI governance. In Proceedings of the 2022 ACM
2019

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Conference on Fairness, Accountability, and Transparency . 1434–1445.
[80] Christian Pohl, Stephan Rist, Anne Zimmermann, Patricia Fry, Ghana S Gurung,
Flurina Schneider, Chinwe Ifejika Speranza, Boniface Kiteme, Sébastian Boillat,
Elvira Serrano, et al . 2010. Researchers’ roles in knowledge co-production:
experience from sustainability research in Kenya, Switzerland, Bolivia and
Nepal. Science and public policy 37, 4 (2010), 267–281.
[81] Bridget Pratt and Jantina De Vries. 2023. Where is knowledge from the global
South? An account of epistemic justice for a global bioethics. Journal of medical
ethics 49, 5 (2023), 325–334.
[82] Alan Pritchard. 1969. Statistical bibliography or bibliometrics. Journal of
documentation 25 (1969), 348.
[83] Miriam Prys-Hansen. 2023. The global south: a problematic term. Internationale
Politik Quarterly (2023).
[84] Rida Qadri, Renee Shelby, Cynthia L Bennett, and Emily Denton. 2023. AI’s
regimes of representation: A community-centered study of text-to-image models
in South Asia. In Proceedings of the 2023 ACM Conference on Fairness, Account-
ability, and Transparency . 506–517.
[85] Stephanie Carroll Rainie, Tahu Kukutai, Maggie Walter, Oscar Luis Figueroa-
Rodríguez, Jennifer Walker, and Per Axelsson. 2019. Indigenous data sovereignty.
(2019).
[86] Mohammad Rashidujjaman Rifat, Abdullah Hasan Safir, Sourav Saha, Ja-
hedul Alam Junaed, Maryam Saleki, Mohammad Ruhul Amin, and Syed Ishtiaque
Ahmed. 2024. Data, Annotation, and Meaning-Making: The Politics of Cate-
gorization in Annotating a Dataset of Faith-based Communal Violence. In The
2024 ACM Conference on Fairness, Accountability, and Transparency . 2148–2156.
[87] Abdullah Hasan Safir. 2025. Dataset three. https://doi .org/10.6084/
m9.figshare.29045321. Accessed: 2025-05-13.
[88] Abdullah Hasan Safir. 2025. Dataset two. https://doi .org/10.6084/
m9.figshare.29045270. Accessed: 2025-05-13.
[89] Edward Said. 1978. Orientalism. Pantheon Books.
[90] Edward Said. 1993. Culture and Imperialism . Chatto & Windus.
[91] Nithya Sambasivan, Shivani Kapania, Hannah Highfill, Diana Akrong, Praveen
Paritosh, and Lora M Aroyo. 2021. “Everyone wants to do the model work, not
the data work”: Data Cascades in High-Stakes AI. In proceedings of the 2021 CHI
Conference on Human Factors in Computing Systems . 1–15.
[92] Martina Sardelli. 2022. Epistemic Injustice in the Age of AI. Aporia 22 (2022),
44–53.
[93] Ben Shneiderman. 2022. Human-centered AI . Oxford University Press.
[94] Gayatri Chakravorty Spivak. 1988. Can the Subaltern Speak? In Marxism
and the Interpretation of Culture , Cary Nelson and Lawrence Grossberg (Eds.).
Macmillan, Basingstoke, 271–313.
[95] Ganesh Surwase, Anil Sagar, BS Kademani, and K Bhanumurthy. 2011. Co-
citation analysis: An overview. (2011).
[96] John Symons and Ramón Alvarado. 2022. Epistemic injustice and data science
technologies. Synthese 200, 2 (2022), 87.
[97] Jasmina Tacheva and Srividya Ramasubramanian. 2023. AI Empire: Unraveling
the interlocking systems of oppression in generative AI’s global order. Big Data
& Society 10, 2 (2023), 20539517231219241.
[98] Doreen Tembo, Gary Hickey, Cristian Montenegro, David Chandler, Erica
Nelson, Katie Porter, Lisa Dikomitis, Mary Chambers, Moses Chimbari, Noni
Mumba, et al. 2021. Effective engagement and involvement with community
stakeholders in the co-production of global health research. bmj 372 (2021).
[99] Andreas Theodorou and Virginia Dignum. 2020. Towards ethical and socio-legal
governance in AI. Nature Machine Intelligence 2, 1 (2020), 10–12.
[100] Charis Thompson. 2004. Co-producing CITES and the African elephant. In
States of Knowledge . Routledge, 67–86.
[101] Nees Van Eck and Ludo Waltman. 2010. Software survey: VOSviewer, a computer
program for bibliometric mapping. scientometrics 84, 2 (2010), 523–538.
[102] Nees Jan Van Eck and Ludo Waltman. 2007. Bibliometric mapping of the
computational intelligence field. International Journal of Uncertainty, Fuzziness
and Knowledge-Based Systems 15, 05 (2007), 625–645.
[103] Nees Jan Van Eck and Ludo Waltman. 2014. Visualizing bibliometric networks.
In Measuring scholarly impact: Methods and practice . Springer, 285–320.
[104] Anthony FJ Van Raan. 2005. For your citations only? Hot topics in bibliometric
analysis. Measurement: interdisciplinary research and perspectives 3, 1 (2005),
50–62.
[105] Michael Veale, Kira Matus, and Robert Gorwa. 2023. AI and global governance:
modalities, rationales, tensions. Annual Review of Law and Social Science 19, 1
(2023), 255–275.
[106] Rick Vogel and Wolfgang H Güttel. 2013. The dynamic capability view in strate-
gic management: A bibliometric review. International Journal of Management
Reviews 15, 4 (2013), 426–446.
[107] Melanie Walker and Carmen Martinez-Vargas. 2022. Epistemic governance and
the colonial epistemic structure: Towards epistemic humility and transformed
South-North relations. Critical Studies in Education 63, 5 (2022), 556–571.
[108] Adrienne Williams, Milagros Miceli, and Timnit Gebru. 2022. The exploited
labor behind artificial intelligence. Noema Magazine 22 (2022).
[109] Alan Winfield. 2019. Ethical standards in robotics and AI. Nature Electronics 2,
2 (2019), 46–48.
[110] Wei Xu. 2019. Toward human-centered AI: a perspective from human-computer
interaction. interactions 26, 4 (2019), 42–46.
[111] Yi Zhang, Mengjia Wu, George Yijun Tian, Guangquan Zhang, and Jie Lu. 2021.
Ethics and privacy of artificial intelligence: Understandings from bibliometrics.
Knowledge-Based Systems 222 (2021), 106994.
A Appendix: Full-size images of 1 (a), 2 (a), 2(b),
3(a), 4(a) and 4(b) and top categories of
academic fields and venues represented in
our dataset
2020

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
Figure 5: Network visualisation of co-citation analysis of cited authors in AI Ethics (full size image of Fig. 1a)
Figure 6: Network visualisation of citational practices in AI Ethics among Global Institutions (full size image of Fig. 2a)
2021

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Figure 7: Network visualisation of co-authorship practices in AI Ethics among Global Institutions (full size image of Fig. 2b)
Figure 8: Network visualisation of co-word Analysis of academic literature in AI Ethics (full size image of Fig. 3a)
2022

Distributive Epistemic Injustice in AI Ethics FAccT ’25, June 23–26, 2025, Athens, Greece
Figure 9: Network visualisation of citational practices in AI Ethics among countries worldwide (full size image of Fig. 4a)
Figure 10: Network visualisation of co-authorship practices in AI Ethics among countries worldwide (full size image of Fig. 4b)
2023

FAccT ’25, June 23–26, 2025, Athens, Greece Safir et al.
Figure 11: Top categories of academic fields represented in our dataset (from WoS)
Figure 12: Top categories of academic venues represented in our dataset (from WoS)
2024
