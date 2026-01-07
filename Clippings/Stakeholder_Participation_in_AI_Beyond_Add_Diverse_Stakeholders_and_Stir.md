---
title: "Stakeholder Participation in AI Beyond Add Diverse Stakeholders and Stir"
authors:
  - Fernando Delgado
  - Stephen J.H. Yang
  - Michael Madaio
  - Qian Yang
year: 2021
type: document
doi: []
base: clippings
source: Manual
tags:
  - Tech/AI
last_enrichment_run: 2025-08-20
updated: 2025-08-20
apa_citation: Fernando Delgado et al., 2021
---

[[Stakeholder_Participation_in_AI_Beyond_Add_Diverse_Stakeholders_and_Stir.pdf]]

## PDF text extraction

Stakeholder Participation in AI:
Beyond “Add Diverse Stakeholders and Stir”
Fernando Delgado
Cornell University
fad33@cornell.edu
Stephen Yang
Cornell University
sy364@cornell.edu
Michael Madaio
Microsoft Research
michael.madaio@microsoft.com
Qian Yang
Cornell University
qianyang@cornell.edu
1 Introduction
Both AI and HCI communities increasingly call for more stakeholder participation in AI system
design, development, and maintenance [60, 56, 31, 59, 45]. Participation can allow AI systems to
better reﬂect their end users’ and stakeholders’ values, preferences, and needs. It can also help
scholars and practitioners to better anticipate and account for AI’s negative downstream impacts,
such as fairness and equity breakdowns [ 6, 25, 23, 42]. In parallel and responding to these calls,
participatory AI projects and research publications have started to emerge across HCI and AI
communities [46, 34, 27].
Despite the growing consensus that end-users and stakeholders should participate, enormous varia-
tion and implicit disagreements exist among current approaches to participatory AI. For example,
researchers frequently described their approach as “participatory design workshops”, yet there is a
noticeable lack of discussion around the tactics deployed in these workshops [29, 53]. For example,
how did the workshops/interviews account for stakeholders’ diverse (and sometimes conﬂicting)
values? Whether or how were they more effective than focus groups and interviews in traditional
user-centered design or agile development processes? For AI practitioners who are interested in
taking a participatory approach to AI design/development, it remains challenging to assess the extent
to which a participatory tactic or process can actually achieve inclusiveness or fairness goals. For
researchers who are interested in advancing this participatory turn in AI, it remains challenging to
have a principled discussion about the pros and cons of existing approaches and how we might best
choose to do so in going forward [5].
This paper aims to add theoretical grounding, structure, and clarity to the emergent research discourses
around stakeholder participation in AI. Taking a lesson from early HCI work in integrating women’s
perspectives into a male-dominated curriculum, we cannot just add diverse end-users and stakeholders
“and stir. It takes work, new ways of thinking, and new kinds and methods of openness, to bring
substantively new voices into a conversation.” [35] This paper takes this proposition as a starting
place. We ﬁrst offer a brief overview of the many approaches to increasing participation elaborated in
HCI design, political theory, and social science research. We derive ﬁve dimensions of participation
that AI practitioners or researchers can readily use in assessing the extent to which any participatory
tactic or process meaningfully empowers stakeholders in AI design. Finally, we highlight three
challenges that practitioners face when taking participatory approaches to AI design. These ﬁndings
come from our analysis of 56 research publications on participatory AI, as well as 12 IRB-approved
semi-structured interviews with researchers and practitioners who had written one or more of these
publications. With these theoretical and empirical analyses, we hope to push forward a principled
discussion around stakeholder participation in AI design as a way to account for diverse human values
and ethics.
35th Conference on Neural Information Processing Systems (NeurIPS 2021), Sydney, Australia.
arXiv:2111.01122v1  [cs.AI]  1 Nov 2021

2 Navigating the Many Approaches to Stakeholder Participation
This paper aims to provide more clarity and structure to the research discourses around participatory
AI. As a ﬁrst step, we review the range of existing participatory approaches across HCI design,
political theory, and social science research. We ﬁrst highlight their differences, and then identify ﬁve
questions that these diverse approaches address (namely, ﬁve “dimensions of participation”).
2.1 Prior Approaches to Participation and Their Differences
• User-centered design: inquiring stakeholders during need ﬁnding and design evaluation.
Over the past decades, the double-diamond user-centered design process has become the most com-
mon design process in industry practices [7]. It actively engages with end users when technology
designers work to identify user needs and assess their design ideas [33, 40].
• Service design: understanding and shaping value propositions and interactions among stakeholders.
Service design shares many features with user-centered design, but expands the notion of the “users”
to other stakeholders impacted by the technology service [ 13, 14, 13]. Using methods such as
service blueprint and value stream mapping, service designers explicitly consider how their design
decisions impact of the constellation of stakeholders through explicit interactions or implicit value
propositions over time. Some scholars consider service design as “participatory” [47, 24].
• Participatory design (PD): mixing diverse voices and challenging power structures.
In user-centered design and service design, technology designers collect, synthesize, and translate
stakeholders’ diverse inputs into concrete design decisions. In contrast, PD aims to enable stake-
holders to provide direct inputs in technology design [19, 52]. For stakeholders–who typically are
not experts in the technology themselves–to provide valuable inputs, PD scholars highlight that
participation needs to “take place neither in the users’ domain nor in the technology developers’
domain” [37]. PD practitioners need to create a hybrid space that allows diverse stakeholders
to meaningfully contribute “ a mix of motivations, histories, and goals ” without a clear set of
“authority relations, incentives, and obligations” [28, 20]. Noteworthily, PD highlights the work of
uncovering and challenging existing “authority relations”, including both power structures between
technology designers and impacted stakeholders, as well as power dynamics among and within
each group of impacted stakeholders [37].
• Co-design: creative cooperation between stakeholders and technology designers across the whole
span of a design process [48, 54, 26]. While closely related to PD, co-design typically lacks its
explicitly political component [54].
• Action research: improving researchers’ capacities and processes [9]. Particularly relevant to
this work is participatory action research approaches, which engage stakeholders as co-inquirers
and co-construct research plans and interventions [55, 58, 21, 44]. This normative aim to improv-
ing research processes differentiates participatory action research from PD, despite their many
similarities [18]. Some recent HCI research has begun to adopt action research approaches [21, 20].
• Value-sensitive design: accounting for indirect stakeholders and moral values. Value-sensitive
design can seem similar to participatory design, yet with a particular emphasis on the ethical values
of direct and indirect stakeholders [15, 16]. While valuable and appealing, scholars have argued
that value-sensitive design broadens the scope of PD to an unmanageably large scale [4].
• Social choice theory and mechanism design: quantitative aggregation of stakeholder preferences.
Social choice theory focuses on identifying individuals’ preferences and developing an aggregated,
mathematical preference-ranking model (for example, polling and ranking individuals’ public policy
preferences) [50, 3, 51]. In recent years, the ﬁeld of mechanism design has translated this approach
into a framework for including stakeholders into algorithmic decision-making [1, 10, 22, 57].
• Participatory democracy and civic participation: involving citizens and stakeholders in a broad
range of civic decision making. Participatory democracy conceptualizes civic participation as a
spectrum, from least intense (e.g., stakeholders spectating or expressing preferences) to most intense
(e.g., deliberating, negotiating, or deploying expertise through dialogues) [2, 17, 43, 30, 8, 32].
• Deliberation theory: qualitatively weighing and discussing competing perspectives and policies.
Deliberation theory emerged in response to mechanistic approaches to aggregating stakeholder pref-
erences (e.g., social choice theory) [39, 11, 41]. It emphasizes the importance of bringing together
small groups of people to discuss and qualitatively weigh competing arguments for policies [11].
2

Figure 1: Tactics for increasing stakeholder participation in designing AI, from consulting to em-
powering. These are sequential decisions that AI practitioners and researchers need to make when
including stakeholders in their AI design and development decision-making.
2.2 Dimensions of Participation: An Analytical Framework
From the existing approaches to participation, we identify ﬁve questions that they collectively
address: Why is participation needed? What is on the table? Which stakeholders should be involved?
What form does their participation take? Finally (although this is cross-cutting across the other
questions), how is power distributed among the participating stakeholders and between stakeholders
and technology designers/engineers? These ﬁve questions can serve as a valuable analytical tool
for AI practitioners and researchers. They can help illuminate the often implicit differences across
the aforementioned existing approaches to and theories of participation. These questions also aid
practitioners in assessing the extent to which a chosen participatory tactic or process can indeed
meaningfully empower diverse stakeholders in their AI design (Figure 1).
Take “what form does participation take” as an example. If taking aSocial Choice Theory approach,
AI practitioners can poll stakeholders and mathematically aggregate and rank their preferences
afterwards [46, 22]. Advocates of Participatory Design traditions might argue that this polling-and-
preference-aggregation approach fails to account for the power imbalance between AI researchers and
stakeholders. The power to translate stakeholders’ high-level values and preferences into concrete
AI design decisions still lies in the hands of the researchers [36]. Participatory democracy research
offers additional alternative forms of participation, for example, AI researchers can bring together
3

stakeholders to deliberate merits and negotiate trade-offs of particular design decisions. They
can encourage stakeholders to provide evidence to support their policy preferences and to change
their preferences in light of new information as emphasized by advocates of Deliberation Theory
[39, 11, 12]. By synthesizing how different theories of participation addressed this question of “what
form does participation take”, researchers and practitioners can better consider a wide range of
options available, with awareness of their known strengths and weaknesses.
3 Mapping the Current Participatory Practices in Designing AI
We have identiﬁed a range of approaches to stakeholder participation in design (of policies, research,
and technology). We have also identiﬁed ﬁve dimensions with which AI practitioners can synthesize
this wide range of approaches to participation. In this section, we report on challenges and tensions
that AI practitioners face when making decisions along the dimensions we outline in Figure 1. These
tensions and challenges emerged from our analysis of participatory AI publications and interviews
with AI researchers and practitioners, providing key topics for workshop discussion and future
research in increasing stakeholder participation in AI.
Organizational mandates substantively constrain the scope of what is on the table and who is
involved. Interviewees across the industry, public sectors, and academia reported that top-down orga-
nizational constraints largely determined “what is on the table” and “which stakeholders are involved”
in their participatory AI projects. Corporations’, research teams’, and government agencies’ timelines,
priorities, mandates, and resource levels are often in tension with their desire to maximally empower
stakeholders. Multiple interviewees in the public sector, for example, described that legislative
efforts mandated the use of AI risk assessment tools [e.g., 49, 25]. Only how - not whether - AI will
be deployed is on the table for stakeholders in such cases. These observations raise crucial questions
for the HCI and AI communities: How can our larger organizational structures ensure meaningful
stakeholder participation, for instance, in deciding whether an AI should exist at all? How should
AI practitioners manage the timespan and nature of diverse stakeholder participation, in the context
of agile development cycles in industry and relatively short project and funding cycles in academia?
Participatory AI project owners exert executive authority in deciding tactics of participation.
Despite their intentions to empower stakeholders and democratize the AI design process, those who
“own” the participatory AI project had unparalleled authority in making decisions about participatory
approaches in practice (including the questions we pose in Figure 1). They often, if not always,
decided who are considered stakeholders, what role each stakeholder plays, how they interact, whether
they need to reach a consensus at the end, etc. These observations urge us to discuss what a more
democratic method might look like for deciding the approaches to stakeholder participation.
AI researchers and practitioners feel caught between a desire to fulﬁll an idealized vision
of empowered stakeholder participation and real-world constraint on time and resources.
Interviewees reported that they felt caught between an idealized, ambitious vision of stakeholder
empowerment and the practical constraints of time and resources. One interviewee described what
they viewed as an idealized version of participation as “an absurd argument... ”because “if I wanted
full participation meaning like I want this person literally coming to the ofﬁce with me and making
every decision with me and doing all these things, all of a sudden, they don’t have a life to live,
right?” In light of the unrealistic vision of “full participation”, participatory AI projects we surveyed
made expansive use of proxies as stand-ins for broader classes of stakeholders who are brought in
to provide a stakeholder voice to address discrete design challenges [cf. 38]. For example, a project
on educational AI asked educators to “think like they were [children’s] personas”, thereby helping to
design the AI for children. In another project described in our interviews, a stakeholder participated
in an AI design process by training a machine learning model of their value and preferences. This
model will vote for a resource allocation outcome on their behalf in the future, for an unspeciﬁed
amount of time, even if the stakeholder’s preferences change.
This tension between the ideal and pragmatic constraints of participation reveals crucial open research
questions. On the one hand, what constitutes a minimal level of meaningful participation, for instance,
when deciding whether or how human and algorithmic proxies might meaningfully represent the
values and preferences of a group of stakeholders? On the other, at what point do stakeholder
participation and empowerment reach a point of diminishing returns? Addressing these questions is a
vital next step in improving stakeholder participation in AI design and development practice.
4

References
[1] Rediet Abebe and Kira Goldner. Mechanism design for social good. AI Matters, 4(3):27–34,
2018.
[2] Sherry R Arnstein. A ladder of citizen participation. Journal of the American Institute of
planners, 35(4):216–224, 1969.
[3] Kenneth J Arrow. Social choice and individual values. Yale university press, 2012.
[4] Alan Borning, Batya Friedman, and P Kahn. Designing for human values in an urban simulation
system: Value sensitive design and participatory design. In Proceedings From the Eighth
Biennial Participatory Design Conference. Citeseer, 2004.
[5] Tone Bratteteig and Guri Verne. Does ai make pd obsolete? exploring challenges from artiﬁcial
intelligence to participatory design. In Proceedings of the 15th Participatory Design Conference:
Short Papers, Situated Actions, Workshops and Tutorial - Volume 2, PDC ’18, New York, NY ,
USA, 2018. Association for Computing Machinery.
[6] Munmun De Choudhury, Min Kyung Lee, Haiyi Zhu, and David A Shamma. Introduction to
this special issue on unifying human computer interaction and artiﬁcial intelligence. Human–
Computer Interaction, 35(5-6):355–361, 2020.
[7] Design Council. The ‘double diamond’ design process model. Design Council, 2005.
[8] John Dewey. {1927} The Public and Its Problems. Athens, OH: Ohio University Press, 1954.
[9] John Elliot. Action research for educational change. McGraw-Hill Education (UK), 1991.
[10] Jessie Finocchiaro, Roland Maio, Faidra Monachou, Gourab K Patro, Manish Raghavan, Ana-
Andreea Stoica, and Stratis Tsirtsis. Bridging machine learning and mechanism design towards
algorithmic fairness. In Proceedings of the 2021 ACM Conference on Fairness, Accountability,
and Transparency, pages 489–503, 2021.
[11] James S Fishkin and Robert C Luskin. Experimenting with a democratic ideal: Deliberative
polling and public opinion. Acta politica, 40(3):284–298, 2005.
[12] James S Fishkin and Jane Mansbridge. The prospects and limits of deliberative democracy:
Introduction. Daedalus, 146(3):6–13, 2017.
[13] Jodi Forlizzi. Moving beyond user-centered design. interactions, 25(5):22–23, 2018.
[14] Jodi Forlizzi and John Zimmerman. Promoting service design as a core practice in interaction
design. In Proceedings of the 5th International Congress of International Association of
Societies of Design Research-IASDR, volume 13, 2013.
[15] Batya Friedman. Value-sensitive design. interactions, 3(6):16–23, 1996.
[16] Batya Friedman, Peter Kahn, and Alan Borning. Value sensitive design: Theory and methods,
2002.
[17] Archon Fung. Varieties of participation in complex governance. Public administration review,
66:66–75, 2006.
[18] Janne Gleerup, Lars Hulgaard, and Simon Teasdale. Action research and participatory democ-
racy in social enterprise. Social Enterprise Journal, 2019.
[19] Judith Gregory. Scandinavian approaches to participatory design. International Journal of
Engineering Education, 19(1):62–74, 2003.
[20] Christina Harrington, Sheena Erete, and Anne Marie Piper. Deconstructing community-based
collaborative design: Towards more equitable participatory design engagements. Proceedings
of the ACM on Human-Computer Interaction, 3(CSCW):1–25, 2019.
[21] Gillian R Hayes. Knowing by doing: action research as an approach to hci. In Ways of Knowing
in HCI, pages 49–68. Springer, 2014.
5

[22] Zoë Hitzig. The normative gap: mechanism design and ideal theories of justice. Economics &
Philosophy, 36(3):407–434, 2020.
[23] Anna Lauren Hoffmann. Terms of inclusion: Data, discourse, violence. new media & society,
page 1461444820958725, 2020.
[24] Stefan Holmlid. Participative; co-operative; emancipatory: From participatory design to service
design, 2012.
[25] Ada Lovelace Institute, AI Now Institute, and Open Government Partnership. Algorithmic
accountability for the public sector report, 2021.
[26] Maaike Kleinsmann and Rianne Valkenburg. Barriers and enablers for creating shared under-
standing in co-design projects. Design Studies, 29(4):369–386, 2008.
[27] P. M. Krafft, Meg Young, Michael Katell, Jennifer E. Lee, Shankar Narayan, Micah Epstein,
Dharma Dailey, Bernease Herman, Aaron Tam, Vivian Guetler, Corinne Bintz, Daniella Raz,
Pa Ousman Jobe, Franziska Putz, Brian Robick, and Bissan Barghouti. An action-oriented ai
policy toolkit for technology audits by community advocates and activists. In Proceedings of
the 2021 ACM Conference on Fairness, Accountability, and Transparency, FAccT ’21, page
772–781, New York, NY , USA, 2021. Association for Computing Machinery.
[28] Christopher A. Le Dantec and Sarah Fox. Strangers at the gate: Gaining access, building rapport,
and co-constructing community-based research. In Proceedings of the 18th ACM Conference on
Computer Supported Cooperative Work & Social Computing, pages 1348–1358. ACM, 2015.
[29] Min Kyung Lee, Daniel Kusbit, Anson Kahng, Ji Tae Kim, Xinran Yuan, Allissa Chan, Daniel
See, Ritesh Noothigattu, Siheon Lee, Alexandros Psomas, et al. Webuildai: Participatory frame-
work for algorithmic governance. Proceedings of the ACM on Human-Computer Interaction,
3(CSCW):1–35, 2019.
[30] Walter Lippmann. The phantom public. Transaction Publishers, 1993.
[31] Daria Loi, Thomas Lodato, Christine T Wolf, Raphael Arar, and Jeanette Blomberg. Pd
manifesto for ai futures. In Proceedings of the 15th Participatory Design Conference: Short
Papers, Situated Actions, Workshops and Tutorial-Volume 2, pages 1–4, 2018.
[32] C. B Macpherson. Democratic theory: essays in retrieval . Clarendon Press, 1973. OCLC:
606090.
[33] Ji-Ye Mao, Karel Vredenburg, Paul W Smith, and Tom Carey. The state of user-centered design
practice. Communications of the ACM, 48(3):105–109, 2005.
[34] Donald Martin Jr, Vinodkumar Prabhakaran, Jill Kuhlberg, Andrew Smart, and William S Isaac.
Participatory problem formulation for fairer machine learning through community based system
dynamics. arXiv preprint arXiv:2005.07572, 2020.
[35] Michael J. Muller. Participatory Design: The Third Space in HCI, page 1051–1068. L. Erlbaum
Associates Inc., USA, 2002.
[36] Michael J Muller. Participatory design: the third space in hci. the humancomputer interaction
handbook: fundamentals, evolving technologies and emerging applications, 2002.
[37] Michael J Muller and Sarah Kuhn. Participatory design. Communications of the ACM, 36(6):24–
28, 1993.
[38] Dylan Mulvin. Proxies: The cultural work of standing in. MIT Press, 2021.
[39] PerOla Öberg. Deliberation. In Handbook on theories of governance. Edward Elgar Publishing,
2016.
[40] Judith S Olson and Wendy A Kellogg. Ways of Knowing in HCI, volume 2. Springer, 2014.
[41] David Owen and Graham Smith. Survey article: Deliberation, democracy, and the systemic
turn. Journal of Political Philosophy, 23(2):213–234, 2015.
6

[42] Scott Pobiner and Timothy Murphy. Participatory approaches to machine learning, 2018.
[43] Francesca Polletta. Freedom is an endless meeting. In Freedom Is an Endless Meeting .
University of Chicago Press, 2012.
[44] Lauge Baungaard Rasmussen. Action research—scandinavian experiences. AI & SOCIETY,
18(1):21–43, 2004.
[45] People + AI Research. Boundary objects for participatory machine learning: Pair symposium
2020 recap, November 2020.
[46] Samantha Robertson and Niloufar Salehi. What if i don’t like any of the choices? the limits
of preference elicitation for participatory algorithm design. arXiv preprint arXiv:2007.06718,
2020.
[47] Joanna Saad-Sulonen, Amalia De Götzen, Nicola Morelli, and Luca Simeone. Service design
and participatory design: time to join forces? In Proceedings of the 16th Participatory Design
Conference 2020-Participation (s) Otherwise-Volume 2, pages 76–81, 2020.
[48] Elizabeth B.-N. Sanders and Pieter Jan Stappers. Co-creation and the new landscapes of design.
CoDesign, 4(1):5–18, 2008.
[49] Devansh Saxena, Karla Badillo-Urquiola, Pamela Wisniewski, and Shion Guha. A framework
of high-stakes algorithmic decision-making for the public sector developed through a case study
of child-welfare. arXiv preprint arXiv:2107.03487, 2021.
[50] Amartya Sen. Social choice theory: A re-examination. Econometrica: journal of the Economet-
ric Society, pages 53–89, 1977.
[51] Amartya Sen. Social choice theory. Handbook of mathematical economics, 3:1073–1181, 1986.
[52] Jesper Simonsen and Toni Robertson. Routledge international handbook of participatory design.
Routledge, 2012.
[53] C Estelle Smith, Bowen Yu, Anjali Srivastava, Aaron Halfaker, Loren Terveen, and Haiyi Zhu.
Keeping community in the loop: Understanding wikipedia stakeholder values for machine
learning-based systems. In Proceedings of the 2020 CHI Conference on Human Factors in
Computing Systems, pages 1–14, 2020.
[54] Marc Steen. Co-design as a process of joint inquiry and imagination.Design Issues, 29(2):16–28,
2013.
[55] Kim M Unertl, Chris L Schaefbauer, Terrance R Campbell, Charles Senteio, Katie A Siek,
Suzanne Bakken, and Tiffany C Veinot. Integrating community-based participatory research
and informatics approaches to improve the engagement and health of underserved populations.
Journal of the American Medical Informatics Association, 23(1):60–73, 2016.
[56] Kush Varshney, Tina Park, Inioluwa Deborah Raji, Gaurush Hiranandani, Narasimhan Harikr-
ishna, Oluwasanmi Koyejo, Brianna Richardson, and Min Kyung Lee. Participatory speciﬁcation
of trustworthy machine learning, 2021.
[57] Salomé Viljoen, Jake Goldenfein, and Lee McGuigan. Design choices: Mechanism design and
platform capitalism. Big Data & Society, 8(2):20539517211034312, 2021.
[58] Nina B Wallerstein and Bonnie Duran. Using community-based participatory research to
address health disparities. Health promotion practice, 7(3):312–323, 2006.
[59] Christine T. Wolf, Haiyi Zhu, Julia Bullard, Min Kyung Lee, and Jed R. Brubaker. The changing
contours of "participation" in data-driven, algorithmic ecosystems: Challenges, tactics, and an
agenda. In Companion of the 2018 ACM Conference on Computer Supported Cooperative Work
and Social Computing, CSCW ’18, page 377–384, New York, NY , USA, 2018. Association for
Computing Machinery.
[60] Angela Zhou, David Madra, Inioluwa Deborah Raji, Bogdan Kylych, Smitha Mill, and Richard
Zemel. Participatory approaches to machine learning, 2020.
7
