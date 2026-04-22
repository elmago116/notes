---
title: "Evaluating AI-generated design solutions in a basic design studio - International Journal of Technology and Design Education"
source: "https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y"
authors: "[[Selen Çiçek]],[[Mine Özkar]]"
published: 2025-10-17
created: 2026-03-11
description: "The first-year studio in architecture programs plays a pivotal role in introducing novice designers to the complexities of design problems. Interpreting mu"
tags:
  - "tech/ai"
  - "design/evaluation"
DOI:
Type:
year:
---
Zotero automatically redirected your request to link.springer.com through the proxy at sire.ub.edu.[Don’t Proxy This Site](https://link-springer-com.sire.ub.edu/article/10.1007/) [Proxy Settings](https://link-springer-com.sire.ub.edu/article/10.1007/) [✕](https://link-springer-com.sire.ub.edu/article/10.1007/)

## Evaluating AI-generated design solutions in a basic design studio

- Published:
- (2025)
- [Cite this article](https://link-springer-com.sire.ub.edu/article/10.1007/#citeas)

Access provided by Consorci de Serveis Universitaris de Catalunya (CSUC)

[Save article](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/save-research?_csrf=7Z6fXyt_qc8rrLBG4FXRZps6h7mM5hL_)

[View saved research](https://link-springer-com.sire.ub.edu/saved-research)

 [![](https://media-springernature-com.sire.ub.edu/w72/springer-static/cover-hires/journal/10798?as=webp) International Journal of Technology and Design Education](https://link-springer-com.sire.ub.edu/journal/10798) [Aims and scope](https://link-springer-com.sire.ub.edu/journal/10798/aims-and-scope) [Submit manuscript](https://www.editorialmanager.com/itde/)

## Abstract

The first-year studio in architecture programs plays a pivotal role in introducing novice designers to the complexities of design problems. Interpreting multifaceted design briefs and generating viable solutions can be challenging for novice designers, given their lack of prior experience. This study seeks a method to enhance students’ understanding in a basic design studio. By creating synthetic design solutions to the given problem definitions in a sample set of assignments, it enlarges the solution space to include a variety of responses to a design brief. Using assignment briefs from two institutions, text-to-image diffusion models were employed to produce diverse solutions that preserved the semantic organization of each brief. After an initial generation, expert feedback was incorporated, refining prompts and producing a second set of synthetic solutions, which were then evaluated alongside a control group in semi-structured interviews with design experts. This evaluation focuses on whether the explicitness of problem definitions and expert feedback separately and together impact synthetic solution generation. Initial findings indicate that AI-generated solutions perform in correlation with the brief definition. Diffusion models can rapidly generate a wide range of design solutions to briefs, particularly in the early stages of assignments. However, without feedback, later-stage solution spaces tend to be filled with arbitrary visuals. With expert guidance, synthetic solution spaces have the potential to expose students to a broad spectrum of solutions, enabling them to better interpret design problems, grasp key concepts, and develop critical perspectives on their design processes. These findings offer valuable insights into the role of AI in interpreting design problems and generating solutions, emphasizing its potential to enhance the comprehension and exploration of design problems in early design education.

### Similar content being viewed by others

### Critical questions on the emergence of text-to-image artificial intelligence in architectural design pedagogy

Article 25 October 2024

### The Human Designer in Times of Artificial Intelligence: Diffusion-Driven Architectural Design Explorations

Chapter © 2026

### Beyond Generative A.I. to Reduce the Gap Between Architecture and Its Techniques

Chapter © 2025

## Introduction: first encounter with the design problems

Basic design is considered the foundation for all design disciplines in the first year of design studios (Aytaç Dural, [2002](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR2 "Aytaç Dural, T. (2002). Theatre-architecture-education: Theatre as a paradigm for introductory architectural design education. Middle East Technical University Faculty of Architecture Press."); Besgen et al., [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR6 "Besgen, A., Kuloglu, N., & Fathalizadehalemdari, S. (2015). Teaching/learning strategies through art: Art and basic design education. Procedia-Social and Behavioral Sciences, 182, 428–432. 
https://doi-org.sire.ub.edu/10.1016/j.sbspro.2015.04.813
")). The studio is commonly referred to as the foundational design studio, preliminary design studio, or basic design studio. Regardless of its name, the critical role of the studio remains the same: teaching novice designers the concept of design reasoning implicitly (Akin, [1990](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR1 "Akin, Ö. (1990). Computational design instruction: Toward a pedagogy. In The electronic design studio: Architectural knowledge and Media in the Computer era [CAAD futures ‘89 conference proceedings / ISBN 0-262-13254-0] (pp. 302–316). MIT Press.")). Despite its critical role, the students often have difficulty fully comprehending the significance of the studio.

The struggle for students begins as they encounter the definitions of design problems for the first time. Typically, novice design students have previously dealt only with well-defined problems -structured with a singular goal, demanding a single, absolute truth or one-way valid answer. Having been used to derive instant solutions through pre-established methods and formulas in primary and secondary education, students are unaccustomed to questioning the nature of given problems or developing methodologies to address them (Saranlı, [1998](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR44 "Saranlı, T. (1998). Başlangıçtan bugüne temel tasarım. In N. Teymur & T. Aytaç Dural (Eds.), Temel Tasarım / Temel Eğitim. ODTÜ Mimarlık Fakültesi Yayınları.")).

Design problem definitions rarely lend themselves to solutions through pre-defined, straightforward, and simple methodologies. In most cases, each unique design problem necessitates a student’s interpretation, leading to its reconstruction for a full understanding of its inherent goals. Consequently, the initial encounter with the ill-defined or wicked nature of design problems can be overwhelming for novice students (Casakin, [2002](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR10 "Casakin, H. (2002). Well-defined versus ill-defined design problem solving: The use of visual analogy. In D. Durling & J. Shackleton (Eds.), Common ground - DRS international conference 2002, 5-7 September. 
https://doi-org.sire.ub.edu/10.21606/drs.2002.6
"); Dorst, [2005](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR17 "Dorst, K. (2005). Studying Design Problems. In H. Achten, K. Dorst, P. J. Stappers, & B. de Vries (Eds.), Design research in the Netherlands 2005 – Proceedings. Technische Universiteit Eindhoven, Faculteit Bouwkunde.")), given their lack of training to provide answers in contexts where the problem itself is not explicitly structured. Therefore, the students in a basic design studio generally do not have a clear insight about how to approach it to solve the problem, nor can they see what the actual problem of the given task is. Establishing an explicit conceptual framework about the nature of given problems could prove beneficial in introducing students to the inherent ambiguities of the design process, encompassing the crucial aspect of problem reconstruction (van Dooren, [2020](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR52 "van Dooren, E. (2020). Making the design process in design education explicit: Two exploratory case studies. Design and Technology Education: An International Journal, 25(1), 13–34 
https://doi-org.sire.ub.edu/10.24377/DTEIJ.article1273
")).

A basic design studio can provide a ground for collective reasoning by enabling various interactions among the actors of the studio. Within the hermeneutical framework of a conventional design studio, the two essential actors are the students and instructors. These actors interact with each other in one-to-one (student-instructor) sessions, class discussions, and juries (students-instructors-students). Students also converse and collaborate among themselves (student-student), by studio culture, during individual solution-generation processes attempting to help each other by explicating the ambiguities of the given problems and tasks among themselves (Park, [2020](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR41 "Park, S. (2020). Rethinking design studios as an integrative multi-layered collaboration environment. Journal of Urban Design, 25(4), 523–550. 
https://doi-org.sire.ub.edu/10.1080/13574809.2020.1734449
")).

With the emergence of generative AI, its involvement in the studio as another actor seems inevitable. However, it is essential to critically define the role and scope of these tools in pedagogical settings. Without clear integration strategies, students may perceive AI as a shortcut to developing design solutions, bypassing the experiential and reflective dimensions of learning-by-doing. Instead, this research positions AI as an actor which extends the capacities of design studios by fostering collaborative reasoning among students, instructors.

The introduction of generative AI to the design studio ecosystem presents a complex dynamic. It is unlike a diverse cohort of students generating myriad solutions to design challenges. Unlike human designers, AI lacks the capacity to discern the appropriateness or validity of its outputs. This underscores the need for instructors to play a pivotal role in guiding students through the process of critically evaluating and refining these AI-generated solutions. By leveraging their expertise, instructors can help students navigate the abundance of design possibilities, fostering a critical dialogue that bridges human intuition with machine-generated creativity. Establishing a collaborative framework where students, educators, and AI agents engage in iterative critique and discussion allows for the integration of collective intelligence, facilitating innovative and meaningful design outcomes. Through this interaction, AI can serve not as a mere shortcut, but as a complementary tool that enhances students’ comprehension, creativity, and problem-solving capabilities, ultimately expanding their engagement with the design process.

Despite the rapid advancement of AI technologies, there is a notable lack of comprehensive research on the integration of AI tools within design education, particularly in early design studios. Most existing studies focus on AI’s technical capacities rather than exploring its pedagogical implications or how it can be effectively integrated to enhance students’ interpretative skills when engaging with ambiguous design briefs.

In this context, this paper reconsiders the gap in understanding and elucidating the various definitions of design problems and seeks a method to enhancee students’ understanding of ill-defined design problems in the context of the basic design studio, through reconceptualizing *design space*. It is hypothesized that offering a *design space* generation mechanism using AI-aided tools may help elucidate the ambiguous problem definitions that are not clearly stated in given assignment briefs.

To evaluate the impact of problem definitions on the design solutions, the proposed methodology draws a comparative framework by analyzing the assignment brief data of two renowned design intuitions that constitute the two problem spaces of the study. To analyze and assess the visual impacts of these problem spaces on the generated solutions, a series of synthetic solution spaces are generated through AI models.

In the realm of generative design, many studies focus on creating solution spaces using various computational algorithms as teaching aids for early design education (Chase, [2003](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR11 "Chase, S. C. (2003). Revisiting the use of generative design tools in the early stages of design education. In In proceedings of the 21st international conference on education and research in computer aided architectural Design in Europe. 
https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2003.465
")). Rule-based systems, such as shape grammars, prove effective in generating intricate forms and patterns from a simple set of rules defined by explicit constraints, making them suitable for educational design studio setups (Economou, [2001](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR19 "Economou, A. (2001). Shape grammars in architectural design studio. In Proceedings of the 2000 ACSA technology conference: The intersection of design and technology. MIT."); Knight, [1999](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR37 "Knight, T. (1999). Applications in architectural design and education and practice. Report for the NSF/MIT workshop on shape computation.")). However, the applicability of these rule-based systems in basic design studios is constrained when the design brief lacks explicit rules or objectives. These systems often confine designers to a single visual domain, posing a challenge for first-year design students in translating written design problems into a visual medium through interpretation.

As discussed in section “ [AI agents in design education](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec3) ” in detail, the potential implementation of AI-aided tools emerges as promising for novice designers. Machine learning models (ML) generate novel solutions by analyzing and synthesizing hidden patterns in provided data across multiple domains, without requiring a specific structure of rules or algorithms. Unlike prior generative design algorithms, it becomes feasible to generate solutions that address design problems not explicitly defined. Thus, to generate synthetic solution spaces based on design problems stated in assignment briefs, a text-to-image AI model was employed.

As presented in section “ [Image generative AI models](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec4) ”, in the current state of the art, Diffusion Models (DM) distinguish themselves from other generative AI models for their ability to produce high-quality image samples in a multi-modal working environment (Dhariwal & Nichol, [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR16 "Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. Advances in Neural Information Processing Systems, 34, 8780–8794.")). DM can be implemented in various contexts and tasks to generate images closely aligned with complex and nuanced text descriptions. The selection of the text-to-image DM model for the scope of the study is due to the need to generate solutions by using complex and nuanced descriptions of the briefs as text prompts. The architecture of the natural language processing (NLP)-based text-to-image diffusion model was deemed suitable for the generation process of solutions, aligning with the assignment-based, learning-by-doing educational model of the basic design studio.

Section “ [Methodology & experiment overview](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec5) ” outlines the methodology to generate a series of synthetic solution spaces by the DM, that correspond to the two problem spaces. It involves generating solution spaces through the direct translation of the assignment brief into text prompts or revised text prompts via the implemented feedback mechanism.

As presented with the case in section “ [Case study & results](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec6) ”, the assignment briefs taken from first-year design studio archives are translated into text prompts while preserving semantic organization, for the generation of the first sets of solution spaces. These solution spaces undergo evaluation by design experts, resembling a critique session in the studio. Feedback obtained from these sessions is then utilized to revise the text prompts, forming the basis for generating the secondary solution spaces.

To provide a comprehensive basis for the discussion in section “ [Implications of synthetic solutions on the design space of the basic design studio](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec15) ”, we evaluate the performance of synthetic solution spaces through design experts interviews by two comparative frameworks: Firstly, the performances of the solutions of two problem spaces collected from the assignment briefs of two different institutions are compared, to elucidate the impact of the explicitness of the problem definitions. Secondly, the solution spaces generated by the solo guidance of the assignment brief and the secondary ones that are supplemented by the feedback sessions are examined, to enlighten the impact of the feedback procedure on the performance of the generated solutions.

Building on the findings from the synthetic solution space generation and expert assessments, section “ [Discussion: synthetic design space generation process](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Sec18) ” explores the potential implications of incorporating text-to-image AI tools into early design education. This section reflects on the role of feedback in enhancing AI-generated solution spaces, highlights challenges associated with current model limitations, and discusses potential strategies for integrating AI tools to support student comprehension of complex, ambiguous design problems. It considers how these tools might complement traditional studio practices by expanding students’ design exploration and providing an innovative assessment resource for instructors.

### Reframing the concept of design space in the basic design studio

As this study aims to integrate AI tools for generating *design space* for a basic design studio, it is important to reframe the concept theoretically with its inherent subsets as problem and solution spaces. Computational design research suggests that the cognitive limits of the human designer using computational tools have been extended in terms of increased memory capacity and process speed. Through algorithmic processes controlled with parameters in constrained contexts, it becomes possible to generate a myriad of alternative solutions to a given challenge. Such multiplicity is often referred to as the design space.

Yet, design space often carries imprecise metaphors and unspoken assumptions that take several different forms in the design research field (Halskov & Lundqvist, [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR31 "Halskov, K., & Lundqvist, C. (2021). Filtering and informing the design space: Towards design-space thinking. Acm Transactions on Computer-Human Interaction. 
https://doi-org.sire.ub.edu/10.1145/3434462
")). While it is traditionally defined as “the aggregation of all possible design solutions in a given task,” it is also understood as the changing set of potentialities shaped by the designer during the act of designing (Goldschmidt, [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR25 "Goldschmidt, G. (2015). The pagoda design space: Extending the scope of design. In T. Taura (Ed.), Principia Designae -Pre-Design, Design, and PostDesign. Springer. 
https://doi-org.sire.ub.edu/10.1007/978-4-431-54403-6_5
"); Kan & Gero, [2018](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR34 "Kan, J. W. T., & Gero, J. S. (2018). Characterizing innovative processes in design spaces through measuring the information entropy of empirical data from protocol studies. Artificial Intelligence for Engineering Design, Analysis and Manufacturing, 32(1), 32–43. 
https://doi-org.sire.ub.edu/10.1017/S0890060416000548
")). Woodbury and Burrow ([2006](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR56 "Woodbury, R. F., & Burrow, A. L. (2006). Whither design space? Artificial Intelligence For Engineering Design, Analysis And Manufacturing, 20(2), 63–82. 
https://doi-org.sire.ub.edu/10.1017/S0890060406060057
")) further define it as a network of related design structures visited during exploration, while other scholars describe it as a descriptive metaphor for collections of design ideas (Halskov et al., [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR32 "Halskov, K., Dove, G., & Fischel, A. (2021). Constructing a design space from a collection of design examples. She Ji: The Journal of Design, Economics, and Innovation, 7(3), 462–484. 
https://doi-org.sire.ub.edu/10.1016/j.sheji.2021.07.001
")).

Krıshnamurtı ([2006](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR38 "Krıshnamurtı, R. (2006). Explicit design space? Artificial Intelligence for Engineering Design, Analysis and Manufacturing, 20(2), 95–103. 
https://doi-org.sire.ub.edu/10.1017/S0890060406060082
")) defines the design space as a combination of the problem and solution spaces. The *problem space* refers to the conceptual domain in which the design problem is defined, including its goals, constraints, and initial conditions, while the *solution space* encompasses the range of possible design responses or alternatives that can be generated in relation to that problem. The inclusion of problem space in the design space definition, relates to the nature of the design problems themselves, and whether they are ill-defined or well-defined, a distinction that plays a decisive role in shaping the openness or closedness of the design space. The first understanding takes the design problems as primary examples of the ill-defined or ill-structured ones; in terms of their initial, goal, and intermediate states are being specified incompletely (Reed, [2015](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR43 "Reed, S. K. (2015). The structure of ill-structured (and well-structured) problems revisited. Educational Psychology Review, 28(4), 691–716. 
https://doi-org.sire.ub.edu/10.1007/s10648-015-9343-1
"); Simon, [1975](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR48 "Simon, H. A. (1975). The functional equivalence of problem-solving skills. Cognitive Psychology, 7, 268–288.")). The solutions generated in response to such problems bear no direct relation to precedent solution cases, as the algorithms or procedures to solve them are not fully identified or codified (Casakin, [2002](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR10 "Casakin, H. (2002). Well-defined versus ill-defined design problem solving: The use of visual analogy. In D. Durling & J. Shackleton (Eds.), Common ground - DRS international conference 2002, 5-7 September. 
https://doi-org.sire.ub.edu/10.21606/drs.2002.6
")). Each attempt at a solution therefore generates unexplored alternatives, a condition directly linked to design creativity (Goldschmidt & Weil, [1998](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR26 "Goldschmidt, G., & Weil, M. (1998). Contents and structure in design reasoning. Design Issues, 14(3), 85–100. 
https://doi-org.sire.ub.edu/10.2307/1511899
")). In contrast, well-defined problems provide clear goals and explicit conditions, identifying the necessary information and resources in advance, and thereby reducing ambiguity in the solution process (Lloyd & Scott, [1994](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR39 "Lloyd, P., & Scott, P. (1994). Discovering the design problem. Design Studies, 15(2), 125–140. 
https://doi-org.sire.ub.edu/10.1016/0142-694X(94)90020-5
")).

This distinction between ill-defined and well-defined problems aligns closely with the notion of openness of the design space. However, this openness should not be treated as binary opposites but rather as a fluid continuum shaped by both problem characteristics and the interpretive capabilities of the designer. Even when problem definitions seem fixed, their inherent ambiguity allows for varying degrees of reinterpretation and reformulation. Each act of framing a problem contributes to the co-evolution of the problem and solution spaces and, by extension, the broader design space. Ill-defined problems have potential open up the design space by introducing multiple interpretive pathways. Additionaly, the designer’s prior knowledge and design reasoning ability is also factors that might expand the design space. As Simon ([1957](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR47 "Simon, H. A. (1957). Models of man: Social and rational. John Wiley and Sons.")) has argued through the notion of bounded rationality, a designer’s decision-making process is always constrained by their cognitive and contextual limitations.

In this sense, the ambiguity embedded in design problems not only opens up the problem space but also sets the ground for the continuous expansion of the design space as a whole. This perspective creates a natural link to the basic design studio, which itself can be conceptualized as a dynamic and evolving design space. Within this context, the given design briefs as in form of assignments constitute the problem space, framing the conditions, boundaries, or conceptual challenges that guide exploration. In response, the students’ proposals and design attempts form the evolving solution space. The interplay of these two domains does not remain static but unfolds in a dynamic and iterative manner during the studio process.

As illustrated in the proposed hermeneutic cycle of a basic design studio in Fig. [1](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig1), the design space of a studio evolves through continuous organic reflective action between novice designers and instructors, as well as through the shifting interactions between the problem and solution subspaces. These subspaces continuously overlap through the reflective practices of students and instructors upon the design medium, further shaped by critiques. In this cycle, openness and closedness are not static states but dynamic qualities that shift as problems are interpreted, redefined, and addressed through iterative solution attempts. Students’ tacit knowledge at the outset transforms into contextual understanding as they increasingly internalize design vocabulary and frameworks, fostered by the pedagogical strategies employed in the studio.

![Fig. 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig1_HTML.png?as=webp)

**Fig. 1**

In basic design studio contexts, the design briefs commonly contain both explicit parameters—such as visual attributes like color, size, number of elements, material type, or texture—which can be associated with well-defined problem elements, as well as more abstract or conceptual formulations that evoke ill-defined problem characteristics. Rather than determining openness or closedness in an absolute manner, these mixed formulations contribute to varying degrees of interpretive latitude within the hermeneutical cycle. It is in this iterative interpretive process that the design space expands, adapting to the evolving cognitive engagement of the designer. However, the impact of the problem definitions in this organic process of the studio remains ambiguous in terms of ill-defined and well-defined ones.

Thus, while measuring the ambiguity of design problems into duality of extremes may be reductive, it is necessary to draw a clear framework for the research that focuses on identifying the impact of the design problems stated in the assignment briefs on the synthetic solutions. Therefore, the two-fold problem definitions inherited in the assignment briefs were reframed in the context of the problem spaces of the basic design studio as follows:

- *Well-Defined Problems:* The statements that explicitly indicate the properties of the design elements and the visual field i.e., color, size, number of elements, material type, texture, etc.
- *Ill-Defined Problems:* The statements define abstract concepts and notions, which could challenge novice designers to fully understand the requirements of the solution process.

These problem identifications are further used to discuss the implications of two types of problems stated in the briefs on the performance evaluations of AI-generated synthetic solutions.

### AI agents in design education

The exploration of Artificial Intelligence (AI) as computational means to emulate natural intelligence formally began in the 1950 s and accelerated in recent years, driven by intense competition (Smuha, [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR49 "Smuha, N. A. (2021). From a ‘race to AI’ to a ‘race to AI regulation’: Regulatory competition for artificial intelligence. Law, Innovation, and Technology, 13(1), 57–84. 
https://doi-org.sire.ub.edu/10.1080/17579961.2021.1898300
")). As a result, AI-driven tools are now widely accessible, assisting with various tasks across domains. However, the classification of these tools as genuinely “intelligent” remains contentious, largely due to limitations in their knowledge bases and reasoning abilities (Boden, [1990](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR7 "Boden, M. A. (Ed.). (1990). The philosophy of artificial intelligence. Oxford University Press."); Dreyfus, [1992](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR18 "Dreyfus, H. L. (1992). What Computers Still Can’t Do. MIT Press.")). These limitations bear particular significance in design education, where AI’s capacity to act as a creative collaborator or educational aide is continually scrutinized.

The integration of AI in design thinking and its role within design processes presents both theoretical and practical challenges. As AI’s generative capabilities advance, ethical considerations surrounding its use in creative fields have intensified, with ongoing debates in both academic and professional spheres (Stark & Crawford, [2019](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR51 "Stark, L., & Crawford, K. (2019). The work of art in the age of artificial intelligence: What artists can teach us about the ethics of data practice. Surveillance & Society, 17(3/4), 442–455. 
https://doi-org.sire.ub.edu/10.24908/ss.v17i3/4.10821
")). This issue is especially pertinent in design education, where students often bring AI tools into their workflows independently, necessitating careful consideration of AI’s pedagogical, ethical, and creative dimensions (Flechtner & Stankowski, [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR24 "Flechtner, R., & Stankowski, A. (2023). AI is not a wildcard: Challenges for integrating AI into the design curriculum. In Proceedings of the 5th annual symposium on HCI education (pp. 72–77). 
https://doi-org.sire.ub.edu/10.1145/3587399.3587410
")). With advancements in the field, researchers stress the importance of establishing frameworks that encourage responsible AI integration.

Although the number of studies are limited particularly on the integration of AI in the context of early design education, the literature on AI in design education setups is evolving. The advent of Large Language Models (LLMs) and multi-modal Diffusion Models (DMs) has further propelled research at the intersection of AI and design education, resulting in a notable increase in relevant publications. This surge is evident by the growing number of papers from 2014 to 2024 in Web of Science (WOS) and CuminCAD databases searched through the keywords such as “design studio”, “design education”, “architectural design education”; and “AI”, “Artificial Intelligence”, “Machine Learning”, “Deep Learning”. These investigations discuss diverse aspects of the integration in terms of, inspecting the perception of students and educators towards AI in the design realm; exploring the creativity in the design process leveraged by the generative power of AI; or questioning the tutoring and assessing abilities of AI in the design processes.

One critical area of exploration centers on how students and educators perceive AI within design processes. Recent studies have explored this dimension, revealing both enthusiasm and caution. Sciannamè ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR46 "Sciannamè, M. (2023). Machine learning (for) design: towards designerly ways to translate ML for design education. 
https://doi-org.sire.ub.edu/10.13140/RG.2.2.27065.34405
")) emphasizes the importance of aligning machine learning concepts with design values through workshops, helping students navigate complex AI tools by fostering a clearer understanding. Wang et al. ([2024](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR54 "Wang, Y., Zhao, Y., Tian, X., Yang, J., & Luo, S. (2024). The influence of subjective knowledge, technophobia and perceived enjoyment on design students’ intention to use artificial intelligence design tools. International Journal of Technology and Design Education. 
https://doi-org.sire.ub.edu/10.1007/s10798-024-09897-3
")) analyze factors such as technophobia, enjoyment, and subjective knowledge that influence students’ intentions to use AI, underscoring the impact of affective and social factors on their acceptance of these technologies. While some studies, like Cao et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR9 "Cao, Y., Aziz, A. A., & Arshard, W. N. R. M. (2023). University students’ perspectives on artificial intelligence: a survey of attitudes and awareness among interior architecture students. Internatıonal Journal of Educatıonal Research And Innovatıon. 
https://doi-org.sire.ub.edu/10.46661/ijeri.8429
")), found that students are generally open to AI integration, they also noted persistent concerns about job security, reflecting broader societal anxieties about automation and its implications for future employment. Bartlett and Camba ([2024](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR4 "Bartlett, K. A., & Camba, J. D. (2024). Generative artificial intelligence in product design education: Navigating concerns of originality and ethics. International Journal of Interactive Multimedia and Artificial Intelligence, 8, 55–64. 
https://doi-org.sire.ub.edu/10.9781/ijimai.2024.02.006
")) explored how AI can enhance creativity, but they also raised ethical concerns, cautioning against over-reliance that could potentially impede creativity in high-performing teams. Figoli et al. ([2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR23 "Figoli, F., Rampino, L., & Mattioli, F. (2022). AI in the design process: Training the human-ai collaboration. 
https://doi-org.sire.ub.edu/10.35199/epde.2022.61
")) note that hands-on workshops significantly altered perceptions of human-AI collaboration, suggesting that structured engagement can foster more positive attitudes toward AI integration. These findings support the notion that structured engagements with AI can positively shape attitudes toward its integration in design education.

Alongside student perceptions, researchers have underscored the importance of foundational AI literacy for designers. For instance, Basarir ([2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR5 "Basarir, L. (2022). Modelling AI in architectural education. Gazı Unıversıty Journal of Scıence, 35, 1260–1278. 
https://doi-org.sire.ub.edu/10.35378/gujs.967981
")) and Sorguç et al. ([2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR50 "Sorguç, A., Kruşa Yemişçioğlu, M., & Yetkin, O. (2022). Demystifying machine learning for architecture students. Eskişehir Technical University Journal of Science and Technology A - Applied Sciences and Engineering, 23, 60–67. 
https://doi-org.sire.ub.edu/10.18038/estubtda.1169816
")) designed courses to develop graduate students’ understanding of data literacy, pattern recognition, and machine learning fundamentals. Their findings reinforce the value of grounding students in AI’s capabilities and limitations to promote responsible usage in design settings.

Another focal point in the literature is the AI’s role in enhancing ideation and alleviating cognitive load for students. For example, Kim ([2024](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR36 "Kim, S. J. (2024). Generative artificial intelligence in collaborative ideation: Educational insight from fashion students. Ieee Access, 12, 49261–49274. 
https://doi-org.sire.ub.edu/10.1109/ACCESS.2024.3382194
")) showcase AI’s role in collaborative ideation within fashion design, where it supports creativity without overshadowing human input, promoting a harmonious co-creative process. Similarly, Cudzik et al. ([2024](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR15 "Cudzik, J., Nyka, L., & Szczepański, J. (2024). Artificial intelligence in architectural education-Green campus development research. Global Journal of Engineering Education, 26(1), 20–25.")) demonstrate the application of an open-sourced text-to-image DM in projects, illustrating how AI facilitates rapid visual material generation, which in turn enables students to iterate more freely and creatively. Studies like those by Fareed et al. ([2024](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR21 "Fareed, M. W., Nassif, A. B., & Nofal, E. (2024). Exploring the potentials of artificial intelligence image generators for educating the history of architecture. Heritage, 7(3), 1727–1753. 
https://doi-org.sire.ub.edu/10.3390/heritage7030081
")) and Hsiao & Zhang ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR33 "Hsiao, M.-Y., & Zhang, S. (2023). Research on the educational application of generative artificial intelligence images in the design of semiotics learning models. In In proceedings of the 8th international conference on educational technology (pp. 8–15). 
https://doi-org.sire.ub.edu/10.1145/3637907.3637947
")) further expand on this concept by integrating text-to-image models into design education. In a similar vein, Zhou et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR58 "Zhou, C., Zhang, X., & Yu, C. (2023). How does AI promote design iteration? The optimal time to integrate AI into the design process. Journal Of Engineering Design. 
https://doi-org.sire.ub.edu/10.1080/09544828.2023.2290915
")) and Chiou et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR13 "Chiou, L.-Y., Hung, P.-K., Liang, R.-H., & Wang, C.-T. (2023). Designing with AI: An exploration of co-ideation with image generators. In In proceedings of the 2023 ACM designing interactive systems conference. DIS ‘23: Designing interactive systems conference. ACM. 
https://doi-org.sire.ub.edu/10.1145/3563657.3596001
")) explore how the timing of AI integration affects design iteration, concluding that well-timed AI support can streamline the exploration of visual concepts and promote broader design thinking. Building on the idea of creative support, Bank Stigsen et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR3 "Bank Stigsen, M., Moisi, A., Rasoulzadeh, S., Schinegger, K., & Rutzinger, S. (2023). AI diffusion as design vocabulary - investigating the use of AI image generation in early architectural design and education. In eCAADe proceedings (Vol. 2, pp. 587–596). eCAADe 2023: Digital design reconsidered. eCAADe. 
https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2023.2.587
")) and Kavakoglu et al. ([2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR35 "Kavakoglu, A. A., Almac, B., Eser, B., & Alacam, S. (2022). AI driven creativity in early design education - a pedagogical approach in the age of industry 5.0. In 40st eCAADe Proceedings. 
https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2022.1.133
")) highlight how AI tools could help students navigate design problems by offering diverse visual references. These findings suggest that AI can act as a catalyst for creative exploration, allowing students to explore and refine their ideas more efficiently.

While previous research has examined AI’s generative power, other studies position AI as an instructional aide within design education. Granero and Piegari ([2020](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR30 "Granero, A. E., & Piegari, R. G. (2020). How does AI affect higher design education? An investigation to open the debate. In Blucher design proceedings (pp. 683–688). Congreso SIGraDi 2020. Editora blucher. 
https://doi-org.sire.ub.edu/10.5151/sigradi2020-94
")) explore the use of AI as a tutor, highlighting its ability to guide creativity and offer advanced, formative feedback. This aligns with the findings of Farshad et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR22 "Farshad, S., Zorin, E., Amangeldiuly, N., & Fortin, C. (2023). Engagement assessment in project-based education: A machine learning approach in team chat analysis. Education and Information Technologies, 29, 13105–13131. 
https://doi-org.sire.ub.edu/10.1007/s10639-023-12381-5
")), who utilize machine learning to measure engagement and collaboration in project-based learning, suggesting that AI can automate and scale assessment without sacrificing quality. Conceição et al. ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR14 "Conceição, S. M., Diehl, N. C., & Bruscato, L. M. (2023). ChatGPT for briefing creation. SIGraDi 2023 | accelerated landscapes. 
https://doi-org.sire.ub.edu/10.5151/sigradi2023-435
")) demonstrate LLM’s utility in generating design briefs, which could assist in administrative tasks, although they note the necessity of oversight to ensure the accuracy and relevance of the outputs. Finally, Zhao & Gao ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR57 "Zhao, Y., & Gao, L. (2023). Classroom design and application of art design education based on artificial intelligence. International Journal of Information Technology and Web Engineering. 
https://doi-org.sire.ub.edu/10.4018/IJITWE.334008
")) explore the broader application of smart classroom systems, which highlighted how AI could enhance interactivity and engagement, indirectly improving the quality of art and design education by fostering a more interactive and adaptive learning environment.

Beyond aiding in the generation of creative solutions, AI has also been employed to improve assessment practices in design education settings. Chaudhuri & Dhar ([2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR12 "Chaudhuri, N. B., & Dhar, D. (2023). Designing deep-network based novelty assessment model in design education. Applied Soft Computing. 
https://doi-org.sire.ub.edu/10.1016/j.asoc.2022.109966
")) developed a Novelty Assessment Model (NAM) that evaluates creativity, addressing the issue of subjectivity in design evaluations by providing consistent, scalable assessments. Similarly, Ertürk & Üzümcü ([2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR20 "Ertürk, M.,Üzümcü, N. E. (2022). Görsel iletişim tasarım eğitiminin değerlendirme süreçlerinde üçüncü göz: bir yapay zekâ modeli. Sanat ve Tasarım Dergisi, 12(1), 191–202. 
https://doi-org.sire.ub.edu/10.20488/sanattasarim.1133850
")) applied AI to infer aesthetics in visual communication design, showing that machine learning models could offer unbiased, consistent evaluations. These approaches suggest that AI can help streamline feedback and improve the quality of assessments, especially in educational contexts where individualized feedback is challenging to scale.

Building on these insights, this research contributes a distinct perspective by concentrating on the foundational level of design education—specifically, the basic design studio, where the challenges of “ill-defined” design problems with inherent ambiguities are particularly pronounced. Rather than engaging directly with students, this study evaluates the performance of AI-generated solution spaces across two comparative frameworks: first, by examining how AI interprets and responds to varying levels of ambiguity within two distinct problem spaces; and second, by comparing solution spaces generated under different conditions—one guided solely by the original definitions of the design brief, and another enhanced with design expert feedbacks to clarify the briefs. This comparative analysis reveals AI’s capacity to interpret and address complex design problems through diverse criteria, providing insights into how AI might support the traditional setup of basic design studios.

By generating synthetic solution spaces that visualize the ambiguities of design briefs, this study positions AI as a potential co-creative agent that can introduce structured problem-solving to inherently unstructured design tasks, offering a complementary pathway for design education to support novice designers as they engage with challenging, ambigous design problems.

### Image generative AI models

Following the literature overview on AI’s potential in design education, this section introduces the foundational principles of deep learning to establish a basis for understanding key generative AI models. By outlining the distinctive strengths of previous generative AI models, this section highlights why Diffusion Models (DMs), with their capacity to convert textual prompts into rich visual outputs, are particularly suited to interpreting complex design briefs and generating synthetic design spaces that aid in tackling ill-defined problems.

Deep learning constitutes a specialized branch within machine learning, characterized by Artificial Neural Networks (ANN) featuring multiple layers (Goodfellow et al., [2016](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR28 "Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. The MIT Press.")). These algorithms are engineered to autonomously acquire hierarchical representations of data, proving effective across diverse applications including image and speech recognition, natural language processing, and generative modeling. Rooted in the architecture of ANNs, concepts within Deep Neural Networks (DNNs) are deemed “deep” due to the presence of numerous hidden layers situated between input and output layers, colloquially referred to as the latent space (Goodfellow et al., [2014](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR29 "Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). Generative Adversarial Networks (Version 1). arXiv. 
https://doi-org.sire.ub.edu/10.48550/ARXIV.1406.2661
")). Within this wide framework, DM and Generative Adversarial Network (GAN) models are heralded for their superior performance in image generation compared to other deep learning algorithms.

GAN algorithms, in particular, stand as pioneers in the realm of image-generative machine learning models, characterized by their dual DNN structures comprising discriminator and generator blocks, which interact dynamically (Brock et al., [2018](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR8 "Brock, A., Donahue, J., & Simonyan, K. (2018). Large Scale GAN Training for High Fidelity Natural Image Synthesis (Version 2). arXiv. 
https://doi-org.sire.ub.edu/10.48550/ARXIV.1809.11096
")). However in the current state DMs, distinguish themselves from other image-generative deep learning algorithms by their ability to generate high-quality image samples within a multi-modal operational framework (Dhariwal & Nichol, [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR16 "Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. Advances in Neural Information Processing Systems, 34, 8780–8794.")). The computational architecture of DMs bears a resemblance to that of GAN models, sharing a common foundation in the form of inherent DNN structures. However, the primary distinctions lie in the type of provided data and the generation process. While image-to-image GAN models operate by taking visual data as input and generating outputs through the transformation of information between discriminator and generator blocks (distinguishing between “real” and “fake”), diffusion models adopt a different approach. In the case of text-to-image DMs, they process textual inputs by subjecting them to a defined Markov chain of diffusion steps, gradually introducing random noise to the data and subsequently constructing desired data samples from this noise (Weng, [2021](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR55 "Weng, L. (2021). What are diffusion models? Lilianweng. Github. Io. Retrieved from 
https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
")).

In the current state of the field, there exists a prevailing consensus regarding the advantages of text-to-image DMs over other image-generative deep learning models across three key dimensions:

1. 1.
	Data Availability: Textual data sources typically offer a larger pool of image-related information compared to corresponding image datasets. While other models often rely on specific datasets sourced from diverse origins, text-to-image diffusion models are speculated to leverage the expansiveness of the world wide web, affording access to a broader array of data within controlled environment frameworks. However, the data sources (image repositories) that are used to train these models are generally not shared with the public, causing ethical dilemmas in artistic communities in terms of authenticity and copyright issues.
2. 2.
	Semantic Representations: Textual descriptions inherently furnish more explicit and detailed information about desired image outputs across various contexts. Consequently, generating images that align with specified criteria is facilitated, given the richness of information provided by textual prompts.
3. 3.
	Attention Mechanism: Text-to-image models can be engineered to integrate an attention mechanism, directing focus to specific segments of the input text during image generation. This affords finer control over the generated images, enabling the assignment of “weight” to text and image prompts within diffusion model interfaces.

Text-to-image DMs represent a subset of generative models that leverage natural language descriptions to produce images, integrating methodologies from both Natural Language Processing (NLP) and computer vision (Cao et al., [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR9 "Cao, Y., Aziz, A. A., & Arshard, W. N. R. M. (2023). University students’ perspectives on artificial intelligence: a survey of attitudes and awareness among interior architecture students. Internatıonal Journal of Educatıonal Research And Innovatıon. 
https://doi-org.sire.ub.edu/10.46661/ijeri.8429
")). The foundational architecture of text-to-image DM models can be delineated into two primary components: Text Encoding, which encompasses the incorporation of NLP techniques, and Image Generation, facilitated through the diffusion process (Fig. [2](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig2)). At a macroscopic level, text-to-image diffusion models commence by encoding the input text description into a latent representation utilizing an NLP model. With the advent of the transformer, network architecture marked a significant advancement in the field, particularly in handling lengthy text sequences. The Transformer model comprises an encoder and a decoder, both composed of a stack of identical layers. Each layer comprises two sub-layers: a self-attention mechanism and a feed-forward neural network (Vaswani et al., [2017](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR53 "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. 
https://doi-org.sire.ub.edu/10.48550/arXiv.1706.03762
") ).

![Fig. 2](https://media-springernature-com.sire.ub.edu/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig2_HTML.png)

**Fig. 2**

As highlighted by Vaswani et al. ([2017](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR53 "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. 
https://doi-org.sire.ub.edu/10.48550/arXiv.1706.03762
")), the attention mechanism embedded within the transformer network empowers text-to-image diffusion models to selectively focus on various segments of the input text during encoding, facilitating the capture of long-range dependencies among words within a sentence. Additionally, the self-attention mechanism inherent in the transformer architecture enables the model to compute attention weights for each word in the input sequence, thereby assessing the significance of individual words in computing the output representation (Vaswani et al., [2017](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR53 "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. 
https://doi-org.sire.ub.edu/10.48550/arXiv.1706.03762
")). The DMs are adept at generating images that closely align with the input text description, even when dealing with intricate and nuanced descriptions. This capability is important, particularly in the context of generating synthetic design spaces characterized by the inherent ambiguities of design problems outlined in assignment briefs.

## Methodology & experiment overview

The aim of this research is to analyze and assess how different problem definitions shape the design space within a basic design studio and to searching for a tool that help students better understand ill-defined design problems. To investigate this, a structured methodology is employed to evaluate the interpretive capabilities of Diffusion Models (DMs) in generating synthetic solution spaces that reflect varying levels of ambiguity. By conducting a comparative analysis of assignment briefs from two institutions, this approach examines how DMs respond to these diverse problem definitions, considering their potential to support traditional studio learning by offering nuanced interpretations of complex design briefs.

As displayed in the research flowchart in Fig. [3](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig3), the methodology consists of three main stages: analyses of the Problem Spaces (PSs); generation of Solution Spaces (SSs), and assessment of these SSs with design experts.

![Fig. 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig3_HTML.png?as=webp)

**Fig. 3**

In the first stage, the collected assignment brief data from PSs of two different institutions are analyzed. The assignment selection criteria are defined and the problem definitions in those briefs are identified.

In second stage, the SSs differ in whether they were produced solely under the guidance of the assignment brief or revised through a series of expert feedback sessions. For each problem space (PS), the assignment briefs were translated into text prompts while preserving their semantic structure. Using these fixed prompts, the first SS sets and control group SSs were generated for each PS. Within each SS, every problem definition was represented by a single solution - randomly selected from four solutions generated in a single prompt run - which was used consistently in both the expert feedback sessions and the later assessment process. Three design experts reviewed the first SSs in dedicated feedback sessions, while the control group SSs were retained for direct comparison in the final assessment. Feedback from the experts led to prompt revisions based on recurring issues or strengths identified across the solutions in the first SS sets (Fig. [4](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig4)). This additional feedback stage was introduced to document potential improvements between the control group and second SSs produced by the AI tool. Because in the current state-of-the-art, the text-to-image diffusion models lack contextual knowledge of the basic design realm and neither inherit a learning curve nor are able to receive feedback as a reinforcement learning strategy. Therefore to replicate synthetically the critique/feedback processes of a conventional basic design studio practice, a series of feedback procedures are implemented in the research methodology.

![Fig. 4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig4_HTML.png?as=webp)

**Fig. 4**

In the final stage of the method, design experts assessed the performances of the SSs through semi-structured interviews. The first part of the interview consisted of three questions posed to the design expers to assess the performance of the SSs and the explicitness of the brief by ordinal scale rating. In the second part, the experts were asked to comment on their insights of the experiment considering their pedagogical expertise. Comparing the synthetic generation method with their observations in the organic solution generation processes in traditional studio setup, highlights the potentials of the method as a tool in the basic design studio.

## Case study & results

This section applies the methodological framework developed in the previous section, to generate a series of synthetic SSs guided by the assignment briefs from two institutions and time frames. As discussed within the theoretical background, the design space of the conventional basic design studio is reframed as follows: Problem Space (PS) consists of the assignment briefs given in the basic design studio, which contain both ill- and well-defined design problems. Solution Space (SS) is considered as the design process outputs that are developed under the guidance of the design briefs. Two PS are collected from the first-year design studios of two different design institutions. These two institions are intentionally selected, since both studios share multiple commonalities, despite representing cases from different time frames. While the sequential pattern of the assignment briefs suggests a degree of alignment, the level of explicitness in briefs, the definition of the design problems, reveals a significant difference.

The analyses and selection criteria of the PSs of two first-year design studios are explained in this section. Assignment brief selection criteria are set the same for both PS taken from Institution1(i1), Middle East Technical University (METU) and Institution 2 (i2), Izmir University of Economics (IUE), by considering the common sequence observed frequently in-between as; abstraction, the definition of the design elements, transformation into another medium, and creation of a 2D composition. The assignment briefs and stages that require a generation of the 3D design work are eliminated. Table [1](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab1) exemplifies the assignment brief sequences of two problem spaces taken from the i1 and i2 basic design studios.

**Table 1 Assignment brief sequences of two institutions.(AS: Assignment Sequence)**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/1)

### Identifications of the problem spaces

The first PS constitutes from sixteen assignment stages collected from the archival data of the i1, Middle East Technical University, ARCH 101 basic design course held between the 2003-2007 years fall semesters. In the analyzed timeframe we noticed that the assignment briefs are mostly defined in a consequent order. In most cases, the stages of the assignment briefs require development on top of the previous stage with new problem definitions.

As exemplified in Table [1](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab1), the observed sequence starts with the abstraction of real-life objects or body parts, and each student is required to interpret the described scene, act or object to be utilized as a design element in the upcoming stage. In some cases, bodily senses are used as an element of design that needs to be abstracted and transferred into a visual design medium. The common pattern generally continues in the second step by implementing these abstracted forms into the design elements and then into a composition or a pattern. The properties of abstracted design elements are in most cases defined explicitly in the assignment brief in terms of size, color, material, and number. The third step of the observed common pattern in the brief data is making a geometric analysis of the composition (or pattern) on a tracing paper by drawing. As highlighted by one of the design experts during the interview sessions, the importance of the analysis stage is to encourage novice designers to make use of the regulating lines to find out the formal relations of the design elements. Also, this analysis stage is consciously designed to enhance the definitions of the design elements in terms of their reproducibility. After improving the formal definitions of design elements, the following step usually requires translation of the design work onto a new design medium, in terms of extracting the reproducible shapes and forms from the analysis. The final step of the sequence generally continues with the utilization of the reproduced elements on the visual field by repeating them multiple times and various scales. In some cases, the number of the element also increases in the stages of the same assignment brief.

The expert interviews indicated an implicit agenda in the final stages of the briefs for guiding the students to explore i.e. the “grouping” issue of the formal relations and design elements. These initial groups formed are further encouraged implicitly to be organized in the composition by the gestalt principles, although these principles were not mentioned in the assignment briefs.

The second set of design briefs used in the scope of the study is taken from the i2, Izmir University of Economics (IUE), FFD 101 arts and design studio consisting of the 24 assignment stages given to the first-year students from the 2022-2023 academic year fall semester.

In the initial analysis procedure of the assignment brief sequences, a common pattern was observed similar to the set of i1 assignment briefs. The overall structure of the studio was designed on the similar grounds to the i1 case. This similarity can be assumed as a result of the common i1 backgrounds of the studio coordinators’, and designers’ of the assignment briefs. However, there were several differences observed between the two sequences and the explicitnesses of the design briefs (Table [1](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab1)).

As raised during the interview sessions by design expert A, the initial step of the sequence of the i1 that had started with the abstraction of the body and senses was eliminated from the sequence structure in the case of i2. Instead, the real-life frames or objects within their surrounding context were given to the students as the composition to be analyzed. The aim of this alteration was further explained as easing the students’ comprehension process of the element properties by analyzing an image by drawing regulating lines, extracting shapes, and grouping the design elements.

The first step of the sequence in i2 PS is generally transferring an analysis of a finished, non-man-made composition on a tracing paper by drawing to extract the properties of design elements. After the analyses on the tracing paper concluded, the design briefs guided students to reproduce the design elements by changing the scale and increasing the number of the initial analysis. These copies of the analyses further act as a compositional elements to be organized on the visual medium, to let the students discover the relations of them by using regulating lines to control the visual field. Similar to the case of i1 the sequence continues with the translation of the study on a new design medium by extracting the shapes and forms, through the element definitions from the analysis drawings.

From the observed sequence patterns of two first-year design studios, it is possible to state that both studios share multiple common points in the curriculum. On the other hand, the degree of the implicitness of the brief varies, as reframed as ill-defined design problems, in the scope of the study. The element properties were usually defined explicitly in both problem spaces; however, the organization types and the gestalt principles were not mentioned in the briefs. This implicit agenda in the studio procedure is considered an intricate part of the basic design pedagogy, for encouraging the novice designer to learn by doing in terms of discovering the implicit relations and visual rules of their design mediums.

The elimination of the abstraction process from the i1 indicates a difference in the explicitness between the briefs, when the interpretation skills of the first-year design students are considered. This difference can be exemplified by comparing the first stages of assignment briefs of two institutions (Table [1](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab1)): For example, while the brief from i1 PS outlines an explicit process for students to follow in developing a design solution, the instruction to “represent a sound of a syllable” may appear ambiguous to a novice designer, particularly at the early stages of the studio. In contrast, the second PS of i2 first-year design studio presents more explicitly defined directional steps. The impact of these differing approaches to problem definition was expected to be highlighted in the synthetic SS, as one of the study’s key findings.

### Generation of solution spaces

In this section, the generation procedures of the first, control group, and second SSs are explained in detail. For generating solution with text-to-image DMs, a specific syntactic and semantic structure is required to translate the assignment briefs into text prompts. As the methodology necessitates not only the generation of a single solution space from one set of assignment briefs but also multiple problem spaces, a control mechanism is incorporated into the translation process of all assignment briefs into text prompts. The design problems articulated in the assignment briefs are translated into text prompts while preserving the semantic organization of the descriptions. Maintaining the semantic structure of the written descriptions during translation is essential to enable a valid comparative analysis between the SSs produced by the DM.

The DM developed by the Midjourney is employed to generate solutions to the design problems outlined in the assignment briefs. As the analyzed briefs prescribe a sequential order of solution generation, the image outputs from earlier stages are used as image prompts in the subsequent stages of the generation process.

Firstly the first and control group SSs are generated by translating assignment briefs directly into text prompts. Secondly, the feedback sessions are conducted with the design experts on the qualities of design solutions in the first SSs, to revise the text prompts. These revised- text prompts are further used to generate the second SSs.

#### Translating the assignment briefs into text-prompts

Building on the selection and structure of design briefs, this section outlines the necessary adjustments for translating these briefs into effective text prompts for use in DMs. The semantic hierarchy of the original brief definitions is preserved; however, certain adjustments are required when translating a design brief into a text prompt suitable for input into a DM. These alterations are grouped under three headings: syntactic alterations; sentence case alterations; and the use of parameters and versions. Table [2](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab2) examines the impact of these prompt alterations on the DM over one of the assignment briefs of i1 PS.

**Table 2 The visual impacts of text-prompt alterations in terms of: syntactic; sentence case; usage of model versions and parameters**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/2)

*Syntactic Alterations:* The first group of modifications pertains to the syntactic structure of the written design brief statements. The direct application of the inherent syntactic hierarchy from the original briefs is not feasible, as diffusion models (DMs) process information in a manner significantly different from human cognition. While readers interpret design briefs as coherent narratives describing a process, DMs rely on text tokens organized according to a semantic hierarchy, which is structured by special elements (e.g., commas “,” or colons “::”) by their internal attention mechanisms. In contrast, design briefs are conventionally written to articulate a process rather than emphasizing such syntactic markers.

As a result, necessary syntactic modifications were introduced to ensure that the text prompts conveyed essential information in a manner comprehensible to the diffusion model. For instance, in the Midjourney model, text prompts are separated by commas to preserve the semantic hierarchy of the input (Midjourney, [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR40 "Midjourney (2023). Midjourney documentation. Retrieved August 6, 2023, from 
https://docs.midjourney.com/docs/models
")). Upon reviewing the assignment tasks, it became evident that comma usage was prevalent in the original briefs. Therefore, to maintain the semantic integrity of the brief while adapting to the model’s parsing method, these commas were either removed or replaced with the conjunction “and” where appropriate. Furthermore, in cases where the design brief comprised paragraphs with two or more sentences, full stops were utilized to avoid disrupting the continuity of the task description.

Another key alteration was related to the way the Midjourney model handles numerical descriptions. Rather than using numeric values, the model interprets numerical details through verbal descriptions (Midjourney, [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR40 "Midjourney (2023). Midjourney documentation. Retrieved August 6, 2023, from 
https://docs.midjourney.com/docs/models
")). Therefore, when the design brief specified numerical elements, such as the number of design components or the repetition of features within the composition, these were converted into verbal form. This syntactic modification ensured that numerical specifications were communicated in a manner that aligned with the diffusion model’s interpretive mechanisms, ultimately enhancing the model’s ability to process and generate the desired outputs.

*Sentence Case Alterations:*The expressions stated as briefing the students with the usage of personal pronouns or indications i.e. “you”, “your”, “a group of students” are eliminated. Because during the experimentation, it is noticed that the pronouns used in the prompts, deflects the model to depict the designer instead of depicting the design work itself. Secondly, the experimentations on the model show that the material specifications defined at the end of the text prompt succeed to generate solutions that fit better into the context. These specifications are defined as the reference for the material aspects of the 2D design medim.

*The Use of Parameters and Versions:*The size of the design medium can be defined by using the specific parameter, aspect ratio (Midjourney, [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR40 "Midjourney (2023). Midjourney documentation. Retrieved August 6, 2023, from 
https://docs.midjourney.com/docs/models
")). Since the aspect ratio defined by the default mode of image generation is 1:1, the “--ar x: y” parameter is used at the end of the prompt cases to maintain the correct dimension of the design medium.

The prompt weights and negative prompting are used frequently during the generation of the solutions. Diffusion models work by conditioning the cross-attention layers of the diffusion model with contextualized text embeddings (Ploennigs & Berger, [2022](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR42 "Ploennigs, J., & Berger, M. (2022). AI art in architecture. 
https://doi-org.sire.ub.edu/10.48550/ARXIV.2212.09399
")). In other words, the Midjourney model enables users to emphasize or de-emphasize certain parts of the prompts, by the inherent transformer-based attention mechanism of the model. During the solution generation with longer text prompts that describe multiple requirements for the design task, it is noticed that the model started to deflect by adding irrelevant objects to the generated scenes. To avoid that situation in those cases, both positive and negative prompt weights are used (Table  [2](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab2)). The prompts weights are increased by the usage of double columns and negative prompts were used by adding the “—no” parameter at the end of the prompt. It enabled the model to generate output that corresponds better to the defined context of the brief.

The fourth and fifth versions of the model (v4 and v5, entered the text prompt as “-- v4” or “-- v5”) are used to generate all the solutions. The parameters that control the image output visual characteristics, quality, and style i.e. stylize, chaos, etc. are kept as default in all generation cases.

#### Feedback sessions

Following the generation of the first solution spaces (SSs) by prompting the assignment briefs into a diffusion model, a series of individual feedback sessions were conducted with three design experts. Each session lasted approximately three hours, during which the experts reviewed solutions from the first SSs. A separate set of SSs, generated with the same text prompts, was kept as a control group for the subsequent assessment stage.

Each design expert individually evaluated a total of 40 synthetic solutions during the feedback sessions. Of these, 16 solutions were generated using assignment brief data collected from the i1 archive, while the remaining 24 solutions were generated from the i2 archive.

All three design experts selected for the feedback procedure have over ten years of experience teaching foundational design studios. They also share a common background, each holding a Bachelor of Architecture degree from i1, though from different time periods. Notably, all three contributed to the development of at least one set of assignment briefs used in this study and were already familiar with these briefs. Additionally, they had prior experience observing the solution-generation process in a conventional basic design studio.

At the beginning of each session, the aims and scope of the research were explained briefly. Also, the generation methods of the solution spaces were mentioned. The design experts were guided by the authors to give written feedback for each solution by the guidance of the three following codes:

1. 4.
	The definitions of the elements of the design work, in terms of using the potentials of the material, scale, color, and texture properties.
2. 5.
	The skills of organizing the design elements on the visual field, in terms of searching for formal relations between the elements and overall control mechanism for the composition through the operations and transformations derived from the gestalt principles.
3. 6.
	The visual implication of the design themes such as dominance, balance, contrast, hierarchy, rhythm, etc.

After the feedbacks were collected through three semi-structured interview sessions with the design experts, the common points mentioned by the experts were highlighted by a congruency analysis. The feedbacks given for each solution under three main codes were identified using spreadsheets, to analyze the collected feedback data. The feedbacks given for each code were composed into one, considering the common points highlighted by reviewers. Table [3](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab3) demonstrates the assignment brief and initial solution space instance, and shows the design experts’ feedback given according to defined codes.

**Table 3 The design brief given in studio of i1 (a), and its translation in to text-prompt (b), which are used to generate a initial SS (c) are displayed. (d) demonstrates the individual feedbacks of the design experts according to defined codes and (e) shows the composed feedback for each code. (DE: Design Experts)**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/3)

#### Revision of the text-prompts

Following the collection of feedback through three semi-structured interviews with design experts, a congruency analysis was conducted to identify common themes. Feedback for each solution was organized under three main codes using spreadsheets to facilitate analysis. For each code, feedback points were synthesized into a single, cohesive summary, taking into account the common themes highlighted by the experts.

The main difference between the translation process into text-prompts from the initial stage is re-formulating the sentence cases in the brief. Since one of the aims is evaluating the impact of the problem definitions in the assignment briefs on the generated solutions, the semantic organization of the briefs was not altered during the generation process of the first SSs. However, during the generation of the second set of SSs, the required revisions were made by adding the keywords obtained from the feedback sessions and also restructuring the sentence cases.

Table [4](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab4) illustrates a case where the prompt revision procedure was applied based on the feedback summarized in Table  [3](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab3). Key points highlighted by the design experts were strategically integrated into the text prompt to ensure that essential visual and organizational elements were communicated effectively while maintaining specificity in material details and parameters. The revision process followed a whole-to-detail approach, beginning with a broad overarching concept and gradually incorporating finer details.

**Table 4 Revision of the text prompts through the composed feedback and the corresponding solution of the second SS**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/4)

In the revised sentence structure, the main visual characteristic of the desired outcome (for example, a 2D composition or a black-and-white drawing) was positioned as the initial text token, providing a clear starting point for interpreting the design intent. Following that, the organizational aspects of the design elements, such as their arrangement of the elements, grouping issues, etc. were elaborated upon. Next, material characteristics (i.e., color and texture) were specified and placed closer to the end of the prompt to ensure clarity and precision. Finally, any additional parameters related to the design were incorporated into the prompt structure to refine the instructions further.

### Assessment of the solution spaces through design expert interviews

The generation step was concluded with three sets of SSs for each PS collected from the assignment briefs of two institutions: the first sets of SSs; control groups and second sets of SSs. The purpose and generation mechanisms of each set, as well as their roles in the assessment process of the research, are outlined below:

- *First Solution Spaces:* Generated directly from the assignment briefs and later subjected to feedback.
- *Control Groups: G* enerated directly from the assignment briefs but kept as a control group for assessment without any alterations or revisions.
- *Second Solution Spaces:* Generated using revised prompts that incorporated feedback, by refining the assignment briefs based on expert insights.

The first SS and control group were expected to reflect only the visual aspects of the problems explicitly defined in the briefs, whereas the second SS aimed to capture implicit requirements, typically conveyed to students during studio instruction. Subsequently, the control groups and second SSs were comparatively assessed by the same design experts through semi-structured interviews.

The interview consisted of two parts: the first part gathered quantitative data, where experts rated performance of each solution answering the questions posed below on an ordinal scale (1 = poor, 2 = poor-average, 3 = average, 4 = average-excellent, 5 = excellent). The second part focused on qualitative feedback, where open-ended questions encouraged detailed reflections on the different solution spaces.

At the beginning of each session, the generation methods of the control groups and second SSs were explained to the experts. To evaluate the impact of the brief’s explicitness on the generated solutions, experts were asked first to assess the explicitness of the design problem. Clarifications on the definitions of ill-defined and well-defined problems, as reframed for this study, were provided to guide the experts’ evaluations. Following this, the experts rated both the explicitness of the problem statements in the assignment briefs and the performance of the SSs presented in visual form, in response to the three questions posed.

- *(Q1) Please rate the overall explicitness of the brief definition in terms of the inherent ill-defined problems.*
- *(Q2) Please rate the performances of the solutions in the control group and second solution space in terms of answering the “well-defined problems”.*
- *(Q3) Please rate the overall compositional quality of the solutions in the control group and second solution space.*

In this study, “performance of the solution space” denotes the expert-judged evaluation of the generated solutions according to the questions stated above. These three questions collectively aim to evaluate the alignment between the problem definitions and the generated design solutions from complementary perspectives: Q1 focuses on the brief itself, assessing how explicitly it conveys its intentions while retaining the inherent openness of ill-defined problems. Q2 measures how effectively the generated solutions address the well-defined components of the brief, capturing the explicit and objectively verifiable aspects of performance. Q3 provides a holistic assessment, in which ill-defined and well-defined aspects are considered together; since the inherently open-ended qualities of ill-defined problems cannot be evaluated in complete isolation from their well-defined counterparts, “overall compositional quality” here reflects the integrated assessment of both dimensions. Together, these criteria enable a nuanced evaluation that spans the spectrum from measurable, well-defined requirements to more interpretive, ill-defined dimensions of design solutions. Table [5](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab5) shows a part of the visual documentation used in the interview sessions that demonstrates design briefs taken from the i2 PS and the control group and second SS generated accordingly.

**Table 5 An example visual form demonstrated to the reviewers that displays solutions of the control group and second SSs and given briefs**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/5)

The results of the quantitative data were evaluated for each design space separately, by calculating the mean of the design experts’ rates given for the explicitness of the brief and each performance of the solutions. Figure [5](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig5) illustrates the mean ratings provided by design experts regarding the performance of solutions across control groups and the second set of solution spaces (SS) under the three key evaluation questions.

![Fig. 5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig5_HTML.png?as=webp)

**Fig. 5**

The results reveal the comparative impact of well-defined problem-solving, compositional quality, and feedback processes on design outcomes. The overall trend indicates that feedback incorporation significantly enhances solution space performance in both control and second SS groups, with explicit improvement in addressing ill-defined design problems.

## Implications of synthetic solutions on the design space of the basic design studio

The explicitness of the assignment briefs, the performance of the design solutions in addressing well-defined problems, and the overall compositional quality of the design works were evaluated by expert ratings based on the guiding questions (Fig. [5](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig5)). The results, which present the mean ratings provided by each design expert for the two design spaces, were analyzed within two comparative frameworks: (i) the impact of problem definition on the overall performance of the generated solutions, examined through a comparison of the two PS; and (ii) the impact of the feedback process, assessed by comparing the performance of the control group with that of the secondary solution spaces.

The results displayed in Fig. [5](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig5) indicate that, all synthetic solution spaces generated by the text-to-image diffusion model performed below the average for both answering the design problem requirements in terms of the well definitions and the overall compositional quality of the design solution. However, the feedback mechanism applied in the generation method of the second solution space increased the performance evaluation scores of the solutions for both questions posed. The comparative evaluations of the data in terms of the two institutions’ design spaces and the performance of the control group and second SSs contribute to the research findings and valuable insights into the importance of the problem definition and feedback process.

### Impact of the problem space on the solution spaces

The assessment made clear that the text-to-image AI model is limited to providing solid answers to the well-defined design problems in the current state, due to the limitations of the model. However, the comparison of design spaces of two different time frames contributes to the discussion in terms of the impact of the brief definitions on the generated solution performances.

Firstly, the average of the design expert rates indicates that definitions of the i2 PS are more explicit than the PS of i1 overall by 1 point difference in ordinal scale.

Secondly, as assessed by the second question [5](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig5), the evaluated performance of the control group and the second solution space of i2 was found to be more effective in addressing the well-defined problems stated in the briefs. This holds regardless of the differing generation methodologies applied for the SSs, particularly with respect to the use of varied text prompts and the inclusion of a feedback mechanism. The performance difference between the SSs of i2 and i1 in response to Question 2 (Q2) was measured as 0.4 for the control group SS and 0.5 for the second SS.

Similar results were obtained for the performances of the problem spaces of both institutions with respect to the third question, which evaluates the overall compositional quality of the solutions (Q3). The control group of i2 was rated 0.7 points higher on the ordinal scale than the control group SS of i1. Likewise, the second SS of i2 was assessed 0.4 points higher than the second SS of i1.

Based on the evaluations derived from the mean ratings of each design expert, it can be stated that the explicitness of the design briefs correlates with the overall performance of the design solutions. Although the mean scores of the design spaces from the two institutions do not differ significantly, this correlation is also evident in the individual assessments of each design expert, as illustrated in Fig. [6](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig6).

![Fig. 6](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig6_HTML.png?as=webp)

**Fig. 6**

### Impact of the feedback process on the solution spaces

The results indicate that the performance evaluations of the second SSs surpassed that of the control groups in responding to Q2 and Q3. In other words, the solutions generated through the revised text prompts addressed the well-defined design problems more effectively and demonstrated higher overall quality compared to those generated solely from brief-guided text prompts. This outcome can be attributed to the explicitness of the brief definitions, as the feedback processes made the implicit agenda of the design briefs more explicit. Consequently, the overall performance of the solution spaces in both institutions improved (Fig. [7](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig7)).

![Fig. 7](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig7_HTML.png?as=webp)

**Fig. 7**

When comparing the performance improvement rates of the solution spaces under Q3, it becomes evident that the overall compositional quality of the solutions in i1’s solution space improved more than in the cases of i2. This difference between the design spaces may be attributed to the influence of the initial brief definitions. Since the assignment briefs in i2’s problem space were evaluated as less explicit than those in i1’s, it can be inferred that the feedback process was more effective in clarifying the implicitly stated design agendas in the i1 briefs.

Additionally, a difference is observed in the improvement rates of performance of the solutions between the two questions asked in Q2 and Q3. Figure [8](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig8) presents a line chart illustrating the variation in improvement rates, showing the average rates across both the i1 and i2 design spaces.

![Fig. 8](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig8_HTML.png?as=webp)

**Fig. 8**

As the line graph demonstrates, all three expert ratings answers correlate and indicate that the overall quality of the solutions assessed by Q3 had improved sharper than the performance of answering the well-defined problems, assessed by Q2 (Fig. [7](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig7)). That is to say, the performances of SSs in answering well-defined problems are limited in a certain extent to represent element properties in comparison to the overall quality of the composition. On the other hand, the overall qualities of the design solutions have a greater potential for improvement by implementing a series of feedback layers in the process.

## Discussion: synthetic design space generation process

The results managed to shed light on the main inquiries of the research defined in the limited-scope study in terms of, evaluating the impact of the design briefs on the design solutions of a basic design studio, and searching for a method to ease the students’ comprehension and solution generation processes for the ill-defined design problems.

As shown by the results of the design expert interviews, there is a certain correlation between the explicitness of the design briefs and the overall performance of the solutions generated by an AI model, likewise the student designer’s performance in a conventional first-year design studio.

Secondly, the quantitative assessment results proved that the overall performance of the solution spaces is able to increase by implementing a feedback process in the generation mechanism. That is to say, the feedback process is essential for both synthetic and organic solution generation processes to underline the ill-defined design problems and implicit design agendas covered in the briefs. Although the evaluations indicated that in the current state performance of the AI tool is limited in representing well-defined problems, it has the potential to help the students understand the ill definitions of the problems by generating a myriad of solutions that they can see and learn, as long as the process is supported by expert guidance.

The methodology of the study has limitations in terms of the generic AI model used. To uncover the full potential of the implementation of text-to-image AI model in a first-year design studio, the current limitations of the models should be addressed.

### Representing element properties

The results of the quantitative assessments demonstrated that the performance of the solution space can increase when the ill-defined design problems in briefs are elucidated through the feedback process. However, the results of the performance of all solution spaces were assessed below the average in terms of both Q2 and Q3. However, it is clear from Fig. [9](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig9) that the text-to-image AI model performance of representing the element properties (Q2), as encoded as well-defined problems, is lower than the overall quality of the generated composition (Q3).

![Fig. 9](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig9_HTML.png?as=webp)

**Fig. 9**

Figure [9](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig9) compares the performances of solution spaces (SS) based on two metrics: Q2 (ability to address well-defined problems) and Q3 (overall quality of the design). The comparative analysis reveals that although both metrics improved through feedback loops, the compositional quality (Q3) showed a more substantial increase, suggesting that feedback strengthens the creative and organizational aspects of the solutions more effectively than solving well-defined problems.

As highlighted in both feedback and interview sessions by the experts and observed during the SS generation process, the text-to-image diffusion model has certain limits for representing the properties of the design elements in terms of number of the elements, size, scale, color, texture and technique. Although the prompt weights of the briefs were increased to overcome this issue during the generation process of the secondary solution spaces, the increase in the performance of the SS for Q2 remained less than the increase in Q3 (Fig. [8](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig8)).

On the contrary, the compositional qualities of the solution spaces were assessed remarkably higher by the experts. Besides, during the quantitative part of the interview sessions, all three design experts commented similarly that in some of the cases, the compositional qualities of the generated solution could have been rated higher (with almost 5 points corresponding to excellent performance in the ordinal scale). However, since the generated solution did not fulfill the well-defined requirements of the briefs in terms of element properties, and since this situation is often considered a reason for disqualification in a conventional studio, the ratings of Q3 were decreased concerning the ratings of Q2.

One of these cases, in which each reviewer expressed this issue mentioned above is previously demonstrated in Table [3](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab3). Even though the brief defined the number of the design elements as nine as explicitly as possible, the AI model was not able to employ nine elements in both solutions. Yet all design experts agreed that it is possible to trace the visual impact of each identified ill-defined problem on both SS, especially in the second SS. However, since the element properties also affect the overall quality of the composition, the reviewers’ rates for the Q3 also had to decrease. Table [6](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Tab6) shows the decrease in the reviewer’s ratings over the same example, due to the limitation of the model to represent material properties.

**Table 6 Impact of model deflection to represent well-defined problems on the assessment results of overall quality of the composition**

[Full size table](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y/tables/6)

This deflection in representing element properties can be considered one of the main limitations of the generic text-to-image diffusion model, due to its context-free database. Assuming that the amount of contextual image data from the design educational setups is not significant in the training dataset compared to the other contexts, the deflection of the model in reflecting the element properties in the context of the basic design studio might be unavoidable by using a generic AI model.

### The learning curve

As highlighted during the interview sessions, current model versions lack the ability to build upon previously acquired knowledge. This limitation represents one of the AI tool’s most significant drawbacks compared to novice designers, as it prevents the development of a reasoning mechanism. Consequently, while the model’s learning curve remains static, novice designers improve their abilities over the semester by developing reasoning skills within the studio environment.

As discussed within the theoretical background, one of the fundamental aims of the basic design studio is teaching the novice designer how to reason. This ability was obtained in the studio by a learning-by-doing paradigm supported by the feedback loops with the studio instructors. However, since the text-to-image AI tool is deprived of inheriting a reasoning mechanism conveyed in the basic design studio, it is not possible for it to build upon the constructed knowledge.

To partially overcome this issue, the feedback mechanism was implemented in the generation procedure of the second set of SSs. The results proved that the feedback process was effective in increasing the individual performances of the outcomes, likewise the students of a typical basic design studio. However, since the feedback processes only strengthen the qualities defined implicitly or explicitly in the brief definitions within a single brief, the improvement of the performance of the model during the sequential stages of the task remained limited. In other words, the text-to-image AI model had to start from scratch for each new prompt entered, whereas the students in the basic design studio would improve their performance in generating design solutions and also their abilities to understand the brief definitions. Figure [10](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#Fig10) exemplifies the learning curve of the AI model with two sequences taken from the assessment results of the secondary SS of i2.

![Fig. 10](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs10798-025-10033-y/MediaObjects/10798_2025_10033_Fig10_HTML.png?as=webp)

**Fig. 10**

### Implementing the text-to-image AI tools into basic design studio

Despite the limitations of the model in the current state, exploring potential integration strategies for its use in a basic design studio is valuable. Such strategies could support first-year design students in understanding and responding to various types of design problems. These strategies can be considered in two main areas: expanding the design space available to students and providing instructors with alternative tools for assessing assignment briefs.

The findings indicate that text-to-image AI models can generate a wide range of design solutions to a brief quickly, though they currently lack the capability to fully address well-defined problems. However, experts viewed the model’s performance as promising, especially for generating quality compositions with expert guidance on ill-defined problems. Consequently, implementing this tool in a basic design studio could help novice designers better understand abstract and ambiguous concepts in briefs that present ill-defined design challenges.

One potential implementation strategy of the tool could involve expanding the design space of panel discussions/critiques by the expert selection of synthetic solutions that address the same problem in various ways. This approach aligns with the collective learning culture often emphasized in the studio through discussions of a variety of student works to address specific points raised by the brief. Through the discussion of synthetic design solutions, students can learn about the different solutions offered by AI.

Moreover, the implementation of the tool may contribute to panel discussions by increasing the pace of the student reasoning process. The time required to create a solution varies from hours to weeks depending on the assignment or studio work. Generally, panel discussions are held after students complete their submissions, leaving students uncertain whether their solution aligns with the brief’s requirements. In some cases, the design brief may contain ill-defined problems that are beyond the comprehension level of novice designers, resulting in no solution being generated. If the students are guided to generate synthetic solutions based on the brief statement, panel discussions could occur immediately after the assignment is given. This approach could enhance student performance by helping students understand the requirements of the design problems and the points they need to avoid before delivering design solutions through their interpretation of the briefs.

In other words, the implementation might contribute to the students’ reasoning process alluding to the “see-move-see” pattern defined by Schön ([1992](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR45 "Schön, D. A. (1992). The reflective practitioner: How professionals think in action (1st ed.). Routledge. 
https://doi-org.sire.ub.edu/10.4324/9781315237473
")). This entails students first “seeing” the synthetic solutions, then “moving” to generate their own solutions with the interpretations obtained from the seeing process, and finally seeing how their solutions compare and contrast to those generated by the AI model.

Furthermore, the model could serve the studio instructors an alternative assessment for the level of explicitness in brief definitions. The pedagagoical strategies of basic design studio emphasizes to define the brief explicitly for the students to understand, but also implicit enough not to guide them towards the same solution path. Even though the synthetic solutions perform better under the explicit directions in terms of the results obtained in the limited scope of the study, this doesn’t necessarily mean that novice designers perform the same way. However, during the initial phases of the first-year design studio, the novice designers can be compared to the current limited state of the AI tool, as neither of them has developed contextual knowledge or equipped design reasoning mechanisms.

Using the text-to-image diffusion model (DM) to evaluate the clarity of early-stage briefs could be beneficial. By prompting the DM with the brief as a text prompt, the resulting synthetic solutions can be analyzed for their strengths and limitations, allowing for potential revisions to the brief’s clarity. This approach effectively treats the AI model as a novice designer, adjusting the brief’s level of explicitness based on the prior evaluation of performance of the generated synthetic solutions.

## Conclusion

The central focus of the research revolves around investigating the influence of the problem space on the design space within the context of the basic design studio, to devise a methodology to assist students in comprehending ill-defined design problems more effectively. The concept of design space is identified as a promising framework through which to reconstruct and reinterpret these problems, ultimately facilitating the generation of solutions.

To assess the impact of different problem definitions on the generated design solutions, two sets of assignment brief data from distinct institutions are analyzed. These briefs are retrospectively examined to distinguish between statements of ill-defined and well-defined design problems. Additionally, synthetic solution spaces are generated visually using a text-to-image diffusion model. This process involves translating assignment briefs into text prompts and implementing a feedback loop. The generated solution spaces vary based on their generation mechanisms. The first and second solution spaces are created solely based on the assignment briefs, without altering the semantic structures of the prompts. In contrast, the third set of solutions incorporated revised text prompts, highlighting implicit definitions from the briefs with feedback sessions. To evaluate the impact of problem definitions, design expert interviews are conducted to assess the solutions generated through the two different mechanisms, both quantitatively and qualitatively.

The assessment results indicated a clear association between the clarity of brief definitions and the performance of synthetic solution spaces. The feedback sessions enhance the performance of all solution spaces, particularly in generating high-quality compositions under ill-defined design problems. This outcome suggested that the impact of the feedback sessions elucidates the implicit aspects of ill-defined problem statements in the briefs. However, it also underscores the limited ability of the AI model to represent well-defined problems due to constraints inherent in the current state-of-the-art generic diffusion model, such as the lack of context-based training data and reasoning mechanisms. Despite these limitations, design experts repeatedly express optimism about the model’s potential to effectively represent ill-defined design problems.

Based on the findings of the research, the potential implementation strategies for text-to-image AI tools in the basic design studio can be summarised in two main points:

1. 7.
	The number of design solutions displayed to the students can be multiplied, by the careful selection of the solutions by the studio instructors to enrich the contextual discussion held in the panel reviews. Hence the students can move on to their organic solution generation processes from these experiences and interpretations gained by the exposure of expanded design space.

Considering AI as a crowded class of students capable of developing myriad solutions to design problems without discerning their correctness adds complexity to the studio dynamic. Just as students engage in diverse approaches to problem-solving, AI algorithms can generate a multitude of design solutions based on various parameters and constraints. However, unlike students, AI lacks the ability to discern the validity or appropriateness of these solutions in the studio process. Therefore, it becomes imperative for instructors to guide students in critically evaluating and refining the outputs generated by AI, leveraging their own expertise and judgment to navigate through the plethora of options presented.

By fostering a collaborative environment where students, instructors, and AI agents engage in iterative dialogue and critique, design studios can harness the collective intelligence of all actors involved to achieve meaningful and innovative design outcomes. This integration might open up new avenues for exploration and collaboration, where AI serves as a complementary tool to enhance students’ understanding, creativity, and design problem-solving skills within the design process.

However, it is essential to ensure that students do not view AI as a shortcut to developing design solutions, thereby bypassing the important learning-by-doing process inherent in studio pedagogy. Instead, the incorporation of AI has the potential to enhance the current capabilities of design studios by fostering collaborative reasoning among students, instructors, and AI agents. The key lies in using AI to augment the learning experience, encouraging students to critically engage with AI-generated solutions and refine them through their own creative and analytical processes.

1. 8.
	The inherent ambiguity level of the design problem can be tested on a synthetic solution generation process, beforehand exposing the students to the design briefs. It might be seen as an intermediate stage of the design problem definition process, to finetune the degree of ambiguity and abstractness of the briefs to the comprehension level of the novice designers.

The limitations of the presented research are twofold, arising from methodological choices and the technical constraints of the AI model. Firstly, the evaluation relied on a representativity sampling approach: from four images generated per problem definition, one was randomly selected for expert evaluation. This ensured feasibility and comparability while reflecting the assignment briefs, yet inevitably narrowed the representativeness of the solution space. Additionally, all three design experts had prior familiarity with the pedagogical frameworks of both institutions—a deliberate choice to ensure informed interpretation of the briefs and outputs. While this may be seen as a limitation, it was considered a justified trade-off to avoid greater interpretive inconsistencies from uninformed evaluators.

Secondly, the technical limitations of the presented research are related to the limits of the generic DM used in the scope of the study, as previously presented as: lack of contextual data for training a context-aware text-to-image DM and; a lack of ability to build up a knowledge based on the previous inputs. In future studies, the limitations of the study related to the use of a generic AI model can be solved, by developing an open-source text-to-image diffusion model with the contextual data collected from the educational setups of the basic design studio. It might be possible to implement a feedback mechanism into the model’s computational architecture to the model as reinforcement learning to improve the performance of the generated solutions, as alluding to the instructor critique sessions in the basic design studio. Furthermore, the ongoing studies in the generative AI field aim to build up knowledge, by implementing a sequence-to-sequence architecture into the diffusion models (Gong et al., [2023](https://link-springer-com.sire.ub.edu/article/10.1007/s10798-025-10033-y#ref-CR27 "Gong, S., Li, M., Feng, J., Wu, Z., & Kong, L. (2023). DiffuSeq: Sequence to sequence text generation with diffusion models. 
https://doi-org.sire.ub.edu/10.48550/arXiv.2210.08933
")). Thus, the model might be able to develop its understanding of the design problems and improve its solution generation performance by providing an incremental learning curve.

## Change history

- ### 10 November 2025
	The original article has been corrected several incorrect numbered subheadings appeared within the main text has been corrected.

## References

- Akin, Ö. (1990). Computational design instruction: Toward a pedagogy. In *The electronic design studio: Architectural knowledge and Media in the Computer era \[CAAD futures ‘89 conference proceedings / ISBN 0-262-13254-0\]* (pp. 302–316). MIT Press.
- Aytaç Dural, T. (2002). *Theatre-architecture-education: Theatre as a paradigm for introductory architectural design education*. Middle East Technical University Faculty of Architecture Press.
- Bank Stigsen, M., Moisi, A., Rasoulzadeh, S., Schinegger, K., & Rutzinger, S. (2023). AI diffusion as design vocabulary - investigating the use of AI image generation in early architectural design and education. In *eCAADe proceedings (Vol. 2, pp. 587–596). eCAADe 2023: Digital design reconsidered*. eCAADe. [https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2023.2.587](https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2023.2.587)
	[Chapter](https://doi-org.sire.ub.edu/10.52842%2Fconf.ecaade.2023.2.587)
- Bartlett, K. A., & Camba, J. D. (2024). Generative artificial intelligence in product design education: Navigating concerns of originality and ethics. *International Journal of Interactive Multimedia and Artificial Intelligence,**8*, 55–64. [https://doi-org.sire.ub.edu/10.9781/ijimai.2024.02.006](https://doi-org.sire.ub.edu/10.9781/ijimai.2024.02.006)
	[Article](https://doi-org.sire.ub.edu/10.9781%2Fijimai.2024.02.006)
- Basarir, L. (2022). Modelling AI in architectural education. *Gazı Unıversıty Journal of Scıence, 35*, 1260–1278. [https://doi-org.sire.ub.edu/10.35378/gujs.967981](https://doi-org.sire.ub.edu/10.35378/gujs.967981)
	[Article](https://doi-org.sire.ub.edu/10.35378%2Fgujs.967981)
- Besgen, A., Kuloglu, N., & Fathalizadehalemdari, S. (2015). Teaching/learning strategies through art: Art and basic design education. *Procedia-Social and Behavioral Sciences,**182*, 428–432. [https://doi-org.sire.ub.edu/10.1016/j.sbspro.2015.04.813](https://doi-org.sire.ub.edu/10.1016/j.sbspro.2015.04.813)
	[Article](https://doi-org.sire.ub.edu/10.1016%2Fj.sbspro.2015.04.813)
- Boden, M. A. (Ed.). (1990). *The philosophy of artificial intelligence*. Oxford University Press.
	[Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20philosophy%20of%20artificial%20intelligence&publication_year=1990)
- Brock, A., Donahue, J., & Simonyan, K. (2018). *Large Scale GAN Training for High Fidelity Natural Image Synthesis (Version 2)*. arXiv. [https://doi-org.sire.ub.edu/10.48550/ARXIV.1809.11096](https://doi-org.sire.ub.edu/10.48550/ARXIV.1809.11096)
- Cao, Y., Aziz, A. A., & Arshard, W. N. R. M. (2023). University students’ perspectives on artificial intelligence: a survey of attitudes and awareness among interior architecture students. *Internatıonal Journal of Educatıonal Research And Innovatıon*. [https://doi-org.sire.ub.edu/10.46661/ijeri.8429](https://doi-org.sire.ub.edu/10.46661/ijeri.8429)
- Casakin, H. (2002). Well-defined versus ill-defined design problem solving: The use of visual analogy. In D. Durling & J. Shackleton (Eds.), *Common ground - DRS international conference 2002, 5-7 September*. [https://doi-org.sire.ub.edu/10.21606/drs.2002.6](https://doi-org.sire.ub.edu/10.21606/drs.2002.6)
	[Chapter](https://doi-org.sire.ub.edu/10.21606%2Fdrs.2002.6)
- Chase, S. C. (2003). Revisiting the use of generative design tools in the early stages of design education. In *In proceedings of the 21st international conference on education and research in computer aided architectural Design in Europe*. [https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2003.465](https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2003.465)
	[Chapter](https://doi-org.sire.ub.edu/10.52842%2Fconf.ecaade.2003.465)
- Chaudhuri, N. B., & Dhar, D. (2023). Designing deep-network based novelty assessment model in design education. *Applied Soft Computing*. [https://doi-org.sire.ub.edu/10.1016/j.asoc.2022.109966](https://doi-org.sire.ub.edu/10.1016/j.asoc.2022.109966)
	[Article](https://doi-org.sire.ub.edu/10.1016%2Fj.asoc.2022.109966)
- Chiou, L.-Y., Hung, P.-K., Liang, R.-H., & Wang, C.-T. (2023). Designing with AI: An exploration of co-ideation with image generators. In *In proceedings of the 2023 ACM designing interactive systems conference. DIS ‘23: Designing interactive systems conference*. ACM. [https://doi-org.sire.ub.edu/10.1145/3563657.3596001](https://doi-org.sire.ub.edu/10.1145/3563657.3596001)
	[Chapter](https://doi-org.sire.ub.edu/10.1145%2F3563657.3596001)
- Conceição, S. M., Diehl, N. C., & Bruscato, L. M. (2023). *ChatGPT for briefing creation*. SIGraDi 2023 | accelerated landscapes. [https://doi-org.sire.ub.edu/10.5151/sigradi2023-435](https://doi-org.sire.ub.edu/10.5151/sigradi2023-435)
- Cudzik, J., Nyka, L., & Szczepański, J. (2024). Artificial intelligence in architectural education-Green campus development research. *Global Journal of Engineering Education,**26* (1), 20–25.
- Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. *Advances in Neural Information Processing Systems,**34*, 8780–8794.
- Dorst, K. (2005). Studying Design Problems. In H. Achten, K. Dorst, P. J. Stappers, & B. de Vries (Eds.), *Design research in the Netherlands 2005 – Proceedings*. Technische Universiteit Eindhoven, Faculteit Bouwkunde.
- Dreyfus, H. L. (1992). *What Computers Still Can’t Do*. MIT Press.
- Economou, A. (2001). Shape grammars in architectural design studio. In *Proceedings of the 2000 ACSA technology conference: The intersection of design and technology*. MIT.
- Ertürk, M.,Üzümcü, N. E. (2022). Görsel iletişim tasarım eğitiminin değerlendirme süreçlerinde üçüncü göz: bir yapay zekâ modeli. *Sanat ve Tasarım Dergisi, 12* (1), 191–202. [https://doi-org.sire.ub.edu/10.20488/sanattasarim.1133850](https://doi-org.sire.ub.edu/10.20488/sanattasarim.1133850)
- Fareed, M. W., Nassif, A. B., & Nofal, E. (2024). Exploring the potentials of artificial intelligence image generators for educating the history of architecture. *Heritage,**7* (3), 1727–1753. [https://doi-org.sire.ub.edu/10.3390/heritage7030081](https://doi-org.sire.ub.edu/10.3390/heritage7030081)
	[Article](https://doi-org.sire.ub.edu/10.3390%2Fheritage7030081)
- Farshad, S., Zorin, E., Amangeldiuly, N., & Fortin, C. (2023). Engagement assessment in project-based education: A machine learning approach in team chat analysis. *Education and Information Technologies,**29*, 13105–13131. [https://doi-org.sire.ub.edu/10.1007/s10639-023-12381-5](https://doi-org.sire.ub.edu/10.1007/s10639-023-12381-5)
	[Article](https://link-springer-com.sire.ub.edu/doi/10.1007/s10639-023-12381-5)
- Figoli, F., Rampino, L., & Mattioli, F. (2022). *AI in the design process: Training the human-ai collaboration*. [https://doi-org.sire.ub.edu/10.35199/epde.2022.61](https://doi-org.sire.ub.edu/10.35199/epde.2022.61)
	[Book](https://doi-org.sire.ub.edu/10.35199%2Fepde.2022.61)
- Flechtner, R., & Stankowski, A. (2023). AI is not a wildcard: Challenges for integrating AI into the design curriculum. In *Proceedings of the 5th annual symposium on HCI education* (pp. 72–77). [https://doi-org.sire.ub.edu/10.1145/3587399.3587410](https://doi-org.sire.ub.edu/10.1145/3587399.3587410)
	[Chapter](https://doi-org.sire.ub.edu/10.1145%2F3587399.3587410)
- Goldschmidt, G. (2015). The pagoda design space: Extending the scope of design. In T. Taura (Ed.), *Principia Designae -Pre-Design, Design, and PostDesign*. Springer. [https://doi-org.sire.ub.edu/10.1007/978-4-431-54403-6\_5](https://doi-org.sire.ub.edu/10.1007/978-4-431-54403-6_5)
	[Chapter](https://link-springer-com.sire.ub.edu/doi/10.1007/978-4-431-54403-6_5)
- Goldschmidt, G., & Weil, M. (1998). Contents and structure in design reasoning. *Design Issues,**14* (3), 85–100. [https://doi-org.sire.ub.edu/10.2307/1511899](https://doi-org.sire.ub.edu/10.2307/1511899)
	[Article](https://doi-org.sire.ub.edu/10.2307%2F1511899)
- Gong, S., Li, M., Feng, J., Wu, Z., & Kong, L. (2023). *DiffuSeq: Sequence to sequence text generation with diffusion models*. [https://doi-org.sire.ub.edu/10.48550/arXiv.2210.08933](https://doi-org.sire.ub.edu/10.48550/arXiv.2210.08933)
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. The MIT Press.
- Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). *Generative Adversarial Networks (Version 1)*. arXiv. [https://doi-org.sire.ub.edu/10.48550/ARXIV.1406.2661](https://doi-org.sire.ub.edu/10.48550/ARXIV.1406.2661)
- Granero, A. E., & Piegari, R. G. (2020). How does AI affect higher design education? An investigation to open the debate. In *Blucher design proceedings (pp. 683–688). Congreso SIGraDi 2020. Editora blucher*. [https://doi-org.sire.ub.edu/10.5151/sigradi2020-94](https://doi-org.sire.ub.edu/10.5151/sigradi2020-94)
	[Chapter](https://doi-org.sire.ub.edu/10.5151%2Fsigradi2020-94)
- Halskov, K., & Lundqvist, C. (2021). Filtering and informing the design space: Towards design-space thinking. *Acm Transactions on Computer-Human Interaction*. [https://doi-org.sire.ub.edu/10.1145/3434462](https://doi-org.sire.ub.edu/10.1145/3434462)
	[Article](https://doi-org.sire.ub.edu/10.1145%2F3434462)
- Halskov, K., Dove, G., & Fischel, A. (2021). Constructing a design space from a collection of design examples. *She Ji: The Journal of Design, Economics, and Innovation,**7* (3), 462–484. [https://doi-org.sire.ub.edu/10.1016/j.sheji.2021.07.001](https://doi-org.sire.ub.edu/10.1016/j.sheji.2021.07.001)
	[Article](https://doi-org.sire.ub.edu/10.1016%2Fj.sheji.2021.07.001)
- Hsiao, M.-Y., & Zhang, S. (2023). Research on the educational application of generative artificial intelligence images in the design of semiotics learning models. In *In proceedings of the 8th international conference on educational technology* (pp. 8–15). [https://doi-org.sire.ub.edu/10.1145/3637907.3637947](https://doi-org.sire.ub.edu/10.1145/3637907.3637947)
	[Chapter](https://doi-org.sire.ub.edu/10.1145%2F3637907.3637947)
- Kan, J. W. T., & Gero, J. S. (2018). Characterizing innovative processes in design spaces through measuring the information entropy of empirical data from protocol studies. *Artificial Intelligence for Engineering Design, Analysis and Manufacturing,**32* (1), 32–43. [https://doi-org.sire.ub.edu/10.1017/S0890060416000548](https://doi-org.sire.ub.edu/10.1017/S0890060416000548)
	[Article](https://doi-org.sire.ub.edu/10.1017%2FS0890060416000548)
- Kavakoglu, A. A., Almac, B., Eser, B., & Alacam, S. (2022). AI driven creativity in early design education - a pedagogical approach in the age of industry 5.0. In *40st eCAADe Proceedings*. [https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2022.1.133](https://doi-org.sire.ub.edu/10.52842/conf.ecaade.2022.1.133)
	[Chapter](https://doi-org.sire.ub.edu/10.52842%2Fconf.ecaade.2022.1.133)
- Kim, S. J. (2024). Generative artificial intelligence in collaborative ideation: Educational insight from fashion students. *Ieee Access,**12*, 49261–49274. [https://doi-org.sire.ub.edu/10.1109/ACCESS.2024.3382194](https://doi-org.sire.ub.edu/10.1109/ACCESS.2024.3382194)
	[Article](https://doi-org.sire.ub.edu/10.1109%2FACCESS.2024.3382194)
- Knight, T. (1999). *Applications in architectural design and education and practice. Report for the NSF/MIT workshop on shape computation*.
- Krıshnamurtı, R. (2006). Explicit design space? *Artificial Intelligence for Engineering Design, Analysis and Manufacturing, 20* (2), 95–103. [https://doi-org.sire.ub.edu/10.1017/S0890060406060082](https://doi-org.sire.ub.edu/10.1017/S0890060406060082)
	[Article](https://doi-org.sire.ub.edu/10.1017%2FS0890060406060082)
- Lloyd, P., & Scott, P. (1994). Discovering the design problem. *Design Studies,**15* (2), 125–140. [https://doi-org.sire.ub.edu/10.1016/0142-694X(94)90020-5](https://doi-org.sire.ub.edu/10.1016/0142-694X\(94\)90020-5)
	[Article](https://doi-org.sire.ub.edu/10.1016%2F0142-694X%2894%2990020-5)
- Midjourney (2023). Midjourney documentation. Retrieved August 6, 2023, from [https://docs.midjourney.com/docs/models](https://docs.midjourney.com/docs/models)
	[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Midjourney%20documentation&publication_year=2023)
- Park, S. (2020). Rethinking design studios as an integrative multi-layered collaboration environment. *Journal of Urban Design,**25* (4), 523–550. [https://doi-org.sire.ub.edu/10.1080/13574809.2020.1734449](https://doi-org.sire.ub.edu/10.1080/13574809.2020.1734449)
	[Article](https://doi-org.sire.ub.edu/10.1080%2F13574809.2020.1734449)
- Ploennigs, J., & Berger, M. (2022). AI art in architecture. [https://doi-org.sire.ub.edu/10.48550/ARXIV.2212.09399](https://doi-org.sire.ub.edu/10.48550/ARXIV.2212.09399)
- Reed, S. K. (2015). The structure of ill-structured (and well-structured) problems revisited. *Educational Psychology Review,**28* (4), 691–716. [https://doi-org.sire.ub.edu/10.1007/s10648-015-9343-1](https://doi-org.sire.ub.edu/10.1007/s10648-015-9343-1)
	[Article](https://link-springer-com.sire.ub.edu/doi/10.1007/s10648-015-9343-1)
- Saranlı, T. (1998). Başlangıçtan bugüne temel tasarım. In N. Teymur & T. Aytaç Dural (Eds.), *Temel Tasarım / Temel Eğitim*. ODTÜ Mimarlık Fakültesi Yayınları.
- Schön, D. A. (1992). *The reflective practitioner: How professionals think in action* (1st ed.). Routledge. [https://doi-org.sire.ub.edu/10.4324/9781315237473](https://doi-org.sire.ub.edu/10.4324/9781315237473)
	[Book](https://doi-org.sire.ub.edu/10.4324%2F9781315237473)
- Sciannamè, M. (2023). Machine learning (for) design: towards designerly ways to translate ML for design education. [https://doi-org.sire.ub.edu/10.13140/RG.2.2.27065.34405](https://doi-org.sire.ub.edu/10.13140/RG.2.2.27065.34405)
- Simon, H. A. (1957). *Models of man: Social and rational*. John Wiley and Sons.
- Simon, H. A. (1975). The functional equivalence of problem-solving skills. *Cognitive Psychology,**7*, 268–288.
	[Article](https://doi-org.sire.ub.edu/10.1016%2F0010-0285%2875%2990012-2)
- Smuha, N. A. (2021). From a ‘race to AI’ to a ‘race to AI regulation’: Regulatory competition for artificial intelligence. *Law, Innovation, and Technology,**13* (1), 57–84. [https://doi-org.sire.ub.edu/10.1080/17579961.2021.1898300](https://doi-org.sire.ub.edu/10.1080/17579961.2021.1898300)
	[Article](https://doi-org.sire.ub.edu/10.1080%2F17579961.2021.1898300)
- Sorguç, A., Kruşa Yemişçioğlu, M., & Yetkin, O. (2022). Demystifying machine learning for architecture students. *Eskişehir Technical University Journal of Science and Technology A - Applied Sciences and Engineering,**23*, 60–67. [https://doi-org.sire.ub.edu/10.18038/estubtda.1169816](https://doi-org.sire.ub.edu/10.18038/estubtda.1169816)
	[Article](https://doi-org.sire.ub.edu/10.18038%2Festubtda.1169816)
- Stark, L., & Crawford, K. (2019). The work of art in the age of artificial intelligence: What artists can teach us about the ethics of data practice. *Surveillance & Society, 17* (3/4), 442–455. [https://doi-org.sire.ub.edu/10.24908/ss.v17i3/4.10821](https://doi-org.sire.ub.edu/10.24908/ss.v17i3/4.10821)
	[Article](https://doi-org.sire.ub.edu/10.24908%2Fss.v17i3%2F4.10821)
- van Dooren, E. (2020). Making the design process in design education explicit: Two exploratory case studies. *Design and Technology Education: An International Journal, 25* (1), 13–34 [https://doi-org.sire.ub.edu/10.24377/DTEIJ.article1273](https://doi-org.sire.ub.edu/10.24377/DTEIJ.article1273)
	[Article](https://doi-org.sire.ub.edu/10.24377%2FDTEIJ.article1273)
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. [https://doi-org.sire.ub.edu/10.48550/arXiv.1706.03762](https://doi-org.sire.ub.edu/10.48550/arXiv.1706.03762)
- Wang, Y., Zhao, Y., Tian, X., Yang, J., & Luo, S. (2024). The influence of subjective knowledge, technophobia and perceived enjoyment on design students’ intention to use artificial intelligence design tools. *International Journal of Technology and Design Education*. [https://doi-org.sire.ub.edu/10.1007/s10798-024-09897-3](https://doi-org.sire.ub.edu/10.1007/s10798-024-09897-3)
	[Article](https://link-springer-com.sire.ub.edu/doi/10.1007/s10798-024-09897-3)
- Weng, L. (2021). *What are diffusion models? Lilianweng*. Github. Io. Retrieved from [https://lilianweng.github.io/posts/2021-07-11-diffusion-models/](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
- Woodbury, R. F., & Burrow, A. L. (2006). Whither design space? *Artificial Intelligence For Engineering Design, Analysis And Manufacturing,**20* (2), 63–82. [https://doi-org.sire.ub.edu/10.1017/S0890060406060057](https://doi-org.sire.ub.edu/10.1017/S0890060406060057)
	[Article](https://doi-org.sire.ub.edu/10.1017%2FS0890060406060057)
- Zhao, Y., & Gao, L. (2023). Classroom design and application of art design education based on artificial intelligence. *International Journal of Information Technology and Web Engineering*. [https://doi-org.sire.ub.edu/10.4018/IJITWE.334008](https://doi-org.sire.ub.edu/10.4018/IJITWE.334008)
	[Article](https://doi-org.sire.ub.edu/10.4018%2FIJITWE.334008)
- Zhou, C., Zhang, X., & Yu, C. (2023). How does AI promote design iteration? The optimal time to integrate AI into the design process. *Journal Of Engineering Design*. [https://doi-org.sire.ub.edu/10.1080/09544828.2023.2290915](https://doi-org.sire.ub.edu/10.1080/09544828.2023.2290915)

[Download references](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/s10798-025-10033-y?format=refman&flavour=references)

## Acknowledgments

The authors would like to express their gratitude to Tuğyan Aytaç Dural for generously sharing her archives from the Middle East Technical University ARCH 101 Basic Design Studio (2004–2005). The authors also thank Selahattin Önür, Nihal Bursa, and Erkan Gencol for their consent for the use of related materials. They also thank Ali Aslankan for providing access to the Izmir University of Economics Faculty of Fine Arts and Design first-year design studio archive. Finally, the authors acknowledge the contributions of the independent reviewers who participated in the assessment procedures as design experts. The authors also thank Ethem Gürer and Amina Rezoug Ayar for their helpful discussions during the research process.

## Author information

### Authors and Affiliations

1. Graduate School, Department of Informatics, Architectural Design Computing Program, Istanbul Technical University, Istanbul, Türkiye
	Selen Çiçek
2. Department of Architecture, Istanbul Technical University, Istanbul, Türkiye
	Mine Özkar

### Corresponding author

Correspondence to [Selen Çiçek](https://link-springer-com.sire.ub.edu/article/10.1007/).

## Ethics declarations

### Conflict of interests

On behalf of all authors, the corresponding author states that there is no conflict of interest.

## Additional information

### Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

The original online version of this article was revised: several incorrect numbered subheadings appeared within the main text has been corrected.

## Rights and permissions

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

## About this article

[![Check for updates. Verify currency and authenticity via CrossMark](https://link-springer-com.sire.ub.edu/article/10.1007/)](https://crossmark-crossref-org.sire.ub.edu/dialog/?doi=10.1007/s10798-025-10033-y)

### Cite this article

Çiçek, S., Özkar, M. Evaluating AI-generated design solutions in a basic design studio. *Int J Technol Des Educ* (2025). https://doi-org.sire.ub.edu/10.1007/s10798-025-10033-y

[Download citation](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/s10798-025-10033-y?format=refman&flavour=citation)

- Received:
- Accepted:
- Published:
- Version of record:
- DOI: https://doi.org/10.1007/s10798-025-10033-y

### Share this article

Anyone you share the following link with will be able to read this content:

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Basic design](https://link-springer-com.sire.ub.edu/search?query=Basic%20design%20&facet-discipline=%22Education%22)
- [Design space](https://link-springer-com.sire.ub.edu/search?query=Design%20space&facet-discipline=%22Education%22)
- [Design problems](https://link-springer-com.sire.ub.edu/search?query=Design%20problems&facet-discipline=%22Education%22)
- [Design briefs](https://link-springer-com.sire.ub.edu/search?query=Design%20briefs&facet-discipline=%22Education%22)
- [Artificial intelligence in design education](https://link-springer-com.sire.ub.edu/search?query=Artificial%20intelligence%20in%20design%20education&facet-discipline=%22Education%22)
- [Text-to-image diffusion models](https://link-springer-com.sire.ub.edu/search?query=Text-to-image%20diffusion%20models&facet-discipline=%22Education%22)

### Profiles

1. Selen Çiçek [View author profile](https://link-springer-com.sire.ub.edu/researchers/97919223SN)

This website sets only cookies which are necessary for it to function. They are used to enable core functionality such as security, network management and accessibility. These cookies cannot be switched off in our systems. You may disable these by changing your browser settings, but this may affect how the website functions. Please view our privacy policy for further details on how we process your information.