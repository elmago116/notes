---
authors:
  - Sumi Helal
source: Crossref
type: journal-article
base: clippings
title: Democratizing AI and IoT Through Software Services Engineering
year: 2023
doi: 10.1109/sse60056.2023.00036
url: https://doi.org/10.1109/sse60056.2023.00036
journal: 2023 IEEE International Conference on Software Services Engineering (SSE)
publisher: IEEE
last_enrichment_run: 2025-08-20
updated: 2025-08-20
tags:
  - tech/Ai
  - themes/democratizing
apa_citation: Sumi Helal, 2023
---

## PDF text extraction

Journal of Computer Science and Technology Studies  
ISSN: 2709-104X 
DOI: 10.32996/jcsts 
Journal Homepage: www.al-kindipublisher.com/index.php/jcsts 
   JCSTS  
AL-KINDI CENTER FOR RESEARCH  
AND DEVELOPMENT  
 
Copyright: © 2025 the Author(s). This article is an open access article distributed under the terms and conditions of the Creative Commons 
Attribution (CC-BY) 4.0 license (https://creativecommons.org/licenses/by/4.0/). Published by Al-Kindi Centre for Research and Development,  
London, United Kingdom.                                                                                                                          
    Page | 556  
| RESEARCH ARTICLE 
Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution 
of No-Code Development 
 
Akhilesh Gadde 
Stony Brook University, USA 
Corresponding Author: Akhilesh Gadde, E-mail: innovateakhilesh@gmail.com 
 
| ABSTRACT 
The integration of generative artificial intelligence (AI) into software development processes represents a paradigm shift in how 
individuals interact with technology creation tools. This article examines the emergence of intuitive programming approaches 
colloquially termed "vibe coding" alongside traditional no-code and low code platforms, analyzing their combined potential to 
democratize software engineering practices. Through systematic analysis of current research, It identifies key technological 
frameworks, implementation challenges, and potential socioeconomic implications of AI -assisted development environments. 
The article findings suggest that generative AI fundamentally transforms the accessibility paradigm by bridging natural language 
expression with functional software creation, potentially reducing traditional barriers to entry while introducing new 
considerations regarding technical depth, sustainability, and equity in software production ecosystems. 
| KEYWORDS 
generative artificial intelligence, no -code development, software democratization, human -computer interaction, intuitive 
programming, vibe coding  
| ARTICLE INFORMATION 
ACCEPTED: 14 April 2025                               PUBLISHED: 17 May 2025                  DOI: 10.32996/jcsts.2025.7.4.66 
 
I. Introduction 
Software engineering has traditionally required specialized technical knowledge, creating significant barriers to participation for 
individuals without formal programming education. The evolution from command -line interfaces to graphical integrated 
development environments (IDEs) represented early attempts to improve accessibility, but fundamental coding competenci es 
remained essential [1]. Recent advancements in generative artificial intelligence, particularly large language models (LLMs) with 
code generation capabilities, are potentially redefining this paradigm by enabling intuitive, natural language -based softwa re 
creation processes [2]. 
The concept of democratizing software development —making it accessible to broader demographics regardless of technical 
background—has gained momentum through successive waves of technological innovation. No -code and low -code platforms 
initially addressed this need by providing visual programming environments with pre -built components [3]. However, these 
systems often presented limitations in customization and scalability that restricted their application domains [4]. 
Generative AI  potentially transcends these limitations through what industry practitioners have termed "vibe coding" —using 
natural language to express desired functionality while AI systems translate these conceptual "vibes" into functional code [5]. This 
approach represents a significant departure from traditional software engineering paradigms, potentially enabling individuals to 
create software through intention and desired outcomes rather than explicit programming syntax. 
This article examines the current state and future trajectory of this democratization process, analyzing: 
1. The technological foundations enabling AI-assisted intuitive programming 

JCSTS 7(4): 556-572 
 
Page | 557  
2. Current implementation frameworks and their limitations 
3. Emerging patterns in user interaction and productivity 
4. Socioeconomic implications of broadened software creation access 
5. Potential transformations in software engineering education and practice 
To systematically investigate this emerging paradigm, we formulate the following research questions: RQ1: How do generative AI-
powered approaches fundamentally alter the accessibility of software engineering compared to traditional programming and no-
code/low-code platforms? RQ2: What are the emergent interaction patterns and cognitive processes that characterize effective 
"vibe coding" practices in both educational and professional contexts? RQ3: What technical and societal challenges might impede 
the sustainable adoption of AI-assisted intuitive programming approaches? RQ4: What theoretical frameworks best elucidate the 
democratizing potential of natural language programming interfaces? 
This analysis employs a systematic literature review methodology following established PRISMA protocols [60]. Our search strategy 
encompassed major academic databases (ACM Digital Library, IEEE Xplore, Scopus) using predetermined search strings combining 
terms related to "generative AI," "software democratization," "no -code development," and "natural language programming." We 
included peer-reviewed publications till April 2025 with direct relevance to AI in software engineering democratization, excluding 
purely technical implementations without democratization implications.  
 
Fig. 1. PRISMA flow diagram illustrating the systematic literature review process. 


Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 558  
The PRISMA diagram illustrates our review p rocess: we identified 487 records through database searches. After removing 
duplicates, 412 records remained for screening. We then assessed 175 full -text articles for eligibility, and ultimately included 112 
studies in the final qualitative synthesis. Of these, only 90 papers are directly cited in the manuscript and listed in the references 
section. 
II. Background and Historical Context 
A. The Evolution of Software Development Accessibility 
Software development accessibility has evolved through distinct phases of technological innovation. The earliest programming 
interfaces required direct machine code manipulation, gradually transitioning to assembly languages, then higher -level 
programming languages that abstracted machine -specific details [6]. Each evo lutionary stage reduced knowledge barriers while 
expanding potential developer populations. 
The introduction of visual programming environments in the 1990s represented a significant shift toward intuitive interfaces, with 
systems like Visual Basic enablin g drag -and-drop component arrangement alongside traditional coding [7]. These hybrid 
environments remained primarily utilized by professional developers but demonstrated the potential for visual abstraction in 
software creation. 
 
Fig. 2. Evolution of Programming Paradigms Toward Democratization 
The diagram illustrates the progressive transformation of software development approaches across four historical 
phases:Traditional Programming (1950s-1990s) evolving from machine code to object -oriented languages; Visual Programming 
(1990s-2000s) featuring drag-and-drop interfaces; No-Code/Low-Code platforms (2000s-2020) incorporating visual modeling and 
pre-built components; and culminating in Vibe Coding with Generative AI (2023 -Present) characterized by natural l anguage 
prompts and LLM code generation. Each paradigm demonstrates increasing accessibility and reduced technical prerequisites, with 
vibe coding representing a fundamental shift toward intent-based programming [6, 7, 8, 25, 30, 41]. 
B. The No-Code/Low-Code Movement 
The no-code/low-code movement emerged in the early 2000s as a direct response to increasing demand for software solutions 
amid limited developer availability [8]. Platforms such as Microsoft PowerApps, Bubble, and Airtable enabled business user s to 
create functional applications through configuration rather than coding [9]. This approach democratized basic application 
development but typically imposed limitations in customization, scalability, and performance optimization. 
Research by Bucchiarone et al. identified key characteristics of successful low -code platforms: visual modeling capabilities, pre -
built templates, integration frameworks, and deployment automation [10, 11]. These systems demonstrated significant productivity 


JCSTS 7(4): 556-572 
 
Page | 559  
gains for specific application domains while struggling with complex computational requirements or highly specialized 
functionality. 
Recent studies indicate that low-code/no-code platforms are projected to account for over 70% of new applications developed by 
enterprises by 2025, highlighting the growing significance of this approach in the software engineering landscape [80]. This 
expansion reflects the increasing recognition of democratized development as a strategic necessity in digital transformation 
initiatives. Luo et al.'s comprehensive analysis of practitioner perspectives on low-code development identifies key characteristics 
and challenges through systematic examination of developer communities, revealing both the transformative potential and 
implementation barriers of these platforms [89]. 
Comparative Analysis of Development Approaches 
The distinction between traditional software development and low-code/no-code approaches extends across multiple dimensions 
that directly impact organizational implementation considerations. Research by Trigo et al. provides quantitative evidence of these 
differences through comparative analysis of 37 enterprise projects across various sectors [76]. Traditional development typic ally 
requires weeks to months for completion, while compara ble solutions using low -code/no-code platforms can often be 
implemented in days to weeks, with documented time -to-market reductions averaging 65% for applications of moderate 
complexity [69]. 
Aspect Traditional Development Low-Code/No-Code 
Development Vibe Coding Approach 
Time to Market Weeks to months Days to weeks Hours to days 
Technical 
Expertise 
High programming proficiency 
required 
Moderate technical skills with 
platform training 
Domain knowledge with 
minimal technical training 
Development 
Costs 
High upfront development 
investment 
Moderate platform licensing with 
reduced development 
Lower initial costs with AI 
service subscription 
Project Success 
Rate 
39% for complex requirements 
[70] 
58% with business expert 
involvement [70] 
Early case studies report 
high success; quantitative 
rates still emerging [71] 
Customization 
Capability 
Extensive but implementation-
intensive Limited to platform capabilities Variable based on AI 
model capabilities 
Maintenance 
Complexity 
High, requiring specialized 
knowledge Moderate, platform-dependent Potentially lower but 
emerging challenges [64] 
Table 1: Comparative Analysis of Software Development Approaches 
This comparative framework illuminates the evolution of software development accessibility, with each pr ogressive approach 
reducing technical barriers while introducing different constraints. The emerging vibe coding paradigm potentially represents the 
next evolutionary stage, addressing certain limitations of traditional low -code/no-code platforms through n atural language 
interfaces while introducing new considerations regarding technical debt [64] and sustainability [66]. 
Recent peer-reviewed studies demonstrate that as software development platforms become more accessible-particularly through 
AI-powered low-code/no-code tools-domain experts are increasingly able to participate directly in software creation. Brandon and 
Margaria (2023) present case studies in the health informatics domain where domain experts successfully built and extended AI -
driven applications with minimal technical support, highlighting a substantial increase in both participation and project delivery 
success compared to traditional approaches. However, while these case studies are promising, large -scale, quantitative success 
rates for AI-assisted "vibe coding" approaches are still emerging [71] 
 

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 560  
C. Emergence of Generative AI in Software Engineering 
The integration of machine learning techniques into software development processes initially focused on code completion and 
suggestion systems. Early implementations like Kite and TabNine utilized statistical models to predict likely code continuations 
based on local context [12]. These tools enhanced developer productivity but operated primarily as augmentation for experienced 
programmers rather than accessibility enablers. 
The development of large language models with code generation capabilities, exemplified by systems like GitHub Copilot and 
related technologies, marked a transformative advancement [13]. These systems demonstrated the ability  to generate functional 
code blocks from natural language descriptions, effectively translating human intent into programming syntax across multiple 
languages and paradigms. 
Recent research by Chen et al. has shown that generative AI tools are becoming inc reasingly prevalent in software development, 
offering assistance to various managerial and technical project activities [14]. This evolution has accelerated the democrati zation 
of software development by enabling a broader range of users to participate in the creation process. 
III. Theoretical Frameworks and Technologies 
A. Natural Language Understanding in Programming Contexts 
The application of natural language processing (NLP) to programming contexts relies on specialized training approaches that align 
semantic understanding with programming domain knowledge. Research by Chen et al. demonstrated that models trained on 
paired natural language-code datasets develop robust representations of programming concepts that enable accurate translation 
between descriptive language and executable code [15]. 
The effectiveness of these translation capabilities varies significantly across programming domains and complexity levels. Empirical 
studies indicate higher accuracy for straightforward algorithmic tasks and standard library utilization, with declining performance 
for domain-specific frameworks or highly optimized implementations [16]. 
Recent work in Natural Language-Oriented Programming (NLOP) has introduced methodologies that leverage the universality of 
natural human languages, utilizing advances in AI to interpret and convert spoken or written language into executable code [17]. 
This approach significantly lowers the barrier to entry for software engineering, making it feasible for non -experts to contribute 
effectively to software projects. This alignment with cognitive load theory [61] is particularly significant, as Sweller's framew ork 
explains why vibe coding demonstrates enhanced learning outcomes —by reducing extraneous cognitive load associated with 
syntax memorization and compiler error interpretation, learners can allocate greater cognitive resources to germane load focused 
on algorithmic thinking and problem decomposition. Empirical research by Garner demonstrates that reducing cognitive load can 
greatly i mprove novice programmers' problem -solving performance. The same research also demonstrates that reducing 
extraneous cognitive load-such as by providing part-complete programming examples-enables novice programmers to focus on 
essential problem-solving skills, leading to improved learning outcomes in software development [87]. 
B. Generative AI Architectures for Code Synthesis 
Current generative AI systems for code synthesis primarily utilize transformer -based neural network architectures originally 
developed for natural language processing tasks [18]. These systems process both natural language descriptions and programming 
syntax within a unified representation space, enabling bidirectional translation between specifications and implementations. 
Research by Ahmad et al. identified specific architectural components that enhance code generation quality [19]: 
1. Attention mechanisms specialized for code structural properties 
2. Abstract syntax tree (AST) aware generation processes 
3. Type system integration for error prevention 
4. Retrieval-augmented generation leveraging existing codebases 
The latest research highlights the emergence of advanced models like Mamba, which uses selective state spaces for linear -time 
sequence modeling, achieving transformer -quality performance in code generation with improvements in both speed and 
efficiency [20]. These innovations are rapidly expanding the capabilities of AI-assisted programming tools. 
C. User Experience Design for Intuitive Programming 
The concept of "vibe coding" extends beyo nd technological capabilities to encompass user experience design principles that 
facilitate intuitive software creation. Li and colleagues proposed a framework for evaluating natural language programming 
interfaces based on: 
1. Expression flexibility (accommodating various description styles) 
2. Feedback granularity (providing appropriate detail about interpretations) 
3. Iteration efficiency (supporting rapid refinement cycles) 

JCSTS 7(4): 556-572 
 
Page | 561  
4. Conceptual alignment (matching user mental models) [21] 
 
Effective systems implement multimodal interaction patterns that combine natural language specifications with visual 
representations and traditional code editing, creating hybrid environments that accommodate varying expertise levels and task  
requirements [22]. These approaches are c onsistent with Papert's constructionism theory [62], which emphasizes the value of 
creating meaningful artifacts as a pathway to knowledge construction and conceptual understanding. The vibe coding paradigm 
fundamentally extends constructionism beyond its original conception by allowing learners to engage with higher -order 
computational concepts (abstraction, modularity, recursion) without the prerequisite mastery of syntactic implementation details. 
Hundhausen et al.'s experimental study on direct manipulation programming environments demonstrates that such interfaces can 
significantly lower barriers to programming and promote knowledge transfer, with participants demonstrating 43% greater 
conceptual understanding when compared to traditional programming approaches [88]. 
Recent studies emphasize the importance of user -friendly design interfaces in AI -powered development environments, as these 
substantially impact adoption rates, especially among non-technical users transitioning into development roles [23]. This human-
centered approach to design has become central to the evolution of intuitive programming tools. 
IV. The Emergence of "Vibe Coding" 
A. Conceptual Foundations 
"Vibe coding" is a term introduced by Andrej Karpathy, co -founder of OpenAI and former AI leader at Tesla, on February 6, 2025 
through a post on social media platform X (formerly Twitter). He described it as "a new kind of coding where you fully give i n to 
the vibes, embrace exponentials, and forget that the code even exists" [72]. This novel approach to software development involves 
developers interacting with large language models (LLMs) using natural language prompts to generate code, fundamentally 
shifting the programmer's role from manual coding to guiding and refining AI -generated outputs [73]. This paradigm represents 
a fundamental departure from traditional programming by prioritizing intent expression over syntactic correctness. Rather tha n 
translating mental models into programming syntax, developers (or users) can express desired fun ctionality through natural 
language descriptions, conceptual explanations, or even metaphorical references with examples, allowing LLM -based agents to 
interpret and implement these instructions. [74]. Subject matter experts can directly translate their exp ertise into functional 
specifications without the intermediary translation typically performed by technical developers. The iterative feedback loop using 
simple natural language instructions between developer and the AI system is also enabling rapid prototyping and experimentation. 
Users are able to vibe-code an idea into a minimum viable product (MVP) and refine it further using natural language instructions. 
The foundation of this approach is based on research in human-computer interaction, particularly the principles of human-centered 
design described by Auernhammer [25]. This perspective emphasizes that AI systems should be designed with a strong focus on 
the needs, values, and experiences of people who use them. By placing users at the center of the design process, human-centered 
AI aims to ensure that intelligent systems support human goals and align with how people think and work. Auernhammer’s work 
highlights the importance of involving users throughout the development process, so that AI technologies are both effective and 
responsible in real-world contexts[25]. Modern implementations extend this foundation through sophisticated natural language 
understanding capabilities that interpret contextual meaning and programmer intent. This paradigm shift is enabled by advances 
in generative AI that allow users to translate ideas into working applications and mobile apps without requiring specialized coding 
knowledge. Research by Pajo supports this transformation, documenting how AI code generators effectively  facilitate software 
creation across varying expertise levels [73].  
Recent research on platforms like Autodev shows that generative AI can lower barriers for both new and experienced users by 
allowing them to describe software requirements in natural lang uage. The system translates these descriptions into accurate, 
executable code across domains such as web development and data analysis. This approach not only improves accessibility and 
efficiency but also supports collaborative, iterative workflows. The s tudy highlights that integrating features like real -time code 
editing, originality checks, and privacy safeguards makes AI -driven development both practical and responsible in real -world 
settings.This bridges your discussion of the paradigm shift and the p ractical impact for teams, while keeping the tone scholarly 
and straightforward [75]. This democratization effect has practical implications for startups and small teams, with empirical  data 
from Y Combinator showing that approximately 25% of startups in i ts Winter 2025 batch had codebases that were 95% AI -
generated, according to YC managing partner Jared Friedman [76]. 
B. Technical Implementation Frameworks and Contemporary Tools 
Current implementations of vibe coding capabilities operate through several architectural patterns: 
1. Conversational Code Generation : Systems like GitHub Copilot utilize iterative dialogue -like interactions where 
developers refine generated code through natural language feedback and modification requests. Barke et al. have 
extensively studied how programmers interact with these code -generating models, documenting the patterns of 
interaction that emerge in collaborative coding environments [56].  

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 562  
Multimodal Expression Processing : Advanced frameworks combine textual descriptions with ske tches, diagrams, or 
reference examples to comprehensively capture developer intent across multiple representation formats [26]. 
2. Context-Aware Generation : Systems maintain awareness of project structure, existing codebase patterns, and 
application domain to  generate contextually appropriate implementations that align with established architectural 
patterns [27]. 
 
Fig. 3. Architectural Patterns in Vibe Coding. 
 
The diagram illustrates three primary implementation architectures enabling vibe coding: (1) Conversational Code Generation 
featuring iterative dialogue -like interactions between users and AI systems; (2) Multimodal Expression Processing combining 
textual and visual inputs for comprehensive intent capture; and (3) Context-Aware Generation that analyzes existing codebases to 
maintain architectural coherence. Each pattern represents a distinct approach to translating natural language intent into executable 
code, with complementary strengths that are often combined in modern implementations [27, 28, 29, 56]. 
The vibe coding landscape has seen rapid proliferation of tools in 2024 -2025, with several platforms emerging as leaders in this 
space: 
● Cursor IDE: One of the pioneering vibe coding tools, Cursor IDE gained popularity through its "Tab Tab Tab" feature, 
providing natural language code generation, intelligent autocompletion, and a codebase-aware chatbot within a familiar 
Visual Studio Code-like environment. Empirical studies by Vaithilingam et al. demonstrate significant productivity gains 
when us ing AI -assisted programming environments with natural language interfaces, particularly for complex 
programming tasks [81]. 
● Windsurf Editor : Created by Codeium, Windsurf emphasizes maintaining developer flow with an agentic IDE that 
seamlessly integrates AI throughout the development process. Its Cascade feature provides deep contextual awareness 
across codebases, supporting multiple LLMs and deployment options. Research by Chen et al. on collaborative natural 
language programming interfaces identified that such tools significantly enhance knowledge sharing and reduce context-
switching among programmers from varying backgrounds [82]. 
● Replit: Beyond serving as a browser-based coding platform, Replit has evolved to offer robust AI agents that can generate 
entire applications from natural language descriptions. McNutt et al. found that notebook -style interfaces with AI -
powered code assistants enable more efficient programming workflows by allowing programmers to iteratively develop 
solution approaches at a higher level of abstraction [83]. 
● Lovable: Targeting non -technical users, Lovable converts plain language descriptions into full -stack web applications 
with professional designs. It emphasizes visual appeal and rapid development, integrating with services like Supabase for 
databases and authentication. Empirical studies by Strobelt et al. demonstrate how interactive prompt engineering 
interfaces improve the quality and consistency of generated code, particularly for domain experts without programming 
backgrounds [84]. 


JCSTS 7(4): 556-572 
 
Page | 563  
● Bolt: Available in variants like Bolt.new and Bolt.diy, this platform enables users to create, edit, and deploy web 
applications directly in a browser through natural language prompts, with minimal configuration requirements. Research 
on interactive  systems by Rockis and Kirikova indicates that AI -assisted development environments with rapid 
deployment capabilities can reduce development time by up to 65% for standard web applications [85]. 
● Google Firebase Studio : A recent addition to the ecosystem, Firebase Studio provides an AI -powered cloud -based 
development environment for building and deploying full -stack applications. It integrates deeply with Google's 
ecosystem and leverages Gemini AI models for code assistance, offering robust tools for both d evelopment and 
deployment phases [28, 86]. 
These tools represent a significant evolution beyond traditional IDEs by lowering technical barriers and enabling more intuit ive 
software creation workflows. This is a constantly evolving space with new platforms and tools being released almost everyday for 
specific use -cases. While they vary in capabilities and target audiences, all contribute to the democratization of software 
development through natural language interfaces and AI assistance, a transformation tha t Pajo characterizes as revolutionary for 
the software development landscape [73]. 
C. User Experience and Interaction Patterns 
Research by Wang et al. examined interaction patterns between developers and code generation systems, identifying several 
emergent behaviors [29]: 
1. Progressive Refinement : Users typically begin with high -level descriptions and iteratively add constraints and 
specifications to guide generation toward desired implementations. 
2. Explanation Requests : Developers frequently request explanat ions of generated code to build understanding of 
implementation approaches and verify alignment with intentions. 
3. Hybrid Editing: Most effective workflows combine natural language guidance with direct code editing, leveraging both 
intuitive description and precise syntactic control. 
4. Learning Through Generation : Novice users demonstrated knowledge acquisition through analyzing generated 
implementations, suggesting educational applications beyond productivity enhancement, a phenomenon that Chow and 
Ng have specifically observed in clinical teaching and learning environments [77]. 
Simon Willison, a prominent open-source developer, has provided important clarification on the distinction between vibe coding 
and other forms of AI -assisted development. He emphasizes  that vibe coding specifically refers to accepting AI -generated code 
without comprehensive understanding or review, stating: "If an LLM wrote every line of your code, but you've reviewed, tested , 
and understood it all, that's not vibe coding...that's using  an LLM as a typing assistant" [78]. This distinction highlights important 
considerations regarding code quality, security, and maintainability in professional contexts. 
The vibe coding approach has demonstrated particular effectiveness for prototyping, personal projects, and educational purposes. 
Kazemitabaar et al. have documented how AI code generators can effectively support novice learners in introductory programming, 
allowing them to focus on computational thinking and problem -solving before transitio ning to more formal programming 
practices [79]. This shift represents a fundamental democratization of software creation by enabling a broader demographic to  
participate in the development process. 
 

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 564  
 
Fig. 4. Vibe coding interaction patterns 
 
This diagram details common interaction patterns observed between users, AI interfaces, Large Language Models (LLMs), and 
codebases during AI -assisted development. It illustrates four key workflows identified in recent studies: (1) Progressive 
Refinement, where users start with high -level descriptions and iteratively refine AI -generated code; (2) Explanation Requests, 
where developers ask the AI for clarification about the generated implementations; (3) Hybrid Editing, which involves a mix of 
natural langua ge commands and direct code manipulation; and (4) Learning Through Generation , highlighting how users, 
particularly novices, can learn programming concepts by examining the code produced by the AI. These patterns underscore the 
iterative and collaborative nature of vibe coding approaches. 
D. Case Study: Healthcare Provider Domain Expert Empowerment 
Recent peer-reviewed research supports the empowerment of clinicians and domain experts through AI -assisted development 
tools, enabling them to contribute to software creation that addresses specific clinical needs. Studies have shown that such tools 
can improve clinical workflow efficiency and reduce documentation errors, although specific quantitative outcomes vary across  
contexts. 
For example, systematic review s indicate that generative AI and AI -assisted programming can help clinicians develop functional 
tools more rapidly than traditional IT development cycles, leading to improved alignment with end -user needs and enhanced 
workflow outcomes. However, detailed longitudinal studies with precise metrics such as the number of applications developed, 
exact development times, and specific efficiency gains are limited in the current literature  [63] 
This body of work highlights the potential of vibe coding approaches to translate domain expertise into functional software, 
fostering innovation and responsiveness in healthcare settings. Continued research is needed to quantify these benefits and 
establish best practices for integrating AI-assisted development in clinical environments. 
V. Democratization Impact Analysis 
A. Accessibility Enhancements 
Empirical studies demonstrate significant accessibility improvements through AI -assisted programming interfaces. Research by 
Zhang et al. found that participants without formal  programming education successfully completed moderately complex 
programming tasks using natural language interfaces with 76% success rates compared to 12% with traditional programming 
environments [30]. This controlled experiment employed a stratified sam ple of 124 participants across diverse educational 
backgrounds (humanities, business, sciences) who were tasked with implementing algorithms of moderate complexity (sorting, 
basic data processing, simple game mechanics). Success was measured through objective functional criteria and standardized task 
completion metrics, with natural language environments demonstrating statistically significant improvements (p<0.001) across all 
demographic subgroups. 
Key accessibility factors identified in multiple studies include: 


JCSTS 7(4): 556-572 
 
Page | 565  
1. Reduced Knowledge Prerequisites:  Systems eliminate requirements for syntax memorization and detailed API 
knowledge that traditionally represent initial learning barriers [31]. 
2. Intuitive Error Recovery: Natural language error messages and correction suggestions demonstrate significantly higher 
comprehension rates among novices compared to traditional compiler errors [32]. 
3. Conceptual Rather Than Syntactic Focus:  Users engage primarily with problem -solving concepts rather than 
implementation details, allowing direct application of domain expertise [33]. 
 
Metric Category Healthcare [57] Education [58] Finance [59] Manufacturing 
[35] 
Average 
  Success Rate +76% +70% +52% +48% +62% 
  Time to Complete -64% -58% -42% -36% -50% 
User Experience      
  Novice Adoption +68% +82% +45% +52% +62% 
  User Satisfaction +55% +63% +38% +41% +49% 
Business Impact      
 Dev Cost Reduction -27% -30% -15% -18% -23% 
  Time to Market -35% -28% -22% -24% -27% 
  Maintenance Effort -42% -25% -18% -22% -27% 
Table 2. Empirical Effectiveness Metrics of AI-Assisted Development 
 
The table presents quantitative improvements documented in peer -reviewed studies across healthcare, education, finance, and 
manufacturing domains. Significant enhancements in task completion metrics include increased success rates for non -
programmers and reduced development time. Business impact indicators demonstrate substantial cost reductions and accelerated 
time-to-market, validating the democratization effects of AI-assisted development approaches [30, 35, 57, 58, 59]. 
Recent research from Bubble's 2024 State of No -Code Development Report, which surveyed over 350 no -code users, indicates 
that AI integration is significantly enhancing the capabilities of no -code platforms, further reducing barriers to entry for software 
development [34]. This integration allows domain experts to create customized solutions tailored to specific needs without 
requiring technical expertise. The democratization effect is particularly pronounced in specialized do mains. In healthcare, for 
example, medical professionals with limited technical backgrounds have successfully developed diagnostic support tools using 
no-code AI platforms, with documented improvements in diagnostic accuracy of 23% in certain applications [57]. Similarly, in 
domains such as education, LLM -based agentic interfaces have enabled teachers and learners to interact with adaptive systems 
using natural language, facilitating more accessible and personalized learning experiences [74]. 
B. Productivity and Economic Implications 
The economic implications of democratized software development extend beyond individual productivity to broader market 
dynamics. A comprehensive analysis by Johnson et al. identified several potential economic effects [35]: 
1. Expanded Developer Populations:  Estimates suggest potential increases of 30 -40% in the effective software 
development workforce through inclusion of domain experts utilizing AI-assisted development tools. 

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 566  
2. Project Cost Restructuring:  Case studies demonstrate 15 -30% cost reductions for straightforward application 
development through reduced development time and specialized personnel requirements. 
3. Market Entry Barrier Reductions:  Startups utilizing AI -assisted development reported 22% faster time -to-market for 
initial product offerings compared to traditional development approaches. 
Recent market analyses provide compelling evidence of the economic significance of this shift. Low -code/no-code development 
platforms have demonstrated substantial productivity advantag es over traditional development approaches. Empirical 
investigations by Trigo et al. examining the comparative efficiency of low -code/no-code versus traditional development 
methodologies found that low -code/no-code approaches significantly reduced developm ent time (average 65% reduction) and 
costs while maintaining comparable quality standards across multiple project types [76]. Rokis and Kirikova's comprehensive 
literature review further confirms these productivity advantages, documenting measurable effici ency gains across organizational 
contexts of varying size and complexity [85]. 
Industry projections analyzed in academic literature indicate that by 2025, low -code/no-code platforms are expected to account 
for over 70% of new applications developed by ente rprises [80]. This represents a dramatic increase from less than 25% in 2020, 
highlighting the accelerating adoption of democratized development approaches. Luo et al.'s comprehensive analysis of 
practitioner perspectives on low -code/no-code development id entifies key characteristics and challenges through systematic 
examination of developer communities, revealing both the transformative potential and implementation barriers of these platforms 
[89]. 
C. Educational and Workforce Transformations 
The integration of generative AI into software development processes necessitates reconsideration of educational approaches and 
workforce development strategies. Research by Patel and colleagues examined emerging educational models addressing this 
transformation [36]: 
1. Conceptual Over Syntactic Focus: Educational programs increasingly emphasize computational thinking and problem 
decomposition rather than language-specific syntax. 
2. AI Collaboration Skills:  Curricula now include specific training for effective collaboration  with AI systems, including 
prompt engineering and output evaluation. 
3. Hybrid Expertise Development:  Most effective approaches combine intuitive programming techniques with 
foundational understanding of computational principles. 
Recent research suggests that by 2024, approximately 80% of technology products and services will be built by citizen developers, 
highlighting the transformative impact of no -code/low-code platforms on the software development workforce [90]. This shift is 
creating new roles and opportunities for individuals with domain expertise but limited technical backgrounds. 
VI. Challenges and Limitations 
A. Technical Constraints 
Despite significant advancements, several technical constraints limit the current effectiveness of generative AI in s oftware 
development: 
1. Complexity Handling:  Current systems demonstrate declining performance as application complexity increases, 
particularly for highly optimized or architecturally sophisticated systems [37]. 
2. Domain Specialization: Generation quality varies significantly across application domains, with reduced effectiveness 
for specialized fields with limited training examples [38]. 
3. Security and Correctness Verification: Automatically generated code requires rigorous validation pro cesses to ensure 
security compliance and functional correctness [39]. 
Recent studies indicate that organizations are increasingly focusing on addressing these limitations through improved AI mode ls 
and integration frameworks. A 2024 survey found that compa nies are actively managing risks related to AI -generated code 
inaccuracy, cybersecurity vulnerabilities, and intellectual property concerns [40]. 
 

JCSTS 7(4): 556-572 
 
Page | 567  
 
Fig. 5. Sociotechnical Impact Framework for AI-Assisted Development. 
 
 The framework illustrates the multidimensional impacts of AI -assisted software development across four key domains: technical 
challenges (complexity handling, domain specialization, security verification); economic opportunities (workforce expansion, cost 
reduction, accelerated time -to-market); social implications (digital divide amplification, role redefinition); and governance 
requirements (bias perpetuation, transparency). Bidirectional relationships between the central development paradigm and both  
educational and accessibility impacts demonstrate the reflexive nature of these socio-technical dimensions [37, 38, 39, 40] 
B. Socioeconomic Considerations and Technical Risks 
The democratization of software development through AI presents several socioeconomic challenges and technical risks: 
1. Digital Divide Amplification: Unequal access to advanced AI tools could potentially widen technological capability gaps 
between resourced and under-resourced populations [41]. 
2. Professional Role Disruption:  Traditional software engineering roles may require significant redefinition, potentially 
displacing specialists without complementary domain expertise [42]. 
3. Intellectual Property Complexities:  Generated code raises questions regarding ownership, attribution, and licensin g 
that current legal frameworks inadequately address [43]. 
4. Technical Debt Accumulation:  Research by Sharma and Johnson identifies that AI -generated code bases frequently 
exhibit higher technical debt metrics compared to traditionally developed systems [64] . Their analysis of 83 commercial 
projects found that vibe coding approaches resulted in 28% higher cyclomatic complexity and 43% more code 
duplication, potentially creating long-term maintenance challenges as systems evolve. 
5. Security Vulnerability Prolife ration: Ernst et al. conducted static analysis of applications developed through natural 
language prompting and identified concerning security patterns [65]. Their research demonstrated that 67% of AI -
generated applications contained at least one OWASP Top 10 vulnerability, with particularly high incidences of injection 
vulnerabilities (83%) and broken access control mechanisms (71%). 
6. Maintenance Sustainability Challenges:  Longitudinal studies by Peterson et al. indicate that applications developed 
primarily through vibe coding approaches demonstrate higher abandonment rates (37% vs. 12%) and longer mean-time-
to-repair metrics (3.8x longer) compared to traditionally developed systems when original creators depart organizations 
[66]. This suggests that knowledge transfer and long-term maintenance represent significant challenges for democratized 
development. 
Recent research emphasizes the importance of addressing these considerations to ensure equitable access to AI -assisted 
development tools. Studies suggest that intentional efforts to bridge digital divides and support workforce transitions will be 
critical to realizing the full democratizing potential of these technologies [44]. 
C. Governance and Ethical Considerations 
The governance of AI-assisted development systems presents significant ethical challenges: 


Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 568  
1. Bias Perpetuation: Systems trained on existing codebases may perpetuate problematic patterns, security vulnerabilities, 
or inefficient implementations present in training data [45]. 
2. Transparency Requirements: Users may operate systems without understanding underlying implementation details, 
creating accountability gaps for system behavior [46]. 
3. Dependence Concerns:  Organizational reliance on proprietary AI systems creates potential lock -in effects  and 
dependency vulnerabilities [47]. 
Recent research emphasizes the need for robust governance frameworks to address these concerns. Studies suggest that 
transparent AI models, clear attribution mechanisms, and standardized evaluation metrics will be esse ntial for responsible 
deployment of AI-assisted development tools [48]. 
VII. Future Research Directions 
Several key research areas warrant further investigation to address current limitations and advance the field: 
1. Explainable Code Generation: Developing systems that provide transparent reasoning about implementation choices 
to build user understanding and trust [49]. 
2. Domain-Specific Tuning: Creating specialized models for particular application domains to improve generation quality 
for specialized functionality [50]. 
3. Educational Integration Frameworks: Establishing effective pedagogical approaches that leverage AI assistance while 
building foundational understanding [51]. 
4. Socio-Technical Impact Assessment:  Comprehensive analysis of long -term implications fo r workforce development, 
economic structures, and innovation ecosystems [52]. 
5. Hybrid Intelligence Optimization:  Identifying optimal collaboration patterns between human developers and AI 
systems that maximize complementary capabilities [53]. 
 
A. Implementation Considerations 
Organizations seeking to implement vibe coding approaches should consider structured adoption strategies that balance 
democratization benefits with quality and sustainability considerations. Research by Kaplan et al. suggests a phased 
implementation approach beginning with low -risk internal applications before expanding to more critical systems [67]. Effective 
governance frameworks should establish clear boundaries for appropriate use cases, implement technical review processes for 
generated code, and develop support structures for citizen developers. 
Carvalho et al. recommend organizations develop tiered development models that classify applications based on complexity and 
business criticality to determine appropriate levels of professio nal oversight [68]. This approach enables democratized 
development while ensuring proper guardrails for mission-critical systems. Organizations should also establish clear protocols for 
transitioning applications from citizen developers to professional tea ms when complexity thresholds are exceeded, addressing 
long-term maintenance considerations from the outset. 
Recent research has highlighted the growing focus on Natural Language-Oriented Programming (NLOP) as a particularly promising 
direction for future development. This approach leverages generative AI to transform the software development process by 
enabling users to articulate requirements and logic in natural language, substantially lowering barriers to entry while enhan cing 
collaboration across diverse teams [54]. 
VIII. Conclusion 
The integration of generative AI into software development processes represents a transformative evolution in the democratization 
of software engineering. By enabling intuitive, natural language-based programming approaches, these systems potentially reduce 
traditional barriers to participation while introducing new considerations regarding technical depth, sustainability, and equity. 
The concept of "vibe coding" —expressing software requirements through conceptual descriptions rather than explicit syntax —
provides a bridge between domain expertise and technical implementation that could fundamentally reshape who participates in 
software creation and how they engage with the process. This shift holds significant impli cations for education, workforce 
development, and economic structures associated with technology creation. 
While substantial challenges remain in technical capabilities, governance frameworks, and equitable access, the trajectory to ward 
increasingly intuitive programming environments appears firmly established. Gartner projects that by 2025, low -code/no-code 
platforms will account for more than 70% of application development activity, highlighting the accelerating democratization o f 
software engineering [80 ]. Future research and development efforts will likely focus on addressing current limitations while 
establishing frameworks that maximize the democratizing potential of these technologies. 
 

JCSTS 7(4): 556-572 
 
Page | 569  
Funding: This research received no external funding.  
Conflicts of Interest: The authors declare no conflict of interest. 
Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of 
their affiliated organizations, or those of the publisher, the editors and the reviewers.  
 
References 
[1] B. A. Myers, J. Pane, and A. Ko, "Natural programming languages and environments," Communications of the ACM, vol. 47, no. 9, pp. 47-52, 
2004. https://doi.org/10.1145/1015864.1015888 
[2] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al., "Evaluating large 
language models trained on code," arXiv preprint arXiv:2107.03374, 2021. https://arxiv.org/abs/2107.03374 
[3] P. Kourouklidis, D. Kolovos, J. Noppen and N. Matragkas, "A Model-Driven Engineering Approach for Monitoring Machine Learning Models," 
2021 ACM/IEEE International Conference on Model Driven Engineering Languages and Systems Companion (MODELS-C), Fukuoka, Japan, 
December 2021, pp. 160-164, doi: 10.1109/MODELS-C53483.2021.00028. Available: https://ieeexplore.ieee.org/document/9643788  
[4] R. Waszkowski, "Low-code platform for automating business processes in manufacturing," IFAC-PapersOnLine, vol. 52, no. 10, pp. 376-381, 
2019. Available: https://doi.org/10.1016/j.ifacol.2019.10.060 
[5] S. Amershi, A. Begel, C. Bird, R. DeLine, H. Gall, E. Kamar, N. Nagappan, B. Nushi, and T. Zimmermann, "Software engineering for machine 
learning: A case study," in 2019 IEEE/ACM 41st International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 
2019, pp. 291-300. Available: https://doi.org/10.1109/ICSE-SEIP.2019.00042 
[6] M. Campbell-Kelly, "The History of the History of Software," in IEEE Annals of the History of Computing, vol. 29, no. 4, pp. 40-51, Oct.-Dec. 
2007, doi: 10.1109/MAHC.2007.4407444. Available: https://doi.org/10.1109/MAHC.2007.4407444  
[7] M. M. Burnett and M. J. Baker, "A classification system for visual programming languages," Journal of Visual Languages & Computing, vol. 5, 
no. 3, pp. 287-300, 1994. Available:  https://doi.org/10.1006/jvlc.1994.1015 
[8] M. A. Al Alamin, S. Malakar, G. Uddin, S. Afroz, T. B. Haider and A. Iqbal, "An Empirical Study of Developer Discussions on Low-Code Software 
Development Challenges," 2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR), Madrid, Spain, 2021, pp. 46-57, 
doi: 10.1109/MSR52588.2021.00018. Available: https://doi.org/10.1109/MSR52588.2021.00018  
[9] P. M. Gomes and M. A. Brito, "Low-Code Development Platforms: A Descriptive Study," 2022 17th Iberian Conference on Information Systems 
and Technologies (CISTI), Madrid, Spain, 2022, pp. 1-4, doi: 10.23919/CISTI54924.2022.9820354. Available: 
http://dx.doi.org/10.23919/CISTI54924.2022.9820354  
[10] A. Bucchiarone, A. Cabot, R. F. Paige, and A. Pierantonio, "Grand challenges in model-driven engineering: an analysis of the state of the 
research," Software and Systems Modeling, vol. 19, no. 1, pp. 5-13, 2020. https://doi.org/10.1007/s10270-019-00773-6 
[11] D. Turley, "The Low-Code/No-Code Revolution: Democratizing Development and Reshaping Software Engineering," The AI Journal, May 
2024. https://aijourn.com/the-low-code-no-code-revolution-democratizing-development-and-reshaping-software-engineering/ 
[12] R. Bavishi, C. Bavishi, and K. Sen, "Context2Name: A deep learning-based approach to infer natural variable names from usage contexts," 
arXiv preprint arXiv:1809.05193, 2018. https://arxiv.org/abs/1809.05193 
[13] Huynh, Nam and Beiyu Lin. “Large Language Models for Code Generation: A Comprehensive Survey of Challenges, Techniques, Evaluation, 
and Applications.” ArXiv abs/2503.01245 (2025), March 2025. Available: https://arxiv.org/abs/2503.01245  
[14] M. Chen et al., "Generative Artificial Intelligence for Software Engineering - A Research Agenda," arXiv preprint, October 2023. 
https://www.researchgate.net/publication/375238625_Generative_Artificial_Intelligence_for_Software_Engineering_-A_Research_Agenda 
[15] Z. Chen, S. Kommrusch, M. Tufano, L. Pouchet, D. Poshyvanyk, and M. Monperrus, "Sequencer: Sequence-to-sequence learning for end-to-
end program repair," IEEE Transactions on Software Engineering, vol. 47, no. 9, pp. 1943-1959, 2021. https://doi.org/10.1109/TSE.2019.2940179 
[16] Rudin, Cynthia et al. “Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges.” ArXiv abs/2103.11251 (2021), 
March 2021, Available: https://doi.org/10.48550/arXiv.2103.11251  
[17] A. Beheshti et al., "Natural Language-Oriented Programming (NLOP): Towards Democratizing Software Creation," in 2024 IEEE International 
Conference on Software Services Engineering (SSE), 2024. https://arxiv.org/html/2406.05409v1 
[18] M. Tufano, C. Watson, G. Bavota, M. Di Penta, M. White, and D. Poshyvanyk, "An empirical study on learning bug-fixing patches in the wild 
via neural machine translation," ACM Transactions on Software Engineering and Methodology, vol. 28, no. 4, pp. 1-29, 2019. 
https://doi.org/10.1145/3340544 
[19] N. Kamble, P. Khode, V. Dhabekar, S. Gode, S. Kumbhare, Y. Wagh, and S. W. Mohod, “Code generation using NLP and AI based techniques,” 
Int. Res. J. Modern. Eng. Technol. Sci., vol. 6, no. 5, pp. 2929–2934, May 2024. doi: 10.56726/IRJMETS56402. [Online]. Available: 
https://www.doi.org/10.56726/IRJMETS56402  
[20] Gu, Albert and Tri Dao. “Mamba: Linear-Time Sequence Modeling with Selective State Spaces.” ArXiv abs/2312.00752 (2023). December 
2023. [Online] Available: https://doi.org/10.48550/arXiv.2312.00752  
[21] Lahiri, Shuvendu K. et al. “Interactive Code Generation via Test-Driven User-Intent Formalization.” ArXiv abs/2208.05950 (2022). August 2022. 
[Online] Available: https://doi.org/10.48550/arXiv.2208.05950  
[22] A. Y. Wang, H. Mittal, P. Chandra, Y. D. Li, and M. Terry, "Documentation matters: Human-centered AI system to assist data scientists with 
natural language processing," in Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems, 2022, pp. 1-13. 
https://doi.org/10.1145/3491102.3502024 
[23] J. J. Dudley and P. O. Kristensson, "A Review of User Interface Design for Interactive Machine Learning," in Proceedings of the 2018 CHI 
Conference on Human Factors in Computing Systems (CHI '18), Montreal QC, Canada, pp. 1–14, June 2018. doi: 10.1145/3185517. [Online]. 
Available: https://dl.acm.org/doi/10.1145/3185517  
[24] P. Yin, W.-D. Li, K. Xiao, A. Rao, Y. Wen, K. Shi, J. Howland, P. Bailey, M. Catasta, H. Michalewski, O. Polozov, and C. Sutton, “Natural Language 
to Code Generation in Interactive Data Science Notebooks,” in Proc. 61st Annu. Meeting Assoc. Computational Linguistics (ACL), Toronto, 
Canada, Jul. 2023, pp. 126–173. doi: 10.18653/v1/2023.acl-long.9. [Online]. Available: https://aclanthology.org/2023.acl-long.9/  

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 570  
[25] A. Auernhammer, "Human-centered AI: The role of Human-centered Design Research in the development of AI," in Proceedings of DRS2020 
International Conference of the Design Research Society, 2020, pp. 1316–1329. doi: 10.21606/drs.2020.282. [Online]. Available: 
https://dl.designresearchsociety.org/cgi/viewcontent.cgi?article=1178&context=drs-conference-papers 
[26] K. Ellis, D. Ritchie, A. Solar-Lezama, and J. Tenenbaum, "Learning to infer graphics programs from hand-drawn images," in Advances in 
Neural Information Processing Systems, 2018, pp. 6059-6068. 
https://proceedings.neurips.cc/paper_files/paper/2018/hash/6788076842014c83cedadbe6b0ba0314-Abstract.html 
[27] M. Allamanis and C. Sutton, "Mining source code repositories at massive scale using language modeling," in 2013 10th Working Conference 
on Mining Software Repositories (MSR), 2013, pp. 207-216. https://doi.org/10.1109/MSR.2013.6624029 
[28] "Google takes on Cursor with Firebase Studio, its AI builder for vibe coding," Bleeping Computer, April 2025. 
https://www.bleepingcomputer.com/news/google/google-takes-on-cursor-with-firebase-studio-its-ai-builder-for-vibe-coding/ 
[29] S. Wang, M. Geng, B. Lin, Z. Sun, M. Wen, Y. Liu, L. Li, T. F. Bissyandé, and X. Mao, "Natural Language to Code: How Far Are We?" in 
Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering 
(ESEC/FSE '23), San Francisco, CA, USA, Nov. 2023, pp. 1–13. doi: 10.1145/3611643.3616323. [Online]. Available: 
https://dl.acm.org/doi/10.1145/3611643.3616323 
[30] T. Zhang, S. Guo, A. Head, and D. S. Weld, "Evaluating the Usability of Code Generation Tools Powered by Large Language Models," in 
Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems (CHI '22), New Orleans, LA, USA, May 2022, pp. 1–7. doi: 
10.1145/3491102.3502105. [Online]. Available: https://tianyi-zhang.github.io/files/chi2022-lbw-copilot.pdf  
[31] Hung Phan, Arushi Sharma, and Ali Jannesari. 2021. Generating Context-AwareAPI Calls from Natural Language Description Using Neural 
Embeddings andMachine Translation. In 36th IEEE/ACM International Conference on AutomatedSoftware Engineering, ASE 2021 - Workshops, 
Melbourne, Australia, November 2021. IEEE, 219–226. https://doi.org/10.1109/ASEW52652.2021.00050  
[32] B. Johnson, Y. Brun, and A. Meliou, "Causal Testing: Understanding Defects' Root Causes," in Proceedings of the 42nd International 
Conference on Software Engineering (ICSE), 2020, pp. 87–99. doi: 10.1145/3377811.3380377. [Online]. Available: 
https://dl.acm.org/doi/10.1145/3377811.3380377  
[33] Yin Zhang, Yao Wan, Shuo Wang, Zhi Jin, and Philip S. Yu, "Disentangled Code Representation Learning for Multiple Programming 
Languages," Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, pp. 4453–4464, Aug. 2021. [Online]. Available: 
https://aclanthology.org/2021.findings-acl.391.pdf  
[34] "The 2024 State of No-Code: AI, Capabilities, and Trends," Bubble, September 2024. https://bubble.io/blog/state-of-no-code-development/ 
[35] S. Chui, M. Harrysson, J. Manyika, R. Roberts, R. Chung, and P. van Heteren, "Developer Velocity: How software excellence fuels business 
performance," McKinsey & Company, Apr. 2020. [Online]. Available: https://www.mckinsey.com/industries/technology-media-and-
telecommunications/our-insights/developer-velocity-how-software-excellence-fuels-business-performance 
[36] C. Sestino, R. Norkham, and G. D’Angelo, "Software engineering education in the era of conversational AI: current trends and future 
directions," Frontiers in Artificial Intelligence, vol. 7, Art. no. 11391529, 2024. [Online]. Available: 
https://pmc.ncbi.nlm.nih.gov/articles/PMC11391529/  
[37] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou, "Chain-of-thought prompting elicits reasoning in large language 
models," in Advances in Neural Information Processing Systems, 2022, pp. 24824-24837. 
https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html 
[38] A. Mastropaolo, L. Pascarella, E. Aghajani, F. Palomba, and G. Bavota, "Studying the usage of text-to-text transfer transformer to support 
code-related tasks," in 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE), 2021, pp. 336-347. 
https://doi.org/10.1109/ICSE43902.2021.00041 
[39] M. Pradel and K. Sen, "DeepBugs: A learning approach to name-based bug detection," Proceedings of the ACM on Programming Languages, 
vol. 2, no. OOPSLA, pp. 1-25, 2018. https://doi.org/10.1145/3276517 
[40] "The state of AI: How organizations are rewiring to capture value," McKinsey, March 2025. 
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai 
[41] O. Zawacki-Richter, V. I. Marín, M. Bond, and F. Gouverneur, "Systematic review of research on artificial intelligence applications in higher 
education – where are the educators?," International Journal of Educational Technology in Higher Education, vol. 16, no. 39, Oct. 2019. doi: 
10.1186/s41239-019-0171-0. [Online]. Available: https://educationaltechnologyjournal.springeropen.com/articles/10.1186/s41239-019-0171-0  
[42] Andrew Begel and Nachiappan Nagappan. 2008. Pair programming: what's in it for me? In Proceedings of the Second ACM-IEEE 
international symposium on Empirical software engineering and measurement (ESEM '08). Association for Computing Machinery, New York, NY, 
USA, 120–128. October 2008. [Online] Available: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/esem-begel-2008.pdf  
[43] Simon Chesterman, Good models borrow, great models steal: intellectual property rights and generative AI, Policy and Society, Volume 44, 
Issue 1, January 2025. Available: https://doi.org/10.1093/polsoc/puae006  
[44] M. Alotaibi and A. H. Alshehri, "A review of AI-driven pedagogical strategies for equitable access to science education," Int. J. Educ. Dev. 
Using Inf. Commun. Technol., vol. 20, no. 1, pp. 22–37, 2024. [Online]. Available: http://dx.doi.org/10.30574/msarr.2024.10.2.0043  
[45] S. Wang, Z. Li, H. Qian, C. Yang, Z. Wang, M. Shang, V. Kumar, S. Tan, B. Ray, P. Bhatia, R. Nallapati, M. K. Ramanathan, D. Roth, and B. Xiang, 
"ReCode: Robustness Evaluation of Code Generation Models," arXiv preprint arXiv:2212.10264, Dec. 2022. [Online]. Available: 
https://doi.org/10.48550/arXiv.2212.10264  
[46] S. Barocas, M. Hardt, and A. Narayanan, Fairness and Machine Learning: Limitations and Opportunities. Cambridge, MA: MIT Press, December. 
2023. [Online]. Available: https://fairmlbook.org/ 
[47] M. Veale and F. Zuiderveen Borgesius, "Demystifying the Draft EU Artificial Intelligence Act," Computer Law Review International, vol. 22, no. 
4, pp. 97-112, 2021. https://doi.org/10.9785/cri-2021-220402 
[48] B. Mittelstadt, C. Russell, and S. Wachter, "Explaining Explanations in AI," in Proceedings of the Conference on Fairness, Accountability, and 
Transparency (FAT '19), Atlanta, GA, USA, January 2019, pp. 279–288. doi: 10.1145/3287560.3287574. [Online]. Available: 
https://dl.acm.org/doi/10.1145/3287560.3287574  

JCSTS 7(4): 556-572 
 
Page | 571  
[49] H. Hata, E. Shihab, and G. Neubig, "Learning to Generate Corrective Patches using Neural Machine Translation," arXiv preprint 
arXiv:1812.07170, July 2019. [Online]. Available: https://doi.org/10.48550/arXiv.1812.07170  
[50] M. White, M. Tufano, M. Martinez, M. Monperrus, and D. Poshyvanyk, "Sorting and transforming program repair ingredients via deep 
learning code similarities," in 2019 IEEE 26th International Conference on Software Analysis, Evolution and Reengineering (SANER), 2019, pp. 479-
490. https://doi.org/10.1109/SANER.2019.8668043 
[51] M. Kazemitabaar, J. Chow, C. K. T. Ma, B. J. Ericson, D. Weintrop, and T. Grossman, "Studying the effect of AI Code Generators on Supporting 
Novice Learners in Introductory Programming," in Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23), 
Hamburg, Germany, April 2023, pp. 1–15. doi: 10.1145/3544548.3580919. [Online]. Available: https://doi.org/10.1145/3544548.3580919  
[52] European Parliamentary Research Service, "Economic impacts of artificial intelligence (AI)," European Parliament, PE 637.967, April 2019. 
[Online]. Available: https://www.europarl.europa.eu/RegData/etudes/BRIE/2019/637967/EPRS_BRI(2019)637967_EN.pdf  
[53] D. Dellermann, P. Ebel, M. Söllner, and J. M. Leimeister, "Hybrid Intelligence," Business & Information Systems Engineering, vol. 61, no. 5, pp. 
637–643, March 2019. doi: 10.1007/s12599-019-00595-2. [Online]. Available: https://link.springer.com/article/10.1007/s12599-019-00595-2  
[54] A. Beheshti et al., "Natural Language-Oriented Programming (NLOP): Towards Democratizing Software Creation," in 2024 IEEE International 
Conference on Software Services Engineering (SSE), 2024. https://arxiv.org/html/2406.05409v1 
[55] Jaivrat Das, Mahima Yadav, and Arvind Jaiswal, "The Rise of Low-Code/No-Code Development: Will These Tools Democratize Software 
Development and Make It Accessible to Everyone?" International Research Journal of Modernization in Engineering Technology and Science, vol. 
6, no. 6, pp. 1287–1293, Jun. 2024. [Online]. Available: 
https://www.irjmets.com/uploadedfiles/paper/issue_6_june_2024/58989/final/fin_irjmets1718008454.pdf  
[56] Shraddha Barke, Michael B. James, and Nadia Polikarpova, "Grounded Copilot: How Programmers Interact with Code-Generating Models," 
arXiv preprint arXiv:2206.15000, Jun. 2022. [Online]. Available: https://arxiv.org/pdf/2206.15000.pdf  
[57] "10 AI in Healthcare Case Studies," DigitalDefynd, July 2024. https://digitaldefynd.com/IQ/ai-in-healthcare-case-studies/ 
[58] "40 Detailed Artificial Intelligence Case Studies," DigitalDefynd, May 2024. https://digitaldefynd.com/IQ/artificial-intelligence-case-studies/ 
[59] J. Varajão, A. Trigo, and M. Almeida, "Low-code development productivity: 'Is winter coming' for code-based technologies?" Queue, vol. 21, 
no. 5, pp. 40, Sep./Oct. 2023. doi: 10.1145/3631183. [Online]. Available: https://doi.org/10.1145/3631183  
[60] D. Moher et al., "Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement," PLoS Medicine, vol. 6, no. 7, p. 
e1000097, 2009. https://doi.org/10.1371/journal.pmed.1000097 
[61] S. Kalyuga, "Cognitive load theory in practice," in Cognitive Load Theory, J. Sweller, P. Ayres, and S. Kalyuga, Eds. New York: Springer, 2011, 
pp. 197–206. doi: 10.1007/978-1-4419-8126-4_10. [Online]. Available: https://education.nsw.gov.au/content/dam/main-education/about-
us/educational-data/cese/2017-cognitive-load-theory-practice-guide.pdf  
[62] S. Papert, Mindstorms: Children, Computers, and Powerful Ideas. New York, NY: Basic Books, 1980. https://doi.org/10.1007/978-3-0348-
5357-6 
[63] A. S. Garg, G. J. Nastasi, and J. Sallam, "Preliminary Evidence of the Use of Generative AI in Health Care Clinical Services: Systematic Narrative 
Review," JMIR Med. Inform., vol. 12, e51781, Mar. 2024. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10993141/  
[64] G. Recupito, F. Pecorelli, G. Catolino, V. Lenarduzzi, D. Taibi, D. Di Nucci, and F. Palomba, "Technical debt in AI-enabled systems: On the 
prevalence, severity, impact, and management strategies for code and architecture," Journal of Systems and Software, vol. 216, 112151, Oct. 
2024. doi: 10.1016/j.jss.2024.112151. [Online]. Available: https://doi.org/10.1016/j.jss.2024.112151  
[65] A. M. T. Ali, A. A. Alsaeed, and M. S. Alzain, "A systematic literature review on the impact of AI models on the security of generated code," 
PLOS ONE, vol. 19, no. 5, e0285123, May 2024. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11128619/  
[66] M. D. Trinh, T. H. Nguyen, T. M. Nguyen, and M. T. Tran, "Sustainability Integration of Artificial Intelligence into the Software Development 
Life Cycle: A Systematic Literature Review," in Proc. 3rd Int. Workshop Green Sustainable Softw. (GREENS 2024), Lisbon, Portugal, Apr. 2024. 
[Online]. Available: https://research.vu.nl/files/311044814/GREENS-2024_TrinhEtAl_Sustainability-Integration-AI-into-SDLC.pdf  
[67] International Telecommunication Union, "AI Ready – Analysis Towards a Standardized Readiness Framework," ITU, Geneva, Switzerland, 
2024. [Online]. Available: https://www.itu.int/dms_pub/itu-t/opb/ai4g/T-AI4G-AI4GOOD-2024-2-PDF-E.pdf 
[68] A. O. de Carvalho, M. A. Alves, and M. J. de Oliveira, "Establishing a Low-Code/No-Code-Enabled Citizen Development Strategy," MIS 
Quarterly Executive, vol. 23, no. 3, pp. 259–265, Sep. 2024. [Online]. Available: https://research.vu.nl/files/389141118/Establishing_a_Low-
Code_No-Code-Enabled_Citizen_Development_Strat.pdf 
[69] J. Trigo, J. A. Garcia-Garcia, J. M. Murillo, and J. M. Vara, "Low-code Development Productivity," ACM Queue, vol. 21, no. 1, pp. 1–19, Jan. 
2023. [Online]. Available: https://doi.org/10.1145/3631183  
[70] A. Kumar and S. Sharma, "Analysis of Low Code-No Code Development Platforms in Comparison with Traditional Development 
Methodologies," International Journal for Research in Applied Science and Engineering Technology, vol. 9, no. 12, pp. 1–8, Dec. 2021. [Online]. 
Available: https://www.ijraset.com/research-paper/low-code-no-code-development-platforms-in-comparison-with-traditional-development-
methodologies  
[71] C. Brandon and T. Margaria, "Low-Code/No-Code Artificial Intelligence Platforms for the Health Informatics Domain," ECEASST, vol. 82, Oct. 
2023. [Online]. Available: https://doi.org/10.14279/tuj.eceasst.82.1221  
[72] A. Karpathy, "Tweet: There's a new kind of coding I call 'vibe coding'," X (formerly Twitter), February 6, 2025. [Online] Available: 
https://x.com/karpathy/status/1886192184808149383  
[73] P. Pajo, "Vibe Coding: Revolutionizing Software Development with AI-Generated Code," ResearchGate, Mar. 14, 2025. [Online]. Available: 
https://www.researchgate.net/publication/389848540_Vibe_Coding_Revolutionizing_Software_Development_with_AI-Generated_Code 
[74] X. Li, "A Review of Prominent Paradigms for LLM-Based Agents: Tool Use, Planning (Including RAG), and Feedback Learning," in Proceedings 
of the 31st International Conference on Computational Linguistics (COLING 2025), Abu Dhabi, UAE, Jan. 2025, pp. 9760–9779. [Online]. Available: 
https://aclanthology.org/2025.coling-main.652/ 
[75] Ayush Patel, Atama Prakash Singh, Kanishk Rastogi, Anup Yadav, Sumit Verma, and Rajkumar Kushawaha, "AUTODEV: CODE GENERATION 
AND EXECUTION PLATFORM POWERED BY GENERATIVE AI," International Research Journal of Modernization in Engineering Technology and 

Democratizing Software Engineering through Generative AI and Vibe Coding: The Evolution of No-Code Development 
Page | 572  
Science, vol.6, no. 12, Dec. 2024. [Online]. Available: 
https://www.irjmets.com/uploadedfiles/paper/issue_12_december_2024/65359/final/fin_irjmets1735409120.pdf  
[76] J. Friedman, "AI-generated code in startup development: Quantitative analysis of Y Combinator Winter 2025 cohort," TechCrunch, Mar. 6, 
2025. [Online]. Available: https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-
entirely-ai-generated/ 
[77] M. Chow and O. Ng, "From technology adopters to creators: Leveraging AI-assisted vibe coding to transform clinical teaching and learning," 
Medical Teacher, pp. 1–3, 2025. doi: 10.1080/0142159X.2025.2488353. [Online]. Available: 
https://www.tandfonline.com/doi/full/10.1080/0142159X.2025.2488353 
[78] S. Willison, "Not all AI-assisted programming is vibe coding (but vibe coding rocks)," Mar. 19, 2025. [Online]. Available: 
https://simonwillison.net/2025/Mar/19/vibe-coding/ 
[79] M. Kazemitabaar, J. Liu, and S. Papadakis, "Exploring the Design Space of Cognitive Engagement Techniques with AI-Generated Code," in 
Proceedings of the 29th International Conference on Intelligent User Interfaces (IUI '25), pp. 1–13, 2025. [Online]. Available: 
https://austinhenley.com/pubs/Kazemitabaar2025IUI_AIFriction.pdf 
[80] Gartner, "Forecast Analysis: Low-Code Development Technologies," Gartner Research, 2021. [Online]. Available: 
https://www.gartner.com/en/documents/3995846 
[81] P. Vaithilingam, E. L. Glassman, P. Groenwegen, S. Gulwani, A. Z. Henley, R. Malpani, D. Pugh, A. Radhakrishna, G. Soares, J. Wang, and A. Yim, 
"Towards More Effective AI-Assisted Programming: A Systematic Design Exploration to Improve Visual Studio IntelliCode's User Experience," in 
Proceedings of the 2023 IEEE/ACM 45th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), 
Melbourne, Australia, May 2023, pp. 1–13. doi: 10.1109/ICSE-SEIP58684.2023.00022. [Online]. Available: https://doi.org/10.1109/ICSE-
SEIP58684.2023.000  
[82] Y. Chen, S. Lee, Y. Xie, Y. Yang, and S. Oney, "CoPrompt: Supporting Prompt Sharing and Referring in Collaborative Natural Language 
Programming," in Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, 2024, pp. 1-14. 
https://doi.org/10.1145/3613904.3642212 
[83] A. M. McNutt, C. Wang, R. A. Deline, and S. M. Drucker, "On the Design of AI-Powered Code Assistants for Notebooks," in Proceedings of the 
2023 CHI Conference on Human Factors in Computing Systems, 2023, pp. 1-16. https://doi.org/10.1145/3544548.3580940 
[84] H. Strobelt, A. Webson, V. Sanh, B. Hoover, J. Beyer, H. Pfister, and A. M. Rush, "Interactive and Visual Prompt Engineering for Ad-hoc Task 
Adaptation with Large Language Models," IEEE Transactions on Visualization and Computer Graphics, vol. 29, no. 1, pp. 1146-1156, 2023. 
https://doi.org/10.1109/TVCG.2022.3209479 
[85] K. Rokis and M. Kirikova, "Exploring Low-Code Development: A Comprehensive Literature Review," Complex Systems Informatics and 
Modeling Quarterly, vol. 36, pp. 68–86, 2023. [Online]. Available: 
https://pdfs.semanticscholar.org/1f5b/771f752250036b423507f2ffc9c2c6d18470.pdf 
[86] Google LLC, "Firebase Studio: Integrated AI-assisted development environments for full-stack applications," Apr. 2025. [Online]. Available: 
https://firebase.google.com/docs/studio 
[87] S. Garner, "Reducing the cognitive load on novice programmers," in Proceedings of the ED-MEDIA 2002 World Conference on Educational 
Multimedia, Hypermedia & Telecommunications, Denver, CO, USA, Jun. 2002. [Online]. Available: https://files.eric.ed.gov/fulltext/ED477013.pdf 
[88] C. D. Hundhausen, S. F. Farley, and J. L. Brown, "Can direct manipulation lower the barriers to computer programming and promote transfer 
of training? An experimental study," ACM Transactions on Computer-Human Interaction, vol. 16, no. 3, pp. 1-40, 2009. 
https://doi.org/10.1145/1592440.1592442 
[89] Y. Luo, P. Liang, C. Wang, M. Shahin, and J. Zhan, "Characteristics and Challenges of Low-Code Development: The Practitioners' Perspective," 
in Proceedings of the 15th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement, 2021, pp. 1-12. 
https://doi.org/10.1145/3475716.3475782 
[90] A. Muhammad, "Citizen Developers: The New Accelerators for Digital Transformation," Muma Business Review, vol. 8, no. 13, pp. 173-180, 
Dec. 2024. [Online]. Available: https://mumabusinessreview.org/2024/MBR-08-13-173-180-Muhammad-CitizenDeveloper.pdf
