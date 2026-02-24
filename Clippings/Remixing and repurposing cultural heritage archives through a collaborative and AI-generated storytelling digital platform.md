---
title: "Remixing and repurposing cultural heritage archives through a collaborative and AI-generated storytelling digital platform"
authors:
  - Pedro Almeida
  - Ana Teixeira
  - Ana Velhinho
  - Rui Raposo
  - Telmo Silva
  - Luis Pedro
year: 2024
type: journal-article
journal: "Proceedings of the 2024 ACM International Conference on Interactive Media Experiences Workshops"
doi: 10.1145/3672406.3672419
base: clippings
source: Crossref
tags:
  - op/doc/tool
  - themes/GLAM
  - Humanities/culturalHeritage
last_enrichment_run: 2025-08-20
pages: 100-104
publisher: ACM
url: https://doi.org/10.1145/3672406.3672419
apa_citation: Pedro Almeida et al., 2024
---

[[Remixing and repurposing cultural heritage archives through a collaborative and AI-generated storytelling digital platform.pdf]]

## PDF text extraction

Remixing and repurposing cultural heritage archives through a
collaborative and AI-generated storytelling digital platform
Pedro, A. F. S., Almeida
Digimedia, University of Aveiro
almeida@ua.pt
Ana, L. M., Teixeira
Digimedia, University of Aveiro
almt00@ua.pt
Ana, S., Velhinho
Digimedia, University of Aveiro
ana.velhinho@ua.pt
Rui, M. A., Raposo
Digimedia, University of Aveiro
raposo@ua.pt
Telmo, E. M. C., Silva
Digimedia, University of Aveiro
tsilva@ua.pt
Luís, F. M. G., Pedro
Digimedia, University of Aveiro
lpedro@ua.pt
ABSTRACT
With the digitization of archives, fragments of cultural heritage
are migrating to dedicated platforms and made available in curated
experiences that rely on the curators’ work. Polariscope proposes a
collaborative storytelling platform to share, visualize and co-create
collective memories. It aims to gather citizens and institutions to
promote rich digital experiences through interactive and narra-
tive visualizations around meaningful cultural events. The project
proposes a solution assisted by Artificial Intelligence (AI) able to
generate automatic stories based on these archives. The develop-
ment methodology and the architecture model of the integration of
AI tools are presented in the paper. The paper also presents some
promising preliminary results of user testing to achieve such a goal,
based on the development of an interaction protocol with GPT 3.5
for the creation of stories.

## Notes for digital libraries article
- **Process-driven**:
  - “Polariscope proposes a collaborative storytelling platform to share, visualize and co-create collective memories. It aims to gather citizens and institutions to promote rich digital experiences through interactive and narrative visualizations around meaningful cultural events.” (Abstract)
  - “The development methodology and the architecture model of the integration of AI tools are presented in the paper. The paper also presents some promising preliminary results of user testing to achieve such a goal, based on the development of an interaction protocol with GPT 3.5 for the creation of stories.” (Abstract)
  - “Within this scope, the Polariscope, an R&D project resulting from a consortium between academia and a municipal historical archive, proposes a collaborative storytelling platform to share, visualize and co-create collective memories.” (Introduction)
- **Methodological tools**:
  - “The project proposes a solution assisted by Artificial Intelligence (AI) able to generate automatic stories based on these archives. The development methodology and the architecture model of the integration of AI tools are presented in the paper.” (Abstract)
  - “The paper also presents some promising preliminary results of user testing to achieve such a goal, based on the development of an interaction protocol with GPT 3.5 for the creation of stories.” (Abstract)
- **Participation level**:
  - “Polariscope proposes a collaborative storytelling platform to share, visualize and co-create collective memories. It aims to gather citizens and institutions...” (Abstract)
  - “Designed as an online community that gathers citizens and institutions, the platform intends to promote rich digital experiences through interactive and narrative visualizations around meaningful cultural events and heritage data, presenting multimedia resources from archives and testimonies shared by people.” (Introduction)
  - Preliminary user testing noted in the abstract (interaction protocol with GPT 3.5).
- **Epistemic justice**:
  - “Cultural heritage values the collective memory of the population where each person has their own bit of information. Typically, such memories were shared in person-to-person interactions.” (Introduction)
  - “Designed as an online community that gathers citizens and institutions, the platform intends to promote rich digital experiences through interactive and narrative visualizations around meaningful cultural events and heritage data, presenting multimedia resources from archives and testimonies shared by people.” (Introduction)
CCS CONCEPTS
• Information systems; •Information systems applications;
• Multimedia information systems ; • Multimedia content
creation;
KEYWORDS
Artificial intelligence, Automatic stories, Collaborative storytelling,
Cultural heritage archives
ACM Reference Format:
Pedro, A. F. S., Almeida, Ana, L. M., Teixeira, Ana, S., Velhinho, Rui, M. A.,
Raposo, Telmo, E. M. C., Silva, and Luís, F. M. G., Pedro. 2024. Remixing
and repurposing cultural heritage archives through a collaborative and
AI-generated storytelling digital platform. InProceedings of the 2024 ACM
International Conference on Interactive Media Experiences Workshops (IMXw
’24), June 12, 2024, Stockholm, Sweden. ACM, New York, NY, USA, 5 pages.
https://doi.org/10.1145/3672406.3672419
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, topostonserversortoredistributetolists, requirespriorspecificpermission
and/or a fee. Request permissions from permissions@acm.org.
IMXw ’24, June 12, 2024, Stockholm, Sweden
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1794-9/24/06
https://doi.org/10.1145/3672406.3672419
1 INTRODUCTION
From the beginning of time, mankind has been able to perpetuate
fragments of its existence through the seemingly simple act of sto-
rytelling. It was, and still is, an essential activity for preserving
intangible cultural heritage and making sense of tangible cultural
patrimonywhichis,bydefault,fullofblankspacesrarelycompleted
without the information provided by stories shared by others. Cul-
turalheritagevaluesthecollectivememoryofthepopulationwhere
each person has their own bit of information. Typically, such mem-
ories were shared in person-to-person interactions. Stories were,
and still are, excellent means for such dissemination of culture.
With the digitalization of archives, fragments of cultural heritage
are categorized in dedicated platforms that play a very relevant role
in perpetuating the information. Regarding its dissemination to the
public, the information is usually exhibited in manually curated
experiences or made available through categorized search engines.
In emerging platforms, human-powered techniques, such as folk-
sonomic categorization, and machine-driven data processing using
Artificial Intelligence (AI), are expanding the possibilities for en-
richingandconnectinginstitutionaldigitalcollectionsandinformal
community archives [1]. Some cultural heritage online portals have
been using those strategies to increase audience awareness and en-
gagement towards digital archives, namely Google Arts & Culture,
the global showcase leveraged by the services of this tech giant, and
Europeana, the virtual library created in 2005 to make accessible
and give visibility to Europe’s cultural heritage. In these online
archives, the manual curated exhibitions play an important role
as alternatives to traditional face-to-face storytelling. But these
curations mostly rely on the users’ work to create stories. The
critical analysis of the conclusions provided by two relevant studies
memories [2] [3] regarding the benchmarking of this type of plat-
form reveals two relevant aspects: i) first, there is a clear promotion
of participatory approaches with audiences and the adoption of
digital storytelling strategies to empower the sector; ii) second,
however, there is a lack of platforms embracing solutions that can
automatically generate stories.
Within this scope, the Polariscope, an R&D project resulting
from a consortium between academia and a municipal historical
archive, proposes a collaborative storytelling platform to share,
visualize and co-create collective memories [4]. Designed as an on-
line community that gathers citizens and institutions, the platform
intends to promote rich digital experiences through interactive
and narrative visualizations around meaningful cultural events and
heritage data, presenting multimedia resources from archives and
100


IMXw ’24, June 12, 2024, Stockholm, Sweden Pedro Almeida et al.
testimonies shared by people. The project aims to provide a place
for participatory sharing and to assist participants in co-creating
scenarios. Also, the project aims to assist archive promoters in au-
tomatically processing media fragments to create stories that may
be able to share the collective memories attached to such archives.
Additionally, the team proposes to develop a solution assisted by AI
tools that may be able to generate automatic stories based on these
archives. Moreover, it aims to try to integrate narrative principles
in order not only to create stories that can reflect the archives but
also to create more compelling stories that appeal to viewers.
This paper proposes a solution assisted by recommendation tools
and generative AI to create compelling stories around significant
cultural heritage assets presented in multimedia formats. Some
preliminary results, including the development of an interaction
protocolwithGPT3.5andusertestingofAI-generatedstoriesbased
on controlled datasets, are also presented to grasp future work to
the development of a functional prototype.
2 STATE OF THE ART
Cultural heritage is being digitalized, with multiple solutions being
created to help preserve relevant content and make it available
using digital exhibitions and curated presentations. Emergent ad-
vances like AI provide opportunities to expand how these archives
can be presented [1]. Therefore, this section includes the highlights
of two relevant studies regarding visualization and digital story-
telling trends, and the analysis of AI solutions that may provide an
opportunity for new ways to tell stories about cultural heritage.
Considering the communication of digital collections to a broad
audience, the focus of the large aggregating portals of cultural
and artistic heritage, namely Google Arts & Culture1 and Euro-
peana2, has been the use of playful approaches, based on games
and challenges, that put users in contact with the works and in-
formation about them. Google Arts & Culture stands out with the
possibility of geographic exploration (using Maps, Street View and
360ºtechnology), as well as providing semantic correlations and
recommendations based on the user’s activity. In the case of the Eu-
ropeana portal, providing extensive digital collections, it explores
disruptive initiatives such as the annual GIF IT UP – Remixing
Cultural Heritage competition3, which values the emotional dimen-
sion of appropriations and derivations produced by users to give
visibility in social networks to resources from digital collections.
These dynamics inherent to an increasingly participatory culture
[5] have led the institutions of memory, referred to as GLAM (gal-
leries, libraries, archives, museums), to adapt their ways of working
and brought the opportunity to direct people’s participation to en-
rich collections and integrate community archives with records of
personal stories and experiences [6].
2.1 Visualization and Storytelling in Cultural
Heritage Collections
To gain an overview of current and future trends in the use of
visualization and storytelling approaches applied in projects and
platforms linked to cultural heritage, two studies were considered.
1https://artsandculture.google.com/
2https://www.europeana.eu/pt
3https://gifitup.net/en/
Thesestudies werechosen because both arefocusedon applications
adopted in the field by well-established GLAM institutions. Addi-
tionally, both studies are relevant because one of the studies was
held by a Europeana task force, which is an authoritative repository
inthefield[ 2], andtheotherstudyregardsspecificallyvisualization
strategies within cultural heritage online applications [3]. These
studies map some characteristics of user profiles, tasks, types of
content, forms of presentation, modalities of interactivity, as well
as narrative approaches.
The visualization study [3] synthetizes practices linked to her-
itage from a sample of 70 cases, including academic research and
implemented web-based products. Based on the results, the authors
propose seven interrelated concepts to address future trends and
challenges within the scope of visualization interfaces for cultural
heritage: 1)Serendipity – focusing on curiosity through more open
experiences; 2) Generosity – promoting richest, most accessible
and contextualized presentation and navigation with quality infor-
mation, from multiple perspectives and different levels of detail
and favouring the participation of casual users; 3)Criticality –
supporting interpretative approaches to cultural objects, through
visualization interfaces that promote plurality and appropriation
by users; 4)User guidance and narration – using strategies to enrich
visualizations of open exploration by the user, including sharing
of personal stories; 5)Remote or in-person access – using various
types of digital access interfaces; 6)Uncertainty – recognizing the
need for rigor face to the imprecision, ambiguity and interpretative
openness of data and metadata; 7)Contextualization – considering
emerging linked open-data standards making available structured
and quality databases, to enhance correlated visualizations.
As for the storytelling study [2], it identifies and analyses ex-
amples of digital storytelling approaches implemented by entities
linked to cultural heritage, and proposes guidelines and recommen-
dations, including seven digital storytelling tips: 1)Be personal –
Personal stories can evoke the past and help the audience relate to
the story on an emotional level; 2)Be informal but expert – Overly
technical and academic language can put people off, but stories
shouldn’t be impoverished; 3)Tell those hidden stories – Giving
visibility to inaccessible heritage and stories that have not yet been
told by involving the public and creating a sense of community,
identity and shared history; 4)Illustrate your points – How visuals
and text work together in the stories; 5)Signpost your journey –
Digital storytelling requires having a clear sense of the narrative
structure, from beginning to end; 6)Be specific – It often works best
to move from specific details and topics to the big picture; 7)Be
evocative –Itispossibletoenrichstoriesthroughpoetic, descriptive
and evocative images and approaches.
In both studies [2] [3] there was still limited user participation,
particularly in terms of contributing with content, despite some
story creation and curation features being explored based on re-
sources from the collections. In both studies, most cases were
somewhat lacking innovative approaches in terms of participation
and co-creation features, continuing to provide low autonomy. In
addition, these cases also take little advantage of current advances
in AI in creative domains, whether at a generative level or in its
potential to assist in the curation of content and the creation and
presentation of stories, taking away benefit from more powerful
processing and semantic correlation.
101

Remixing and repurposing cultural heritage archives through a collaborative and AI-generated storytelling digital platform IMXw ’24, June 12, 2024, Stockholm, Sweden
2.2 Digital storytelling and AI solutions for
content discovery and generation
Given the advances in AI, multiple tools and platforms using it
have emerged, particularly in storytelling. These tools, referred to
as storytellers, underwent state-of-the-art benchmarking to com-
prehend their characteristics and features. Storyteller tools have
diverse applications, including assisting writers in generating ideas,
creating presentations, and developing interactive stories.
Some of these platforms, such as “AI Dungeon”4, allow users to
get inside the story and interact with its environment and charac-
ters, similar to playing an adventure game and creating the char-
acters and environment themselves. Similarly, “NovelAI”5 enables
story creation through user-machine interaction, using a prompt
box for the user to guide the story. “NovelAI” allows users to
tinker with more advanced features regarding algorithm control,
such as randomness or creativity levels for the generated narrative.
Other platforms, like “Artflow”6, focus on generating an audiovi-
sual narrative, where users provide initial information (such as a
briefdescriptionofthestory, targetaudience, andstorytheme), and
the system generates multiple images accompanied by text, both of
which can be edited by the user. In this case, the result is a video
story displaying multiple images with captions and narration.
Additional tools, like “StoryscapeAI”7, allow users to insert an
initial prompt. After the story begins, users can continue writing
prompts for story generation or use suggested premade prompts.
For users who prefer a more classical format, platforms like “Story-
Bird”8 and “InstaNovel”9 generate narratives in book and chapter
formats, respectively. While the former allows users to edit text
and images, the latter does not, making it challenging to customize
the story. For users seeking a simple approach without requiring
an account or subscription, “AI Story Generator”10 enables users
to write a prompt with the story’s subject, and a story will be gen-
erated. Finally, another tool that allows the creation of stories but
in a presentation-like format is “Tome”. Like previously discussed
platforms, “Tome”11 generates a story based on the user’s prompt
but presents it in a style with multiple text or image boxes, all of
which are resizable and movable. Users can also add images and
videos and rearrange all the content, allowing a more flexible way
of displaying the story.
Based on this analysis, it was observed that the generated story
content was mostly fictional, even if based on actual events, which
could be problematic if the goal of a particular story were to be
factual. Additionally,inalltools,thecontentusedforthegeneration
of stories was external and not user-generated or user-uploaded
content to create and remix their own narratives.
3 THE POLARISCOPE PROPOSAL
Considering the identified limitations on visualization and digi-
tal storytelling solutions targeted at cultural heritage content, the
4https://play.aidungeon.com/
5https://novelai.net/
6https://app.artflow.ai/story-gallery
7https://storyscapeai.app/
8https://storybird.ai/
9https://instanovel.ai/
10https://www.aistorygenerator.org/
11https://tome.app/
Polariscope project proposes a collaborative storytelling platform
to share, visualize and co-create collective memories. It aims to
gather citizens and institutions in an online platform intended to
promote rich digital experiences through interactive and narrative
visualizations around meaningful cultural events and heritage data
[4]. These narrative visualizations may be created by users, but
it is the team’s goal to incorporate AI solutions to assist them in
co-creation scenarios, for example, by providing content recom-
mendations during curation activities. Moreover, our purpose is
to assist even more in the storytelling role of the platform by au-
tomatically processing media fragments and integrating narrative
principles to create more compelling stories that can appeal to
viewers. Currently, we are working with two universities and Por-
tuguese GLAM institutions using human-centred and participatory
design methodologies, namely focus groups, user research and user
experience evaluations. The next steps include field trials during
events in partnership with these stakeholders, aiming at a possible
future adoption of this platform by cultural institutions.
3.1 Methodology and architecture model
With storytelling at its core, the Polariscope platform relies on mul-
timodal types of content (text, images, videos, and audio) derived
from digital archives and users’ uploads, leading to the co-creation
of new stories and add-on contributions to existing stories. Each
content is enriched with metadata, typically time, place, keywords,
and a description (what, where, when, how, why, and how) that
helpstoputthestoryintocontext. Butweneedtoconsiderthatthis
information may not be available in every content. Additionally, it
is also important to note that the content submitted to the platform
will be available to the public in multiple visualization formats
allowing interaction around the content (e.g. likes, comments or
upload of related content.). Therefore, the social activity around
each content is also information to be taken into consideration.
Bearing this in mind, the team proposes a solution that integrates
several AI tools aiming to create stories prompted by bits of content
(Figure 1).
Figure 1 provides an overview of the solution being planned
within the Polariscope as a digital storyteller making use of a set of
AI tools to assist in different stages from metadata enrichment to
content recommendation and generative.
In Step 1, a metadata extraction module will examine any type
of media (image, video, audio, or text) uploaded to the platform
and, in the case of some of the metadata missing, it will extract
complementary metadata. The metadata will be extracted using
AI-based tools, such as keyword extraction12 (for text), object de-
tection13 (for image and video) and speech-to-text14 operations
combined with keyword extraction (for audio). These tools will
be applied using EdenAI’s APIs that are available for developers
to easily integrate into projects, each of them presenting a list of
providers such as Amazon, Google and IBM that process the given
media. The extracted metadata will be added to the database and
combined with the metadata uploaded by the user. Additionally,
since the content may be integrated into multiple collections of the
12https://app.edenai.run/bricks/text/keyword-extraction
13https://app.edenai.run/bricks/image/object-detection
14https://app.edenai.run/bricks/speech/asynchronous-speech-to-text
102

IMXw ’24, June 12, 2024, Stockholm, Sweden Pedro Almeida et al.
Figure 1: The architecture of the Polariscope storyteller.
platform, the social activity around each content will be also stored
as an additional metadata parameter (e.g. content popularity).
A second module, in Step 2, is responsible for identifying seman-
tic correlations between media content, taking into consideration
each content’s metadata. To provide these semantic correlations a
recommendation system will be integrated to assist users in discov-
ering content and providing useful information for the automatic
story creation engine.
Thefinalmodule, Step3, assistsintheprocessofcreatingcurated
stories, being that curation done by users or AI-generated. In
the case of user-created stories, the module will assist the user in
choosing which content to add to his story, providing suggestions
of media based on semantic correlations of the content already
available in the story and the possible following ones. In the case
of AI-generated stories, the recommendation engine will be used
for a preliminary selection of relevant content. This selection will
be sent to the generative module. For the generation of stories, the
team will make use of the OpenAI chat completions15 API for text
generation. For that, a set of prompts has been defined to allow the
contents to be analyzed and sorted into an engaging story to be
generated by the model.
3.2 Preliminary results and future work
As described in the previous section, several AI-driven tools are
being integrated into the Polariscope technical architecture. After
the extraction tools and the most suitable recommendation systems
have been identified and some tests done, the team is now carrying
out integration tests of module 3. Nevertheless, validations on the
technical solutions of modules 1 and 2 are still required (Figure 1).
Regarding specifically the automatically curated stories feature
in module 3, due to its complexity, a set of intermediate develop-
ments have already been made based on content processed by the
OpenAI API. To validate the preliminary results, user testing was
15https://platform.openai.com/docs/guides/text-generation/chat-completions-api
carried out, focusing exclusively on the quality of the text gener-
ated from images and texts on memories of cultural heritage topics
relevant to the project. The focus of the evaluation was the text
generated by AI (the story), built from a given number of media
from controlled datasets.
For the generation of stories with the OpenAI system, the GPT
3.5 model was adopted. The researchers developed a set of prompts
with the variation of theTemperature parameter (a GPT parameter
that allows the definition of the level of creativity in the generation
of texts by controlling the randomness in the choice of words by
the algorithm) for directly delivering the requests to Chat GPT, not
relying on a GenAI intermediary API. For the creation of stories, a
set of content (descriptions of images and texts) was shared with
Chat GPT. The EdenAI was used to extract missing information,
like generating short descriptions of images16 and keywords17 of
the media content to provide whenever this content lacked within
a supplied description.
The generated stories were assessed as to their interest and ap-
peal for communicating thematic memories through storytelling
to users. Users’ assessment requested scoring each generated text
on a 7-parameter scale of the most relevant parameters defined
by Fu et al. to evaluate components related to the correctness of
the text and its emotionality and potential involvement:Interest;
Engagement; Quality; Comprehensibility; Fluency; Informativeness;
and Accuracy [7].
The study involved 10 participants using non-probability conve-
nience sampling. The participants were higher education postgrad
students in the field of Communication Science Technologies, aged
between 18 and 35 years old. Although the participant’s highest
scores in the 7 parameters went for the texts with a higher Tem-
perature value (1) which corresponds to more creative outputs, in
the historical topic the sample ended up choosing as best text the
one with a lower Temperature (0,1) which had a lower total score
among the parameters, proving that this is not a linear or merely
16https://portal.vision.cognitive.azure.com/demo/image-captioning
17https://app.edenai.run/bricks/image/object-detection
103

Remixing and repurposing cultural heritage archives through a collaborative and AI-generated storytelling digital platform IMXw ’24, June 12, 2024, Stockholm, Sweden
rational choice. Results do not provide a clear indication of the
best Temperature value to use in the generation of the stories, hav-
ing assessed different preferences on the type of generated texts
depending on the original datasets, either those being memories
based on historical events or memories based on local festivities.
Participants diverged as to what they value, either objectivity and
formality or a more creative and approachable tone in the stories.
Nevertheless, the results showed that the generated stories pleased
participants.
Hence, further tests will consider the differences in the nature
and topic of the generated texts. Although all the texts used in this
study had an informative purpose, some seemed to apport a more
personal storytelling nature, while others came across as more
informative due to their historical and factual nature. These results
led the team to discuss the pros and cons of designing adaptative
Temperature-related options concerning text generation. In the
first case, the user would be able to choose the Temperature of the
generated text, while in the second case, the platform would learn
from users’ feedback and find the most suitable Temperature over
time. A bit along the lines of human feedback and Reinforcement
Learning principles [8] [9] [10].
The team also assessed the AI-generated stories in comparison
with manual-generated stories. Less than a third of the participants
were able to identify the texts generated by AI which may be con-
sidered a positive result of Polariscope’s engine to generate texts
based on predefined content, confirming results in other studies on
this issue [11] [12] [13] [14].
4 CONCLUSIONS
Delivering automatic and captivating stories to users is challeng-
ing but it can make a significant difference in promoting cultural
heritage digital archives. The way information is combined and
presented to users, and the user experience it provides, are cru-
cial. Therefore, the Polariscope project aims to create a disruptive
platform that combines multimedia content with compelling inter-
faces and great storytelling material. As a participatory platform,
Polariscope will allow the creation of manually curated content ex-
hibitions assisted by a recommendation engine that helps curators
choose the right content from the collaborative digital archive. It
will allow users to be storytellers of collective memories of mean-
ingfulevents. Havingthisinmindandalliedwiththedevelopments
in the AI field, a fully automated storyteller can be pursued. The
team is developing an engine that combines different AI-powered
tools, namely, to extract metadata from shared content, a recom-
mendation system that can establish semantic correlations between
content and a generative AI engine that can combine all informa-
tion into stories. Prototypes using ChatGPT and other AI tools are
being developed, and the first promising results are being achieved.
Further tests with the mobile app interface will be carried out, re-
garding the evaluation of the automatic stories and the assistant
aid in user-generated stories. Once developed, the platform will
be tested with different stakeholders in events that mobilize com-
munities into participation, by providing them with visualization
and storytelling features for sharing and remixing cultural heritage
media archives and people’s collective memories.
ACKNOWLEDGMENTS
This work is financially supported by National Funds through FCT
– Fundação para a Ciência e a Tecnologia, I.P., under the project
2022.04424.PTDC and the project UIDB/05460/2020.
REFERENCES
[1] Thiel, S., Bernhardt, J. C. (2020). AI in Museums: Reflections, Perspectives and
Applications, Bielefeld: transcript Verlag. https://doi.org/10.1515/9783839467107
[2] Europeana (2021). Europeana as A Powerful Platform for Storytelling
Task Force - Report and Recommendations. Europeana Network
Association. https://pro.europeana.eu/files/Europeana_Professional/
Europeana_Network/Europeana_Network_Task_Forces/Final_reports/
EuropeanaasaPowerfulPlatformforStorytellingReport.pdf
[3] Windhager, F., Federico, P., Schreder, G., Glinka, K., Dörk, M., Miksch, S. & Mayr,
E. (2019). Visualization of Cultural Heritage Collection Data: State of the Art and
Future Challenges. IEEE Transactions on Visualization and Computer Graphics,
vol. 25, no. 6: 2311-2330. https://doi.org/10.1109/TVCG.2018.2830759
[4] Velhinho, A., Almeida, P. (2023). POLARISCOPE – A Platform for the Co-creation
and Visualization of Collective Memories. Design, User Experience, and Usabil-
ity: 12th International Conference, DUXU 2023, HCII 2023 Proceedings, Part II.
Springer https://doi.org/10.1007/978-3-031-35696-4_20
[5] Jenkins, H. (2008). Convergence Culture. Where Old and New Media Collide.
New York, London: New York University Press.
[6] Velhinho, A., Almeida, P. (2023a). The Legacy of Collective Memory in Digi-
tal Culture: Digitisation, Cultural Mapping and Co-Creation. Comunicação e
Sociedade, 43. https://doi.org/10.17231/comsoc.43(2023).4344
[7] Fu, J., Ng, S. K., Jiang, Z., & Liu, P. (2023). GPTScore: Evaluate as You Desire.
arXiv. http://arxiv.org/abs/2302.04166
[8] Stiennon, N., Ouyang, L., Wu, J., Ziegler, D., Lowe, R., Voss, C., Radford, A.,
Amodei, D., & Christiano, P. F. (2020). Learning to summarize with human
feedback. Advances in Neural Information Processing Systems, 33: 3008–3021.
[9] Lee, H., Phatale, S., Mansoor, H., Lu, K., Mesnard, T., Bishop, C., Carbune, V., &
Rastogi, A. Rlaif (2023): Scaling reinforcement learning from human feedback
with AI feedback. arXiv. https://arxiv.org/abs/2309.00267
[10] Sharma, A., Keh, S., Mitchell, E., Finn, C., Arora, K., & Kollar, T. (2024). A Critical
Evaluation of AI Feedback for Aligning Large Language Models.arXiv. https:
//arxiv.org/abs/2402.12366
[11] Clark, E., August, T., Serrano, S., Haduong, N., Gururangan, S., Smith, N.A.
(2021). All That’s ‘Human’ Is Not Gold (2021). Evaluating Human Evaluation of
Generated Text. In: Zong, C., Xia, F., Li, W., e Navigli, R. (eds.) Proceedings of the
59th Annual Meeting of the Association for Computational Linguistics and the
11th International Joint Conference on Natural Language Processing (Volume 1:
7282–7296). Association for Computational Linguistics.
[12] Köbis, N., & Mossink, L. D. (2021). Artificial intelligence versus Maya Angelou:
ExperimentalevidencethatpeoplecannotdifferentiateAI-generatedfromhuman-
written poetry.Computers in human behavior,114, 106553.
[13] Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics for AI-
generated language are flawed.Proceedings of the National Academy of Sci-
ences,120(11), e2208839120.
[14] Kumar, R., & Mindzak, M. (2024). Who Wrote This? Detecting Artificial
Intelligence–Generated Text from Human-Written Text.Canadian Perspectives
on Academic Integrity,7(1). https://doi.org/10.55016/ojs/cpai.v7i1.77675.
104
