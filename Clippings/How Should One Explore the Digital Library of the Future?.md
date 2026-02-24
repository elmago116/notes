---
title: How Should One Explore the Digital Library of the Future?
year: "2021"
authors:
  - Edward A. Fox
  - Prashant Chandrasekar
tags:
  - lis/HCI
  - Tech/KG
  - design/UX
  - lis
Type: Article
journal: Data and Information Management,
apa_citation: Fox & Chandrasekar, 2021
doi: https://doi.org/10.2478/dim-2021-0003
---
![[How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man.pdf#page=2&rect=48,396,560,732|How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man, p.350]]

![[How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man.pdf#page=3&rect=34,489,365,735|How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man, p.351]]

![[How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man.pdf]]


Linked PDF file(s) for **How-Should-One-Explore-the-Digital-Library-of- 2021 Data-and-Information-Man**:

- [[PDF/How-Should-One-Explore-the-Digital-Library-of-_2021_Data-and-Information-Man.pdf]]

## PDF text extraction

Data and Information Management, 2021; 5(4): 349–362
Research Article Open Access
Edward A. Fox*, Prashant Chandrasekar
How Should One Explore the Digital Library of the 
Future?#
https:/ /doi.org/10.2478/dim-2021-0003
received November 23, 2020; accepted February 7, 2021.
Abstract: This article partially addresses a challenge 
from Licklider in his 1965 book on “ Libraries of the 
Future,” focusing on how to build extensible digital 
libraries that can dramatically expand the support of 
exploration. A new methodology connects the efforts of 
User eXperience researchers with those of subject matter 
experts (domain scientists, curators, researchers, and so 
on) and developers. This allows constructing a knowledge 
graph representing the relationships among goals, tasks, 
workflows, and services. A reasoner empowers authorized 
users to have their goals met with suitable workflows 
that are dynamically generated and executed. Student 
teams have applied the new methodology to support 
users interested in tweets, web pages, or electronic 
theses and dissertations, as well as those curating and 
experimenting with those collections. Exploration is thus 
broadened across content types and their elements, with 
an extensible set of services, to address an arbitrary set of 
stakeholder goals.
Keywords: Licklider, 5S framework,  scenarios,  
procognitive, adaptive self-organization, artificial 
intelligence, human–computer interaction, knowledge 
graphs, user experience, customer  discovery, workflows
1  Introduction
Motivated by the Foreword of the book “ Libraries of the 
Future” (dedicated to Vannevar Bush) (Licklider, 1965), 
this article focuses on users, exploration (White & Roth, 
2009), and future directions of the digital library (DL) 
field, moving us toward procognitive systems. Many 
different DL “users,” each a member of a society, engage 
in a diversity of scenarios, often involving some aspect of 
exploration, usually of the DL content streams. Services – 
e.g., searching, browsing, recommending, and visualizing 
– help those users leverage knowledge structures and 
spatial representations. Following on the final sentence 
of Dr Licklider’s 1965 book, we “call for a formal base 
plus an overlay of experience,” leading to a new way to 
build better DLs. Dr Licklider said that we seek “the facts, 
concepts, principles, and ideas that lie behind the visible 
and tangible aspects of documents,” to help us acquire 
and use knowledge. The key support for exploration comes 
from the following consideration: “The console of the 
procognitive system will have two special buttons, a silver 
one labeled ‘Where am I” and a gold one labeled ‘What 
should I do next?’ ” Accordingly, this article considers 
how to build and use a DL suitable for such exploration.
For >55  years, researchers have applied artificial 
intelligence (AI), natural language processing (NLP), 
representations (data, information, and knowledge), 
question-answering, databases, human–computer 
interaction (HCI), and other techniques described by Dr 
Licklider, to facilitate exploration. We have a vast range 
of hardware and software services available, but without 
a more formal approach, adaptive self-organization and 
tailored exploration will not be enabled.
The 5S (Societies, Scenarios, Spaces, Structures, and 
Streams) framework (Fox, Gonçalves, & Shen, 2012; Shen, 
Gonçalves, & Fox, 2013; Fox & Silva Torres, 2014; Fox & 
Leidig, 2014) can help us build, apply, and improve (Shen, 
Vemuri, Fan, & Fox, 2006; Moreira et al., 2009) DLs to 
facilitate exploration (Vemuri, Silva Torres, Fox, Fan, & 
Shen, 2006), through a formal approach that will simplify 
such efforts, making them extensible through both human 
and computing agents.
To more easily build DLs, we propose collaboratively 
constructing knowledge graphs (Meno & Vincent, 2020) 
– involving user experience (UX) (Hartson & Pyla, 2012) 
designers, subject matter experts (SMEs), and developers 
*Corresponding author: Edward A. Fox, Department of Computer 
Science, Virginia Tech, Blacksburg, VA 24061, United States.  
Email: fox@vt.edu 
Prashant Chandrasekar, Department of Computer Science, Virginia 
Tech, Blacksburg, VA 24061, United States 
# This paper is derived from the keynote presentation with the same 
title at the Joint Conference on Digital Libraries (JCDL) 2020.
 Open Access. © 2021 Edward A. Fox, Prashant Chandrasekar, published by Sciendo. 
  This work is licensed under the Creative 
Commons Attribution-NonCommercial-NoDerivatives 3.0 License.

350    Edward A. Fox, Prashant Chandrasekar
who specify connections to services and workflows, 
enabling DL operations atop a workflow engine (Liew et al., 
2016). User exploration, recommendations of adaptations 
of existing workflows, and AI-based optimizations and 
solutions to new problems will all expand the knowledge 
graph to ensure new and more helpful assistance. When 
this is accomplished, we could teach and learn about 
this next generation of DLs, further developing suitable 
curricula and educational modules that rest upon a solid 
theoretical foundation, helping spread understanding of 
key concepts and best practices (Pomerantz, Oh, Yang, 
Fox, & Wildemuth, 2006; Pomerantz, Wildemuth, Yang,  
& Fox, 2006).
1.1  Problem
Exploration in DLs generally is too narrowly conceived 
and, therefore, only supports a limited type of exploration. 
Exploration as presently thought of (via searching, 
browsing, and visualizations) is for relatively static DLs 
where the goal is to find one or more documents. What 
about goals and tasks that address the needs of a broader 
audience or set of stakeholders? What about exploration 
across the Information Life Cycle, as in Figure 1? There is 
no room for typical DL systems to evolve, in terms of user 
interaction or functionality, based on evolving user needs.
This is primarily because the typical DL tends to 
focus on delivering one class of content to one type of 
user. As a result, typical DLs are prone either to becoming 
obsolete much sooner than expected or to require massive 
enhancement at great cost; there is little-to-no room for 
narrowly conceived systems to grow.
1.2  Broadening of Scope for DLs
To address this problem, we consider the 5S framework, 
which brings us back to fundamentals, to view a DL as a 
complex system with the following characteristics (Fox, 
Gonçalves, & Shen, 2012; Fox & Leidig, 2014; Fox & Silva 
Torres, 2014; Shen, Gonçalves, & Fox, 2013):
i. Helps satisfy the information needs of users 
(societies);
ii. provides information services (scenarios);
iii. organizes information in usable ways (structures);
iv. presents information in usable ways (spaces); and
v. communicates information to users (streams).  
Figure 1. The information life cycle involving different DL activities, adapted from Borgman et al. (1996). Note: UCLA, University of California, 
Los Angeles.

 How Should One Explore the Digital Library of the Future?   351
Exploration can be reconceptualized from such 
theoretical foundations, covering a broad range of 
possibilities for each of the five Ss and their combinations 
(e.g., different scenarios for different societies).
An extended version of the Information Life Cycle 
(Borgman et al., 1996), which incorporates the key 
performance indicators in the outer ring (Shen, Vemuri, 
Fan, & Fox, 2006; Moreira et al., 2009; Shen, Gonçalves, & 
Fox, 2013), shown in Figure 1, appears to limit exploration 
to Discovery, but we also should support exploration 
during Utilization and Creation, as well as tasks related 
to Reputation, Retention Mining, Archiving, and 
Preservation.
Further, document exploration should be broadened 
both vertically and horizontally. The first brings in 
subdocuments (e.g., passages, figures, tables, definitions, 
and references) and collections of documents (e.g., 
according to classification or clustering or linking, or in 
special collections, or through federation or harvesting). 
The second brings in other digital objects, ranging over 
content types (media, genres) and varying as to size/
scale/granularity, as well as peculiarities of domain (e.g., 
archaeology, health care). Users are not only authors, 
editors, reviewers, and readers but also curators, SMEs, 
sponsors, inventors, reporters, data scientists, digital 
librarians, and digital library researchers/developers. 
The last two categories need support for work across the 
building of DL software, its deployment as an operational 
DL, its filling with content, and across an extensible set 
of services including those shown in the taxonomy in  
Figure 2.
Exploration should cover not only simple interactions 
involving queries, facets, browsing, and/or visualization 
but also long and complex symbiotic collaborations 
that make use of not only HCI but also AI (with NLP , 
planning, inference, prediction, learning, and so on) to 
address needs, tasks, and goals (Licklider, 1965). These 
broaden much further through the emergence of entire 
ecosystems, with edge computing spread over the Internet 
of Things (IoT). Exploration can involve integrations 
and synchronizations across all of these, extending the 
already-existing combinations. This calls for treating each 
type of exploration as a digital object, to be combined 
through workflows and other programmatic schemes, 
which can be facilitated through the 5S approach to 
formally define each type of exploration.
1.3  Scope of the Solution
In this section, we focus on people who need a system 
wherein (a) Curators/SMEs/end users can explore existing 
information and request newer information goals in the 
same information domain; (b) UX researchers, through 
customer discovery, can capture and represent the 
information goals (Ulwick, 2005); and (c) Developers/
scientists/data analysts can continuously produce/
improve upon solutions to extract/derive/extend the 
information.
Our solution, partially explained in the remainder of 
this article, connects two systems, with a semiautomatic 
process/engine in the middle. System 1 is a DL for UX 
Figure 2. DL services taxonomy, adapted from Fox, Gonçalves, and Shen (2012). 

352    Edward A. Fox, Prashant Chandrasekar
researchers to explore and capture evolving user goals. 
Its engine supports a collaborative effort between UX 
researchers and developers to break down goals into tasks 
and subtasks and to reuse/build services to support each 
task. System 2 is a DL for end users, curators, researchers, 
and SMEs; it allows them to explore both information and 
information goals.
We have not built System 1 in software; rather, we 
adopt a collaborative human-implemented approach. 
Thus, the UX process of customer discovery has been 
tied into System 1’s engine component. We discuss that 
in the next section (Section 2), which explains our new 
methodology. Then, we introduce System 2 in Section 3.
2  New Methodology to Build DLs
This section describes the first part of our effort to build 
a workflow-based information system solution that 
supports SMEs.1 We specify a methodology that will help 
design a set of workflows built to answer specific SME 
needs. In the first step of the methodology, we identify 
the user goals using the expertise of a UX researcher.  In 
the second step, we consult with developers, analysts, 
and/or scientists and associate each goal with specific 
tasks. In the third step, using the experience of the 
developers and the information captured in the previous 
steps, we describe all implementation-specific functions 
and entities that are required for solving each task. 
Then, using all of the information, we construct a joint 
representation of information goals and workflows. 
This joint representation guides our information  system 
solution.
2.1  Process of Customer Discovery
Our methodology begins with the process of UX research 
(Hartson & Pyla, 2012). A UX researcher is tasked with 
studying users, their habits, and behaviors, as well as 
forming design-informing models using various standard 
practices and procedures. These include contextual 
inquiry and analysis, persona building, and usability 
testing. Everything begins with understanding the user, 
their roles, and their goals. In commercial settings, such 
1 In the interest of brevity, we use “SME” throughout, as shorthand 
for those in any of the various stakeholder groups, including end 
users, curators, researchers, data scientists, and others involved in 
development, operation, preservation, archiving, and so on.
customer discovery (Ulwick, 2005) is essential to ensure 
product–market fit.
The design process does not end with this. The 
UX researcher then should work with a UX designer, 
a user interface (UI) designer, a product manager, and 
the development team as part of an exhaustive, but 
elegant, process that ensures sound product design. In 
our case, the “product” that we are building starts with 
a set of workflows and workflow-related information 
that we forward to the workflow engine. The designers, 
mentioned above, come into play primarily when building 
an interactive system, where the design of the UI plays a 
significant role in designing and developing every other 
part of the system. Accordingly, in future versions of our 
system, those designers have an additional challenge, 
regarding how to present the set of workflows and how to 
aid SMEs to interact with an interface that would trigger 
them.
The UX research process is conducted to answer the 
following questions, for each type of user or stakeholder.
i. Who is the user?
ii. What are their g oals?
iii. How do they currently accomplish those goals?
With the user-related information, we can construct what 
is known as a “user persona.” In a persona, we can list the 
user’s role. The category of user role for all of our users is 
that of an “SME in their area of research.” We can further 
enrich the details of the persona by identifying research 
interests, data sets they frequently work with, and other 
information related to their research. Defining a persona 
gives the implementation team a point of reference when 
building a solution.
While it might not be essential to capture a rich 
persona for the sake of building the workflow, capturing 
the research goals (or problems), on the other hand, is 
very important. In some cases, an SME might even provide 
some restrictions and require us to follow a set of steps to 
achieve the goal.
Once we identify both the user persona and the goal(s), 
we apply the 5S approach to store the information. We 
map the persona-related information to the Society aspect 
of our description. The goal is captured in a Scenario. In 
the case that the SME breaks down the goal into a set of 
tasks, the Structure aspect of the 5S framework would 
represent the association among goals and tasks. We can 
choose the structure to be a graph structure where the 
goal is the root node, and its children are the tasks. Such 
a structure implies that the tasks need to be completed as 
a part of solving the goal. Furthermore, tasks may have 
child descendants themselves.

 How Should One Explore the Digital Library of the Future?   353
Once we have identified specific research goals that 
are of interest to the different user personas, we need to 
come up with a plan to solve them.
2.2  Workflows
2.2.1  Process of Workflow Generation: Part 1
In this step, we attempt to break the goal down into units 
knows as tasks. Tasks can be further broken down into 
subtasks. As defined by Hartson and Pyla in their book on 
UX, a task or a subtask refers to things that users do in order 
to achieve their goal (Hartson & Pyla, 2012). A subtask 
can be thought of as a task by itself. We can produce 
this breakdown through the expertise of engineers and 
developers who are familiar with addressing such goals 
and tasks. In some cases, the identified goal need not be 
broken down further. For example, if one of the goals of 
SMEs is to collect tweets about an event, and they provide 
the UX researcher with a search query, the developer may 
decide that this goal can be solved without  breaking it 
down into smaller units. In that case, we treat the goal as a 
task and move on to the next step of the process. So, when 
and to what extent do we break down the goals?
When the developer identifies that the goal requires 
multiple steps to solve, they break down the goal into a set 
of tasks. The primary purpose of identifying the tasks is to 
guide the overall design such that the final design of the 
workflow should support the task and subtasks identified.
A hierarchical relationship is formed between goals, 
tasks, and subtasks. The meaning of the relationship is 
this: doing a subtask is a part of doing a task.
We apply the 5S framework to store the tasks and 
subtasks, in addition to the relationships between them 
and the goal. As discussed in Step 1, the relationship 
between the goal, tasks, and subtasks is mapped to the 
Structure aspect of our 5S-framework-based description.
Prior to this step, we were provided with SME goals 
that might not have been described to an extent such 
that we could facilitate support. The process of breaking 
down goals into tasks is not straightforward. Through the 
expertise of the developers, we were able to process the 
goals and produce a set of “solvable” units (or tasks). We 
next have to find a way to address these user tasks.
2.2.2  Process of Workflow Generation: Part 2
At this stage, we have identified all aspects of the 
workflow that need support from functions. It is in this 
step that we decide what set of functions we want to 
apply to complete each (sub)task. We again borrow the 
definition of a function from Hartson and Pyla (2012), as 
a thing that the system does. This step requires the most 
active collaboration between the UX researchers and the 
developers. To design a solution for a task, developers 
have many options of functions or algorithms from which 
they can choose.
The UX researcher interacts with the developer to 
exchange user expectations on output and the available 
information on inputs. One of two things happens:
i. The SMEs ha ve briefed the UX researcher on their 
requirements, and the information is in the UX-er’s 
possession. In this case, this information is passed on 
to the developer, and the developer makes a decision 
accordingly.
ii. Alternatively, the UX researcher gets limited 
information due to the nonfamiliarity of the SME with 
the various stages of implementation.
Based on the discussion, the developer might have 
to include an input/output service as a part of the 
workflow to solicit input from the SME regarding the 
implementation. During this period, the developer also 
identifies other implementation-specific parameters. 
Finally, the developer identifies existing services, or 
designs a set of new services, each of which encapsulates 
an algorithm or function that is essential for the specific 
task to be complete. Figure 3 highlights the aspects of the 
services that the developer captures.
Ultimately, the developers combine all of the services 
and create a workflow based on what they have learned 
and the structure of the decomposition of the goal into 
tasks and subtasks. We can derive the workflow sequence 
by doing a topological ordering of the graph structure. 
Through this step of the methodology, we can create a 
workflow that represents the combined execution of all of 
the subtasks and tasks that make up the goal.
2.3  Summary of Methodology
We thus have the following methodology: (1) a process 
to take the user goals and produce a solution that is built 
specifically for them; and (2) a unified representation of 
SME goals, workflows that support those goals, and all 
the mappings in between. Representing user goals and 
workflows in this manner removes the knowledge barrier 
and terminology mismatch generally experienced when 
using standard workflow management systems. The 
workflows are written for SME information goals. From the 

354    Edward A. Fox, Prashant Chandrasekar
SMEs’ point of view, they only need to request the desired 
information, and the information system implementation 
should generate a workflow. This generated workflow, 
when executed, will produce the information that they 
requested.2 The information supported by the information 
system workflows is dependent on the stakeholder/
research community and its problems/needs. As SME 
needs evolve over time, new services/workflows can 
be designed and incorporated, making the information 
system extensible.
3  New DL Design
In this section, we address the following question: How 
do we facilitate information discovery of what we have 
extracted in a manner that is accessible to SMEs?
To be able to do so, we need the following:
i. Processes to build a knowledge base to capture and 
store the artifacts/information;
ii. a representation that organizes them in a manner that 
maintains the various associations (goals to tasks, 
tasks to services);
iii. a processing component or an engine to compile these 
associations and deduce the relationships between 
information goals as well as between intermediate 
states of information; and
iv. a solution that should scale to handle large numbers 
of goals and tasks.
2 The UI and execution of the workflow by the workflow engine are 
out of the scope of this article.
These needs match well with the characteristics and 
components of a knowledge graph (Ehrlinger & Wöß, 
2016).
The SMEs can leverage a knowledge graph where 
the nodes represent the  end “state” of the information 
that they want to acquire. The relationship between the 
nodes leads to the events/operations taken to reach the 
goal. Thus, we define a workflow as a sequence of events/
operations that changes the state of information. From the 
SMEs’ point of view, all they need to do is select the node 
representing their interest. Under the hood, the very same 
representation leads to a set of paths that represent data 
analysis-based workflows, which, when executed, deliver 
the information requested by the SMEs. The representation 
of the knowledge eliminates the need for the SME to know 
the details of the operations. Additionally, the structure’s 
flexibility allows us to represent data analysis workflows 
of any form, eliminating the need for an additional 
knowledge base and a middle layer to translate user 
queries to workflows. We can capture and represent both 
the SME information needs and the workflows together. 
The scope of information supported by the graph is 
flexible and is dependent on the (research) community 
and the problems that the knowledge graph-based system 
is looking to support.
We could represent workflows as either control-flow 
graphs or data-flow graphs (Liew et al., 2016). Control-
flow graphs are made up of tasks serving as nodes, with 
the order of execution specifying the edges. In data-
flow graphs, tasks (edges) represent the flow of the data 
(nodes). In either case, workflows are represented as 
directed-acyclic graphs or directed-cyclic graphs (to 
support iteration). Regardless of which abstraction one 
chooses to adopt, the constraint we face represents not 
one but multiple workflows for a particular end goal (state 
of information). We want to represent task precedence 
or data dependency AND multiple paths to a particular 
information/node state. Regardless of the abstraction 
we select, we cannot represent both types of information 
using a “binary” edge.
Accordingly, we model the SME goals and workflows 
using a directed hypergraph-based knowledge graph. 
Unlike other abstractions, a hypergraph allows us to 
specify n-ary relations or “hyperedges” within a graph 
(Gallo, Longo, Pallottino, & Nguyen, 1993). This property 
allows us to represent multiple data dependencies of a task 
with just one (hyper)edge. As a result, every edge incident 
to a node of interest to an SME represents a different path 
(or workflow) to achieve that state of information. It would 
Figure 3. Example template showing the implementation-specific 
information that is captured in Part 2 of the methodology. Note: I/O, 
input/output.

 How Should One Explore the Digital Library of the Future?   355
be very cumbersome to capture this relationship using 
only traditional “binary” edges.
Figures 4 and 5 are examples of two hypergraph 
representations of information goals and their relationship 
with one another via services. Table 1 gives details on the 
nodes of Figure 5.
Let us consider a toy example as shown in Figure 4. 
This is a graphical representation of information goals/
states of information (shown as alphabets) connected to 
one another by services (shown as numbers). All of this is 
identified from the methodology. From this representation, 
we can observe that there are three different workflows 
to derive information goal “a.” All three workflows can 
derive that information goal. Based on the input provided, 
a workflow is selected.
With our proposed representation of the hypergraph, 
we can support the various types of explorations that are 
of interest to the SMEs.
The top of Figure 6 showcases the artifacts produced 
from the methodology. The artifacts serve as digital objects 
for the “new” DL. These DL components, shown at the 
bottom of the figure, are essential pieces to operationalize 
each user type’s new kind of exploration. At the center 
of it all, we have the knowledge graph along with the 
reasoner and the graph-based representation of artifacts 
produced from the methodology. When a user of the 
system requests some state as their information goal, the 
reasoner generates the set of services or transformations 
that will produce the requested information. The reasoner 
forwards this information to the Workflow Management 
System (WMS). The WMS is responsible for orchestrating 
and executing the workflow, which consists of individual 
services. This component will connect with a Services 
Registry. The registry will index and store all of the 
services built by developers. The exploratory activities of 
the users via an interface trigger the entire process. The 
range of exploratory activities supported by this DL will 
be dynamic and based on the domains of the following 
components: (a) ever-changing needs of the SME or 
researchers, (b) the advances in models/algorithms 
deployed as services by the developers, and (c) the type 
Figure 5. A graphical representation of one of the workflows from 
a case study. Notes: The basis of the workflow is to produce a 
comparison of tweets that report outages, against tweets that 
report restoration of services, during a hurricane. As in Figure 4, the 
nodes represent the information goals and the edges represent the 
workflow services to produce that information. Note: SME, subject 
matter expert.
Figure 4. A toy example of workflow services connecting the 
various states of information. Nodes represent information goals. 
(Hyper)Edges represent the workflow services that perform the 
transformations.
Table 1
Description of Nodes for the Case Study Graph Shown in Figure 5
Node/information 
goal
Description
A Hurricane-related tweets
B Tweets with sentiment score
C Tweets with geolocation
D Tweets classified into the following 
categories: Caution and advice; Injured or 
dead people; Utility damage; Sympathy 
emotional support; and so on
E Tweets about outage
F Tweets about restoration
G Tweets classified into the following 
categories: Power; Transportation; Sewage; 
Water; Communication

356    Edward A. Fox, Prashant Chandrasekar
and quality of content created by the curators. Each of 
the user goals, services, and data collections is a digital 
object in the DL. We describe the exploratory activities in 
the next section.
4  Exploratory Activities
Table 2 lists the broad categories of services supported by 
the new DL. When called upon, these services make use of 
and affect the digital objects described in Table 3.
4.1  Exploration for the UX-Researcher
A UX-researcher (UX-R) can author and submit an SME 
Persona digital object. As the UX-Rs learn more about the 
SME, through usability testing, qualitative and quantitative 
interviews, contextual inquiry and analyses, and so on, 
they can further describe the Persona. Furthermore, their 
efforts would identify SME goals. They would use the same 
services to add or update the Goal digital objects for each 
Persona digital object. Through the process of customer 
discovery, if they observe a way to break down the Goal 
into smaller units, they would call upon the service to 
register the Goal–Task breakdown digital object.
This DL creates a platform for UX-Rs to share 
information. A UX-R can explore the repository of 
Personas, learning about a Persona’s information 
goals and expectations in terms of input and output. 
Furthermore, they can explore the intersection and 
difference in information goals among a variety of 
Personas and possibly draw a connection between them.
As can be seen, the exploratory efforts of the UX-R 
extend the functionality of the DL. As UX-Rs discover 
Personas, Goals, and Tasks, more types of SME (or 
researcher) exploratory efforts are supported.
4.2  Exploration for Curator
A curator can author and submit a Data set digital object. 
Alternatively, if the knowledge graph has an information 
goal that generates a workflow that does a form of data 
collection via crawling, then the curator could explore 
that information goal and provide “seed” information, 
such as websites to crawl, as input to the workflow.
Curators can explore the various collections and learn 
the different information that the developers have derived 
through their development efforts.
As in the case with the UX-R, the curator’s exploratory 
efforts result in more collections being available for 
exploration (by developers and SMEs), thereby extending 
the functionality of the DL.
Table 2
Definitions of Digital Library (DL) Services
Service Description
Authoring Creates a digital object and incorporates it into 
some collection of the DL.
Describing Produces a description of a digital object and 
incorporates this description into the object’s 
set of metadata specifications.
Submitting Incorporates the following:
1) new objects into the collections of the DL;
2) a new metadata specification into the set of 
metadata specifications of a digital object; or
3) a new operation into the set of operations of a 
service manager.
Browsing Given an anchor of a hypertext, returns a set of 
digital objects.
Searching Given a query, a collection, and an index for 
that collection, returns – for each object in the 
collection – a real number indicating how well 
the query matches with the object.
Exploratory
Inquiring
Given a goal as a query and objects in a 
collection via Searching, returns information 
extracted from workflow execution.
Table 3
Digital Library: Different Types of Digital Objects
Object Description
Persona Description of SME preferences in terms of 
information requirements, user interactions, and 
so on.
Goal Description of an information goal with the 
expectations of input data and output data, in 
addition to their format.
Task A step in the process of producing the SME goal.
Goal–Task 
Structure
A structured sequence of tasks, which, when 
executed, produces the desired information goal.
Service A “container” of software code that is meant to 
support a task.
Data set A document or collection that is curated by 
curators, to be used in (or produced by) services.

 How Should One Explore the Digital Library of the Future?   357
4.3  Exploration for Developer
The developer has the expertise to break down the 
information goals into solvable units. As noted in the 
Methodology section, this process of identifying solvable 
units might happen in collaboration with UX-Rs, who 
serve as proxies for SMEs. They explore the DL to find goals 
that need solving. If not already resolved by the UX-R, they 
then can author and submit the Goal–Task dependency 
structure digital object. Their main contribution to the 
knowledge graph, and the workflow generation process, 
is building services that transform each node/information 
state from one state to another. The developers make this 
contribution by authoring, describing, and submitting 
models and algorithms packaged as services to the DL. 
Their exploratory activity increases the DL ’s functionality, 
thereby increasing the support for information goals 
requested by the SME.
4.4  Exploration for SME
All of the exploratory efforts conducted by the other user 
types increase the range of exploration possible by SMEs. 
From the SMEs’ point of view, their information goals 
either have been built or are in the process of being built 
(after being submitted by the UX-R). When they interact 
with the system, SMEs indirectly explore all of the different 
services built by the developers and indirectly explore 
various tasks that produce intermediate information, 
Figure 6. Summary of methodology. Notes: The artifacts produced from the different steps of the methodology are shown at the top. They 
lead to the components of the new DL, shown at the bottom. Note: I/O, input/output; KG, knowledge graph; SME, subject matter expert; UX, 
user experience.

358    Edward A. Fox, Prashant Chandrasekar
but they directly explore the goals of interest. When they 
interact with the system, they identify information of 
interest to them and provide the information that they 
currently have. The DL system takes over the responsibility 
to find the set of transformations to take the SME’s input 
and produce the desired result.
We want the system solution implementation to 
support the following SME query: Given an information 
goal as a query, what is the workflow to derive this 
information?
4.4.1  Algorithm for Workflow Generation
Let us again consider the toy graph in Figure 4.
Let us say the SME wants the information goal “a.” 
There are three possible workflows, broken down as 
follows:
i. a = Service 1, or
ii. a = Service 2, or
iii. a = Service 3 + Service 4 + Service 5 + Service 6
We can achieve this breakdown if we go down the three 
different “paths” leading up to the information goal 
“a.” When these workflows, or sequences of services, 
are  executed by any workflow engine, we can send the 
generated information back to the SME. We can similarly 
construct workflows to generate any of the goals in the 
graph. To generate a sequence, we recursively go “up” the 
graph starting with the node representing the information 
requested by the SME. The recursion continues until 
we reach nodes with no parent. Since there are three 
hyperedges incident to the information goal “a,” there are 
three possible “paths” one could take and, therefore, three 
different workflow sequences (as we have highlighted 
above).
This process of generating a workflow is similar to the 
recursive replacement traversal of a context-free grammar 
(CFG) for generating sentences (Chomsky, 1956; Chomsky 
& Lightfoot, 2002).
A CFG is a type of formal grammar that consists of 
a set of rules known as “production rules.” We can use 
these rules to generate and describe all patterns of strings 
in a context-free language (Chomsky, 1956). A CFG has the 
following components:
i. Terminal Symbol: Characters or letters that appear in 
the strings of the language.
ii. Nonterminal Symbol: Variables that are placeholders 
for terminal symbols.
iii. Production Rule: Rules for replacing nonterminal 
symbols.
We start with a string with nonterminal symbols, and 
based on the rules, we generate a string that only has 
terminal symbols. Let us consider an example that is 
shown in Wikipedia (Wikipedia contributors, 2020).
In this example, we want to construct a language, 
where each string has only two characters from the 
alphabet: 𝛼 and 𝛽. The production rules can be found in 
Table 4.
To generate a two-alphabetic character string, we 
begin with the rule that has the S symbol. So initially our 
string is AA.
We have two replacement rules. Therefore, valid 
strings in the language can  be any of [“𝛼𝛼 ”, “𝛼𝛽”, “𝛽𝛼”, 
“𝛽𝛽”].
To summarize, to generate a sentence from a CFG, we 
begin with the start symbol. We then successively expand 
each leftmost nonterminal symbol until we replace all 
nonterminals. This recursive replacement of nonterminals 
is similar to the traversal of the directed hypergraph. Thus, 
a CFG sentence is like a workflow.
Let us consider the productions for the toy graph in 
Figure 4, shown in Table 5. After loading this grammar, 
when we attempt to generate sentences starting with the 
nonterminal S, the sentences produced will represent the 
sequence of services we need to execute, also known as a 
workflow. For instance, one of the generated sentences, 
when starting with S → a, will be S → 3(4((5)(6))). This 
means that to generate information goal “a,” a possible 
workflow is a sequence of executing service 5, service 6, 
service 4, and finally, service 3.
This algorithm is naive and is known to not scale well. 
Moreover, this solution could   have two specific problems 
(McKenzie, 1997):
i. The recursive process might fail to halt.
ii. The process does not uniformly generate a sentence at 
random.
Table 4
Example Production Rules
Left-hand side Right-hand side
S → AA
A → 𝛼
A → 𝛽
Note: Terminal symbols = 𝛼, 𝛽. Nonterminal symbol = A. S is a 
special type of nonterminal symbol that only appears in the initial 
string.

 How Should One Explore the Digital Library of the Future?   359
The first problem would occur if the grammar has a 
production of the following form: S → S S | a. This situation 
does not arise for our productions because the workflows 
are not cyclic. There will never be a circumstance where 
a nonterminal in the left-hand side of the production 
(which, in our case, is an output produced from a service) 
appears in the right-hand side of the production (which, 
in our case, represents an input to the service).
The second problem does not apply either since we 
are looking to generate  all “sentences” (or workflows) 
beginning with the particular “start symbol” (or 
information goal), i.e., all possible workflows. Further, 
given the non-recursive nature of the productions, the 
algorithm should scale linearly to the size of the graph (or 
𝒪  (V + E), where V = the number of information goals and 
E = number  of services).
Accordingly, in our prototype, this process is how 
we generate workflows  based on the information goals 
requested by SMEs.
5  Case Study
CS5604, Information Storage and Retrieval, is a course 
that has been taught during the fall semester by the first 
author. Engaging in problem-based learning, students 
build an information retrieval system. Student teams are 
tasked to each build portions of the integrated system. 
In Fall 2020, the approach was an application of the 
new methodology; the second author helped guide this 
process. Students in each team took on the roles of UX-R 
and developer.
This system’s goal is to facilitate exploration for SMEs, 
curators, and researchers for each of three collections: 
tweets, web pages, and electronic theses and dissertations 
(ETDs). Students formed five teams: one team to mine 
Table 5
Production Rules for Toy Graph 
Left-hand side Right-hand side
S → a | r
a → 1b | 2c | 3d
d → 4ef
e → 5g
f → 6h
r → 7gh
b → ∅
c → ∅
g → ∅
h → ∅
Note: S is a special type of nonterminal symbol that only appears in 
the initial string.
Figure 7. Web page team’s artifact from interviewing their SME. The rectangles represent information goals and states, while the ovals 
represent the tasks. Together, they show the breakdown of the main workflow. Note: WARC, Web Archive file format

360    Edward A. Fox, Prashant Chandrasekar
each document type, one team to design and construct 
the front-end interface, and one team to facilitate and 
integrate development efforts. Users can work both with 
these three types of documents and with associated 
metadata, extracted information, and derived constructs 
(such as chapter summaries). The three student teams 
(referred to as “content” teams) played the UX-R role 
and interviewed their respective SMEs. The SMEs for this 
effort were researchers with goals that involved each of 
the collections. The content teams as UX-Rs interviewed 
their respective SME and extracted SME information 
goals. For the tweet and ETD content teams, the SMEs 
provided them with values that they want to extract/
derive from the source material. For the team that mined 
web pages, the SME, in addition, provided the team with 
information goals and a workflow that he/she wanted built  
(see Figure 7).
Table 6 lists the infrastructure details of the 
implementation of the system.
Figure 8 shows the architecture of the overall DL 
system solution.
Through the UI, the SME will be able to search the 
three collections that are indexed in ElasticSearch, as well 
as request information goals, which will trigger workflow 
generation and execution via Apache Airflow. Apache 
Airflow will execute Docker containers in a dynamically 
generated sequence. Each container is a service that 
supports each task identified by the developers. Ceph is 
mounted on all of the containers so that Airflow can take 
the information processed from one service and pass it 
on to the next service. The inputs to the workflow and 
the outputs from the workflow executions are transacted 
via the UI. The curators can add and manage data 
collections through the UI as well. The developers can 
use a separate interface that will allow them to add and 
manage the services that they are building. In a planned 
implementation, there will be an interface for UX-Rs to 
explore the different Personas and their goals.
Figure 8. Architecture design of the implementation of the DL system by the CS5604 class. Note: ETDs, electronic theses and dissertations; 
NFS, Network File System; VM, virtual machine.
Table 6
Framework/Tools Used by Teams for Each Component of the DL
DL component Framework/tool
Workflow Management 
System
Apache Airflow
Service Docker Container
Services Registry Docker Container and Kubernetes 
Container Cluster
Knowledge Graph RDBMS-based representation of 
Graph
Reasoner Python-based service to generate 
workflows
Explorer Interface ReactiveSearch and NodeJs
Note: RDBMS, Relational Database Management System.

 How Should One Explore the Digital Library of the Future?   361
6  Evaluation
After building an instance of the DL, we need to evaluate 
whether the system solution facilitates exploration and 
to what extent. The design of the DL makes the system 
extensible to evolving user information needs. This 
extensibility is possible because the representation of 
workflows is modular. As a result, developers can build 
multiple solutions on top of the existing workflows. As 
more and more technological solutions are discovered, 
goals could be attained in a different (and possibly easier) 
manner. Our representation allows developers to define 
multiple paths to a goal. Any interface or visualizations 
can showcase all of the different ways in which the users 
can attain the goals and how they are connected. This 
interaction will facilitate the exploration of information 
and information relationships.
Additionally, the DL can be evaluated based on the 
“dimensions of quality” identified by authors who defined 
a “quality model” for DLs (Gonçalves, Moreira, Fox,  & 
Watson,  2007).
Figure 9 showcases the qualities to evaluate services. 
The DL that we have defined is a workflow-based DL; we 
define a workflow as a sequence of services. So, each 
dimension can be measured as a cumulative measure over 
each individual service performance.
One could conduct a user study, where prospective 
users discover information from the DL interface. From 
the study, we can assess the following:
i. the different user g oals that they query;
ii. the DL ’s list of recommended workflows (in response 
to the user query);
iii. the workflows selected by users; and
iv. the system’s performance in terms of efficiency 
and effectiveness of workflow execution and other 
dimensions shown above.
In this manner, we can learn precisely how the DL supports 
exploration.
7  Conclusion
This article presents a DL framework supporting 
exploration both for end users and for a society of other 
users, whose exploratory activities build and improve 
the system’s extensible functionality. We describe a 
methodology wherein UX-Rs, SMEs (including end users, 
curators, data scientists, DL researchers, and so on), 
and developers work together to build a set of workflow 
artifacts, such as workflow goals, workflow tasks, and 
services to support each task. The end  product is a DL 
with an interface that allows SMEs to find information 
without learning the data mining effort executed by the 
workflows required to produce it. This functionality is 
possible because of two essential DL components: (1) a 
reasoner; and (2) a knowledge graph-based goal–task–
workflow representation. The reasoner applies a goal-
directed search of the graph-based representation of 
the workflow artifacts produced from execution of the 
methodology and extracts relationships between various 
information and information states.
Through the methodology, we introduce the various 
new digital objects that are part of this framework. The 
exploratory activities of the UX-R, developer, and curator 
modify these digital objects. These exploratory activities 
Figure 9. DL services corresponding with “DL dimensions of quality with respective metrics,” as presented in Gonçalves, Moreira, Fox,  and 
Watson (2007).

362    Edward A. Fox, Prashant Chandrasekar
directly increase the range of explorations possible by 
SMEs.
We hope that future DL exploration takes into account 
the SMEs and other stakeholders who are extending the 
system solution. This approach can thus further increase 
the life and usefulness of DLs.
Acknowledgments: The authors thank the US National 
Science Foundation for its support through the grants IIS-
1619028, CMMI-1638207 , OAC-1835660, and IIP-1924726. We 
thank the Institute of Museum and Library Services for 
support through the grant LG-37 -19-0078-19. We also thank 
the student teams in CS5604 and CS4624 for their work.
References
Borgman, C. L., Bates, M. J., Cloonan, M. V., Efthimiadis, E. N., 
Gilliland-Swetland, A. J., Kafai, Y . B., … Maddox, A. B. (1996). 
Social aspects of libraries. Final report to the National Science 
Foundation. Retrieved from https:/ /escholarship.org/uc/
item/7tw0x377
Chomsky, N. (1956). Three models for the description of    language. 
IRE Transactions on Information Theory, 2 (3), 113–124. doi: 
10.1109/TIT.1956.1056813
Chomsky, N., & Lightfoot, D. W. (2002). Syntactic structures. Berlin, 
Germany: De Gruyter Mouton. doi: 10.1515/9783110218329
Ehrlinger, L., & Wöß, W. (2016). Towards a   definition of knowledge 
graphs. Retrieved from http:/ /ceur-ws.org/Vol-1695/paper4.pdf
Fox, E. A., Gonçalves, M. A., & Shen, R. (2012). Theoretical 
foundations for digital libraries: The 5S (societies, scenarios, 
spaces, structures, streams) approach: Synthesis lectures 
on information concepts, retrieval, and services.  San 
Rafael, California (USA): Morgan & Claypool Publishers. doi: 10. 
2200/S00434ED1V01Y201207ICR022
Fox, E. A., & Leidig, J. P . (2014). Digital   libraries applications: 
CBIR, education, social networks, eScience/simulation, and 
GIS: Synthesis lectures on information concepts, retrieval, 
and services. San Rafael, California (USA): Morgan & Claypool 
Publishers. doi: 10.2200/S00565ED1V01Y201401ICR032 
Fox, E. A., & Silva Torres, R. (2014). Digital library technologies:  
Complex objects, annotation, ontologies, classification, extraction, 
and security: Synthesis lectures on information concepts, retrieval, 
and services. San Rafael,  California  (USA): Morgan & Claypool 
Publishers. doi: 10.2200/S00566ED1V01Y201401ICR033
Gallo, G., Longo, G., Pallottino, S., & Nguyen, S.  (1993). Directed 
hypergraphs and applications. Discrete Applied Mathematics, 
42(2-3), 177–201.
Gonçalves, M. A., Moreira, B. L., Fox, E. A., & Watson, L. T. (2007). 
What is a good digital library?  A quality model for digital 
libraries. Information Processing & Management, 43 (5), 1416–
1437. doi: 10.1016/j.ipm. 2006.11.010. 
Hartson, R., Pyla, P . (2012). The UX book: Process and guidelines for 
ensuring a quality user experience.  San Francisco, CA, USA: 
Morgan Kaufmann Publishers Inc. 
Licklider, J. C. R. (1965). Libraries of the future. Cambridge, 
Massachusetts: MIT Press. 
Liew, C. S., Atkinson, M. P ., Galea, M., Ang, T. F., Martin, P ., & Hemert, 
J. (2016). Scientific workflows: Moving across paradigms. ACM 
Computing Surveys, 49(4). doi: 10. 1145/3012429
McKenzie, B. (1997). Generating strings at random from a context free   
grammar. Retrieved from http:/ /hdl.handle.net/10092/11231
Meno, E., & Vincent, K. (2020). Twitter-based   knowledge 
graph for researchers. Retrieved from http:/ /hdl.handle. 
net/10919/98239
Moreira, B. L., Goncalves, M. A., Laender, A. H. F., & Fox, E. A. (2009). 
Automatic evaluation of digital libraries with 5SQual. Journal of 
Informetrics, 3(2), 102–123. doi: 10.1016/j.joi.2008.12.003. 
Pomerantz, J., Oh, S., Yang, S., Fox, E. A., & Wildemuth, B. M.  (2006).  
The core: Digital library education in library and information 
science programs. D-Lib Magazine, 12(11). doi: 10.1045/
november2006-pomerantz. 
Pomerantz, J., Wildemuth, B. M., Yang, S., & Fox, E. A. (2006). 
Curriculum development for digital libraries. Proceedings of the 
6
th ACM/IEEE-CS Joint Conference on Digital Libraries (JCDL ’06), 
175–184. doi: 10.1145/1141753.1141787
Shen, R., Gonçalves, M. A., & Fox, E. A. (2013). Key issues regarding 
digital libraries: Evaluation and integration: Synthesis 
lectures on information concepts, retrieval, and services. 
San Rafael,  California  (USA): Morgan & Claypool Publishers.
doi:10.2200/S00474ED1V01Y201301ICR026
Shen, R., Vemuri, N. S., Fan, W.,   & Fox., E. A. (2006). What is a 
successful digital library? In J. Gonzalo, C. Thanos, M. F. Verdejo, 
& R. C. Carrasco (Eds.). Research and Advanced Technology for 
Digital Libraries (pp. 208–219).  Alicante, Spain: Springer. doi: 
1438. 1007/11863878_18
Ulwick, A. W. (2005). What customers want: Using outcome-driven 
innovation to create breakthrough products and services
.   New 
York, NY: McGraw-Hill Education.
Vemuri, N. S., Torres, R. D. S., Fox, E. A., Fan, W., & Shen, R.   (2006).  
Exploring digital libraries: Integrating browsing, searching, 
and visualization. Proceedings of the 6
th ACM/IEEE-CS 
Joint Conference on Digital Libraries (JCDL ’06),  1–10. doi: 
10.1145/1141753. 1141755
White, R. W., & Roth, R. A. (2009).  Exploratory search: Beyond the 
query-response paradigm: Synthesis lectures on information 
concepts, retrieval, and services. San Rafael,  California  (USA): 
Morgan & Claypool Publishers. doi: 10.2200/
S00174ED1V01Y200901ICR003
Wikipedia contributors (2020). Context-free grammar — Wikipedia, The   
free encyclopedia. Retrieved from https:/ /en.wikipedia.org/w/
index.php?title=Context-free_grammar&oldid=934576648
