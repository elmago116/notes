---
title: Analysis of the Usability of Automatically Enriched Cultural Heritage Data
source: https://link-springer-com.sire.ub.edu/chapter/10.1007/978-3-031-57675-1_4?fromPaywallRec=true
authors:
  - Fernando Moral-Andrés
  - Elena Merino-Gómez
  - Pedro Reviriego 
published: 2024-01-01
created: 2025-12-11
description: This chapter presents the potential of interoperability and standardised data publication for cultural heritage resources, with a focus on community-driven approaches and web standards for usability. The Linked Open Usable Data (LOUD) design principles, which rely on...
tags:
  - Humanities/culturalHeritage
  - tech/metadata/FAIR
  - tech/LOD
  - op/acc/leer
DOI: https://doi.org/10.1007/978-3-031-57675-1
ISBN: ISBN 978-3-031-57674-4
---
![[Decoding Cultural Heritage Fernando Moral-Andrés Elena Merino-Gómez Pedro Reviriego Editors A Critical Dissection and Taxonomy of Human Creativity through Digital Tools.pdf]]

## Abstract

This chapter presents the potential of interoperability and standardised data publication for cultural heritage resources, with a focus on community-driven approaches and web standards for usability. The Linked Open Usable Data (LOUD) design principles, which rely on JSON-LD as lingua franca, serve as the foundation.

We begin by exploring the significant advances made by the International Image Interoperability Framework (IIIF) in promoting interoperability for image-based resources. The principles and practices of IIIF have paved the way for Linked Art, which expands the use of linked data by demonstrating how it can easily facilitate the integration and sharing of semantic cultural heritage data across portals and institutions.

To provide a practical demonstration of the concepts discussed, the chapter highlights the implementation of LUX, the Yale Collections Discovery platform. LUX serves as a compelling case study for the use of linked data at scale, demonstrating the real-world application of automated enrichment in the cultural heritage domain.

Rooted in empirical study, the analysis presented in this chapter delves into the broader context of community practices and semantic interoperability. By examining the collaborative efforts and integration of diverse cultural heritage resources, the research sheds light on the potential benefits and challenges associated with LOUD.

## 1 Introduction

The success of the International Image Interoperability Framework (IIIF—pronounced “triple-eye-eff”),<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn1">1</a></sup> a model for presenting and annotating digital resources that is backed by a global community developing and maintaining agreed-upon application programming interfaces (APIs) (Snydman et al., [2015](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR24 "Snydman, S., Sanderson, R., & Cramer, T. (2015). The international image interoperability framework (IIIF): A community & technology approach for web-based images. In Archiving Conference (pp. 16–21). IS&T (2015). 
https://purl.stanford.edu/df650pk4327
")), must be learnt from by the cultural heritage sector with respect to the possibility and benefits of widespread interoperability. If, as a community, we can expand from our silos of knowledge into a connected system of interoperable information, the entire sector will benefit, both from the audience perspective of vastly increased access to the information and from the publishing perspective of ease of cataloguing and delivery.

This knowledge network would be maintained by GLAM (Galleries, Libraries, Archives, and Museums) organisations as the owners and custodians of cultural and natural history objects and, as such, those organisations are best positioned to maintain information about the objects. The publication of that knowledge in an easy to use and consistent methodology will bring about the same ecosystem of tools, usage, and understanding as we have seen emerge via IIIF over the last decade. Moreover, IIIF has provided a foundational framework that has not only facilitated the emergence but also guided the development of Linked Art, a community working together to create a shared model based on linked data to semantically describe cultural heritage resources, enabling it to embrace and adhere to analogous structural paradigms. It will facilitate the creation of discovery and research systems without the expense of current aggregators that transform the data and ensure that the data is kept up to date by incentivising the publishers to do so for their own benefit, rather than for the good of the aggregator. Yale has demonstrated the possibility of this vision through the creation of LUX, which aggregates multiple, independent data sources as Linked Open Usable Data (LOUD),<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn2">2</a></sup> reconciles and enriches the records, and makes a large-scale research and discovery system available for unencumbered use.

If more institutions were to publish their data in a consistent and interoperable manner, in order to get the benefits demonstrated by LUX, all institutions’ systems and user experience would be improved by access to the totality of the community’s knowledge. This would directly improve exhibitions knowledge with access to all of the host institutions’ and lending institutions’ records, and it would allow stronger bibliographic and museum linking such as others’ objects as subjects of published works and facilitate the creation of digital catalogues raisonnés (such as the Van Gogh World Wide project <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn3">3</a></sup> and the Duchamp Research Portal <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn4">4</a></sup>). Additionally, it would better serve critical shared knowledge management tasks, such as the maintenance of living artist information. The entire community can contribute their knowledge without significantly changing their existing knowledge management practices, by transforming and using their data according to the LOUD design principles.

The audiences also directly benefit, be that for teaching and learning, research or general awareness and interest. There are only a few use cases in which the owning institution or physical location is the significant factor, instead the user just wants to discover and interact with the objects via their digital surrogate. If a user is interested in the artist J.M.W. Turner, for example, it is of little concern that “Rain, Steam and Speed” is at the National Gallery in London, while “Dort or Dordrecht: The Dort Packet-Boat from Rotterdam Becalmed” is in New Haven, when you can digitally find them via interoperable, semantic descriptions and bring images of them together to compare them side by side wherever you are through IIIF.

Participating institutions would further benefit via economies of scale. With decentralised data and interfaces, but centralised shared services, such as entity reconciliation and mapping of common datasets, we avoid the challenges of having a single centralised system which inevitably does not perform at scale and costs a lot of money for a single organisation to maintain, and the data is not kept up to date as there is no incentive to do so. However, with centralised shared and standards-based services that could be funded and maintained by the community, we ensure that the functionality is available to all and the costs can be defrayed beyond a single organisation.

That vision might sound like a fanciful fiction at first, but given the impact of IIIF for access to image content, we must consider first why it was so successful, and second how we can apply that understanding to advancing broad and usable access to cultural knowledge globally.

We begin in Sect. [2](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Sec2) with the details of data usability, highlighting the role of JSON-LD, the principles underlying LOUD, and the implications of IIIF. In Sect. [3](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Sec8), we discuss Linked Art, including its conceptual data model, API principles, and the adoption of its metadata profile. In Sect. [4](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Sec12), we demonstrate IIIF and Linked Art through LUX, Yale Collections Discovery platform. In Sect. [5](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Sec15), we reflect on community engagement and data enrichment. Finally, we conclude in Sect. [6](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Sec18).

## 2 Data Usability

Tim Berners-Lee’s vision for the Semantic Web (Berners-Lee et al., [2001](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR4 "Berners-Lee, T., Hendler, J., & Lassila, O. (2001) The semantic web. Scientific American, 284, 34–43.")), or the web of Knowledge, has been around for almost as long as the web itself and has been convincingly argued to be ultimately unachievable on a global scale (Target, [2018](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR25 "Target, S. (2018). Whatever Happened to the Semantic Web?. 
https://twobithistory.org/2018/05/27/semantic-web.html
")), across all knowledge domains.

Moreover, Bizer et al. ([2009](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR5 "Bizer, C., Heath, T., & Berners-Lee, T. (2009). Linked Data - The Story So Far. IJSWIS, 5, 1–22. 
https://doi-org.sire.ub.edu/10.4018/jswis.2009081901
")) identified several persistent challenges for the Semantic Web, a decade after the conception of the Resource Description Framework (RDF), a method for description and exchange of graph data, which include data-driven user interfaces, application architectures, schema mapping, link maintenance, licensing, trust, quality, relevance, and privacy concerns.

However, with the creation of JavaScript Object Notation for Linked Data (JSON-LD) as a developer-friendly serialisation of RDF, we have seen some aspects of that vision realised over the past 10 years.

### 2.1 JSON-LD

At the time of writing, in October 2023, JSON-LD is used by \\(45.9\\%\\) of all websites around the world.<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn5">5</a></sup> IIIF also uses JSON-LD, although few systems actually depend on the graph that it describes and tend to treat it as JavaScript Object Notation (JSON) of a particular structure. With almost half of all websites using a knowledge graph serialisation and the success of IIIF in the cultural heritage sector, it is clear that JSON-LD has played a critical role compared to previous attempts.

JSON, as a data syntax and a lightweight data interchange format, is very easy to work with both in the browser and in data management systems. It is compact and relatively easy to read and scan by the human eye, while enabling nested structures and values that align with programming languages. It can be created by hand in a text editor or serialised from other data structures using common libraries and tools. This is important because, we argue, the audience for Linked Open Data (LOD) is the developer and not a researcher or other end user of an application. For LOD to be used, it must be usable, and usability is determined not objectively without context, but instead by the needs and understanding of the user (Sanderson, [2019](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR20 "Sanderson, R. (2019). Keynote: Standards and communities: connected people, consistent data, usable applications. In 2019 ACM/IEEE Joint Conference on Digital Libraries (JCDL) (p. 28). IEEE. 
https://doi-org.sire.ub.edu/10.1109/JCDL.2019.00009
")). The user of the data is the developer, and thus they determine its usability to accomplish their current task, typically to build an application that either publishes or consumes that data to enable discovery and access to the knowledge that it encodes.

### 2.2 LOUD Design Principles

In his EuropeanaTech 2018 keynote, Sanderson argues that for data to be usable it must have five core features (Sanderson, [2018](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR19 "Sanderson, R. (2018). Shout it Out: LOUD. In EuropeanaTech Conference 2018, Rotterdam. 
https://www.slideshare.net/Europeana/shout-it-out-loud-by-rob-sanderson-europeanatech-conference-2018
")), known as the LOUD design principles and paralleling to some extent Tim-Berners Lee’s Five Star Open Data Deployment Scheme:<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn6">6</a></sup>

1. It must have the right Abstraction for the audience. The typical approach is to publish in excruciating and incomprehensible detail absolutely everything that is known about a particular topic in a complex structured form. This is neither usable nor necessary for the majority of use cases—the right abstraction of that data is one which allows the user (the developer) to accomplish their task relatively easily and, if at all possibly, enjoyably. If the developer likes to work with the data, then they will continue to do so and will encourage others to use that format, creating a virtuous cycle. In the same way that the designer of a car’s control systems, a mechanic working on it, and the driver all need different access and understanding of that system, so does different audiences need different access to cultural heritage knowledge.
2. There must be few barriers to entry. If it is easy to get started, hopefully by merely reading the data and understanding what is happening, then more developers will get started using the data. If it takes a long time to see any sign of progress, many developers will look for an easier route. Conversely, the more people who start and continue to work with the data, the more tools become available, and the more awareness of the data there is. This accelerates the virtuous cycle by demonstrating that not only is it the correct abstraction, but it is also quick to accomplish the task.
3. It must be comprehensible by simply reading the data, rather than having to use specialised tools or require significant initial research to know how to interpret it. A spreadsheet without column headers is incomprehensible, as are formats that rely exclusively on numeric naming conventions for classes, properties, or other structures. Uniform Resource Identifiers (URIs) are central in linked data, but URIs should be treated as if they are opaque—users should not read semantics into the URI, and publishers should not feel the need to try and encode details of what the URI identifies within the URI itself. This means that the data must provide some assistance to the user by giving a label or name along every URI.
4. There must be solid documentation, which has working examples to learn from. While many developers like to get started by reading the data, it is impossible to intuit all of the semantics and possible constructions from looking at examples. There must be solid, easily discoverable reference material that documents very clearly and explicitly what is permissible in the format. That documentation must have examples of each feature, and those examples should be complete and able to be dropped into an implementation of the specification in order to see it in practice.
5. There should be few exceptions, and instead the data should be internally consistent. Every exception is another rule that the developer needs to understand and then implement in their code. These exceptions are often jarring and uncomfortable to work with, leaving the developer wondering why there is this difference and what other differences there are that they do not yet know about. Conversely, being as consistent as possible means that tools are easy to build and to create testing frameworks to prove that they are correct and complete.

Overall, the main intention of LOUD is to provide straightforward access to data, primarily for software developers. Thus, a balance must be established that addresses the need for data completeness and accuracy, which depends on the ontological construct, and the pragmatic concerns of scalability and ease of use.

### 2.3 Adherence of the IIIF Presentation API 3.0 to the LOUD Design Principles

The IIIF specifications <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn7">7</a></sup> can be easily demonstrated to fulfil all of these requirements for usability. Taking the IIIF Presentation API version 3.0 as the baseline, its goal is not semantic interoperability, but instead to provide enough information to the audience—the software engineer—to create a view of the object using the referenced images, metadata, and other content, i.e., the IIIF Presentation API specifies a standardised description of a collection or compound object (via the Manifest resource) enabling a rich and complex user experience (Appleby et al., [2020](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR2 "Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2020). IIIF Presentation API 3.0. 
https://iiif.io/api/presentation/3.0/
")). Comparing this to the above fields, we find that it meets them all easily.

The abstraction of the data is appropriate for the audience to accomplish the expressed task of building a viewing application, as it does not attempt to encode any semantic or descriptive metadata, instead it aligns its structure with that intended usage. Instead of a myriad of metadata fields to understand, it has (label,value) pairs that are divided up by language, in a structure that is easy to read and easy to code with. It is laid out in such a way that the first part of the data structure is the first part that the developer needs to render to the user, and even URIs are abstracted away into the JSON-LD context document, allowing the developer to deal only with easy-to-read strings and numbers.

Figure [1](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig1) shows an IIIF Manifest from the Yale Center for British Art, along with the structure of the digital object and its attached descriptive and legal metadata, being displayed in a compatible viewer.

![A screenshot of a website displaying a painting titled Dort or Dordrecht, The Dort Packet-Boat from Rotterdam Becalmed by Joseph Mallord William Turner. The painting depicts two sailboats on a calm body of water, with dark clouds and a hazy sky in the background.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig1_HTML.png?as=webp)

**Fig. 1**

There are few barriers to entry to get started with either publishing (a complete instance can be created in just a few lines of code or easily written by hand) or to build a consuming application. A complete implementation is a lot of work, but to get started is easy, even for someone with minimal programming experience. As it is easy to get started, many have followed through to create wonderful applications that use it.

It is easily understood by reading through the data. The structure and naming conventions are easy to follow and conform to the expected usage. As JSON, it is a syntax that is very familiar to developers, and that it is also JSON-LD is not even necessary to know, let alone understand, in order to use it.<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn8">8</a></sup>

The documentation is clear and kept up to date. The definition of the structure and possible properties, along with the expected values, are well indexed with expectations for clients and publishers as to what a minimally conforming instance will contain. The examples in the specification itself are not complete, as that would take up a lot of space; however the accompanying cookbook maintains a steady progression of examples and explanations from simple to the most complex.

Finally, there are few exceptions, even to the way in which images, text, video, and other content such as tags or commentary are brought together, in this case through the W3C Web Annotation Data Model (Sanderson et al., [2017](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR22 "Sanderson, R., Ciccarese, P., & Young, B. (2017). Web Annotation Data Model. 
https://www.w3.org/TR/annotation-model/
")). The naming conventions of properties, the usage of those properties, and the expected usage of them are all clearly defined and do not have special rules based on the context where they are used.

As such, the IIIF Presentation API is, according to the five criteria set out, highly usable, and we argue this is the fundamental reason for its success.

### 2.4 IIIF Design Principles

The IIIF Design Principles,<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn9">9</a></sup> divided into 13 main parts, from 2.1 to 2.13, express the way in which the IIIF community designed the APIs, leading to their usability. It must be noted that the design principles are not expressed in terms of usability, but as more objective constructs or methodologies that can be followed, which then result in usable data (Appleby et al., [2018](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR1 "Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2018). IIIF Design Principles. 
https://iiif.io/api/annex/notes/design_principles/
")).

The first design principle, 2.1, is to scope the work through shared use cases. This ensures that the goals of the specifications are clear and well understood, such that the specifications will allow the developer to accomplish their aims, if those aims are met by the use cases that are agreed upon. It also ensures that the specifications are focused on practical details, not on theoretical issues, thereby making them easier to understand. This principle directly deals with requirements A and B.

The next three principles (2.2, 2.3, and 2.4) focus on being as easy as possible and keeping the barriers to entry minimal. These deal with requirements A, B, and E. By avoiding specific technologies as requirements and selecting simple (and consistent) solutions, the APIs are easy to get started with and appropriate for the audience and have few exceptions to deal with.

Principles 2.5–2.7, 2.9, and 2.10 are about implementation details with the web and in particular to follow the linked data principles and good web practices. These principles do not fall into the categories above directly but instead are to ensure that the implementations are performant and fit within existing technologies and standards.

The closest principle to the notion of usability is perhaps 2.8, which asserts that the specifications should be designed with JSON-LD in mind. The document says that the intent here is to ensure that the data “is as easy to use as possible without the need for a full RDF development suite” and that this will increase the likelihood of adoption. The details of designing for JSON-LD in the IIIF context are then well described later in that document.

The final three principles (2.11, 2.12, and 2.13) return to ease of adoption and implementation by ensuring that the different APIs do not all need to be implemented together but instead are loosely coupled, by ensuring that it is internationalised and usable around the world and that it is easy to extend the specifications to local use cases by defining what is expected to work in which conditions and leaving everything else unsaid.

### 2.5 The Success and Adoption of IIIF

A number of factors have contributed to the success and uptake of the IIIF.

First, it hinges significantly on the presence of robust and well-designed software implementations, encompassing both servers and clients.

Servers are essential for hosting, managing, and serving resources in a manner compliant with IIIF specifications. These server-side software solutions should efficiently handle image requests, metadata retrieval, and other IIIF API interactions while maintaining high performance and scalability.

Equally important are well-designed, attractive, and usable client implementations that are open source and easy to set up as they form the interface through which end users access and interact with digital resources. For instance, the existence of Mirador <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn10">10</a></sup> and the Universal Viewer <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn11">11</a></sup> along with the OpenSeadragon <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn12">12</a></sup> library which they use for dealing with zoomable images made interoperability an easy case to make to decision-makers and funders.

As detailed in a study by Raemy in ([2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR16 "Raemy, J. A. (2023). Characterising the IIIF and Linked Art communities: Survey report. University of Basel. 
https://hal.science/hal-04162572
")), the IIIF community’s success is underpinned by its inclusive and collaborative nature, the availability of interoperable APIs, and compatible implementations. Raemy emphasises the community’s openness, friendliness, and commitment to aiding others in their endeavours. Furthermore, the study highlights the collaborative essence of the IIIF community, its connections with prominent figures in the field, and the active participation of technical experts. Raemy also commends the community’s well-structured organisation, seamless coordination, and the invaluable support provided by IIIF staff to facilitate cooperation among members. Comprehensive documentation, a pragmatic approach, and the ability to address specific shared need further contribute to the community’s success. The IIIF community’s dedication to developing specifications, providing practical solutions and continually evolving the standard, underpins its continued appeal.

In light of these attributes that have propelled the IIIF community to prominence, it is noteworthy to delve into a specific aspect of its approach. In striving for widespread adoption of its specifications, the IIIF community undertakes several proactive initiatives, such as writing “cookbook recipes” <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn13">13</a></sup> to encourage publishers to adopt common patterns in modelling classes of complex objects, enable client software developers to support these patterns, for consistency of user experience, and demonstrate the applicability of IIIF to a broad range of use cases.

Additionally, the community remains highly active, furthering its reach and influence, notably through its various committees and interest groups.<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn14">14</a></sup> By consistently seeking advancements and adaptations, the IIIF community not only ensures its relevance but also propels the field forward. This commitment is epitomised by its active exploration of avenues to formally disseminate 3D objects within its framework (Haynes, [2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR8 "Haynes, R. (2023). Evolving standards in digital cultural heritage – developing a IIIF 3D technical specification. In M. Ioannides & P. Patias (Eds.), 3D research challenges in cultural heritage III: Complexity and quality in digitisation (pp. 50–64). Springer International Publishing. 
https://doi-org.sire.ub.edu/10.1007/978-3-031-35593-6_3
")).

By adopting these easy-to-implement specifications, institutions immediately experience the advantage of not needing to tackle the more complex user-facing components. When considering Linked Art and semantic cultural heritage data, we will look at Yale’s LUX from this perspective: If the specifications are easy to publish, is there an adoptable consuming application that demonstrates the value of publishing the data?

While the IIIF Presentation API 3.0 focuses on providing a structured framework with sufficient metadata to facilitate a seamless remote viewing experience, it still does not convey semantic information that Linked Art can provide. This highlights a gap that Linked Art bridges by enriching the understanding and integration of cultural heritage data in the digital realm.

## 3 Linked Art

Linked Art <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn15">15</a></sup> is a community-driven initiative collaborating to define a metadata application profile, the model, to describe cultural heritage, and the technical means, a RESTful API, for conveniently interacting with it. More specifically, it is an RDF application profile of the CIDOC Conceptual Reference Model (CIDOC-CRM) serialised in JSON-LD that incorporates Getty vocabularies,<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn16">16</a></sup> such as the Arts and Architecture Thesaurus (AAT), the Thesaurus of Geographic Names (TGN), and the Union List of Artist Names (ULAN), and leverages other commonly used RDF ontologies like RDF Schema (RDFS) and Dublin Core for disambiguating closely related property names used by CIDOC-CRM (Newbury, [2018](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR13 "Newbury, D. (2018). LOUD: Linked open usable data and linked.art. In 2018 CIDOC Conference (pp. 1–11). International Council of Museums (2018). 
https://cidoc.mini.icom.museum/wp-content/uploads/sites/6/2021/03/CIDOC2018_paper_153.pdf
")). Linked Art recognises another important perspective: that of software developers who, in many cases in collaboration with scholars, build applications that make use of collections data held by cultural heritage institutions and embrace the LOUD design principles (Page et al., [2020](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR14 "Page, K. R., Delmas-Glass, E., Beaudet, D., Norling, S., Rother, L., & Hänsli, T. (2020). Linked art: Networking digital collections and scholarship. In Digital Humanities 2020 Book of Abstracts (pp. 504–509). Alliance of Digital Humanities Organizations (ADHO), Online. 
https://dh2020.adho.org/wp-content/uploads/2020/07/139_LinkedArtNetworkingDigitalCollectionsandScholarship.html
")).

The goal of Linked Art is to use linked data to enhance cultural heritage collections, particularly focusing on artworks and their origins. This approach enables consistent and structured ways for art institutions to share art-related data. Since it is based on the high-level ontology CIDOC-CRM, which is developed and maintained by the International Committee for Documentation of the International Council of Museums (Doerr, [2003](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR6 "Doerr, M. (2003). The CIDOC conceptual reference module: An ontological approach to semantic interoperability of metadata. AI Magazine, 24, 75. 
https://doi-org.sire.ub.edu/10.1609/aimag.v24i3.1720
")), Linked Art describes assertions in an event-centric paradigm rather than a conventional object-centric framework. Thus, any activity can be potentially represented in an event-centric ontology and is advantageous for modelling temporal data, enabling better discovery of relationships as well as facilitating fine-grained tracking of changes and historical analysis.

### 3.1 Conceptual Model

Linked Art is documented, much like IIIF, in an incremental approach where common use cases of stakeholders—compiled through GitHub issues in a transparent manner <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn17">17</a></sup> —greatly influence the model (Raemy, [2022](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR15 "Raemy, J. A. (2022). Améliorer la valorisation des données du patrimoine culturel grâce au linked open usable data (LOUD). In N. Lasolle, O. Bruneau, & J. Lieber (Eds.), Actes des journées humanités numériques et Web sémantique (pp. 132–149). Les Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies (AHP-PReST); Laboratoire lorrain de recherche en informatique et ses applications (LORIA), Nancy. 
https://doi-org.sire.ub.edu/10.5451/unibas-ep89725
")).

Figure [2](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig2) shows the high-level conceptual model of Linked Art. It comprises some of the CIDOC-CRM classes leveraged by Linked Art. The model <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn18">18</a></sup> primarily addresses five of these provenance questions: “what”, “where”, “who”, “how”, and “when”, akin to some extent to the W7 model developed by Ram and Liu to capture provenance semantics (Ram & Liu, [2009](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR18 "Ram, S., & Liu, J. (2009). A new perspective on semantics of data provenance. In Proceedings of the First International Conference on Semantic Web in Provenance Management (pp. 35–40). CEUR-WS.org. 
https://ceur-ws.org/Vol-526/InvitedPaper_1.pdf
")).

![A framework of activities connected with a question word. They are timespan, type, actor, place, physical, information, and digital objects.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig2_HTML.png?as=webp)

**Fig. 2**

The model consists of various interconnected components, some of which share common patterns, while others have unique patterns tailored to their specific characteristics. When working with an open ontology like CIDOC-CRM, having these common baseline patterns is valuable. They have been established through experience with datasets from numerous museums, offering practical ways to structure cultural heritage data.

There are a few core properties that every resource should have for it to be a useful part of the world of linked data:

@context:

It contains a reference to the context mapping which determines how to interpret the JSON as LOD. It is not a property of the entity being described, but of the document. It must be present.

id:

It captures the URI that identifies the object. Every resource must have exactly one id, and it must be an HTTP URI.

type:

It captures the class of the object or rdf:type in RDF. Every resource must have exactly one class. This allows software to align the data model with an internal, object oriented class-based implementation.

\_label:

It captures a human readable label as a string, intended for developers or other people reading the data to understand what they are looking at. Every resource should have exactly one label and must not have more than one. It is just a string and does not have a language associated with it—if multiple languages are available for the content, then implementations can choose which is most likely to be valuable for a developer looking at the data.

Additionally, CIDOC-CRM functions as a framework that needs to be extended through the utilisation of additional vocabularies and ontologies to become useful. The provided mechanism for achieving this is the classified\_as property, which points to a term from a controlled vocabulary. This is in contrast to the type property mentioned earlier, which is reserved for CIDOC-CRM defined classes and a few specific extensions as required.

Below is a JSON-LD snippet example of an assertion stating that this object is a painting and, therefore, an artwork, using AAT terms.

{ "@context": "https://linked.art/ns/v1/linked-art.json", "id": "https://linked.art/example/object/20", "type": "HumanMadeObject", "\_label": "Simple Example Painting", "classified\_as": \[ { "id": "http://vocab.getty.edu/aat/300033618", "type": "Type", "\_label": "Painting" }, { "id": "http://vocab.getty.edu/aat/300133025", "type": "Type", "\_label": "Work of Art" } \] }

Further identified patterns within the conceptual model, all vetted by the Linked Art community, consist of object descriptions, people and organisations, places, digital integration (such as leveraging the IIIF specifications), provenance of objects, collections and sets, exhibitions of objects, primary sources of information, assertion level metadata, and dataset level metadata. Each pattern plays a pivotal role in defining and organising data related to artworks, artists, locations, digital assets, historical contexts, collections, exhibitions, and the metadata that underpins this interconnected web of cultural heritage data.

### 3.2 API Design Principles and Requirements

Linked Art also follows the footsteps of IIIF in terms of scoping how web specification should be developed by defining its own sets of API design principles and requirements.<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn19">19</a></sup>

The design principles are rooted in practicality and interoperability. They are crafted with shared, well-understood use cases, ensuring that the resulting specifications solve real-world problems. Internationalisation is prioritised to remove language barriers for users. The APIs aim for simplicity, allowing for both basic and complex use cases, with the flexibility to smart small and incremental build-up. They avoid dependency on specific technologies, making them adaptable across various implementations. By following REST principles, they seamlessly align with the web, ensuring easy caching and interaction. JSON-LD serves as the primary serialisation method, promoting user-friendly representations. Whenever possible, Linked Art adheres to existing standards and best practices to integrate seamlessly with the broader web-based cultural heritage data landscape. Extensibility is encouraged, enabling experimentation and early adoption of new versions. Lastly, Linked Art embraces the network’s role in information access, recognising that a multitude of publishing environments is more valuable than overly simplistic consuming implementations.

The Linked Art API requirements are grouped into four key areas and further illustrate how Linked Art aims to provide implementation-based guidance for creating specifications that are not only practical but also responsive to the needs of the cultural heritage sector.

Trivial to Implement:

Linked Art adheres to principles that prioritise ease of implementation, allowing data to be generated without the need for databases or dynamic systems.

Consistency across Representations:

It is maintained by ensuring that each statement appears in only one response document, if possible. Moreover, if a resource has references from multiple other resources, then it needs to be in its own response. Lastly, an efficient handling of inverse relationships is required as each connection should be encoded in a one-way direction, although Linked Art considers exceptions for performance and easy data access through a separate API for some cases.

Division of Information:

It focuses on representing one-to-many relationships from the “many” side, defining deterministic and straightforward rules for data representation, and embedding resources when they have a 1:1 relationship with their parent to reduce the number of separately maintained resources.

URI Requirements:

This requirement stipulates that resources not requiring separate dereferencing do not need their own URIs, and the flexibility of URI structure is maintained, allowing for a broad range of implementations without specific URI structure requirements for API endpoints.

If there are not any specific URI structure requirements, there are best practices for URIs documented within the Linked Art protocol <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn20">20</a></sup> with preferred endpoint paths. The top-level entity endpoints <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn21">21</a></sup> align mostly with the core classes of the Linked Art model. At the time of writing, there are eleven endpoints, loosely based on the conceptual model presented previously:

Concepts:

Types, Materials, Languages, and others, as full records rather than external references

Digital Objects:

Images, services, and other digital objects

Events:

Events and other non-specific activities that are related but not part of other entities

Groups:

Groups and Organisations

People:

Individuals

Physical Objects:

Physical things, including artworks, buildings, or other architecture, books, parts of objects, and more

Places:

Geographic places

Provenance Activities:

Various events that take place during the history of a physical thing

Sets:

Sets, including collections and sets of objects used for exhibitions

Textual Works:

Texts worthy of description as distinct entities, such as the content carried by a book or a journal article

Visual Works:

Image content worthy of description as distinct entities, such as the image shown by a painting or a drawing

### 3.3 Adoption of Linked Art

Linked Art, being a relatively novel initiative in comparison to IIIF, has faced challenges in achieving the same level of widespread adoption. The lack of awareness and limited availability of tools and services has hindered broader engagement within the Linked Art community (Raemy, [2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR16 "Raemy, J. A. (2023). Characterising the IIIF and Linked Art communities: Survey report. University of Basel. 
https://hal.science/hal-04162572
")).

However, a pivotal moment is on the horizon for Linked Art. Yale’s LUX stands out as a pioneering and substantial implementation, symbolising a turning point and serving as a catalyst for change. LUX, recognised as a flagship initiative, effectively showcases the substantial potential and transformative influence embedded in the Linked Art and IIIF specifications.

The valuable insights and advancements brought forth by LUX hold the promise to reshape the prevailing perspectives within the community. In the subsequent section, a detailed exploration into the transformative impact of LUX ensues, shedding light on its potential to shape perceptions, and importantly, its role in potentially fostering increased adoption of portals implementing standards that adhere to the LOUD design principles.

## 4 LUX: Yale Collections Discovery

LUX <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn22">22</a></sup> is an implementation of Linked Art and IIIF as a discovery and research platform for the combined collections of Yale University. This encompasses the Yale Center for British Art (YCBA), the Yale University Art Gallery (YUAG), the Yale Peabody Museum (YPM), and the Yale University Library (YUL). These collections encompass art, natural history, bibliographic and archival collections, and all of the related people, organisations, places, concepts, and events, totaling some 41 million records at the time of writing (Fig. [3](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig3)).

![A screenshot of the Yale University Library website homepage. It has a banner with the text LUX Yale Collections Discovery. Below the banner is the search bar. A photo of a clock with a paragraph of text on the LUX description is at the center.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig3_HTML.png?as=webp)

**Fig. 3**

Beyond just using the Linked Art metadata application profile, the development of LUX also tried to apply the same principles to other decisions that were needed when mapping data and use cases from the systems of record into Linked Art and which functionality was important to implement.

The system consists of several interconnected components, namely data harvesting, data pipeline, back-end database, middle tier, and front-end. These components have been integrated according to established standards including both IIIF and Linked Art, so that any individual component can be replaced without requiring a complete rewrite of the system.

### 4.1 Developing a LOUD-Driven Discovery Platform

The usability of the data was extremely important to the development process as it meant that a relatively junior front-end software engineer was able to build the application without significant assistance. The data format being easy to understand and work with meant she could dive in and get started and stakeholders could immediately see results. The consistency of the structure meant that components could be built that leveraged the repeated patterns and then could be reused whenever that pattern was encountered. By following the design principles adopted from IIIF, the implementation architecture meant that the resulting system is performant, scalable, relatively modular, and easy to adopt and adapt.

Discussions around data mapping decisions were easier given the design principles and specifications. Rather than having discussions about competing viewpoints, which has often led to frustration and lack of commitment, they could instead be structured around working cooperatively to identify which possibilities best aligned with the principles and which were outside them. Examples of requested modelling that was determined through this process to be outside of the usability guidelines, and therefore out of the scope of the work, was a desire to align the parallel structures of textual description and structured data around dimensions and materials of an object, the inclusion of data about the metadata such as the provenance of where individual assertions came from in the merged records, and structured data around uncertainty of assertions. Cases that would have led to inconsistency and more exceptions in the mapping included that animals referenced as subjects or actors could be treated as people, and fossils in the natural history museum could be treated as human made objects. Without the structures to help focus the attention on usability rather than correctness and completeness, these situations all would have led to either long and fraught discussions or aggravated developers needing to deal with more and more complex data structures.

This paradigm also helped with determining the correct approach for systems architecture and functionality. The hardest challenge of using a knowledge graph was the need to have a traditional record style interface with keyword search, facets, and views of the individual entities. A triplestore or native graph-based system does not easily enable any of these and requires multiple systems to be used in conjunction, which increases the complexity of development and maintenance of the platform. Instead after several months of research, a multi-modal platform was licensed which can treat the records as records and extract the relevant parts of the graph and allow a single query to use the features of both worlds simultaneously.

Again following the principles such as “simple as possible but no simpler”, the graph parts of the queries were analysed against the search requirements and the resulting relationships simplified to only what was necessary. As the record maintains the full data, no information is lost; however the performance and ease of development was increased by collapsing complex chains of relationships down to only one artificial predicate. For example, in order to capture the role of each artist in the production of an artwork, the object is produced by a Production event, which then has parts to represent the roles, and each part is carried out by a Person or Organisation. To simplify the common query of objects produced by a given artist, that was reduced to the equivalent of the Dublin Core relationship of creator in the graph. This pattern was then applied across all of the record types and requirements such that only relationships between records were materialised, resulting in a 40% reduction in the size of the data and a much more performant system.

One of the principles of Linked Art is that each relationship should only be present in the dataset in one record, including inverse relations. For example, if there are two Place records and one place is part of the other such as a county within a state, then the part of the relationship is only expressed in the county, and the state does not list all of the counties, cities, or other localities which are part of it. This direction is intentional to keep the size of each record down and relatively consistent. However, it leads to the inevitable and obvious question of how do you determine, in this case, the places which are part of the state? As the solution requires looking up many records, the implementation is a search on that property. To avoid technology dependence on a particular query language or search engine, the Linked Art API makes use of the Hypertext Application Language (HAL) specification (Kelly, [2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR9 "Kelly, M. (2023). JSON Hypertext Application Language. Internet Engineering Task Force. 
https://datatracker.ietf.org/doc/draft-kelly-json-hal-10
")), which allows the record to include links to search URIs and give each a name. The front-end needs only follow the link to receive a paginated list of all of the results, in the same format as for any other set of search results. This layer of indirection avoids technology dependence and increases the usability for the front-end developer, who no longer needs to understand the data model and query language in order to retrieve the list of child places, but instead is provided a named link in the record to follow, and a standard response with all of the functionality needed to produce different user interfaces for different situations.

Several other practical choices were facilitated through the LOUD principles and practices. In the LOD world, there is a fascination with federated queries—distributing the query among multiple, potentially heterogeneous systems, and then bringing the results back together before presenting them to the user. This paradigm is unreliable as the speed of the search is dependent on the speed of the slowest participating system, and if any system is offline for some reason, then the results will necessarily be incomplete. The alternative is to harvest all of the data from every participating system and combine it in advance into a single infrastructure. The trade-off is between the extent to which the results are out of date with the source system and the speed at which searches can be accomplished by end users. Given the relatively infrequent change of the majority of the records and that the users’ information needs can likely still be satisfied by information that is a day out of date, the harvest approach was selected. The records are made available for synchronisation leveraging the IIIF Change Discovery API 1.0 (Appleby et al., [2021](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR3 "Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2021). IIIF Change Discovery API 1.0.0. 
https://iiif.io/api/discovery/1.0/
")), with the Linked Art data taking the place of the IIIF resources. This was significantly easier to implement by the participating libraries, archives, and museums than every unit maintaining their own query endpoint.

### 4.2 Automatically Enriched Cultural Heritage Data

The LUX platform is distinguished by its extensive connections, not only within various Yale units but also outside, as it incorporates external data sources during data processing. These sources encompass a wide range of subject areas and perspectives. This enriches the data accessible to users by matching records within LUX. For instance, one of the key procedures employed to harmonise works and objects involves incorporating reconciled Wikidata records,<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn23">23</a></sup> allowing for meaningful connections between items, for instance, in the YCBA collection and related works. Additionally, these sources incorporate additional names and terms from authority records and subject headings, such as those from the French National Library (BnF).<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn24">24</a></sup> the Library of Congress (LoC),<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn25">25</a></sup> or the German-speaking Integrated Authority File (GND).<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn26">26</a></sup> In addition, LUX integrates Wikimedia images that are in the public domain, as illustrated by Fig. [4](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig4).<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn27">27</a></sup>

![A screenshot of a webpage titled LUX Yale Collections Discovery. It displays information about several works of art by J M W Turner. The text includes titles, dates, producers, and identifiers for the works. There are links to additional information for each work of art.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig4_HTML.png?as=webp)

**Fig. 4**

This integration significantly enhances the record by combining knowledge from different Yale units, Getty vocabulary terms, national libraries, and other external sources as shown in Fig. [5](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig5). This is an example of the positive impact and improvement that can be achieved by linking disparate data sources. The linking process is automated within the data processing code, using equivalent URI and intelligent matching of names associated with people, places, and things. However, matching and merging data into a single LUX record can be a complex task. Data quality is affected by human imperfections, as all data are derived from human input.

![A screenshot of a data sources page titled Data Sources. The text below the title states that the information has been automatically generated from the sources listed below and may be inaccurate. There is a link to report any issues. Below this text is a list of U R Ls.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig5_HTML.png?as=webp)

**Fig. 5**

Figure [6](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fig6) depicts the overall data transformation, reconciliation, enrichment, and publication workflow for LUX. The base records come from both internal and external sources.

![A flowchart of a LUX data pipeline. The database, such as I L S, A Space, Y C B A , Y U A G, Y P M, and external datasets, are connected with Harvest. It is followed by transform, reconcile, re-identify, merge, load, and mark logic. A laptop is connected to mark logic trough LUX and web cache.](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-031-57675-1_4/MediaObjects/607727_1_En_4_Fig6_HTML.png?as=webp)

**Fig. 6**

The process (diamonds) named Harvest runs nightly, triggered by an operating system level scheduler to poll each stream to find and retrieve records that have changed since the previous harvest. For external datasets that do not have associated Activity Streams, these records are either retrieved *en masse* via downloadable dump files or as needed when another record refers to them. The initial state, and all subsequent states after transformations have occurred, is stored in the “Record Caches” store. All records are passed through source-specific transformation routines (Transform) in order to either map from arbitrary data formats or validate and clean up records already provided in Linked Art. Once the information is available in a consistent format, the records are first sent to a reconciliation engine (Reconcile) to discover further identities from various datasets to be able to collect all information about a particular entity eventually into a single record.

In terms of sources, internal records are harvested from the museums and library systems using the IIIF Change Discovery API, which is in turn an implementation of the W3C Activity Streams 2.0 specification (Snell & Prodromou, [2017](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR23 "Snell, J. M., & Prodromou, E. (2017). Activity Streams 2.0. 
https://www.w3.org/TR/activitystreams-core/
")). This allows a modern and easy-to-implement solution based on JSON documents, which are easy to create, publish, and use across a variety of different back-end data pipelines. Either external sources are collected record by record over the network as needed, or if a dump file of entire dataset is available, that is downloaded and ingested into the local cache on a regular basis. The transformations are implemented in Python using the Cromulent library <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn28">28</a></sup> on a source by source basis; however, much of the heavy lifting is taken care of by the library code and these transformation routines are easy and fast to write. The validation is performed using a series of JSON Schemas for Linked Art at the syntax level <sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn29">29</a></sup> and however could be done using Shapes Constraint Language (SHACL) (Knublauch & Kontokostas, [2017](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR10 "Knublauch, H., & Kontokostas, D. (2017) Shapes Constraint Language (SHACL). 
https://www.w3.org/TR/shacl/
")) or other technologies to validate semantically as well.

Once the records are connected, they have their internal identifiers rewritten to a central set of unique identifiers by means of “Identifier Map”, a very fast in-memory database, that maps the original URIs to the internal identifiers (Re-Identify). The result is a transformation of the records where the data remains the same, but the identifiers are now consistent. The records from multiple sources that have been mapped to the same identifier are then merged together (Merge) to form the single record for the entity. The resulting dataset is then annotated with some additional features for indexing and exported to Load into the back-end query engine, a product called MarkLogic,<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn30">30</a></sup> a licensed system by a company called Progress.<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn31">31</a></sup>

In order to interact with the data, a user connects to the LUX portal in their web browser and performs a search. That search is sent through a middle tier gateway that allows for seamless transition between MarkLogic installations (a process known as blue/green switching) and through an internal web cache built with Varnish to ensure that repeated queries are only evaluated once. Additional web caches are in place between the user and the LUX front-end, including CloudFront,<sup><a href="https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#Fn32">32</a></sup> react cache, and the browser’s native web cache, to ensure performance is as fast as possible.

After the public launch of LUX in May 2023, the focus for LUX involves developing various services. Among the requested services is direct access to the identifier map of equivalencies, as well as the associated indexes for reconciliation. The open documentation of these services will be of significant value to individuals and institutions within the cultural heritage sector. By providing open access to these resources, LUX facilitates streamlined data reconciliation processes and the creation of meaningful connections between diverse cultural heritage datasets. This accessibility will enable a wider community to make effective use of LUX’s capabilities, thereby promoting enriched data and interconnected cultural heritage resources across the sector.

## 5 Discussion

This discussion is divided into two parts reflecting on the IIIF and Linked Art communities as well as the development of LUX.

First, we discuss the dimension of community engagement required to create open and interoperable standards, emphasising the collective effort required to create specifications that can be seamlessly integrated into different systems.

The effectiveness of the second dimension, which focuses on how LOUD standards can facilitate data enrichment, is greatly enhanced by the successful implementation of the first dimension. The collaborative approach to standards development lays the foundation for comprehensive data enrichment processes and highlights the need for standardised approaches to improve data enrichment in different domains.

### 5.1 Community Engagement Fosters Open Standards and Interoperability

The openness of a standard, while critical, is arguably not sufficient for widespread adoption. Achieving successful interoperability often depends on having a significant platform, either through commercial influence or through community involvement as articulated by Nelson and Van de Sompel ([2022](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR12 "Nelson, M. L., & Van de Sompel, H. (2022). D-lib magazine pioneered web-based scholarly communication. In Proceedings of the 22nd ACM/IEEE Joint Conference on Digital Libraries (pp. 1–12). Association for Computing Machinery (2022). 
https://doi-org.sire.ub.edu/10.1145/3529372.3530929
")):

> Because of the growing global adoption of open standards by GLAM institutions, especially IIIF specifications stand as a testimony that rich interoperability for distributed resource collections is effectively achievable. But other promising specifications that aim for the same holy grail are struggling for adoption, and, many times, lack of resources is mentioned as a reason. While that undoubtedly plays a role, it did not stand in the way of rapid adoption of protocols that have emerged from large corporations, such as the Google-dominated schema.org. This consideration re-emphasises that a core ingredient of a successful interoperability specification, and hence of achieving an interoperable global information web, is a large megaphone, either in the guise of commercial power or active community engagement.

For community-driven initiatives like IIIF and Linked Art, they require transparent practices that facilitate on-boarding of new members and governance, such as the establishment of a consortium, to steer the initial vision. However, it is essential to recognise that flexibility is equally paramount, particularly in the early stages of an initiative. Embracing adaptability allows these initiatives to respond to evolving needs and emerging insights from new members, ensuring that the initial vision remains dynamic and responsive to the changing landscape.

Channeling the perspective of the World Wide Web Consortium (W3C) to accomplish a demonstration of (interoperable) implementations (Etemad & Rivoal, [2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR7 "Etemad, E. J., & Rivoal, F. (2023). W3C Process Document. 
https://www.w3.org/2023/Process-20230612/
")), here is how we define interoperability within a LOUD lens:

Interoperability is a state in which two or more tested, independently developed technological systems can interact successfully according to their scope through the implementation of agreed-upon standards.

This necessitates the development and availability of several compliant tools and software that adhere to these standards, forming an ecosystem of interoperable solutions. In striving for interoperability, it is essential to recognise the formation of sub-communities or satellite groups, often existing within or adjacent to communities. They play a critical role in the creation and maintenance of tools that align with the specified standards. Heavy reliance on a particular tool, if left without dedicated care and maintenance, can pose significant challenges. In such cases, communities need to rally and take collective action to ensure the tool’s sustainability and continued functionality. These instances underscore the necessity for a shared commitment to support and collectively manage critical tools, demonstrating the communal responsibility and collaborative ethos that should define community-driven initiatives.

On a different level, the success of collaboration for developing LUX can be attributed to a shared vision that recognises the value of highlighting the connections between diverse collections across different domains. This shared vision has enabled the resources of all participating units to contribute significantly over a number of years through active participation in committees, working groups, and unit-level development efforts.

### 5.2 LOUD Standard Facilitates Data Enrichment

Interoperability and openness stand as essential cornerstones in the facilitation of robust data enrichment processes. The principle of interoperability engenders a collaborative environment wherein disparate data sources and formats converge to augment the quality and completeness of data. This convergence is pivotal in data enrichment, allowing for a seamless flow of data across a spectrum of tools and platforms. Concurrently, openness advocates for unhindered accessibility and availability of data, often epitomised by adherence to open standards. Through the lens of data enrichment, these principles synergistically operate to accommodate a diverse array of sources and perspectives, cultivating a more comprehensive and accurate enrichment process.

The LOUD paradigm embodies the harmonisation of interoperability and openness within data enrichment efforts. By harmonising data enrichment with specifications compliant with the LOUD design principles, data connections are strengthened, ultimately improving both scholarly understanding and user experience by providing enriched, accessible, and contextually interwoven data.

Many cultural heritage institutions have yet to embrace open APIs at scale, which hinders data accessibility and interoperability. Factors such as resource constraints, lack of awareness of the benefits, and complexity of implementation contribute to this slow adoption. Yet despite these challenges, LOUD specifications, such as Linked Art, offer a promising opportunity to address these issues and improve interoperability and data sharing in the cultural heritage domain. As such, Yale’s LUX serves as an exemplary model of how combining these specifications, namely IIIF and Linked Art APIs, can provide pathways for robust data pipelines, data reconciliation, and subsequent data enrichment, thereby helping the cultural heritage field to progress.

## 6 Conclusion

Both IIIF and Linked Art, supported by their dedicated and collaborative communities, are strongly committed to advancing the accessibility and interoperability of cultural heritage resources and their associated metadata. These communities actively contribute to the development and maintenance of shared APIs that are critical to promoting the seamless discovery and use of cultural heritage.

LUX serves as a compelling case study for the use of linked data at scale, demonstrating the real-world application of automated enrichment in the cultural heritage sector. By leveraging linked data technologies, LUX enables users to seamlessly access and explore vast collections of cultural heritage data across Yale’s museums, libraries, and archives in a single environment. The platform demonstrates how automatically enriched data can improve accessibility, usability, and interoperability, ultimately transforming the way users engage with and discover cultural heritage resources.

Achieving semantic interoperability requires the establishment of sound LOUD-compliant ecosystems and workflows (Manz et al., [2023](https://link-springer-com.sire.ub.edu/chapter/10.1007/?fromPaywallRec=true#ref-CR11 "Manz, M. C., Raemy, J. A., & Fornaro, P. (2023). Recommended 3D workflow for digital heritage practices. In Archiving Conference (pp. 23–28). Society for Imaging Science and Technology. 
https://doi-org.sire.ub.edu/10.2352/issn.2168-3204.2023.20.1.5
")). More specifically, the use of standards such as Linked Art is essential to enable effective data sharing across different domains. In addition, the use of IIIF APIs plays a key role in the seamless delivery and annotation of image-based resources. Importantly, it is possible for institutions of limited resources and size, not necessarily of the scale of larger institutions such as Yale, to achieve this type of interoperability. Collaboration and engagement with the wider IIIF and Linked Art communities becomes critical, providing vital support and expertise, particularly in the absence of human resources or skills.

This combination of collaborative standards and real-world application underscores the potential and need for initiatives such as IIIF and Linked Art to drive transformative progress in the cultural heritage sector and beyond.

## Notes

1. 1.
	International Image Interoperability Framework (IIIF): [https://iiif.io](https://iiif.io/).
2. 2.
	Linked Open Usable Data (LOUD): [https://linked.art/loud](https://linked.art/loud).
3. 3.
	Van Gogh Worldwide: [https://vangoghworldwide.org](https://vangoghworldwide.org/).
4. 4.
	Duchamp Research Portal: [https://www.duchamparchives.org](https://www.duchamparchives.org/).
5. 5.
	Usage statistics of JSON-LD for websites: [https://w3techs.com/technologies/details/da-jsonld](https://w3techs.com/technologies/details/da-jsonld).
6. 6.
	5-star Open Data: [https://5stardata.info/](https://5stardata.info/).
7. 7.
	IIIF API Specifications: [https://iiif.io/api/](https://iiif.io/api/).
8. 8.
	Starting in 2018, upcoming IIIF specifications and enhancements to current specifications have embraced JSON-LD 1.1 instead of JSON-LD 1.0. This shift offers numerous advantages, such as the capacity to finely define the impact of context definitions and exert greater control over the specific JSON serialisation. JSON-LD Implementation Notes: [https://iiif.io/api/annex/notes/jsonld/](https://iiif.io/api/annex/notes/jsonld/).
9. 9.
	IIIF Design Principles: [https://iiif.io/api/annex/notes/design\_principles/](https://iiif.io/api/annex/notes/design_principles/).
10. 10.
	Mirador: [https://projectmirador.org/](https://projectmirador.org/).
11. 11.
	Universal Viewer: [https://universalviewer.io/](https://universalviewer.io/).
12. 12.
	Openseadragon: [https://openseadragon.github.io/](https://openseadragon.github.io/).
13. 13.
	IIIF Cookbook: [https://iiif.io/api/cookbook/](https://iiif.io/api/cookbook/).
14. 14.
	IIIF Community: [https://iiif.io/community/](https://iiif.io/community/).
15. 15.
	Linked Art: [https://linked.art](https://linked.art/).
16. 16.
	Getty Vocabularies: [https://www.getty.edu/research/tools/vocabularies/](https://www.getty.edu/research/tools/vocabularies/).
17. 17.
	Issues from the Linked Art GitHub repository: [https://github.com/linked-art/linked.art/issues](https://github.com/linked-art/linked.art/issues).
18. 18.
	Linked Art Data Model: [https://linked.art/model/](https://linked.art/model/).
19. 19.
	Linked Art API Design Principles and Requirements: [https://linked.art/api/1.0/principles/](https://linked.art/api/1.0/principles/).
20. 20.
	Linked Art API Protocol: [https://linked.art/api/1.0/protocol/](https://linked.art/api/1.0/protocol/).
21. 21.
	Linked Art API Endpoints: [https://linked.art/api/1.0/endpoint/](https://linked.art/api/1.0/endpoint/).
22. 22.
	LUX, Yale Collections Discovery: [https://lux-collections-yale-edu.sire.ub.edu/](https://lux-collections-yale-edu.sire.ub.edu/).
23. 23.
	Wikidata: [https://www.wikidata.org](https://www.wikidata.org/).
24. 24.
	BnF Data: [https://data.bnf.fr](https://data.bnf.fr/).
25. 25.
	ID.LOC.GOV—Linked Data Service: [https://id.loc.gov](https://id.loc.gov/).
26. 26.
	Integrated Authority File (GND): [https://gnd.network](https://gnd.network/).
27. 27.
	J. M. W. Turner. (circa 1799). *Self Portrait* \[oil on canvas\], Tate Galley, London, UK. [https://commons.wikimedia.org/wiki/File:Joseph\_Mallord\_William\_Turner\_Self\_Portrait\_1799.jpg](https://commons.wikimedia.org/wiki/File:Joseph_Mallord_William_Turner_Self_Portrait_1799.jpg).
28. 28.
	Cromulent: [https://github.com/linked-art/crom](https://github.com/linked-art/crom).
29. 29.
	JSON Validator for Linked Art: [https://github.com/linked-art/json-validator](https://github.com/linked-art/json-validator).
30. 30.
	MarkLogic: [https://www.marklogic.com/](https://www.marklogic.com/).
31. 31.
	Progress: [https://progress.com/](https://progress.com/).
32. 32.
	Amazon CloudFront: [https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/).

## References

- Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2018). *IIIF Design Principles*. [https://iiif.io/api/annex/notes/design\_principles/](https://iiif.io/api/annex/notes/design_principles/)
- Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2020). *IIIF Presentation API 3.0*. [https://iiif.io/api/presentation/3.0/](https://iiif.io/api/presentation/3.0/)
- Appleby, M., Crane, T., Sanderson, R., Stroop, J., & Warner, S. (2021). *IIIF Change Discovery API 1.0.0*. [https://iiif.io/api/discovery/1.0/](https://iiif.io/api/discovery/1.0/)
- Berners-Lee, T., Hendler, J., & Lassila, O. (2001) The semantic web. *Scientific American, 284*, 34–43.
- Bizer, C., Heath, T., & Berners-Lee, T. (2009). Linked Data - The Story So Far. *IJSWIS, 5*, 1–22. [https://doi-org.sire.ub.edu/10.4018/jswis.2009081901](https://doi-org.sire.ub.edu/10.4018/jswis.2009081901)
- Doerr, M. (2003). The CIDOC conceptual reference module: An ontological approach to semantic interoperability of metadata. *AI Magazine, 24*, 75. [https://doi-org.sire.ub.edu/10.1609/aimag.v24i3.1720](https://doi-org.sire.ub.edu/10.1609/aimag.v24i3.1720)
- Etemad, E. J., & Rivoal, F. (2023). *W3C Process Document*. [https://www.w3.org/2023/Process-20230612/](https://www.w3.org/2023/Process-20230612/)
- Haynes, R. (2023). Evolving standards in digital cultural heritage – developing a IIIF 3D technical specification. In M. Ioannides & P. Patias (Eds.), *3D research challenges in cultural heritage III: Complexity and quality in digitisation* (pp. 50–64). Springer International Publishing. [https://doi-org.sire.ub.edu/10.1007/978-3-031-35593-6\_3](https://doi-org.sire.ub.edu/10.1007/978-3-031-35593-6_3)
- Kelly, M. (2023). *JSON Hypertext Application Language*. Internet Engineering Task Force. [https://datatracker.ietf.org/doc/draft-kelly-json-hal-10](https://datatracker.ietf.org/doc/draft-kelly-json-hal-10)
- Knublauch, H., & Kontokostas, D. (2017) *Shapes Constraint Language (SHACL)*. [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/)
- Manz, M. C., Raemy, J. A., & Fornaro, P. (2023). Recommended 3D workflow for digital heritage practices. In *Archiving Conference* (pp. 23–28). Society for Imaging Science and Technology. [https://doi-org.sire.ub.edu/10.2352/issn.2168-3204.2023.20.1.5](https://doi-org.sire.ub.edu/10.2352/issn.2168-3204.2023.20.1.5)
- Nelson, M. L., & Van de Sompel, H. (2022). D-lib magazine pioneered web-based scholarly communication. In *Proceedings of the 22nd ACM/IEEE Joint Conference on Digital Libraries* (pp. 1–12). Association for Computing Machinery (2022). [https://doi-org.sire.ub.edu/10.1145/3529372.3530929](https://doi-org.sire.ub.edu/10.1145/3529372.3530929)
- Newbury, D. (2018). LOUD: Linked open usable data and linked.art. In *2018 CIDOC Conference* (pp. 1–11). International Council of Museums (2018). [https://cidoc.mini.icom.museum/wp-content/uploads/sites/6/2021/03/CIDOC2018\_paper\_153.pdf](https://cidoc.mini.icom.museum/wp-content/uploads/sites/6/2021/03/CIDOC2018_paper_153.pdf)
- Page, K. R., Delmas-Glass, E., Beaudet, D., Norling, S., Rother, L., & Hänsli, T. (2020). Linked art: Networking digital collections and scholarship. In *Digital Humanities 2020 Book of Abstracts* (pp. 504–509). Alliance of Digital Humanities Organizations (ADHO), Online. [https://dh2020.adho.org/wp-content/uploads/2020/07/139\_LinkedArtNetworkingDigitalCollectionsandScholarship.html](https://dh2020.adho.org/wp-content/uploads/2020/07/139_LinkedArtNetworkingDigitalCollectionsandScholarship.html)
- Raemy, J. A. (2022). Améliorer la valorisation des données du patrimoine culturel grâce au linked open usable data (LOUD). In N. Lasolle, O. Bruneau, & J. Lieber (Eds.), *Actes des journées humanités numériques et Web sémantique* (pp. 132–149). Les Archives Henri-Poincaré - Philosophie et Recherches sur les Sciences et les Technologies (AHP-PReST); Laboratoire lorrain de recherche en informatique et ses applications (LORIA), Nancy. [https://doi-org.sire.ub.edu/10.5451/unibas-ep89725](https://doi-org.sire.ub.edu/10.5451/unibas-ep89725)
- Raemy, J. A. (2023). *Characterising the IIIF and Linked Art communities: Survey report*. University of Basel. [https://hal.science/hal-04162572](https://hal.science/hal-04162572)
- Raemy, J. A., Gray, T., Collinson, A., & Page, K. R. (2023). Enabling participatory data perspectives for image archives through a linked art workflow. In A. Baillot, W. Scholger, T. Tasovac, & G. Vogeler (Eds.), *Digital Humanities 2023 Book of Abstracts* (pp. 515–516). Alliance of Digital Humanities Organizations (ADHO). [https://doi-org.sire.ub.edu/10.5451/unibas-ep95099](https://doi-org.sire.ub.edu/10.5451/unibas-ep95099)
- Ram, S., & Liu, J. (2009). A new perspective on semantics of data provenance. In *Proceedings of the First International Conference on Semantic Web in Provenance Management* (pp. 35–40). CEUR-WS.org. [https://ceur-ws.org/Vol-526/InvitedPaper\_1.pdf](https://ceur-ws.org/Vol-526/InvitedPaper_1.pdf)
- Sanderson, R. (2018). Shout it Out: LOUD. In *EuropeanaTech Conference 2018, Rotterdam*. [https://www.slideshare.net/Europeana/shout-it-out-loud-by-rob-sanderson-europeanatech-conference-2018](https://www.slideshare.net/Europeana/shout-it-out-loud-by-rob-sanderson-europeanatech-conference-2018)
- Sanderson, R. (2019). Keynote: Standards and communities: connected people, consistent data, usable applications. In *2019 ACM/IEEE Joint Conference on Digital Libraries (JCDL)* (p. 28). IEEE. [https://doi-org.sire.ub.edu/10.1109/JCDL.2019.00009](https://doi-org.sire.ub.edu/10.1109/JCDL.2019.00009)
- Sanderson, R. (2020). *The Importance of being LOUD*. LODLAM 2020, Los Angeles, CA. [https://www.slideshare.net/azaroth42/the-importance-of-being-loud](https://www.slideshare.net/azaroth42/the-importance-of-being-loud)
- Sanderson, R., Ciccarese, P., & Young, B. (2017). *Web Annotation Data Model*. [https://www.w3.org/TR/annotation-model/](https://www.w3.org/TR/annotation-model/)
- Snell, J. M., & Prodromou, E. (2017). *Activity Streams 2.0*. [https://www.w3.org/TR/activitystreams-core/](https://www.w3.org/TR/activitystreams-core/)
- Snydman, S., Sanderson, R., & Cramer, T. (2015). The international image interoperability framework (IIIF): A community & technology approach for web-based images. In *Archiving Conference* (pp. 16–21). IS&T (2015). [https://purl.stanford.edu/df650pk4327](https://purl.stanford.edu/df650pk4327)
- Target, S. (2018). *Whatever Happened to the Semantic Web?*. [https://twobithistory.org/2018/05/27/semantic-web.html](https://twobithistory.org/2018/05/27/semantic-web.html)

## Acknowledgements

We want to express our deep appreciation to the dedicated contributors within the IIIF and Linked Art communities, who have served as a continual source of inspiration for our work. We also extend our thanks to our colleagues at the University of Basel and Yale University for their unwavering support and expertise.

## Editor information

### Editors and Affiliations

## Rights and permissions

## About this chapter

### Cite this chapter

Raemy, J.A., Sanderson, R. (2024). Analysis of the Usability of Automatically Enriched Cultural Heritage Data. In: Moral-Andrés, F., Merino-Gómez, E., Reviriego, P. (eds) Decoding Cultural Heritage. Springer, Cham. https://doi-org.sire.ub.edu/10.1007/978-3-031-57675-1\_4

- [.RIS](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/978-3-031-57675-1_4?format=refman&flavour=citation "Download this article's citation as a .RIS file")
- [.ENW](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/978-3-031-57675-1_4?format=endnote&flavour=citation "Download this article's citation as a .ENW file")
- [.BIB](https://citation-needed-springer-com.sire.ub.edu/v2/references/10.1007/978-3-031-57675-1_4?format=bibtex&flavour=citation "Download this article's citation as a .BIB file")
- DOI https://doi.org/10.1007/978-3-031-57675-1\_4
- Published
- Publisher Name Springer, Cham
- Print ISBN 978-3-031-57674-4
- Online ISBN 978-3-031-57675-1
- eBook Packages [Computer Science](https://link-springer-com.sire.ub.edu/search?facet-content-type=%22Book%22&package=11645&facet-start-year=2024&facet-end-year=2024) [Computer Science (R0)](https://link-springer-com.sire.ub.edu/search?facet-content-type=%22Book%22&package=43710&facet-start-year=2024&facet-end-year=2024)

## Publish with us

[Policies and ethics](https://www-springernature-com.sire.ub.edu/gp/policies/book-publishing-policies)