---
title: Linked Data for Digital Humanities
year: 2024
type: article
base: clippings
source: pdf
tags:
  - Tech/SemanticWeb
  - tech/LOD
  - Humanities/digitalHumanities
authors:
  - Nurmikko-Fuller, Terhi
---

Linked PDF file(s) for **LINKED OPEN DATA FOR DIGITAL HUMANITIES -- Nurmikko-Fuller, Terhi, -- Taylor & Francis (Unlimited), Abingdon, Oxon, 2024 -- Abingdon, Oxon ; -- 9781000929706 -- 634ba7ba88ebb41d81b1b47a38161bf1 -- Anna’s Archive**:

- [[Linked Data for Digital Humanities.pdf]]

## PDF text extraction

Linked Data for Digital Humanities 
Linked Open Data for Digital Humanities provides insights into how digital 
technologies can enrich and diversify humanities scholarship and make it 
pioneering in the digital age. 
Written in non-specialist language, the book illustrates how information is 
captured, published, represented, accessed, and interpreted using computational 
systems and, in doing so, shows how technologies actively shape the way we 
understand what we encounter. Focusing as it does on underlying Web architecture 
and projects accessible online, the book has an inherently international focus. 
The interdisciplinary case study examples include bibliographic data from works 
published in England between 1470 and 1700; literature from ancient Iraq; jazz 
performances, predominantly from the USA in the 1930s; and even reach as far 
as an alien, ﬁctional future. Whilst these case study examples span vast spatio-
temporal distances, they all share a common thread in the use of the Linked Data 
information publication paradigm. Using existing computer science methods, as 
well as processes such as ontology development and database design, the book 
also includes reﬂections on practical considerations and oﬀers advice about how 
to take institutional policies, socio-cultural sensitivities, and economic models into 
consideration when implementing Linked Data projects. 
Linked Open Data for Digital Humanities discusses technological issues in the 
context of humanities scholarship, bridging disciplines and enabling informed 
conversations across disciplinary boundaries. It will be of interest to humanities 
scholars, computer and data scientists, and library and information scientists. 
Dr Terhi Nurmikko-Fuller is Senior Research Fellow at the Centre for Social 
Research & Methods at the Australian National University. Her research focuses on 
interdisciplinary experimentation into ways digital technologies and computational 
methods can be used to support and diversify research in the humanities, arts, and 
social sciences in general, and in relation to public culture, including Web Science, 
and the cultural heritage sector in particular. Terhi’s publications centre on topics 
related to Linked Data but cover a range of others from the role of gamiﬁcation 
and informal online environments in education to 3D digital models of items in 
museums in the UK and Australia. 

 
 
 
 
 
  
 
   
 
Digital Research in the Arts and Humanities 
Founding Series Editors: Marilyn Deegan, Lorna Hughes and 
Harold Short 
Current Series Editors: Lorna Hughes, Nirmala Menon, Andrew 
Prescott, Isabel Galina Russell, Harold Short and Ray Siemens 
Digital technologies are increasingly important to arts and humanities research, 
expanding the horizons of research methods in all aspects of data capture, inves-
tigation, analysis, modelling, presentation and dissemination. This important se-
ries covers a wide range of disciplines with each volume focusing on a particular 
area, identifying the ways in which technology impacts on speciﬁc subjects. The 
aim is to provide an authoritative reﬂection of the ‘state of the art’ in technology-
enhanced research methods. The series is critical reading for those already engaged 
in the digital humanities, and of wider interest to all arts and humanities scholars. 
The following list includes only the most-recent titles to publish within the 
series. A list of the full catalogue of titles is available at: www.routledge.com/ 
Digital-Research-in-the-Arts-and-Humanities/book-series/DRAH 
Transformative Digital Humanities 
Challenges and Opportunities 
Edited by Mary McAleer Balkun and Marta Mestrovic Deyrup 
Medieval Manuscripts in the Digital Age 
Edited by Benjamin Albritton, Georgia Henley and Elaine Treharne 
Access and Control in Digital Humanities 
Edited by Shane Hawkins 
Information and Knowledge Organisation in Digital Humanities 
Global Perspectives 
Edited by Koraljka Golub and Ying-Hsang Liu 
Networks and the Spread of Ideas in the Past: 
Strong Ties, Innovation and Knowledge Exchange 
Edited by Anna Collar 
For more information about this series, please visit: https://www.routledge.com/Digital-Research-
in-the-Arts-and-Humanities/book-series/DRAH 

 
  
Linked Data for Digital 
Humanities 
Terhi Nurmikko-Fuller 

 
 
 
 
 
    
 
  
 
   
 
    
 
 
 
 
 
 
 
 
First published 2024 
by Routledge 
4 Park Square, Milton Park, Abingdon, Oxon OX14 4RN 
and by Routledge 
605 Third Avenue, New York, NY 10158 
Routledge is an imprint of the Taylor & Francis Group, an informa business 
© 2024 Terhi Nurmikko-Fuller 
The right of Terhi Nurmikko-Fuller to be identiﬁed as author of this work 
has been asserted in accordance with sections 77 and 78 of the Copyright, 
Designs and Patents Act 1988. 
All rights reserved. No part of this book may be reprinted or reproduced or 
utilised in any form or by any electronic, mechanical, or other means, now 
known or hereafter invented, including photocopying and recording, or in 
any information storage or retrieval system, without permission in writing 
from the publishers. 
Trademark notice: Product or corporate names may be trademarks or 
registered trademarks, and are used only for identiﬁcation and explanation 
without intent to infringe. 
British Library Cataloguing-in-Publication Data 
A catalogue record for this book is available from the British Library 
ISBN: 978-1-032-05515-2 (hbk) 
ISBN: 978-1-032-05518-3 (pbk) 
ISBN: 978-1-003-19789-8 (ebk) 
DOI: 10.4324/9781003197898 
Typeset in Times New Roman 
by Apex CoVantage, LLC 

 Tytöille – for the girls 



 Contents 
Preface  x 
 Context for This Book xi 
 How to Read This Book  xiii 
 Who Should Read This Book  xv 
 Structure of the Book  xvi 
 Conventions Used in This Book  xvii
 In Summary  xviii
Acknowledgements xx
 Abbreviations  xxii
 Bibliography xxv 
 1 A False Dichotomy 1 
1.1 Preamble  1
 1.2 Interdisciplinarity  2 
 1.3 Snow’ s Two Cultures  5 
 1.4 The Role of Humanities in Computer Science  10 
 1.5 Linked Data and the Humanities – A Perfect Pair? 12 
 1.5.1 The First Wittgenstein and the RDF Triple  13 
 1.5.2 The Second Wittgenstein and Explicit Statement of 
Facts 14 
 1.5.3 Foucault, Semantic Web, and Properties  16 
 1.5.4 Meaning Derived From Connections 17 
1.6 Conclusion 18
 Bibliography 21 
 2 Privacy, Ethics, and Trust 23 
2.1 Preamble  23 
 2.2 The Unavoidable Orwellian Reference  24 
 2.3 Privacy as a Right, Not a Privilege  26
 2.4 Privacy Paradox  28 
 2.5 Trusting Data Producers, Trusting Data Consumers  30 
  

viii Contents 
 2.6 Potential for Disaster  32 
 2.7 We Need to Talk About Strava  33 
 2.8 On the Questions of Ethics  36
 2.9 Conclusion 37
 Bibliography 39 
3  Closed But Not for Business  42
 3.1 Preamble 42 
3.2 Data 43
 3.2.1 Unreproducible Data  45
 3.2.2 Unstructured Data  46
 3.2.3 Ambiguous Data  47
 3.2.4 Incomplete Data  48
 3.2.5 Messy Data  49
 3.4 Openness 50
 3.4.1 Open Source  51
 3.4.2 Open Access  52
 3.4.3 Open Data  53 
3.4.4  Linked Open Data  54 
3.5  Be F AIR, and CARE  56 
3.6  To Be or Not to Be Open?  56 
3.7  Solutions Combining Accessible and Inaccessible Data  58 
3.8  Case Study: The ElePHãT  Project (Bibliographic 
Metadata) 59
 3.9 Conclusion 62
 Bibliography 64 
4  “Truth” and Bias  66
 4.1 Preamble 66 
4.2 Ontologies 67 
4.3  Bias in Ontologies  69 
4.4  Document Your Design  71 
4.5  Justify Your Choices  73 
4.6  Case Study: Old Babylonian Literature  75 
4.6.1  Choosing the Case Study  76 
4.6.2  Three Ox-Drivers of Adab  76
 4.6.3 Ontological Representation  77 
4.6.3.1  Material Objects in Museums  77
 4.6.3.2 Bibliographical Metadata  79
 4.6.3.3 Narrative Structure  79
 4.7 Conclusion 81
 Bibliography 84 

Contents i x 
5  Data Demands  86
 5.1 Preamble  86 
 5.2 The More Things Change  88 
 5.3 Bias in Tool Recommendations  90
 5.4 Diﬀ erent Demands of Diﬀ erent Technologies  93 
5.6  Case Study: JazzCats  94 
 5.6.1 Tabular Data: The Body and Soul Discography  95 
 5.6.2 Relational Databases to RDF: Weimar Jazz 
Database 96 
 5.6.3 Ready-Made RDF: Linked Jazz  97 
 5.6.4 Querying Across Three Datasets Using SP ARQL   97
 5.7 Conclusion 98
 Bibliography 101 
 6 Future Directions  103
 6.1 Preamble  103 
 6.2  The Non-Linear Approach to Discussing Linked Data in the 
Digital Humanities  104 
 6.3  The Tech-Focused Summary of Linked Data in the Digital 
Humanities 109
 6.4 Conclusion 115
 Bibliography 118
 Glossary 119
 Index 122 
 

 
 
 
 
  
 
 Preface 
This book discusses the Linked Data method in a critical theoretical framework, 
examined through a Digital Humanities lens. As described in Chapter 1 , Linked 
Data is a way of doing things; of making information available online using exist-
ing Web technologies and architecture. It is an information publication paradigm. 
The fundamental concept behind the method is that by making information avail-
able online in ways that are accessible to both humans and software agents, it will 
be possible to begin aggregating all the data that has been published online, or at 
least all the data that has been published online using this method. In order to do so, 
we need to publish information online as structured data – these datasets are then 
interlinked with each other, creating an interconnected network of information. 
Software agents can navigate this decentralised network (or “knowledge graph”) 
across disciplinary silos and datasets. The great aim of this method is that eventu-
ally, it will be possible to beneﬁt from collective and global knowledge: not just to 
visit webpages but for browsers to provide users with results to searches that give 
us answers, not just hyperlinks to sites with relevant content. The whole of the Web 
could become a database with truly global reach. 

 
 
 
 
  
 
  
 
 
 
  
  Context for This Book 
Technological development, implementation, and uptake do not occur in isolation. 
Institutional, social, political, and ﬁnancial considerations all play a role. By illus-
trating the ways information is captured, published, represented, accessed, and in-
terpreted using computational systems, this book shows how technologies actively 
shape the way we understand what we encounter online. We no longer live in a 
world where digital and computational technologies are built exclusively to repre-
sent analogue systems, but instead ﬁnd ourselves in a situation where these systems 
can have an eﬀect on determining what information is accessed and how. Trawling 
through a library’s card catalogues has been replaced by the goal of optimising our 
keyword searches on Google so that the correct link is displayed at the top – or at 
least “above the fold”.
1 Never has there been a greater need for digital literacy and 
critical evaluation of online content, or of the various processes utilised for knowl-
edge representation and information retrieval. 
Thirty years ago, Sir Tim Berners-Lee (the inventor of the HyperText Transfer 
Protocol, and thus accredited with being the inventor of the Web) had a vision of 
a global hypermedia system that could meaningfully capture the entirety of human 
knowledge across the world. The Web as we know it today has yet to (fully) reach 
this goal – the vast majority of the information we encounter online is available for 
human eyes as text, image, and multimedia, but behind the scenes, data structures, 
which can fail to grasp the necessary nuance of the information they hold, dictate 
the way we discover this content. 
Knowledge representation using graph structures is a powerful computational 
method. The largest and dominant companies on the Web (Google and Facebook, 
for example) have been implementing graph technologies for years, but little 
knowledge of this has trickled down to the public, or the academic community, 
that stands to gain from it. The terms “Linked Data” and “Semantic Web” have yet 
to be fully absorbed into the public vernacular to the same extent as other online 
phenomena and technologies, such as social media and algorithms; regular users 
do beneﬁt from these technologies but are rarely informed about them. 
This book addresses this knowledge gap in part and engages the reader in a jour-
ney of critical evaluation and practical implementation of one of the most powerful 
information publication paradigms the world has ever seen: Linked Data. The aim 

 
 
 
    
 
xii Context for This Book 
is to illustrate and explain the aﬀordances and the challenges of this technology, 
particularly as it applies to the Digital Humanities. 
Note 
1 “Above the fold” is a term with its origins in traditional (paper-based) media. The upper 
half of the front page of a newspaper still remains the location for the most important 
news story or eye-catching headline. In web development, the term is used to describe that 
initial top of a webpage, speciﬁcally content that is visible to the user without scrolling 
down the page or clicking on something. 

 
 
  
  
 
 
 
 
    
 
   
  
 
   
 
  
   
 
 
 
    
 
   
 How to Read This Book 
This book is a summary of heuristics from existing projects, navigating the space 
between theoretical possibilities and pragmatic implementation. In a very literal 
sense, it is a critical companion: “critical” not because it is exclusively negative, 
but because it incorporates analyses and discussions of the strengths and weak-
nesses of Linked Data. And, “companion”, because the aim of this book is to be 
read alongside technical manuals and handbooks, not instead of them. The aim is 
to show examples of existing projects, and explain how each has been aﬀected by 
various diﬀerent external considerations. As such, this book could potentially ben-
eﬁt anyone embarking on using Linked Data. 
There are many ways to amalgamate information (online or otherwise), and the 
Linked Data method is simply one of them. Similarly, there are many equally valid 
but diﬀerent methods for creating Linked Data, depending on the project’s aims, 
the team’s skills, and the availability of resources such as servers. This book does 
not propose to be a deﬁnite guide to the method of Linked Data (tools, activities, 
etc.) or oﬀer a set of step-by-step instructions to be followed to implement a pro-
ject. Rather, its purpose is to engage the reader in an informed conversation about 
methodology of Linked Data: the important things that surround this method, its 
guiding principles, the theory behind it, and our core values as practitioners. 
Other publications have already fulﬁlled the function of a technical manual for 
Linked Data methods speciﬁcally, ranging from the early works of Allemang and 
Hendler’s  Semantic Web for the Working Ontologist ( 2011 ) and  DuCharme’s 2013 
publication Learning SP ARQL; there is also Hyvönen’s handbook for Linked Data 
(2018), and a plethora of newer ones (often with speciﬁc foci), including Theo-
charis and Tsihrintzis’ 2023 volume Production and Publication of Linked Open 
Data: The Case of Open Ontologies; indeed there is a more recent publication from 
Hyvönen (2022 ), too. For galleries, libraries, archives, and museums (GLAM) sec-
tor data in particular, there are a number of projects and prototypes, but in terms of 
technical how-to guides, it is worth giving Seth van Hooland and Ruben Verborgh’s 
(2014 ) Linked Data for Libraries, Archives and Museums a go. These books oﬀer 
succinct summaries of terminologies, detailed explanations about processes, and 
oﬀer practical advice. This book seeks to mirror and complement all these publi-
cations and approaches by including extra-technical considerations (institutional 

 
 
  
 
 
 
 
 
  
xiv How to Read This Book 
policies, data access models, etc.) that aﬀect the Linked Data paradigm in the 
conversation. 
The chapters and case studies tackle separate issues and diﬀerent technical as-
pects of the Linked Data methodology. Although the chapters beneﬁt from comple-
mentary information and examples, it is possible to opt not to read the book as a 
single narrative from beginning to end, but instead to dip into the book, reading one 
chapter at a time, to dive in deep with one particular aspect. The technical aspects 
that build up to an increasingly comprehensive picture give the book an internal 
cohesion that mirrors the Linked Data workshop at the Digital Humanities Ox-
ford Summer School ( Nurmikko-Fuller, 2022 ): ﬁrst, the W3C standard Resource 
Description Framework (RDF) is introduced; this is followed by a description of 
ontologies and Web Ontology Language (OWL). The workﬂow and thus the chap-
ters in this book culminate in a description of SPARQL Protocol and RDF Query 
Language (SPARQL). 

 
 
 
 
 
 
 
 
 
 
  
  
  
 Who Should Read This Book 
An audience of academics and researchers, either involved in or interested in pur -
suing Linked Data as a tool – the “Linked Data curious” – was envisioned for 
this book. It is intended to fuel discussions of issues and topics that aﬀect Digital 
Humanities researchers (referred to henceforth as “DHers”) in general; of those 
that involve Linked Data in particular; of those that we should all be aware of as 
citizens of a Digital Data Economy. Computer scientists can gain an understanding 
of why a successful Linked Data project requires more than a shift from one pro-
gramming language to another (from JSON to JSON-LD); Humanities researchers 
can see ways in which Linked Data can support and enrich their existing research 
paradigms. This book has use for those who have yet to complete a Linked Data 
project and for those who want to expand their understanding of this technology 
and its aﬀordances and limitations beyond just what is technologically necessary 
and possible. 
For interdisciplinary researchers in Digital Humanities, the book provides im-
portant insights into how to take institutional policies, socio-cultural sensitivities 
and economic models into consideration when implementing their Linked Data 
projects. It will be both of use and of interest to students across a vast range of 
disciplines, in and out of the broad church of Digital Humanities: DHers should 
engage with the book as a discipline-driven discussion and collection of case study 
examples of successful collaborations reaching over various diﬀerent disciplinary 
borders. 
Written in non-specialist language, the book is intended to be of interest to data 
scientists, information professionals, library and information scientists, museums 
and cultural-heritage professionals, and historians of a vast range of specialisations 
looking for case study examples of the use of computational tools in their domains. 
It provides insights into how digital technologies can enrich and diversify tradi-
tional Humanities scholarship, and make it relevant and pioneering in the digital 
age. The aim was to keep the book suﬃciently light, and the expression of the ideas 
similarly suﬃciently clear to not deter any general reader who might be curious to 
ﬁnd out more or have a budding interest in Linked Data, or even more generally 
just the topics discussed throughout the book. 

  
 
  
  
     
 
 
 
 
 Structure of the Book 
The narrative begins by establishing the broader ﬁeld of Digital Humanities as 
the context in which the rest of the book is to be understood. Core concepts and 
jargon are sprinkled throughout the book, acronyms deﬁned where relevant and 
the nomenclature of the technology and the methodology deconstructed with the 
introduction of the idea they refer to. In doing so, it is possible to establish a shared 
vocabulary without overloading the text with jargon or details of technologies; 
to minimise miscommunication and discussions that are at cross-purpose. This 
is particularly important since the community of practice that has grown around 
this methodology has borrowed from others very generously: ontology, record, re-
source, subject, object, and so on. The list of words that mean diﬀerent things is 
long and needs to be explicitly articulated. 
Beyond the technological aspects, each chapter, in turn, examines a diﬀerent is-
sue, such as institutional policies, economic models of higher education establish-
ments and memory institutions, and the inherent biases of information structures 
such as databases. Case study examples in Chapters 3 , 4 , and 5 illustrate diﬀerent 
practical and pragmatic considerations that every Linked Data practitioner in the 
Humanities context (either at centre stage or on the periphery) should be aware of 
before commencing a project. The book ﬁnishes with a brief indulgence in future 
gazing: given all that we know now, where do we perceive Linked Data will take 
us next? 

  
 
      
 
 
 
  
 
  
 
 
 
  
 
 
 Conventions Used in This Book 
The following typographical conventions are used in this book: 
• Italics – for emphasis (as well as for titles and names of statues). 
• Courier New– to distinguish speciﬁc expressions of RDF, SPARQL queries, 
and ontology-related terminology from the main body of text. Sample data snip-
pets, code, and preﬁxes are similarly in this font. 
• Punctuation is outside of quote marks, unless incorporated into a string of char-
acters, for example, as the instance for the Objectin an RDF triple. 
• Most of the HTTP URIs mentioned in this book will not point to a page, video, 
image, audio ﬁle, or website. They represent abstract notions and the relation-
ships between things. Attempts to click on these (e.g. should they appear as 
hyperlinks in a PDF) will systematically and inevitably return a 404 error code. 
This is because these identiﬁers are uniform resource identiﬁers (URIs) and not 
uniform resource locators (URLs): they are not pointing to a speciﬁc location 
where a resource exists; there is no digital ﬁle, page, or other resource for the 
browser to display. Where possible, Example.org is used in URIs to emphasise 
the fact that they refer to illustrative examples. In some cases, the URIs are 
genuine examples of data from various projects and the base URI will reﬂect 
that. They will return a 404, for the reasons outlined earlier. 

  
 
 
 
 
  
 
 
 
 
 
 
   
  
  
 In Summary 
In this book, the Linked Data method and its processes will be described in the 
context of the Digital Humanities. The aim is to demystify key concepts to al-
low greater access and engagement with the technology. The aim is to enable an 
ever-increasing number of practitioners to beneﬁt from the computational power 
of Linked Data and graph databases. The book provides context and a critical 
framework for the thoughtful development of Linked Data project s. All of this is 
achieved through heuristics accumulated in various projects, each focusing on a 
diﬀerent area of investigation. 
Comprehensive engagement with the topic (Linked Data), particularly in its in-
terdisciplinary context (Digital Humanities), requires a robust understanding of 
both: we can only truly see the value of the method for the latter with a suﬃcient 
understanding of the opportunities and limitations of the former. We will need to 
explore the messy, complicated, incomplete, and ambiguous data of the Humani-
ties, and evaluate where (and how) Linked Data can (and cannot) be used to sup-
port scholarship and investigation. And, in turn, where these challenges of the data 
can be used to test the robustness of this technology itself. There is a lot to unravel, 
and each of the topics is, in and of itself, worthy of a multitude of volumes, not just 
a section in one book. 
Writing with the task of communicating the intricacies of Linked Data in the 
context of Digital Humanities to an interdisciplinary audience runs the risk of over-
simplifying to the point of confusion. With this potential ﬂaw in mind, the book 
deliberately steers away from providing the most detailed and speciﬁc technologi-
cal instructions, wishing to show only enough of the technology so that the reader 
can assess what is easy, what is hard, what is trivial, what is impossible. Reading 
this book might not provide all the technological skills required for the implemen-
tation of a fully ﬂedged Linked Data project, but it will provide suﬃcient knowl-
edge to enable those who are new to the method to understand what is happening. 
Further, it provides them the cognitive tools to critically evaluate the technology, 
and projects that have opted to utilise it. As such, the relevant technologies will be 
discussed at a level of diﬃculty that will, ideally, leave a sense that there are more 
things to uncover, that there are other, more technical and diﬃcult aspects still to 
discover. 

 
 
 
 
   
    
 
 
    
In Summary xix 
This level of understanding of Linked Data as a technology mirrors in many 
ways the thoughts and values of the Digital Humanities community, especially 
when it comes to computer science skills such as programming, writing code, and 
developing software. Although the community has not yet reached unilateral agree-
ment on the issue, James Gottlieb’s comments are compelling: 
You can’t be a digital humanist if you don’t understand the digital. That 
doesn’t mean you have to be able to code any more than being a scholar 
of French literature means you have to be able to write French literature. 
You just have to be able to understand the nuances of what you’re studying 
and how you are studying it. Otherwise, how can you properly interpret the 
results?
1 
In many ways, this is the idea that has scoped the extent of the technological 
engagement in this book: aiming to provide details at a level where they give suf-
ﬁcient information to enable critical engagement. 
Note 
1 www.jamesgottlieb.com/2012/03/08/coding-and-digital-humanities/. Accessed 02/05/2022. 

 
 
 
    
 
 
 
 
 
 
 
 
 Acknowledgements 
This book has been written on the traditional lands of the Ngunnawal and Ngambri. 
I acknowledge the Traditional Owners and Custodians of the lands on which I work 
and live, and pay my respects to Indigenous Elders past, present, and emerging. 
Sovereignty has never been ceded. Canberra sits on what always was and always 
will be Aboriginal land. 
I owe a huge debt of gratitude to a lot of people. The case studies, examples, and 
projects that are mentioned in this book are the result of collaborations, and I would 
like to thank all my amazing co-authors. I want to single out Dr David Weigl, 
Prof Stephen Downie, Dr Kevin Page, Pip Willcox, Prof Dave De Roure, and Prof 
David Bainbridge as colleagues who helped inform and develop my thinking and 
practical approaches to Linked Data in myriad contexts over several years, but in 
particular, in the ElePhãT project, discussed in Chapter 3 . To Prof Graeme Earl, Dr 
Nick Gibbins and Dr Mark Weal, who supervised my initial investigations into the 
world of Linked Data ( Chapter 4 ), and got me hooked on this methodology. 
Special thanks to Prof Paul Pickering, who deserves a whole paragraph. 
To date, I have taught the workshop that shares its name with this book at the 
Digital Humanities Summer School at the University of Oxford, UK, a total of 
seven times, and attended it once as a student. I want to acknowledge the partici-
pants of those workshops, for their questions have enabled and demanded that I 
inspect and investigate Linked Data from many diﬀerent perspectives. I want to 
thank John Pybus, Graham Klyne, and Dr Kevin Page (again!), for delivering that 
content with me, challenging my approaches where necessary and always provid-
ing a robust sounding board for testing out ideas. Thank you also to Megan Gooch 
and Prof Dave De Roure (again!), for not only making these opportunities for the 
Summer School happen, but also with the Gale Scholar Asia Paciﬁc Digital Hu-
manities Oxford Fellowship, another perfect opportunity to engage and develop 
my Linked Data skills and ideas, and to get to know other Linked Data in the 
Humanities folk. 
The LAWDI events of 2012 and 2013 were nothing short of fundamental to my 
academic development as a Linked Data methodologist and gave me a sense of 
belonging to a global community who were also – like me! – interested and excited 
about Linked Data. The organisers, funders, and participants to both those events 

 
  
 
   
  
 
Acknowledgements xxi 
deserve my thanks, but I will single out Associate Professor Sebastian Heath and 
Dan Pett, because they are the ones who made it happen for me. 
A very special thank-you to Dr Lily Withycombe and Cosi the Aussie, who 
together delivered on Lily’s promise to read every single sentence. To Dr Katrina 
Grant, for creating such a collegial and supportive environment in which I wrote 
this book and indeed all of the time in the Centre for Digital Humanities Research! 
A heartfelt thank-you to my family for their support and love: Äite ja Iskä, 
Markka, Sanna, Janne, Pekko, ja tietysti Jeﬀ – kaikki tukevat ihmiset. Uskon, että 
vuosien varrella kirjahyllyihinne päätyy lukemattomia mun kirjoituksia! Milla, 
Leah, Nella, ja Hannah – te olette maailman parhaimmat tyypit, ja muistakaa aina, 
että jos teidän tätinne pystyy kirjoittamaan kirjan, niin kyllä teistäkin jokaikinen 
aivan varmasti pystyy ihan mihin vaan. 

  
 
 
 
 
  
 
   
  
  
 
  
  
  
 
 
  
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 Abbreviations 
AI Artiﬁcial Intelligence 
AHRC Arts and Humanities Research Council (UK) 
AR Augmented Reality 
ARC Australian Research Council 
BBC British Broadcasting Corporation 
CARE Collective beneﬁt, Authority to control, Responsibility, Ethics 
CC Creative Commons 
CEO Chief Executive Oﬃcer 
CIDOC CRM International Council of Museums (ICOM)’s Conceptual 
Reference Model 
CITA Biblioteca Escolar Digital 
COVID-19 Illness caused by a virus called coronavirus 
CSIRAC Commonwealth Scientiﬁc and Industrial Research Automatic 
Computer 
CSIRO Commonwealth Scientiﬁc and Industrial Research Organisation 
CSV Comma Separated Value 
D2RQ D2RQ Platform 
DHer Digital Humanities Researcher 
EEBO-TCP Early English Books Online Text Creation Partnership 
EPSRC Engineering and Physical Sciences Research Council (UK) 
ETCSL Electronic Text Corpus of Sumerian Literature 
EU European Union 
FAIR Findable, Accessible, Interoperable, Reusable 
FOAF Friend of a Friend 
FOMO Fear of Missing Out 
FOR Field of Research (for the ARC) 
FRBR Functional Requirements for Bibliographic Records 
FRBRoo FRBR-Object-Oriented 
GDPR General Data Protection Regulation (EU) 
GLAM Galleries, Libraries, Archives, and Museums 
Go8 Group of Eight 
GPS Global Positioning System 
GUI Graphical User-Interface 

 
 
  
  
 
 
  
  
 
 
 
 
 
  
 
 
  
  
 
 
 
  
  
 
 
 
  
 
 
 
 
 
 
  
  
 
 
 
 
   
  
  
 
List of Abbreviations xxiii 
HASS Humanities, Arts, and Social Sciences 
HTDL HathiTrust Digital Library 
HTTP HyperText Transfer Protocol 
HTTPS Hypertext Transfer Protocol Secure 
IBM International Business Machines Corporation, a technology 
corporation 
IFLA International Federation of Library Associations and Institutions 
IFLA LRM IFLA Library Reference Model 
J-DISC Online Jazz Discography 
JISC Joint Information Systems Committee 
JSON JavaScript Object Notation 
JSON-LD JSON for Linking Data 
KR Knowledge Representation 
LGBTQIA+ Lesbian, Gay, Bisexual, Transgender, Queer, Intersex, Asexual, 
Pansexual 
MODS Bibliographic Metadata Ontology 
MADS Bibliographic Metadata Ontology (extension to MODS) 
MySQL Open-Source Relational Database Management System 
NEPOMUK Networked Environment for Personalized, Ontology-Based 
Management of Uniﬁed Knowledge  
NKOS Networked Knowledge Organisation Systems 
OCR Optical Character Recognition 
OWL Web Ontology Language 
PARADISEC Paciﬁc And Regional Archive for Digital Sources in Endangered 
Cultures 
PDF Portable Document Format 
PR Public Relations 
PROV-O Provenance Ontology 
QS Quantiﬁed Self 
RDBMS Relational database management system 
RDF Resource Description Framework 
RDFS RDF Schema 
RO Research Object Ontology 
SIG Special Interest Group 
SPARKLIS Query Builder with Natural Language Processing 
SPARQL SPARQL RDF and Query Language 
SQL Structured Query Language 
STEM Science, Technology, Engineering, Mathematics 
STEAM Science, Technology, Engineering, Arts, Mathematics 
SVO Subject-Verb-Object 
TEI Text Encoding Initiative 
TTL Terse RDF Triple Language (a syntax and ﬁle format for RDF) 
URI Uniform Resource Identiﬁer 
URL Uniform Resource Locator 
URN Uniform Resource Number 

 
 
 
  
 
  
xxiv List of Abbreviations 
VIAF Virtual International Authority File 
W3C World Wide Web Consortium 
WYSIWYG What You See Is What You Get 
XML eXtensible MarkUp Language 
Xpath XML Path Language 
XSLT Extensible Stylesheet Language Transformations 

  
 
   
 
 
  
 
 
  
  
 
  
  
 
 
 Bibliography 
Allemang, D., and Hendler, J. (2011). Semantic Web for the Working Ontologist: Eﬀective 
Modeling in RDFS and OWL. Elsevier. 
DuCharme, B. (2013). Learning SP ARQL: Querying and Updating With SP ARQL 1.1 . 
O’Reilly Media, Inc. 
Hyvönen, E. (2022). “Digital Humanities on the Semantic Web: Sampo Model and Portal 
Series”. Semantic Web, 1–16. 
Juloux, V . B., Gansell, A. R., and Di Ludovico, A. (eds.). (2018). CyberResearch on the 
Ancient Near East and Neighbouring Regions: Case Studies on Archaeological Data, 
Objects, Texts, and Digital Archiving. Leiden: Brill. 
Nurmikko-Fuller, T. (2022). “Teaching Linked Open Data Using Bibliographic Metadata”. 
Journal of Open Humanities Data, 8. 
Theocharis, S., and Tsihrintzis, G. A. (2023). “Production and Publication of Linked Open 
Data: The Case of Open Ontologies”. In Semantic Knowledge Modelling via Open Linked 
Ontologies. Artiﬁcial Intelligence-Enhanced Software and Systems Engineering , vol. 4. 
Springer. 
van Hooland, S., and Verborgh, R. (2014). Linked Data for Libraries, Archives and Muse-
ums: How to Clean, Link and Publish Your Metadata. Facet Publishing. 



 
    
 
      
  
    
 
   
  
   
  
   
 
  
 
 
 
   
   1 A False Dichotomy 
1.1 Preamble 
Auguste Rodin’s sculpture the Gates of Hell is a masterpiece. It can be seen at 
one of several possible locations worldwide (the three original bronze casts are 
in Paris, Philadelphia, and Tokyo, with later versions to be found in Zurich, Stan-
ford, Seoul, and Mexico City). It is a colossal piece, six metr es in height and four 
metres in width. It is not as much decorated with, but consisting of almost 200 ﬁ g-
ures, including the famous The Thinker and The Kiss but dozens of lesser-known 
ones too, such as Ugolino and His Children. Some of them are small (15 cm), and 
others are a metre or so. Several diﬀerent stories are played out in the Gates, all 
within their own space contributing to a cohesive (albeit chaot ic and sporadic) 
surface of the clearly deﬁned structure, one which is internally multifaceted and 
diverse. The shared narrative that binds them beyond the Gates is that all refer to 
the original context of Dante’s Inferno. All this internal complexity, which plays 
across two halves of one whole, makes the Gates of Hell an excellent metaphor for 
the interdisciplinarity of Digital Humanities. 
Those engaged in the practice of Digital Humanities regardless of their respec-
tive methodological approaches may chuckle at the thought of the Gates of Hell as 
a metaphor for the discipline. What sins, passions, and grievous lapses in judge-
ment led into the Hell that is interdisciplinary research? Perhaps the sentiment of 
abandoning all hope will ring true for some, at least at one time or other. But it is 
the heterogeneous mix of characters and literary motifs conﬁned within the whole 
of the sculpture that makes for an ideal visual representation for various granulari-
ties of the Digital Humanities. The ﬁgures (which diﬀer in shape and size) speak to 
the way research in the ﬁeld manifests as myriad individual projects that can (and 
do!) vary in scope and size; the topics and motifs represent the diversity of domains 
and methodologies represented and engaged with; and whilst this one monolithic 
thing consists in fact of many diverse things, these are nevertheless brought to-
gether through a cohesive shared context. Since the book is about Linked Data in 
the Digital Humanities, it might make sense to focus on one ﬁgure alone (naturally 
the analogy for this methodology would be The Thinker!), but rather than engage 
in such a myopic investigation from the beginning, it is necessary to understand the 
bigger picture – the wider context – in which the book sits. 
DOI: 10.4324/9781003197898-1 

 
    
 
 
   
   
  
 
 
 
  
 
 
  
 
  
  
  
 
 
2 A False Dichotomy 
At its simplest level, the Gates metaphor serves to illustrate that two parts are 
needed to make one meaningful whole: the gate itself consists of two doors that 
meet perfectly in the middle. In the context of Digital Humanities, it is the two aca-
demic disciplines of the Sciences and the Arts, which might seem as the unlikeliest 
of bedfellows and in so many ways worlds apart, which nevertheless come together 
perfectly. 
1.2 Interdisciplinarity 
Throughout the years, researchers in the Digital Humanities have repeatedly en-
gaged in what is the seemingly unachievable task of succinctly and absolutely de-
ﬁning the discipline. 
1 
Why do we as a discipline have such a need to deﬁne the ﬁeld, over and over? 
Or to put it another way, why does Digital Humanities as a ﬁeld defy deﬁnition? 
It has, after all, existed as a “discipline in its own right” (Schreibman et al., 2004 : 
xxiii) for almost two decades. In that time, it has undergone much growth, diver -
siﬁcation, and expansion. It has become more widely recognised, at least in North 
America and Europe. It clearly sits at the intersection of Humanities disciplines 
and computational technologies ( Schreibman et al., 2015 ; Svensson, 2010 ; and 
Burdick et al., 2016 ; Zeng, 2019 ), although the dividing lines can seem somewhat 
arbitrary at times (archaeology is in Humanities, palaeography is in the Sciences), 
whilst at others, the application of methodologies from one risks constituting 
poorly constructed research in the other, especially where the researchers applying 
these computational methods appear to suﬀer from hubris and a lack of expertise 
in the Humanities ﬁeld. The use of facial-recognition software on portraits, for ex-
ample de la Rosa and Suárez (2015 ), is harshly condemned by Bishop (2018 : 124) 
with the words “only to someone entirely unfamiliar with modernism would this 
[research ﬁnding] come as a surprise”. 
The issue here is that as a truly interdisciplinary ﬁeld, Digital Humanities incor-
porates (or has the potential to incorporate) any and all the myriad sub-disciplines 
that make up the behemoth domain of Humanities, Arts, and Social Sciences 
(HASS). Add to this all the possible methodologies and approaches from Science, 
Technology, Engineering, Mathematics (STEM) as well. The possible number of 
combinations makes the future directions of Digital Humanities investigation in-
crease exponentially in all directions at once. Even just focusing on the Humanities 
alone, we ﬁnd seemingly endless diﬀerent directions for investigation. This is un-
surprising, since this collection of disciplines covers vast diversity, the intellectual 
and academic equivalent of the Tropical Andes. Humanities scholars engaged in 
topics that range from examining pictographic cave paintings left by the earliest 
of our ancestors to evaluating portraits of human faces created by artiﬁcial intel-
ligence (AI) algorithms. The question then arises: In a ﬁeld that collectively maps 
and discusses domains and topics that together cover the entirety of the human ex-
perience, what unites us and gives a sense of comradery? Is it the shared struggle of 
wrangling the ambiguous, messy, and incomplete data (discussed more closely in 
Chapter 3 ) that characterises HASS subjects? That, and the absolute fundamental 

 
  
 
  
  
  
   
 
  
  
 
  
  
 
 
 
 
 
 
 
 
  
 3 A False Dichotomy 
recognition of the importance of critically evaluating the role of interpretation in 
analysis. 
Interdisciplinarity is, like Digital Humanities, a concept that seemingly deﬁes 
succinct deﬁnition. There are musings over the boundaries between inter-, multi-, 
and even trans-disciplinarity. It is diﬃcult to discuss transdisciplinarity as anything 
but the features shared across all academia: the need for digital infrastructure to 
enable students to submit their work; the policies that determine the number of 
international scholarships, and so on. But for inter- and multi-disciplinary ideas, 
the diﬀerentiation and the delivery of their promise is harder still. 
There may be a temptation to succumb to the types of non-deﬁnition as made 
famous by Potter Stewart (an associate justice of the Supreme Court, in the context 
of deﬁning obscenity, speciﬁcally in the context of a ﬁlm accused of containing 
pornography): “I shall not today attempt further to deﬁne the kinds of material I 
understand to be embraced within that shorthand description, and perhaps I could 
never succeed in intelligibly doing so. But I know it when I see it”.
2 Perhaps we 
can do one better. 
Arguably one of the simplest and most compelling analogies was ﬁrst presented 
in Repko and Szostak (2020 ): multidisciplinary is like fruit salad. The dish is unde-
niably a whole, it serves a purpose, it is clear in function, it is greater than the sum 
of its parts. . , but those composite parts are nevertheless separate. But beyond that, 
the speciﬁc parts of the salad are also changeable. A fruit salad will still be a fruit 
salad even if this particular one doesn’t have apples in it. Similarly, it is possible to 
take out all the chunks of oranges, but it is still a fruit salad. And, each component 
keeps itself a separate entity, even if consumed together. Academic panels are a 
good example: the panel is multidisciplinary, consisting of representatives from 
many diﬀerent areas, with speciﬁc aims, paradigms, areas of expertise, and so on. 
The next example is one of interdisciplinarity, and here the metaphor is of a fruit 
smoothie. There are many ingredients, all initially changeable, but, ultimately, in a 
blended drink, there is no way to remove a component. Both the strawberry and the 
banana are equally important, equally essential, and equally inherent in the com-
position of the smoothie. They have been broken down, and merged, fully mixed 
to such an extent that it is impossible to tell where one begins and the other ends. 
This approach has been the case with the skills and information acquisition among 
researchers in many successful Linked Data-driven Digital Humanities projects. 
Interdisciplinarity should be unequivocally supported in resea rch, teaching, 
and in every committee and panel. Many in the academy have been sold on the 
beneﬁts of interdisciplinarity for research, at least in theory: ce rtainly, there are 
funding opportunities and research council prerequisites to illustrate interdisci-
plinarity in investigatory teams. In the pedagogical context, i t might not be quite 
as universally embraced, and indeed interdisciplinarity may be easier to intro-
duce to postgraduate students who have a solid grounding in one home discipline. 
That having been said, interdisciplinary built into pedagogy can improve the de-
livery of authentic assessment ( Nurmikko-Fuller and Hart, 2020). For example, 
although Reeves et al. (2002 ) do not explicitly use the term, their criteria for 
success learning ticks many of the boxes of interdisciplinarity , such as asking 

 
 
 
 
 
  
 
 
 
 
 
     
 
 
  
  
 
 
 
 
 
  
   
 
 
 
  
  
4 A False Dichotomy 
students to examine the task from diﬀerent perspectives using a variety of sources, 
and having learning objectives and deliverables that consist of things that can be 
integrated and applied across diﬀerent subject areas, leading to what they call 
“beyond domain-speciﬁc outcomes”. 
Yet, at the very heart of interdisciplinarity is conﬂict. Anecdotally, there are 
stories of researchers and academics from diﬀerent disciplines losing their tempers 
trying to work with colleagues from others, but those types of personality-driven 
project-internal struggles are ones that anyone with experience of working in any 
team will recognise. What is speciﬁc to interdisciplinary teams, such as those in 
the Digital Humanities, is that projects have participants from at least two broad 
disciplines (e.g. Computer Science and the Humanities). Conﬂict can arise because 
the matrices for evaluating success are very diﬀerent in these two ﬁelds, and that, 
in turn, aﬀect what each member sees as a success, and what their aims and agen-
das are. And those can be mutually exclusive. A simple example of this might be 
something like the publication paradigm: computer scientists publish in a space 
and academic tradition that is more likely to produce co-authored papers that are 
published in proceedings of carefully ranked and indexed conferences. Their col-
leagues in the Humanities might labour alone over a single manuscript for years. 
In some ways then, comparing academic success between diﬀerent ﬁelds is like 
comparing apples and oranges. 
Understanding Digital Humanities is understanding the diﬀerences between 
STEM and HASS, and the eﬀect they have. STEM and HASS are categorised not 
only as two separate things, as falling to the opposite ends of the spectrum, as far 
apart as can be possible. Again anecdotally, interdisciplinarity has been described 
as sitting on two chairs simultaneously, but the ﬁeld is much more dynamic than 
that. If we must keep to the analogy of sitting down in some form, then Digital 
Humanities is closer to trying to ride two galloping horses, at all times hoping they 
do not choose to bolt in diﬀerent directions. But even that analogy fails: the horses 
are too clearly deﬁned, tangibly diﬀerent things. 
Could we then describe Digital Humanities as a ﬁeld that deﬁnes itself as sit-
ting at the intersection between two completely diﬀerent things? We could, and 
often do, at least in the vernacular of the discipline. But that dichotomy is a false 
one. And not just in Digital Humanities, but as a general axiom. Nowhere is still 
more evident than in the interdisciplinary spaces where these two clearly and un-
equivocally overlap. There are a number of diﬀerent domains, many of which 
have established themselves as disciplines in their own right, manifesting through 
topic-speciﬁc publication venues such as journals, conferences, academic centres 
and departments, professorial roles, and so forth. By no means an exhaustive list, 
these disciplines count among themselves the likes of Digital Humanities, Web 
Science, Cybernetics, Digital Scholarship, Humanities Computing, Computational 
Linguists, Digital Design, Digital Musicology and Music Information Retrieval, 
Distant Reading and Text Analysis, Library and Information Sciences, and so on, 
indeed there is an entire acronym combining them all – STEAM
3 – which has 
enjoyed sporadic and occasional popularity. Could we surmise that there are no 
ﬁelds left in all of HASS that are absolute in their refusal to engage with any digital 

 
 
 
  
 
 
 
 
 
   
 
  
 
 
 
     
   
 
 
   
   
 
A False Dichotomy  5 
technologies? Are there any (broadly deﬁned) computational methods that are yet 
to be applied to the study and analysis of HASS data? Not many, if any. 
Among researchers of the Humanities, there is sometimes a notion of a self-
proclaimed luddism. It is worn sometimes as a badge of honour, and always forms 
a part of the individual’s identity: “I’m not good with computers” they mutter, often 
whilst editing the audio and the visuals of a video they recorded on their mobile 
device to send to a satellite sitting in space so that it can immediately appear on 
the screen of some unknown user on the other side of the planet. Tagged, naturally, 
with internet slang and acronyms that illustrate the idiolect of someone belonging 
to the global community that calls the Information Highway that is the World Wide 
Web home. 
“Luddite” is a perhaps not entirely un-derogatory blanket term for people who 
do not like, enjoy, or feel particularly conﬁdent in the use of digital and computa-
tional tools and platforms. The term has its origins in a secret society (of types) of 
19th-century England, amongst (in particular) textile workers, who abhorred the 
introduction of the mechanised looms in the wake of the Industrial Revolution. 
The conﬂicts did become bloody, even fatal, and resulted in the penal transporta-
tion of some identiﬁed members, but over time the label of “luddite” has become 
diluted and generalised to apply to a rather more innocent type of dislike of com-
puters. Amongst some Humanities researchers, this label is an attractive one: it is 
a method of asserting identity, of being of something more pure and traditional, of 
perhaps adhering to the good old ways, the proper intellectual work. And with that 
comes an insistence (no matter how false) of a lack of skill or ability. But do our 
colleagues from Computer Science do anything as a regular user that colleagues in 
the Humanities do not do? How much of what we observe in diﬀerences of skill can 
be just as well interpreted as diﬀerent degrees of conﬁdence or a badge of identity? 
And why is this expectation of skill and knowledge one that ﬂows only from the 
Humanities to Computer Science? Or to put it another way, how often do Computer 
Scientists consider carrying out their research whilst engaging with Humanities 
methods such as historical criticism, or with the aim of situating their research into 
a robust framework of, say, socialist feminist theory? 
1.3 Snow’s Two Cultures 
There are undeniable diﬀerences in the ways these two broad disciplines of HASS 
and STEM approach research and scholarship, how (academic) achievement is 
measured, and thus what, in essence, success looks like. In this context, the Gates 
may not be a perfect analogy: yes, the doors form one cohesive whole, but the dif-
ferences between the two halves are largely superﬁcial. Underneath is all, the doors 
are structurally identical. But is this not true of STEM and HASS as well? How 
deep do these contrasting features need to reach in order to constitute a fundamen-
tal diﬀerence? 
What is illustrated here is that the diﬀerences we see between ﬁelds of STEM 
and those of HASS are, essentially, behavioural diﬀ erences within a shared aca-
demic landscape that nevertheless adheres to a set of universal rules, where the 

 
  
 
 
  
 
 
  
 
 
 
 
 
 
   
  
 
 
 
 
 
6 A False Dichotomy 
universe as it is understood is academia internationally. These diﬀerent approaches 
are caused and perpetuated by both internal and external factors and perceptions. 
Perhaps it is for this reason that navigating this particular research terrain can be 
such a hellish task. 
The idea is nothing new, nor unique: Snow published on the topic in the mid- to 
late twentieth century ( Snow, 1961 ) and so proliﬁc is the insistence of academics 
to come back to the idea that the Two Cultures has its own Wikipedia entry. 
4 The 
section of this essay that has most often and most consistently captured the atten-
tion and the imagination of audiences over the decades is a comparison of domain 
expertise and experience, epitomised by familiarity with either the Second Law of 
Thermodynamics or the works of Shakespeare: it’s classic STEM versus HASS. 
This juxtaposition of literature versus the hard sciences is a narrative that is very 
common in epitomising the challenges of interdisciplinary research, and is par -
ticularly relevant, as we saw earlier, in Digital Humanities. It is also one that runs 
throughout Snow’s thesis. 
But there are other segments too. This one articulates the chasm of interdisci-
plinary communication: 
Two groups-comparable intelligence, identical in race, not grossly diﬀerent 
in social origin, earning about the same incomes, who had almost ceased to 
communicate at all, who in intellectual, moral and psychological climate had 
do little in common that instead of going from Burlington House or South 
Kensington to Cheldea, one might have crossed an ocean. In fact . . . much 
further than across an ocean – because after a few thousand Atlantic miles, 
one found Greenwich Village talking precisely the same language as Chel-
sea, and both having about as much communication with M.I.T. as though 
the scientists spoke nothing but Tibetan. 
Setting the question of interdisciplinary communication aside for a moment, the 
quote deserves some unpacking and a comment or two in terms of being a product 
of its time. We might want to exclaim about the increased diversity of academia, 
for example, citing examples of proliﬁc and prestigious professors and leaders who 
represent minority groups. The truth is that improvement in this regard has been 
incredibly slow over the last half century. BBC describes the rate of progress as 
“glacial” and points out that in January 2021, only 1% of professors in the UK were 
black.
5 What was true in 1961 is true in 2021: especially in terms of more senior 
roles, academics (lecturers, professors) in both STEM and HASS are in the institu-
tions of the Global North and Western societies racially homogenous. This is true 
of Digital Humanities as well. 
Two other speciﬁed characteristics remain to be discussed: equal pay and social 
origin. Much has been written about ﬁrst-generation academics ( Ives and Castillo-
Montoya, 2020 provide a systematic review), but the status itself is not universally 
recognised or explicitly addressed. In a recent (2021) study of Australian higher 
education, Patﬁeld et al. interviewed almost 6,500 students enrolled in govern-
ment schools in the territory of New South Wales. Their ﬁndings illustrated that 

   
 
 
 
   
 
 
  
     
 
  
   
 
 
 
  
    
 
  
 
  
 
 7 A False Dichotomy 
the national education policy, which focused on six groups (including Indigenous 
groups, learners from low socio-economic backgrounds, students in regional or 
remote areas, those with disabilities, non-native English speakers, and women in 
non-traditional ﬁelds), was insuﬃcient for not explicitly addressing the challenges 
of ﬁrst-generation academics. While change may be afoot, much still needs to hap-
pen before we can conﬁdently dismiss Snow’s description of the socio-economic 
consistency of the background of most academics, be they of STEM, HASS, or any 
of the myriad disciplines in between. 
In terms of pay, the prevailing assumption is one of the supremacy of Science 
over the Humanities, but recent publications have illustrated that the truth is more 
complicated. A 2015 study by Emolument (a pay-data website), 
6 which recorded 
academic salaries from the UK and the USA, found that whilst in the early stages of 
their careers, STEM graduates earn up to 29% more than their HASS counterparts 
(in the USA; in the UK the equivalent ﬁgure was 6%), by the 15th year of their 
career, Humanities graduates were earning 7% more than their peers with a degree 
in the sciences. In this regard, there are no discipline-driven diﬀerences that would 
be maintained throughout an entire academic career – perhaps issues of promotion 
and salary are examples of transdisciplinary issues. 
What does remain clear is that research funding is allocated in very diﬀerent 
ways: in the UK, the Engineering and Physical Sciences Research Council (EP-
SRC) had an annual budget of £898 million in 2015–2016 
7 – the equivalent sum 
for the Arts and Humanities Research Council (AHRC) for the same year was only 
£98M.
8 But how does this aﬀect Digital Humanities? Could it be that the success of 
Digital Humanities in the UK (e.g. King’s College London, for example, is consid-
ered to be a globally leading institution) has been helped and aided by the division 
of funding councils along these disciplinary lines – perhaps this opens up greater 
numbers of opportunities? To take my interdisciplinary PhD as an example, I was 
able to apply to both the EPSRC and the AHRC – and was oﬀered grants by both. 
An interdisciplinary project in Digital Humanities was seen in the UK at least at the 
time as desirable, and more crucially fundable, by both parties. 
This is not a universal pattern. We can contrast it with the Australian setup: 
there is just one, monolithic Australian Research Council (ARC). Here too, there 
are diﬀerences between the ways funding is allocated between STEM and HASS – 
but this discrepancy in funding is accredited to a diﬀerence in the culture of ap-
plying for grants. In 2021, the ARC noted that the “success rates across the range 
of ﬁelds of research the ARC funds are reasonably consistent. While a far greater 
percentage of STEM applications are received, the success rate is fairly similar at 
approximately 21 per cent since 2012”. 
9 Between 2011 and 2015, some 47,000 
applications were submitted from the STEM ﬁelds, with fewer than 17,000 from 
the HASS disciplines. The categorisation of Digital Humanities projects is at the 
discretion of the scholar, since predetermined Field of Research (or FOR) codes 
are used to classify the proposal and ﬁnd reviewers. There is no speciﬁc FOR code 
for Digital Humanities in particular, although recent years have seen the develop-
ment of several speciﬁc ones (e.g. Digital History). The problem this presents is 
that, perhaps rather counter-intuitively, these divisions splinter an already diverse 

 
 
 
  
 
  
  
  
 
 
 
 
   
   
 
 
 
 
 
  
  
 
  
 
  
 
8 A False Dichotomy 
ﬁeld even further. It also means that comprehensively interdisciplinary research 
agendas become very challenging to establish: Digital History, for example, would 
be a subset of History, and thus reviewed by Historians according to the criteria 
and parameters of their discipline: what we want is a main dish of History, with a 
side serving of the Digital.
10 
In terms of absolute dollars awarded for research, there is a notable diﬀ  er-
ence in both the total sum of funding and the value of an average grant across 
the STEM/HASS divide. To illustrate the point, let’s refer agai n to the ARC. The 
Grants Dataset 
11 details the University Group (i.e. be they Group of Eight Uni -
versities,12 Innovative Research Universities, or Not Aligned Universities ), the 
Administering Organisation, the State/Territory, Project Code, Program, Scheme, 
and two FOR 13 codes for each successful grant, regardless of type, between 2002 
and 2021. The Dataset divides the grants into HASS, STEM, and Not Speciﬁed. 
Using the ARC’s internal categorisation, we can see that within that ten-year pe-
riod, there was a notable diﬀerence in the number of successful grants as well as 
the average funding amount awarded per successful grant between STEM and 
HASS. Between 2002 and 2021, the total number of HASS grants aw arded was 
7,703. These were awarded across 17 diﬀerent schemes.
14 The total sum of the 
grants was $2,667,319,642. The average value of an awarded gran t is $346,315. 
As there is no way of retrieving Digital Humanities projects (i n the absence of a 
speciﬁc FOR code), it’s not possible to reﬂect on the funding of the ﬁ eld as an 
entity. 
For STEM, the numbers are larger across the board. There have been 21,668 
successful grants over the period of 2002–2021. That’s roughly thrice as many as 
in HASS – this reﬂects the earlier claim that the rates of success have been largely 
consistent: there were almost three times as many applications from STEM disci-
plines than from HASS, so it stands to reason that with the similar rate of success, 
thrice as many grants would be successful as well. This greater number of appli-
cations also shows in the vastly larger overall sum of dollars awarded to STEM 
research by the ARC over this ten-year period: the total sum was $10,616,548,122. 
Here, the pattern of thrice no longer holds: the total sum of money awarded for 
the sciences is ﬁve times as high as that received by the Humanities and Arts. This 
reﬂects on the average size of a successful grant: for the STEM disciplines, the 
value is some $140,000 higher, averaging at $489,942 per grant. The funding was 
awarded across 19 distinct schemes (two more than for HASS). 
15 There is thus a 
twofold diﬀerence in the way STEM and HASS researchers apply for funding: 
STEM researchers apply more frequently and in greater numbers, and, second, 
they ask, on average, for larger grants. The former is undoubtedly the result of a 
history of funding: STEM has received more funding so has been in a position to 
employ more researchers who then in turn are expected to apply for funding that 
creates more positions for new STEM researchers to ﬁll. In this aspect, are the 
HASS disciplines missing out on a trick? It boils down to there being two diﬀerent 
types of academic culture. 
Many would generalise the work of a Humanities scholar as that which is 
typically carried out in isolation, whilst STEM roles are often built into labs and 

  
    
  
 
 
  
 
 
  
    
 
  
 
 
 
 
 
  
 
 
  
 
 
 
 
 
 9 A False Dichotomy 
research clusters. Is the number of Humanities scholars low because the culture of 
grants is one of supporting individual endeavour rather than establishing research 
clusters around a lead investigator? In other words, are there at least seemingly 
fundamental diﬀerences between the broad categories of research manifestation of 
diﬀerent  cultures of applying? Perhaps diﬀerent cultures of research, and a largely 
diﬀerent set of expectations? How then do we successfully map and measure 
achievements in a research landscape when such diﬀerences permeate the process 
from the outset? And perhaps most importantly, which of the two cultures is the 
one for Digital Humanities? 
To return to Snow’s quote, we can see that since the 1960s, the academic 
landscape has both changed and remained the same. The academic population 
is still largely homogenous in terms of race and socio-economic background – 
disciplinary diﬀerences do exist in terms of income and funding but these hark 
back to cultural diﬀerences not between individuals but between the behemoth 
disciplinary classiﬁcations of STEM and HASS. In their 2015 publication, Bod 
and Kursell note that whilst strides have been made in both camps to recognise 
similarities in infrastructures and methodologies, many of the “historiographies 
of the sciences and the Humanities seem to persist as two separate ﬁelds” (p. 337). 
In our collective quest to understand where we are at – so as to know which way 
the future lies – we look back on the history of our disciplines, but do so in ways 
that perpetuate the divide between Us and Them, deﬁning the history of STEM and 
HASS by way of excluding the other. These cultural diﬀerences of paradigms of 
publication, research agendas, funding models, and exclusive histories currently 
perpetuate the chasm between these two areas, and complicated communication 
between them. But for what purpose and to whose beneﬁt? Arguably, neither side 
has more to gain from this dichotomy than they do from the aggregation of skills 
and knowledge from both sides. And why should research be split into either HASS 
or STEM in the ﬁrst place? What purpose does it serve and what tangible beneﬁts 
are to be reaped from it? 
All this serves to remind us that in relation to Digital Humanities there is no 
chasm between STEM and HASS. Digital Humanities research can – and has 
been – funded by diﬀ erent research councils depending on the individual project 
and not according to a pre-existing disciplinary pigeon hole. The Digital Humani-
ties Department at King’s College London provides an excellent example of this. 
16 
and clearly underscores the interdisciplinary nature of the ﬁeld. 
The Department at King’s received almost £5,145,000 from the EPSRC to fund 
eight projects over a period of 16 years starting in 2008 and almost £13,660,000 
from the AHRC to fund 64 projects 2000–2022. Drilling down into the data from 
2012–2023 further highlights several important issues in relation to scale. Look-
ing at those awarded between 2012 and 2022, we can see that the  AHRC funded 
31, while the EPSRC awarded just 6. Having said that, the EPSRC awarded larger 
sums in terms of both the total allocation and the average amount per grant than the 
AHRC. The total value of grants from the AHRC was just over £6,800,000 (with 
an average grant size of £220,000); whereas from the EPSRC, the total was over 
£4,600,000 (with an average grant of £777,000). Moreover, there was a marked 

 
 
 
 
 
  
 
 
    
 
 
  
 
 
     
   
10 A False Dichotomy 
diﬀerence in relation to the numbers of recipients in the grants themselves. Almost 
half (45%) of those awarded by the AHRC went to single applicants, with another 
32% going to investigatory teams of just two. In sharp contrast, half of the success-
ful applications to the EPSRC were awarded to teams of six or more applicants. 
Even more signiﬁcantly, all of the highest-grossing grants from both the AHRC 
and the EPSRC were awarded to teams of multiple investigators. In fact, all grants 
with a value of more than £1,000,000 awarded by both research councils were 
awarded to teams (and supports the argument regarding co-authorship discussed 
in Section 1.2). 
1.4 The Role of Humanities in Computer Science 
The public face of the Digital Humanities has often been dominated by litera-
ture and text analysis. So much so, that an axiom persists in the discipline that 
the ﬁrst-ever Digital Humanities project was the Index Thomisticus, a collabora-
tion between IBM and an Italian Jesuit priest Father Roberto Busa, in the 1940s 
and 1950s. It was a project of computational linguistics, indexes, and computer-
generated concordance. But it is possible to argue that this origin story is ﬂawed, 
because we can show that HASS has been a part of the development of computers, 
digital platforms, and hypertext systems since the beginning. There have always 
been interdisciplinary thinkers, much before we coined convenient descriptive la-
bels to categorise them. 
One example comes to us from Iraq a millennia before the invention of digi-
tal electronic computers. As I described in the 2023 piece for the Conversation,
17 
when Europe was in the midst of the so-called Dark Ages, interdisciplinary think-
ers collaborated in what is known as the “House of Wisdom” (Bayt-al Hikmah) 
in Baghdad ( Al-Khalili, 2010 ). It was a centre of translation, learning, poetry, en-
gineering, theology, and myriad other subjects: it was a centre for what we could 
now categorise as pioneering inventions in science, technology, and engineering, 
all carried out by poets, musicians, philosophers, linguists, and librarians. For ex-
ample, in 850 AD, the Banu Musa brothers wrote and published a work known as 
the “Book of Ingenious Devices”, which describes automata and other precursors 
to modern robots, and what has even been argued to be the world ’s ﬁrst program-
mable machine ( Koetsier, 2001 ). Another scholar of the House of Wisdom at the 
time was Mohammad ibn Musa al-Khwarizmi, whose name inspired the terms “al-
gebra” and “algorithm”. Al-Khwarizmi worked closely with al-Kindi, an Abbasid 
polymath who was both a student of cryptanalysis and a pioneer in music theory. 
The House of Wisdom was a centre of interdisciplinary thinkers establishing the 
foundations of the types of mathematics and engineering that have been instrumen-
tal in the development of Computer Science. 
Music gives us another perfect example, for it has been part of the history of me-
chanical computers since the very beginning. The earliest of examples comes from 
the worlds of Ada Lovelace, widely considered the ﬁrst computer programmer in 
recognition of her Notes
18 for Charles Babbage’s Analytical Engine, published in 
1843. The Notes were written as an addition to the work of translating the article 

  
 
 
 
 
 
   
 
 
 
 
  
 
   
 
 
  
 
 
  
 
 
 
 
   
 
A False Dichotomy 1 1 
written by Luigi Menabrea: Lovelace’s comments ended up being triple the length 
of Menabrea’s article, and are now described by the Mathematical Association of 
America as “a classic in the early literature on computers”.
19 
There are those who seek to critique, down-play, or dispute Lovelace’s contri-
bution to Computer Science (e.g. see Misa (2016 ) for a summary of work in this 
vein). But if nothing else, Ada’s family background makes for a fascinating case 
study example for the Nature versus Nurture debate. Ada was the only legitimate 
daughter of the infamous poet Lord Byron, and her mother (who was also a math-
ematician), in an attempt to protect her from her father’s detrimental inﬂuence, 
encouraged her to discard the arts and pursue mathematics and logic exclusively 
instead. This did not prevent Ada from being subject of gossip regarding extramari-
tal aﬀairs, or end up being what turned out to be a very poor 
20 gambler indeed. But 
more signiﬁcantly, she was undoubtedly an interdisciplinary thinker. 
The signs of what we would today consider to be interdisciplinary thinking are 
clear in her Notes (as published in Misa, 2016 ): 
Supposing, for instance, that the fundamental relations of pitched sounds in 
the science of harmony and of musical composition were susceptible of such 
expression and adaptations, the engine might compose elaborate and scien-
tiﬁc  pieces of music of any degree of complexity or extent 
(Note A, p. 694)  
and less speciﬁcally “the Analytical Engine weaves algebraic patterns just as 
the Jacquard-loom weaves ﬂowers and leaves” (Note A, p. 696; Lovelace refers to 
the “art of weaving” in Notes C). Thus, in her processes of making meaning of the 
potential of computation, of understanding algorithmic concepts and their applica-
tions, and in communicating her ideas about the potential of the Engine to others, 
Lovelace referred to notions of music, and art. If not this, then what could be the 
earliest-known example of what we now refer to not just as interdisciplinary but 
also as speciﬁcally  Digital Humanities thinking? 
Lovelace was not the only one to see the potential between these new machines 
and music, and the latter is a feature of the history of digital computers. The Com-
monwealth Scientiﬁc and Industrial Research Automatic Computer (CSIRAC) was 
among the pioneers of stored-programme computers, and Australia ’s ﬁrst digital 
one – and almost certainly the ﬁrst anywhere to play music ( Doornbusch, 2004 ). 
Whilst myriad reasons, research agendas, and so on are likely to have contributed 
to the development of CSIRAC, simply the thought of testing whether a machine 
such as this could play music illustrates the ubiquity of Humanities subjects across 
the diversity of the STEM disciplines as well. The crucial diﬀerence here is that it 
is a Humanities subject matter, and not a methodology, which plays a role. 
Beyond these origins of mechanical, electronic, and digital computers as hard-
ware, Humanities data (the subjects of research and investigation in the Humanities, 
such as literature, music, and art) has also played a major role in the development 
of hypertext systems: Prof Dame Wendy Hall has accredited her work in the 1980s 
with the archive of Earl Mountbatten as eventually leading to the development of 

 
   
 
 
 
  
  
 
 
  
   
  
  
 
  
 
     
   
 
  
     
      
 
      
 
 
      
     
 
12 A False Dichotomy 
Microcosm21 (an early contemporary to the Web), and Dallas (1992 ) outlined his 
suggestions for semantic components and logic programming (with a case study of 
ﬁgurative art on Classical Attic funerary markers) nearly a decade before  Berners-
Lee’s et al. (2001 ) article launched the concept of semantic technologies to the 
masses. 
1.5 Linked Data and the Humanities – a Perfect Pair? 
Having these ideas of the interdisciplinary of the Digital Humanities in our 
minds, it is time to address the second major part of the title for the book: 
Linked Data. 
In early 2021, Miriam Posner described Linked Data as “not really one key 
piece technology, but a set of best practices for publishing data on the Web”. 22 She 
is right that there is no one key piece of software that is used to create Linked Data, 
but there are many diﬀerent methods, workﬂows, tools, and so forth. And yes, it 
is a process for data publication. But it is more than that. It is a speciﬁc methodol-
ogy, and a standardised one at that. Linked Data is a way of doing things, namely, 
the publication of information online in accordance with internationally speciﬁed 
standards using existing Web technologies and architecture. It is an information 
publication paradigm. 
And it’s not a matter of best practice, per se. The quality of the Linked Data is 
measured by its adherence to the Five Star Standard. This standard, which has been 
deﬁned by Tim Berners-Lee, was published by the World Wide Web Consortium 
(W3C) in 2013. 
23 It is depicted and expanded on in Table 1.1 . 24 Note that there is 
no set software, no particular details as to how each stage of Linked Data quality 
is to be reached. 
  Table 1.1 Five Star Standard of Linked Open Data 
Quality Description Example 
☆ Data is available on the 
Web, in any format. 
☆☆ Data is available as 
machine-readable, 
structured data, but in a 
proprietary format. 
☆☆☆ Data is available as 
machine-readable, 
structured, and non-
proprietary format. 
☆☆☆☆ Data is published using 
W3C open standards. 
☆☆☆☆☆ Data is connected to other 
Linked Data online. 
PDF of a dataset (not machine actionable, 
but viewable by human users). 
A tabular dataset is made available as an 
MS Excel spreadsheet, which requires 
anyone wishing to access the data to have 
that speciﬁc software installed. 
A tabular dataset is made available as 
a CSV ﬁle, which can be used with 
many diﬀerent software and many 
programming languages can be used to 
read it. 
Data has been converted to RDF and it can 
be queried using SPARQL. 
Data published as RDF has external links to 
other Linked Data resources or authority 
ﬁles such as VIAF.org or Wikipedia. 

 
 
 
    
 
   
 
    
      
       
   
     
   
    
 
 
   
     
 
      
   
     
  
 
 
A False Dichotomy 1 3 
Put together, we can see the (at least seemingly) ideal pairing of the Linked 
Data methodology with Humanities datasets is based on a simple premise: humans 
are network thinkers, and Linked Data is a network technology (Nurmikko-Fuller, 
2018 ). The parallels between the two run wide and deep. Even the terminologies 
we used to describe the concepts of Linked Data echo earlier Humanities thought 
and analysis. 
1.5.1 The First Wittgenstein and the RDF Triple 
In his opening statement to Tractatus Logico-Philosophicus, Wittgenstein (1922 ) 
quotes Kürnberger to say that “whatever a man knows . . . can be said in three 
words”. Similarly, one of the cornerstones of the Linked Data approach is that all 
knowledge can be captured in statements of three components. We call this the 
RDF (or Resource Description Framework) triple. 
RDF is a W3C speciﬁcation. It is not a speciﬁc piece of software that enables 
one to implement a Linked Data project, but rather an abstract data model that 
enables us to publish data in a machine-navigable format. There are two key con-
siderations for understanding RDF from a technological perspective. First, RDF 
is mostly expressed in triples, which, as the nomenclature would suggest, consists 
of three parts. These parts are called the Subject, the predicate, and the 
Object. At least the Subject and the predicatemust always be a URI, the 
Objectcan be a URI, a string (of letters), or an integer (numbers). If the Object
of one triple is a URI, it can be the Subject another triple, thus resulting in an 
interconnected graph, which when visualised often looks like a network diagram 
of arcs and nodes: we consider the Subjectand Object to be data entities, and 
the predicate between as a relationship, that connects the two and gives them 
meaning. 
The Subject-predicate-Objectlayout lends itself very well to the sen-
tence structure of a subject-verb-object (SVO) language, such as English. By way 
of a simple example, we could state a fact: William Shakespeare wrote “Romeo & 
Juliet”. The Wittgensteinian pattern of three in adherence to the SVO layout is clear: 
the subject (William Shakespeare) wrote (verb) “Romeo & Juliet” (the object). And 
this pattern would lend itself to representation as an RDF triple: Subject (Wil-
liam Shakespeare) predicate (wrote) Object(“Romeo & Juliet”). In this very 
literal and somewhat oversimpliﬁed sense, facts can be expressed in RDF in the 
equivalence of three words. The RDF triple is often visualised as a minute net-
work diagram. The Subject and Object are the nodes (often depicted as dots 
or circles); the predicateis an arrow (a directed, labelled line) running from the 
Subjectto the Object. Examples of these visualisations are readily available.
25 
The step that many beginners ﬁnd the biggest leap is that rather than these 
human-friendly diagrams of circles and lines, RDF is expressed explicitly through 
Hypertext Transfer Protocol (HTTP) URIs. This might seem suddenly very heavy 
in acronyms, but we’re all very familiar with them as the location of pages on the 
Web. Some browsers now hide the preﬁx, but all pages on the Web have a distinc-
tive identiﬁer that can be seen in the address bar of the browser. And they all start 

 
 
 
 
 
  
 
  
  
  
 
 
  
 
 
 
 
 
 
 
 
 
 
  
 
  
  
14 A False Dichotomy 
with HTTP://. Where Linked Data diﬀers from this current Web of pages and sites 
is that these HTTP URIs point to data instances, and the relationships between 
those data instances. 
The Web of Documents is a hypermedia system based on hyperlinks that con-
nect disparate resources online. Each resource sits at a speciﬁc location, captured 
as a unique identiﬁer. Unique in the context of the entirety of the whole Web. No 
two pages can have the same address, or the process of retrieving that content and 
displaying it to the user in the browser would fail. The technical speciﬁcations of 
these diﬀerent types of identiﬁers have been published many times before ( Wood 
et al., 2014 , is a good example), which is why they will not be the focus here. 
There are essentially three types of universal identiﬁers on the Web: the URI 
(uniform resource identiﬁer), URL (uniform resource locator), and URN (which 
refers to numbers). URLs and URNs are often considered to be equal but diﬀ  er-
ent subsets of URIs, but in the case of the Linked Data paradigm in particular, the 
URI is rather more uniquely speciﬁc. They are used to point not to existing digital 
resources, but information entities and the relationships between those entities. On 
the current Web, URLs are addresses where websites sit. We click on a link, and are 
expected to be taken to a page, an image, an audio ﬁle, or a video. URIs in Linked 
Data projects on the other hand, if clicked, are likely to return a 404 error code: 
there is often no digital resource (no “thing”) that it points to. This is not a failure 
of the system or an example of the tech axiom or adage of “a feature not a bug”. 
Rather, this is an example of the ways in which URIs are used to represent both the 
underlying database structure and the data that populates it. 
In the Linked Data context, we can conﬁdently say that Wittgenstein had it right 
a century ago, but we need to update the quote to say “whatever a man knows . . . 
can be said in three URIs”. 
1.5.2 The Second Wittgenstein and Explicit Statement of Facts 
Wittgenstein’s proposition 1.1 is that “The World is the totality of facts, not of 
things” ( 1922 : 5). This concept is fundamental to Linked Data projects: RDF tri-
ples are created to specify absolute and unambiguous relationships between unam-
biguous entities. So absolute is the adherence to unequivocal facts that there is a 
speciﬁc assertion regarding it, or its absence: The Open World Assum ption takes 
that a statement can be true even if it is not explicitly known to be true. Linked 
Data methods and Semantic Web tools such as the OWL have this assumption built 
into them. The practical outcome of this is that it is possible to represent statements 
which are inexplicit, or have yet to be explicitly proven, and, as long as the graph 
adheres to its own internally consistent logic, it is technologically possible to make 
statements that we do not believe in, or which we cannot prove. 
Furthermore, since Linked Data is a method of representing digital content, 
all “things” are intangible. Let’s imagine a simple set of information represented 
as three URIs. One of them refers to William Shakespeare (author and histori-
cal ﬁgure), another to a play (“Romeo and Juliet”, for example), and a third to a 
relationship that deﬁnes Shakespeare as the author of the play. In the case of the 

 
    
 
    
  
  
  
  
  
 
  
 
  
 
 
  
  
  
 
 
 
 
 
  
 
 
 
  
 
  
 
 
 
 
A False Dichotomy 1 5 
example of William Shakespeare, the URI (in this case, let’s use http://viaf.org/ 
viaf/96994048/) does not point to a tangible, real-life person: it is not an identi-
ﬁer for a thing. The URI points to a digital resource that has information about 
that thing, in this case, William Shakespeare. It is from the Virtual International 
Authority File (VIAF) and is used to represent the idea of Shakespeare. But why? 
Because VIAF is an example of an authority ﬁle. The URI does not point to a 
webpage about Shakespeare, nor a picture of him, nor any of his works. The URI 
has a page that is rendered in the browser, but what it refers to is an internation-
ally agreed-upon identiﬁer for the historical person. 
The point becomes quite philosophical here. Essentially, Shakespeare is a notion 
in the universe, which has timelessness to it. He manifested at one time as a (tangible) 
person, but his physical existence does equate to the totality of his existence. It is to 
this physical manifestation of a person that we can attach some concrete assertions, 
such as his name, or place of birth. But the relationship between Shakespeare the au-
thor and his work is a persistent truth: he will always be the entity that wrote the play. 
Creation dates can provide an example that helps diﬀerentiate between a tan-
gible manifestation of a person and their abstracted counterpart. If the URI was to 
point to a webpage, it’s creation date would be in, say, 2022. When a URI points to 
a notion of a person, we can assert this creation date (birth) as having been in 1564. 
In some systems, explicitly deﬁned rules may determine which kinds of assertions 
are possible about diﬀerent entities. 
But what determines which kinds of assertions are possible? In the Linked 
Data world, this is usually accomplished through ontologies. Although the term 
is borrowed from philosophy, in the realm of Linked Data, ontologies are a spe-
ciﬁc thing. Perhaps the most famous of deﬁnitions for ontologies is the one from 
Gruber (1993 ): “An ontology is an explicit speciﬁcation of a conceptualization”. 
Ontologies are discussed in more detail in Chapter 4 , so for now, we must content 
ourselves with a simpler explanation. Conceptually, an ontology is a description of 
a topic, a domain, a universe. They consist of listings of the diﬀerent entities that 
exist in that space (such as people, or places, or concepts, or events, or types of 
pizza), and the relationships that can exist between those entities. If you think that 
sounds a lot like the RDF triple described earlier, you would be absolutely right. 
What this simple premise equates to is that any ontology we design ends up rep-
resenting not just the data but also our knowledge about that subject. It reﬂects all the 
information about that topic that has been made available to us, and thus too then, 
either directly or indirectly, ontologies capture our biases, because they are informed 
by our reality, or more precisely, our understanding of our reality. But, their primary 
aim is to capture the facts: that is to say, to explicitly state the existence of the fun-
damental components of knowledge that exist in the represented topic or domain. 
More tangibly, an ontology is a ﬁle read by a piece of software. It is not com-
plicated technologically: they can be written in simple text-editing software such 
as NotePad or TextEdit that do not add formatting, hidden code, or hypertext to 
the ﬁle – for this reason, more complex word-processors such as Microsoft Word 
are not suitable for the task. These ﬁles map the domain: to write an ontology is to 
build semantic models with RDF, which are more speciﬁc models than the RDF 

 
 
 
 
 
   
   
   
 
     
  
   
 
 
 
 
16 A False Dichotomy 
triple or the abstract model itself. We do this to facilitate information exchange and 
to let others (humans and software agents alike) know what our data is about. It is 
a way of scaling complexity but also a method for adding meaning to your data so 
that it becomes discoverable and usable by others. 
Several other of Wittgenstein’s propositions echo with relevance and familiarity 
with the abstract data model of RDF and the First and Second Order Logics that we 
used to validate ontological structures. This is not to say that Linked Data proves 
that Wittgenstein achieved his aim of “[solving] the problems of philosophy” 
( Grayling, 1988 : 12), but what we can see clearly is that the approaches of Western 
philosophers and data scientists alike are inﬂuenced by the same perspectives for 
categorising, understanding, representing, and analysing the reality we encounter. 
It’s almost as if there were not, at the conceptual and cognitive level, such big dif-
ferences between philosophers of HASS and the data scientists of STEM. 
1.5.3 Foucault, Semantic Web, and Properties 
The World Wide Web was ﬁrst launched in 1989. The ﬁrst time the public was 
made aware of the idea of the Semantic Web was in 2001. How then could the 
French philosopher Michel Foucault (1926–1984) know to talk about the “seman-
tic web” and “properties” two decades earlier ( Foucault, 1970 : 17–18)? 
Properties (or perhaps more accurately properties) we have seen already, 
but what of the Semantic Web? Wilks and Brewster (2009 : 1) described it as a 
“more powerful, more functional, and more capable version of [the] document 
and language-centric Web”. Since then, it has become increasingly synonymous 
with the “Web of Data”. 
26 What the Web and the Semantic Web have in common is 
that both are, simply put, hypermedia systems (or, perhaps, since the interlinking 
occurs at the level of speciﬁc data instances, it would be better described as a hy-
perData system) concerned with the publishing of information publicly in a shared 
technological format that enables software agents to infer meaning. If Linked Data 
is the process, then the Semantic Web is the noun. 
In fact, Foucault’s terminology is discussing an even older information-
structuring process, dating to the sixteenth century. This use of terminology il-
lustrates the conceptual similarities of the way human beings make sense of the 
universe: both the words “semantic” and “web” are signiﬁcant, and capture the idea 
of meaning-making through connections between things. Foucault goes on further 
to describe the understanding of ideas using terms which are remarkably reminis-
cent of the way we describe RDF triples: 
Thus, by this linking . . . that brings like things together and makes adjacent 
things similar, the world is linked together like a chain. At each point of 
contact, there begins and ends a link that resembles the one before it and the 
one after it; and from circle to circle, these similitudes continue, holding the 
extremes apart . . . yet bringing them together.  
( Foucault, 1970 : 19) 

 
      
    
   
 
 
 
 
 
 
 
  
 
  
 
  
 
 
 
A False Dichotomy 1 7 
The phrasing conjures up an image of interconnected triples, where each looks 
the same (consisting as they all do, of a Subject, a predicate, and an Ob-
ject, each where possible consisting of URIs), and where the Object of one 
triple constitutes the Subject of another, creating an interconnected knowledge 
graph. The properties that connect the two capture the connections between things, 
just as described in the quote above. And who could argue with the parallel of cir-
cles and lines when comparing and contrasting them to the ways in which ontologi-
cal structures and instance-level data are represented in Linked Data papers using 
diagrams of circles and lines? 
The borrowing of the term “ontology” by computer scientists from philosophers 
is perhaps the worst-kept secret of the Linked Data community, and one that can 
cause confusion in the intersection of Humanities and Computer Science that is the 
Digital Humanities. As noted by  Foucault (1970 : 120): 
For two centuries, Western discourse was the locus of ontology. When it 
named the being of all representation in general, it was philosophy: theory 
of knowledge and analysis of ideas. When it ascribed to each thing resented 
the name that was ﬁtted to it, and laid out the grid of well-made language 
across the whole ﬁeld of representation, then it was science – nomenclature 
and taxonomy. 
Foucault’s description of human cognition parallels that of Vannevar Bush (an 
American engineer). As we noted in Nurmikko-Fuller and Pickering (2021 ), this 
is clear in the context of Bush’s description of the motivation for the Memex some 
15 years earlier ( 1945 : 14): 
The human mind does not work [in a direct] way. It operates by association. 
With one item in its grasp, it snaps instantly to the next that is suggested by 
the association of thoughts, in accordance with some intricate web of trails. 
And even more recently still, Simpson (2020 ) summarises explicitly on the par-
allels between hypertext systems and cognitive processes – the same description 
can easily be applied to the parallels between graph databases and mindmaps. 
1.5.4. Meaning Derived From Connections 
In both the ﬁelds of Philosophy and of Computer Science, an agreement exists as to 
the way meaning is conjured through connections. It should not be surprising then, 
based even on these two examples alone, that the Semantic Web would manifest in 
such a way as well. As noted by Simpson (2020 , July): “graph-based hypertext . . . 
provided a better way of representing the interconnected way in which I thought 
and worked”. It seems the natural ﬁt of technology and thought to utilise the com-
putational process of Linked Data to represent, capture, and query information we 
as humans have collected about the human world. 

 
 
 
  
 
  
 
  
 
 
   
 
    
 
 
  
 
 
  
 
 
 
 
 
 
 
18 A False Dichotomy 
Furthermore, all data contains a degree of ambiguity, a fuzziness at the edges. To 
this point, Linked Data methodologists have sought ways to eliminate this vague-
ness; to clean it up and remove it. The absolute unambiguity of URIs has been 
cited as the ultimate method for identifying and uniquely labelling everything. In-
stead of eliminating this ambiguity, it should be actively embraced; innovative, 
disciplinary-neutral methodologies should be developed to purposely capture and 
leverage ambiguity and methods for incorporating it into automated processes of 
machine inference should be more deliberately explored. 
Perhaps unsurprisingly, scholars have done little to address ambiguity and 
vagueness using Linked Data. An examination of existing ontologies through 
aggregator projects such as the Linked Open V ocabularies highlights a very lim-
ited number of existing examples of knowledge representation systems that ad-
dress uncertainty. Silvio Peroni’s 2013 work on vagueness would be one such 
example, 
but the lack of uptake and widespread use of his ontology is perhaps 
reﬂected in the fact that it is no longer available online (the URI returns an 
all-too-familiar 404 error code). Peroni’s other ontological wo
rk (with Shot-
ton, 2018) does not 
explicitly cover methods for capturing the uncertainty or 
the incompleteness of data. In other cases where ambiguity and vagueness are 
represented in ontological structures (such as the OntoMedia ontology, 
27 which 
allows a thing to be categorised as an “Unknown”), they are unambiguously 
captured as information entities (i.e. Class in the ontology). In this way, they 
essentially represent vagueness and uncertainty to the human user, not at the 
computational level. 
The great unfulﬁlled promise of Linked Data is machine inference, the auto-
mated deduction of implicit connections and relationships between explicitly 
declared facts. It has immense potential for coping with messy data: capturing 
ambiguity rather than eliminating it. The core of the challenge is thus not simply 
how to apply powerful Semantic Web ( Berners-Lee et al., 2001 ) technologies to 
Humanities investigations, but how to develop these technologies to confront the 
problem of semantic ambiguity within Linked Data. 
Some two decades ago, Linked Data was identiﬁed as a practical method for 
realising a next stage in the development of the Web: an evolution from a Web of 
Documents ( Képéklian et al., 2015 ) to a Web of Data ( Berners-Lee, 1999 ). To infer 
new knowledge from this proliferation of datasets, we must ﬁnd ways that enable 
us to capture the importance of and the eﬀect of various degrees and types of uncer-
tainty inherent in them. Although this data is utilised by both people and automated 
processes alike, until now, there is little evidence of systematic attempts to identify 
a comprehensive solution, either in the academy or in the industry. 
1.6 Conclusion 
The chapter began with the setting of a scene for understanding the interdiscipli-
nary world of the Digital Humanities by way of a visual metaphor of Rodin’s Gates 
of Hell. Myriad sculptures together constitute one larger, cohesive piece. Projects 
in the Digital Humanities vary in ambition, scope, focus, agenda, funding sources, 

 
 
   
 
 
 
  
 
 
 
 
 
 
  
  
  
 
   
  
 
 
 
 
 
  
 
 
  
  
  
     
 
 
  
  
 
 
 
 
A False Dichotomy 1 9 
team size, methodology, data, and desired research outcome. All our projects are 
diﬀerent, but there is a clear sense of belonging to a larger whole – a shared con-
text. And yet, the division of the Gates into two doors underlying the sculptures can 
be seen as representing the binary ﬁelds of STEM and HASS. They are parallel, 
but not identical. Analysing the diﬀerences between the two disciplines highlights 
two things: that there are many diﬀerences and that the dichotomy between the two 
is false! 
Snow’s Two Cultures theory gives us a way to grapple with that paradox. There 
are many overarching similarities in STEM and HASS at the level of the greater 
academy: the homogeneity of high-ranking members of universities, for example. 
But at the ground roots level, we see evidence of very diﬀerent cultural approaches 
and behavioural models. These aﬀect how funding is applied for, how research is 
carried out, and how results are disseminated. There are clear diﬀerences in how 
success is measured. 
And yet, this seems like a relatively modern diversion. The origins of com-
putation include clearly interdisciplinary thinkers: Ada Lovelace, the world’s 
ﬁrst computer programmer, is a perfect example of someone who recognised 
the potential of computational machines to make music. Music, arts, and his-
torical documents have inﬂuenced not only the birth of Digital Humanities as 
a ﬁeld but also the development of computers and hypertext systems, such as 
Microcosm. 
The Digital Humanities is inherently diverse and home to many diﬀerent 
digital tools and computational methodologies. The ﬂexibility of the Linked 
Data approach in particular makes it an excellent pairing with the cognitive 
processes of Humanities scholars and researchers. The network-like representa-
tion of ideas, associations, and connections sometimes expressed by mindmaps 
are an ideal match for the knowledge graphs of interconnected RDF triples that 
sit at the heart of the Linked Data approach. It’s this shared goal and process of 
making meaning through connections that make the Linked Data method such 
an ideal ﬁt for the (Digital) Humanities. And this, in turn, proves that the di-
chotomy between STEM and HASS is false: both are needed in equal measures, 
to reach this shared goal. 
As the lens through which Linked Data is examined in this book, Digital 
Humanities deserves to be deﬁned and discussed. But has interdisciplinarity 
itself become the methodology du jour? Perhaps so, but it seems this (rela-
tively) new way of doing things is one that’s here to stay (the Gates are a 
timeless classic, after all!). Regardless of the disciplinary context, we all live 
in an era of increasingly sophisticated algorithms mapping, mea suring, and af-
fecting our lives through data-driven analytics. The Data Economy (see Chap-
ter 2 ) impacts the daily lives of an ever-increasing number of citizens. Linked 
Data oﬀers us ways to capture complexity in data, and even scale it gracefully. 
But to do so well in an inherently interdisciplinary way, and with thoughtful, 
critical engagement, we must combine this computationally powerful tool with 
considerations of human-centred issues of privacy, trust, agency, authority, and 
ethical engagement. 

 
 
     
    
  
  
  
     
 
    
    
     
    
    
     
     
    
 
  
    
     
 
 
      
 
   
  
 
     
 
 
 
 
 
    
     
20 A False Dichotomy 
Notes 
1 Although he may not have been the originator of the Digital Humanities-speciﬁc take 
on “That’s on me, I set the bar too low” meme (to say data provenance with memes is 
diﬃcult would be an understatement), one of the ﬁrst to tweet it was Ryan Cordell 
(@ryancordell) on 01/06/2021. Ryan’s take was: 
Jake : “I’m an expert in Digital Humanities” 
Jess : “Oh yeah? Name the top 10 most important Digital Humanities articles” 
Jake : “What is Digital Humanities?” 
Jess : “That’ s on me, I set the bar too low” 
2 www.mtsu.edu/first-amendment/article/1359/potter-stewart#:~:text=Potter%20 
Stewart%20(1915%E2%80%931985),pithy%20prose%20resulted%20in%20a. Accessed 
31/01/2023. 
3 STEAM refers to Science, Technology, Engineering, Arts, and Mathematics. 
4 https://en.wikipedia.org/wiki/The_Two_Cultures. Accessed 03/08/2021. 
5 www.bbc.com/news/education-55723120. Accessed 03/08/2021. 
6 www.emolument.com/career_advice/sciences_vs_humanities_students_salaries_who_ 
earns_more#gsc.tab=0. Accessed 24/08/2021. 
7 https://epsrc.ukri.org/about/facts/budget/. Accessed 24/08/2021. 
8 https://ahrc.ukri.org/documents/strategy/arts-humanities-research-council-delivery-
plan-2015-2016/. Accessed 24/08/2021. 
9 www.arc.gov.au/grants-and-funding/apply-funding/grants-dataset/trend-visualisation/ 
ncgp-trends-success-rates. Accessed 24/08/2021. 
10 Linked Data projects are perhaps most suitably categorised as 080707 Organisation of 
Information and Knowledge Resources: It is a nested subset of ﬁrst Library and Infor -
mation Sciences, and ultimately Information and Computing Sciences. Although I have 
no objection to this, I note that the classiﬁcation is not  neutral. 
11 www.arc.gov.au/grants-and-funding/apply-funding/grants-dataset. Accessed 21/03/2022. 
12 Group of Eight (or Go8) universities refers to a cluster of research-intensive universities 
in Australia. These are the University of Melbourne, the Australian National University, 
the University of Sydney, the University of Queensland, the University of Western Aus-
tralia, the University of Adelaide, Monash University and UNSW (University of New 
South Wales) Sydney. Like the Ivy League of the United States or the Russell Group 
Universities of the UK, this group consists of universities which rank highly both in 
Australia and internationally. For more information about the Go8, see https://go8.edu. 
au/about/the-go8 . Accessed 21/03/2022. 
13 FOR (or Fields of Research) Codes are a mode of classiﬁcation utilised to measure 
and analyse research in Australia and New Zealand. For more information about 
FOR and how they ﬁt within a wider classiﬁcation system, see www.arc.gov.au/ 
grants/grant-application/classiﬁcation-codes-rfcd-seo-and-anzsic-codes . Accessed 
21/03/2022. 
14 These 17 schemes were Discovery Early Career Researcher Award; Discovery Projects; 
Australian Laureate Fellowships; ARC Future Fellowships; Industrial Transformation 
Training Centres; Discovery Indigenous; Linkage Infrastructure, Equipment and Facili-
ties; Linkage Projects; ARC Centres of Excellence; Special Research Initiatives; Support-
ing Responses to Commonwealth Science Council Priorities; Learned Academies Special 
Projects; Industrial Transformation Research Hubs; Discovery Indigenous Researchers 
Development; Linkage – International; Federation Fellowships; and, Research Networks. 
15 The two additional schemes to award funding for STEM research exclusively are the 
Super Science Fellowships and the Linkage-CSIRO. 
16 https://kclpure.kcl.ac.uk/portal/en/organisations/digital-humanities(b2f7d708-74dd-
4fbe-b858-a36f316611dc)/projects.html?query=. Accessed 25/01/2023. 

     
 
     
     
    
     
      
    
      
        
  
 
    
     
 
 
  
  
 
 
 
 
 
  
 
  
   
   
  
 
 
  
 
   
  
    
 
 
 
A False Dichotomy 2 1 
17 https://theconversation.com/long-before-silicon-valley-scholars-in-ancient-iraq-
created-an-intellectual-hub-that-revolutionised-science-191589. Accessed 31/01/2023. 
18 See, for example, https://play.google.com/books/reader?id=EIVqHUm9WlkC&pg=GBS. 
PA690&hl=en_GB . Accessed 24/08/2021. 
19 www.maa.org/press/periodicals/convergence/mathematical-treasure-ada-lovelaces-
notes-on-the-analytic-engine. Accessed 24/08/2021. 
20 All puns intended. 
21 www.museumsandtheweb.com/forum/report_cultural_heritage_and_the_semantic_ 
web_study_da.html. Accessed 03/08/2021. 
22 www.youtube.com/watch?v=VZBpFiLbi-Y&feature=youtu.be&ab_channel=MiriamPosner. 
Accessed 03/08/2021. 
23 www.w3.org/2011/gld/wiki/5_Star_Linked_Data. Accessed 25/05/2022. 
24 The table is inspired by other sources such as www.w3.org/2011/gld/wiki/5_Star_ 
Linked_Data#:~:text=Short%20description%3A%20Tim%20Berners%2DLee,the%20 
previous%20step(s ) and  https://5stardata.info/en/ . Accessed 14/02/2023. 
25 See, for example, www.w3.org/TR/rdf11-primer/, https://stackoverﬂow.com/questions/ 
69877279/retrieve-objects-from-rdf-triples or www.marklogic.com/blog/making-new-
connections-ml-semantics/ for simple examples of the triple visualised as labelled cir -
cles and arrows. Accessed 14/02/2023. 
26 www.w3.org/DesignIssues/LinkedData.html. Accessed 27/05/2022. 
27 www.semanticscholar.org/paper/OntoMedia%3A-An-Ontology-for-the-Representation-
of-Jewell-Lawrence/c8e6add16ad6efd76ca13135c5fcf808f73cf3c5. Accessed 24/01/2023. 
Bibliography 
Al-Khalili, J. (2010). Pathﬁ nders: The Golden Age of Arabic Science. Penguin UK. 
Berners-Lee, T. (1999). Weaving the Web: The Past, Present and Future of the World Wide 
Web by Its Inventor. London: Orion Publishing Co. 
Berners-Lee, T., Hendler, J., and Lassila, O. (2001). “The Semantic Web”.  Scientiﬁ c Ameri-
can, 284(5), pp. 34–43. 
Bishop, C. (2018). “Against Digital Art History”.  International Journal for Digital Art His-
tory, 3(July). 
Burdick, A., Drucker, J., Lunenfeld, P., Presner, T., and Schnapp, J. (2016). Digital_ 
Humanities. MIT Press. 
Bush, V . (1945). “As We May Think”.  The Atlantic Monthly, 176(1), pp. 101–108. 
Dallas, C. (1992). “Syntax and Semantics of Figurative Art: A Formal Approach”. In Reilly, P., 
and Rahtz, S. (eds). Archaeology and the Information Age: A Global Perspective. Routledge. 
de la Rosa, J., and Suárez, J. (2015). “A Quantitative Approach to Beauty: Perceived At-
tractiveness of Human Faces in World Painting”. International Journal for Digital Art 
History, 1, pp. 112–129. 
Doornbusch, P. (2004). “Computer Sound Synthesis in 1951: The Music of CSIRAC”. Com-
puter Music Journal, 28(1), pp. 10–25. 
Foucault, M. (1970). The Order of Things: An Archaeology of the Human Sciences. Vintage 
Books, A Division of Random House, Inc. 
Grayling, A. C. (1988).  Wittgenstein: A Very Short Introduction. Oxford University Press. 
Gruber, T. R.(1993). “A Translation Approach to Portable Ontology Speciﬁcations”. Knowl-
edge Acquisition, 5(2), pp. 199–220. 
Ives, J., and Castillo-Montoya, M. (2020). “First-Generation College Students as Academic 
Learners: A Systematic Review”.  Review of Educational Research, 90(2), pp. 139–178. 

 
  
   
 
 
 
 
 
 
  
 
 
 
  
 
 
 
  
 
  
   
 
 
 
 
   
  
 
  
 
  
 
  
 
   
  
 
   
  
 
 
   
22 A False Dichotomy 
Képéklian, G., Curé, O., and Bihanic, L. (2015). “From the Web of Documents to the Linked 
Data”. In Zimányi, E., and Kutsche, R. D. (eds). Business Intelligence. eBISS 2014. Lec-
ture Notes in Business Information Processing, vol 205. Springer. 
Koetsier, T. (2001). “On the Prehistory of Programmable Machines: Musical Automata, 
Looms, Calculators”. Mechanism and Machine Theory, 36(5), pp. 589–603. 
Misa, T. J. (2016). “Charles Babbage, Ada Lovelace, and the Bernoulli Numbers”. In Ham-
merman, R., and Russell, A. L. (eds). Ada’ s Legacy: Cultures of Computing From the 
Victorian to the Digital Age. Morgan and Claypool. 
Nurmikko-Fuller, T. (2018). “Publishing Sumerian Literature on the Semantic Web”. In Ju-
loux, V ., Gansell, A., and Di Ludovico, A. (eds). CyberResearch on the Ancient Near East 
and Neighboring Regions. Brill. 
Nurmikko-Fuller, T., and Hart, I. E. (2020). “Constructive Alignment and Authentic Assess-
ment in a Media-Rich Undergraduate Course”. Educational Media International, 57(2), 
pp. 167–182. 
Nurmikko-Fuller, T., and Pickering, P. (2021). “Reductio ad Absurdum?: From Analogue 
Hypertext to Digital Humanities”. Proceedings of the 32nd ACM Conference on Hyper -
text and Social Media (ACMHT21), Dublin, Ireland, 30 August–02 September. 
Patﬁeld, S., Gore, J., and Weaver, N. (2021). “On ‘Being First’: The Case for First-
Generation Status in Australian Higher Education Equity Policy” .  The Australian Edu-
cational Researcher, pp. 1–19. 
Peroni, S., and Shotton, D. (2018). “The SPAR Ontologies”. In Vrandečić, D. et al. (eds). 
The Semantic Web – ISWC 2018. Lecture Notes in Computer Science , vol. 11137. 
Springer. 
Reeves, T., Herrington, J., and Oliver, R. (2002). “Authentic Activities and Online Learn-
ing”. Proceedings of the 25th Higher Education Research and Development Society of 
Australasia (HERDSA) Annual Conference, Perth, Western Australia, 7–10 July. 
Repko, A. F., and Szostak, R. (2020). Interdisciplinary Research: Process and Theory. Sage 
Publications. 
Schreibman, S., Siemens, R., and Unsworth, J. (eds.). (2004). A Companion to Digital Hu-
manities. Blackwell. 
Schreibman, S., Siemens, R., and Unsworth, J. (eds.). (2015). A New Companion to Digital 
Humanities. John Wiley & Sons. 
Simpson, R. M. (2020). “Augustine as ‘Naturalist of the Mind’”. In Proceedings of the 
31st ACM Conference on Hypertext and Social Media (ACMHT20), Virtual Event, USA, 
13–15 July. 
Snow, C. P. (1961). “The Two Cultures and the Scientiﬁc Revolution”. In  The Rede Lecture 
1959. Cambridge University Press. 
Svensson, P. (2010). “The Landscape of Digital Humanities”. Digital Humanities Quarterly, 
4(1). 
Wilks, Y ., and Brewster, C. (2009). Natural Language Processing as a Foundation of the 
Semantic Eeb. Now Publishers Inc. 
Wittgenstein, L. (1922). Tractatus Logico-Philosophicus . London Kegan Paul, Trench, 
Trubner & Co., Ltd. Harcourt, Brace & Company, Inc. 
Wood, D., Zaidman, M., Hausenblas, M., and Ruth, L. (2014). Linked Data: Structured 
Data on the Web. Manning. 
Zeng, Marcia Lei (2019). “Semantic Enrichment for Enhancing LAM Data and Supporting 
Digital Humanities. Review Article”. El Profesional de la Información, 28(1), p. e280103. 

 
  
    
 
  
 
 
 
 
   
 
  
  
 
 
   2 Privacy, Ethics, and Trust 
2.1 Preamble 
On July 5, 1993, Peter Steiner published a cartoon about Internet anonymity in The 
New Yorker. The image is well known 1: two dogs are at a desk in an oﬃce, with a 
computer on the table. The white dog sits on the ﬂoor – the black dog sits on the 
chair, eﬀectively at the desk, and is turning round to say something to his compan-
ion on the ﬂoor. The caption reads: “On the Internet, nobody knows you’re a dog”. 
This now cult status meme seems, perhaps with the clarity brought on by the 
hindsight of a quarter of a century, to have captured the public’s fear at that time 
regarding the ability of users to send and receive messages to and from anyone, 
globally, with no accountability, given that no matter how nefarious the person or 
their aims, they possessed the ability to hide in anonymity, or the option of using a 
fake name – the feeling was anyone could (and would!) be out there. Some stran-
ger, someone wholly unknown to you, might be able to communicate with you, 
or with your children. The danger of the online world, as it was perceived then, 
was of individual people, bad people, who could ﬁnd you, but who could not be 
found in return (by law enforcement, for example). Whether or not this captures a 
genuine fear, a mere moral panic, or indeed is just a modern reinterpretation with 
our current fears projected onto it, it is clear the issues of privacy and trust have 
been a challenge for the users, abusers, and developers of the online medium since 
the very days of the Web. Those early days in which the Web was launched to the 
public were in August 1991, two years before this comic was published. 
Twenty-two years later, on February 23, 2015, and also in The New Yorker , 
Kaamran Hafeez revisited the motif. This time, both dogs, looking noticeably 
older, are sitting on the ﬂoor with a man sitting at the desk on his machine. The cap-
tion this time is “Remember when, on the Internet, nobody knew who you were?”. 
Fears of the public are no longer of the unidentiﬁable boogie man lurking among 
the pixels – the new Big Bad are online oligopolies such as Alphabet 
2 (the owner 
of Google, among others) and social media giants such as Facebook, all of them 
thriving by converting our (often readily disclosed) data into ﬁnancial gain through 
targeted marketing and proﬁling of behaviours. The pendulum has swung to the 
opposite extreme, from complete anonymity to the death of privacy in this era of 
the Data Economy ( Allen, 2016 ), where knowledge isn’t just power, it is also cold 
hard cash. 
DOI: 10.4324/9781003197898-2 

 
 
 
     
    
  
 
   
 
 
 
 
 
 
  
 
 
  
 
 
24 Privacy, Ethics, and Trust 
(Digital) Humanities scholars who investigate the lives of historical persons 
may not be familiar with the processes of applying for ethical clearance for one’s 
research, or the issues of privacy when digging into the private lives of their sub-
jects. Computer scientists may be driven by tackling challenges of technical de-
velopment, or perhaps opportunities for monetisation, and not prioritise concerns 
for how their tools might be used. Case study examples of machine learning algo-
rithms having gone awry to great public dismay include the Google Photos debacle 
of 2015 when people were categorised as gorillas;
3 when the Technology Review 
published a story of algorithms showing racist bias when sentencing people to 
prison;
4 and the advertising of chief executive oﬃcer (CEO) positions only to men 
and not women. 5 Another example of development and implementation with seem-
ingly little or no consideration for any ethical issues is in the context of Pokémon 
Go!, an augmented reality (AR) mobile game, where players were lured by the 
prospect of capturing rare monsters to what were simply inappropriate locations: 
the National September 11th Memorial, the Arlington National Cemetery, and the 
Truce Village (in the Demilitarized Zone between South and North Korea), and 
even Auschwitz ( Greenﬁeld, 2017 : 64–65). 
There are, undoubtedly, at least three diﬀerent considerations at play here: ﬁrst, 
whether the tool itself is ethical (or not, such as in the case of the facial recogni-
tion app FindFace, which works in conjunction with one of Russia’s largest social 
media sites, Vkontakte, and “allows users to photograph people in a crowd and 
work out their identities, with 70% reliability”);
6 second, whether the data used 
to populate the project and train the algorithm is diverse enough (or not, as in the 
aforementioned case of Google Photos); and ﬁnally third, whether users are engag-
ing with tools in an ethical way (Pokemon Go!). In any data collection act, there are 
also profound ethical considerations as to how the privacy of the individuals whose 
data is collected can be ensured. 
2.2 The Unavoidable Orwellian Reference 
No paper discussing issues of privacy and surveillance seems to be without its Or-
wellian analysis. The fruit hangs low for a comparison between Nineteen Eighty-
Four and the state of surveillance technology in the early 21st century. But aligning 
the two as equivalent or even similar is an oversimpliﬁcation (Nurmikko-Fuller 
and Pickering, 2022). Orwell’s vision fails to match the current reality of the West-
ern world in two ways. First, we are not living under the tyranny of a single des-
potic leader. Second, unlike Winston’s stolen moments with his diary, we have 
nowhere to hide. As noted by  Greenﬁeld (2017 ), data takes many forms, including 
that of text and video footage. Social media content is thus a prime example of vast 
quantities of data produced incessantly by users across the glo be. This data which 
maps our every move, every mood, every meal, everything. 
The question that may then arise is one of deﬁning what exactly constitutes 
“surveillance”? To avoid rushing head-ﬁrst down a rabbit-hole of semantics and 
dictionary deﬁnitions, I’ll cut to the chase: is surveillance which is not just enabled 
by the huge numbers of pieces of expensive hardware we choose to carry on our 

  
 
 
 
 
    
 
 
  
  
  
 
 
  
 
  
 
 
 
 
 
 
Privacy, Ethics, and Trust 2 5 
person (signs of aﬄuence, social prestige, etc.) or use in our homes but actively 
feed by the content we deliberately choose to share still surveillance? As we argued 
in Nurmikko-Fuller and Pickering (2022), social media users are all data produc-
ers, but there are myriad other ways we all produce data, even those who abhor the 
thought of a Facebook proﬁle, those of us who baulk at smartphones, by those who 
lurk (having created a proﬁle on one platform or another, but do not post content 
themselves). Each banking transaction, every online bill, those shoes we brought 
from the Online Only part of the website, the pizza we got delivered yesterday, all 
those commercial actions leave a digital footprint. So do all your online searches, 
the shows you stream, the people you message. The epitome of the omniscience 
and ubiquity of surveillance manifest in products and services (although neither is 
a product many would wish to acquire nor a service that any of us can easily opt out 
of) that propose to ease our everyday lives and schedules. Google’s Smart Reply 
and Smart Compose are very clear examples. As described by Natt Garun in 2020: 
7 
You can also choose to allow Gmail’s machine learning to personalise the 
suggestions based on the way you write your emails by choosing “Smart 
Compose personalization”. For example, if you greet your colleagues with 
“Hi, team” versus “Hello, everyone”, it will automatically drop in whatever 
you use most often. 
The crucial phrase here is “ you use most often”. The only way this can be 
achieved is by the systematic and complete reading of all the content you have 
written to date. Every email, every reply. Where in this scenario is the space to hide 
from the all-observing screen? There is no nook or cranny of privacy here. 
“But!” those who would read Garun’s aforementioned article on the Verge 
beyond that quote will shout “You have to opt into them both!”. And quite right 
they are. 
Let’s consider in this context “surveillance” equating to a loss of privacy. Of 
constant, albeit asynchronous observation. Although the user might not be under 
scrutiny and recording at all times by Google specially, the total history of collec-
tive email correspondence can be examined at any one given time . What can only 
be said then is that the option of not being observed on the current Web begins to 
feel like it is simply not an option. Or, perhaps it is an option, but it is not an option 
that is in any realistic means available to the user, or anyone else who has similar 
preferences, habits, or lifestyle choices . Proﬁling is powerful because it does not 
require the proﬁler to observe you: it’s enough to observe enough people who are 
like you. 
Beyond the overt social media posts of data sharing, we are all observed cov-
ertly though data that records, inter alia, medical, ﬁnancial, and biological data; 
we are monitored by the state. One of the challenges of Linked Data is actually a 
privacy debacle waiting to happen: What would happen if all this information from 
diﬀerent sources would be deliberately amalgamated to create a comprehensive 
and complete picture of an individual? Or (more frighteningly perhaps) of a type of 
individual likely to engage in a particular type of behaviour? 

 
  
 
  
 
  
 
 
 
   
 
  
 
 
  
 
 
  
26 Privacy, Ethics, and Trust 
Given that much of the Data Economy is centred on proﬁling for behaviours 
(Bechmann, 2013 ), that may be all that matters: proﬁt can be turned not just from 
successful targeted marketing, but also through a process of identifying shared 
behaviours. User proﬁling is the method of eﬀectively using the observed and re-
corded habits of users to predict (rather successfully!) the behaviours of others. 
Demography, consumer choices, time spent on a page, keyword search patterns, all 
contribute towards a comprehensive collection of data about a user. In some cases, 
data aggregated in a speciﬁc context has been sold to the highest bidder: one of 
the more nefarious instances of this being from the UK, where the National Health 
Service (NHS) sold the data of millions of clients to pharmaceutical companies in 
2019.
8 
In all online activities, there are serious concerns about privacy, ethics, and 
trust. This is even more poignant when discussing a technology (Linked Data) 
that is perfectly designed to overcome all aspirations of privacy, and instead com-
bine complementary information about our person (health data, consumer habits, 
tax records, employment, hobbies, home address, Netﬂix listings, holiday plans, 
frequency of ordering pizza, etc.) until a comprehensive and complete picture is 
formed. Ethical? Of course not. Possible? You bet your cotton socks it is. 
2.3 Privacy as a Right, Not a Privilege 
In his 2011 TED Talk, Mikko Hyppönen 
9 described three kinds of online attack. 
His focus was predominantly on the way governments have used digital technolo-
gies such as Trojans to monitor and attack their own citizens. His concluding state-
ment in made in that context speciﬁcally: 
[You might think:] “But why should I worry? I have nothing to hide ”. And 
this is an argument that doesn’t make sense. Privacy is implied. Privacy is 
not up for discussion. This is not a discussion between privacy against secu-
rity. It’s a question of freedom against control. And while we might trust our 
governments right now, right here in 2011, any rights we give away will be 
given away for good. 
A decade later, in the aftermath of events like the Trump Administration in the 
USA, and the Cambridge Analytica scandal, we can see the signiﬁ cance of these 
words. But, surely democratic governments at least are in some ways regulated, 
held accountable, controllable in some way? But what of private companies? What 
about Facebook? 
The other signiﬁcant part of the statement is the implication of privacy. Any 
researcher wanting to conduct experiments or scrape data from Facebook would 
be faced with a rigorous process of successfully applying for ethics approval. In 
the case of more open, more public platforms such as Twitter and Reddit, this is 
relatively straightforward, as the content posted on these forums is open and pub-
licly available. The same cannot be said of all forums and platforms. There is an 
implied privacy with Facebook, for example, that content is only visible to you 

 
 
  
 
   
    
   
  
  
 
   
 
   
 
 
 
   
   
 
   
 
  
 
 
 
Privacy, Ethics, and Trust 2 7 
and your friends (the speciﬁcs have changed over the years as Terms & Conditions 
have been edited, updated, reworded, etc.). And so now we understand the outrage 
that led the CEO of Facebook Mark Zuckerberg appearing in front of the American 
Senate’s Commerce and Judiciary committees 
10 in 2018 in a hearing addressing 
Facebook’s privacy policy and their use (and abuse) of data. To quote Chairman 
Thune: 
One reason that so many people are worried about this incident is what it 
says about how Facebook works. The idea that for every person who decided 
to try an app, information about nearly 300 other people was scraped from 
your service is, to put it mildly, disturbing. And the fact that those 87 million 
people may have technically consented to making their data available doesn’t 
make those people feel any better. The recent revelation that malicious ac-
tors were able to utilise Facebook’s default privacy settings to match email 
addresses and phone numbers found on the so-called Dark Web to public Fa-
cebook proﬁles potentially aﬀecting all Facebook users only adds fuel to the 
ﬁre. What binds these two incidents is that they don’t appear to be caused by 
the kind of negligence that allows typical data breaches to happen. Instead 
they both appear to be the result of people exploiting the very tools that you 
created to manipulate users’ information. 
In the aftermath of this intensive scrutiny into the manner in which its users’ data 
had been insidiously accessed by a third party, Facebook’s numbers and annual 
turnover declined, but only momentarily: in January 2019, BBC published data 
showing that not only had Facebook emerged unscathed but its proﬁts had actually 
increased.
11 But at least this furore over Cambridge Analytica – the beneﬁciary of 
the raid on Facebook’s data – exposed two things: ﬁrst, that privacy in the social 
media sphere was never an option; and second, that confessing to a smaller crime 
(targeted marketing) appeases many to such an extent that more egregious viola-
tions remain undetected let alone punished (Nurmikko-Fuller and Pickering, 2022). 
The truth emerges that to live in the Data Economy, as we all do, is to live in 
a time of what Zuboﬀ (2019 ) called “surveillance capitalism”. Two metaphors of 
overt and constant observation, Orwell’s Nineteen Eighty-Four ( 1949 ) and Jeremy 
Bentham’s idea of the Panopticon have dominated discourse, but are ill-equipped 
as metaphors for the types of non-government-driven surveillance that social me-
dia giants have so successfully monetised ( Browne et al., 2020). The aim of the 
data collection and user observation is not as a reprimand or punishment, but rather 
as a method for revenue generation. Surveillance capitalism, which is undoubtedly 
the true modus operandi of social media giants such as Facebook, is “parasitic and 
self-referential. It revives Karl Marx’s old image of capitalism as a vampire that 
feeds on labour, but with an unexpected turn. Instead of labour, surveillance capi-
talism feeds on every aspect of every human’ s experience” ( Zuboﬀ, 2019 ). 
Since data is the currency of the Age, could data sovereignty and control over 
our own data present a solution? Certainly, there have been eﬀ orts to legislate 
such power and control over what seems to be as inherently ours as our physical 

 
 
 
 
  
 
 
  
   
 
  
 
 
    
 
 
   
 
28 Privacy, Ethics, and Trust 
bodies – since the law allows us to determine who can have acce ss to by physical 
being, why would it not extend to the digital representation as well? The policies 
of the European Union are a good example of exactly that type o f policy. 
Calls for data sovereignty may well have originated in concerns around transna-
tional data ﬂows enabled by cloud computing ( Irion, 2012 ), but it has been increas-
ingly applied to the global movement12 of understanding the term in the context of 
the data of Indigenous groups and their autonomy from post-colonial states ( Ku-
kutai and Taylor, 2016 ). Alas, no solution has been proven to be a silver bullet. 
The challenges here are myriad, and range from data literacy to cultural sensitivi-
ties; from non-Western knowledge structures to the collection, use, and misuse of 
Indigenous data; and practical and pragmatic considerations of data acquisition, 
curation, and maintenance. 
At the same time, users across all demographic groups have been becoming more 
aware of the possibility and the need to assert control over their data have had, in 
some cases, political outcomes. A well-known example of this is the European Un-
ion’s General Data Protection Regulation 2016/679 (GDPR). Primarily focused on 
the regulation in EU law of issues related to data protection and individual privacy 
(and thus seen, arguably, as predominantly aﬀecting the European Union and the 
European Economic Area), it nevertheless also addresses the transfer of personal 
data outside the EU. The concern is that if data could be made into a commercial 
product, which we could opt to sell, it risks perpetuating privacy as a privilege of 
the wealthy, who have the luxury of opting not to sell their data. How this would 
aﬀect the economic models of Instagram inﬂuencers or self-perpetuating promo-
tion machines such as the Kardashians (social media socialites, famous for be-
ing famous) is unclear. What the immense wealth of the likes of Kim Kardashian 
(US$1 billion) 
13 and her sister Kylie Jenner (US$700 million) 14 proves is that in the 
current data climate, there are millions to be made in engaging in the performance 
of sharing one’s life online. 
2.4 Privacy Paradox 
No conversation about the publication of data online could be complete without 
the inclusion of the Privacy Paradox ( Gerber N. et al., 2018 ). And indeed the dis-
cussions related to privacy, ethics, and trust in this chapter are in the very context 
of understanding human behaviour as paradoxical. It is a discussion that appreci-
ates that current social norms dictate that personal data is voluntarily produced and 
shared as postings of text, image, sound, video, and the combination of all those 
ingredients. It is an understanding that there are some who have learnt to monetise 
on the sharing of their data and that these so-called inﬂuencers represent a wholly 
new brand of celebrity. But just as not all musicians become rock stars, so too are 
the billions of marketing dollars denied to most of the Web’s digital denizens. We 
are all producing data, but only some have found a way to make the dollars. 
The Privacy Paradox refers to the “paradoxical dichotomy between privacy at-
titudes and privacy behaviour” exhibited by users of online (and in particular social 
media) platforms ( Kokolakis, 2017 : 125). It stipulates that even when aware of the 

  
  
   
   
 
 
  
 
  
 
 
   
  
 
   
   
  
 
  
 
 
 
  
 
 
Privacy, Ethics, and Trust 2 9 
possibility of surveillance and the compromise of their privacy, users nevertheless 
choose to engage with social media. As  O’Hara and Shadbolt (2014 : 5) assert: 
[the] costs and beneﬁts are the nub of the classic type of privacy problem – 
there are many tangible beneﬁts to be gained by allowing intrusions into one’s 
life, but there is also the intangible worry. We simply ﬁnd it hard, as humans, 
to balance the tangible beneﬁts and the intangible costs. . . In an evil dictator-
ship, one has a good idea of how personal information will be u sed, and so 
can plan accordingly. But in a capitalist democracy, it is much harder to decide 
how information will be used in the future. The beneﬁts are there for all to 
see; the costs are not. This may be why our defences are so often down when 
our privacy is threatened. 
There is thus an agreement that users may exhibit, when asked, a pro-privacy at-
titude, but it is not one strong enough to aﬀect their behaviour. But how much of 
this narrative makes an implicit assumption that all users are capable of asserting 
changes to ensure their privacy, and further, that users could, even if they so choose, 
to opt out? Even in the years preceding the COVID crisis, Zuboﬀ (2019 ) described 
the Internet as “essential for social participation”, and suggestions of abstinence 
from social media were dismissed as detrimental to quality of life and causing 
of increased loneliness ( Vally and D’Souza, 2019 ). During lockdowns and social 
distancing, the community-connecting aspects of social media have undoubtedly 
gone considerably beyond fear of missing out (FOMO). Moore and March (2020 ) 
reported on the positive eﬀect of social media as promoting social cohesion, easing 
the sense of isolation during the pandemic. Wiederhold (2020 ) and Cauberghe et al. 
(2021 ) similarly proved the necessity of social media as a coping mechanism for 
alleviating anxiety during COVID-19. 
Barth and de Jong (2017 ) deﬁned the privacy paradox as the ‘documented fact 
that users have a tendency towards privacy-compromising behaviour online which 
eventually results in a dichotomy between privacy attitudes and actual behaviour’ 
( Barth and de Jong, 2017 ; see also Acquisti, 2004 ). In other words, whilst users 
might be concerned – or express, or feign, concern – about the privacy of their data, 
the fact is that they are unwilling to change their online behaviour to protect it. The 
most compelling commodity in this data exchange is convenience, and we sacriﬁce 
our privacy on the altar of convenience with relentless enthusiasm. Every social 
media proﬁle we create; every post we publish; every cookie we accept, every 
page we cache, as well as every bit and byte of information we insouciantly store 
in the browser; every automated log of geo-coordinates, provide spatio-temporal 
information to unseen eyes. We all understand this at some level. But does it aﬀect 
the way we behave? 
Abstention from this or that social platform makes no diﬀerence. Portable 
technologies – smart phones, watches, even pacemakers – collect data about us 
and those with whom we interact as well as those who we simply pass in the street, 
all without our explicit consent. We are passively, mindlessly, inadvertently the 
subjects of data collection: our photos are geotagged, our movements are traced via 

 
 
 
      
 
 
 
  
      
 
  
 
 
 
 
   
   
  
  
   
  
     
30 Privacy, Ethics, and Trust 
phone location, and little additional inference is required to determine where we 
live, work, or spend our free time (Liccardi et al., 2016). Surﬁng the net lays bare 
our consumer choices, hobbies, predilections, and sexual preferences, which can 
be read in conjunction with State records of our educational attainments, illnesses, 
bank balances, investments, tax returns, employment history, and even parking 
ﬁnes. New technologies such as AI, deep learning, and machine inference are be-
ing applied to extant datasets to predict outcomes as radically diverse as the likeli-
hood of terrorist activity 
15 and the suitability for a prestigious job or public oﬃce. 16 
Indeed, unsurprisingly, information is systematically collected to identify and then 
inﬂuence our political preferences. 
2.5 Trusting Data Producers, Trusting Data Consumers 
As users of the Web, we have a number of diﬀerent roles. The three most sig-
niﬁcant ones are those of the data producer, the data consumer, and information 
retriever. 
As data producers, we (as individual users) have long been encouraged to edu-
cate ourselves as to the privacy concerns that arise from our willingness to share 
our lives openly online: Kawase et al. (2013 ) used the example of critical tweets 
about one’s employer potentially causing professional damage a decade ago. Ar -
guably, this role is one of privilege and prestige, limited to those who are on the 
correct side of the Digital Divide: to contribute data to the online world is not 
cost-neutral, nor is it without its barriers. To post on Instagram, one must have a 
smartphone or mobile device that in turn needs to incorporate the technology and 
be in the capable hands of a user with at least adequate skills of photography (not 
to mention the download and installation of the app itself). We need WiFi or a 
monthly contract with an Internet service provider (ISP); the hardware has costs, 
the software has costs, and Web connection has costs. Similarly, the use of the 
hardware necessitates a degree of skill and manual dexterity, the software requires 
at least some skill to engage with it; the Internet connection requires the ﬁnancial 
means for paying for monthly instalments. 
However, human individuals are not the only types of data producers: com-
panies, institutions, businesses, conglomerates, and even national governments 
(in the form of data.gov, data.gov.uk, and others) all produce copious amounts of 
data, deliberately. Then is also the covertly collected data: the Terms of Service 
of TikTok, for example, mandate that “you must provide accurate and up-to-date 
information about yourself (such as your date of birth)”, 
17 but mention nothing of 
the “aggressive” 18 data harvesting the platform carries out: their Privacy Policy 
stipulates they collect data about users (name, date of birth, phone number, pass-
word, etc.); content (content and its metadata, including geographical locations); 
purchasing history, and so on. TikTok also collects the content of private messages 
between users, and, again, the associated metadata. “Even if you are not a user , 
information about you may appear in content created or published by users on the 
Platform”.
19 Furthermore, as exposed by WIRED in 2021, “TikTok infers factors 
such as your age range, gender and interests based on the information it has about 

   
    
 
 
 
 
  
 
 
 
 
 
    
   
  
 
    
 
 
 
 
Privacy, Ethics, and Trust 3 1 
you. In the US, TikTok can collect biometric information including face and voice-
prints”.20 Choice, control, and autonomy have very little to do with how much data 
is generated, but we are all data producers all the same. 
Perhaps it is in the category of data consumers that most obviously consist of 
agents other than individual humans. Depending on where along the workﬂow we 
focus, data is retrieved, analysed, and reported on by not only individuals but also 
research clusters, companies, and even software agents. It is in this space, above 
all others, where we can see the deﬁning characteristics of the Information Age, the 
Web sitting at the very core of the Data Economy: knowledge was always power, 
but now it is also cold hard cash. In this space, we have seen the emergence of com-
mercial clients, of which at the time of writing none could be argued to be more 
prominent (nor controversial) as Facebook. The most remarkable aspect of this 
platform is that it is exactly that: a platform, a stage on which we (the users) carry 
out our performative acts of social engagement. Facebook does not build anything, 
it does not make anything – all the content, all the reason to be there, as a user, is 
provided by the user. 
None can doubt the signiﬁcance of the Web as the largest, near-ubiquitous hy-
permedia system that dominates information exchange globally. As information 
retrievers, we have moved away from trawling through a library’s card index to 
optimising our keyword searches on Google so that the correct link is displayed 
above the fold on our screens. Two important considerations arise here: ﬁrst, the 
Filter Bubble (coined by Eli Pariser in 2011 ), a result of Google’s personalised 
searchers, which prioritises the content we discover online based on prior success-
ful searches (i.e. the links we have clicked on previously), and distorts how we see 
and understand the world, especially if we are lulled into believing that our search 
results are unbiased or neutral. Second, is the role that the Web plays as a tool for 
cognitive extension ( Clark and Chalmers, 1998 ): we might not know all that we 
know, or be able to remember it, but we know that we can retrieve that information, 
and what keywords to use to maximise the likelihood of ﬁnding our way to that 
material. To quote Zuboﬀ (2019 ): “the entangled dilemmas of knowledge, author-
ity, and power are no longer conﬁned to workplaces as they were in the 1980s. Now 
their roots run deep through the necessities of daily life , mediating nearly every 
form of social participation” (italics my own, for emphasis). It is thus no hyperbole 
to say that never before has there been a greater need for digital literacy and criti-
cal evaluation of what we encounter online, and a recognition of the agents, which 
determine the content we see. 
Finally, in an era of Linked Data and machine learning in a Data Economy, it 
is not the individual that matters. What is important is behaviour, which can be 
mapped, modelled, proﬁled and, ultimately, applied to others. As noted by Zuboﬀ 
(2019 ), “surveillance capitalism feeds on every aspect of every human’ s experi-
ence”. Every human, every experience. Our footsteps count (literally), not us. Pro-
ﬁling provides immense amounts of data that is most valuable when it is aggregate. 
Even if there is no one else who behaves exactly like you, there are those who 
behave exactly like you in some ways. When the individual portraits of a cohort are 
overlaid a digital identikit proﬁle can be formed. 

 
  
 
   
 
 
 
  
        
 
  
   
  
  
  
 
     
  
   
 
    
  
 
 
  
  
 
32 Privacy, Ethics, and Trust 
2.6 Potential for Disaster 
The most prominent selling point of Linked Data – its entire raison d’etre! – is to 
connect disparate data sources that contain information about the same thing (or 
the same category of thing) published online. Since this is achieved through the use 
of HTTP URIs (as described in Chapter 1 ), each data instance (such as a speciﬁ c 
individual, place, or event) and every characteristic about that entity are captured 
in an entirely unambiguous way. The amalgamation of complementary information 
from diﬀerent sources is possible because we can unambiguously state that both 
datasets contain information about the same thing. 
For much of research, this is a fantastic thing. Museum collections are enriched 
by objects and their metadata even if held in collections in diﬀerent countries (e.g. 
Europeana);
21 numismatists have very successfully merged their data (Nomisma. 
org); 22 sites such as DBpedia, 23 Wikimedia Commons, 24 and Wikidata 25 reach be-
yond disciplinary silos and merge data covering the contents of the encyclopaedic 
Wikipedia. At the time of writing, the Linked Open Data Cloud 26 had a taxonomy 
of nine diﬀerent categories, 27 but one of these is the inherently nebulous and un-
deﬁned “User-Generated” – which, by the way, is something diﬀerent from “So-
cial Networking”, “Media”, and “Cross Domain”. As of May 2020, the Cloud’s 
dataset contained 1,301 datasets, which in turn contained 16,283 links. 
28 These 
are small numbers: but note that each dataset has a minimum of 1,000 triples and 
a minimum of 50 links connecting up to other datasets that are already part of 
the Cloud. A thousand triples may well be the minimum limit for inclusion, but 
it is by no means representative of a typical dataset. To give some examples, the 
aforementioned DBpedia’s 2015 release of Data Set 3.8 consisted of 1.89 billion 
RDF triples. 
29 The Biblioteca Escolar Digital CITA contains only 930,765 triples; 30 
GeoNames Semantic Web has 93,896,732 of them; 31 the Hellenic Police has a mere 
145,368.32 The opportunity and aﬀordance presented by this aggregation of data is 
the enrichment and diversiﬁcation of a given topic from a range of sources – and, 
potentially, the discovery of new information from places and datasets we didn’t 
know to query. 
The W3C lists a number of beneﬁts to the adoption of the Linked Data model. 
33 
These range from the somewhat abstract notions of making data “shareable, ex-
tensible, and easily re-usable”. What is interesting, telling, and worth noting at 
this stage is that the W3C has identiﬁed diﬀerent categories of users who they 
perceive as having a speciﬁc and particular interest in the Linked Data methodol-
ogy. The site lists diﬀerent categories under four headings: Researchers, Students, 
and Patrons; Organisations; Librarians, Archivists, and Curators; and Developers 
and Vendors. The detailed descriptions are themselves rather generic and rather 
exchangeable between the categories. 
34 Alas, there is no equivalent page where the 
W3C would list the drawbacks or challenges of Linked Data. 
Yet, the Linked Data paradigm is a potential privacy disaster. The practical and 
pragmatic methods for anonymising data are centred around removal of details. 
A simple example of this might be a database of addresses. Instead of having the 
name (say, “Dr Smith”) and the address (e.g. “123 Example Street”) of a person, 

 
 
  
 
 
 
   
 
 
 
 
 
 
 
 
 
 
 
Privacy, Ethics, and Trust 3 3 
the database would contain the address, and in lieu of a name, an alphanumeric 
code to serve as the identiﬁer for the entity dwelling at that address. The pairing 
for the name and the identiﬁer could reasonably be expected to sit somewhere else, 
perhaps on an encrypted hard drive, or some other non-Web-enabled device. This 
seems rather straight-forward. So what’s the problem? 
The challenge here is Linked Data’s entire purpose is to help us ﬁll in the gaps 
by bringing in information from other sources. In this case, you might then reason-
ably expect that there might be another database, which holds, say, the shopping 
details of Dr Smith. In this database, anonymisation has occurred through the re-
moval of the delivery address of the goods (123 Example Street). So what happens 
when the two datasets are merged? You got it. Now we know where Dr Smith lives 
and where they like to shop. 
This example might seem rather benign, but who among us would like to see 
diﬀerent types of information about us combined for use by external entities? In-
surance companies, for example, might reasonably be delighted to be able to access 
information about a client’s lifestyle (from devices and platforms such as Garmin 
watches, Strava, etc.), shopping habits, and medical records. 
35 A moral, ethical, and 
philosophical question might then be: “Should people who have healthier lifestyles 
be recipients of better/cheaper insurance premiums?”. Or what data is collected, 
say, by the state, and used to determine whether a person is deserving of beneﬁts, 
lower rates of taxation, or the ability to vote? It might seem dismissible as dys-
topian fear mongering, but let’s recall Hyppönen’s warning: access to data once 
granted to a benevolent state will not be relinquished by a malevolent one. 
With so much potential for misuse and abuse, why collect this data at all? And 
why share it? We need to discuss the Quantiﬁed Self (QS). 
2.7 We Need to Talk About Strava 
The QS is, in and of itself, a privacy paradox. It is the phen omenon or practice of 
collecting biological, behavioural, environmental, and other data about oneself. In 
the mainstream, it is particularly popular with athletes who re cord data to better 
understand and develop their training. Information about heart rate, speed, cadence, 
global positioning system (GPS), and a myriad other details are diligently collected. 
All this information is useful, valuable, and for athletes, trainers, and indeed anyone 
who ﬁts the label of a “data fetishist” ( Sharon and Zandbergen, 2017 ), genuinely 
interesting. But what could possibly go wrong with sharing this data openly? 
Let’s focus on an easy example: location data. In the days before Uber, few of us 
would have considered giving our address to a complete stranger online. Because 
they might ﬁnd you! But now, we give this information to strangers, Whose very 
purpose, and (very literal, in the case of Uber!) drive is to come and get you! The 
obvious workaround for stationary location data is to move to a random or mean-
ingless location, but this is not always possible: swimming pools, for example, are 
rather immobile, running tracks also, and even cycling routes and lanes are rather 
immutable. Add to this the inherently repetitive nature of training in terms of loca-
tion, time of day, and frequency, and the data could be easily used to predict the 

 
 
  
 
 
 
 
 
 
  
  
    
  
 
 
  
 
 
  
 
 
 
 
  
   
 
  
 
34 Privacy, Ethics, and Trust 
next time a user will be at a speciﬁc location. Data from Strava (an American Web 
platform that enables users to track physical exercise such as running and cycling 
and to share that data with others through the platform’s social networking func-
tionality) has already been used to identify hidden locations using this pattern of 
training (in this case, a military base).
36 
But the scary thing of location tracking data goes further still. In their 2016 pa-
per, Liccardi et al. proved that simply by observing location and time of day, partic-
ipants were able to determine whether the data in question displayed the subject’s 
home address, work place, or route on their commute. Of these, the commute was 
the easiest to spot, and the place of employment the second. Simply by combining 
two types of information (when and where), it would be possible to infer greater 
detail about a person. Where do they work? What do they do? A location pin at a 
military base or a university campus might be a clue. 
It is not just a matter of being vulnerable when you are found: the absence of 
the resident from a home would naturally make it more attractive to opportunistic 
crime. Interestingly, much of the academic work using Strava data is ﬁrmly in 
the space of improving and developing high-performance cyclists (Lee and Sener 
published a literary review on the topic in 2021 ), or in studies examining the eﬀect 
of air pollution ( Sun et al., 2017 ). Popular media on the other hand is a rich source 
of content about undesirable behaviours enabled by platforms like Strava, such as 
“Strava-stalking”. Elizabeth Barber (writing for WIRED, a magazine focusing on 
technology, society, and politics) 
37 and Katie O’Malley (for ELLE, a lifestyle mag-
azine that mostly focuses on fashion) 38 have both published in a confessional sense 
(albeit in styles of writing that ﬂirt dangerously with trivialising the problem). Oth-
ers seem to consider it perfectly reasonable to look up the details of a person who 
shares a short segment of tarmac with them. One user of an open but specialist 
forum commented “I just looked at who was in front of me on a local segment, and 
googled a few of them. One guy keeps cropping up so I posted a comment on one 
of his rides which is pretty close to one of mine”.
39 
Given then that a person could leave themselves so vulnerable by sharing lo-
cation, surely no one would opt to do that? That is precisely where the paradox 
kicks in. Especially with many athletes, the QS provides an additional inspiring 
opportunity for competition. Who wants to win on just race day, when you can win 
the daily race? In January 2022, Strava had 76 million users. 
40 And that number is 
increasing. But whose responsibility is it when things go wrong? 
There is a further twist to the tale of mixing QS data with third-party software 
and services. Via Strava, data isn’t just shared between people (other users), it can 
also be shared across diﬀerent hardware, software, and companies. Those familiar 
with the Facebook and Cambridge Analytica scandal in the 2010s 
41 will know that 
data sharing (or selling) between companies can elicit strong reactions – in the 
aftermath of public outrage, lawsuits, a Netﬂix documentary, and ﬁnes to the Brit-
ish Information Commissioner’s Oﬃce, Cambridge Analytica ﬁled for bankruptcy. 
Facebook emerged largely unaﬀected: in the months following the scandal, there 
was a reported drop in posts, 
42 but, online movements such as #delete/DeleteFacebook 
have had no eﬀect: Statista reports a total of 2.91 billion monthly users for the 

  
  
  
    
 
 
   
 
  
  
 
 
 
  
  
  
 
 
 
 
 
 
Privacy, Ethics, and Trust 3 5 
social media behemoth’s site. 43 Alternatives such as WhatsApp and Instagram may 
have attracted more users as a result – this is a rather moot point from a data pri-
vacy perspective since both platforms are owned by Facebook. 
The issue here is largely reported to be a discrepancy between what data Face-
book and Cambridge Analytica were claiming to be sharing, and what they actu-
ally did. The numbers were huge: 270,000 Facebook users opted in. But as large 
as these numbers were, they were not the full story: it was not only these users but 
their entire social networks that were collected, resulting in a ﬁnal ﬁgure of 87 mil-
lion proﬁles being aﬀected. 
44 
Public outrage (albeit one that was not widely published) ensued when Strava 
disconnected its ties with Apple Health in March 2022. Prior to this date, Strava 
users could and would use the service to collect data about their athletic achieve-
ments. Strava shares this information from and with other third parties. For years, 
45 
users could sync up their data from various diﬀerent pieces of equipment to Strava 
(including watches like Garmin, Polar, etc.), and through to Apple Health. Suc-
cessful completion of the tasks would result in a satisfying data visualisation on 
the watchface referred to as “Closing Your Rings”.
46 Without much notice, Strava 
opted to disable the backend functionality that made that sharing with Apple Health 
possible. DC Rainmaker critiqued the decision, saying: 
There’s not a single sport/ﬁtness device I’m aware of that doesn’t integrate 
with Strava. Thus, it’s become the de facto interchange for sport/ﬁtness data 
over the last few years. And while Strava undoubtedly touts that often, I don’t 
think they’ve fully grasped the downstream ramiﬁcations of that. Either in 
policy or technically . . . Strava’s solution is for you to spend less time with 
their platform. I can’t imagine any company saying “Look, how about you 
don’t use our services?” . . . they don’t understand the technical ramiﬁca-
tions of why their workarounds don’t actually work. Never mind that’s not a 
consumer-friendly practice anyway. 
47 
So strong was the public backlash, so unwavering the demand to have their data 
shared across platforms, that Strava backtracked on the decision, and re-established 
this possible syncing.
48 
But why does any of this matter? Because it illustrates the disjoint between 
assumptions that the privacy paradox is the exclusive right of Instagram inﬂuenc-
ers or teen agers struggling with a sense of potential social isolation. The privacy 
paradox is much more an issue of convenience/entitlement to service that it is of 
FOMO. And, to refer back to the earlier question about surveillance, is it surveil-
lance still if the user demands to have the right to have their data issued to several 
diﬀerent companies, any of which might utilise it for analysis, target marketing, 
user proﬁling, or monetise it the simpler of way of just sell it on to someone else? 
At what point of the data consumer to surveillance victim pathway does the respon-
sibility of the user over their own data come into play? 
And, if we know this is happening at an industry level, and enabled by companies 
and users alike, why do we get some antsy at the prospect of this data aggregation 

 
 
  
 
 
 
 
  
 
 
 
 
 
 
 
 
    
              
  
 
 
  
 
  
 
 
 
  
  
   
 
 
   
 
36 Privacy, Ethics, and Trust 
happening through software or methodologies like Linked Data? Is there any dif-
ference if we are surveilled by people or by algorithms? 
2.8 On the Questions of Ethics 
The topic of ethics is a huge and complex space. Even if focusing exclusively 
on the role of ethics in context to research carried out in the Digital Humani-
ties, the topic is multifaceted and complex. As discussed earlier, one of the ma-
jor considerations of using Linked Data in particular is the potential violation 
of privacy it presents: this is a considerable ethical consideration. In 2022, the 
20th European Networked Knowledge Organization Systems (NKOS) Workshop 
was carried out (virtually) as part of the Joint Conference for Digital Libraries. 
49 
It centred on issues relating to topics of multilingual, multicultural, unbiased 
knowledge representation with considerations of diversity, equity, and inclusion. 
One of the prevailing challenges is around inclusion of diversity within research 
and the inclusion of diﬀerent perspectives into knowledge representation para-
digms: questions around terminology and semantic shifts (e.g. should “illegal 
aliens” be substituted with “undocumented immigrants”?). The Getty V ocabular-
ies have opted for an approach of assisted decision making, and the provision of 
contextual information: For example, terms that have been deemed pejorative or 
objectionable are labelled “avoid use” for new indexing, but historical, obsolete, 
or objectionable terms are not deleted since they provide access and enable dis-
covery. 
50 The use of the Homosaurus vocabulary (discussed further in Chapter 4 ) 
in Sweden 51 and the representation of Indigenous knowledge 52,53,54 ﬂag the need 
for considerations such as the need to be sensitive not only to the desires and 
rights of present-day people (e.g. when describing the gender or identity of an 
artist) but also in applying that sensitivity retrospectively to historical data, such 
as the preferred name of places, locations, and sites. Metadata records of various 
cultural heritage collections across the globe will need to begin to consider how 
they will update terminologies without aﬀecting indexing and thus information 
retrieval. 
Existing guidance for research data particularly in relation to Indigenous ma-
terial exists in the form of the CARE data principles (discussed further in Chap-
ter 3 ). 
55 In the Australian context, the National Statement on Ethical Conduct in 
Human Research 56 is almost entirely silent on the topic of collecting and analys-
ing digital data: in fact, the word “digital” occurs only once in the documentation 
(p. 33), but it does refer to “social media” more frequently (ﬁve times in total). 
These ethical considerations are related to “recruitment strategies [which must] 
adhere to the ethical principles of justice and respect” (p. 28), privacy concerns 
(p. 36) and the Terms and Conditions of various diﬀerent platforms (p. 37). 
The topics on diversity and inclusions were ﬂagged by Estill et al. (2022 ) in the 
context of the Digital Humanities and the disciplines annual international ﬂagship 
conference as well. Issues of (prohibitively) high costs of attendance, lack of lin-
guistic diversity, and the ethical division of labour in conference organisation high-
light that not only is the research process itself that is worthy and needing of ethical 

 
 
  
 
 
   
 
 
 
 
 
  
  
 
 
 
 
 
 
 
 
 
   
 
 
 
 
Privacy, Ethics, and Trust 3 7 
considerations and sensitive approaches, but also, indeed the entire academic land-
scape, from institutional hiring practices to the dissemination of research outputs, 
which need to be examined and evaluated for thoughtful, equitable, and ethical 
research. 
2.9 Conclusion 
This chapter has discussed how the fundamental concepts of privacy, ethics, 
and trust sit at the core of the Linked Data paradigm. Thought-experiments and 
real-life examples have illustrated how disambiguation and amalgamation of 
information from several diﬀerent sources ﬁll in the gaps to thwart any and all 
attempts of anonymisation (privacy); to question where we should draw the 
lines regarding what data should be Open and Linked (ethics); and highlight 
the several diﬀerent ways in which trust plays a fundamental role in knowledg e 
exchange. 
Is privacy a fundamental right that should be protected, a privilege of the aﬄ  u-
ent, or indeed something already irretrievably lost? The notion of privacy is neither 
straightforward to deﬁne nor a universal constant. The discussion in this chapter is 
situated within a historical context, examining the development of the concept of indi-
vidual privacy and one’s right to it as seen and experienced through a Eurocentric lens. 
The second section of the chapter focused on the question of ethics especially 
when using the Linked Data method with personal, ﬁnancial, medical, socio-
culturally sensitive, or otherwise private data. It also questioned who should have 
access to the merged data, and whether or not authorities and governments should 
be enabled to create comprehensive pictures of individuals. 
Trust is given and earned by data consumers and data producers. It is worth 
questioning the eﬀect living in the Data Economy has had on our approaches to in-
formation exchange. The social media revolution saw us all turn into data produc-
ers, and fundamentally changed the information publication paradigm. A decade or 
so later, we live in a time of fake news and alternative facts. Has the democratisa-
tion of information production caused a devaluation of information authorities and 
oﬃcial sources, and how this phenomenon might aﬀect the Linked Data paradigm? 
Should all relevant datasets be connected to? If not, who gets to decide what is 
included, and what is not? 
The topics of privacy, trust, and ethics are all immense, and any one of them 
could easily warrant an entire career examining them. To merge them all into one 
chapter has done little but set the scene for a more detailed discussion of the Linked 
Data paradigm, but one that is grounded ﬁrmly in the understanding of these topics, 
and an awareness of the potential pitfalls. 
Our ideas about privacy, ethics, and trust are multifaceted, but they have also 
changed – from the perspective of society, expectation, cultural norms, and so on – 
over time. The issues of data sovereignty and user responsibility are recurring mo-
tifs in the conversations regarding these topics, but until there are clear ﬁnancial or 
legislative incentives or rules in place, platforms are unlikely to make fundamental 
changes to their modus operandi. As with any system of supply and demand, the 

 
 
 
 
 
 
    
 
  
    
     
      
 
     
   
     
    
     
     
    
    
       
     
      
     
    
    
    
    
    
    
    
    
    
    
38 Privacy, Ethics, and Trust 
Data Economy is unlikely to disappear until there is some grand change to the way 
we produce and consume content online. 
The question of whether it may or may not be ethical to merge readily available 
data may fall silent when faced with a public reaction that is rather reminiscent of 
the Three Wise Monkeys: it is completely OK for platforms to make millionaires 
out of their shareholders using data about us, as long as there is a societal agree-
ment to turn a blind eye to it all. But hey, who doesn’t want a nifty tricoloured 
circle on their watch once a day? 
Notes 
1 It is readily available online (indeed, it has its own Wikipedia page), but copyright re-
strictions mean that inclusion of the image in this book would either incur a ﬁnancial 
cost, or constitute copywrong (the unethical or illegal use of material through disregard 
for copyright law). 
2 https://abc.xyz/. Accessed 11/06/2021. 
3 www.theverge.com/2018/1/12/16882408/google-racist-gorillas-photo-recognition-
algorithm-ai. Accessed 27/05/2022. 
4 www.technologyreview.com/2019/01/21/137783/algorithms-criminal-justice-ai/. 
Accessed 25/02/2021. 
5 www.independent.co.uk/life-style/gadgets-and-tech/news/google-s-algorithm-shows-
prestigious-job-ads-men-not-women-10372166.html. Accessed 25/02/2021. 
6 https://www.theguardian.com/technology/2016/may/17/ﬁndface-face-recognition-app-
end-public-anonymity-vkontakte#:~:text=FindFace%2C%20launched%20two%20 
months%20ago,identities%2C%20with%2070%25%20reliability. 
7 www.theverge.com/21315189/gmail-ai-smart-reply-compose-tools-enable-turn-on-
how-to. Accessed 04/04/2022. 
8 www.theguardian.com/politics/2019/dec/07/nhs-medical-data-sales-american-pharma-
lack-transparency. Accessed 05/04/2022. 
9 www.ted.com/talks/mikko_hypponen_three_types_of_online_attack. Accessed 25/02/2021. 
10 www.washingtonpost.com/news/the-switch/wp/2018/04/10/transcript-of-mark-
zuckerbergs-senate-hearing/. Accessed 25/02/2021. 
11 www.bbc.com/news/technology-46755608. Accessed 27/05/2022. 
12 https://aiatsis.gov.au/publication/116530. Accessed 19/05/2022. 
13 www.forbes.com/sites/maddieberg/2021/04/06/kim-kardashian-west-is-oﬃcially-a-
billionaire/?sh=1bef518121bb. Accessed 25/02/2021 
14 www.forbes.com/proﬁle/kylie-jenner/?sh=3a70b59155b5. Accessed 25/02/2021 
15 www.technologyreview.com/2019/01/21/137783/algorithms-criminal-justice-ai/. 
Accessed 25/02/2021. 
16 www.independent.co.uk/life-style/gadgets-and-tech/news/google-s-algorithm-shows-
prestigious-job-ads-men-not-women-10372166.html. Accessed 25/02/2021. 
17 www.tiktok.com/legal/page/eea/terms-of-service/en. Accessed 30/01/2023. 
18 www.theguardian.com/technology/2022/jul/19/tiktok-has-been-accused-of-aggressive-
data-harvesting-is-your-information-at-risk. Accessed 30/01/2023. 
19 www.tiktok.com/legal/page/eea/privacy-policy/en. Accessed 30/01/2023. 
20 www.wired.co.uk/article/tiktok-data-privacy. Accessed 30/01/2023. 
21 https://pro.europeana.eu/page/linked-open-data. Accessed 25/02/2021. 
22 https://nomisma.org/. Accessed 05/04/2022. 
23 www.dbpedia.org/. Accessed 05/04/2022. 
24 https://commons.wikimedia.org/wiki/Main_Page. Accessed 05/04/2022. 
25 www.wikidata.org/wiki/Wikidata:Main_Page. Accessed 05/04/2022. 
26 https://lod-cloud.net/. Accessed 05/04/2022. 

    
    
    
    
    
    
     
    
 
      
      
 
    
     
     
    
 
     
 
     
 
 
     
     
     
    
     
     
    
    
     
     
     
     
    
     
 
 
   
Privacy, Ethics, and Trust 3 9 
27 These categories are: Cross Domain, Geography, Government, Life Sciences, Linguis-
tics, Media, Publications, Social Networking, and User-Generated.  
28 https://lod-cloud.net/#about. Accessed 05/04/2022. 
29 http://downloads.dbpedia.org/wiki-archive/data-set-38.html. Accessed 05/04/2022. 
30 https://lod-cloud.net/dataset/biblioteca-escolar-digital-cita. Accessed 05/04/2022. 
31 https://lod-cloud.net/dataset/geonames-semantic-web. Accessed 05/04/2022. 
32 https://lod-cloud.net/dataset/hellenic-police. Accessed 05/04/2022. 
33 www.w3.org/2005/Incubator/lld/wiki/Beneﬁts. Accessed 05/04/2022. 
34 Why, for example, would creating “an open, global pool of shared data that can be used 
and re-used to describe resources, with a limited amount of redundant eﬀort” be exclu-
sively of interest to libraries? 
35 https://slate.com/technology/2014/09/insurance-companies-are-using-quantiﬁed-self-
data-for-accountability-tracking.html. Accessed 06/04/2022. 
36 www.bbc.com/news/technology-42853072#:~:text=Online%20ﬁtness%20tracker%20 
Strava%20has,the%20heatmap%2C%20a%20spokesman%20said. Accessed 06/04/2022. 
37 www.wired.com/story/strava-love-surveillance/. Accessed 07/04/2022. 
38 www.elle.com/uk/life-and-culture/culture/a32955987/strava-stalker/. Accessed 07/04/2022. 
39 https://singletrackworld.com/forum/topic/strava-stalking-etiquette/. Accessed 07/04/2022. 
40 www.businessofapps.com/data/strava-statistics/#:~:text=Strava%20currently%20has%20 
76%20million,adds%20one%20million%20every%20month. Accessed 06/04/2022. 
41 An event of such historical magnitude that it warranted a Wikipedia entry: https:// 
en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal . 
Accessed 07/04/2022. 
42 www.theguardian.com/technology/2019/jun/20/facebook-usage-collapsed-since-scandal-
data-shows#:~:text=Since%20April%202018%2C%20the%20ﬁrst,the%20business% 
20analytics%20ﬁrm%20Mixpanel. Accessed 07/04/2022. 
43 www.statista.com/statistics/264810/number-of-monthly-active-facebook-users-
worldwide/. Accessed 07/04/2022. 
44 www.theguardian.com/technology/2019/mar/17/the-cambridge-analytica-scandal-
changed-the-world-but-it-didnt-change-facebook. Accessed 07/04/2022. 
45 www.dcrainmaker.com/2022/03/strava-abruptly-ends-3rd-party-data-push-to-apple-
health.html Accessed 06/04/2022. 
46 www.apple.com/au/watch/close-your-rings/. Accessed 06/04/2022. 
47 www.dcrainmaker.com/2022/03/strava-abruptly-ends-3rd-party-data-push-to-apple-
health.html. Accessed 07/04/2022. 
48 www.tomsguide.com/news/strava-just-removed-this-key-apple-watch-feature-but-we-
have-a-solution Accessed 07/04/2022. 
49 https://nkos-eu.github.io/2022/programme.html. Accessed 26/01/2023. 
50 https://nkos-eu.github.io/2022/content/NKOS2022-presentation-harpring.pdf. Accessed 
26/01/2023. 
51 https://nkos-eu.github.io/2022/content/NKOS2022-abstract-golub.pdf. Accessed 26/01/2023. 
52 https://nkos-eu.github.io/2022/content/NKOS2022-abstract-shiri.pdf. Accessed 26/01/2023. 
53 https://digital.lib.washington.edu/researchworks/handle/1773/46601. Accessed 26/1/2023. 
54 https://nkos-eu.github.io/2022/content/NKOS2022-abstract-kong.pdf. Accessed 26/01/2023. 
55 www.gida-global.org/care. Accessed 25/02/2021. 
56 www.nhmrc.gov.au/about-us/publications/national-statement-ethical-conduct-human-
research-2007-updated-2018. Accessed 26/01/2023. 
Bibliography 
Acquisti, A. (2004). “Privacy in Electronic Commerce and the Economics of Immediate 
Gratiﬁcation”. Proceedings of the 5th ACM Conference on Electronic Commerce , New 
York, USA, 17–20 May. 

 
  
 
 
 
 
  
  
   
 
 
 
  
  
 
 
 
  
  
 
 
  
   
  
 
  
  
  
 
  
 
   
  
 
 
 
 
 
   
 
40 Privacy, Ethics, and Trust 
Allen, A. L. (2016). “Protecting One’s Own Privacy in the Big Data Economy”. Harvard 
Law Review Forum, 130(2), pp. 71–78. 
Barth, S., and De Jong, M. D. (2017). “The Privacy Paradox – Investigating Discrepancies 
Between Expressed Privacy Concerns and Actual Online Behaviour – A Systematic Lit-
erature Review”. Telematics and informatics, 34(7), pp. 1038–1058. 
Bechmann, A. (2013). “Internet Proﬁling: The Economy of Data Interoperability on Face-
book and Google”. Mediekultur: Journal of Media and Communication Research, 29(55), 
p. 19. 
Browne, K., Swift, B., and Nurmikko-Fuller, T. (2020). “Camera Adversaria”. Proceedings 
of the 2020 CHI Conference on Human Factors in Computing Systems , Honolulu, USA, 
25–30 April. 
Cauberghe, V ., Van Wesenbeeck, I., De Jans, S., Hudders, L., and Ponnet, K. (2021). “How 
Adolescents Use Social Media to Cope With Feelings of Loneliness and Anxiety Dur -
ing COVID-19 Lockdown”. Cyberpsychology, Behaviour, and Social Networking, 24(4), 
pp. 250–257. 
Clark, A., and Chalmers, D. (1998). “The Extended Mind”.  Analysis, 58(1), pp. 7–19.
Estill, L., Guiliano, J., Ortega, É., Terras, M., Verhoeven, D., and Layne-Worthey, G. C. 
(2022). “The Circus We Deserve?: A Front Row Look at the Organization of the An-
nual Academic Conference for the Digital Humanities”.  Digital Humanities Quarterly , 
16(4). 
Gerber, N., Gerber, P., and V olkamer, M. (2018). “Explaining the Privacy Paradox: A Sys-
tematic Review of Literature Investigating Privacy Attitude and Behaviour”. Computers & 
Security, 77, pp. 226–261. 
Gillespie, A. A. (2002). “Child Protection on the Internet – Challenges for Criminal Law”. 
Child and Family Law Quarterly, 14, p. 411. 
Greenﬁeld, A. (2017).  Radical Technologies: The Design of Everyday Life. Verso. 
Irion, K. (2012). “Government Cloud Computing and National Data Sovereignty”. Policy & 
Internet, 4(3–4), pp. 40–71. 
Kawase, R., Nunes, B. P., Herder, E., Nejdl, W., and Casanova, M. A. (2013). “Who Wants 
to Get Fired?”. Proceedings of the 5th Annual ACM Web Science Conference , Paris, 
France, 2–4 May. 
Kierkegaard, S. (2008). “Cybering, Online Grooming and Ageplay”. Computer Law & Se-
curity Review, 24(1), pp. 41–55. 
Kokolakis, S. (2017). “Privacy Attitudes and Privacy Behaviour: A Review of Current Re-
search on the Privacy Paradox Phenomenon”. Computers & Security, 64, pp. 122–134. 
Kukutai, T., and Taylor, J. (2016). Indigenous Data Sovereignty: Toward an Agenda. Aus-
tralian National University Press. 
Lee, K., and Sener, I. N. (2021). “Strava Metro Data for Bicycle Monitoring: A Literature 
Review”. Transport Reviews, 41(1), pp. 27–47. 
Liccardi, I., Abdul-Rahman, A., and Chen, M. (2016). “I Know Where You Live: Inferring 
Details of People’s Lives by Visualizing Publicly Shared Location Data”. Proceedings 
of the 2016 CHI Conference on Human Factors in Computing Systems , San Jose, USA, 
7–12 May. 
Moore, K., and March, E. (2020). “Socially Connected During COVID-19: Online Social Con-
nections Mediate the Relationship Between Loneliness and Positive Coping Strategies”. 
Preprint. www.researchgate.net/publication/342371471_Socially_Connected_during_ 
COVID-19_Online_social_connections_mediate_the_relationship_between_loneliness_ 
and_positive_coping_strategies 

 
  
   
 
  
  
 
  
  
 
  
 
 
 
   
 
 
   
  
 
Privacy, Ethics, and Trust 4 1 
Nurmikko-Fuller, T., and Pickering, P. (2022). “Crisis What Crisis?”. In Leitch, S., and Pick-
ering, P. (eds). Rethinking Social Media and Extremism . Australian National University 
Press. 
O’Hara, K., and Shadbolt, N. (2014). The Spy in the Coﬀee Machine: The End of Privacy as 
We Know It. Oneworld Publications. 
Orwell, G. (1949). Nineteen Eighty-Four. Secker & Warburg. 
Pariser, E. (2011). The Filter Bubble: How the New Personalised Web Is Changing What We 
Read and How We Think. Penguin. 
Sharon, T., and Zandbergen, D. (2017). “From Data Fetishism to Quantifying Selves: 
Self-Tracking Practices and the Other Values of Data”. New Media & Society , 19(11), 
pp. 1695–1709. 
Sun, Y ., Du, Y ., Wang, Y ., and Zhuang, L. (2017). “Examining Associations of Environmen-
tal Characteristics With Recreational Cycling Behaviour by Street-Level Strava Data”. 
International Journal of Environmental Research and Public Health, 14(6), p. 644. 
Vally, Z., and D’Souza, C. G. (2019). “Abstinence From Social Media Use, Subjective Well‐
Being, Stress, and Loneliness”. Perspectives In Psychiatric Care, 55(4), pp. 752–759. 
Wiederhold, B. K. (2020). “Using Social Media to Our Advantage: Alleviating Anxi-
ety During a Pandemic”. Cyberpsychology, Behavior, and Social Networking , 23(4), 
pp. 197–198. 
Wood, A. C., and Wheatcroft, J. M. (2020). “Young Adult Perceptions of Internet Communi-
cations and the Grooming Concept”. Sage Open, 10(1), p. 2158244020914573. 
Zuboﬀ, S. (2019). The Age of Surveillance Capitalism: The Fight for a Human Future at the 
New Frontier of Power. Proﬁle Books. 

 
 
 
 
 
 
 
 
 
   
   
  
  
   3 Closed But Not for Business 
3.1 Preamble 
Do you remember when Lars Ulrich, the drummer and founding member of the 
American heavy metal band, Metallica, testiﬁed before the U.S. Senate Committee 
on the Judiciary in relation to legal action the band was taking against an Internet-
based company? Ulrich told the members of the Committee that the band had been 
alerted to the fact that their music was being “hijacked”. Napster, he stated, had 
enabled anyone “around the world” to illegally download their entire copy-righted 
music catalogue in a digital format from the Internet for free. Napster, he con-
tinued, had “never invested a penny in Metallica’s music or had anything to do 
with its creation”. The band’s legal investigators had identiﬁed 335,435 users of 
Napster’s peer-to-peer platform who had downloaded Metallica’s music. Ulirich 
likened them to those who had “won one of those contests where you get turned 
loose in a store for ﬁve minutes and get to keep everything you can load into your 
shopping cart”. “With Napster, though”, he testiﬁed, “there’s no time limit and 
everyone’s a winner – except the artist”. Ulrich’s testimony, and Metallica’s action 
more generally, attracted a ﬂurry of attention, including the master satirists, Trey 
Parker and Matt Stone, who included it in an episode of South Park that aired in 
2003: 
Kyle : We d-didn’t think it was that big a deal. 
Detective : Not a big deal! You think downloading music for free is not a big deal?! 
Put your coats on! I’m gonna show you something! And I don’t think 
you’re gonna like it! This is the home of Lars Ulrich, the drummer for 
Metallica. Look. There’s Lars now, sitting by his pool. 
Kyle : What’s the matter with him? 
Detective : This month he was hoping to have a gold-plated shark tank bar installed 
right next to the pool, but thanks to people downloading his music for 
free, he must now wait a few months before he can aﬀord it. 
1 
The spirited rebuttal before the Committee by Napster’s CEO, Hank Barry, is 
less well known. Napster was not infringing copyright law, he told the Com-
mittee, and the hostility to his company merely reﬂected the music business’s 
DOI: 10.4324/9781003197898-3 

 
 
 
  
 
   
 
 
  
 
 
 
  
   
   
 
  
 
 
 
 
 
 
 
  
 
   
 
 
Closed But Not for Business 4 3 
failure to come to terms with new technology. Metallica had sued Napster for 
$10 million and eﬀectively won the case when it was settled out of court. By thi s 
time, Metallica had been followed into Court by other artists seeking recompense 
from Napster for breach of copyright. Napster had been launched in 1991, and 
by 2001, it was facilitating tens of millions of music transfers per month. By the 
time Metallica and others had ﬁnished pursuing it, the corporation had ﬁled for 
bankruptcy. It proved to be a pyrrhic victory. Napster was followed by a raft of 
other peer-to-peer sites, each shut down in succession, but even at the time of 
writing, Metallica’s catalogue can be found on-line and down-loaded for “free”. 
2 
Today massive corporations, most notably the Swedish subscription platform, 
Spotify, have transformed the legal consumption of music on-line into a multi-
billion dollar business and the only squabbles are among each other. And, it’s all 
just data anyway isn’t it? 
Well it is, and it isn’t. Or, at least it’s not that simple. Metallica v. Nap-
ster highlights complexity. What began as composed music was rehearsed, 
performed, recorded onto analogue tape or digitally, pressed onto vinyl and pro-
duced as CDs, commodiﬁed (sold), broadcast (again sold), ‘hijacked’ and given 
away for “free” (actually monetised again), downloaded and at various points 
in this process, it became music again. In other words, data is complex: data 
is everywhere, and everything is data. In general discourse, especially in the 
Digital Humanities, we may often cognitively shortcut to thinking about data as 
just digital data (spreadsheets are often what springs to mind), but the Humani-
ties are rich with structured, semi-structured, and even unstructured data: every 
collected dataset, every museum database, every narrative, every interpretation 
of historical facts, a melody of a composition, the subject of a painting. Data is 
ubiquitous. 
3.2 Data 
Data as a concept is something that needs to be understood and appreciated for its 
complexity and nuance. Living as we do in the Digital Age, data is often a short-
hand term for digital, quantitative data. But that’s not all the data there is. Mate-
rial collected from interviews is a prime example of qualitative data; research in 
the Humanities is (and has been for centuries) focused on the use and close study 
of unstructured data. And this is also true of the Digital Humanities, which has a 
multitude of data, both qualitative and quantitative, both digital and analogue. The 
reference model for Open Archival Information Systems (p. 10 of Section 1) 
3 de-
ﬁnes data as “interpretable representation of information” and provides examples 
such as tables with numbers, text, audio recordings, material objects, and digital 
data (at the level of bits); the National Statement on Ethical Conduct in Human Re-
search
4 categorises data (including summary data and metadata) into raw, cleaned, 
or transformed; it cites, inter alia, examples such as interviews, questionnaires/ 
surveys, personal histories and biographies, images, audio recordings and other 
audio-visual materials, observations, administrative records, and digital informa-
tion about mobile device usage as data. 

 
 
 
  
 
 
   
 
 
    
  
 
 
 
 
 
 
 
 
 
  
 
44 Closed But Not for Business 
We can add to this historical and cultural heritage data, and indeed just about any 
written materials, depictions, sounds, or any other materials that tell us something 
of the world. Primary sources especially in the Humanities can easily constitute 
materials which are not digitised and which cannot be accessed using web crawl-
ing or scraping: the analogue hypertext system reported on in Nurmikko-Fuller 
and Pickering (2021 ) is a prime example of this. The Digging into Data Challenge 
5 
has funded 50 projects focusing on myriad diﬀerent kinds of data, much of which 
is not digital. 
Data is attached to a number of adjectives: data can be Big, O pen, Linked or 
Meta. It can be machine- or user-generated, it can be real-time . Many verbs lend 
themselves happily to being the suﬃx to the data-preﬁx: engineering, govern-
ance, mining, production, consumption, storytelling, literacy, aggregation, mod-
elling, clearing, and visualisation. You can even combine it wi th nouns: fabric, 
lakes, analyst, architecture, model, warehouse, and culture. And to this we can add 
one more in the form of “divided data” (a term coined by one of my anonymous 
reviewers) – to refer to collections of information such as spr eadsheets and lists 
and databases, but ones that have not been connected to any oth er information 
sources with the use of Linked Data or any other aggregation process. These data-
sets are the ones that are likely to correspond to suboptimal research data manage-
ment plans: yes, they sit on the hard drives of speciﬁ c individuals. But how can 
these datasets be recorded, discovered, utilised? The sheer vol ume of data created 
and generated but potentially lost is bound to be staggering. Perhaps the Humani-
ties could consider a paradigm shift, where the data, as well as its interpretation, 
would be recognised as a valid research output? 
But not all data is generated as a result of robust academic endeavour. The 
most obvious context in which we can see user-led data production in over -
drive is social media. The multimedia giants that dominate the online world are, 
at the time of writing, Facebook, Instagram, and (Elon Musk’s acquisition of 
the platform notwithstanding) Twitter, but also include discussion forums and 
text-heavy platforms such as Reddit, as well as the more niche environments 
of LinkedIn, ResearchGate, and others. Each posting of content, be it a peer-
reviewed journal article, or even a TikTok video that fails to go viral, is our con-
tribution to the abundance of data available online. This is not a new problem: 
this constant production of new content has been described usin g terms such as 
“an avalanche”, and “a deluge” for a decade if not two. The choice of metaphor 
is not accidental: both terms convey the notion of the sheer overwhelming quan-
tity of material. 
The subdomains of HASS are an incredibly diverse ﬁeld with a staggering 
range of domains, methodologies, heuristics, epistemologies, and research agen-
das. HASS encompasses ﬁelds as diverse as history, music, library and information 
sciences, archaeology, social sciences, art, and anthropology, but to name but a 
simple few. It is home to a range of methodologies, from qualitative interviews 
and the collection of oral histories, to quantitative analyses of data collected from 
online posting and social media. Yet even with all this internal diversity, there is 
something that is unique that combines the subdisciplines of HASS. But what is 

 
 
 
   
 
 
 
 
 
 
 
 
  
 
  
 
 
   
    
    
 
   
   
    
Closed But Not for Business 4 5 
this unifying feature? Certainly, it is the focus on human endeavour, and on how 
humans have experienced, interpreted, and interacted with the world around them. 
It may not be a truth universally acknowledged, but the Humanities has data. 
Without a doubt. It’s there, everywhere. But what makes it tricky is that most Hu-
manities data simultaneously has one or more of four deﬁning characteristics: it is 
ambiguous, messy, incomplete, and unstructured. The ﬁfth element is one of (un) 
reproducibility. 
3.2.1 Unreproducible Data 
Humanities data is in many ways unreproducible. The statement might initially 
sound absurd, but on closer inspection can be shown to ring true. The secret is in 
the explicit articulation and deﬁnition of what we mean when we say “Humanities 
data”. 
As a premise, let’s agree that Humanities data can be one of two things (or in-
deed both). It can be the primary source (an original manuscript, or a painting, say), 
or it can be the result of a process of analysis, a secondary source that amalgamates 
a number of primary sources and uses them as evidence to support a conclusion. In 
some ways, we could understand these two datasets as being part of one biography 
of an information object: the primary sources are a necessary part of the life span 
of the thing of which the secondary sources are a ﬁnal or subsequent result. Perhaps 
we can equate this idea to the life of a butterﬂy: the primary sources are the cater -
pillar, the secondary sources are the butterﬂy. The pupa is a black box, a process 
during which transformation occurs. 
But how does this explain the (un)reproducibility of Humanities data? Undoubt-
edly, the secondary sources are at least to some extent reproducible. We present the 
information (all the things we know about our caterpillars!) and use it to justify the 
ultimate butterﬂy. Others observing our caterpillars and the metadata of our cater-
pillars will more or less be able to, if not agree with the ﬁnal butterﬂy, then at least 
see why this is the butterﬂy we produced. 
But what all Humanities primary data has in common is a degree of undeﬁ n-
ability. The primary source cannot be reproduced, because the primary, original 
datasource (the manuscript, the musical score, the painting) is a manifestation of an 
abstract notion that can only exist in the mind of the creator. We can thus never start 
from the start. This notion has been explicitly captured in the CIDOC CRM 
6 and 
FRBRoo7 ontologies (discussed in greater details in Chapter 4 ) that capture cultural 
heritage data (museums and libraries respectively). The latter for example explic-
itly diﬀerentiates between E28 Conceptual Object(which “comprises non-
material products of our minds . . . [that] cannot be destroyed. They exist as long 
as they can be found on at least one carrier or in at least one human memory. Their 
existence ends when the last carrier and the last memory are lost”), 
8 and E73 In-
formation Object(which “comprises [of] identiﬁable immaterial items, such 
as poems, jokes, data sets, images, texts, multimedia objects, procedural prescrip-
tions, computer program code, algorithm or mathematical formulae, that have an 
objectively recognizable structure and are documented as single units”), 
9 and E33 

 
  
  
 
 
 
 
 
  
 
   
 
   
   
  
 
   
  
46 Closed But Not for Business 
Linguistic Object (“[including] written texts, recorded speech or sign lan-
guage”),10 although the ontological structure representing an idea, the conception 
and expression of that idea, the documents carrying the information of the idea, and 
the content of the inscription in which the idea is formulated is far more complex 
in the CIDOC CRM than these three Classesalone. 
Perhaps then it is simply impossible to start at the very start of the biography of 
Humanities data. We do not possess the means of recreating the cognitive processes 
that existed in the past, or ephemeral performances that disappeared as soon as they 
were no longer being observed and experienced. Undoubtedly, for the Humanities 
researcher, what can only ever exist by its very deﬁnition is a manifestation of a 
cognitive process (itself powered by innumerable tacit and intangible aspects of the 
lived experience, feelings, idiosyncratic aims and intentions of the creator) – and 
itself is already the result of an act of interpretation, a product of an act of transla-
tion of an intangible, nebulous, and abstract concept into a thing that enables the 
communication of that idea to someone else. What we can analyse is the record that 
captures the process, the event, the moment, but we never have the equivalent of 
what might constitute “raw” data. 
3.2.2 Unstructured Data 
Data is everywhere, and everything. As  Greenﬁeld (2017 : 211) puts it: 
Most of the world’s data . . . does not happen to reside in the neat tablet or 
crispy cellular structure of any database. . . So the new ways of handling such 
situations is to look for emergent patterns in previously unstructured data, 
like a large body of text, a series of images, or indeed a real-time video feed. 
But how easy is it for us to forget that  all this content equates to all this data? 
Schöch (2013 ) somewhat anecdotally noted that the vernacular of scholars in 
the Humanities has not traditionally described the analysis as focusing on “data”. 
The material is described more in terms of the objects that con stitute the primary 
source(s) – newspapers, books, plays, musical compositions, paintings, and so on. 
Neither these objects nor the historical context that provides much of the metadata 
about them (who made them, who owned them, what do they capture , how are 
they to be understood, what role did they play in contemporary society, etc.) are 
necessarily or frequently represented in structured formats such as tabular data 
held in a spreadsheet. Yet, there is still much information her e, a lot of data for 
analysis. 
Details of the object biography can be, and are, collected and stored exactly in 
such a way by memory institutions (museums, archives, libraries), but for many 
Humanities and Digital Humanities scholars and researchers, pulling out signiﬁ  -
cant details from unstructured data (say, for example, people or places embedded 
in the narrative of a piece of writing) to create datasets forms a signiﬁcant if some-
what thankless part of the workﬂow. Table 3.1 illustrates how the unstructured text 
of a piece of ﬁctional narrative could be turned into structured, tabular data. 

  
    
 
  
 
 
 
 
  
    
 
 
 
 
  
  
 
 
 
Closed But Not for Business 4 7
  Table 3.1 From unstructured narrative to tabular: a location-based example  
  Unstructured data    Location data  
“The Park Lane Hospital for the Dying was a 
sixty-story tower of primrose tiles. As the 
Savage stepped out of his taxicopter a convoy 
of gaily-coloured aerial hearses rose whirling 
from the roof and darted away across the Park, 
westwards, bound for the Slough Crematorium” 
( Huxley, 1932 : 163). 
Park Lane 
Park Lane Hospital for the Dying 
the Park 
Slough Crematorium 
Whilst named entity recognition and disambiguation remain some of the chal-
lenges of natural language processing, their importance as tools for working with 
descriptive and unstructured data cannot be questioned ( van Hooland and Ver -
borgh, 2014 : 168–169). But in some aspects, pulling the tangible, structured data 
out of text is itself an act of data management, curation, and thus, ultimately, of 
interpretation. 
In many ways, the example in Table 3.1 is less indicative of purely unstruc-
tured data, which might be better characterised with an example of the plot of a 
novel. A commonly occurring subset of data, particularly in the GLAM sector, is 
one of semi-structured data, typically exempliﬁed by those unstructured sections 
within metadata records. Anyone with familiarity with a collections management 
system will know of an equivalent of an information category referred to as “notes” 
or “misc.” or “miscellaneous”. Zeng (2019 ) provides examples of structured data 
(catalogues, archival ﬁnding aids, indexing and abstracting databases, curated re-
search datasets, etc.), semi-structured data (e.g. unstructured sections within oth-
erwise structured datasets or within metadata; TEI ﬁles’ content outside of the 
Header section), and unstructured data (documents, cultural artefacts, etc., which 
can be either digitised or analogue; covering all kinds of media and formats), which 
illustrate this point perfectly. 
3.2.3 Ambiguous Data 
Case study examples of ambiguity in Humanities data are not diﬃcult to ﬁnd. The 
historical use of patronyms and the tradition of apprenticeships within families 
makes the following scenario familiar to most prosopographers. Imagine a set of 
census data. In the list, there is an address for the people who live there, and their 
prospective employment status. How then could we diﬀerentiate, for example, a 
father and a son, who live in the same address, and who work in the family busi-
ness? A dataset recorded as a snapshot in time would not necessarily include any 
additional information, and disambiguation is only possible through the addition of 
information from external sources. 
There are other sorts of ambiguities in data. These could be problems of disam-
biguation as above, or problems with data alignment arising from issues such as the 

 
 
 
  
 
 
  
 
 
 
 
  
  
 
 
48 Closed But Not for Business 
omission of part of a word. Let’s consider the case of two names: Jane Smith and 
Jane A. Smith. A character recognition process might fail to identify them as refer-
ring to the same entity, because the letters in the strictest sense do not adhere to the 
same identical pattern. To human cognition, especially where aided by additional 
knowledge about the person (e.g. that the person’s middle name is Agnes), there’s 
little ambiguity here, merely more information in one context than the other. Such 
discrepancies in the data can cause challenges for data scientists or anyone wishing 
to aggregate data from these two contexts. Without foreshadowing the remainder 
of the book too much, this is exactly the sort of problem that Linked Data could 
help us solve. 
3.2.4 Incomplete Data 
Humanities data is incomplete. This axiom of information compl eteness becomes 
ever clearer and more truthful the further back in time we move. The evidence we 
have from the ancient world, for example, is eloquently deﬁned by Cunningham 
(2013 : 99) as being “highly erratic . . . partially due to accidents of modern recov-
ery and partially to accidents of ancient survival”. These twin considerations of 
Preservation and Discovery reﬂect the truth that not all instances of all creative 
and intellectual human endeavour have survived, nor has all that has survived 
been rediscovered to date. It would be one thing to say that Hu manities data is 
incomplete, and that interdisciplinary researchers and domain e xperts in various 
ﬁelds within HASS must accept their fate as working with datasets which Tay-
lor (2013 : 290) so poetically equates to the night sky, with i nformation dotted 
throughout the vastness of the unknown as “scattered specks of light against an 
overwhelming sea of darkness, punctuated by a few spots of inte nse brightness”. 
The truth alas is a degree more complex, for new information in the form of 
long-lost or recently discovered primary sources emerge through scholarship in 
archives, museums, and collections of all kinds. To extend Taylor’s metaphor, our 
knowledge of history may well be like the night sky, but we are  forever discover-
ing new stars in an inﬁnitely expanding universe, and have only begun to explore 
the role of the dark matter and dark energy that ﬁ lls what we thought was the 
empty space in between them. 
A consideration which will undoubtedly seem obvious to some, and shocking 
to others is simply this: put, there is no incentive, desire, or reason for Humanities 
scholars to remove the complexity nor ambiguity from their data – no aim to ﬁll in 
the gaps or tidy up the datasets. Consider for example a scenario of a historical doc-
ument. The ﬁrst page of the document describes some of its metadata, namely the 
publication date, with the following words: “The yere of our lorde a. M.CCCCC. 
and .ix.”. This might present a challenge for someone tasked with entering this in-
formation to a collections database. First, because it is not just a string of letters but 
indeed a cluster of words for a piece of data for which one might rightly expect a 
number; second, because it is not fully written in according to the rules of contem-
porary English, but instead represented with Roman numerals (thus requiring some 
domain knowledge); and thirdly, it might not have the granularity necessitated by 

 
 
 
  
 
 
  
  
 
 
  
  
 
 
  
    
 
    
    
   
   
  
  
 
  
 
 
    
 
  
Closed But Not for Business 4 9 
the database schema, which might adhere to the DD-MM-YYYY format. What 
should the person responsible for the data entry do? 
For a historian, the answer is to do nothing at all. The absence of a data unit 
would itself be informative about the document, and the insertion of false data 
(inaccurate date) would be an unfathomable abomination. The absence of data is 
by far a lesser crime than the introduction of false positives. But what of databases 
that force the user to enter a date? For any data and computer scientist, the answer 
is likely to be January 1st. But why? One is undoubtedly from familiarity, and 
perhaps a belief that the date is innocuous: 1st January 1753 (1753–01–01) is the 
minimum date value for the Datetime ﬁeld in SQL Servers, for example, and the 
Unix Epoch (the starting point for counting time as seconds) is similarly on 1st 
January, albeit in 1970. Even Oracle databases have a date range that starts on 
1st January 4712 BCE (and ﬁnishes on 31st December 9999). A technical norm 
or custom of the ﬁeld as it may be, the use of 1st January as a placeholder date is 
deeply problematic especially when working with Humanities data, where such a 
detail could strongly skew the analysis and interpretation of the data. Bishop (2018 : 
125) worried that “theoretical problems are steamrolled ﬂat by the weight of the 
data” – how much more concerning then, if that data is not representative of the 
historical period it claims to capture, but an arbitrary modern convention? 
3.2.5 Messy Data 
There are two kinds of messy data. The ﬁrst, as understood by computer and data 
scientists, is information that is captured as structured, tabular data, but it is rid-
dled with ambiguity, omission, and does not adhere to a standard. In other words, 
exactly the sort of data that Humanities scholars will work with when compiling 
their datasets and databases from historical sources. 
Another challenge presented by historical data is the challenges it presents 
to optical character recognition (OCR) software in a much more literal take on 
“messy”. An example of a very simple tabular dataset that combines both types 
of messy data is from the project Lord Mayor’ s Costume Balls in Sydney in 1857 
and 1879 .
11 This prototype project focuses on very structured data: a list of the 
guests who attended an annual costume ball organised by the Lord Mayor, and 
their costumes, as published by the Sydney Morning Herald. A digitised version 
of the primary source
12 is available from Trove, 13 the National Library of Aus-
tralia’s digital archive. 14 Alongside the portable document format (PDF) of the 
historical newspaper is the OCR. Table 3.2 illustrates the potential for messiness 
in even the simplest and most structured of datasets, showing a number of false 
positives. Note that the messiness remains although at the time of writing, six 
anonymous volunteers had already contributed to the tidying up of the OCR for 
this speciﬁc page. 
Academics will invariably discuss the challenges of the messiness of this par -
ticular data presents to the process of mapping it ontologically (a word used here 
speciﬁcally in the sense of the Linked Data paradigm and knowledge represen-
tation, and not in the sense of a branch of philosophy) and the exploration of 

 
 
  
  
 
 
   
   
  
 
 
 
 
 
  
  
 
 
 
 
   
  
     
 
  
  
  
  
  
  
50 Closed But Not for Business
  Table 3.2 Challenges to OCR in the Lord Mayor’ s Costume Balls in Sydney in 1857 and 
1879 project data 
OCR from digitised historical document Text as it appears to human users 
in the digitised historical document 
  (blurred but legible)  
Lewis” Mr. S. H., Italian brigand s h> s ^’f; -Í Lewis, Mr. S. H., Italian brigand 
Levey, Mrs. Philip *’-.*”’” ¿’* Levey, Mrs. Phillip 
Levein, Mrs. J., Norma ‘ * * +<’”r↓’: Levein, Mrs. J., Norma 
Lawson, Miss, Air * ‘’,*, iJ J/”,”,. Lawson, Miss, Air 
Lawson, Miss, Night, ‘ “ ‘L. ‘ “ < Lawson, Miss, Night 
LeGuirè.Mr.- \\T^Z>* Le Guirè, Mr. – - 
that information in a Linked Data system ( Nurmikko-Fuller and Pickering, 2021 ; 
Gatti, T. et al., 2022 ). Even with a preliminary investigatio n having successfully 
been completed, what remains unclear are issues such as whether the omission 
of the costume is, itself, a piece of information. The process of recording the 
names and costumes was possibly one of the announcements, whereby as a guest 
would arrive, a local government oﬃcial clerk might (or might not) record their 
name and their costume, and then announce them (or might not). Are there omis-
sions? Or if so, were they simple mistakes or omissions by the frantically scrib-
ing journalists or government oﬃcials? Or did the guest perhaps arrive without 
a costume? And so on. In the absence of additional datasets and pictographic 
evidence, there is little we can do to address that particular ambiguity, caused 
by the absence of information. The only solution would be to add to our existing 
dataset with external information. 
3.4 Openness 
Openness, accessibility, transparency. All three have something in common but re-
fer to diﬀerent aspects and outcomes to the way research, data, and code are shared 
online. Diﬀerent types of stakeholders are likely to have very diﬀerent takes on the 
issue. A politician may welcome the opportunity to share data to show transpar -
ency; a researcher may wish to share their data as part of proving the reproduc-
ibility of their ﬁndings, or disseminate their publications freely to improve their 
engagement with the academic community, and to support scholars hip. Although 
there are many beneﬁts to freely sharing research (referred to as Open Access), in-
formation (Open Data), and code (Open Source), there are also some complicating 
factors. Not all data can be open (e.g. cultural, societal, privacy-related reasons); 
Open Access requires a revolutionary paradigm shift for the publication industry; 
Open Source can be abused and misused, and so on. Conﬂict arises when seem-
ingly altruistic opportunities for information and knowledge sharing collide with 
neoliberal and capitalist complexities which nevertheless are an undeniable part of 
modern societies. 

 
 
  
 
 
    
 
 
 
 
  
 
  
 
  
  
   
  
  
 
 
  
Closed But Not for Business 5 1 
3.4.1 Open Source 
In the simplest of terms, “Open Source software” is a term that applies to computer 
programmes and coding that have been published under free and open licences. 
This means that the code is (at least to some degree and within the limits of certain 
conditions) accessible without cost, but also that anyone wanting to use the code 
can make changes to it. What those limits and conditions are depends on the licens-
ing that the creator of the code has used. Many programmers publish their data on 
platforms such as GitHub, which in May 2022 had over 83 million developers. 
The axiom of the Open Source community is that software might be “free as speech, 
not free as in beer” – an expression attributed to Richard Stallman ( Lessig, 2006 ). The 
idea behind the slogan is that anyone should be able to access and edit the code (opti-
mistically, the idea is that the code could be improved), as long as those who are edit-
ing it similarly share their resulting code openly and for reuse. For example, Creative 
Commons (CC) licences 
15 cover a myriad of diﬀerent types and levels of permissions 
for intellectual property such as software in the context of copyright laws. Many of 
these stipulate that the degree of freedom (libre) assigned to the original source code be 
also applied to any and all derivatives, perpetuating the Open model and encouraging 
the reuse and further development of existing code, software, and programmes. The 
application of licences is essential, because (and there are country-speciﬁc exceptions 
to this) copyright (and its restrictions) are applied automatically. Only by opting to use 
a speciﬁc Open licence can a programmer ensure their code is truly ‘free’. 
But even within the software development community, seemingly a chasm ex-
ists between so-called free software and Open Source. Although in some ways 
fundamentally similar in their drive for accessible software that can be edited and 
changed by developer (libre), the Free Software Foundation is keen to establish 
that theirs is one of a philosophical, moral, and intellectual approach: 
The free software movement campaigns for freedom for the users of com-
puting; it is a movement for freedom and justice. . . When we call software 
“free”, we mean that it respects the users’ essential freedoms: the freedom 
to run it, to study and change it, and to redistribute copies with or without 
changes. This is a matter of freedom, not price, so think of “free speech”, 
not “free beer”. . . By contrast, the open source idea values mainly practical 
advantage and does not campaign for principles.
16 
The diﬀerence between these values and the rest of the Open Source com-
munity are not easy to establish. What can be said is that the core values of Open-
Source.com (what they refer to as the “Open Source Way”) are predominantly 
practical and pragmatic ones: transparency, collaboration, releasing early and of-
ten, inclusive meritocracy, and community. 
17 
From a business model perspective, the freeware movement is the most relevant 
here. Unlike Open Source code or free software, freeware refers to proprietary 
software. Examples of the latter are well-known names such as Microsoft Oﬃce, 
or Adobe Creative Cloud – these are software that are the opposite of Open Source, 

 
 
 
 
 
  
        
   
 
  
 
 
  
  
 
 
   
 
 
  
 
 
  
52 Closed But Not for Business 
as the creators of the code have applied such exclusively rigid and restrictive rules 
and licences that users may not and cannot edit the underlying code. These types of 
software are often also called non-free or closed-source. 
The requirement for 3 stars in the Five Star Standard for Linked Open Data 
stipulates the use of non-proprietary data formats. Why then should we consider 
proprietary software now? The reason for this is that proprietary software has a spe-
ciﬁc type of Open business model that is applied to it, namely freemium. The core 
concept here is that, whilst the software is certainly not libre, a simple version (with 
limited functionality) is gratis. That is to say, there is no monetary cost involved in 
the acquisition of the software in the ﬁrst instance, but in order to access the full 
functionality, or to be entitled to technical support should anything go wrong, the 
user must pay a fee or enter into a subscription model. Example of the very popular 
freemium business model include very diverse platforms such as Sketchfab.com, 
18 
LinkedIn,19 and Spotify 20 as well as games such as PokemonGo!, 21 Minecraft,22 and 
the Steam platform, 23 which oﬀer some free gameplay, but also enable the purchas-
ing of digital artefacts and objects in exchange for real-world money. 
3.4.2 Open Access 
Where Open Source applies to the software being used for the analysis, Open Ac-
cess is related to the (academic) research output in terms of peer-reviewed research 
publications, reports, and papers. Open Access terminologies categorise accessibil-
ity on a predominantly two-pronged approach: green, or gold. 
24 Gold Open Access 
is not gratis for the author, but it does mean that the publication in its ﬁnal peer-
reviewed and copy-edited form is accessible to the research community and the 
public free of charge (that is to say, it is not behind a paywall, or only accessible to 
those with a subscription). The drawback or limitation of this approach is that the 
cost of Gold standard Open Access is often prohibitively high for scholars looking 
to publish the work they have completed outside of a funded project that has an 
allocation in the budget for this speciﬁc purpose. As an illustrative example, at the 
time of writing, examples of Gold Open Access rates for one major publisher were 
between US$500 and US$5,000 per publication.
25 
Green Open Access, which is also referred to as self-archiving, allows the author to 
make a (often, but not exclusively pre-print) version of the text available through their 
personal website, institutional repository, or other similar platform. Copyright restric-
tions may result in embargo periods or other delays, but ultimately the document is 
openly accessible. The rules and regulations of speciﬁc publishers can also aﬀect which 
version (e.g. prior to copyediting) of the publication can be made accessible in this way. 
In recent years, many research funding bodies such as the Australian Research 
Council (ARC) and the Arts and Humanities Research Council and the Engineer -
ing and Physical Sciences Research Council in the UK have mandated Open 
Source publication of funded projects. This trend is also being reﬂected by Google 
Scholar. The function is relatively new at the time of writing: speciﬁc matrices are 
embedded into author proﬁles, showing which papers are required to be openly ac-
cessible, and which Research Council’s requirements must be met in that regard. 
26 

   
 
  
  
  
  
 
 
 
  
 
  
 
 
 
  
 
   
 
 
 
 
 
  
 
 
  
Closed But Not for Business 5 3 
3.4.3 Open Data 
Open Data refers to information that has been published online in a way that is 
accessible to others. It too, like Open Source software, should be published with 
an Open licence. Open Data meets the criteria of the FAIR data principles (dis-
cussed further later), and meets four of the Five Star Standard of Linked Open 
Data (as seen in Chapter 1 ). In addition to appropriate licensing, datasets should 
be published online using non-proprietary software. A common example of this 
is that a tabular dataset (a spreadsheet) made available as a CSV ﬁle is best; shar-
ing it as an MS Excel document is OK, but not ideal; uploading a PDF of that 
spreadsheet is never the right thing to do, but even that is better than not sharing 
the data at all! 
The ﬁrst mention of the axiom of “information wants to be free”, which is taken 
as the premise to many a conversation about Open Data, dates to the early 1980s. 
Now forming part of the vernacular of most practitioners, its origin is attributed 
to Stewart Brand. So iconic is this anthropomorphic metaphor, that it has its own 
Wikipedia page. 
27 
The problem here is that the phrase is ambiguous in its exact meaning. The hom-
ophone “free” has several meanings, each of which could equally apply for data, 
and carry strong socio-economic ramiﬁcations. “Free” could be “without cost” 
(gratis), or it could be “without imprisonment or restriction” ( libre). Open Data 
advocates and Web-utopianist data scientists may tout the former, but the transcript 
of the event in which the phrase was recorded tells a diﬀerent story: the full quote 
illustrates that the original focus was on the monetary value of information: 
In fall 1984, at the ﬁrst Hackers’ Conference, [Stewart Brand] said in one 
discussion session: “On the one hand information wants to be expensive, 
because it’ s so valuable. The right information in the right place just changes 
your life. On the other hand, information wants to be free, because the cost of 
getting it out is getting lower and lower all the time . So you have these two 
ﬁghting against each other.” (That was printed in a report/transcript from the 
conference in the May 1985 *Whole Earth Review*, p. 49.)
28 
This attitude of data being valuable comes as no surprise to a ny of us living in 
the Information Age, and as part of the Data Economy. Yet, the underlying push 
for Open Data is driven by the idea that data should be accessi ble by everyone 
(without monetary cost) and that once in possession of said dat a, researchers and 
developers should be able to use, reuse, and republish that data similarly without 
restrictions. 
Whilst this may not be an attractive proposition for the personal data of living 
peoples (as discussed later), there is an increasing push by funding bodies across 
the globe to make research data as open as possible. 
Alas, in some cases, there seems to be a lack of clarity as to what the Open pol-
icy applies to. The ARC policy, for example, stipulates that “Any Research Outputs 
arising from an ARC supported research Project must be made openly accessible 

 
    
 
 
 
   
 
 
 
 
   
 
 
  
 
  
  
 
 
 
54 Closed But Not for Business 
within a twelve (12) month period from the date of publication”, but also states that 
“Research Outputs do not include research data and research data outputs”.29 This 
is a challenging contradiction for disciplines such as Digital Humanities in general 
and Linked Data practitioners in particular, for whom the building, development, 
structuring, and publication of the research dataset itself constitutes a signiﬁcant 
part of the research workﬂ ow. 
In opting to publish information openly and in an accessible manner (as FAIR 
data, as Open Data), data producers and owners make a deliberate policy deci-
sion. The reasons behind this are often centred around transparency, such as with 
government data as the sites data.gov., data.gov.uk, and data.gov.au all illustrate. 
These datasets have been used across the globe for myriad purposes, ranging from 
social beneﬁt by highlighting cyclists’ safety in London, UK ( Collins and Graham, 
2019 ); to planning a city in India (Bick et al., 2018); modelling urban infrastructure 
in Russia ( Lantseva and Ivanov, 2016 ); reconstruction of cultural heritage sites in 
Cyprus (Themistocleous, 2017); assessing the risk of waterlogging in China (Lin 
et al., 2018); and mapping slums in Kenya ( Mahabir et al., 2020 ). 
3.4.4 Linked Open Data 
Linked Data, Linked Open Data, and the Semantic Web represent a cluster of terms 
that almost refer to the exact same thing, and are thus used synonymously. The key 
word here though is “almost”. A closer examination and a more t horough decon-
struction of the terms highlights fundamental diﬀerences between them, in ways 
that cover technological and philosophical diﬀerences. A top-level or broad deﬁni-
tion of these terms is given below, followed by a more detailed discussion, which 
more precisely dwells into the nitty-gritty of these diﬀerent terms. 
As the nomenclature would suggest, Linked Data and Linked Open Data are 
very closely aligned. Both refer to a process, a method, a way of publishing infor-
mation online by utilising existing Web architecture and technologies. The term 
“Open” carries with it institutional and legal ramiﬁcations, signifying that the data 
that has been incorporated into this project is free (as in gratis) and be accessed 
without monetary cost to the data consumer (e.g. not hidden behind a paywall), but 
also free (as in libre) to be downloaded and even edited by the user. Data can be 
Linked without being Open (as discussed later in the chapter). Much of the data 
currently available online is Open, but not Linked (since has not been published 
according to the Linked Data Five Star Standard – see Section 1.5). 
On the Semantic Web, this level of granularity of interconnected resources falls 
short of the aim – here it is the meaning, the value, the content of that resource is 
captured and presented in a format that makes it meaningful to both humans and 
software agents alike. In this sense, the Semantic Web is a thing, a collection of 
things, a manifestation of technological implementation. It is a thing inasmuch as 
the Web is a thing – in some ways quantiﬁable, in other ways nebulous, intangible, 
and perhaps a little incomprehensible as well. 
If the Semantic Web is a thing, then Linked Data and Linked Open Data are 
methods. They are a process, or collection of agreed-upon processes, that enables 

 
 
  
   
 
  
  
 
 
 
 
  
 
  
 
   
 
 
 
 
 
 
     
  
   
    
 
  
 
  
  
Closed But Not for Business 5 5 
the current manifestation of the Semantic Web. They do not represent the ﬁrst or 
only attempts that have been made to make the Semantic Web manifest, for earlier 
in the history of the former, the AI community made what ultimately turned out 
to be unsuccessful attempts to develop just that. Knowledge representation (KR), 
one of the cornerstones of the Semantic Web, has been discussed for near-on four 
decades (Levesque, 1984) within the ﬁeld of AI, which, in turn, has been a ﬁeld of 
active research since at least the 1950s. Berners-Lee has discussed Web-facilitated 
machine interaction for almost three decades (since 1996), and his initial vision 
for a hypertext system already enabled connections which went beyond simply 
linking human-readable documents: that is to say, even the earliest imaginations of 
the Web in the mind of its creator where ones of capturing semantics, and machine-
readability has been a desired or intended feature of the system from the beginning 
( Berners-Lee, 1999 ). Even the interested general public was introduced to the term 
more than two decades ago in an article in The Scientiﬁ c American ( Berners-Lee 
et al., 2001 ), although there may still be some distance to be covered before we can 
conﬁdently assert that the Semantic Web has gone fully mainstream. 
The purpose of publishing information online is that it presents us with an 
opportunity to capitalise on the value of the data that we have, and to generate 
further data (as researchers, scholars, academics, curators, etc.). As Linked Data 
practitioners, we can do this by capturing the information embedded into our 
datasets; by publishing that information, so that others may encounter it, and 
beneﬁt from it; by using it as a part of a knowledge graph, which, in turn, enables 
us to leverage computationally powerful operations such as inferring implicit 
knowledge from explicitly declared fact, and to enrich existing datasets with 
information accessible from elsewhere; and by harvesting the beneﬁts – both inten-
tional and unintentional – of using this data, of linking it, and of allowing others 
to reuse it and build on it. It enables software agents to navigate the data, and to 
infer connections within it. 
This connecting of datasets is not ground-breaking per se. After all, clicking on 
a link of one page and being taken to another is the most basic of human interac-
tions on the Web. Where Linked Open Data diﬀers from that is that rather than 
being limited to content and hypermedia structures that are navigable by human 
users, relevant information can be (potentially) identiﬁed and connected to any-
where online, and that information, once found, can be incorporated into a process 
of automated inference. Whether or not this hypothetical ambition has quite been 
reached yet is another matter entirely. 
The Five Star Standard is used to refer to Linked Open Data, but the ﬁrst 
three stages refer exclusively to standards that should be adhered to with Open 
Data. Data can be Open (especially when published according to the FAIR data 
management principles 
30 of having been made publicly available for ﬁndability, 
access, interoperability, and reuse), without being Linked. It could also be Linked 
without being Open. Only the four- and ﬁve-star levels, which refer to the use 
of W3C standards of RDF (Reference Description Framework) and SPARQL 
(SPARQL Protocol and RDF Query Language) respectively can be shown to 
refer to Linked Data speciﬁcally. In summary, if you publish your data online 

 
 
 
 
 
 
 
 
 
   
 
  
  
 
    
   
 
 
 
56
 Closed But Not for Business 
as RDF, and link to other people’s data, you will have reached Five Star Linked 
Open Data. 
3.5 Be FAIR, and CARE 
How do we regain agency? How do we recover Data Sovereignty? The option 
of curtailing data collection is fanciful, and if history tells us anything, it is that 
legislation and regulation are invariably ineﬀective. What begins with hot air ends 
as waste paper. What is needed are clusters of multifaceted solutions, which ad-
dress both the technical and human considerations. Educating pr ogrammers and 
software engineers to the subtleties of ethics and providing op portunities to learn 
from past mistakes is but one aspect; diversifying datasets to remove biases (both 
historical and modern) is another. Ensuring ethical considerations form an integral 
part of software development, especially with artiﬁcial intelligence, deep learn-
ing, and machine inference, should take priority in the workﬂow, rather than be 
a simple add-on. Alerting users at all levels to be aware of co vert data collection, 
fake news and targeted political marketing, is insuﬃcient on its own; a signiﬁ cant 
improvement in digital literacy across the population is needed before any real 
change can be seen. What is necessary then are root and branch changes to the 
way we interface with the digital world. 
To this eﬀect, we should consider the FAIR and CARE data principles. FAIR 
data is Findable, Accessible, Interoperable, and Reusable. 
31 In this regard, it is a 
perfect match to Five Star Linked Data: to meet the criteria of Five Stars, data 
needs to be published online in such a way that it can be interacted with (down-
loaded, edited, connected to, in other words, reused), which, in turn, necessitates 
that it is discoverable and openly accessible. The issues of privacy, ethics, and trust 
are, however, not explicitly addressed in either the Five Star Linked Data Standard 
nor the FAIR data principles. 
CARE data principles 
32 were developed speciﬁcally in the context of Indig-
enous data, and of data sovereignty. CARE explicitly articulates the need for Col-
lective Beneﬁt, Authority to Control, Responsibility, and Ethics. 
33 These principles 
were developed in response to FAIR, and in recognition of the fact that Indigenous 
Peoples are often not part of the decision-making process. The CARE documenta-
tion unambiguously states that “the current movement toward open data and open 
science does not fully engage with Indigenous Peoples’ rights and interests”, and 
furthermore, that whilst FAIR facilitates data sharing, it does so often among enti-
ties who are part of a recognised social, economic, and political elite. In doing so, 
these principles (risk) ignoring existing power dynamics, and do little to address 
the danger of perpetuating intellectual colonialism and a Western-only canon for 
information collection and representation. 
3.6 To Be or Not to Be Open? 
The cultural heritage sector is one where the business models of various insti-
tutions have opted for non-Open policies. GLAM are known to cha rge fees for 

  
 
 
 
 
  
 
 
  
 
  
 
  
 
 
  
  
  
  
  
 
 
Closed But Not for Business 5 7 
researchers and academics for the rights to access and use digi tal images of the 
objects in their collections. The British Museum is an example of a complex and 
almost entirely case-by-case approach to the issue: a student can use an image (at 
either 72 dpi, which is not a high enough quality for a printout, or 300 dpi) in their 
doctoral thesis free of cost, but should that thesis be selecte d for publication, the 
author must apply for a new permission and pay the associated cost. 
34 The question 
then arises as to what exactly is the cost covering? This is an example of a speciﬁ c 
business model that seeks to monetise data access at the cost ( pun intended!) of 
Open Access. 
Another example of institutional policy with a deliberate aim of keeping infor -
mation inaccessible by the public and the research community is from the GLAM 
sector in Australia. The story is detailed in Bongiorno (2021 ), but I will summarise 
its main points by way of providing context: The National Archives of Australia 
have two copies of the so-called Palace Letters, a collection of correspondence be-
tween the Governor-General John Kerr and Sir Martin Charteris (Queen Elizabeth 
II’s private secretary) regarding the lead-up to the dismissal of Whitlam’s Labor 
government in 1975 (one of great controversies of recent Australian political his-
tory).
35 The second copy was made by David Smith to acquiesce to Kerr’s request: 
these were deposited by Kerr’s family in the National Archives, with an instrument 
of deposit that the correspondence be made available to the public in 2005. 
When the date rolled around, rather than release the material to the public, the 
National Archives determined that their copies constituted a “personal” collection, 
and as such were not subject to the Archives Act. 
36 When taken to court over the 
issue by Professor Jenny Hocking, so determined were the Archives to keep this 
material from the public, that they secretly renegotiated a new instrument of de-
posit with Kerr’s stepdaughter. This locks the material away until at least 2027, and 
even then it will only accessible to those able to successfully navigate a mine-ﬁeld 
of international bureaucracy. But why would an institution such as the National 
Archives, a self-proclaimed “pro-disclosure organisation”, 
37 go to court just to pre-
vent Commonwealth records from being accessible by researchers? 
The Open Source, Open Data, and Open Access communities have all been 
promoting the notion of openly available information. The idea is not a new one, 
and has circulated amongst the tech-utopianists for decades. Al though the foci of 
these communities of practice, data standards, and policies are diﬀerent, they share 
terminology and ideology. For the Linked Open Data community, the openness of 
data is in many ways and in many cases a necessary starting point, as is the sharing 
of new datasets (e.g. RDF datasets) for further linking and interaction by others. 
There are also a number of popular Open Source software, which are used and 
recommended (such as Protege) 
38 by ontology developers and implementers across 
all disciplinary boundaries. 
Not all data should be Open. Culturally sensitive data is one example. As discussed 
in Chapter 2 , with data publication come privacy concerns. There are aspects to our 
medical, personal, and ﬁnancial information that we might not want to be public 
knowledge – and who would want their insurance company getting their hands on a 
complete medical history, frequency of ordered pizza deliveries, alongside perhaps 

 
 
  
 
  
 
 
 
 
 
 
 
  
 
 
  
   
 
 
   
  
 
    
 
 
 
  
 
58
 Closed But Not for Business 
one’s tax records, posts detailing one’s social life (including, say habits relating to 
drinking or smoking), and a comprehensive breakdown of our ﬁnances? Why should 
the state be privy to a complete picture of our social interactions, consumer habits, 
opinions, preferences? Would we want someone else (anyone else!) to be able to ac-
cess all the information about us in one comprehensive picture? Where is privacy, if 
all about us can be known? The case for the preservation of privacy of the individual 
is relatively easy to make, but what are the considerations when we examine research 
data? Information that has been generated through the consistent work of academics, 
for example, and paid for by research council funding, and thus ultimately by the tax-
payer. Should we all not be in a position to beneﬁt from access to that data, that infor-
mation, and that knowledge? As mentioned earlier, there may well be social, cultural, 
and ethical reasons why not all data should always be immediately completely Open. 
But what about when political and ﬁnancial motivation become the driving force 
behind the decision as to whether or not material is made accessible? 
3.7 Solutions Combining Accessible and Inaccessible Data 
PARADISEC (Paciﬁc and Regional Archive for Digital Sources in Endangered 
Cultures)
39 is a digital archive, which (at the time of writing) contains 14,000 
hours of audio, 2,000 hours of video, and representing 1,281 la nguages. It has 
been purposely designed to adhere to international archiving st andards, and its 
goal is to provide access to the material within the archive to members of in-
terested communities. The default for the metadata in PARADISEC is the CC 
Attribution-ShareAlike 4.0 International Licence, but the acces s conditions of the 
project stipulate that “Speciﬁc restrictions accompany each item”, 40 complicating 
the picture when it comes to accessing the material in the coll ection. But how is 
this possible with a project as large and heterogeneous as PARA DISEC, which 
holds 500 collections? 
The solution and the unique way in which PARADISEC diﬀers from many of 
the other examples in this book is that rather than being data-driven in its method 
for assigning access and restrictions, the approach is one of user-vetting instead. 
Possible due to the still relatively small user-base of content contributors, the PAR-
ADISEC workﬂows 
41 allow for a number of diﬀerent types of engagement and 
data deposit processes, but it is the registered user to whom the access rights are 
granted, not the digital resource. Admin and access information, data access condi-
tions, and data access details are assigned to individual users. 
PARADISEC operates a strict take-down policy. Any item deposited in the ar -
chive, if asked by anyone for any reason to be restricted or hidden, will be done 
so. This reﬂects the project’s understanding and respect for working with culturally 
sensitive material included in the PRADISEC archive, which can include content 
that is categorised as Secret-Sacred, or either Women’s Business or Men’s Busi-
ness. Since I’m neither an expert, stakeholder, nor a representative of a relevant 
community, I will not pursue this narrative further. 
This project is an example of one technical solution to the problem of diﬀerent 
degrees of access. It is diﬀerent from many other examples since it assigns access 

 
 
  
 
 
  
    
 
  
  
   
 
  
 
  
 
 
 
   
 
 
Closed But Not for Business 5 9 
rights to individual users, rather than to categories or speciﬁc instances of data. 
For an example of the latter, let’s examine the ElePHãT project, a case study in the 
amalgamation of data from diﬀerent sources that are subject to diﬀerent copyright 
restrictions and diﬀerent international laws. 
3.8 Case Study: The ElePHãT Project (Bibliographic Metadata) 
The ElePHãT project – Early English Print in HathiTrust, Linked Semantic Work-
sets Prototype – was funded through the Andrew W. Mellon Foundation Workset 
Creation for Scholarship Analysis project award ( Page et al., 2017 ). The aim of this 
project was to combine information from two complementary but disparate library 
collections: the Early English Books Online Text Creation Partnership (EEBO-
TCP) and the HathiTrust Digital Library (HTDL) ( Page and Willcox, 2015 ). 
EEBO-TCP is the result of a collaboration between ProQuest 
42 (a commercial 
company) and over 150 universities and libraries. It is led by the University of 
Michigan in the United States, and by the University of Oxford in the UK. The aim 
of EEBO-TCP is to generate and provide access to fully searchable XML-encoded 
texts representing the content of the English Short Title Catalogues I and II; the 
Thomason Tracts; and the Early English Books Tract Supplement, which together 
constitute a collection of material printed in English between 1473 (a date that 
constitutes the arrival of the printing press in England) and 1700. At the time of 
the ElePHãT project, Phase I of the EEBO-TCP was open and free for the public to 
access. This collection of available data of 25,000 texts constituted the EEBO part 
of the ElePHãT project. 
The origins of the HTDL are rooted in a public and legal debate about Open 
Access. The lengthy process of court cases has been covered from a number of 
diﬀerent perspectives ( Jones and Janes, 2010 ; Grimmelmann, 2010 ; Meyer, 2015 ), 
but a short recap here will help illustrate the way in which issues of copyright have 
restricted access to information, and why the HTDL is still in a complicated posi-
tion negotiating restrictive copyright on the one side, and their open mission on 
the other. 
The HTDL has its origins in the Google Books initiative. Although the public 
relations (PR) machine of Google claims that Google Books was at the heart of 
the development of the search engine from its conception in 1996 (inspired by the 
Stanford Digital Library Project-supported work Sergey Brin and Larry Page car-
ried out as graduate students), 
43 the large scanning of books in academic libraries 
by Google’s machines didn’t start until 2004. A year later, they were sued by the 
Author’s Guild. The process of legal battles took several years – in 2012, a district 
court ruled that the Google Books initiative and the resulting HTDL constituted a 
legal form of fair use (a prominently USA-based law which allows limited use of 
copyrighted material even without the copyright holder’s permission). 
The University of Michigan was one of the early adopters in terms of their 
participation in the Google Books project. Theirs was a vision of systematic but 
also controlled access to the storing and discovery of the academic content held in 
their institutional libraries. In recent years, the HTDL has grown beyond the core 

 
 
   
 
 
  
  
 
  
 
  
 
   
   
 
  
  
 
        
        
       
        
 
  
  
 
  
 
 
60 Closed But Not for Business 
of Google Books database, with additional content coming from the tertiary educa-
tion institutions around the globe that form their participatory listings. Alas, 66% 
of the HTDL context is under copyright, and access is limited t o metadata only 
( Jett et al., 2016 ). 
The niche and very ﬁnely curated dataset from the EEBO-TCP was matched, 
complemented, and enriched by a subset of the collection at the HTDL. At the time, 
the HTDL – which is itself an amalgamation of the collections of research institu-
tions and libraries in the USA, Europe, and Australia – included over 15 million 
digitised volumes (as of early 2021, this number had increased to almost 17.5 mil-
lion).
44 This can be broken down to almost 7.5 million book titles, nearly 500,000 
serial titles, and a staggering 5.3 billion pages ( Page et al., 2017 ). 
For the purposes of the ElePHãT project, a speciﬁc subset of the HTDL limited 
to materials that were published in English between 1470 and 1700 was used. Since 
the material is representative of the collections of many diﬀerent institutions, the 
available inherited bibliographic metadata varies between resources based on the 
institutional standards and policies of the originating libraries ( Page and Willcox, 
2015 ). Furthermore, as noted by Jett et al. (2016 ), both the content of texts and their 
associated metadata have been produced and OCRd by diﬀerent institutions using 
diﬀerent workﬂows, and contain idiosyncrasies that make them resistant to any 
attempts of large-scale, automated processes of standardisation and data tidying. 
It also results in a number of duplicates and alternatives, which nevertheless have 
suﬃcient diﬀerences in the metadata to make them appear as unique resources, and 
are only discovered to be identical once the content is examined. 
For both the EEBO-TCP and the HTDL collections, the original data was in a 
non-RDF format. Workﬂows which have been extensively reported on ( Page and 
Willcox, 2015 ; Page et al., 2017 ; Jett et al., 2016 ) will not be repeated here in great 
detail. Suﬃce to say that data held in alternative formats such as relational data-
bases and encoded as XML where converted to RDF using ontological structures 
that beneﬁtted from Classes and properties (explained further in Chapter 
4) from several bibliographic metadata ontologies, such as Bibliographic metadata 
ontology (MODS) 
45 and extension to MODS (MADS), 46 Bibframe,47 FRBRoo,48 
as well as Schema, 49 PROV , 50 and RO 51 ( Nurmikko-Fuller et al., 2015 ; Page et al., 
2017 ). It is important to note that as of February 2020, FRBRoo has been replaced 
by LRMoo. 
52 However, since the FRBRoo ontology propertiesand Classes 
were used at the time, and any URIs pointing to these concepts and relationships 
within the ElePHãT project RDF have the FRBRoo ontology preﬁx. 
The two aggregated corpora represent very diﬀerent aspects of the digital li-
brary spectrum: EEBO-TCP is a small but open and ﬁnely curated dataset; the 
HTDL subset is vast, with automatically generated metadata records, with con-
siderable restrictions to access. The ElePHãT project is thus a perfect case study 
example of a project where complementary but disparate datasets were converted 
into RDF and merged, but the resulting knowledge graph was not completely and 
comprehensively available to all users. It is an example of how technical solutions 
could be applied to beneﬁt from the Linked Data paradigm, even when some of the 
data is Open, and some of it is not. The solution here was to restrict access to some 

 
  
 
 
  
 
  
   
   
 
   
 
  
 
 
 
   
   
 
   
   
 
 
  
  
   
 
 
  
 
  
 
 
Closed But Not for Business 6 1 
of the produced RDF by some users. The implemented system architecture reﬂects 
this dichotomy of public and privileged data access through the SPARQL endpoint 
( Page et al., 2017 ). 
The copyright restrictions apply only to the deposited material, but not to the 
metadata. The most valuable aspect of the inclusion of the HTDL data is that it 
could be used to aﬀect the outcome of the SPARQL queries used to search through 
the aggregated datasets. That is to say that although the user could not see what the 
material was in the HTDL, that data would still act as one of the aﬀecting condi-
tions that aﬀected the ﬁnal results. The user can see that there is something in the 
HTDL that aﬀected the ﬁnal outcome of the query, but they cannot see what that 
something was. 
In addition to this restrictive policy on the record metadata, the ElePHãT 
project contains another form of non-open data in the form of JISC Digital 
Books. The project’s user interface (the Workset Viewer) 
53 allows users to query 
the project’s RDF triples: this includes the metadata of records from both the 
EEBO-TCP and the HTDL, as well as information about the alignments between 
works, people, and locations in the data. All this is freely and openly accessible, 
and the workset viewer provides example queries that pull content from both 
collections. For the EEBO data, if the user is from a subscribing institution, they 
may also access digital images of the work 
54 in question from JISC Historical 
Texts. 55 Again, this is a third and separate project, independent of the copyright 
restrictions imposed upon the HTDL, but limited in accessibility due to institu-
tional policy. 
The result of the diﬀerent degrees of openness is that the ElePHãT project re-
sults in three separate user interactions based on institutional policies alone. For 
the sake of clarity of discussion, let’s call the ﬁrst category unlimited access. This 
one consists of users whose institution has access to both the HTDL data, and to 
JISC Historical Texts. Their query will return results that are a list of all the works 
captured in the ElePHãT project, and their results can also display the digital im-
ages of relevant works. The second category of user comes from an institution 
that has access to the HTDL, but no subscription to JISC Historical Text. We can 
call this category project access. In this case, the user can access the digital object 
records in the two collections in the ElePHãT project, but they cannot access the 
third, external material. 
The third type of user experiences limited access. This type of user can access 
the openly available EEBO-TCP data, but cannot see the resources of the HTDL. 
Since the copyright restrictions apply to the digitised pages, the user will still be 
able to see the metadata records of each relevant resource, which will enable the 
user to try to locate the speciﬁc work in another repository or collection. Signiﬁ  -
cantly, the restricted content from the HTDL will still feature in the formation 
of the search results. Taking the “Political Science” example from the EEBOO 
workset viewer, the results from the HTDL of authors who have written on the 
topic inform the authors whose works are retrieved from the EEBO-TCP. 
56 To put 
it simply, the data from the HTDL which itself remains inaccessible to the user still 
features as a part for producing the ﬁnal results that answer the query. 

 
 
  
 
 
  
  
 
 
 
  
  
 
 
  
  
  
   
 
 
 
 
 
 
 
 
 
        
  
 
     
 
 
    
62 Closed But Not for Business 
3.9 Conclusion 
Institutional policies and economic models can aﬀect the practical solutions ap-
plied to a Linked Data project. This chapter took as its premise that if data does 
not contain socio-economically, medically, or other personal data (the exposure of 
which might adversely aﬀect an individual), it should also be Open – but that such 
levels of access are not always possible, even if desired by the researchers imple-
menting the project. 
As we have seen in this chapter, institutional policies and economic models can 
aﬀect how open a given cultural heritage institution makes their collections and 
data. This consideration, which is entirely removed from the theoretical, philo-
sophical, and even ethical values and premises of the researcher, nevertheless im-
pacts the implementation of Linked (Open) Data. The problems are multiplied in 
the process of aggregating data from two or more diﬀerent sources, with diﬀerent 
sets of institutional policies, and publishing in a machine-processable format. The 
practical solutions applied to projects where the involved institutions have diﬀerent 
policies are discussed in the context of a case study example, namely the ElePHãT 
project, which combined bibliographic metadata records from the Early English 
Books Online Text Creation Partnership with a subset of the HTDL. 
Linked Data and Linked Open Data are often used synonymously, with the 
former serving as a shorthand for the latter. There are clear d iﬀerences though, 
and they consist of technical, social, and economical aspects, the most funda-
mental (as reﬂected in the nomenclature) is the degree (if any!) to which th e 
data is Open (and thus accessible by human users and software agents alike). 
Institutional policies and economic models can and do aﬀect the practical and 
pragmatic solutions that researchers and developers can utilise in their projects. 
There are also diﬀerent but interconnected institutional policies and economic 
models that speciﬁcally aﬀect the “Open” of the data, and much more so than 
the “Linked” – it is thus not an issue of either limited (or deliberately limiting) 
the computational capacity: it is about what data can, should, and will be made 
accessible, and the (often ﬁnancial) reasons and motivations behind those deci-
sions. In other words, there are economic considerations which can and do lead 
to situations where not all information is published as FAIR data, even if it could 
be, and arguably, should be. This issue is not one that affects RDF and graph 
databases alone (in fact, most of the projects and examples of such limitations 
are non-Linked Data projects). 
Notes 
1 Trey Parker and Matt Stone, South Park, Season 7, Episode 9, aired 29 October 2003. http:// 
edition.cnn.com/TRANSCRIPTS/0007/11/se.01.html and www.mtv.com/news/1121985/ 
lars-ulrich-tells-senate-committee-napster-hijacked-metallicas-music/ . Both accessed 
28/05/2022. 
2 https://money.cnn.com/2001/07/12/news/napster/ accessed 28/05/22. Tom Lamont, 
‘Napster: the day the music was set free’, www.theguardian.com/music/2013/feb/24/ 
napster-music-free-ﬁle-sharing . Accessed 28/05/22. 
3 https://public.ccsds.org/pubs/650x0m2.pdf. Accessed 26/01/2023. 

     
    
    
    
      
       
  
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
      
     
 
    
    
    
    
    
    
    
 
    
     
    
     
    
    
    
     
    
5 
10 
15 
20 
25
30 
35
40 
Closed But Not for Business 6 3 
4 www.nhmrc.gov.au/about-us/publications/national-statement-ethical-conduct-human-
research-2007-updated-2018. Accessed 26/01/2023. 
https://diggingintodata.org/awards. Accessed 26/01/2023. 
6 www.cidoc-crm.org/version/version-7.1.1. Accessed 24/08/2021. 
7 www.cidoc-crm.org/frbroo/home-0. Accessed 24/08/2021. 
8 Scope notes are on p. 77 of www.cidoc-crm.org/sites/default/ﬁles/cidoc_crm_v.7.1.1_0. 
pdf . Accessed 24/08/2021. 
9 As earlier, but p. 99. Note that “An instance of E73 Information Object does 
not depend on a speciﬁc physical carrier, which can include human memory, and it can 
exist on one or more carriers simultaneously”. 
As above, but p. 80. 
11 http://lmb.cdhr.anu.edu.au/. Accessed 03/08/2021. 
12 https://trove.nla.gov.au/newspaper/article/13000723/1494784. Accessed 03/08/2021. 
13 https://trove.nla.gov.au/. Accessed 03/08/2021. 
14 www.nla.gov.au/. Accessed 03/08/2021. 
https://creativecommons.org/about/cclicenses/. Accessed 01/06/2021. 
16 www.gnu.org/philosophy/open-source-misses-the-point.html. Accessed 01/06/2021. 
17 https://opensource.com/open-source-way. Accessed 01/06/2021. 
18 https://sketchfab.com/. Accessed 01/06/2021. 
19 www.linkedin.com/. Accessed 01/06/2021. 
www.spotify.com/au/. Accessed 01/06/2021. 
21 https://pokemongolive.com/en/. Accessed 01/06/2021. 
22 www.minecraft.net/ﬁ -ﬁ. Accessed 01/06/2021. 
23 https://store.steampowered.com/. Accessed 01/06/2021. 
24 There are also other alternatives, such as the Hybrid, Bronze, Diamond/Platinum, and 
Black. 
As outlined at https://service.elsevier.com/app/answers/detail/a_id/5972/supporthub/ 
publishing/~/what-does-it-cost-to-publish-gold-open-access%3F/#:~:text=Please%20 
read%20more%20on%20full,from%20500%20%2D%205000%20US%20dollars . Ac-
cessed 01/06/2021. 
26 https://scholar.google.com/intl/en/scholar/citations.html?1#publicaccess. Accessed 
01/06/2021. 
27 https://en.wikipedia.org/wiki/Information_wants_to_be_free. Accessed 07/05/2021. 
28 www.rogerclarke.com/II/IWtbF.html. Accessed 06/05/2021. 
29 www.arc.gov.au/policies-strategies/policy/arc-open-access-policy. Accessed 07/05/2021. 
www.ands.org.au/working-with-data/fairdata. Accessed 27/05/2021. 
31 www.ands.org.au/working-with-data/fairdata. Accessed 25/02/2021. 
32 www.gida-global.org/care. Accessed 25/02/2021. 
33 The CARE Principles for Indigenous Data Governance can be downloaded in full from 
https://static1.squarespace.com/static/5d3799de845604000199cd24/t/5da9f4479ecab2 
21ce848fb2/1571419335217/CARE+Principles_One+Pagers+FINAL_Oct_17_2019. 
pdf . Accessed 25/02/2021. 
34 www.britishmuseum.org/terms-use/copyright-and-permissions. Accessed 27/05/2021. 
www.aph.gov.au/About_Parliament/Parliamentary_Departments/Parliamentary_ 
Library/FlagPost/2020/November/The_dismissal. Accessed 28/05/2021. 
36 www.legislation.gov.au/Details/C2019C00005. Accessed 28/05/2021. 
37 www.naa.gov.au/about-us/media-and-publications/media-releases/hocking-v-dg-
national-archives-australia#:~:text=‘The%20National%20Archives%20is%20 
a,compelling%20need%20to%20withhold%20it. Accessed 28/05/2021. 
38 https://protegewiki.stanford.edu/wiki/Main_Page. Accessed 07/05/2021. 
39 www.paradisec.org.au/. Accessed 02/06/2021. 
www.paradisec.org.au/deposit/access-conditions/. Accessed 02/06/2021. 
41 https://paradisec-archive.github.io/PARADISEC_workﬂows/. Accessed 07/06/2021. 
42 www.proquest.com/index. Accessed 06/05/2021. 

 
     
    
    
    
    
    
    
    
    
     
    
     
 
    
    
 
 
 
  
 
 
 
 
 
 
  
 
  
 
 
 
  
 
  
 
 
   
  
 
  
 
 
 
 
 
 
64 Closed But Not for Business 
43 https://books.google.com/googlebooks/about/history.html. Accessed 07/06/2021. 
44 www.hathitrust.org/about. Accessed 07/05/2021. 
45 www.loc.gov/standards/mods/modsrdf/. Accessed 07/05/2021. 
46 https://id.loc.gov/ontologies/madsrdf/v1.html. Accessed 07/05/2021. 
47 www.loc.gov/bibframe/. Accessed 07/05/2021. 
48 www.cidoc-crm.org/frbroo/home-0. Accessed 07/05/2021. Since February 2020, FRBRoo 
has been replaced by LRMoo (https://cidoc-crm.org/frbroo/ModelVersion/lrmoo-f.k.a.-
frbroo-v.0.6). Accessed 30/01/2023. 
49 https://schema.org/. Accessed 07/05/2021. 
50 www.w3.org/TR/prov-o/. Accessed 07/05/2021. 
51 https://wf4ever.github.io/ro/2016-01-28/. Accessed 07/05/2021. 
52 https://cidoc-crm.org/frbroo/ModelVersion/lrmoo-f.k.a.-frbroo-v.0.6. Accessed 30/01/2023. 
53 http://eeboo.oerc.ox.ac.uk/. Accessed 06/06/2021. 
54 An example of this is at https://data.historicaltexts.jisc.ac.uk/view?pubId=eebo-ocm122 
66003e, but the page is not accessible to the public nor to those whose academic institu-
tions do not subscribe. 
55 https://historicaltexts.jisc.ac.uk/. Accessed 07/06/2021. 
56 The query translates to: “Select all works from the EEBO-TCP, which have been written 
by authors who have also published on the topic of ‘Political Science’ in the HTDL”. 
This reﬂects the presence of the genre in the HTDL, but not in the EEBO-TCP. 
Bibliography 
Berners-Lee, T. (1999). Weaving the Web: The Past, Present and Future of the World Wide 
Web by Its Inventor. Orion Publishing Co. 
Berners-Lee, T., Hendler, J., and Lassila, O. (2001). “The Semantic Web”.  Scientiﬁ c Ameri-
can, 284(5), pp. 34–43. 
Bick, I. A., Bardhan, R., and Beaubois, T. (2018). “Applying Fuzzy Logic to Open Data for 
Sustainable Development Decision-Making: A Case Study of the Planned City Amara-
vati”. Natural Hazards, 91(3), pp. 1317–1339. 
Bishop, C. (2018). “Against Digital Art History”. International Journal for Digital Art His-
tory, 3(July). 
Bongiorno, F. (2021). “The Wait of History”.  Inside Story, May 7, 2021. https://insidestory. 
org.au/the-wait-of-history/ 
Collins, D. J., and Graham, D. J. (2019). “Use of Open Data to Assess Cyclist Safety In 
London”. Transportation Research Record, 2673(4), pp. 27–35. 
Cunningham, G. (2013). “The Sumerian Language”. In Crawford, H. (ed). The Sumerian 
World. Routledge. 
Gatti, T., Nurmikko-Fuller, T., Pickering, P., and Swift, B. (2022). “Having a Ball: A Linked 
Data Approach to Fancy Dress in Colonial Australia”. Proceedings of the International 
Digital Humanities Conference 2022 (DH2022), Tokyo, Japan, 27–29 July. 
Greenﬁeld, A. (2017).  Radical Technologies: The Design of Everyday Life. Verso. 
Grimmelmann, J. (2010). “The Elephantine Google Books Settlement”. Journal of the Cop-
yright Society, USA, 58, pp. 497–520. 
Huxley, A. (1932).  Brave New World. Longman. 
Jett, J., Nurmikko-Fuller, T., Cole, T. W., Page, K. R., and Downie, J. S. (2016). “Enhancing 
Scholarly Use of Digital Libraries: A Comparative Survey and Review of Bibliographic 
Metadata Ontologies”. Proceedings of the 16th ACM/IEEE-CS on Joint Conference on 
Digital Libraries, Newark, USA, 19–23 June. 
Jones, E. A., and Janes, J. W. (2010). “Anonymity in a World of Digital Books: Google 
Books, Privacy, and the Freedom to Read”.  Policy & Internet, 2(4), pp. 43–75. 

  
 
    
 
 
 
 
 
 
  
 
  
 
  
 
 
 
 
 
 
 
 
  
 
  
 
 
  
 
 
 
  
 
 
 
 
Closed But Not for Business 6 5 
Lantseva, A. A., and Ivanov, S. V . (2016). “Modeling Transport Accessibility With Open 
Data: Case Study of St. Petersburg”.  Procedia Computer Science, 101, pp. 197–206. 
Lessig, L. (2006). “Free, as in Beer”. WIRED, 9 January 2006. www.wired.com/2006/09/ 
free-as-in-beer/ . 
Levesque, H. J. (1984). “Foundations of a Functional Approach to Knowledge Representa-
tion”. Artiﬁcial Intelligence, 23, pp. 155–212. 
Lin, T., Liu, X., Song, J., Zhang, G., Jia, Y ., Tu, Z., . . . and Liu, C. (2018). “Urban Water-
logging Risk Assessment Based on Internet Open Data: A Case Study in China”.  Habitat 
International, 71, pp. 88–96. 
Mahabir, R., Agouris, P., Stefanidis, A., Croitoru, A., and Crooks, A. T. (2020). “Detecting 
and Mapping Slums Using Open Data: A Case Study in Kenya”. International Journal of 
Digital Earth, 13(6), pp. 683–707. 
Meyer, R. (2015). “After 10 Years, Google Books Is Legal”.  The Atlantic, October 20. 
Nurmikko-Fuller, T., Page, K. R., Willcox, P., Jett, J., Maden, C., Cole, T., . . . and Downie, 
J. S. (2015). “Building Complex Research Collections in Digital Libraries: A Survey of 
Ontology Implications”. Proceedings of the 15th ACM/IEEE-CS Joint Conference on 
Digital Libraries Knoxville, USA, 21–25 June. 
Nurmikko-Fuller, T., and Pickering, P. (2021). “Reductio ad Absurdum?: From Analogue 
Hypertext to Digital Humanities”. Proceedings of the 32nd ACM Conference on Hyper -
text and Social Media (ACMHT21), Dublin, Ireland, 30 August–2 September. 
Page, K. R., Nurmikko-Fuller, T., Cole, T., and Downie, J. S. (2017). “Building Worksets 
for Scholarship by Linking Complementary Corpora”. Proceedings of the International 
Digital Humanities Conference 2017 (DH17), Montreal, Canada, 8–11 August. 
Page, K. R., and Willcox, P. (2015). ElEPHã T: Early English Print in the HathiTrust, a 
Linked Semantic Worksets Prototype . Final Report for Workset Creation for Scholarly 
Analysis: Prototyping Project, University of Illinois at Urbana-Champaign. 
Schöch, C. (2013). “Big? Smart? Clean? Messy? Data in the Humanities”. Journal of Digi-
tal Humanities, 2(3), pp. 2–13. 
Taylor, J. (2013). “Administrators and Scholars: The First Scribes”. In Crawford, H. (ed). 
The Sumerian World. Routledge. 
Themistocleous, K. (2017). “Model Reconstruction for 3D Visualization of Cultural Herit-
age Sites Using Open Data From Social Media: The Case Study of Soli, Cyprus”. Journal 
of Archaeological Science: Reports, 14, pp. 774–781. 
van Hooland, S., and Verborgh, R. (2014). Linked Data for Libraries, Archives and Muse-
ums: How to Clean, Link and Publish Your Metadata. Facet Publishing. 
Zeng, M. L. (2019). “Semantic Enrichment for Enhancing LAM Data and Supporting Digi-
tal Humanities. Review Article”.  El Profesional de la Información, 28(1), p. e280103. 

 
  
 
 
  
 
     
 
 
     
 
   
 
  
   4 “Truth” and Bias 
4.1 Preamble 
In “Good Omens”, Pratchett and Gaiman (1990 : 17) provide a delightful observa-
tion of the subjectivity of winks. An exchange between nuns in their botched at-
tempt to swap the newborn baby of an American diplomat for the Antichrist seemed 
humorous enough, but it’s genius is in conveying the idea that even something as 
simple as a wink is necessarily subject to speciﬁc interpretation, with potential dis-
agreement over meaning, and the possibility of ambiguity between communicat-
ing co-conspirators. The academic value of this concept emerged from an entirely 
unpredicted source: Katrina Grant’s 2022 work “Landscape and the Arts in Early 
Modern Italy” outlines the signiﬁcance of the wink as a case study of anthropologi-
cal investigations, ground in a robust theoretical framework. 
Enter Cliﬀord Geertz (1973 : ﬀ 6), and his description of the wink as mode of 
communication. He surmises a scenario – a thought experiment, if you will – of two 
boys who are manifesting the same physical movement (“rapidly contracting their 
eyelids of their right eye”), but whilst for one it is an involuntary twitch, for the 
other, it is a wink. A deliberate, conspiratorial, socially determined way of passing 
on information. There are thus two completely valid and accurate descriptions of 
the same phenomena – the “truth” and accuracy of the label applied to the eye-lid 
twitching is context-dependent, and requires additional knowledge about the boys, 
their activities, aims, modes of social interaction, and myriad other considerations. 
It is reminiscent of the “6–9” meme.
1 It depicts two men discussing graﬃti on 
the ground. The man on the left proclaims it to be the number six; the man on the 
right, seeing it from the opposite direction, insists it is a nine. Thus, we see that per-
spective is important; we all have preconceptions, and our understanding of facts 
is neither neutral nor objective. It’s not just beauty that’s in the eye of the beholder 
but also the wink, blink, or twitch. 
Googling for the 6–9 meme will bring up a myriad of interpretations of the same 
image by Web users across the globe. One of the more advanced is a discussion 
between two contributors and published on the second discussant’s blog. 
2 The ﬁrst 
editor declares that the two men’s views cannot in fact be both equally correct, 
for there are pieces of contextual information such as the intention of the original 
graﬃti artist (who will have known which number they were depicting) as well as 
DOI: 10.4324/9781003197898-4 

 
 
 
 
 
  
  
 
  
 
   
 
     
   
 
 
 
  
“Truth” and Bias 6 7 
details such as the orientation of the road, the locations of nearby buildings, and so 
forth. They lament the lack of willingness of people to do research, in their rush to 
just be right. The second author has chimed in to counter this argument, stating that 
it is rare that we can omnisciently discuss the motivations of others, and that many 
things we observe are not the result of a deliberate cognitive process. The problem, 
he says, is that we believe in the possibility of objective observation and analysis, 
when those cannot exist. 
And yet, much of knowledge representation and database development seems 
to have that exact aim, or user expectation. Computational technologies, digital 
databases, and algorithms seem to enjoy a status of objectivity – because it’s a 
computer, it doesn’t care or have opinion, so it can’t be biased. This assumption, 
one that sometimes plays a covert role in our thinking, is a falsehood. Every sys-
tem, every algorithm, every dataset contains some decisions that were at some 
point made by someone. That is not to say that digital tools or their creations are 
motivated by exclusively nefarious agendas, but if there is one common thread wo-
ven throughout this book, it is the recognition of the universal truth of Kranzberg’s 
(1986 : 545) First Law: “Technology is neither good nor bad; nor is it neutral”. 
To apply this idea to the speciﬁc context of Digital Humanities, and to Linked 
Data in particular, we need to have a closer look at information representation as 
part of the process. For the purposes of ontological modelling and the Linked Data 
paradigm, the recognition of the impossibility of a completely objective under -
standing of the universe (and everything in it) is absolutely paramount, but how 
actively is this critique or understanding applied to the process? Ultimately, what 
we must contend with is the possibility that we have insuﬃcient information to 
determine whether it is a wink or a blink. Perhaps it is a matter of opinion or per -
spective: one man’s blink is another man’s wink. Thus, we should strive for models 
that enable the representation of both. Sure, this makes the model more complex 
(which has the problem of being computationally more expensive, but also more 
diﬃcult for a human user to comprehend and use). But what’s a little complexity 
when the representation of truth is at stake? 
4.2 Ontologies 
Perhaps the most famous of deﬁnitions for ontologies is the one from Gruber 
(1993 ) that we encountered in  Chapter 1: “An ontology is an explicit speciﬁcation 
of a conceptualization”. The sentence is thrilling in its snappy delivery but also 
impenetrable. What, exactly, is a conceptualisation, and what is a speciﬁcation 
of such a conceptualisation? And does the possibility of an explicit speciﬁcation 
imply the possibility of a vague one? 
Building on Henry Ward Beecher’s metaphor of words as pegs on which ideas 
are hung, Hyvönen (2018 : 150) introduces the concept of ontologies as pegs from 
which words are hung. Ontologies have been declared as being “crucial to the 
Semantic Web” by Wilks and Brewster (2009 : 2).  DuCharme (2013 : 39) describes 
them as “formal deﬁnitions of vocabularies that allow you to deﬁne complex struc-
tures as well as new relationships between your vocabulary terms and between 

 
 
  
  
 
  
  
  
 
 
 
  
 
 
      
      
       
  
  
        
        
 
  
        
         
   
      
  
 
  
    
  
 
 
 
 
68
 “Truth” and Bias 
members of the classes that you deﬁne”, addressing both the schema-level and 
instance-level functionality of ontologies. 
For me, ontologies are formalised structures that act as information templates – 
that is to say, they are machine-readable documents, written in RDF, which explicitly 
state all the possible types of things that can exist in the domain that the ontology 
is mapping (such as people, places, and events perhaps), as well as the possible re-
lationships between those entities (a person might be born in a place, or a person 
might have attended an event). They deﬁne the rules, which determine those RDF 
triples that are possible (and if you so choose, those that are not). They come with 
the promise of enabling automated inference, the process of bringing forth implicit 
information and connections within a dataset, by deducing new links that indirectly 
exist between explicitly declared facts. The aim of an ontology is to provide a for-
malisation that represents the knowledge within and about a speciﬁc domain. For this 
reason, ontologies can be subjective, or include overt or covert biases of the ways in 
which the people who designed them see the world. 
Ontologies consist of Classes and properties. There is no technologi-
cal reason for this, but the human-readable convention that some of us choose to 
use is that the former are written with capital letters, and the latter are all lower 
case. This maps onto the structure of the triple as well: Subjectsand Objects
are instances of Classes, and predicatesare properties. Ontologies are 
commonly visualised as a type of network graphs: where the latter have nodes and 
arcs, the former have circles and lines. The circles are Classes, the lines are 
properties. Ideally, these lines are in fact directed arrows that show the order 
of the triple: propertiesalways run from a Domainto a Range. The former is 
a Classfor which a given propertyis speciﬁcally deﬁned, the latter comprises 
all possible values for that property. 
Ontologies are decentralised and non-hierarchical. They can be navigated from 
any starting point. The only hierarchical structures that ontol ogies exhibit are the 
hypernyms and hyponyms of Classes and properties: Classes can have 
superClassesand subClasses, and propertiescan have superprop-
ertiesand subproperties. These relationships express an increasing granu-
larity or specialisation, and are perhaps best explained via a mnemonic: “All lions 
are animals, but not all animals are lions”. This simple rule explains the relationship 
between superClasses (animals) and subclasses (lions). The key here is 
that lions will have all the characteristics (or properties) that all animals have, 
but there will be some other animals, which do not share all of the characteristics of 
a lion (a herbivore, for example, will have a diﬀerent kind of diet, diﬀerent kind of 
teeth, etc.). Similarly, subClasses inherit all the properties from their super-
Class, so in this example, we would not have to deﬁne for all animals separately 
that they need air, water, a habitat, they mate, they have life spans, etc. 
Although no taxonomy of ontologies exists, they are broadly divisible into four 
main categories: domain-speciﬁc (or domain ontologies), upper (or general ontolo-
gies), representation, and application ontologies. Of these, the ﬁrst is focused on 
the representation of a speciﬁc subset of the world, such as a discipline or area of 
expertise. For scholars of the Humanities and practitioners of the GLAM sector, the 

  
    
  
  
  
 
  
  
 
 
  
 
  
 
 
  
 
 
 
  
 
“Truth” and Bias 6 9 
most well-known is arguably the CIDOC CRM. 3 This particular conceptual refer-
ence model has been extended to include many subdomains, such as (inter alia) 
provenance metadata 4 and social phenomena. 5 It has also been applied successfully 
in the context of the Linked Art community, who have developed the Linked Art 
Model as a simple and more easily applied core of the complex CIDOC CRM. 6 
Upper ontologies on the other hand are designed to model those entities and as-
pects that are a common occurrence, universally. Examples of these might include 
WordNet, which is based on the English lexicon and where the concepts number 
in their hundreds of thousands. Semantic Web languages, such as OWL and RDFS 
(RDF Schema), are representation ontologies, and are used for low-level capture 
(and indeed often the structure of the ontology itself), whilst ontologies built to 
meet the needs of a speciﬁc application are examples of the ﬁnal category. 
Ontologies can vary in their design philosophy. Brewster and O’Hara (2004 ) 
quote Steve Fuller, who divides ontologies into two main categories: the Newto-
nian (a reductionist, more descriptive model) and the Leibnizian (which is more 
concerned with the capture of the nuanced complexities of experience). The beneﬁ t 
of the former is that it is easier to control and administer – the latter is fuzzier but 
may be thus easier to apply. A Newtonian philosophy regarding ontology design 
necessitates a degree of omniscience over the subject domain, but those of the 
Liebnizian school of thought are perhaps more likely to argue that since true ob-
jectivity is unachievable, a data-driven approach is the more truthful of the two 
( Nurmikko-Fuller, 2018 : 348). 
Undeniably and by their very nature, ontologies present a reﬂection of ways in 
which those people who design them perceive reality. Idiosyncratic and culturally 
conditioned values can aﬀect the structure and design of an ontology. Consider, 
for example, the complex issue of sex and gender (which is a diverse and nuanced 
spectrum insuﬃciently captured by the binary of male and female), or the percep-
tion that time is a linear construct. Since ontologies reﬂect the world as interpreted 
by those who design them, a hermeneutic approach to evaluating the embedded 
design decisions becomes nothing short of essential. 
It is not a universally agreed fact that ontologies are strictly necessary for the 
implementations of Linked Data projects. DuCharme (2013 : 310) notes that pro-
viding “a set of property declarations with no class declarations is actually quite 
common because [it enables people to] share their vocabularies for reuse without 
getting involved in more structural declarations of classes and their relationships”. 
Whether or not they are strictly necessary for a Linked Data or Linked Open Data 
implementation, any “working ontologist” ( Allemang and Hendler, 2011 ) will ﬁnd 
them a useful solution for gracefully navigating and scaling the complexities of the 
(digital) Humanities datasets they work with. 
4.3 Bias in Ontologies 
But wait, there’s more to Geertz’s wink. Not satisﬁed with the complexity of the 
question with regard to just two boys, he proposes a third, who engages in the ac-
tivity with malicious intent. The examples become increasingly complex, to build 

 
        
 
 
  
 
 
 
  
   
 
  
 
 
 
 
 
 
  
 
70 “Truth” and Bias 
the argument that although all boys are manifesting the same behaviour, observa-
tion of the eye moment alone is insuﬃcient in the understanding of the meaning 
of that behaviour. 
Western perspectives have permeated almost every aspect of information cap-
ture, representation, and analysis. From Linnaean taxonomy to the inherently racist 
roots of Statistics, to Google search results, Western ways of categorising the world 
have become the only acceptable voice of authority. Much of modern technologi-
cal development, and especially digital and computation development is (right or 
wrongly, given the facilities and outputs of Zhongguancun in the Beijing-Tianjin-
Shijiazhuang Hi-Tech Industrial Belt) accredited to the Silicon Valley of the San 
Francisco Bay Area in Northern California. 
7 The truth is the history of Computer 
Science, both of software and hardware, has been more diverse than the image of 
the modern WASP: this white, Anglo-Saxon Protestant is a privil eged, cisgender, 
heterosexual, atheist male. These men have decided between a wink and a twitch: 
it is in their eye that the beauty
8 is beheld. 
Silicon Valley and the tech giants that are driven by middle-aged white men 
(Tim Cook for Apple, Bill Gates for Microsoft, the slightly younger Mark Zucker-
berg for Facebook, Ted Sarandos and Reed Hastings for Netﬂix, etc.) have come 
under criticism for creating a society that the Guardian describes as 
a networked world dominated by an industry that oozes tech-bro arrogance 
and aﬄuence combined with a profound ignorance of what life is like for 
most people. . . The tech elites who create the products and services are 
unlikely to have experienced social exclusion, racism, misogyny, poverty or 
physical abuse. And in particular they have little idea of what life is like for 
women . . . It’s hard to avoid the conclusion that they still see . . . say, hate 
speech, as a PR problem to be managed rather than as a structural issue that 
requires radical reform.
9 
Cultural background, lived experience, personal preference, prior knowledge, 
and myriad other considerations form part of our perception of the world and how 
we categorise what we encounter. And, just as our own internal biases aﬀect the 
way we interpret information, so too do the design decisions that have gone into 
the development of digital information storages. In a similar way, the histories 
of cultural heritage organisations and scholarly traditions inﬂuence the perceived 
and articulated needs and scope of databases utilised in the sector. Natural History 
museums for example tend to favour hierarchical structures that work well with 
the Linnaean taxonomies working their way down from domains and kingdoms 
down to individual species, but why should we assume a similar structure would 
be appropriate for recording, say anthropological data, or the social networks used 
for prosopography? It is important to remember that even this seemingly scientiﬁ -
cally rigorous approach is prone to error, such as the misclassiﬁcation by Linnaeus 
himself ( Witteveen and Müller-Wille, 2020 ). 
The process of ontological modelling for the Semantic Web, or for Linked 
Data, is all about identifying and representing reality. It is the process of identifying 

 
  
 
 
 
  
 
  
 
 
   
 
 
  
 
 
   
 
 
 
 
 
 
 
  
  
     
   
 
   
   
   
   
       
 
 
 
      
“Truth” and Bias 7 1 
data categories (such as people or places) and the relationships between them. It 
is thus the very epitome of subjectivity. A simple thought experiment illustrates 
the point: if you are not aware of the possibility of a wink as a form of interper -
sonal communication, all instances of an eye movement could only ever be a 
variant of a blink. 
If one were to create an ontology of eye-movement reasons, one might fea-
sibly utilise qualitative research methods and interview the boys to assess their 
reasons, aims, and activities, and situate that in a socio-culturally accurate con-
text. But what to do when there are no people to interview? The assertion of an 
interpretative lens when cast on historical and archaeological material has this 
exact challenge. The risk here is of the temptation to ﬁll in the blanks, or to inter -
pret ﬁnds or historical practice through our modern values, cultural practices, and 
ethical, legal, and social norms of our times. The desire or te ndency to do so can 
be completely covert (so much so, that we are not aware of it ourselves). There is 
also a practical and pragmatic line to be drawn somewhere: there is a diﬀerence 
in the complexity of the model, and thus its relative usability , depending on how 
detailed the granularity of the fact that’s being represented. We might think it’s 
reasonable to diﬀerentiate between diﬀerent kinds of people, for example, based 
say, on their job description (doctor, dentist, cleaner, software developer) or their 
role in society (king, peasant, tax payer), but we might take it for granted that 
all these people operate within a linear space-time continuum. The decision as to 
which aspects of our reality to capture is driven by the knowledge, aims, skills, 
and decisions of the person creating the ontological model. It is thus inherently 
subjective. 
4.4 Document Your Design 
Ontologies can and do exist for an immensely wide range of topics. These 
certainly include domain-speciﬁc ones, which focus on a given discipline or 
area of expertise, such as the CIDOC CRM 
10 for museum data; LRMoo 11 for 
libraries; or the Music Ontology, 12 which, as the nomenclature would suggest, 
maps information about music. But there are also other ontologies that tackle 
much more abstract no tions: the Event
13 ontology, for example. Similarly, 
Provenance Ontology (PROV-O) 14 maps processes, in this case of data prov-
enance. At the very most abstract end of the spectrum are RDF Schema 15 and 
OWL,16 which do not map concepts but the concept of a concept – for example, 
owl:Class deﬁnes a given idea as an entity, rather than a property (a re-
lationship between entities). 
More than one ontology can be the “correct” one in terms of be ing applicable 
to a resource, depending on what the aim of the mapping is: you could have one 
ontology for capturing physiological movements of the facial muscles and another 
for facial expressions as a mode of communication. RDF as a tec hnology is very 
robust to change, and it is also very easy to add enriching information by equating 
Classes and properties from one ontology to respective ones in others – 
technologically. That is to say, you can simply add an addition al RDF triple to 

 
   
       
 
 
  
 
   
     
   
   
      
    
  
 
 
  
 
  
   
  
 
 
      
   
          
      
72 “Truth” and Bias 
equate a Class with another (both ontologies might reasonably have a separat e 
Class for both a twitch and a wink), but knowing that these two Classes i n 
these two diﬀerent ontologies refer to the same thing is an intellectually challeng-
ing and time-consuming task. 
The documentation of design decisions thus becomes of the utmost importance. 
Unfortunately, documenting is a labour-intensive, boring, time-consuming, and ut-
terly under-appreciated task. This can be particularly true in those instances where 
the data category (Class) or characteristic (property) is very familiar concep-
tually to the person responsible for the documentation. “But this is obvious!” we 
exclaim and throw our hands in the air. Or perhaps we internalise this frustration, 
and it only manifests as an involuntary muscle twitch in the eye. 
The ontologies developed by the Library of Congress for capturing bibliographic 
metadata illustrate both excellent and appalling approaches to documentation. 
Remembering that the aim of the documentation is to describe each Class and 
propertywith suﬃcient information to enable someone else (a human scholar!) 
to decide whether or not the Class in question matches the requirements of 
their data, we can compare and contrast the madsrdf:Title from the MADS-
RDF ontology, 
17 with bf:Title from Bibframe 18 (both are by the Library of 
Congress). The Classes refer to the same concept, but the diﬀerence in docu-
mentation is notable ( Table 4.1 ). Insuﬃcient documentation means users can less 
conﬁdently assert equivalence to their data, or to other ontologies, but good quality 
documentation is time-consuming. It would seem though that since the fundamen-
tal premise of Linked Data is to facilitate information exchange, increased inter -
linking, and improved discoverability, it is worth investing that time. 
The reuse of ontologies deﬁned in the context of other projects can fall prey to 
similar concerns. Whilst there are myriad reasons for the reuse of existing ontolo-
gies (beneﬁtting from the insights of experts, time-eﬀective use of an existing re-
source, increased discoverability, etc.), unclear or limited (and in some cases even 
omitted) documentation of the ontology risks the incorrect reuse of a Class or 
property. Perhaps defaulting into the reuse of a suboptimal but known ontology 
is more likely, for reasons identical to those for the picking and choosing of triple-
stores: familiarising oneself with an ontology is time-consuming and intellectually 
challenging. There are clear beneﬁts for the decision to use a known and popular 
ontology, but those decisions do not reﬂect an objective evaluation of all possible 
ontologies (or even all known ontologies). 
  Table 4.1 The diﬀerence in the documentation of two ontologies with the same Class of 
Title, both from the Library of Congress 
Class 
Scope note 
www.loc.gov/mads/rdf/v1#Title 
“Describes a resource whose 
label represents a title”. 
http://id.loc.gov/ontologies/bibframe/Title 
“Title information relating to a resource: 
work title, preferred title, instance title, 
transcribed title, translated title, variant 
form of title, etc.” 

 
 
 
 
 
 
 
  
  
  
  
  
 
 
  
 
“Truth” and Bias 7 3 
4.5 Justify Your Choices 
Seeing bias in ontological modelling can be relatively easy if it pertains to perspec-
tives or associations that are part of our daily thinking and d iscourse. Observing 
a gender bias, for example, might come more readily to a resear cher working on 
gender issues; class theory might be evident to Marxist scholars. One of the chal-
lenges of working with information that captures and represents events of the distant 
past is the constant need to determinedly avoid succumbing to t he temptation of 
presentism. This can be challenging without a healthy degree of self-criticism and 
introspective evaluation – nevertheless, it can be tricky to avoid the uncritical ap-
plication and adherence to modern-day moral, ethical, social, a nd legal standards, 
attitude, and opinions. Examples of issues where we might strug gle to do so are 
historical examples of cultural and social practices which we do not agree with, such 
as human sacriﬁce, child brides, or slavery. Although tackling complex issues, these 
examples have a relative simplicity to them as they constitute extreme examples for 
which many of us will hold deeply seated and unambiguous views – certainly they 
are topics that few us remain ambivalent about, but they are al so ones that show 
a diachronic shift from social acceptance and even active promo tion to the large 
scale condemning and prohibition of an act or practice: what wa s once acceptable 
and good is now abhorrent and bad, or vice versa. The manifestation of issues such 
as the lens of presentism is easy to spot if we condemn practices which were once 
socially acceptable but now to us are not in our historical analysis, and similarly so 
if we build this value judgement into our ontological models. 
There are also other more ambiguous cases, where the risk of presentism is less 
clear, or not as easily distinguished from contemporary cultural perspectives. Ex-
amples might include the prohibition of the consumption of pork, which has long 
roots in some cultural contexts, but is not universally observed. Can we compare 
that to relatively recent changes in some cultural context of say, the banning of 
smoking in public and conﬁned spaces? And will future generations judge us for 
the consumption of sugar, the use of palm oil, and other cultural practices which 
might seem innocuous to us now (leaving the lights on, letting the tap run, choos-
ing to drive short distances)? And there is also the possibility of intangible heritage 
that has been lost and is thus unknown to us: would it not be impossible to build 
an ontological model that captured a fourth option beyond a wink, a blink, and a 
twitch if those three are the only options we know of? 
In a similar way to how we must resist the temptation of applying modern moral 
and ethical views to ancient practices, so too should we consciously try to avoid cat-
egorising the ancient world into knowledge categories that make sense to us today. 
The Linnaean taxonomy of plants is unlikely to map easily to an ancient categorisation 
of herbs and ﬂora, and forcing that categorisation risks the loss of tacit knowledge, 
inferable from the context in which diﬀerent plants may occur, for example. That 
having been said, the Linnaean model itself is a product of a historical period and is 
not entirely without ﬂaw or historical bias. Another rather tragic example of this is at-
tempts by Banks to apply the Linnaean categorisation to Australian ﬂora in 1777 – and 
in doing so forcing the loss of Indigenous knowledge accumulated over millennia. 

 
  
 
  
  
 
 
 
 
 
  
 
 
 
  
 
 
       
      
 
 
  
 
 
  
    
   
  
  
  
  
 
 
 
 
 
 
74 “Truth” and Bias 
By way of an example which is easy to relate to and which has enjoyed some 
time in the public limelight already is the notion of gender binary, which is not, 
although insisted by many non-experts, based on scientiﬁc facts. Human genetics 
are much more complex than a division into just XX or XY chromosomes, and 
even the notion that the gender binary as a traditional social construct is broken 
as soon as we examine this categorisation outside of the Western taxonomies. 
We see this categorisation everywhere on a daily basis although not necessarily 
ubiquitous – but it is in legal documents; it is reﬂected in architecture of build-
ings in the form of toilets and changing rooms; it determines the arrangements 
of clothes in stores; it is reﬂected in the colour coding of products from pens 
to personal hygiene. And indeed there are digital ontologies which categorise 
all human persons into either Female or Male exclusively. An example of this 
is the Networked Environment for Personalized, Ontology-Based Management 
of Uniﬁed Knowledge (NEPOMUK) Contact Ontology, which describes a topic 
as innocuous as contact information. Established in 2007 and updated in 2013, 
the NEPOMUK ontology explicitly and exclusively only permits two genders, 
nco:female and nco:male. The documentation speciﬁes that “instances of 
this Class may include male and female”. 
19 Rather than a conscious attack on 
gender minorities, or the deliberate perpetuation of the binary, this seems a likely 
example of unchecked bias. Since genre is by no means the main focus of this 
ontology, the issue has been solved quickly, eﬃciently, and, arguably, with mini-
mal thought and evaluation. But not with malice. 
Other ontologies such as the Friend of a Friend (better known by its acro-
nym FOAF, pronounced “foafh”), 
20 one of the most frequently used ontologies, 
opts not to explicitly map gender diversity, but rather leaves it open to the user: 
foaf:gender is commented with the gender of this Agent (typically but no t 
necessarily “male” or “female”). . . In most cases the value wi ll be the string 
“female” or “male”. . . Values other than “male” and “female” m ay be used, but 
are not enumerated here. The gender mechanism is not intended to capture the 
full variety of biological, social and sexual concepts associat ed with the word 
“gender”.21 
Recent social interest and the rise of the LGBTQI+ community’s voice has seen 
this categorisation change, and indeed there are ontologies such as Homosaurus, 22 
which has made an attempt to include a greater degree of diversity in its categorisa-
tions of people. This ontology includes non-Western approaches to gender, includ-
ing terms from at least Samoan, Tongan, Italian, Dominican, Indigenous Canadian 
(speciﬁcally Ojibwe), Hindi, Native American (speciﬁcally Mohave), Urdu, and 
Turkish to diversify and enrich the gender binary to cover not just three but many 
other genders as well, including representing gender ﬂuidity and thus enabling an 
idea that gender may not be set and immutable. But this is just one ontology, and 
one that has not yet enjoyed wide-scale adoption to information representation. 
But, certainly it is an example of new things to come, perhaps the ﬁrst of many 
diﬀerent models capturing rich and diverse perspectives onto the categories used 
to deﬁne and understand human groupings in the world. 

 
 
  
 
 
 
 
 
  
  
 
 
 
 
“Truth” and Bias 7 5 
What is important to note here is, whether adhering to the gender binary, or 
deliberately breaking it, the designers of these ontologies were driven by a desire 
and aim to capture the truth of the world as they see it, experience it, and know it. 
There is thus an unavoidable bias in the design of the ontology itself, which can be 
diﬃcult or even impossible to spot until one is explicitly confronted by a contra-
dicting and contrasting viewpoint. 
In other situations, presentism might creep in unobservable and unchallenged. It 
might be present but undetectable because the values or terminologies in use have 
not changed. It could be easier to spot in a historical context , removed from our 
own. An example of the latter is the interpretation of the Mesopotamian archaeo-
logical material through a Biblical lens: consider for example Woolley’s 1923 publi-
cation “Ur of the Chaldees” or his naming each of the near-identical pair of ﬁgurines 
of goats found at the Royal Tombs of Ur as a “Ram in the Thicket” (a reference to 
the motif in Genesis). It appears the naming conventions are le ss of an accidental 
interpretation and more of a deliberate display of knowledge of biblical themes: an 
ophthalmologist sees ocular myokymia in every twitch, wink, and blink. 
4.6 Case Study: Old Babylonian Literature 
The following case study example describes a Linked Data project for capturing 
the narratives of literary compositions 
23 considered to be mythological in genre, 
written in Sumerian 24 by the scribes of ancient Babylon around 2500 BC – a con-
text spatio-temporally, culturally, and linguistically far removed from modern-day 
hubs of technological development. 
Linked Data and ancient Sumerian literary compositions can be successfully 
paired ( Nurmikko-Fuller, 2014 , 2018 ): applying ontologies to content written some 
4,500 years ago enables us to test the robustness and suitability of modern onto-
logical structures to adequately capture and represent ancient world data. But in 
doing so, we must be hypervigilant in not inadvertently superimposing modern 
conventions and perspectives onto ancient world data – or, at the very least, criti-
cally assess whether it is even possible to use modern ontological structures, built 
by modern scholars with modern views to represent modern data in this ancient 
world context. 
What we have here is the juxtaposition of a dataset that is characterised by all the 
attributes of Humanities data: the corpora are rich and heterogeneous in type, genre; 
the texts themselves are often broken, tablets are missing or damaged, and the twin 
accidents of preservation and discovery mean that what we do have is a scattered and 
incomplete sample of what once was. This unstructured data, riddled with linguistic 
and historical uncertainty and ambiguity, oﬀers an incredible opportunity for us to 
test the limits of the Linked Data methodology. It is positioned to support existing 
research paradigms in many ways (such as through the aggregations of collections 
and data from cultural heritage institutions) but can also enable a wholly new set of 
research questions especially at the periphery of disciplines (such as the exchange of 
ideas in Hellenistic Babylonia with the other cultures of the Mediterranean). 

 
 
  
   
 
      
 
  
   
 
 
  
 
  
  
  
  
 
 
 
 
  
 
 
 
76 “Truth” and Bias 
4.6.1 Choosing the Case Study 
The composition could be studied from the perspective of several diﬀerent do-
mains: narratology (e.g. Propp, 1968 ; Campbell, 2008 ), object biography and 
bibliographic metadata, as well as Assyriology. The challenge h ere was to assess 
whether existing Linked Data tools (namely, existing ontologies developed and 
designed to capture those domains) could be used to adequately represent all those 
aspects without succumbing to a reductionist approach or shoe-horning ancient 
concepts into modern ontologies. 
The Three Ox-drivers of Adab
25 has a non-linear narrative structure, which would 
make the narrative arc an interesting challenge to map (in other words, should 
events be represented in a linear fashion, or are the narrative devices of a frame 
story and or a ﬂashback signiﬁcant enough attributes to warrant representation in 
the ontological model?). It has characteristics typical of longer compositions from 
the ancient Near East; representing these would enable the comparison between 
this case study example and other compositions that do not share any motifs or 
protagonists nor location, but instead are similar at a structural level. It also bears 
similarities to another text, The Old Man and the Young Girl ( Alster, 1991 –1993; 
Gadotti, 2014 ), providing an ideal opportunity for comparative analysis between 
representations of texts that have similar content and context. Finally, consisting 
of incomplete fragments separated by several centuries, the primary sources that 
bring us this story are a tangible example of unknown, incomplete, and ambiguous 
unstructured Humanities data.
26 
4.6.2 Three Ox-drivers of Adab 
The ﬁrst 30 lines of the inscription set the scene for an ancient joke or riddle ( Al-
ster, 1991 –1993; Foster, 1974 ; Lambert, 1995 ). This translation is as provided by 
the Electronic Text Corpus of Sumerian Literature: 
27 
Our king! We are ox-drivers. The ox belongs to one man, the cow belongs to 
one man, and the wagon belongs to one man. We became thirsty and had no 
water. 
We said to the owner of the ox, “If you were to fetch some water, then we could 
drink!”. And he said, “What if my ox is devoured by a lion? I will not leave my 
ox!”. 
We said to the owner of the cow, “If you were to fetch some water, then we could 
drink!”. And he said, “What if my cow went oﬀ into the desert? I will not leave 
my cow!”. 
We said to the owner of the wagon, “If you were to fetch some water, then we could 
drink!”. And he said, “What if the load were removed from my wagon? I will 
not leave my wagon!”. 
“Come on, let’s all go! Come on, and let’s return together!” 
“First the ox, although tied with a leash (?), mounted the cow, and then she dropped 
her young, and the calf started to chew up (?) the wagon’s load . Who does this 
calf belong to? Who can take the calf?” 

 
  
 
  
  
 
  
 
 
 
 
 
 
 
 
      
   
   
  
“Truth” and Bias 7 7 
The king is unable to provide a solution, and seeks in turn the council of the “clois-
tered lady” 28 to whom he repeats the tale verbatim. She is able to provide a solution, 
but it is at this point that both tablets are damaged, and the modern audience is left 
without closure. 
4.6.3 Ontological Representation 
Three existing ontologies were combined to capture this data, which contained 
some that was ancient, and some that was modern: the CIDOC Conceptual Refer -
ence Model (CIDOC CRM), 
29 a rather well-known ontology for cultural heritage 
data and object biography; FRBRoo, 30 a formal ontology for the representation of 
bibliographic information, speciﬁcally designed to merge with the CIDOC CRM 
and to thus facilitate the integration of museum and library data; and OntoMedia, 
the bespoke model that focuses on the representation of the narrative in multimedia 
and has similarly been designed as linkable to the CIDOC CRM.
31 
This approach resulted in an underlying interconnected graph structure, which 
could be used to capture the content of myriad other ancient inscriptions. If such 
a Linked Data project were created, it would enable queries that combine aspects 
of several diﬀerent types of data: the narrative content of the text (ancient data, 
incomplete and at times ambiguous, consistently unstructured), the metadata of 
the website that carries it (structured data, if not fully standardised), the associated 
bibliography of secondary sources (standardised bibliographic metadata), and the 
museological data relating to the witness tablets as physical objects in two separate 
collections in cultural heritage institutions residing on diﬀerent sides of the planet 
(similar, but with minor institutional diﬀ erences). An example of such a question 
could be: 
Show me all the inscriptions that are from the Old Babylonian period from 
the city of Nippur, and no larger than 15 cm in size, which have been acquisi-
tioned into collections in the USA, have been on loan to an exhibition in the 
UK, and contain a narrative element of a woman giving a man advice. that 
has been mentioned in two or more publications. 
Such a query would combine elements uniquely captured by each of the three 
ontologies. 
4.6.3.1 Material Objects in Museums 
Let us consider the rather more straightforward, tangible aspects of this heteroge-
neous data. The physical characteristics (object measurements) of the items that 
carry the cuneiform inscriptions (the clay tablets, pegs, cylinders, stamps, and so 
on) map to the existing Classes and properties of the CIDOC CRM with 
relative ease. 
32 In terms of objective truth, there is scope here for detailed data prov-
enance: the propertiesenable the user to specify which type of physical object 
was used to measure the ancient one. 33 In summary, the physical characteristics that 

 
 
 
 
  
  
     
  
 
     
      
   
 
  
  
 
 
 
 
  
 
 
 
     
 
  
 
   
 
      
    
78 “Truth” and Bias 
are captured in the object metadata categories, being of more recent origin than the 
inscription itself, are a clear ﬁt for the CIDOC CRM. 
But let’s push this into a more complicated space. The CIDOC CRM is an event-
based model. This means that, rather than a direct correlation between two things, 
they are connected through an event. For example, a mother and a child would be 
connected through the event of the birth. The crucial detail here is that the events 
in question are not ones from the narrative of the story. These are the remit of On-
tomedia; for CIDOC CRM, the events related to the cuneiform object would be the 
moment it was created by the ancient scribe, or the moment it was acquisitioned 
into a museum collection. Alas, the represented data was restricted to information 
which is available via Electronic Text Corpus of Sumerian Literature 
34 exclusively, 
and it does not contain information about either of those events. 
As well as being event-based, the CIDOC CRM is also a top-down or universal 
ontology. With this comes a greater degree of abstraction in the categorisation data, 
as each Classstrives to be non-speciﬁc enough to be relevant to several diﬀerent 
types of instance. Each text, for example, can also be mapped as an instance of 
E73 Information Object, which is conceptually separate from the physical 
tablet ( E84 Information carrier) that it is written on. The measurements 
are of the physical object, not of the text. Furthermore, as a nested subgroup of 
E24 Physical Man-Made object , E84 inherits the connection between 
E24and E90 Symbolic Object, o ﬀering an alternative way for representing 
the relationship between physical object and the text it carries. 
The beneﬁt of this abstract approach of connecting the physical object and the text 
(which nevertheless are seen as separate entities) is that attributes about each can also 
be easily declared. For example, the maker of the tablet might be a diﬀerent person to 
the composer of the text (imagine a scenario where a pre-shaped tablet is handed over 
to the scribe who proceeds to write something on it), or there may be things about the 
tablet biography that are separate from that particular inscription, as would be with 
the case of tablets where an initial inscription has been erased and another written 
over the top of it: the object would be the same, its measurements would be the same, 
but the text it carried on its surface would have changed to a completely diﬀerent one. 
The full representation of the object biography would thus include two separate but 
equally valid assertions about the text that the object carried. The only way to specify 
a sequence or diﬀerentiate them in time would be through the addition of often con-
textual information (e.g. a relationship in time using properties such as P173 
starts before or with the end of (ends after or with the
start of) and the Class E2 Temporal Entity. 
The process of mapping the concept of the text to the CIDOC CRM was rela-
tively straightforward as it was limited to a generic abstraction: it is an instance 
of F23 Expression Fragment , as well as that of E73 Information 
Object. This means it can be shown to have a language and the bidirectional 
relationship between translation and transliteration can be represented through the 
use of E33 Linguistic Object, E56 Language and P72 has lan-
guage.
35 At this level of complexity, we could facilitate a query that would, for 
example, ask the system to show tablets that were of a particular size, and carried 

 
 
  
 
  
        
   
 
     
    
   
 
 
 
 
 
   
 
 
  
 
  
  
  
   
      
        
“Truth” and Bias 7 9 
an inscription in a speciﬁed language. The query is simple at this stage because 
only one type of information has been captured in the ontology so far. 
4.6.3.2 Bibliographical Metadata 
To increase the complexity of the underlying ontological structure, and to thus 
facilitate a more complex query, we can add additional information about the an-
cient inscription. For example, the bibliographic data of secondary publications 
capturing six categories of information can be mapped using LRMoo. 
36 In the con-
text of the case study of representing Sumerian literature, the ontology of choice 
was FRBRoo, 37 which was connected to CIDOC CRM through the aforementioned 
Classes of E73 Information Object , of which F2 Expression is 
a subclass. FRBRoo has since been replaced by LRMoo, but the Classes and 
properties used in the project were from FRBRoo. These are described here. 
Modern scholars named in the bibliography can be mapped as instances of 
F10 Person , which is an equivalent of E21 in the CIDOC CRM: FRBRoo 
also includes F38 Character, which is deﬁned as referring to “ﬁctional and 
iconographic individuals . . . appearing in works in a way relevant as subjects. 
Characters may be purely ﬁctitious or based on real persons”. 
38 The abstraction 
here is key to its applicability to a wide spectrum of protagonists, it is equally 
valid for the unnamed characters (the slave-girl, the young scribe, the ox-driver) 
as it is to Gilgameš. Interestingly, doing so is in stark contrast to the classiﬁcations 
of modern narratologist, such as Propp and Campbell, who diﬀerentiate between 
the hero and the villain. The problem with their approach is that stories can have 
much greater narrative complexity than what this categorisation represents. Those 
complexities can include changes as part of character development: Gilgameš is an 
excellent example of this. Arguably the most well-known of Mesopotamian literary 
heroes, he is, depending on the composition, perspective of the audience, and sec-
tion with a piece, equally cast as either hero or villain, perhaps simultaneously both 
and thus by logical deduction neither. A semi-mythical demigod possibly originally 
based around the personal cult of a real person, the story of the Epic of Gilgameš 
(for a translation, see George, 1999 ) is (at least partly) one of redemption through 
personal growth: at the beginning, he is a monster, a tyrant, a rapist (exercising 
jus primae noctis) whom his people beg the gods to destroy – at the end, he is the 
champion of mortality, a forlorn lover perhaps. How then are we to categorise him? 
Abstraction and lack of value judgement based on modern-day perspectives and 
loaded terminologies (a hero being good, a villain being bad) makes F38 the ideal 
Class for representing even protagonists as complicated as Gilgameš. 
4.6.3.3 Narrative Structure 
The content of the inscription cannot be mapped to either CIDOC CRM 
nor FRBRoo, but the OntoMedia ontology has several relevant Classes 
and properties. The three men (Man
1, Man 2 and Man 3) are all repre-
sented as om:Characters who are Gender:Male.39 Each also has an 

 
         
       
 
   
     
 
    
      
  
       
   
    
 
  
   
    
  
      
    
         
     
 
  
 
 
 
 
 
 
 
 
 
 
  
 
     
80 “Truth” and Bias 
om:Possession: for Man 1 it is an instance of om:Ox; for Man 2 an entity in 
the class om:Cow; for Man 3, it is a Physical:Item (string:“wagon”). It is 
even possible to capture the giš determinative of the Sumerian ( gišmar), show-
ing this physical item is made of om:Material (string: “wood”). Each has 
a Profession:Rural, which is suﬃciently abstract to avoid any modern 
connotations of divisions into speciﬁc agricultural roles. The men are con-
nected to each other via an Alliance:Friendship. They also have an 
om:Alliance to the king, as well as being citizens of an om:City (Adab). 
The men together are an instance of an om:Group. The king is also an instance 
of om:Character with Gender:Male. He has a Profession:Ruler 
and has an om:Alliance to Adab. The cloistered lady is an  om:Character 
with Gender:Female. This adherence to the gender binary reﬂects neither an 
exclusively modern categorisation nor a dismissal of a potentially more diverse 
gender spectrum of antiquity, but reﬂects a very literal description of the men 
(with the word lu
2, and for the king, lugal) and of the “cloistered woman”. 40 
The interactions between instances of the om:Character are repre-
sented through a series of om:Events, which occur across a number of 
om:Timelines in two separate om:Contexts. These include Gaining
Bond:Enmity for each other (the quarrel); om:Travelbetween two unknown 
om:Locations; om:Ox engaging in Action:Sex with the om:Cow; the 
om:Bovine (young)engages in om:Consumeof the wagon’s load, which is 
a Physical:item. 
Almost all of the diﬀerent elements of the story can thus be mapped individually 
to the OntoMedia ontology, proving the universal nature of that upper-level ontol-
ogy. It shows that it is possible to map all kinds of ﬁctional narratives. It also speaks 
signiﬁcant volumes as to the universal nature of storytelling, and thus of shared 
human experience across cultural boundaries. There is but little in terms of dif-
ferences and diversity in the ways members of the human species experience and 
understand the world. Even when separated by thousands of millennia and miles, 
the topics and motifs that occur in stories are universal. What this mapping shows 
is that abstract concepts can be deﬁned in ways that ensure that moral, ethical, and 
social judgements are excluded from the process of ontological modelling. 
Where the OntoMedia ontology fails to adequately capture the narrative ele-
ments of the ancient inscription is in the granularity of mapping diﬀerent types 
of dialogue. This is a fundamental part of the tradition of the so-called Wisdom 
Literature genre in Sumerian literature; it consists of dialogues, diatribes, debate 
poems, proverb collections, and so forth. Given this is an entire genre of literature, 
a specialist ontology would be needed to adequately capture the taxonomy of types 
of dialogue. 
There are two potential challenges to developing such an ontology: ﬁrst, it is 
possible that the categories might be too speciﬁc to Sumerian literary categories, 
and the model would not be of use to any other types of compositions, potentially 
resulting in information siloing when no other datasets in RDF share the same 
Classesor properties; second, and much more importantly in terms of this 
chapter in particular, is that in doing so we might be inadvertently perpetuating 

 
  
 
 
  
 
 
  
         
  
 
 
 
 
 
 
  
 
 
 
      
  
“Truth” and Bias 8 1 
modern categorisations of ancient literature, which would have seemed alien and 
nonsensical to the ancient scribes writing them. 
But is this a problem of technology? Not exclusively! It is a challenge presented 
by computational tools. In other words, it is a challenge of the Humanities, both 
traditional and Digital. In fact, Ebeling (2007 : ﬀ33) has already noted this exact 
problem, saying the classiﬁcation of literary compositions is a modern convention, 
and there are but a few indicators that would support any theory that the people of 
ancient Mesopotamia thought of the varied collections of mythological and histori-
cal narratives, royal praise poetry, hymns, and proverbs as one cohesive unit. Even 
drawing a deﬁning line between literary (ﬁction-based) and historical (fact-based) 
pieces is complicated – examples of the latter (written regarding people who are 
known to have existed) can contain seemingly ﬁctional elements; consider, for ex-
ample, Šulgi (a genuine historical person, and a king of the Ur III dynasty) claim-
ing Gilgameš as his brother ( Taylor, 2013 : 301). Another similar example is the 
role of the ox-drivers. In this inscription, the three men are described exclusively 
in terms of the things they possess: one owns an ox (gud lu 
2 diš-a-kam), the other a 
cow (ab 2 lu2 diš-a-kam), the third a wooden cart ( jišmar lu 2 diš-a-kam).41 But could 
we refer unambiguously to these men as agriculturists, or farmers? Not necessarily, 
as doing so would risk making inherent assumptions about the division of roles and 
labels to members of bygone societies and civilisations for which we have insuf-
ﬁcient evidence to either conﬁrm or deny. 
And perhaps it is here that it is a good time to stop and think about just how 
deep-routed biases are. If we have to be reminded of diﬀerent ways of understand-
ing personhood, what else might we take for granted in database and information 
representation designs? 
4.7 Conclusion 
The information structures and computational technologies developed in Silicon 
Valley have been criticised for their lack of consideration of cultural, linguistic, 
ethnic, and economic diversity. As driving forces behind the development, the oli-
gopolies of computational technology have aﬀected information representation in 
modern society. Reductionist technologies have sought to eliminate diversity and 
ambiguity (rather than capture it) for the sake of quick and eﬃcient development, 
and have failed to adequately represent the global population. Tasks as seemingly 
simple as adequately and appropriately, as well as respectfully representing the 
name of an individual are complicated or even prevented by database structures. 
Western perspectives have permeated almost every aspect of information capture, 
representation, and analysis. From Linnaean taxonomy to Google search results, 
the Western ways of categorising the world have become the only acceptable voice 
of authority. 
The case study data, which is the narrative content of an ancient inscription (the 
fabula as the events of the story in chronological order and the syuzhet as the actual 
employment of the narrative, which included narrative devices such as focalised 
analepsis or ﬂashbacks, as told from the perspective of a protagonist in the story), 

 
  
 
 
 
 
 
 
 
 
 
 
 
  
   
 
     
    
82 “Truth” and Bias 
is an example of unstructured data. The broken witness tablets 42 are tangible and 
physical proof of this being a case of incomplete data, and the uncertainties of the 
translation of the words in the text a manifestation of ambiguity and uncertainty in 
and about the data. 
Having established the basics of the Linked Data publication paradigm in the 
context of the Digital Humanities ( Chapter 1 ), and given consideration to the ways 
in which issues of privacy should be taken into account when applying this meth-
odology ( Chapter 2 ), and with the wisdom of a case study example of the eﬀects of 
institutional policy ( Chapter 3 ), attention turned to the consideration of how social, 
personal, and cultural perspectives can aﬀect the implementation of Linked Data. 
In the next two chapters, discussion will focus on the way inherent biases (such as 
the moral and ethical values of modern society) can and do manifest in the devel-
opment of ontologies and thus the implementation of the Linked Data paradigm as 
a whole. 
In the context of the Semantic Web and the Linked Data publication paradigm, 
ontologies are less to do with the philosophical categorisation and representation 
of truth, and more to do with the explicit articulation, in a machine-readable for -
mat, of the data entities and the relationships between them that occur in a given 
dataset. But how do we decide what constitutes a data entity, and how do we know 
which relationships to map? This is all part of a lengthy design decision process, 
one which is often quite poorly documented. The way the Universe and reality are 
perceived can and do inﬂuence ontology development. 
The risk of presentism as it is understood in historical analy sis on knowledge 
representation was the focus of this chapter. Discussion has ce ntred on the risk of 
introducing anachronistic present day values, knowledge, ideas, and perspectives 
into the capturing of what is intended to be timeless truths and facts about a dataset. 
The concept is not pushed all the way to philosophical presentism, which is the view 
that neither the future nor the past exists, but to the recognition that the ontological 
representation of data in the Linked Data paradigm is one of a snap-shot in time. 
We can illustrate these ideas in a clear way by opting to focus on the challenges 
of applying modern technologies to historical and ancient world data. The software 
and informational representation tools available today are created with the expecta-
tion that they will be used to complete datasets, created from an omniscient perspec-
tive. Furthermore, they are designed to represent the modern day understanding of 
the world. This chapter posed the question: “How well do these modern technolo-
gies lend themselves to unbiased examinations and representations of the past?” 
Perhaps the right question to ask should have been: “How well d o these modern 
scholars lend themselves to unbiased examinations and representations of the past?” 
Notes 
1 I refer to the term “meme” speciﬁcally and exclusively as it is understood in Internet 
culture, as a concept or repurposed image that is spread from one user to another across 
social media platforms, email, and other content. 
2 https://paulspurpose.com/2017/11/08/69/. Accessed 07/04/2022. 

    
     
     
     
    
 
 
 
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
     
 
 
 
    
 
    
 
 
 
    
“Truth” and Bias 8 3 
3 www.cidoc-crm.org/. Accessed 27/05/2022. 
4 https://cidoc-crm.org/Resources/crmdigital-v3.2-an-extension-of-cidoc-crm-to-
support-provenance-metadata. Accessed 30/01/2023. 
5 https://cidoc-crm.org/crmsoc/Resources/crmsoc-a-cidoc-crm-extension-for-social-
phenomena. Accessed 30/01/2023. 
6 https://linked.art/model/proﬁle/. Accessed 26/01/2023. 
7 Some of the big players in the current Tech-Meets-Data-Economy landscape do re-
ﬂect a more diverse demography (Hewlett Packard with CEO Enrique Lores; Alpha-
bet, and its subsidiary Google, with Sundar Pichai; and Shantanu Narayen at Adobe 
Systems). 
8 By “beauty” I don’t just mean an aesthetic value of a thing or person, but the criteria 
that is applied to success. Their ideas for the correct thing, the right thing, the right and 
correct way of categorising the world. 
9 www.theguardian.com/commentisfree/2021/apr/03/why-silicon-valley-most-astute-
critics-women-tech-gender. Accessed 15/06/2021. 
10 www.cidoc-crm.org/. Accessed 11/06/2021. 
11 https://cidoc-crm.org/frbroo/ModelVersion/lrmoo-f.k.a.-frbroo-v.0.6. Accessed 30/01/2023. 
12 http://musicontology.com/. Accessed 11/06/2021. 
13 http://motools.sourceforge.net/event/event.html. Accessed 11/06/2021. 
14 www.w3.org/TR/prov-o/. Accessed 11/06/2021. 
15 www.w3.org/TR/rdf-schema/. Accessed 11/06/2021. 
16 www.w3.org/OWL/. Accessed 11/06/2021. 
17 https://id.loc.gov/ontologies/madsrdf/v1.html. Accessed 11/06/2021. 
18 https://id.loc.gov/ontologies/bibframe.html. Accessed 11/06/2021. 
19 www.semanticdesktop.org/ontologies/2007/03/22/nco/#Gender. Accessed 11/06/2021. 
20 http://xmlns.com/foaf/spec/. Accessed 11/06/2021. 
21 http://xmlns.com/foaf/spec/#term_gender. Accessed 11/06/2021. 
22 https://homosaurus.org/. Accessed 11/06/2021. 
23 The collection of written works that are classiﬁed as “Sumerian literature” (a term where 
both words could justify a discussion) consist of an eclectic mix of compositions written 
for myriad socio-political and cultural reasons. They share a number of characteristics, 
such as a narrative arc, or the capture of a verbal exchange between two or more entities. 
These texts undeniably have some non-pragmatic purpose – they are not lists, nor glos-
saries, nor recordings of units of agricultural produce, but rather the product of creative 
and artistic minds. Furthermore, they are classiﬁed by Black and Zólyomi (2007: 3) as 
consisting of exemplar texts which were, in antiquity, produced (and survive) in mul-
tiple versions – Ebeling (2007 : 33) agrees, elaborating on their universal nature. Many 
of the compositions in the online resource the Electronic Text Corpus of Sumerian Lit-
erature, and are also listed in ancient catalogues ( Ebeling, 2007 : 34). These texts played 
an important role in scribal education, not only as a vehicle for learning the cuneiform 
script, but also to teach the moral, cultural, historical and social values of their society 
( Taylor, 2013 ). 
24 These texts are thought to be composed by scribes whose native tongue was Akkadian, 
and so “Sumerian” can only be applied conﬁdently as a linguistic label, with no implica-
tion as to the cultural or social identity of the authoring scribe or the commissioner of the 
text (Brisch, 2013). 
25 The composition (which, like most of ancient Mesopotamian compositions is named 
after the ﬁrst line rather than by some other, more abstract or protagonist-driven name) 
has a total length of 95 lines, but it is only the ﬁrst third that survives to any considerable 
extent, with the majority of content missing from line 30 onwards, and the ﬁnal third of 
the composition is riddled with gaps. 
26 Only two tablets carrying the text are known. There appears to be no known prov-
enance for either tablet – the secondary authors have made little comment on possible 

 
 
    
    
    
      
     
 
 
        
    
    
 
    
      
  
     
    
      
 
         
        
 
    
 
     
 
    
 
  
 
   
84 “Truth” and Bias 
geographical origin or ﬁnd spot for either witness, except to say none is known for the 
Louvre fragments ( Alster, 1991 –1993: 27). All of these features greatly complicate the 
process of unambiguously and explicitly mapping all the relevant data to an ontological 
structure. 
27 https://etcsl.orinst.ox.ac.uk/section5/tr565.htm. Accessed 09/06/2021. 
28 Akkadian “sekrum”, a somewhat ambiguous term for a female of the royal household 
who may or may not have had a cult or religious role. 
29 www.cidoc-crm.org/version/version-7.1.1. Accessed 09/06/2021. 
30 http://new.cidoc-crm.org/frbroo/ModelVersion/frbroo-v.-2.4. Accessed 10/06/2021. 
February 2020 saw the replacement of FRBRoo with LRMoo (https://cidoc-crm.org/ 
frbroo/ModelVersion/lrmoo-f.k.a.-frbroo-v.0.6. Accessed 30/01/2023), but the ontology 
used in this project was the FRBRoo. 
31 www.semanticscholar.org/paper/OntoMedia%3A-An-Ontology-for-the-Representa-
tion-of-Jewell-Lawrence/c8e6add16ad6efd76ca13135c5fcf808f73cf3c5. Accessed 
24/01/2023. 
32 These include the objects measurements E16 Measurement and P39 measured 
(was measured by)and P40 observed dimension (was observed in). 
33 How often this information is provided in a collections database, well, I remain scepti-
cal, but the point is that ontologically speaking, the representation  is possible. 
34 https://etcsl.orinst.ox.ac.uk/index1.htm. Accessed 09/06/2021. 
35 The concepts here are suﬃciently abstract not to cause a risk of presentivist interpreta-
tions. We know that the concept of language, for example, was one that was clearly 
attested in Sumerian records (eme-gir). Similarly, abstract nouns and concepts were 
clearly part of the Sumerian world view, as attested by the use of the preﬁx -nam, which 
turns concrete nouns into abstract ones. 
36 https://cidoc-crm.org/frbroo/ModelVersion/lrmoo-f.k.a.-frbroo-v.0.6. Accessed 30/01/2023. 
37 www.cidoc-crm.org/frbroo/home-0. Accessed 24/08/2021. 
38 On p. 65 of the scope notes for the FRBRoo, available at http://new.cidoc-crm.org/ 
frbroo/sites/default/ﬁles/FRBRoo_V2.4.pdf . Accessed 10/06/2021. 
39 Although OntoMedia would allow for a more detailed speciﬁcation of om:Sex (Be-
havioural, Genetic, Gonadal and Phenotypic), since these details are not 
clear, nor provable from the context of the story, the diﬀerentiation is not made here. 
40 Translated in the Electronic Pennsylvania Sumerian Dictionary as a term referring ex-
clusively to women. See http://psd.museum.upenn.edu/nepsd-frame.html . Accessed 
10/06/2021. 
41 Available at https://etcsl.orinst.ox.ac.uk/section5/c565.htm . Accessed 09/06/2021. The 
translation is available at https://etcsl.orinst.ox.ac.uk/section5/tr565.htm . Accessed 
09/06/2021. 
42 This example is one that also strongly supports the need to engage with primary source 
material in the original language, rather than through translation – a point of debate 
amongst some in the Digital Humanities. 
Bibliography 
Allemang, D., and Hendler, J. (2011). Semantic Web for the Working Ontologist: Eﬀective 
Modeling in RDFS and OWL. Elsevier. 
Alster, B. (1991–93). “The Three Ox-Drivers from Adab”. Journal of Cuneiform Studies , 
43–45, pp. 27–38. 
Black, J. and Zólyomi, G (2007) “Introduction to the study of Sumerian”. In Ebeling, J. and 
Cunningham, G. (eds) Analysing Literary Sumerian Corpusbased Approaches, Equinox 
Publishing Ltd. 

  
 
   
  
   
 
 
 
  
 
   
 
  
  
 
   
    
 
  
  
 
  
  
 
   
 
  
 
 
 
  
  
 
  
 
  
  
 
 
 
 
“Truth” and Bias 8 5 
Brewster, C., and O’Hara, K. (2004). “Knowledge Representation with Ontologies: The 
Present and Future”. IEEE Intelligent Systems, 19(1), pp. 72–81. 
Brisch, N. (2013). “History and chronology”. In Crawford, H. (ed). The Sumerian World, 
Routledge. 
Campbell, J. (2008). The Hero With a Thousand Faces (V ol. 17). New World Library. 
DuCharme, B. (2013). Learning SP ARQL: Querying and Updating With SP ARQL 1.1 . 
O’Reilly Media, Inc. 
Ebeling, J. (2007). “Corpora, Corpus Linguistics and the Electronic Text Corpus of Sumer-
ian Literature”. In Ebeling, J., and Cunningham, G. (eds). Analysing Literary Sumerian 
Corpus-based Approaches, 33–50. Equinox. 
Foster, B. R. (1974). “Humor and Cuneiform Literature”. Journal of Ancient Near Eastern 
Studies 6, pp. 69–85. 
Gadotti, A. (2014). “Sumerian Wisdom Literature”. In Chavalas, M. (ed). Women in the 
Ancient Near East. Routledge. 
Geertz, C. (1973). The Interpretation of Cultures. Basic Books, Inc. 
George, A. (1999). The Epic of Gilgamesh: The Babylonian Epic Poem and Other Texts in 
Akkadian and Sumerian. Penguin Books. 
Grant, K. (2022). Landscape and the Arts in Early Modern Italy . Amsterdam University 
Press. 
Gruber, T. R.(1993). “A Translation Approach to Portable Ontology Speciﬁcations”. Knowl-
edge Acquisition, 5(2), pp. 199–220. 
Hyvönen, E. (2018). Semanttinen Web: Linkitetyn Avoimen Datan Käsikirja. Gaudeamus. 
Kranzberg, M. (1986). “Technology and History: ‘Kranzberg’s Laws’”. Technology and 
Culture, 27(3), pp. 544–560. 
Lambert, W. G. (1995). “A Note on the Three Ox-Drivers from Adab”.  NABU, 2, pp. 1–2. 
Nurmikko-Fuller, T. (2014). “Assessing the Suitability of Existing OWL Ontologies for 
the Representation of Narrative Structures in Sumerian Literature”. Current Practice in 
Linked Open Data for the Ancient World, ISAW Papers, 7. http://dlib.nyu.edu/awdl/isaw/ 
isaw-papers/7/nurmikko-fuller/ 
Nurmikko-Fuller, T. (2018). “Publishing Sumerian Literature on the Semantic Web”. In Ju-
loux, V ., Gansell, A., and Di Ludovico, A. (eds). CyberResearch on the Ancient Near East 
and Neighboring Regions. Brill. 
Nurmikko-Fuller, T. (2022). “Teaching Linked Open Data Using Bibliographic Metadata”. 
Journal of Open Humanities Data, 8. 
Pratchett, T., and Gaiman, N. (1990). Good Omens: The Nice and Accurate Prophecies of 
Agnes Nutter, Witch: A Novel. Victor Gollancz Ltd. 
Propp, V . (1968).  Morphology of the Folktale, 2nd ed. University of Texas Press. 
Taylor, J. (2013). “Administrators and Scholars: The First Scribes”. In Crawford, H. (ed). 
The Sumerian World. Routledge. 
Wilks, Y ., and Brewster, C. (2009). Natural Language Processing as a Foundation of the 
Semantic Web. Now Publishers Inc. 
Witteveen, J., and Müller-Wille, S. (2020). “Of Elephants and Errors: Naming and Identity 
in Linnaean Taxonomy”.  History and Philosophy of the Life Sciences, 42(4), 1–34. 

 
 
 
   
 
 
 
  
 
 
 
 
   5 Data Demands 
5.1 Preamble 
“The Man Who Mistook His Wife for a Hat” ( Sacks, 1985 ) is a collection of patient 
stories compiled by a neurologist, each chapter telling the tale of one condition or 
another, and the ways in which it aﬀected the patient. These cases include The Lost 
Mariner, who is incapable of forming new memories and indeed believes himself 
to be several decades younger than he is; and, The Disembodied Lady, a largely 
unique case of “a strapping young woman of twenty-seven, given to hockey and 
riding, self-assured, robust, in body and mind. She had two young children, and 
worked as a computer programmer at home” (ibid.: 26), who lost control of her 
body. The eponymous patient is a musical genius referred to as “Dr P”: he has lost 
the ability to identify things that he sees (although sounds he hears are obvious to 
him). His condition means that he cannot recognise people by their faces, and, in-
stead, sees what his brain interprets as human faces in what turn out to be inanimate 
objects, such as ﬁre hydrants, and furniture. And yes, he does, in fact, according to 
Sacks, at one time literally mistake his wife’s head for a hat. 
Although some of the analysis and hypotheses are dated (the Disembodied Lady 
is initially diagnosed/dismissed as being “hysterical”), these stories provide an in-
sight into the complexities of the human brain. They show us, especially through 
the mistakes, something of how information is categorised in our brains. The dis-
crepancy (the deviation from what we perceive as “normal” cognition) between 
reality as perceived by others (the hat) and the alternative assessment of the situ-
ation (looking at his wife but his brain processing that to be the hat) are almost 
comical, absurd, and satirical. But what is this, but a conﬂict between one way of 
understanding reality, and another? 
The parallels between the human brain and computation have in one form or 
another been part of research discourse around the various takes on the Mind-Body 
problem for over two millennia. The ideas of Plato and Aristotle (some 5th–4th 
centuries BCE) are predated by those in Buddhist thought from around 500 BC. 
In the West, the ideas of Descartes, Kant, Huxley, and Searle continue to inﬂuence 
our thinking. The history of artiﬁcial intelligence is littered with attempts to recre-
ate human cognition as a process. We might look to researchers such as Miller, 
Chompsky, or Pinker, and mull over the ideas of learning about human cognition 
DOI: 10.4324/9781003197898-5 

 
  
 
 
 
   
  
 
  
 
 
   
 
 
   
 
 
  
 
  
  
 
 
 
 
 
 
Data Demands 8 7 
through the process of computational modelling. But, what of a somewhat diﬀerent 
approach? Not one of mimicking the process, but technology as contributing to it? 
Enter Clark and Chalmers (1998 ) and the Extended Mind thesis: to summarise its 
main elements, Clark and Chalmers put forth the idea that technology that exists 
outside of the human mind can be used to extend it, and to support cognitive pro-
cesses such as memory. Their thought experiment is a comparison between Otto 
and Inga, both on their way to the museum. Inga can remember the route (the 
cognitive processes of determining the geospatial coordinates of the ﬁnal stop and 
calculating the optimal route there all occur in her mind or in her brain). Otto, on 
the other hand, has Alzheimer’s and relies on a notepad for the same information. 
In his TED Talk in 2011, 
1 Chalmers declares that digital technologies such as iP-
hone (his speciﬁc example) have ampliﬁed the potential of technology to comple-
ment and even overtake cognitive processes. These devices now complete processes 
that the biological brain used to perform: tasks such as memory (phone numbers 
in Contacts), planning (iCalendar), spatial navigation (Google Maps), desires (via 
an app that retains favourite recipes in a restaurant), and even (although the point 
is made a bit facetiously) decision-making. The popularity of these computers also 
means that the thesis is now much more compelling to a larger number of people, 
who can readily identify with these examples. For the purposes of this chapter that 
focuses on information structuring and preservation, and this book, which looks at 
how Linked Data can be used to infer new knowledge, this rings particularly true 
in two diﬀerent ways: ﬁrstly, databases as memory, and secondly, computational 
tools and methods for speeding up the retrieval of very speciﬁc data snippets (an 
information retrieval task) so that the uniquely human processes of thinking and 
interpretation can be utilised to their greatest eﬀect. In other words, the Extended 
Mind thesis rings true because digital and computational tools are there to store 
information that we can later retrieve or access; ﬁltering through results can help 
us pinpoint relevant data for analysis; but, at the core of it all is human cognition, 
doing something unique in terms of judgement and analysis. 
Given then that museums (and institutions of the other designations in the 
GLAM acronym)
2 of diﬀerent designations and locations (also referred to as 
“memory institutions”!) contain such diﬀerent types of collections retaining very 
diﬀerent kinds of information, is it even possible to develop a database that could 
faithfully represent the information held in all of them? And, is this a uniquely 
technology driven demand? 
If information was the sole responsibility of an individual, would one expect (or 
want) a fully unbiased account? Or, would one expect and even cherish the individual 
slant the information custodian would put on the knowledge that had been passed on 
to them by generations of predecessors? Would we not expect the human mind to 
reinterpret and reapply the knowledge of the past into a present situation, to make 
meaning of tradition and reinterpret that information in the context of the modern 
world? But, when it comes to databases, does the same ﬂexibility apply? Our de-
mands are surely the opposite, with expectations of a pristine preservation of all the 
information, in an immutable fashion. Is that not the ultimate evidence to suggest that 
we expect from our digital databases the objectivity of timeless omniscience? 

 
    
  
 
   
 
  
 
   
 
  
 
 
  
 
  
 
 
 
   
 
  
88 Data Demands 
5.2 The More Things Change 
In April 3 2022, whilst searching for something completely unrelated – a bureau-
cratic document, misplaced – I stumbled upon an email thread from 2011. This 
thread of no fewer than 68 emails (with an additional spin oﬀ thread of eight ad-
ditional ones) was the Museums Computer Group mailing list, and had attempted 
to answer the question “What would an open source museum CMS look like?”. 
A fascinating, and seemingly timeless topic. A rudimentary text analysis high-
lighted a few key issues: the most frequently occurring words reﬂected a discussion 
further down the thread as to whether the acronym “CMS” referred to a “content 
management system” or a “collections management system” – how appropriate 
for this particular list! And yet, there is a note of irony here, given I’ve chosen to 
mention it in a chapter about knowledge representation: the criteria of a collection 
management system for a museum are signiﬁcantly diﬀerent from a content man-
agement system that sits behind a website. Beyond those obvious terms, the words 
that cropped up most frequently were “data”, “open”, “web”. What is less obvious 
from the topic modelling but clear in the thread is that at that point in time, a dec-
ade ago, the tech du jour was Drupal, with most early contributors to the thread 
discussing it and its relative pros and cons. WordPress is mentioned exactly the 
same number of times, but appears in the thread as a new and emerging option. 
Linked Data is mentioned a handful of times, each time as a new or even “future” 
technology. 
The debate between Drupal and WordPress is not what makes this thread an 
evergreen classic: it is old hat. But, from the beginning, there are a number of 
comments and observations from this Special Interest Community (SIG) that still 
remain a matter of debate: “As much as museums look similar, each believes itself 
to be unique ” is surely an axiom of the GLAM sector; “[in museums] you have 
objects, interpretations and metadata”; and “all museums . . . have distinctive col-
lections, brands and so on, but once you strip this away pretty much every mu-
seum website, large or small has the same core functions”. Perry Bonewell (Bolton 
Council, UK) makes a poignant comment: 
It is often not the system per se an institution uses but the way it is used that 
causes many of the problems; things like system/s implementation and devel-
opment, basic and advanced documentation practice and a rudimentary under-
standing of the learnt skills involved in knowledge organisation, data quality 
control, user attitude and support, institutional attitude and resource etc. Many 
cultural institutions simply do not have . . . the resources to do something that 
is quite complex well enough to get the outcomes they need/demand. 
And so we encounter the absence of neutrality in technology, harking back to 
Kranzberg’s law
4 from Chapter 4 . The ways in which information is captured in 
these databases is a reﬂection of someone’s reality (or indeed that of many people), 
sometimes deﬁned as being diﬀerent from something similar by virtue of minutiae. 
Museums with very similar collections will insist on some unique aspect: we might 
say that it equates to an idea where one museum insists on being the keeper of hats, 

 
 
 
 
  
 
  
 
  
  
 
  
 
  
Data Demands 8 9 
the other of caps, and both unilaterally reject the possibility of using a database 
that was designed to capture metadata for headwear. The challenges arise most 
predominantly if we are to propose a diﬀerent categorisation altogether. It is dif-
ﬁcult to come up with a meaningful example because this deviation from standard 
categorisation in information structuring comes across as absurd. If it was a person, 
we might call it madness. If there are museums where the collection is entirely 
based on a colour, for example, or on the tactile sensation of softness or the sense 
of something evaporating, they are surely minor and considered to be niche or 
quirky. And, even if we were to focus our thought experiment on a tangible object, 
museum databases are rarely designed to collect anything akin to memories of the 
emotional responses users had when the object was in use, or the things that we 
think of as being one or more degrees of separation away from the object itself. 
For example, the metadata record for a yellow teacup is unlikely to record that it 
was half of a pair that didn’t match in colour or shape or design but were forever 
designated “a pair” because they were gifted by a colleague at the same time. That 
is not to say that these characteristics couldn’t be used to create collections, nor 
that they don’t add to the rich biography of the object. And, a s human beings we 
collect objects for their intangible and tacit qualities quite readily. Consider a col-
lection of CDs or vinyl, for example, all from diﬀerent artists but ﬁnely curated to 
suit the eclectic and speciﬁc tastes of one person. So if we can readily accept col-
lecting diﬀerent kinds of things, objects, items, why do we struggle with the idea of 
collecting diﬀerent kinds of information about things? And what determines what 
information we do collect about things? And why do we categorise things the way 
that we do? 
Cultural and idiosyncratic understandings might well determine the categories 
in which we slot things in our understanding, but where (and when!) does the idea 
of systematically organising information in this way originate from? In our 2021 
paper, Paul Pickering and I referred back to the thoughts of Vannevar Bush in his 
design of the Memex, but I provide the longer quote here as it clearly illustrates the 
connection to thinking about the GLAM sector in particular: 
Our ineptitude in getting at the record is largely caused by the artiﬁciality 
of systems of indexing. When data of any sort are placed in storage, they 
are ﬁled alphabetically or numerically, and information is found (when it is) 
by tracing it down from subclass to subclass . . . one has to have rules as to 
which path will locate it, and the rules are cumbersome. . . The human mind 
does not work that way. It operates by association. With one item in its grasp, 
it snaps instantly to the next that is suggested by the association of thoughts, 
in accordance with some intricate web of trails. 
Aren’t graph databases and triplestored of Linked Data a much better ﬁt for 
some interconnected thinking? They have immense potential to be used for a much 
more faithful mapping of the cognitive processes of scholars into the digital realm. 
This idea is echoed strongly by Simpson (2020) “graph-based hypertext . . . pro-
vided a better way of representing the interconnected way in which I thought and 
worked”.
5 

 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
 
 
90 Data Demands 
So let’s assume we’re now sold on the idea of Linked Data. Where next? What 
do we do, and where do we start? The truth is there are as many diﬀerent work-
ﬂows for Linked Data production, and everyone has their own favourite, based on 
what they know, what skills they have, and what approach best matches with their 
desired research outputs and agendas. Some tools work better with diﬀerent data 
formats, and there is always a decision to be made as to where along the way is 
the most costly investment – that of human time and eﬀort – to be made. All these 
considerations aﬀect the recommendations we make. 
5.3 Bias in Tool Recommendations 
One of the most frequently asked recommendations is for software. “Which tool 
should I use?”, “What programming language should I learn?”, “What’s the best 
database?”. For a beginner, perhaps a student or academic looking to start their ﬁrst 
project, these probably seem like entirely reasonable questions . The problem here 
is, they are in many ways unanswerable. Or, to put it another way, the only truthful 
and accurate response can only ever be the somewhat unspeciﬁc and undoubtedly 
frustrating “It depends”. 
Many if not most will make recommendations based on their experiences 
of both using and teaching the use of various software tools (I did so myself in 
Nurmikko-Fuller, 2022 ). The trick here is though that these recommendations are 
based entirely and subjectively on personal experience, which, in turn, has histori-
cally been inﬂuenced by several external factors, such as the parameters of prior 
projects that required the use of a particular tool. In some cases, projects may run 
snippets of code that were initially developed as an ad hoc solution to a speciﬁ  c 
problem within a limited time frame in some completely diﬀerent context. The 
issue to be aware of here is that, once the time and eﬀort has been invested into 
learning a speciﬁc tool or piece of software, the bar for reusing that tool is low, 
even if it is not the “best” tool, platform, or software out there. In situations where 
researchers experience additional demands on their time means they are less likely 
to be able to dedicate time to extensively evaluate new tools. It is easy to resort 
to using a tool or engaging in a workﬂow that is already familiar, as long as it is 
good enough even if it is not an ideal match with the project skills, data, or even 
the research aims. 
To return to the notion of “best” with regard to any equipment, tool, or meth-
odology, the challenge here is that, no matter how useful that might be, there is no 
universal standard or criteria for assessing the inherent “betterness” of one tool 
over another. Would it not be best to avoid such hopelessly subjective terminology 
(the other great oﬀenders are “easy” and “simple”, and for very much the same rea-
sons)? The choice of tool, programming language, and digital infrastructure are all 
entirely dependent on factors such as the skills, ambitions, aims, and agenda of the 
researcher, as well the requirements of the data, and other external factors such as 
institutional policy (for example regarding Open Data), existing technical support 
at the institution (if any!), the budget, the size of the research cluster, and so on. 
The “best” tool in one context can be woefully inadequate in another; researchers 

   
 
  
 
 
 
  
 
   
   
  
 
  
 
 
 
 
 
 
 
 
 
 
 
 
Data Demands 9 1 
prefer to invest human time at diﬀerent points in the workﬂow; and ﬁnding an op-
tion that can be managed, used, and supported by the investigatory team is rarely 
a trivial task. 
To make the argument less abstract, we can consider the issue of databases. The 
division by Seth van Hooland and Ruben Verborgh (2014 : 16) of databases into 
four categories is compelling and is applied here too: (i) tabular data, (ii) relational 
model, (iii) meta-MarkUp languages, and (iv) RDF (although much of what is said 
here could also apply to other graph databases). For a researcher wanting to start 
a new project, which approach should they take? The question may seem absurd 
in its reductiveness and simplicity – how could we possibly answer that without 
knowing more? But this is often the ﬁrst step for novice researchers, and a genuine 
question. The issue here is that the question itself needs to be broken down to a 
greater level of granularity, and, we need to recognise two crucial aspects: ﬁrst, 
that the process of creating digital projects is often reiterative, and may require the 
use of diﬀerent tools at diﬀerent stages; and second (and this is often an overlooked 
aspect), these tools are not in any way whatsoever mutually exclusive, and can and 
do often get used together. 
In the context of a Linked Data project, such as JazzCats (as discussed in the 
context of diﬀerent data structures in Chapter 5 ) or the ElePHãT project (please see 
Chapter 3 for the description of this project and the eﬀect of institutional policies), 
many of all of these information structures are used either concurrently, or as part 
of one cohesive workﬂow. One possible Linked Data workﬂow for the production 
of instance-level RDF that makes use of these technologies has been reported on 
elsewhere ( Nurmikko-Fuller, 2022 ). 
The desire to pick the “best” tool is entirely reasonable (any thing else would 
be baﬄing, a deliberate decision to opt for the suboptimal?), but t he problem is 
that the question itself lacks subtlety and nuance. A more appr opriate question 
might be along the lines of “What are the aspects of my project that should be 
considered when designing the workﬂow?”, and as a follow up “How can the tool 
or piece of software that is most suitable for each separate stage of the workﬂ  ow 
be determined?”. The answer is determined by the answers to the long litany of 
considerations outlined earlier – each is a factor for determin ing the choice of 
tool. The reason this is not always given as the answer is often twofold: ﬁrst, there 
is a fear that such an answer is unwelcome (we live in times of a surplus of easy 
answers and of instant gratiﬁcation after all); second, the practitioner being con-
sulted may feel that failure to name a speciﬁc tool implies a lack of expertise on 
their part – an irony, given the opposite is likely. There is a third option as well, 
which is that having invested considerable time, energy, and eﬀ ort to master the 
use of one particular tool or method, we may be reluctant to consider the possi-
bility that it is not the perfect hammer for every nail, or tha t we might not be the 
right person to include on a project or to approach for expert advice. The fourth 
alternative is closely related to this, but from the other side: Having spent consid-
erable time, energy, and eﬀort to master the use of one particular tool, we may be 
conditioned to see the world (or , at least research questions) from the perspective 
of that approach only. 

  
  
 
 
 
 
 
 
 
 
 
  
    
  
 
   
 
 
 
 
92 Data Demands 
For many, when asked for recommendations for a speciﬁc piece of software, 
platform, programming language, or information storage structure, the answer is 
simple, but deceptive. Those with years and even decades of experience will assert, 
with absolute conﬁdence, that they know the only possible technological solution 
to a(ny) given problem: Their Software of Expertise. In some cases, this might be 
a self-serving suggestion, allowing the person to position themselves as irreplace-
able within a project; in others, it will be a well-meaning and genuine suggestion, 
but driven by a blinkered perspective. It does not immediately follow that the sug-
gestions themselves are bad, inaccurate, or undesirable. What it does mean, is that 
they are the result of bias. It is the perspective of the expert whose answers reﬂect 
their lived experience, prior information and even personal choice. It is not to be 
seen as universal, objective truth. 
Information technologies actively shape the way we encounter information, and 
the way we interpret what we see. This is equally true of all information stor -
age and structure approaches, be they library catalogues or the hidden knowledge 
structures of social media giants. Whether we are discussing the computational 
backend that enables Google’s microsecond searches that returns billions of hits, 
or the in-house, custom-built idiosyncratic relational database developed by a pro-
grammer for a speciﬁc project, or indeed a humble spreadsheet, the single copy 
of which sit on an individual researcher’s laptop, all of these approaches both are 
informed by and in turn inform the way that we process information, and the ways 
in which we categorise the world. 
All information technologies can be considered from two complementary but 
very diﬀerent perspectives. On the one hand, there are socio-cultural and politi-
cal considerations: these include aspects such as the popularity of a platform, the 
user experience, and the ease of initial uptake. These considerations – all  human 
things – can have immense impact, but it should prompt us to ask questions about 
the phenomena. For example, is Facebook with its almost 2.8 billion users inher -
ently better as a social media platform than Twitter, which has “only” 396 million 
users?
6 And how would this be measured? What are the driving forces behind the 
choices of users when picking a particular tool, technology, or platform? 
On the other hand, we should consider the technological possibilities and limita-
tions of any given digital platform or computational tool. To understand the tech-
nology, which this book focuses on – Linked Open Data – is to understand the role 
both these considerations have on aﬀecting the way the method has been developed 
and used. Only a thoughtful, critical (but not necessarily exclusively negative) inter-
disciplinary evaluation of this methodology can enable us to systematically gauge 
the strengths and weaknesses of this technology. It is the process by which we can 
determine how we have come to know what we know (an information provenance 
trail, as it were) and to assess whether or not a given (undoubtedly unwavering and 
passionate) testimony of a methodological practitioner and researcher is based on 
personal preference or technological suitability. To be clear – as with any technol-
ogy, Linked Data (nor Linked Open Data, a distinction that will become apparent 
momentarily) is not a silver bullet, and there will be times when it is not the most 
suitable tool. But, there will be other times, when the aﬀordances and possibilities 

 
 
   
 
  
       
   
  
 
 
 
 
 
   
   
  
   
Data Demands 9 3 
created by this information publication paradigm are revolutionary. This process of 
understanding the multifaceted nature of this technology is our way to ensure we 
are thinking about Linked Data critically and clearly, and asking not only the right 
questions but the right kinds of questions. 
Beer (2016 ) provides a scaﬀolding for his analysis of the history of Big Data, 
which lends itself, with minor tweaking, to the topic at hand as well. Beer takes 
his inspiration from Hacking’s 1991 publication (in a volume called The Foucault 
Eﬀect) which discusses the need for a history of statistics, and applies these reﬂec-
tions to Big Data. Following these, the discussion here will cover the institutional, 
political, and other considerations of Linked Data, but rather than focus on the use 
of term by experts or the public (as Beer does), focus will be on the critical evalu-
ation of the methodology. But critical is not intended to be exclusively negative – 
rather, each aspect of the discussion is viewed as a multifaceted thing, and assump-
tions as to whether any of those individual facets might be positive or negative are 
kept to a minimum. As such, the discussion must occasionally approach a topic 
from an abstract and almost philosophical standpoint – they will be balanced with 
examples and more tangible case studies. 
5.4 Diﬀerent Demands of Diﬀerent Technologies 
Diﬀerent knowledge structures – be they relational databases, tabular data, un-
structured text, MarkUp, a knowledge graph – all have various strengths and weak-
nesses. These broad categories of diﬀerent types of structures are best understood 
through a process of explaining them alongside example processes of the conver -
sion of data between diﬀerent formats. To understand why a particular data format 
is more suitable in one context or another is achieved through comparison and 
contrast with others. 
Even a brief comparison between the Linked Data publication paradigm and 
other information structures shows that there are many parallels between it and 
relational databases (e.g. open-source relational database management system 
[MySQL]) and MarkUp languages (e.g. XML). The similarities between them 
include (i) the connection to Web technology (RDF uses Web technology, XML 
is closely linked to Web languages, and relational databases, whilst they do not 
naturally link to the Web, are in fact frequently used to store data behind websites); 
(ii) query languages (SPARQL and SQL share many similarities in function and 
syntax, and XML Path Language (Xpath)/Xquery/XSLT can similarly be used to 
extract information when working with XML documents); and (iii) several ways in 
which these technologies are brought together, for example, some triplestores use 
a relational database to store the RDF triples, there are tools to expose data from a 
relational database management system (RDBMS) as RDF, and, as discussed pre-
viously, one of the syntaxes for RDF is RDF/XML, and it is possible to annotate 
XML documents with RDF metadata. 
There are key technical diﬀerences. Graph databases diﬀer from relational data-
bases in a few fundamental ways. The nomenclature is the key here: the informa-
tion held within the former is structured as a graph – it is not set in a structure or 

 
   
    
 
  
    
  
 
  
 
  
 
 
 
   
  
 
  
     
  
 
94 Data Demands 
a shape, per se, the graph is decentralised and can be navigated from any starting 
point. In a relational database, data is structured in immutable tables, connected to 
other equally inﬂexible ones through key columns. The latter have had decades of 
investment of energy, time, expertise, and so on. The former are the computation-
ally powerful way of capturing semantics and relationships between data entities. 
Triplestores, as the rather uninventive name will have given way, are graph data-
bases that store RDF triples: purpose-built for the storage, editing, maintenance, 
retrieval, and so on of RDF triples in particular. 
Where Linked Data diﬀers from both is that it is inherently ﬂexible – any con-
nections between nodes ( properties between Classes) can be asserted, 
stored, and edited: in relational databases, data is categorised into predeﬁned ta-
bles, eliminating or minimising any possibility of ad hoc chang es. In the case 
MarkUp languages, the knowledge structure is directly dependent on XML lan-
guage and must adhere to deﬁned standard (such as TEI).
7 Another diﬀerence is 
that where RDF necessitates the use of HTTP URIs, in relational databases the 
naming of columns is local. Again, in this regard, MarkUp langu ages are more 
similar, as XML namespaces make very similar use of URIs. One of the chal-
lenges of working with Linked Data is that in terms of developm ent of software 
and tooling, the ﬁeld is comparatively new; this is a considerable diﬀ erence to 
both relational databases and MarkUp languages, for which there are numerous 
mature and scalable tools available. 
The biggest diﬀerence between Linked Data and the other two is in the way data 
is structured. The abstract data model of RDF results in a grap h structure. As the 
nomenclature suggests, relational databases have data contained in sets or tables 
that (as is the case with MarkUp languages) usually map to hierarchical or tree 
structures. 
Each of the three (tabular data, relational databases, and Linked Data) have 
strengths and weaknesses, pros and cons. Although they are often described in that 
order, this listing does not reﬂect a linear progression of improvement. Each has 
a function and a purpose, and none of the three is always the right solution. For 
a comprehensive but easy-to-read comparison of these strengths and weaknesses, 
van Hooland and Verborgh’s (2014 : ﬀ 14) discussion is situated within examples of 
libraries, archives, and museums. An important consideration he re is that various 
diﬀerent tools and workﬂows can be utilised to create RDF from both tabular and 
relational data, enabling the aggregation of the information held in various diﬀ er-
ent types of information structures using Linked Data. 
5.6 Case Study: JazzCats 
Linked Data is most productive when done in collaboration with others ( Burrows 
and Nurmikko-Fuller, 2020 ). JazzCats (Jazz Collection of Aggregated Triples) 
8 is 
a Linked Data project for studying jazz artists, performances, and their prosopog-
raphy through social and professional networks. The project combines metadata 
from three diﬀerent sources – each of these consists of data held in a diﬀerent 
format (tabular, relational, and RDF). As a case study example, it illustrates the 

  
      
  
   
 
  
   
  
 
 
 
  
 
 
 
  
   
 
  
 
 
  
    
    
       
  
   
Data Demands 9 5 
diﬀerent demands imposed upon the researchers and the workﬂow by these diﬀ er-
ent data structures. 
The ﬁrst iteration of JazzCats ( Nurmikko-Fuller et al., 2017, 2018 b) brought 
together three datasets: a discography of Body and Soul (that is to say, a cata-
logue of recordings of this particular jazz standard); 
9 the Weimar Jazz Data-
base,10 which contains musicological metadata; and data from the Linked Jazz 
project, which is a prosopography of jazz musicians. More recently, RDF triples 
capturing information about jazz recordings from the Centre for Jazz Studies 
from Columbia University (J-DISC) 
11 were added to the underlying knowledge 
graph.12 
5.6.1 Tabular Data: The Body and Soul Discography 
The Body and Soul discography describes over 200 recordings, all dated between 
1930 and 2004. It was originally conceived as supplementary material to Bowen’s 
2015 article, and is available as a PDF online, but in neither a machine-processable 
nor non-proprietary format, and thus being an example of one star of the Five Star 
Linked Data Standard (described in Chapter 1 ). Although rich in relevant informa-
tion, the data format (PDF) meant that it could not be incorporated into the project 
knowledge graph as is. An additional process of converting the content of this ﬁle 
was necessary in order to produce a structured dataset that could be used for sub-
sequent stages of the project workﬂow. Personal correspondence with the author 
resulted in him sharing the original spreadsheet with us, and in using tools such as 
OpenReﬁne, the project team converted and tidied this data ( Bangert, 2016 ). It is 
now available from the JazzCats project website as a CSV , and meets the three star 
criteria since it is published online, with an open licence, and in a non-proprietary 
format. Neither the content nor the structure of the dataset has changed. This ex-
ample serves to illustrate that with relatively little eﬀort, projects can publish their 
data at the Three Star Standard. 
The workﬂow for converting this tabular data into RDF has been documented 
elsewhere ( Nurmikko-Fuller et al., 2018 a) and discussed from a generalist Digital 
Humanities ( Nurmikko-Fuller et al., 2017 ) and well as a musicology perspective 
( Nurmikko-Fuller et al., 2018 b, October; Bangert et al., 2018 , September). Here, 
it serves a purpose to repeat the simplicity of the workﬂow as an illustrative exam-
ple and as a point of comparison with alternative methods deployed for the other 
datasets. 
The ﬁrst stage of the production of instance-level RDF was to develop a data-
driven ontological model. The ontology (which is extensively documented on the 
project website) 
13 was mapped where possible to the Music Ontology, 14 and its two 
sister ontologies of Event 15 and Timeline. 16 The resulting structure consists of just 
eight Classes and 21 properties, but these are suﬃcient for the capture of 
the data held within the CSV ﬁle, and to enable us to add this information to the 
project knowledge graph. The ontology was developed and edited using the Stan-
ford University free and open software Protege,
17 well known in the ﬁeld and used 
for ontology development across multiple disciplines. 

     
   
 
  
 
 
  
 
 
   
 
 
     
 
  
   
 
   
 
 
 
      
 
   
 
 
 
 
  
96 Data Demands 
The resulting TTL ﬁle was uploaded alongside the CSV ﬁle to an instance of 
the Web Karma software, from the University of Southern Califor nia. 18 A process 
of manual alignment was then carried out, using the point-and-click user interface 
(UI) of this tool, to specify which columns of the CSV contained the instances for 
a particular Classof the ontology. The resulting RDF triples are virtually erro r-
free, give or take a very small number of errors (fewer than ﬁ ve) that arose from 
unusual characters or spaces within the CSV that cause broken URIs to be minted 
from that data. The pay-oﬀ in terms of the investment of time is clear: the map-
ping process is time-consuming for the human researcher, but th e resulting RDF 
triples are of high quality and require virtually no ad hoc edi ting. This is in stark 
contrast to the workﬂow for the production of RDF to capture the content of the 
Weimar Jazz Database. 
5.6.2 Relational Databases to RDF: Weimar Jazz Database 
Part of the Jazzomat Research Project, the Weimar Jazz Database, 19 is an exten-
sively curated collection of performance transcriptions (mostly solos) produced 
using Sonic Visualiser ( Pﬂeiderer et al., 2017 ). The rich and diverse information 
held within the database contains details about performers and instruments, as well 
as metadata such as title, tempo, and key. The project data contains links to external 
authority ﬁles such as Wikipedia 
20 and MusicBrainz, 21 which is an example of the 
Linked Data-readiness of the data, but also provides an opportunity for a worka-
round for copyright restrictions that prevent access to some of the data (such as 
contextual annotations): the use of temporal markers via MusicBrainz IDs enable 
the identiﬁcation of existing solos, for example ( Abeßer et al., 2014 ; Nurmikko-
Fuller et al., 2018 a). 
The Weimar Jazz Database sits in an instance of SQLite3. 
22 Web Karma, which 
is ideally suited for tabular data, was not the ideal tool for the conversion of this 
data into RDF. Instead, the project workﬂow ( Nurmikko-Fuller et al., 2018 a) con-
sisted of using another open source tool, D2RQ. 
23 The beneﬁt of this approach is 
that the process is largely automated; the drawback is that it requires a two-step 
process, where the second stage is a time-consuming one of data cleaning and 
management. The later stage involves the reconﬁguration of the relational structure 
into a graph one, and thus also has a prerequisite need for the development of an 
ontological structure, or at least an awareness of the Classesand properties
that the instance-level (relational database content) RDF should be mapped onto. 
And therein lies a point of fundamental importance. DHers and our support-
ing technical staﬀ are often asked for advice regarding the “best” possible tool to 
complete a task. There is an existing culture of conﬁdence (even hubris), and of 
uncritically promoting the tool that the person in the position to advise is famil-
iar with using. But the correct answer here too is “It depends”. It depends on the 
desired project outcome, the aim of the speciﬁc task, the existing skills and know-
how of the person or people completing the workﬂow, and it depends on when the 
team wants to spend the human eﬀort. A point to emphasise here is that the safest 
assumption is that there will be some point at which human endeavour plays a 

 
 
 
 
   
    
 
 
 
 
 
  
 
 
  
 
   
  
   
     
Data Demands 9 7 
role, and that no workﬂow is free of it entirely. Where the research team has some 
choice though is in choosing the tool most suitable for the data structures that their 
data is natively in, and at what time of the workﬂow they choose to invest the most 
human eﬀort. 
5.6.3 Ready-Made RDF: Linked Jazz 
The third diﬀerent type of information category is RDF produced by a diﬀerent pro-
ject that was ingested into the JazzCats triplestore. In this case, the RDF was from 
Linked Jazz, 
24 a project from the Semantic Lab at Pratt. 25 As with any aggregator 
project, there are two possible opportunities for combining the RDF from Linked 
Jazz with that of JazzCats: it could either be included via a federated query, or the 
RDF could be accessed, downloaded, and included into the JazzCats triplestore. 
There are pros and cons to either approach, and arguably more than one cor -
rect way of accomplishing either aim. The practical beneﬁts of setting up a system 
that enables the user to query information from several databases using one point 
of entry are clear: this way, the user has access to aggregated information, but the 
responsibility for the maintenance and quality of the data are with the data owner. 
The challenges include security concerns and the need to establish the data map-
pings of what is essentially someone else’s database. The beneﬁt to downloading 
and incorporating another project’s RDF into one’s own triplestore is that querying 
can happen locally. But, if the owner makes any changes to their data, the RDF in-
corporated into another triplestore will not be automatically updated, and thus risks 
deviating from the most up-to-date, gold standard quality of data as maintained by 
the data owner. 
5.6.4 Querying Across Three Datasets Using SPARQL 
For the JazzCats project, we converted tabular data into RDF (Body&Soul); trans-
lated a relational database into RDF (Weimar Jazz Database), and ingested a data-
set that was already in RDF (Linked Jazz). We created a separate, named graph 
for each of the projects: that is to say, there were three distinct knowledge graphs 
in one triplestore. The beneﬁt of this approach was that, if we so chose, we could 
query just one of the datasets by limiting the queries to that graph. Alternatively, 
we can query across all three graphs simultaneously. 
SPARQL contains a standard set of rules that determine the interactions be-
tween client programmes and a server. However, as DuCharme desc ribes at the 
very ﬁrst chance ( 2013 : 1), “you can go far with the query language without wor-
rying about the protocol, so this book doesn’t go into any deta il about it”. And 
neither will this one. 
Ontologies and the Turtle syntax of RDF beautifully mirror SPARQL (the SPARQL 
RDF Protocol and RDF Query Language). 
26 Although not the most recent of pub-
lications, a comprehensive manual on the query language has been written by Bob 
DuCharme (2013 ). Other recommended sources include Wikidata’s SPARQL tem-
plates,
27 and for anyone wishing jump in at the deep end, the SPARQL Playground 28 

 
  
 
 
 
  
 
 
  
  
  
    
 
  
 
 
 
 
  
 
 
  
  
98 Data Demands 
oﬀers opportunities to learn ways to write increasingly complex queries to explore 
an underlying custom dataset. 
Anecdotally, many developers and programmers have commented on the simi-
larity between SPARQL with regard to SQL, the (Structured) Query Language 
for relational databases. This undoubtedly reﬂects a history of education, whereby 
the latter is often incorporated into more traditional pathways for training coding, 
programming, and software development, and the former is the new kid on the 
block. Arguably there is scope for encountering SPARQL from a diﬀerent perspec-
tive, one in which the relational middleman is skipped, and the graph-like thought 
processes of the Humanities scholar are directly translated into the query language 
that was developed speciﬁcally to query data published as RDF. Even the most de-
vout Linked Data sceptic is won over when they get to try their hand at SPARQL – 
teaching the Linked Data workshop at the Digital Humanities Oxford Summer 
School for the last seven years has made this clear. 
Unfortunately for Linked Data, “while SPARQL has proven to be a powerful 
tool in the hands of experienced users, it remains diﬃcult to fathom for lay users” 
( Ngonga Ngomo, 2013 : 977) – and although there are the non-SPARQL frontends 
the likes of Pubby
29 (for follow-your-nose-investigations) and SPARKLIS, 30 no 
clear reigning champion of graphical user-interfaces (GUIs) enabling natural lan-
guage questions equally across all Linked Data projects has yet emerged. the one 
produced by Nomisma.org 
31 is an excellent example of innovation geared towards 
providing services that are not just user-friendly, but represent some of the best ap-
proaches for enabling Humanities researchers to engage with Linked Data (without 
the need to learn SPARQL). 
The data management evaluation raises an interesting question around data prov-
enance, privacy, and trust. The latter two are more comprehensively discussed in 
Chapter 2 , but note that when we are (as we always are in Linked Data) in the busi-
ness of amalgamating information from various diﬀerent external sources, we must 
trust the originator of that data to provide us with the best quality data possible. Or 
do we? Digital Humanities projects that focus on a single dataset quite reasonably 
spend time and energy on data tidying. There is expectation and a correlation be-
tween the results and the responsibility of the project: if there is a mistake in the re-
sults, it is the fault of the project since they have provided inaccurate information. 
But what about Linked Data projects, where we pull in data from diﬀerent sources? 
Should we now be responsible for the accuracy of all the data we have amassed? If 
yes, then how does that reconcile with the fact that any editing of the original data 
within the context of the Linked Data project has now resulted in a deviation from 
the gold standard data of the original project? What if the changes we made were 
in error, and new mistakes were introduced? Or what if the data is not edited, but it 
is misinterpreted or misused? 
5.7 Conclusion 
Diﬀerent knowledge structures (relational databases, tabular data, unstructured text) 
all have various strengths and weaknesses. In this section, the broad categories 

 
 
 
  
 
 
 
  
 
 
 
  
 
 
  
 
 
  
 
 
 
 
Data Demands 9 9 
of diﬀerent types of knowledge structures have been outlined, and example pro-
cesses for the conversion of data into a machine-processable fo rmat have been 
described. The JazzCats project has served as a case study example which com-
bined jazz performance metadata from three diﬀerent sources, each of which was 
held in a diﬀerent kind of solution (a relational database, tabular data, and a graph 
database). 
But should we, as Linked Data practitioners, dedicate time and  eﬀort to under-
standing the history of index card systems, largely obsolete hypertext solutions, or 
the shift in public perception of all things computational being the domain of men 
when just some decades ago all “computers” were women? The answer is twofold. 
First, Linked Data, which is so fundamentally about connections and collabora-
tions, is never going to deliver on its potential in isolation. To be able to collaborate 
with others, we must understand their approaches, and the challenges, opportuni-
ties, and strengths of the technologies and database solutions they use. Second, to 
be able to critically evaluate these technologies, we must understand the context in 
which they arose. 
All information representation systems from spreadsheets to triplestores are 
designed, built, and used to contain information. Not just contain it, but to man-
age, retrieve, and use data. Within these broad categories are myriad examples of 
speciﬁc implementations. Even if we focus on a speciﬁc context like the GLAM 
sector, there are vast numbers of diﬀerent solutions. Some museums prefer cus-
tom-built databases, others opt for oﬀ-the-shelf solutions. The decision for which 
approach to take should be driven by the needs of the institution, the available in-
formation categories, the level of available resources, and the existing skills found 
in-house. Sometimes decisions as to which database to use are based on (expert) 
recommendations. 
The problem with recommendations is that they are always biased. We prefer 
solutions that we are already familiar with, or which play to our existing strengths. 
To think about it another way, would you recommend a tool that was diﬃcult to 
use, and that seemed not to be ﬁt for purpose? I would imagine not! Even well-
intended recommendations can lead to suboptimal advice, as rarely are we fully 
familiar with all the considerations listed earlier with regard to someone else’s 
project. 
The same biases and reasons for these biases also apply to workﬂows. The 
workﬂows that worked for us in the JazzCats project are listed in this Chapter, 
but these were solutions developed for a particular set of circumstances, research 
agendas, and existing levels of skill. Reporting on these workﬂows serves a two-
fold purpose: ﬁrst, they do oﬀer a potential set of solutions that might help with 
the initial set up of a Linked Data project. Second, they illustrate that no matter 
what the original format of the data, it is possible to produce RDF with relatively 
“simple” processes. 
Many conversations in the Digital Humanities around Linked Dat a are centred 
around ideas of ease or simplicity, but this is a loaded set of questions. Software and 
tooling that has a low bar to engagement (ones that are intuitive to use, for example) 
are often recommended, but that rarely equates to simplicity of the tool – quite the 

 
  
 
 
 
  
 
 
 
 
 
 
 
 
 
   
 
 
 
 
 
     
 
    
      
      
    
100 Data Demands 
opposite. In many cases, the simplicity of the user experience hides a remarkable 
level of complexity. 
Ultimately, each project plan and team has to make one decision: when to invest 
human eﬀort. In the case of the workﬂows used in JazzCats, there are two clear 
examples of extremes. The Body&Soul workﬂow produced very high-quality RDF 
triples that required virtually no post hoc ﬁxing or editing. The cost of this was that 
considerable human time and eﬀort was used to map the data (at schema-level) and 
to produce the instance-level RDF in a largely manual mapping process. 
The opposite was true for the Weimar Jazz Database. The workﬂow was largely 
automated and as such, required little in terms of initial investment of human eﬀort. 
The drawback of this is that the process produced a large number of superﬂuous 
URIs in RDF triples, including capturing the relational database structure. A series 
of SPARQL queries had to be run to edit these unnecessary triples from the graph – a 
largely human-driven task. 
In the case of Linked Jazz, decision-making was driven based on existing skill-
sets within the project team. The decision to ingest the RDF triples of another 
project meant that even with limited time and resources, we could maintain a triple-
store with data from three distinct projects. We were more conﬁdent in maintaining 
one triplestore than we were establishing and maintaining options for federated 
querying. The drawback is that if Linked Jazz ever changes their triples, our knowl-
edge graph will not be automatically updated. 
JazzCats is an opportunity to illustrate one additional point. Neither the owners 
of Body&Soul nor the Weimar Jazz Database had to alter their data, edit their infor-
mational storage structures, or relinquish control of their own dataset. In creating 
the RDF, we did essentially duplicate the same information, but the respective data 
owners were able to maintain their set ups unaltered. 
It is diﬃcult to guess whether greater numbers of DHers will engage with the 
Linked Data approach in the future, but there are several beneﬁts to doing so. Risk 
is minimised by maintaining a copy of the data in the original tabular or relational 
database; workﬂows can be picked to limit the need for extensive upskilling; and, 
projects can accurately and truly represent their knowledge though processes such 
as designing and implementing a data-driven ontological structure. The more pro-
jects and people to join in with Linked Data, and contribute to the Linked Data 
crowd, the more diverse and valuable the Cloud becomes. The bar has never been 
lower to take those steps towards accomplishing the techno-utopian dream of a 
Web that bridges the entirety of human knowledge. 
Notes 
1 The talk is no longer available from the TED.com site, but it can be accessed on the TED. 
com’s YouTube channel, at www.youtube.com/watch?v=ksasPjrYFTg&ab_channel= 
TEDxTalks . Accessed 03/05/2022. 
2 GLAM refers to “galleries, libraries, archives, and museums”. 
3 As an example of culture-speciﬁc classiﬁcation, I want to call this time of year “Spring” 
but, in Australia, it was autumn. 
4 Kranzberg’s (1986 : 545) First Law: “Technology is neither good nor bad; nor is it neutral”. 
5 This too is a quote that appears in the Nurmikko-Fuller and Pickering (2021 ) paper. 

 
     
    
    
    
      
    
       
    
    
    
    
    
    
    
    
    
     
        
    
    
    
    
    
    
    
    
 
  
 
 
    
 
 
 
   
  
 
 
  
 
Data Demands 101 
6 www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-
users/. Accessed 23/07/2021. 
7 TEI is the Text Encoding Initiative:  https://tei-c.org/ . Accessed 14/07/2021. 
8 http://jazzcats.cdhr.anu.edu.au/. Accessed 22/06/2021. 
9 Jazz standards are widely known, performed, and recorded compositions that often form 
the part of the repertoire for jazz musicians. 
10 Weimar Jazz Database is available from https://jazzomat.hfm-weimar.de/dbformat/ 
dbcontent.html . Accessed 08/07/2021. 
11 https://jdisc.columbia.edu/. Accessed 09/07/2021. 
12 For more information about the datasets, see http://jazzcats.cdhr.anu.edu.au/about/ . 
Accessed 09/0/2021. 
13 http://jazzcats.cdhr.anu.edu.au/documentation/. Accessed 08/07/2021. 
14 http://musicontology.com/. Accessed 08/07/2021. 
15 http://motools.sourceforge.net/event/event.html. Accessed 08/07/2021. 
16 http://motools.sourceforge.net/timeline/timeline.html. Accessed 08/07/2021. 
17 https://protegewiki.stanford.edu/wiki/WebProtege. Accessed 08/07/2021. 
18 https://usc-isi-i2.github.io/karma/. Accessed 08/07/2021. 
19 https://jazzomat.hfm-weimar.de/dbformat/dbcontent.html. Accessed 09/07/2021. 
20 www.wikipedia.org/. Accessed 08/07/2021. 
21 https://musicbrainz.org/. Accessed 08/07/2021. 
22 For more information about the database format, see https://jazzomat.hfm-weimar.de/ 
dbformat/dbformat.html . Accessed 08/07/2021. 
23 See both http://d2rq.org/d2r-server and http://d2rq.org/ for more information. Accessed 
09/07/2021. 
24 https://linkedjazz.org/. Accessed 09/07/2021. 
25 For more information see https://semlab.io/ . Accessed 08/07/2021. 
26 It is pronounced “sparkle”, and yes, it is a recursive acronym. 
27 https://query.wikidata.org/. Accessed 26/01/2023. 
28 https://sparql-playground.sib.swiss/. Accessed 26/01/2023. 
29 www.w3.org/2001/sw/wiki/Pubby. Accessed 27/05/2022. 
30 https://wiki.dbpedia.org/projects/sparklis. Accessed 27/05/2022. 
31 https://numismatics.org/ocre/. Accessed 26/01/2023. 
Bibliography 
Abeßer, J., Cano, E., Frieler, K., and Pﬂeiderer, M. (2014). “Dynamics in Jazz Improvisation – 
Score-Informed Estimation and Contextual Analysis of Tone Inten sities in Trumpet and 
Saxophone Solos”. Proceedings of the 9th Conference in Interdisciplinary Musicology 
(CIM), Berlin, Germany, 4–6 December. 
Bangert, D. (2016). “JazzCats Body&Soul Discography [dataset]”. Zenodo. http://doi.org/ 
10.5281/zenodo.163886 . 
Bangert, D., Nurmikko-Fuller, T., Downie, S., and Hao, Y . (2018). “JazzCats: Navigating an 
RDF Triplestore of Integrated Performance Metadata”. Proceedings of the 3rd Interna-
tional Workshop on Digital Libraries for Musicology (DLfM), Satellite Event of the 19th 
International Society for Music Information Retrieval Conference (ISMIR), Paris, France, 
28 September. 
Beer, D. (2016). “How Should We Do the History of Big Data?”. Big Data & Society, 3(1). 
Bowen, J. A. (2015). “Who Plays the Tune in ‘Body and Soul’? A Performance History 
Using Recorded Sources”. Journal of the Society of American Music, 9(3), pp. 259–292. 
Burrows, S., and Nurmikko-Fuller, T. (2020). “Charting Cultural History Through Historical 
Bibliometric Research: Methods; Concepts; Challenges; Results”. In Routledge Interna-
tional Handbook of Research Methods in Digital Humanities. Routledge. 

  
   
  
 
 
  
 
 
  
  
 
 
 
 
 
 
 
 
 
 
 
  
  
 
   
  
  
  
 
 
102 Data Demands 
Clark, A., and Chalmers, D. (1998). “The Extended Mind”.  Analysis, 58(1), pp. 7–19. 
DuCharme, B. (2013). Learning SP ARQL: Querying and Updating With SP ARQL 1.1 . 
O’Reilly Media, Inc. 
Kranzberg, M. (1986). “Technology and History: ‘Kranzberg’s Laws’”. Technology and 
Culture, 27(3), pp. 544–560. 
Ngonga Ngomo, A., Bühmann, L., Unger, C., Lehmann, J., and Gerber, D. (2013). “Sorry, I 
Don’t Speak SPARQL: Translating SPARQL Queries Into Natural Language”. Proceed-
ings of the 22nd International Conference on World Wide Web, ACM. 
Nurmikko-Fuller, T. (2022). “Teaching Linked Open Data Using Bibliographic Metadata”. 
Journal of Open Humanities Data, 8. 
Nurmikko-Fuller, T., Bangert, D., and Abdul-Rahman, A. (2017). “All the Things You Are: 
Accessing an Enriched Musicological Prosopography Through JazzCats”. Proceedings of 
the International Digital Humanities Conference 2017 (DH17) , Montreal, Canada, 8–11 
August. 
Nurmikko-Fuller, T., Bangert, D., Dix, A., Weigl, D., and Page, K. (2018a). “Building Proto-
types Aggregating Musicological Datasets on the Semantic Web”. Bibliothek Forschung 
und Praxis, 42(2), pp. 206–221. 
Nurmikko-Fuller, T., Bangert, D., Hao, Y ., and Downie, J. S. (2018b). “Swinging Triples: 
Bridging Jazz Performance Datasets Using Linked Data”. Proceedings of the 1st Inter -
national Workshop on Semantic Applications for Audio and Music , Monterey, USA, 9 
October. 
Nurmikko-Fuller, T., and Pickering, P. (2021). “Reductio ad Absurdum?: From Analogue 
Hypertext to Digital Humanities”. Proceedings of the 32nd ACM Conference on Hyper -
text and Social Media (ACMHT21), Dublin, Ireland, 30 August–2 September. 
Orwell, G. (1949). Nineteen Eightyfour. Secker & Warburg. 
 P ﬂeiderer, M., Frieler, K., Abesser, J., Zaddach, W. G., and Burkhart, B. (eds.). (2017). In-
side the Jazzomat: New Perspectives for Jazz Research. Schott Music GmbH. 
Sacks, O. (1985). The Man Who Mistook His Wife for a Hat and Other Clinical Tales. Sum-
mit Books. 
Simpson, R. M. (2020). “Augustine as ‘Naturalist of the Mind’”. Proceedings of the 31st 
ACM Conference on Hypertext and Social Media (ACMHT20), Virtual Event, USA, 
13–15 July. 
van Hooland, S., and Verborgh, R. (2014). Linked Data for Libraries, Archives and Muse-
ums: How to Clean, Link and Publish Your Metadata. Facet Publishing. 

 
 
  
 
  
  
  
 
  
 
 
 
   6 Future Directions 
6.1 Preamble 
In words attributed to Yogi Berra, an American baseball player: “It’s tough to make 
predictions, especially about the future”. There have been myriad predictions of 
the history of technology over the decades and centuries, some (at least seemingly) 
staggeringly accurate, the others absurd in their error: in 2004, Bill Gates (founder 
of Microsoft) predicted that the problem of spam emails would be solved by 2006. 
1 
In 1995, Cliﬀord Stoll told Newsweek:  
Visionaries see a future of telecommuting workers, interactive libraries and 
multimedia classrooms. They speak of electronic town meetings and virtual 
communities. Commerce and business will shift from oﬃces and malls to 
networks and modems. And the freedom of digital networks will make gov-
ernment more democratic . . . Baloney. 
2 
An example of people getting it right is an article (titled “W hen Woman Is 
Boss” from 1926, by the famous inventor Nikola Tesla. 3 He seemingly correctly 
predicts smartphones (“You will communicate instantly by simple vest-pocket 
equipment”), drones (“Aircraft will travel the skies, study, re viewing the world 
that is unmanned, driven and guided by radio”), and environmental disasters. He 
even foresaw a global hypermedia system that could bridge all the world’s knowl-
edge through interconnected information (Linked Data, or the Semantic Web, per-
haps?): “When wireless is perfectly applied the whole earth will be converted into 
a huge brain, which in fact it is, all things being particles o f a real and rhythmic 
whole”. The revolutions in communication technologies were also clear to Tesla: 
“We shall be able to communicate with one another instantly, irrespective of dis-
tance”. Not only that he had a vision for video conferencing pl atforms almost a 
hundred years before the pandemic introduced terms like “Zoom-f atigue” into the 
common vernacular: 
Through television and telephony we shall see and hear one another as per -
fectly as though we were face to face, despite intervening distances of thou-
sands of miles; and the instruments through which we shall be able to do his 
DOI: 10.4324/9781003197898-6 

 
 
  
 
 
 
 
    
     
 
 
   
  
   
  
104 Future Directions 
will be amazingly simple compared with our present telephone. A man will 
be able to carry one in his vest-pocket. 
And he predicted the new role of women, too: 
the average woman will be as well educated as the average man, and then 
better educated, for the dormant faculties of her brain will be stimulated to an 
activity that will be all the more intense and powerful because of centuries of 
repose. Woman [sic] will ignore precedent and startle civilization with their 
progress. 
It is easy to cherry-pick those of Tesla’s predictions that have come to fruition 
(and those by Stoll which have not). Cognitive bias ensures we notice examples 
we can equate to in our lived experience. And, as evidenced by Tesla’s inventions, 
the man was incredibly smart and insightful, so we surely cannot be surprised at 
the accuracy of his thinking? At this point, it may be worth explicitly noting that 
although the term “Digital Humanities” did not exist in 1926, Tesla was clearly an 
interdisciplinary thinker, bridging STEM and HASS: “He is an engineer, an inven-
tor and, above these as well as basic to them, a philosopher”. 
So where will the future take us? It is hard to say beyond where I hope we will 
go. What we can say is that AI and machine learning are currently of huge inter -
est to researchers, and there are no signs of that interest waning anytime soon 
(she says, immediately wondering whether Blade Runner was that far oﬀ after 
all). Researchers across the globe are increasingly beginning to understand that 
the technologies and the datasets under-pinning machine-driven analyses are often 
inherently ﬂawed. Put simply, even highly sophisticated algorithms developed and 
used with data tainted with historical bias simply reproduce them. To this point, 
technological solutions have often sought to increase simplicity by eliminating 
ambiguity. Future research should seek ways to address fundamental societal prob-
lems by speciﬁcally developing methods for capturing ambiguity and vagueness. 
But it will do so by using various types of data. By capturing information from 
diverse cultures and contexts across time, space, and social, linguistic, cultural and 
ethnic boundaries, rich and complex data from the Humanities provides the best 
proving ground for experimental methodologies and technical solutions that have 
the potential to embrace uncertainty, fuzziness and ambiguity. It is not going too 
far to suggest that until we come to grips with data ambiguity our collective faith 
in data analytics is eﬀectively misplaced. As data analysis is steadily shifting from 
human users to algorithms and software agents, the need to address this issue is 
becoming increasingly urgent. 
6.2 The Non-linear Approach to Discussing Linked Data in 
the Digital Humanities 
Linked Data is a data publication paradigm. It is a method for representing and 
publishing data using existing Web architecture and technologies. Linked Data is 

 
  
 
   
 
  
  
 
   
 
 
   
 
 
 
 
 
 
Future Directions 105 
one possible way of providing information online in adherence to the FAIR data 
principles,4 but it is not the only way. Data aggregation is arguably the raison d’être 
for this method, but Linked Data is not the only technological solution that ena-
bles it. In this paradigm, information is represented as a graph, consisting of in-
terconnected nodes and arcs, of data instances (such as people or places) and the 
relationships between them (such as connecting a person and a place through the 
relationships of the latter being the place of birth for the former): information is 
captured as interconnected triples. But, not all graph databases are triplestores. In 
summary, there are many diﬀerent ways and methods for accomplishing the publi-
cation of information online in a machine-navigable graph. It is perfectly possible 
to implement a Linked Data project that is wholly oﬄine, but beneﬁts from the 
computational heavy-lifting of utilising a knowledge graph. This book has focused 
on discussing one possible method, Linked Data, which is a speciﬁc method, reli-
ant on standards issued by the W3C – the main standards organisation for the Web, 
globally. 
5 
More speciﬁcally, the discussion has focused on the use of the Linked Data 
method for publishing information in the context of Digital Humanities, an inter -
disciplinary ﬁeld that sits at the intersection of Computer Science and the Humani-
ties. Research in this area (as deﬁned in Chapter 1 ) consists of myriad diﬀerent 
niche investigations, but these tend to fall into one of two very broad categories. 
They are either the use of digital tools, software, and algorithms in conjunction 
with Humanities data, with the aim of tackling research questions that are usual or 
typical in the Humanities, albeit answered with the aid of computerised tools on 
a greater scale or at greater speed. Or, they are the application of robust Humani-
ties approaches such as critical evaluation, ethical debate, or theoretically robust 
frameworks (e.g. the application of a Feminist lens, or through, say, a Marxist 
perspective) on the assessment and analysis of digital resources, tools, and meth-
ods. Linked Data projects in the Digital Humanities are often excellent examples 
of truly interdisciplinary work, completed by researchers of diﬀerent domain ex-
pertise: these projects take on the task of representing information by capturing 
the relationships between data entities. This requires expertise in the form of both 
the technical skills of computer scientists (in the creation of RDF triples, for ex-
ample) and the domain-expertise of Humanities researchers (in the identiﬁcation 
and articulation of the data and its internal structures, and the inclusion of tacit 
knowledge): both are essential. There are undoubtedly some who possess both the 
domain knowledge and the technical skill to implement a fully ﬂedged Linked Data 
project in the Digital Humanities, but for the vast majority, the old adage rings 
true: no man is an island. There is no technological reason why anyone choosing 
to establish a Linked Data project in isolation could not do so, but as we argued in 
Burrows and Nurmikko-Fuller (2020), to maximise the beneﬁt of the technology, 
connecting to the information published by other projects is paramount. 
The utility of the Linked Data method for supporting and diversifying research 
in the Humanities is clear because these investigations are often the result of draw-
ing connections between things (locating a person at an event, establishing details 
of interpersonal interactions, or illustrating how something has changed over time 

 
  
  
  
 
  
 
 
  
 
  
 
 
   
 
 
 
 
106 Future Directions 
in a diachronic investigation, etc.), and then inferring further conclusions about 
those things. Humanities researchers have arguably invested network diagrams 
and analogue hypertext systems to support their investigations many times over: 
mindmaps are an example of such a methodology, and a widely used, generic one 
at that – the system developed by Pickering (and published in Nurmikko-Fuller 
and Pickering, 2021 ) is a concrete example of a speciﬁc implementation. Simp-
son (2020 , July) unambiguously declared the cognitive processes of Humanities 
investigations to be interconnected and hypertext-like. Beyond that, the inherent 
ﬂexibility and robustness of the RDF triple, and the absence of any technological 
limitations to the types of data entities and relationships that can be declared (that 
is to say, as long as the resulting knowledge graph does not contain any logical 
inconsistencies, the creator of the ontology and the implementer of the triples can 
have ultimate freedom in how they categorise their data and knowledge about the 
subject), Linked Data provides an ideal technical solution for representing the am-
biguous, messy, and incomplete data of the Humanities. The decentralised graph 
means that information does not need to be forced into strict hierarchies: for exam-
ple, there is no need to declare one book the epitome of a work, and have all other 
versions be secondary interpretations: rather, the graph enables us to represent all 
versions as equally signiﬁcant but diﬀerent manifestations of an intellectual piece. 
That having been said, the practical and pragmatic implementation for Linked 
Data projects is non-trivial, and in the absence of readily available and well-known 
tools (including tools with GUIs and WYSIWYG 
6 designs) can remain beyond the 
scope and possibility of Humanities scholars. The solution is an interdisciplinary 
research cluster, but there can be social, institutional, economic, and academic con-
siderations that make the establishment of such research groups prohibitively dif-
ﬁcult or even seemingly impossible. Lack of familiarity with Linked Data amongst 
the supporting and professional staﬀ at higher education and cultural heritage in-
stitutions (e.g. those working in a central IT provision department) can further dis-
suade humanities academics or GLAM sector professionals from taking on the task 
of implementing Linked Data projects at any scale. 
Institutional policies and economic models can aﬀect Linked Data projects even 
when they do exist. An example of this is the ElePHãT project, described and dis-
cussed in Chapter 3 . This project focused on the investigation and development of 
a user-interface that would enable the querying (using SPARQL) of the collections, 
at the metadata level, of two very diﬀerent digital libraries: the boutique and be-
spoke Early English Books Online – Text Creation Partnership project collection 
(EEBO-TCP), and the behemoth HTDL. The feasibility of this project was based 
on two considerations: ﬁrst, there were suﬃcient schematic similarities between 
the databases of the two digital libraries (including categories such as person/au-
thor, title, publication place, ID number, etc.) to enable schema-level bridging; and 
second, tacit knowledge of speciﬁc individual parallels (such as the same named 
individual, the same publication or work, the same geographical location) con-
tained within the respective databases to enable instance-level anchoring. At face 
value, the two digital libraries have many diﬀerences: one is huge, the other is tiny. 
For the HTDL, the metadata is largely generated through automated processes, the 
EEBO-TCP is manually curated by expert librarians. 

 
  
 
 
  
    
  
 
 
 
 
 
  
 
 
  
  
 
 
  
 
 
Future Directions 107 
From a Linked Data perspective, the main diﬀerence is one of institutional 
policy with regard to the Openness and accessibility of the data: at the metadata 
level, all 25,000 records of Phase I of the EEBO-TCP are publicly available. For 
the HTDL, only about a third of the metadata records are freely available, with a 
whopping 66% or so still restricted under copyright. The technical implementation 
of the ElePHãT project saw the combination of Linked Data (HTDL metadata) 
with Linked Open Data (EEBO-TCP metadata). In practical terms, when querying 
the project UI, the result displays those records that meet the query criteria and are 
available. It is possible to return results that are inﬂuenced and aﬀected by unob-
servable records – in other words, it is potentially possible to show all the records 
that match the query, but not to show records which form part of the knowledge 
graph that connect two or more records together. To put this another way, let’s con-
sider a hypothetical scenario as a way of a thought experiment. 
Let us assume there are two authors. They have both written a single-authored 
monograph, and both the volume and the metadata record are publicly available. 
Let us assume further that building upon the successes of their respective publica-
tions, the two have decided to co-author on a third volume. This one, however, is 
not publicly available, nor is its metadata record. All we can say from the acces-
sibility point of view is that the volume exists, but no other details (such as topic, 
genre, publication place, etc.). Now, let us assume even further that we can query 
the aggregated knowledge graph for the works of authors who have collaborated at 
some point in time. At this stage, we are not focused on the domain or topic – we 
just want to know how proliﬁc the act of co-authorship is in the works recorded by 
these two digital libraries. Although the third (co-authored) volume is not acces-
sible, it forms part of the graph, and is the data point that connects the two authors. 
The results of the query would provide the details of the two single-authored mono-
graphs, and note the existence of the collaborated publication, but not provide the 
details or access to its content. From a user perspective, it can be diﬃcult to assess 
or establish whether this omission is due to a failure of the user-interface, or of the 
underlying project. Rarely do users consider the root-cause of such access limita-
tions to be institutional policy. 
Although Linked Data has many of the hallmarks of bringing forth the type of 
democratised information highway that tech-utopianists can only dream of, the 
business models of many heritage and memory institutions, publishers, and reposi-
tories serve to prevent its large-scale adoption. Signiﬁcant players in the ﬁeld of 
publishing scientiﬁc and research data have a ﬁnancial incentive to prevent Open 
Data and Open Access, but it is these that Linked Data is dependent on. In many 
ways, the work of a Linked Open Data methodologist can only begin when infor -
mation has been made FAIR. At the same time, the oligopolies of the Data Econ-
omy (Alphabet, Meta, etc.) utilise Linked Data methodologies to turn information 
into proﬁt. In many ways, this presents a perfect example of how Linked Data is a 
potential privacy catastrophe waiting to happen. Indeed, there are many examples 
of personal, cultural, and other information which should not be made available 
through Linked Data publication. This technology, which is founded on the prem-
ise of combining complementary information from diﬀerent, disparate data sources 
to address gaps in knowledge, is by its very deﬁnition, a method for removing 

 
 
 
  
 
 
 
 
 
 
 
 
 
 
  
   
 
 
 
108 Future Directions 
anonymisation. Combined with the neoliberal, capitalist aspirations of large corpo-
ration to monetise on information, and the privacy paradox of users providing data, 
and the collection of information about user behaviours both overtly and covertly 
by social media platforms and search engines, Linked Data could be the kiss of 
death to any notion of privacy. It is, potentially, the ultimate tool for nefarious data 
science, just as much as it is for the tech-utopianist views. Linked Data, like any 
technology, is neither good nor bad, nor is it neutral ( Kranzberg, 1986 : 545). 
The neutrality of data capture and knowledge reputation is an unfounded fan-
tasy. It is based on the erroneous idea that machines can in some way oﬀer a method 
of objectivity to information categorisation or its analysis. It’s a fallacy, and one 
that has been shown, particularly in the context of the application of machine learn-
ing, to have potential for detrimental societal impact. The issues here are twofold: 
ﬁrst, no matter how well-intentioned or valiant the eﬀort, no information knowl-
edge structure (database, spreadsheet, mind map or other) is independent of the 
underlying biases of the person or people who create them. That is not to say that 
misogyny, racism, or bigotry are rampant in all databases, but many have exhib-
ited designs that have proven to be problematic: the gender binary is an example 
of one that seems at times to be ubiquitous. Similarly, data itself can only ever be 
retrospective. It is a snapshot of what has come to pass since its creation. For this 
reason, data collects bias – it is a historical bias that shows what has existed before, 
not the ideal or the potential future. This is not a bias of the algorithm, but of his-
tory. In the data used to train the algorithm, success had only been for people who 
had those demographic features. The potential for institutional or systematic bias 
is in both the tool and the data. These biases are often unobservable to users – as 
signiﬁcant a reason as any for keeping the expert in the loop of statistical analysis, 
information representation, and data science. Even Linked Data is no substitute for 
human cognition. 
Observing overt bias such as bigotry can be relatively easy. It is a topic that 
enjoys some mainstream attention, there are training courses for those working 
with data to observe bias in data. Professionals working in the cultural heritage 
sector are undoubtedly aware of historical issues that aﬀected the gender balance 
in the collections: there were times when women were not celebrated as artists, 
when gender-diverse people had no choice but to choose one or the other of a bi-
nary, and so on. In these cases, the data cannot possibly show the subtlety of lived 
experience, nor can we aﬀect historical collecting and acquisition practices, and 
awareness of that bias is in many ways the best that we can do. But what of more 
subtle bias in the data? What of more subtle bias in our database designs?  Chapter 
4  discussed the notions of truth and bias, and the impossibility of having an objec-
tive truth expressed in an unbiased manner. Chapter 5 has examined the role of 
information structures in this process, and of the technical demands they place on 
the Linked Data workﬂow. It has illustrated one ﬁnal beneﬁt to the adoption of 
Linked Data: the possibility of maintaining both the speciﬁc and bespoke database 
structures, developed speciﬁcally for each and every minutiae of the dataset, whilst 
at the same time exposing the information, at least at metadata level, in accordance 

 
 
 
 
 
  
  
  
 
  
 
  
 
 
 
 
 
 
Future Directions 109 
with more universal standards and with the potential for interlinking. It is the pos-
sibility of harnessing the potential for interlinking and inference, of ﬁnding the un-
known unknowns of the data universe, and enriching knowledge across data silos, 
without having to ultimately relinquish control over those speciﬁc data entities that 
are perceived as our own to have and to hold. 
In summary, Linked Data and Linked Open Data are methods for Humanities 
scholars, information disseminators, computer scientists, and everyone in between. 
The potential for aggregating information across the entirety of the connected and 
online human species seems akin to the realisation of the wildest of science ﬁction 
dreams. But it is not mere fantasy nor is it the remit 
7 of future generations. Linked 
Data is already here, it is already happening. What we need to do now is ensure that 
it is developed and implemented in a context of awareness and understanding of its 
potential for both utility and catastrophe. The critical evaluation of this methodol-
ogy and all the projects and datasets that contribute to the vastness of the Linked 
Data Cloud has never been more important. 
6.3 The Tech-Focused Summary of Linked Data in the Digital 
Humanities 
There are several interconnected technologies that play a role in creating, editing, 
managing, storing, and querying Linked Data. There is a cluster of acronyms, too. 
And, there are a few fundamental concepts, which seem simple, but can be philo-
sophically complex. It’s a certain irony of teaching Linked Data that it is diﬃcult 
to discuss these technologies out of the context created by the others: the composite 
parts of a technological implementation that enables us to create interconnected 
information are themselves interconnected. 
Where Linked Data diﬀers from online information aggregation through inter -
connected pages, rather than point to websites or their individuals pages, on the 
Web of Data (the manifestation, or desired end result for publishing all data as 
Linked Data), URIs point to data entities (people, places, etc.), and the relation-
ships between these entities. This is an absolutely fundamental shift – these un-
ambiguous, absolute URIs point to abstract notions, intangible concepts, and the 
(in some cases temporarily bound and even ethereal) relationships between them. 
What this means in terms of the technological implementation is that sometimes 
there is no digital resource (e.g. website, image, audio ﬁle, or video) that the URI 
points to, but the URI represents an abstract concept. Knowledge graphs can also 
contain blank nodes, but as this seeps into the space of technological implementa-
tions, and will not be discussed further here. 
At the very basis of the Linked Data publication paradigm are an aim and a 
promise. The aim is to capture the information within and regarding a particular 
data domain using W3C standards so that the information itself can be published 
online in a format that makes it ﬁndable, accessible, interoperable, and reusable 
(ticking all the boxes of the FAIR data principles) but not just by human users but 
by software agents as well. The promise is twofold: ﬁrst, that by doing so, this data 

 
  
  
 
 
 
  
 
 
 
  
        
  
  
 
 
 
 
 
 
  
 
  
 
110 Future Directions 
can be connected up to other databases anywhere online that have complementary 
information in them (including those far beyond the reach of our current knowledge 
of disciplinary silos), and enriching our knowledge by enabling the discovery of 
so-called unknown unknowns – an infamous phrase uttered by the then U.S. Secre-
tary of Defence Donald Rumsfeld at a U.S. Department of Defence news brieﬁng 
in 2002, 
8 which enjoys an axiom-like notoriety amongst Linked Data practitioners. 
The second promise is of machine inference: the discovery of implicit knowledge 
from explicitly declared facts (a phrase used previously in Nurmikko-Fuller, 2018 : 
340). The aims, it turns out, are relatively easy to achieve, and there are many dif-
ferent workﬂows for the production of Linked Data that can be published according 
to the Five Star Standard. The promises are much less easy to point to, but there 
are examples from the Digital Humanities that have accomplished this, such as the 
Nomisma.org project and the myriad datasets it aggregates.
9 
Linked Data is based on a fundamental concept of interlinking data entities. At 
its core sits RDF – not a method or a tool, per se, but an abstract data model. A 
way of deﬁning things, and the meanings those things have by way of represent-
ing the relationships those things have with each other. The mo st basic model of 
RDF consists of three parts, we call it the triple. Each consists of a Subject, 
predicate, and Object. Since the Object of one triple can be the Sub-
ject of another, it is possible to form interconnected chains of t riples, resulting 
in a knowledge graph. 
RDF can be expressed in a number of diﬀerent serialisations, or syntax. Of 
these, perhaps RDF/XML, Turtle (or the Terse RDF Triple Language) and JavaS-
cript Object Notation for Linked Data (JSON-LD) are the most commonly used, at 
least at the time of writing, although in the future, this might be diﬀerent. The key 
here is that data captured in one serialisation can be expressed in any other, without 
any loss of information. For this reason, practitioners in the ﬁeld of Linked Data 
have strong, almost entirely personal reasons for preferring one over the other. As 
with many things relating to Linked Data, there are many standards that govern 
best practice, but there are also many diﬀerent paths to the same goal, and the 
choice of which syntax to use is as personal as the choice of software. Those, for 
example, who have prior experience of XML (the Extensible Mark-Up Language) 
are likely to ﬁnd that their existing skills are a good match for working with RDF/ 
XML. Similarly, those who have worked with JSON (JavaScript Object Notation) 
will ﬁnd it easier to learn JSON-LD. My personal preference is for the Turtle syn-
tax, because it is considered easier to read by human eyes and brain, and because it 
shares such strong similarities with the SPARQL query language. Therefore, all the 
examples in this book are expressed in Turtle. 
If the lack of creativity in the naming conventions of the Linked Data paradigm 
has yet to become apparent, nowhere is it as clear as with triplestores. This term 
applies to a graph database, and it is used to store triples. As stated by a very 
popular advertising slogan from the UK in the mid-to-late 1990s and the early 
2000s: “it does exactly what it says on the tin”. Graph databases and triplestores 
can be referred to interchangeably in the vernacular of discussions between Linked 
Data practitioners, but strictly speaking, graph databases are more generalised, 

 
 
 
  
  
     
   
 
 
   
      
  
 
 
 
  
  
   
  
   
  
  
   
 
 
 
 
Future Directions 111 
and although they use graph structures (of nodes and arcs, etc.), triplestores are 
purpose-built for the storage, management, and retrieval of RDF triples using se-
mantic queries. 
The cognitive leap Linked Data practitioners need to make in comparing re-
lational databases to triplestores is that the latter contain nothing but RDF triples 
expressed in URIs. Speciﬁcally, HTTP URIs – the ones we know and love as part 
of existing Web architecture. This is because RDF is self-referencing. Let’s sum-
marise this with an example. Let’s say we have a dataset about places. There is 
Helsinki, and Finland, and Europe. We can assign a URI to each of them – for the 
sake of simplicity and clarity of expression, they could be referred to as http://
example.org/Helsinki , http://example.org/Finland , and 
http://example.org/Europe. These are not genuine links and will not re-
sult in a website being displayed in the browser: they are identiﬁers, whose purpose 
is to denote the concept of those places. Again, for the sake of clarity, semantics 
could be embedded into these URIs (an approach that is not universally approved 
of in the Linked Data community). Embedded semantics (which can help make the 
process of manual debugging easier) can complicate the comprehension of the next 
point. So, instead, we will call them http://example.org/p9834tp348, 
http://example.org/le48utnop38, and http://example.org/
aei4gy4wyv .
At this stage, the URIs carry no meaning to either human or machine. What 
is needed are additional URIs which point to characteristics and properties of the 
initial URIs. To make this point clearer, let’s use a cluster of URIs with embedded 
semantics. Note that the rdf:type property shown in the examples is a 
speciﬁc one that declares that the left-most URI is a data instance of the Class rep-
resented by the right-most URI. 
http://example.org/p9834tp348 rdf:type http://example. 
org/City .
http://example.org/le48utnop38 rdf:type http://example. 
org/Country .
http://example.org/aei4gy4wyvt rdf:type http://example. 
org/Continent . 
We can now see the ﬁrst URI refers to a thing that has been deﬁned, by Example. 
org to be something they deﬁne as a “city”, the second one to a country, and the 
third to a continent. We don’t yet know exactly how those concepts are deﬁned, nor 
which city, country, or continent the URIs point to, nor how (if at all) they relate 
to one another. 
This additional information is incorporated into the system through the addition 
of more triples, but in this case, not all of the parts of all of the triples are URIs: to 
improve clarity, human-readable labels are added to show which speciﬁc instances 
these URIs point to, and to make the information easier for human brains to follow. 
These labels are not URIs, but clusters of characters referred to as literals: these 
are not machine-readable and so their main purpose is just to help the human user. 

 
 
  
   
     
  
   
    
   
   
    
 
 
  
   
     
  
   
     
  
   
    
 
  
  
 
 
  
 
 
 
 
  
 
 
  
   
  
112 Future Directions 
The following formatting illustrates the clustering of information about a speciﬁ c 
URIs together: 
http://example.org/p9834tp348 rdf:type http://example. 
org/City;
http://example.org/p9834tp348 rdfs:label “Helsinki”. 
http://example.org/le48utnop38 rdf:type http://example. 
org/Country;
http://example.org/le48utnop38 rdfs:label “Finland”. 
http://example.org/aei4gy4wyvt rdf:type http://example. 
org/Continent;
http://example.org/aei4gy4wyvt rdfs:label “Europe”. 
To save us from repetition and to simplify the expression, we can remove the re-
peated URIs in the Turtle syntax without loss of information, resulting in a cleaner 
example: 
http://example.org/p9834tp348 rdf:type http://example. 
org/City;
http://example.org/p9834tp348 rdfs:label “Helsinki”. 
http://example.org/le48utnop38 rdf:type http://example. 
org/Country;
http://example.org/le48utnop38 rdfs:label “Finland”. 
http://example.org/aei4gy4wyvt rdf:type http://example. 
org/Continent;
http://example.org/aei4gy4wyvt rdfs:label “Europe”. 
The connections between the entities are, again, captured by the addition of fur -
ther triples. We could add a speciﬁc triple to each cluster in order to illustrate 
its relationship with the other. In the case of Helsinki, it would, for example, 
have a relationship with the country of Finland; and indeed, many diﬀerent re-
lationships, all of which we could represent as equally valid characteristics: We 
could specify that Helsinki is located within Finland, and that Finland, in turn, 
is situated within Europe, and use the same property for each triple. We could 
specify that this relationship is bidirectional, and that not only is Finland situated 
within Europe, but Europe has Finland within it. Or, we could specify that Hel-
sinki’s relationship with Finland is unique as the capital city; or, we could assert 
them both. Or, we could choose to have two separate unidirectional properties, 
or implement one of a number of diﬀ erent alternative strategies. There are many 
diﬀerent approaches and solutions, and at the same time, there are no techno-
logical restrictions to what kind of relationships can be asserted, as long as the 
graph must maintain an internal logic. The driving force behind these decisions 
is usually twofold: the desire to capture all the possible relationships in the do-
main, and second, to facilitate the navigation of the graph most eﬃciently using 
SPARQL queries. 
10 

   
 
  
 
 
 
     
 
    
 
 
  
 
 
   
 
  
 
 
     
   
   
 
  
 
Future Directions 1 1 3 
SPARQL enables us to ask questions that navigate the knowledge graph. We 
can do so from any point in the graph, to any other. That is to say, if there are 
connections in the RDF triples, then we can start the question from any Class, 
and traverse the graph to any end point. There is no need to start at the top of a 
hierarchical tree structure, and navigate down to an increasingly speciﬁc point. The 
graph is decentralised, the graph is connected. Furthermore, the underlying graph 
can include data from beyond the system itself: we can ask a Linked Data project 
questions where part of the answer is determined by information available from an 
external data source. Examples of Linked Data project questions that have required 
more than one singular dataset to answer have been the likes of: 
• Which performances of Body and Soul in a speciﬁc key [dataset 1] were re-
corded in a speciﬁc place [dataset 2] by artists that played with a particular artist 
[dataset 3]? For example, identify recordings of Body and Soul in D-ﬂat made 
in New York City by artists who played with Roy Eldridge during their career 
( Nurmikko-Fuller et al., 2018 ); 
• Find all the [written] works contained in [dataset 1] for authors who have at 
least once published on the subject of “Political science” [dataset 2] ( Page and 
Willcox, 2015 ); 
• Use lyrics sung by Siegfried (a character in Richard Wagner’s Der Ring des Ni-
belungen) on Genius.com [dataset 1] as the basis for identifying complementary 
information (text companions [dataset 2], audio [dataset 3], notations [dataset 
4], images [dataset 5]) across various diﬀerent data sources ( Nurmikko-Fuller 
and Page, 2016 ); and 
• Find all ﬁctional monsters that share physical characteristics of claws, tongue, 
or skin with an animal, and that also live in a river habitat (Wang et al., 2019 ). 
The trick here is to recognise two factors: ﬁrst, that these questions are not unrea-
sonable, indeed, they are legitimate research questions that a Humanities scholar 
would quite rightly wish to pursue, and second, that whilst SPARQL here is not 
enabling a task, which would not be possible for a human brain to answer if given 
the necessary information, it is enabling a data-gathering process at a much greater 
scale and speed than would have been possible for a human scholar alone. 
Now, back to our URIs! 
So far we’ve seen that http://example.org/aei4gy4wyvt(Europe) is 
an instance of the information category ( Class) of http://example.org/
Continent, but how do we know what concept http://example.org/
Continent refers to? This is where ontologies come in. 
The structure of the database, all information categories, and all instance-level 
data, are expressed in the same way. But how do we know what the structure is? 
How do we capture the meanings in Linked Data projects, which are, after all, 
about nothing if not semantics? This is where ontologies, vocabularies, and sche-
mas enter centre stage. These three words again refer to very similar concepts, and 
are often used synonymously or interchangeably. The main diﬀerence here is that 
arguably, vocabularies represent only the types of entities that exist in the domain, 

  
 
 
 
     
    
 
 
 
  
 
  
 
 
 
  
 
  
 
 
 
 
114 Future Directions 
whilst ontologies and schema also – crucially! –capture the relationships between 
those entities. For the sake of clarity and simplicity, the discussion here refers to 
“ontologies” exclusively. 
But which triplestore is the best? How does one pick the right one? These ques-
tions, at face value, seem reasonable, and they are ones that pop up often. The 
desire to ﬁnd the most suitable tool is a natural urge, and in the best scenario helps 
reduce wasted time and can be presented as the most cost-eﬀective solution. But 
“best” is inherently subjective, and the solution that might be ideal for one project 
or one programmer is unlikely to be the same for another. Case study examples in 
this book have used diﬀerent triplestores (e.g. Virtuoso 
11 and Blazegraph), 12 and 
these have been selected for reasons such as cost (both are free to use), perceived 
ease of use, existing expertise in the investigatory team, and even the accident of 
prior selection (joining a collaborative project where the other team had already 
installed and successfully used Virtuoso). Recommendations are a valuable and 
important part of the academic discourse, but too often we are forgetful of explic-
itly, critically reﬂecting on the reasons why we use the tools we use. Furthermore, 
once a particular tool has been learnt or a speciﬁc methodology perfected, there is 
a beneﬁt in reuse, as the time invested in acquiring the skill or knowledge does not 
have to be spent again. What this does mean is that we are biased (even if with good 
reason) to reuse an approach or tool we once (perhaps for largely arbitrary reasons) 
happened to learn. This is also true of other aspects of the Linked Data workﬂ ow, 
such as the (re)use of ontologies, and other design decisions. 
As described in Chapter 4 , ontologies are formalised structures, which explicitly 
state all the possible types of things and relationships between things that can ex-
ist in the mapped domain. They are machine-readable documents, written in RDF. 
They act as the schema for the graph database: showing information categories and 
the connections between. As such, they can be designed in many diﬀerent ways, 
but in the Digital Humanities, two types are more prevalent than others: the data-
driven approach, such as the ones we used for the JazzCats case study in Chapter 5 , 
or universal, top-down models such as the CIDOC CRM described in Chapter 4 . 
Because ontologies reﬂect the understanding and knowledge the people designing 
them have of the mapped domain, they inevitably include some degree of cognitive 
bias, making documentation a particularly important, if arduous task. 
Experts in any FOR and scholarship inherently and often unconsciously be-
lieve in the uniqueness of their datasets and research questions. To the outside 
observer, this can be diﬃcult to reconcile. How, or why, for example, would the 
metadata held in a library for a book diﬀer from that of a volume that forms part of 
a museum collection? There is only so much that can be said abo ut a book, surely 
(author, publisher, date of publication, topic, subject, genre, classiﬁcation, shelf 
mark, collection, owning institution, page number, material, size, the list is actually 
vast and I am being deliberately facetious)? The truth is there is a great similar -
ity in the ways in which information about Things (any things!) is collected and 
recorded even across vastly diﬀerent disciplines. Human beings educated in the 
Western tradition of knowledge capture and representation are taught to categorise 
and catalogue the world and that in turn aﬀects the way in which we observe the 

 
 
 
 
  
 
 
 
 
 
 
  
 
 
 
 
 
Future Directions 1 1 5 
world. To have an appreciation of epistemology is then to have, in some way, an ap-
preciation of information provenance. But not often do we stop to question why it 
is that we know that we know, or whence the data or information we are processing 
comes from, and what inherent biases, omissions, perspectives, and so on might be 
embedded within them. And this is true of areas of study far further removed from 
each other than libraries and museums, for what ﬁeld that would not value (even 
demand!) evidence of the data provenance chain? Who wouldn’t want to know 
how you know what you know? 
Another consideration is at the level of methodology. How do you know what 
to do? In some cases, we have done it before, and subsequently seek to repeat a 
successful workﬂow. We also consult each other, through conversation, question 
and answer forums, through systematic reviews of published academic papers. We 
seek to determine what has been successful before, and apply it to a new context. 
Or we develop new ways to make an existing process manifest quicker or at a 
greater scale. But we also default to points of prior expertise even engaging in new 
endeavours. A ubiquitous example of this is in the process of something as innocu-
ous as deciding on a type of database: the decisions are driven often by subjective 
aspects such as the programming languages used to manage them, cost, and exist-
ing familiarity. This is also true when selecting graph databases, and triplestores. 
The best recommendation is thus to identify the tools and workﬂows that best suit 
the research team’s existing skills, goals, aims, deliverables, available resources, 
funding, institutional policy, and desired outcomes. 
There are many ways to achieve Five Star Linked Data, and much in terms of 
freedom to pick the most suitable approaches and workﬂows. The technical chal-
lenges in the future development of Linked Data will undoubtedly include the devel-
opment of new tools and new user-interfaces (such as the prototype GUI reported on 
by Gatti et al., 2022) that enable interaction and creation of data as RDF for novices 
and even self-identifying luddites ( Chapter 1 ). Furthermore, the ever-increasing size 
of the Linked Data Cloud has shown a pattern of exponential growth in the number 
of distinct projects that contribute to it. Future developments in the technical aspects 
of Linked Data are likely to be steps towards a greater combina tion of algorithms 
that fall into the categories of AI and machine learning; reaso ners of increasing 
sophistication will navigate increasingly complex graphs until the techno-utopian 
dream of the bridging of all the information online will be realised. 
6.4 Conclusion 
Linked Data has potential. Linked Data works. But it is not just typing a word into 
a search engine. 
Linked Data is more than a set of recommendations for best practice; it is an in-
formation publication paradigm with a series of W3C standards for implementation 
and quality. It is a method for connecting complementary datasets, and for repre-
senting interconnected facts in graph structures. The technology has already been 
utilised by many of the most powerful entities involved in online publication, but 
relatively little has trickled down to the user. Today, power computational processes 

 
   
   
 
  
   
  
  
 
 
 
 
   
 
  
 
 
 
 
 
  
116 Future Directions 
aﬀect the way we store, discover, and retrieve information online, but much of the 
heavy lifting is happening behind the scenes. Other technologies and approaches 
are enjoying their moment in the limelight of public interest and overt engagement: 
at the time of writing, these are predominantly AI and machine learning. 
Chapter 1 situated the discussion of the use of Linked Data in the context of 
interdisciplinary research in general, and of the Digital Humanities in particular, 
which sits at the intersection of HASS and STEM. Chapter 2 ﬂagged one of the 
major considerations of using Linked Data, and in doing so at a time when we live 
in a Data Economy: Linked Data has the potential to be a privacy catastrophe. It is 
not uniquely so: other technologies could be used to produce the same outcomes, 
proﬁling, and analysis as Linked Data. Surely then the solution is not to avoid us-
ing the methodology, but to engage in the process of information aggregation and 
data science in thoughtful and ethical ways? Or should we take deliberate steps to 
ensure that new generations of up-and-coming data scientists and programmers, 
and their managers and supervisors, are taught to engage with data in a responsible 
and ethical way? And if so, how? Will true change only be possible once those in 
a position to implement legislation, regulation, and develop policies embrace these 
aims and values as a priority? 
Chapter 3 was an opportunity to discuss the plethora of manifestations and 
forms data takes. Although we often refer to the term as if it is a monolith, “data” is 
nuanced and consists not of one big thing but of what seem to be endless instances 
of smaller things, each with some degree of idiosyncrasy and uniqueness. Research 
and academic cultures can also muddy the waters. Chapter 4 illustrated how bi-
ases can creep into knowledge representation, whilst  Chapter 5 has considered the 
demands created by existing information storage solutions from spreadsheets to 
relational databases to triplestores. The case studies in these chapters serve to show 
that the implementation of a complete Linked Data workﬂow is possible using 
Open Source and oﬀ-the-shelf software solutions. It is within the grasp of anyone 
regardless of whether or not they have programming skills or proclaim themselves 
a luddite. 
The future direction of Linked Data in the Digital Humanities is not easy to 
predict, but in the spirit of joyful pessimism, two things are likely: ﬁ rst, as more 
and more academics, researchers, and interested members of the public become 
familiar with the method and their eyes are open to its potenti al we will see an 
increasing number of them adopting the Linked Data paradigm. They will quickly 
realise how this technology can serve them. At the same time, t his increasing 
enthusiasm and uptake will inevitably highlight that there are diﬀerent aspects to 
Linked Data, all of which are diﬃcult, but, inevitably they come to understand 
that successfully confronting the challenges inherent in any of the aspects of the 
Linked Data paradigm increases the pay oﬀ. Linked Data is hard but it’s worth 
the eﬀort. Some might thrive on ontological development, while other s would 
rather focus on projects that automate workﬂows for large-scale (and speed!) data 
aggregation. 
Second, the converts will better understand how the current enthusiasm with AI 
and machine learning will lead to the development of “smarter” and more eﬃcient 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
      
      
 
     
    
    
    
 
Future Directions 1 1 7 
software that will be able to query and infer knowledge over the interconnected 
graphs of the Linked Data Cloud with increasing sophistication. In other words, it 
has the potential to bring us one step closer to the vision of the Semantic Web. At 
that point, it will expose the true extent to which historical bias and Western knowl-
edge structures dominate the ﬁelds of information representation and data science. 
We will have two options then: either start a valiant ﬁght for equity in information 
representation and just sovereignty over it or accept the perpetuation of the ram-
pant intellectual colonialism of the West. 
But what if we saw greater and more diverse representation in the world of 
Linked Data practitioners and ontological developers? As with all of academia, and 
across the powerhouses of policy development, the inclusion of people of diﬀerent 
races, genders, cultures, languages, socio-economic backgrounds, and disciplinary 
domains could (radically) change the landscape. Would this be a way for us to lev-
erage the richness of all diﬀerent ways of perceiving the world, rescuing those that 
are about to disappear, and reviving, where possible, those that have been lost? In 
his 2008 TED Talk, 
13 anthropologist Wade Davis said: 
All human populations share the same raw human genius, the same intellec-
tual acuity. And so whether that genius is placed into technological wizardry 
has been the great achievement of the West or by contrast, into unravelling 
the complex threads of memory inherent in a myth, is simply a matter of 
choice and cultural orientation. 
From a technological perspective, large-scale adoption of Linked Open Data 
could enable us to facilitate a revolutionary paradigm shift in information publica-
tion: to represent all these diﬀerent views of truth as equally valid. But are existing 
socio-economic, or power-driven paradigms simply too entrenched to prevent us 
from ever doing so? With thoughtful, critical engagement mitigating risks, the pros 
could outweigh the cons. Surely it’s worth giving it a go? 
Notes 
1 www.nytimes.com/2004/01/26/business/gates-predicts-that-spam-will-go-away.html. 
Accessed 27/05/2022. 
2 www.newsweek.com/clifford-stoll-why-web-wont-be-nirvana-185306. Accessed 
27/05/2022. 
3 https://babel.hathitrust.org/cgi/pt?id=mdp.39015056079984&view=1up&seq=219&q1= 
Tesla. Accessed 27/05/2022. 
4 Information published as W3C-compliant Linked Data is Findable, Accessible, Interop-
erable, and Reusable. 
5 www.w3.org/. Accessed 09/05/2022. 
6 WYSIWYG is an acronym that refers to a type of user interface. It means “What You 
See Is What You Get”. Most of us will be familiar with it in tools like MS Word or 
Google Docs: user-interfaces where you can aﬀect what you see on screen by clicking 
an icon. We could compare that to something like LaTeX text editors, where the changes 
to the document (making the text bold or in italics, for example) is achieved through 
a process of marking up one document (.tex) and then rendering those changes into a 
another (.pdf). 

      
     
    
      
 
  
       
    
    
      
 
 
 
 
  
 
 
  
 
  
 
 
 
  
  
 
 
 
 
 
 
  
 
  
 
  
 
  
118 Future Directions 
7 In the British sense, of being a task or area of activity assigned to a speciﬁc individual 
or organisation. 
8 www.youtube.com/watch?v=REWeBzGuzCc&ab_channel=CNN. Accessed 20/05/2022. 
9 https://nomisma.org/datasets. Accessed 20/05/2022. 
10 SPARQL (the SPARQL Protocol and RDF Query Language). What a name! This recur-
sive acronym (which contains “SPARQL” in it) refers to what could be considered the 
equivalent for RDF triples of what SQL (Structured Query Language) is for relational 
databases. Indeed many of the commands between SPARQL and SQL are the same 
(such as SELECT, ASK, CONSTRUCT, etc.), and SPARQL can be used to edit, manage, 
delete, add, and change RDF triples held in a graph database (rather than a relational 
database) or a triplestore. 
11 https://virtuoso.openlinksw.com/. Accessed 27/05/2022. 
12 https://blazegraph.com/. Accessed 27/05/2022. 
13 www.ted.com/talks/wade_davis_the_worldwide_web_of_belief_and_ritual/transcript. 
Accessed 29/05/2022. 
Bibliography 
Burrows, S., and Nurmikko-Fuller, T. (2020). “Charting Cultural History through Histori-
cal Bibliometric Research: Methods; Concepts; Challenges; Results”. In Schuster, K., 
and Dunn, S. (eds). Routledge International Handbook of Research Methods in Digital 
Humanities. Routledge. 
Gatti, T., Nurmikko-Fuller, T., Pickering, P., and Swift, B. (2022). “Having a Ball: A Linked 
Data Approach to Fancy Dress in Colonial Australia”. Proceedings of the International 
Digital Humanities Conference 2022 (DH2022), Tokyo, Japan, 27–29 July. 
Kranzberg, M. (1986). “Technology and History: ‘Kranzberg’s Laws’”. Technology and 
Culture, 27(3), pp. 544–560. 
Nurmikko-Fuller, T. (2018). “Publishing Sumerian Literature on the Semantic Web”. In Ju-
loux, V ., Gansell, A., and Di Ludovico, A. (eds). CyberResearch on the Ancient Near East 
and Neighboring Regions. Brill. 
Nurmikko-Fuller, T., Bangert, D., Hao, Y ., and Downie, J. S. (2018). “Swinging Triples: Bridg-
ing Jazz Performance Datasets Using Linked Data”. Proceedings of the 1st International 
Workshop on Semantic Applications for Audio and Music, Monterey, USA, 9 October. 
Nurmikko-Fuller, T., and Page, K. R. (2016). “The Linked Semantic Network That Is Trans-
forming Musicology”. Proceedings of the 1st Workshop on Humanities in the Seman-
tic Web – WHiSe, Co-located With the 13th Extended Semantic Web Conference 2016 
(ESWC) – Heraklion, Crete, Greece, 29 May. 
Nurmikko-Fuller, T., and Pickering, P. (2021). “Reductio ad Absurdum?: From Analogue 
Hypertext to Digital Humanities”. Proceedings of the 32nd ACM Conference on Hyper -
text and Social Media (ACMHT21), Dublin, Ireland, 30 August–02 September. 
Page, K., and Willcox, P. (2015). ElEPHã T: Early English Print in the HathiTrust, a Linked 
Semantic Worksets Prototype. Final Report for Workset Creation for Scholarly Analysis: 
Prototyping Project, University of Illinois at Urbana-Champaign. 
Simpson, R. M. (2020). “Augustine as ‘Naturalist of the Mind’”. In Proceedings of the 
31st ACM Conference on Hypertext and Social Media (ACMHT20), Virtual Event, USA, 
13–15 July. 
Wang, Q., Nurmikko-Fuller, T., and Swift, B. (2019). “Analysis and Visualisation of Nar-
rative in Shanhaijing Using Linked Data”. In Proceedings of the International Digital 
Humanities Conference 2019 (DH19), Utrecht, Netherlands, 9–12 July. 

     
   
     
    
 
 
     
   
     
    
        
        
          
  
     
 Glossary 
Algorithm A ﬁnite list of very rigorously deﬁned instructions so that a step-by-
step procedure for solving a problem, accomplishing a task, or performing a 
computation can be achieved. 
Australian Research Council (ARC) The primary non-medical research fund-
ing agency of the Australian government. 
Big Data A term used to refer to large datasets, which cannot be readily inter-
preted or analysed by humans, but require computational tools. 
CARE A data principle developed as the Indigenous response to the FAIR. 
CARE promotes the inclusion of people and human-centric considerations 
into the publication of data, and refers to Collective Beneﬁt, Authority to Con-
trol, Responsibility, and Ethics. CARE promotes Indigenous data sovereignty, 
and whilst it has many purpose-driven aspects (such as the need for evidence-
based policy development), the bulk of the focus is on people-oriented prin-
ciples, such as relationships, accountability, and the ability of stakeholder 
groups to exercise control over data that pertains to them. 
Comma Separated Value (CSV) A delimited text ﬁle that uses a comma to 
separate values. A spreadsheet and a CSV ﬁle can contain the same data in the 
former, it is displayed in cells (columns and rows), in the latter as a long line of 
text, where each value is not separated from the next one by a comma. 
Creative Commons (CC) A not-for-proﬁt organisation and international net-
work devoted to improving access to creative works by making them available 
through licences that enable legal sharing. 
Database Management System (DBMS) A software system that’s used to store 
data, as well as retrieve it and even run queries. Serves as the interface between 
the human end-user and the database. 
Domain In the Linked Data world, a Domain serves as the Subject for a 
property, that is to say, properties and predicates run from 
Domain (Subject) to Range (Object). In terms of Web architecture, a 
domain refers to a distinct subset of addresses sharing a common suﬃx. An 
academic domain is a recognised area of research or study. 
Extensible MarkUp Language (XML) As the name suggests, XML is a MarkUp 
language. It is used to store and transmit data that’s been encoded in a format 
that is accessible to both humans and software agents. 

    
   
    
   
     
    
    
 
   
    
  
    
   
   
  
 
    
 
       
   
   
120 Glossary 
FAIR A data principle that states that data should be Findable, Accessible, In-
teroperable, and Reusable. It also addresses metadata and supporting digital 
infrastructure, such as search engines. 
FRBRoo FRBR-Object-Oriented 
Graph Database A graph database stores information as nodes and relation-
ships, rather than as a collection of tables or documents. These graph struc-
tures are navigated using semantic queries. 
HathiTrust Digital Library (HTDL) The HathiTrust Digital Library is a large-
scale digital repository. Its collections are an amalgamation of collections 
from various research libraries, including content digitised by Google Books. 
International Organisation for Standardisation (ISO) A worldwide federa-
tion of national standards bodies. 
Knowledge Graph Also referred to as semantic networks, knowledge graphs 
represent data entities (such as people, places, events, or concepts) and the 
relationship between those data entities, forming an interconnected (often de-
centralised) graph or network. 
Luddite Now a blanket term to describe people who dislike computers and digi-
tal technology, the origins of the phrase date back to the 19th century. It was 
named for a movement of labourers who protested against the introduction of 
mechanised processes and machines, particularly in the textile industry. 
Mesopotamia Culturally and linguistically diverse historical region, which geo-
graphically constitutes the area of modern-day Iraq and the surrounding areas. 
Metadata A term that refers to data about (other) data. It applies to all kinds of 
ﬁles and resources, and often (but not exclusively) constitutes details such as 
creation date, size, and creator. 
Methodology A study or critical evaluation of a research method; can also refer 
to a system of methods used and applied in the context of a particular aca-
demic investigation or research process. 
Motif A dominant or recurring idea, especially in an artist’s work. 
Non-proprietary Generic, or something not registered or protected as a trade-
mark or brand name; data published as an MS Excel is in a proprietary for -
mat because the ﬁle can only be read using a speciﬁc piece of software. The 
equivalent data in a CSV ﬁle is in a non-proprietary format. 
Ontology In the Linked Data world, ontologies are ﬁles or conceptualisations 
that identify concepts and categories in a subject area or domain, show their 
properties and the relationships between these categories of subjects, and thus 
provide a self-referencing representation of the domain in question. In the 
Humanities, the term “ontology” is often used in the context of philosophi-
cal study of being: in this book, the word is only used to refer to the former 
(machine-readable document). 
RDF/XML RDF/XML is a syntax to express an RDF graph as an XML document. 
Semantic shift The phenomenon of language change regarding word usage, 
whereby meanings of words can change over time, sometimes becoming un-
recognisable or socially unacceptable. 
SQLite3 C library that provides a lightweight disk-based database. 

 
    
   
 
   
   
 
    
 
    
      
 
   
 
Glossary 121 
Sumerian Linguistic isolate; a now-dead language used in Mesopotamia for sev-
eral millennia BC. 
Syntax In the study of languages, syntax refers to the study of how sentences and 
phrases are formed from smaller linguistic units such as words. In Computer 
Science, the term refers to the structure of statements in a computer language. 
Tabular data Information organised in columns and rows. 
Tech Utopianism An ideology (or ideologies) based on the concept that ad-
vances in technology, engineering, and science could bring about a better fu-
ture (even a Utopia), or at least contribute to the advancement of a utopian 
ideal in a particular context. 
Triplestore A purpose-built database for the storage of RDF triples. Data can be 
retrieved, navigated, edited, and so forth, using semantic queries. They are a 
speciﬁc type of graph database. 
Wisdom literature A genre of literature common in the ancient Mesopotamian 
writings, consisting essentially of words of wisdom, that is, sayings, axioms, 
proverbs, and guidance. 
Workﬂow A sequence of steps or processes that need to be completed in a spe-
ciﬁc order so that a piece of work can be completed. 
Xquery Language for querying XML data. 

  
  
 
   
    
 
 
 
 
 
 
  
  
  
 
  
  
  
  
     
     
  
  
 
 
 
  
 
  
 
  
  
  
  
  
 
 
  
  
  
  
  
 
 
 
 
 
  
   
 
 
  
    
  
  
  
  
  
  
  
  
  
 
  
 Index 
6–9 meme 66 
Adobe Creative Cloud 51 
Adobe Systems 83 n7 
AHRC see Arts and Humanities Research 
Council (UK) 
AI see Artiﬁcial Intelligence 
Akkadian 83 n24,  84 n28 
algorithms: AI and machine learning  2 , 
115 ; false objectivity of  67 ,  104 ; 
glossary 119 ; Humanities data and 
105 ; increasing sophistication of 
19 ; racism and bias of  24 ,  108 ; 
surveillance by 36 ; as term, origin 
of 10 
algorithmic concepts 11 
al-Kindi 10 
Al-Khwarizmi, Mohammad ibn Musa 10 
Allemang, D. xiii 
Alphabet company 23 ,  83 n7,  107 
Analytical Engine 10 
anonymisation 32 – 33 ,  37 ,  108 
anonymity on the internet 23 
AR see Augmented Reality 
ARC see Australian Research Council 
Arlington National Cemetery 24 
Artiﬁcial Intelligence: ethics of  56 ; human 
cognition as a process, attempts to 
recreate by 86 ; human faces created 
by 2 ; machine learning and  2 ,  115 
Arts and Humanities Research Council 
(AHRC) (UK) 7 ,  9 – 10 ,  52 
Augmented Reality (AR) 24 
Australian Research Council (ARC) 7 , 
52 – 54 ; glossary  119 
Babbage, Charles10 
Banu Musa brothers 10 
Barber, Elizabeth  34 
Barry, Hank  42 
Barth, S. 29 
Bayt-al Hikmah (House of Wisdom)  10 
beauty as being in eye of the beholder 66 , 
70 ,  83 n8 
Beecher, Henry Ward  67 
“beer, free as in”  51 
Beer, D.  93 
Bentham, Jeremy 27 
Berners-Lee, Tim xi,  12 ,  55 
bias 66 – 83 ; algorithmic  24 ,  67 ; cognitive 
104 ,  114 ; in database design  108 ; 
deep-routedness of 81 ; gender  73 ; 
historical 104 ,  108 ,  117 ; inherent 
82 ,  115 ; internal  70 ; in ontological 
modelling 73 ; in ontologies  68 , 
69 – 71 ; ontologies and  15 ; overt 
or covert 68 ,  108 ; racist  24 ; in 
recommendation 99 ; removing 
56 ; in Software of Expertise  92 ; 
in tool recommendations 
90 – 93 ; 
unavoidable 75 ; unchecked  74 ; 
underlying 108; workﬂow  99 
Bibliographic Metadata Ontology (MODS) 60 
Bibliographic Metadata Ontology 
(extension to MODS) (MADS) 
60 ,  72 
Biblioteca Escolar Digital (CITA)  32 
‘Big Bad’ 23 
Big Data 44 ,  93 ; glossary  119 
bigotry 108 
biometric information 31 
Bishop, C. 2 ,  49 
Body and Soul discography 95 – 96 
Bonewell, Perry 88 
Bongiorno, F.  57 
Brand, Stewart 53 
Brewster, C.  16 ,  67 
British Broadcasting Corporation (BBC) 
6 ,  27 

 
  
  
  
  
  
  
  
 
  
     
 
 
       
  
  
    
  
  
       
  
  
 
 
  
    
 
  
  
 
  
  
  
 
  
     
 
       
  
  
     
 
 
  
  
  
  
  
 
  
 
 
    
 
 
  
 
 
 
 
  
  
  
   
 
     
  
  
  
  
     
  
  
 
 
 
  
   
 
  
 
 
  
 
 
  
  
  
Index 123 
Buddhist thought 87 
Burrows, S. 105 
Busa, Roberto 10 
Bush, Vannevar  17 ,  89 
Byron (Lord) 11 
Cambridge Analytica  26 – 27 ,  34 – 35 
CARE (Collective beneﬁt, Authority to 
control, Responsibility, Ethics) data 
principles 36 ,  56 ; glossary  119 
Cauberghe, V .  29 
CC see Creative Commons 
CC Attribution-ShareAlike  4 .0 
International Licence 58 
CEO see Chief Executive Oﬃcer 
Chalmers, D. 87 
Charteris, Martin (Sir) 57 
Chief Executive Oﬃcer (CEO)  24 
Chomsky, [N.]  86 
CIDOC CRM see International Council of 
Museums (ICOM)’s Conceptual 
Reference Model 
CITA see Biblioteca Escolar Digital 
Clark, A.  87 
cloud computing 28 
Cloud, the 32 ,  100 ; Adobe Creative 
Cloud 51 
Collective beneﬁt, Authority to control, 
Responsibility, Ethics  see CARE 
comma separated value (CSV) 12 ,  53 , 
95 – 96 ; glossary  119 
Commonwealth Scientiﬁc and Industrial 
Research Automatic Computer 
(CSIRAC) 11 
copyright law 42 – 43 ,  51 
copyright restrictions 52 ,  59 – 61 ,  96 ,  107 
COVID-19 29 
Creative Commons (CC) 51 ; CC 
Attribution-ShareAlike 4 .0 
International Licence 58 ; glossary 
119 
CSIRAC see Commonwealth Scientiﬁ c 
and Industrial Research Automatic 
Computer 
CSV see comma separated value 
Cunningham, G. 48 
D2RQ Platform 96 
Dante’s  Inferno 1 
Database Management System (DBMS); 
glossary 119 
Dallas, C. 12 
Dark Ages  10 
dark energy  48 
dark matter 48 
Dark Web  27 
data 43 – 50 ; accessible and inaccessible, 
combining 58 – 59 ; ambiguous  47 – 48; 
incomplete 48 – 49 ; interpreting 
of, as Humanities research output 
44 ; location  33 – 34 ,  61 ; messy 
49 – 50 ; quantitative  43 ; quantitative 
analysis of 44 ; tabular  95 – 96 ; 
unreproducible 45 – 46 ; unstructured 
46 – 47 ;  see also Big Data ;  Linked 
Data ;  metadata ;  Open Data ; Web 
of Data 
data aggregation 36 ,  62 
data capture 95 – 96 ; Linked Data and  19 , 
110 ,  
113 – 114 ; supposed neutrality 
of 108 
Data Economy 19 ,  26 – 27 ,  31 ,  37 – 38 ,  53 , 
116 
data fetishist 33 
data producers and consumers 30 – 32 
data proﬁling  25 – 26 ,  35 ,  116 
data scraping see scraping 
DBMS see Database Management System 
DBpedia 32 
De Jong, M. 29 
de la Rosa, J. 2 
Descartes, [R.] 86 
DHer see digital humanities researcher 
Digging into Data Challenge 43 
Digital History 8 
Digital Humanities: computer science and 
10 – 12 ; interdisciplinarity and  2 – 4 , 
6 ,  18 – 19 ; linked data and  12 – 18 ; 
linked data in 109 – 117 ; non-linear 
approach to discussing linked data 
in 104 – 109 ; public face of  10 ; 
research funding for 7 – 8 ; Rodin’s 
Gates of Hell and 1 – 2 ,  18 ; Rodin’s 
Thinker and 1 ; two cultures of  9 ,  19 
digital humanities researcher (DHer) xv, 
96 ,  100 
diversity and ambiguity, reductionist 
attempts to eliminate 81 
diversity and inclusion 36 ; gender  74 
domain 1 – 2 ,  15 ,  113 ; Cross Domain  32 , 
39n27 ; data  109 ; disciplinary  117 ; 
glossary 119 ; mapped  114 ; range 
and 68 ; subdomains (HASS)  44 , 
48 ; subject  69 
domain experts and expertise 6 ,  48 ,  105 
domain ontologies 68 

   
  
  
 
  
 
 
  
 
 
    
 
 
  
 
  
      
 
 
 
     
  
  
  
 
 
 
 
 
  
  
 
 
  
  
  
 
 
  
  
     
     
  
    
    
 
  
  
  
  
  
 
 
  
 
  
  
  
  
  
 
 
  
  
  
  
     
   
   
 
  
  
  
  
    
 
  
 
  
 
 
 
  
  
       
   
  
 
  
       
  
124 Index 
domain-speciﬁc outcomes  4 ,  68 ,  71 
Drupal 88 
DuCharme, B. xiii, 67 ,  69 ,  97 
Early English Books Online Text Creation 
Partnership (EEBO-TCP) 59 – 61 , 
106 – 107 
Early English Print in HathiTrust, Linked 
Semantic Worksets Prototype 
(ElePHã T project)  59 – 62 ,  63 ,  107 
EEBO-TCP see Early English Books 
Online Text Creation Partnership 
Electronic Text Corpus of Sumerian 
Literature (ETCSL) 76 – 80 
ElePHã T project  see Early English Print 
in HathiTrust, Linked Semantic 
Worksets Prototype  
Engineering and Physical Sciences 
Research Council (EPSRC) (UK) 
7 ,  9 – 10 
EPSRC see Engineering and Physical 
Sciences Research Council (UK) 
Estill, L. 36 
ETCSL see Electronic Text Corpus of 
Sumerian Literature 
ethics 23 – 38 ; CARE and  56 ,  119 ; question 
of 36 – 37 
EU see European Union 
European Economic Area (EEA)  28 
European Union (EU) 28 
Extended Mind thesis 87 
Extensible MarkUp Language (XML) 
59 – 60 ,  93 – 94 ,  110 ; glossary  119 
Extensible Stylesheet Language 
Transformations (XSLT)  93 
Facebook xi, 23 ,  25 – 27 ,  31 ,  92 ; Cambridge 
Analytica scandal 27 ,  34 – 35 ; 
#delete/DeleteFacebook 34 ; domination of 
44 ; Zuckerberg  27 ,  70 
facial recognition 2 
FAIR (Findable, Accessible, Interoperable, 
Reusable) principles 53 ,  55 ,  56 ; 
glossary 120 
Fear of Missing Out (FOMO) 29 ,  35 
Field of Research (FOC, for the ARC)  7 
Filter Bubble 31 
Findable, Accessible, Interoperable, 
Reusable see FAIR principles 
FindFace 24 
Five Star Standard 12 ,  52 – 56 ,  95 ,  110 ,  115 
FOAF see Friend of a Friend 
FOMO see Fear of Missing Out 
Foucault, Michel 16 – 17 
Foucault Eﬀect (Beer) 93 
FRBR see Functional Requirements for 
Bibliographic Records 
“free, as in beer” 51 
free, meaning of 53 
Free Software Foundation 51 
Friend of a Friend (FOAF) 74 
Functional Requirements for Bibliographic 
Records-Object-Oriented 
(FRBRoo) 45 ,  60 ,  77 ,  79 ; 
glossary 120 
Galleries, Libraries, Archives, and 
Museums (GLAM) sector 47 , 
56 – 57 ,  68 ,  87 – 89 ,  99 ,  106 
Gatti, T.  115 
gender balance 
108 
gender bias 73 
gender binary 75 ,  79 – 80 ,  108 
General Data Protection Regulation 
(GDPR)(EU) 28 
Genesis, Book of 75 
Getty V ocabularies  36 
GLAM see Galleries, Libraries, Archives, 
and Museums (GLAM) sector 
Global Positioning System (GPS) 33 
GPS see Global Positioning System 
Graphical User-Interface (GUI)  98 ,  106 ,  115 
Greenﬁeld, A.  24 ,  46 
Group of Eight (Go8) 8 ,  20 n12 
Gruber, T.  15 ,  67 
Hacker’s Conference 1984  53 
Hafeez, Kaamran 23 
Hall, Wendy (Dame)  11 – 12 
HASS see Humanities, Arts, and Social 
Sciences 
Hastings, Reed 70 
HathiTrust Digital Library (HTDL)  59 – 62 , 
65 ,  106 – 107 ; glossary  120 
Hendler, J. xiii 
historiographies, of sciences and 
humanities 9 
Hocking, Jenny 57 
Hooland, S. van xiii, 91 ,  94 
HTDL see HathiTrust Digital Library 
Humanities 11 ; methodology of  9 ;  see also 
Digital Humanities 
Humanities, Arts, and Social Sciences 
(HASS) 2 – 10 ,  16 ,  19 ,  44 ,  48 ,  104 , 
116 
HTTP see HyperText Transfer Protocol 
HTTPS see Hypertext Transfer Protocol 
Secure 

 
  
  
 
 
 
  
  
  
  
  
   
  
  
  
 
 
 
  
  
  
 
 
     
  
    
 
 
 
     
  
  
  
  
  
 
  
 
  
 
 
 
 
 
 
 
  
  
     
 
 
  
  
  
 
 
 
 
 
 
 
 
 
 
 
 
 
  
  
  
  
 
  
   
hyperdata 16 
hypernyms and hyponyms 68 
hypertext 19 ,  44 ,  106 ; graph-based  89 ; 
obsolete 99 ; systems  11 
HyperText Transfer Protocol (HTTP) URIs 
13 – 14 ,  32 ,  94 ,  111 – 113 
Hyppö nen, Mikko  26 ,  33 
Hyvö nen, E. xiii,  67 
IBM see International Business Machines 
Corporation 
Index Thomisticus  10 
inﬂuencers  28 
information retrievers 31 
Instagram 28 ,  30 ,  35 ,  44 
interdisciplinary 2 – 5 
International Business Machines (IBM) 
Corporation 10 
International Council of Museums 
(ICOM)’s Conceptual Reference 
Model (CIDOC CRM) 45 – 46 ,  69 , 
71 ,  77 – 79 
JazzCats 91 ,  94 – 97 ,  99 – 100 
JavaScript Object Notation (JSON) 110 
JavaScript Object Notation (JSON) for 
Linking Data 110 
J-DISC see Online Jazz Discography 
Jenner, Kylie  28 
JISC see Joint Information Systems 
Committee 
Joint Information Systems Committee 
(JISC) 61 
JSON see JavaScript Object Notation 
JSON-LD see JavaScript Object Notation 
(JSON) for Linking Data 
Kant, [I.] 86 
Kardashian family 28 
Kardashian, Kim 28 
Kerr, John  57 
Kranzberg’s First Law  67 ,  88 ,  100 n4 
Kawase, R. 30 
knowledge 13 ; capture of  114 ; domain-
speciﬁc  68 ; theory of  17 
Knowledge Graph 17 ,  55 ,  93 – 95 ,  105 – 107 , 
109 ; glossary  120 ; interconnected, 
knowledge inferred from 117 ; 
SPARQL and  97 – 98 ,  113 
Knowledge Representation (KR) 55 , 
67 ,  88 ; bias in  116 ; Networked 
Environment for Personalized, 
Ontology-Based Management of 
Uniﬁed Knowledge (NEPOMUK) 
Index 125 
Contact Ontology 74 ; Networked 
Knowledge Organization Systems 
(NKOS) 36 ; systems of  18 
knowledge reputation 108 
knowledge structures 99 ; Western  28 
KR see Knowledge Representation 
LGBTQIA+ (Lesbian, Gay, Bisexual, 
Transgender, Queer, Intersex, 
Asexual, Pansexual) 74 
Liccardi, I. 34 
Linked Art  69 
Linked Art Model  69 
Linked Data: ambiguity and vagueness 
using 18 ; case study, Sumeria 
literary compositions and 75 – 77 ; 
categorization of projects 20 n10; 
Data Economy and 31 ; demands 
of data and 92 – 100 ; divided 
data and 44 ; era of  31; ﬂexibility 
of 19 ,  94 ; future directions 
103 – 117 ; Humanities and  12 – 19 ; 
information exchange facilitated 
by 72 ; interconnectedness of 
103 ; interconnected thinking via 
88 – 90 ; JazzCats as example of 
91 ; Kranzberg’s First Law and 
67 ; Linked Open Data and  54 – 56 , 
62 ; new knowledge inferred via 
87 ; ontological modelling for 
70 ; ontologies  69 ; paradigm  67 ; 
potential for privacy disaster posed 
by 32 – 33 ,  107 ,  116 ; practical 
considerations for implementation 
of 106 ; privacy and ethical issues 
raised by 26 ,  36 – 37 ,  107 ,  116 ; 
problems potentially solved by 
48 ; publication paradigm  82 ,  93 , 
104 – 105 ; raison d’etre of  32 – 33 ; 
sceptics 98 ; SPARQL and  98 ; 
tech-focused summary of digital 
humanities and 109– 115 ; workﬂow 
91 ,  116 ;  see also Five Star Linked 
Data Standard 
LinkedIn 44 
Linked Jazz project 95 ,  97 ,  100 
Linked Open Data 92 ; community  57 ; Linked 
Data and 54 – 56 ,  62 ; Five Star 
Standard for 52 ,  53 ; ontologies  69 
Linked Open Data Cloud 32 
Linked Semantic Worksets Prototype  see 
Early English Print in HathiTrust, 
Linked Semantic Worksets 
Prototype 

  
  
  
  
  
  
 
  
  
  
  
  
 
 
 
 
 
 
      
 
 
  
  
  
  
    
 
  
  
  
  
      
 
  
 
 
 
  
 
 
 
 
 
 
    
 
  
 
 
 
    
 
 
 
  
     
  
  
  
  
       
 
 
 
 
 
   
 
 
 
 
  
  
    
 
  
  
 
 
126 Index 
Lovelace, Ada  10 – 11 ,  19 
Luddite 5 ,  115 ,  116 ; glossary  120 
MADS see Bibliographic Metadata 
Ontology (extension to MODS) 
March, E. 29 
Marx, Karl 27 
Marxism 73 ,  105 
memes 201 n1,  23 ,  69 ,  82 n1 
Memex 17 ,  89 
memory institutions 87 
Menabrea, Luigi 11 
Mesopotamia 75 ,  79 ,  81 ,  83 ; glossary  120 
Meta (formerly Facebook) 107 
metadata: bibliographic 79 ; Bibliographic 
Metadata Ontology (MODS) 60 ; 
Bibliographic Metadata Ontology 
(extension to MODS) (MADS) 60 , 
72 ; cultural heritage collections 
36 ; ElePHã T project (bibliographic 
metadata) 59 – 62 ,  63 ,  107 ; glossary 
120 ; museum object  32 ; National 
Statement on Ethical Conduct 
in Human Research regarding 
43 ; unreproducible data and  45 ; 
unstructured data and 46 
Metallica v. Napster 42 – 43 
methodology: glossary 120 ; HASS  44 ; 
Linked Data xiii–xiv,  1 – 2 ,  9 ,  32 , 
36 ,  37 ,  93 ; Linked Open Data  107 , 
109 ; mindmap  106 
Microcosm 12 
Minecraft 52 
Misa, T.  11 
MODS see Bibliographic Metadata 
Ontology 
monetisation 27 
Moore, K. 29 
motif 1 ,  23 ,  75 – 76 ,  80 ; glossary  120 
Musk, Elon 44 
MySQL see Open-Source Relational 
Database Management System 
Napster 42 – 42 
Narayen, Shantanu 83 n7 
National Statement on Ethical Conduct in 
Human Research 43 
NEPOMUK see Networked Environment 
for Personalized, Ontology-Based 
Management of Uniﬁed Knowledge 
(NEPOMUK) Contact Ontology 
Networked Environment for Personalized, 
Ontology-Based Management of 
Uniﬁed Knowledge (NEPOMUK) 
Contact Ontology 74 
Networked Knowledge Organization 
Systems (NKOS) 36 
NKOS see Networked Knowledge 
Organization Systems 
Nomisma.org project 98 ,  110 
non-proprietary: data 53 ; format  95 ; 
glossary 120 ; software  53 
Nurmikko-Fuller, Terhi  17 ,  25 ,  44 ,  90 , 
100 n5,  
106 ,  110 ;  see also Burrows ; 
Pickering 
Object see Subject and Object 
objects: collecting 89 ; digital  52 ; inanimate 
86 ; material  32 ,  43 ,  46 ; multimedia 
45 ; museum  57 ,  77 – 79 
OCR see Optical Character Recognition 
O’Hara, K. 29 
oligopolies 23 ,  107 
O’Malley, Katie  34 
Online Jazz Discography (J-DISC) 95 
online oligopolies see oligopolies 
ontolog* (ontology, ontologies, 
ontological) 67 – 82 ,  106 ; 
bibliographic metadata 60 ; Beecher 
67 ; bias in  69 – 71 ; “borrowing” of 
term from philosophy 17 ; classes 
and properties of 68; deﬁnition 
of 15 ,  67 – 70 ; development and 
developers 116 – 117 ; DuCharme  68 ; 
FRBRoo 45 ; glossary  120 ; Gruber 
15 ,  67 ; Hyvö nen  67 ; mapping  49 ; 
Linked Data 113 – 114 ; modelling 
73 ,  95 ; Music Ontology  95 ; 
representation 69 ,  77 – 81 ; Semantic 
Web and  67 ;  see also Functional 
Requirements for Bibliographic 
Records ;  International Council of 
Museums (ICOM)’s Conceptual 
Reference Model ;  MADS ;  MODS ; 
NEPOMUK ;  OntoMedia ontology ; 
OWL ; PROVO-O 
ontological structures 16 – 18 ,  46 ,  60 ; 
data-driving 100 ; underlying  79 
OntoMedia ontology 18 ,  77 ,  79 – 80 
Open Access  51 ,  52 
Open Data 51 ,  53 – 54 ;  see also Linked 
Open Data 
openness 50 – 56 
Open Source 51 ,  52 
Open-Source Relational Database 
Management System (MySQL) 93 

 
  
  
       
  
 
  
     
 
  
  
   
     
  
 
  
 
 
  
 
  
  
 
  
     
 
 
 
  
  
   
   
  
     
  
  
      
   
 
 
    
 
     
  
    
  
  
 
 
  
  
 
 
  
 
 
 
 
 
 
 
 
 
  
  
  
  
  
 
 
 
  
  
  
  
  
 
 
 
  
  
  
Index 127 
Optical Character Recognition (OCR) 49 
Orwell, George  24 – 27 
OWL see Web Ontology Language 
Paciﬁc And Regional Archive for Digital 
Sources in Endangered Cultures 
(PARADISEC)  58 
Panopticon 27 
PARADISEC  see Paciﬁc And Regional 
Archive for Digital Sources in 
Endangered Cultures 
Pariser, Eli  31 
Parker, Trey  42 
Patﬁeld, S.  6 
PDF see Portable Document Format 
Peroni, Silvio 18 
perspective (s): blinkered 92 ; business 
model 51 ; contemporary cultural 
73 ; data privacy  35; diﬀerent  4 , 
36 ,  59 ; diverse  74 ; inherent  115 ; 
Linked Data 82 ,  107 ; Marxist 
105 ; modern  76 ; musicology  95 ; 
technological 13 ,  117 ; Western 
70 ,  81 
Pichai, Sundar 83 n7 
Pickering, P.  17 ,  25 ,  100 n5,  106 
PokemonGo! 24 ,  52 
Portable Document Format (PDF) 49 , 
53 ,  95 
PR see public relations 
privacy 19 ,  23 – 38 ,  56 ; case for  58 ; 
data management and 98 ; data 
publication and concerns regarding 
57 ; death of  23 ; Linked Data as 
potential catastrophe for 26 ,  36 – 37 , 
107 ,  116 ; as right not privilege 
26 – 28 ;  see also anonymisation 
Privacy Paradox 28 – 30 ,  35 ,  108 
proﬁles, social media  25 ,  27 ,  29 ,  35 
proﬁling: data  25 – 26 ,  31 ,  35 ,  116 
Provenance Ontology (PROV-O)  71 
PROV-O  see Provenance Ontology 
Pubby 98 
public relations (PR) 59 
QS see Quantiﬁed Self 
Quantiﬁed Self (QS)  33 
Query Builder with Natural Language 
Processing (SPARKLIS)  98 
RDBMS see relational database 
management system 
RDF see Resource Description Framework 
RDFS see Resource Description 
Framework Schema 
RDF/XML 93 ,  110 ; glossary  120 
Reddit 26 ,  44 
Reeves, T.  3 
relational database management system 
(RDBMS) 93 
Repko, A.  3 
ResearchGate 44 
Resource Description Framework (RDF): 
data converted to 60 – 62 ; Five 
Star Linked Data and 115 ; graph 
structure 94 ; instance-level  91 ; 
Linked Data and 110 ; ontologies 
as 68 ,  114 ; MADS-RDF ontology 
72 ; metadata  93 ; RBDMS as  93 ; 
RDF/XML 93 ,  110 ,  120 ; “simple” 
process to produce 99 ; W3C 
standards 55 – 56 
Resource Description Framework Scheme 
(RDFS) 69 ,  71 ; examples of  112 
Resource Description Framework (RDF) 
triple 13 – 14 ,  15 – 16 ,  19 ,  32 ; Body & 
Soul workﬂow  100 ; inherent 
ﬂexibility and robustness of  106 ; 
jazz recording 95 ,  96 – 98 ; querying 
61 ; semantic queries  111 ; skills 
to create 105 ; SPARQL and  113 ; 
storing 93 – 94 ; Terse RDF Triple 
Language 96 ,  110 
Rodin, Auguste  1 – 2 ,  18 
Russia 24 ,  54 
Sacks, Oliver 87 
Sarandos, Ted  70 
Schö ch, C.  46 
Science, Technology, Engineering, 
Mathematics (STEM) 2 – 11 ,  19 ,  116 
Science, Technology, Engineering, Arts, 
Mathematics (STEAM) 4 ,  20 n3 
scraping (of data) 26 – 27 ,  44 
Semantic Lab, Pratt 97 
semantic models 15 
semantics 113 ; embedded  111 
semantic shift 36 ; glossary  120 
Semantic Web  16 ,  18 ,  32 ,  54 – 44 ,  82 , 
103 ,  117 ; Foucault and  16 – 17 ; 
ontological modelling for 70 ; 
ontologies as crucial to 67 ; OWL 
as tool and language of 14 ,  69 ; 
RDFS as language of 69 ;  see also 
ElePHã T project  
Shakespeare, William  6 ,  13 – 15 

     
  
  
  
  
  
  
  
 
  
 
  
   
  
    
 
 
 
 
  
  
  
  
       
  
  
  
    
 
    
 
  
  
  
 
  
  
     
  
  
  
  
  
    
 
  
  
     
  
  
   
 
  
  
 
 
  
  
  
  
  
 
 
 
  
  
       
  
  
  
   
  
  
 
 
    
      
    
  
     
  
  
      
 
  
  
   
   
  
  
  
  
128 Index 
SIG see Special Interest Group 
Silicon Valley  70 ,  81 
Simpson, R. 16 ,  89 
Smith, David 57 
Snow, C.: Two Cultures theory of  5 – 10 ,  19 
social feminist theory 5 
social engagement 31 
social judgement 80 
social media 23 – 25 ,  27 – 29 ,  35 – 37 ,  92 ; 
Linked Data and 108 ; as coping 
mechanism 29 ; data  44 ;  see also 
Facebook; Instagram ;  inﬂuencers ; 
proﬁles, social media ;  Reddit ; 
TikTok ; Twitter 
social networking 34 
SPARKLIS  see Query Builder with Natural 
Language Processing 
SPARQL (SPARQL RDF and Query 
Language) 12 ,  118 n10; endpoint  61; 
queries 61 ,  100 ,  106 ,  110 ,  112 – 113; 
querying across three datasets using 
97 – 98 ; SQL compared to  93 
SPARQL Protocol  55 ,  97 
Special Interest Group (SIG) 88 
Spotify 43 ,  52 
SQL see Structured Query Language 
SQLite3 96 ; glossary  120 
Stallman, Richard 51 
Steiner, Peter  23 
STEM see Science, Technology, 
Engineering, Mathematics 
STEAM see Science, Technology, 
Engineering, Arts, Mathematics 
Steam platform 52 
Stone, Matt 42 
Strava 33 – 36 
Structured Query Language (SQL) 49 ,  98 , 
118 ; SQLite3  96 ,  120 
Suá rez, J.  2 
Subject see Domain 
Subject and Object 13 ,  17 ,  110 
subject domain 69 
Subject-Predicate-Object 13 ,  110 
Subject-Verb-Object (SVO)  13 
Sumerian: glossary 120 
Sumerian literature see Electronic Text 
Corpus of Sumerian Literature 
surveillance capitalism 27 ,  31 
surveillance technology 24 – 25 ,  29 ,  35 – 36 
SVO see Subject-Verb-Object 
syntax 93 ,  97 ,  110 ,  112 ; glossary  121 
Szostak, R. 3 
tabular data 46 ,  47, 49 ,  91 ,  
93 – 94 ; Body 
and Soul discography 95 – 96 ; 
glossary 121 ; JazzCats  97 ,  99 ; 
as knowledge structure 98 ; Web 
Karma 96 
tubular database 100 
tabular dataset 12 ,  53 
tech utopianism 53 ,  57 ,  100 ,  107 – 108 ,  115 ; 
glossary 121 
Terse RDF Triple Language (TTL)  96 ,  110 
Three Wise Monkeys  38 
Trump, Donald  26 
Thune, [John] 27 
TikTok  30 – 31 ,  44 
triplestore 89 ,  93 – 94 ,  99 – 100 ,  105 , 
110 – 111 ,  114 – 116 ; glossary  121 ; 
JazzCat 97 
Truce Village, Korea  24 
trust 23 – 38 ,  56 ,  98 
TTL see Terse RDF Triple Language  
Turtle syntax  97 ,  110 ,  112 
Twitter and tweeting  26 ,  30 ,  44 ,  92 
Ulrich, Lars 42 
Uniform Resource Identiﬁer (URI) 
xvii, 14 
Uniform Resource Locator (URL) xvii, 14 
Uniform Resource Number (URN) 
xvii, 14 
United States Senate hearings: Facebook 
data privacy 27 ;  Metallica v. 
Napster 42 
URI see Uniform Resource Identiﬁer 
URL see Uniform Resource Locator URN 
see Uniform Resource Number 
utopian ideal see tech utopianism 
vagueness 18 ,  67 ,  104 
Verborgh, R. xiii,  91 ,  94 
VIAF see Virtual International Authority File 
Virtual International Authority File (VIAF) 
12 ,  15 
Vkontakte 24 
W3C see World Wide Web Consortium 
(W3C) standard 
web see World Wide Web Consortium 
(W3C) standard 
web crawling or scraping 44 
Web of Data  16 ,  18 ,  109 
Web of Documents  18 
Web Karma software  96 

 
  
  
  
 
  
  
  
  
  
  
  
 
  
  
    
 
      
  
     
  
      
 
  
   
       
Web Ontology Language (OWL)  69 
Web Science  4 
WhatsApp 35 
What You See Is What You Get 
(WYSIWYG) 106 ,  117 n6 
Wiederhold, B.  29 
Wilks, Y .  16 ,  67 
Wisdom, House of  10 
Wisdom Literature  80 ; glossary  121 
Wittgenstein, L.  13 – 16 
WordPress  88 
workﬂows  12 ,  31 ,  46 ,  60 ; designing  91 ; 
glossary 121 ; JazzCat  99 – 100 ; 
Linked Data 91 ,  108 ,  110 ,  114 – 116 ; 
PARADISEC  58 ; RDF  94 – 97 ; 
research 54 ; Weimar Jazz  96 ,  100 
Index 129 
World Wide Web Consortium (W3C) standard 
xiv,  12 ,  32 ,  55 ,  105 ,  109 ,  115 
WYSIWYG see What You See Is What 
You Get 
XML see Extensible MarkUp Language 
(XML ) 
XML Path Language  93 
Xpath see XML Path Language  
Xquery 93 ; glossary  121 
XSLT see Extensible Stylesheet Language 
Transformations  
Zeng, Marcia Lei 47 
Zuboﬀ, S.  27 ,  29 ,  31 
Zuckerberg, Mark  27 ,  70
