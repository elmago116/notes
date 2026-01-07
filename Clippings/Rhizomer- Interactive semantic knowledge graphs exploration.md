---
source: Manual
type: document
base: clippings
title: Rhizomer Interactive semantic knowledge graphs exploration – DOAJ
last_enrichment_run: 2025-08-20
updated: 2025-08-20
journal: SoftwareX
volume: 20
pages: 101235
year: 2022
doi: 10.1016/j.softx.2022.101235
url: https://doaj.org/article/008202e365be4088bbf3be920b03a5b6
authors:
  - Roberto García
  - Juan-Miguel López-Gil
  - Rosa Gil
description: "Rhizomer helps researchers and practitioners explore knowledge graphs available as Semantic Web data by performing the three data analysis tasks: overview, zoom and filter, and details-on-demand."
tags:
  - CCC/visualisation
  - design/UX/user_interface
  - Tech/KG
  - op/projects/similar
apa_citation: Roberto García et al., 2022
---
[Read online](http://www.sciencedirect.com/science/article/pii/S2352711022001534)
[[rhiz]]

[[Rhizomer- Interactive semantic knowledge graphs exploration.pdf]]

#Tech/KG 
## Abstract

[Read online](http://www.sciencedirect.com/science/article/pii/S2352711022001534)
[[rhiz]]

#op/projects/similar  Rhizomer helps researchers and practitioners explore knowledge graphs available as Semantic Web data by performing the three data analysis tasks: overview, zoom and filter, and details-on-demand. This approach makes it easier for users to get an idea about the overall structure and intricacies of a dataset, when compared to existing approaches and even without prior knowledge. Rhizomer is helpful for data reusers, who want to know about the reuse opportunities of a given dataset, and for knowledge graph creators, who can check if the generated data follow their expectations. Rhizomer has been applied in many scenarios, from research and commercial projects to teaching.

## Notes for digital libraries article
- **Process-driven**:
  - “Rhizomer helps researchers and practitioners explore knowledge graphs available as Semantic Web data by performing the three data analysis tasks: overview, zoom and filter, and details-on-demand.” (Abstract)
- **Methodological tools**:
  - Interactive visualization and exploration of knowledge graphs supporting the three data analysis tasks (overview, zoom & filter, details-on-demand). (Abstract)
- **Participation level**:
  - Users (researchers, practitioners, learners) engage with the tool for exploration and data reuse; no participatory design or evaluation process is described in this clipping.
- **Epistemic justice**:
  - The abstract focuses on exploration and data analysis tasks; there is no explicit mention of gender, intersectionality, or epistemic justice.

## PDF text extraction

SoftwareX20(2022)101235
Contents lists available at ScienceDirect
SoftwareX
journal homepage: www.elsevier.com/locate/softx
Originalsoftwarepublication
Rhizomer:Interactivesemanticknowledgegraphsexploration
RobertoGarcíaa,∗,Juan-MiguelLópez-Gil b,RosaGil a
aUniversitat de Lleida, Jaume II 69, 25001 Lleida, Spain
bUniversity of the Basque Country, Paseo Manuel de Lardizabal 1, 20018 Donostia-San Sebastián, Spain
a r t i c l e i n f o
Article history:
Received27June2022
Receivedinrevisedform19September2022
Accepted14October2022
Keywords:
Knowledgegraph
Semanticdata
Visualization
Userinterface
a b s t r a c t
RhizomerhelpsresearchersandpractitionersexploreknowledgegraphsavailableasSemanticWeb
databyperformingthethreedataanalysistasks:overview,zoomandfilter,anddetails-on-demand.
Thisapproachmakesiteasierforuserstogetanideaabouttheoverallstructureandintricaciesof
a dataset, when compared to existing approaches and even without prior knowledge. Rhizomer is
helpfulfordatareusers,whowanttoknowaboutthereuseopportunitiesofagivendataset,andfor
knowledgegraphcreators,whocancheckifthegenerateddatafollowtheirexpectations.Rhizomer
hasbeenappliedinmanyscenarios,fromresearchandcommercialprojectstoteaching.
©2022TheAuthor(s).PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBYlicense
(http://creativecommons.org/licenses/by/4.0/).
Codemetadata
Currentcodeversion RhizomerEyev0.2.1andRhizomerAPIv0.2.1
Permanentlinktocode/repositoryusedforthiscodeversion https://github.com/ElsevierSoftwareX/SOFTX-D-22-00168
PermanentlinktoReproducibleCapsule
LegalCodeLicense GPL-3.0,https://github.com/rhizomik/rhizomerAPI/blob/master/LICENSEand
https://github.com/rhizomik/rhizomerEye/blob/master/LICENSE
Codeversioningsystemused git
Softwarecodelanguages,tools,andservicesused RhizomerEye:TypeScript,Angular.RhizomerAPI:Java,Spring.
Compilationrequirements,operatingenvironments&dependencies RhizomerEye:Node12andRhizomerAPI:Java11
IfavailableLinktodeveloperdocumentation/manual https://github.com/rhizomik/rhizomerAPI/blob/master/README.md
Supportemailforquestions contact@rhizomik.net
Softwaremetadata
Currentsoftwareversion RhizomerEyev0.2.1andRhizomerAPIv0.2.1
Permanentlinktoexecutablesofthisversion Dockerimagesavailable,RhizomerEye
https://hub.docker.com/repository/docker/rhizomik/rhizomer-eyeand
RhizomerAPI:https://hub.docker.com/repository/docker/rhizomik/rhizomer-api
PermanentlinktoReproducibleCapsule
LegalSoftwareLicense GPL-3.0,https://github.com/rhizomik/rhizomerAPI/blob/master/LICENSEand
https://github.com/rhizomik/rhizomerEye/blob/master/LICENSE
Computingplatforms/OperatingSystems Webbased
Installationrequirements&dependencies RecommendedtouseDocker,asdetailedintheinstallationinstructions
Ifavailable,linktousermanual—ifformallypublishedincludeareferenceto
thepublicationinthereferencelist
https://github.com/rhizomik/rhizomerAPI/blob/master/README.md#install
Supportemailforquestions contact@rhizomik.net
∗ Correspondingauthor.
E-mail address: roberto.garcia@udl.cat(RobertoGarcía).
https://doi.org/10.1016/j.softx.2022.101235
2352-7110/© 2022TheAuthor(s). PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Motivationandsignificance
TheSemanticWebprovidesthetoolsandmechanismstobuild
aWebofdatathatfacilitatesdataintegrationattheWebscale
while providing access, in a unified way, through a standard
query language. Compared tothe so-calledWeb 2.0, themain
distinction is that rather than working with a sizable amount
ofscattereddatathatneedssomelevelofhumaninterpretation
to process it, data is integrated and conceptualised in a way
thatcomputersthemselvescan‘‘understand’’itandextractnew
knowledge[1].
However,neithertheSemanticWebnorthesoftwareagents
arecurrentlyentirelyfunctionalforthefollowingtaskstargeted
by this initiative. Extracting meaningful information from re-
searchdocuments[2],providingtoolsforcomputingandextract-
ing ideas from the Semantic Web [3], semantic aware graph-
basedpartitioning[4],andeffectivequeryperformanceinterms
ofqueryexecutiontimeanddatascalabilitybytheuseofdata
storagesolutions[5]remainresearchtopicsinthisfield.From
atrendsperspective,topicssuchaslinkeddata,opendata,and
datasourceshaveincreasedinimportanceovertheyears.Onthe
otherhand,itsinteractionswithotherresearchareashighlight
thecross-disciplinarynatureoftheSemanticWeb[6].
Accessing the Semantic Web is still mostly a human activ-
ity. Even if some degree of integration is achieved, managing
andeffectivelyupdatingsuchanintegratedframeworkmayre-
quiresignificanthumanresources,beextremelytime-consuming
anddifficulttofullyautomate.Thisaccessisthroughtheuser
interfaces and is primarily used for information-seeking tasks.
A popular study area is the interactive Semantic Web, where
technologiesarecreatedusingahuman-centredapproachthat
attempts to improve human engagement with semantic data,
ratherthansimplyenhancingtheefficacyandaccuracyofau-
tomated algorithms and processes. The distinctive characteris-
ticsthataSemanticWebuserinterfaceneedstosupportwere
analysed in [7], while [8] reviews research on user interfaces,
visualizations,andinteractionmethodsfromrelevantSemantic
Webvenues.
Structureddatacalledknowledgegraphs,whicharefrequently
definedusingtheSemanticWebstandardResourceDescription
Framework[1],depictentitiesandtheinteractionsbetweenthem
intheformofagraph.Inparticular,whengraphsfromseveral
datasourcesneedtobecombined,itcouldbechallengingforlay
userstoexamineexistingknowledgegraphs[9].However,there
are still issues with efficiency, usability, and scalability when
extendingthesemanticsearchtodocumentstructureandexter-
nal,formalknowledgesources[10].Effortstowardsinteractive
andintuitiveSemanticWebexplorersarebeingmadeinmulti-
pleareas,suchaslifesciences,geosciences,digitalhumanities,
healthcare,ordefence[11].
ThisworkpresentsRhizomer,atooltoeasilyexploreknowl-
edgegraphsavailableassemanticdatathatprovidesahead-start
forresearchers,practitioners,orevenlayusers,withoutrequiring
priorknowledgeofthedatastructureortheunderlyingSemantic
Webtechnologies.
Softwaredescription
ThroughRhizomer,aknowledgegraphcanbeexploredwith-
out requiring prior knowledge about the dataset structure or
the underlying semantic data and query languages. Rhizomer
isavailableasanopen-sourcewebapplicationwithabackend
(RhizomerAPI)andafrontend(RhizomerEye).
Tofacilitatetheexploration,Rhizomersupportsthethreeclas-
sicaldataanalysistasksproposedbyShneiderman[12]:getting
an overview of the data, zooming and filtering, and viewing
detailsondemand.Eachofthesetasks,furtherdetailedinthefol-
lowingsubsections,issupportedbythefollowingsetoffeatures
implementedbyRhizomer:
• Overview
– WordCloud:overviewtheclassesinadatasetthrough
awordcloudwiththenamesoftheclassesandwhere
theirsizeisproportionaltothenumberofinstancesof
eachclass.
– Network:anoverviewofthemainclasses,andrela-
tionshipsamongthem,usinganetworkrepresentation
whichincludesclassesandrelationshipsnames.
• ZoomandFilter
– ClassesAutocomplete:inputfield,withautocomplete
basedonthenameoftheclassesinstantiatedinthe
dataset,tochoosetheclasstofocuson.
– Global Text Search: input field to search across the
datasetforinstancesrelatedtoliteralscontainingthe
typedtext,orresourcewhoselabelcontainsthattext.
– FacetValuesFilter:facetviewshowingthe10most
commonvaluesforthepropertycorrespondingtothe
facet and constrained to the focused class. Clicking
any of them filters the displayed instances to those
featuringthatvaluefortheproperty.
– FacetValuesAutocomplete:inputfieldtofilterthe
listofinstancesforthefocusedclassusinganyofthe
values for the corresponding property. Typed text is
autocompletedtotheavailablevaluesforthefacet.
– NumericRangeFacet:forfacetswithnumericranges
(likeinteger,decimaloryear),theminimumandmax-
imumvaluesareshowntogetherwithaslidertofilter
instancesbasedonauser-definedrangeofvalues.
– ClassTextSearch:inputfieldfortextsearchamongall
facetvaluesfortheclasscurrentlythefocus.
• Details-on-demand
– InstanceMetadataView:onceaparticularinstanceis
selected, all the metadata describing it is presented.
Thisincludesalldirectpropertiesandvalues.Labelsare
usedinsteadofURIidentifierswhentheyareavailable.
– LinkedDataBrowser:despitelabelsbeingshownin-
steadofURIsforrelationships,theyaredisplayedas
links. When clicked, it is checked if the URI can re-
solvetoRDFdataandthusexplorationcancontinue
byrenderingitusingtheInstanceMetadataView.This
way,RhizomeralsoworksasaLinkedDatabrowser.
Forinstance,ifaDBpediaURIforacityisusedinthe
databeingexplored,itcanbeclickedtoretrievethe
metadatadescribingthecity.
– InverseFacet:facetcorrespondingtoaninverseprop-
ertyforthecurrentlydisplayedinstance.Forinstance,
foraperson,afacettoexplorethepublicationsthat
personhasauthored.
OtherRhizomer’sfeatures,whicharenotspecifictoapartic-
ulartaskare:
• MultilingualSupport:Rhizomeruseslabels,wheneverthey
areavailable,insteadoftheiridentifiers(URIsorfragments
ofthem)torefertoclasses,propertiesandresourcesinthe
databeingexplored.Moreover,itgivespreferencetothose
inthelanguageselectedbytheuseriflabelshavealanguage
tag. Otherwise, it defaults to untagged labels or those in
English.
2

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Fig.1. Overviewasawordcloud,onlineinteractiveversionhttps://rhizomer.rhizomik.net/datasets/dbpedia.
• EndpointGraphsManagement :whentheendpointstoring
the data for a dataset is writable, Rhizomer facilitates its
management through its user interface. It is possible to
creategraphsandloaddataintothemasfurtherdetailed
intheUsagesection.
• Inference: Rhizomer provides inference capabilities for
datasetswithontologieswithrichclasshierarchiesavailable
throughendpointsthatdonotofferthiscapability.Based
onthedataandontologiestobeexplored,Rhizomerma-
terialisesallinferencesregardingsubclasshierarchiesplus
domainandrangerestrictions.Thematerialiseddataisthen
usedduringtheexplorationso,forinstance,allinstancesof
aclasscanbeexploredtogetherevenifthatinformationis
notcapturedexplicitlyintheoriginaldata.
Theinteractiveexplorationfacilitatedbythecombinationof
allthesefeaturesisusefultodiscoverthestructureofanexisting
dataset,forinstance,toreuseit.Moreover,forusersgenerating
newdatasetswithgraphdata,Rhizomerisalsoavaluabletool
tocheckifthedatastructuresatisfiestheexpectations,including
outliers,missingvalues,orissueswiththerelationshipsamong
items.ThefollowingsubsectionsdetailhowRhizomersupports
eachoftheexplorationtasks.
Overview
Withanoverview,usersgetthefullpictureofthedataset.
Rhizomer automatically generates a word cloud to provide an
overviewofthekindsofthingsinthedataset,asshowninFig.1.
Thisisthedefaultoverviewmechanismbecauseitworkseven
forreallybigdatasetslikeDBpedia,withmorethan100million
statements,asthe300mostcommonclassesaredisplayed.
Foramoreinformativeoverviewthatalsoincludeshowthe
main classes relate among them, there is also the option of a
network representation. In this case, the 30 most instantiated
classes are shown as nodes together with the most frequent
properties connecting them as labelled edges. Fig. 2 shows an
exampleofthenetworkoverview.
Listing1: SPARQLquerytoretrieveallinstantiatedclassesand
theirnumberofinstances.Itexcludesanonymousclasses,those
withoutaURItoidentifythem
1 SELECT ?class (COUNT(DISTINCT ?instance) AS ?
n)
2 WHERE {
3 ?instance a ?class
4 FILTER ( !isBlank(?class) )
5 } GROUP BY ?class
Both overview features are completely data-driven, derived
fromqueryingtheunderlyingdatawithSPARQLquerieslikethe
one shown in Listing 1, being SPARQL the standard for graph
databasequerying[13].Thisapproachfacilitatestheexploration
ofschemalessdata,likethatgeneratedbydirectlytransforming
existingdatatoRDF,ortoverifythattheexploreddataconforms
totheintendedschemasandontologies.
It is also possible to configure the schemas and ontologies
thataccompanythedatatobeexplored,incasetheyareavail-
able.Inthiscase,Rhizomerwillusetheontologiestoretrieve
thelabelsfortheclassesandproperties,somoreuser-friendly
presentationscanbebuilt,basedonlabelsinsteadoffragments
ofthecorrespondingURIs.Futureplansincludeleveragingthe
ontologies,whenavailable,togenerateoverviewsthatmakeuse
ofthehierarchicalorganisationofclassesintheontology,like
Treemaps[14].
Zoom and filter
Afteraclassisselectedfromtheoverview,Rhizomergenerates
afacetedview.Itzoomsinandallowsfilteringofresourcesofthe
chosentypebasedontheirproperties,asshowninFig.3.Aswith
thepreviousstep,thisviewisgeneratedautomatically,drivenby
theunderlyingdataevenifitlacksaschema.Thisfeaturealso
allowsexploringdatathatdoesnotfullycomplywithanexisting
3

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Fig.2. Overviewasanetwork,onlineinteractiveversionhttps://rhizomer.rhizomik.net/datasets/dbpedia-net/network.
Listing2: SPARQLquerytoretrieveallfacetsforclassInsect,
whichcorrespondtothepropertiesusedtodescribeitsinstances.
Theresultincludeshowmanyinstancesuseeachfacetandthe
numberofdifferentvaluesperfacet
1 SELECT ?property (COUNT(?instance) AS ?uses)
(COUNT(DISTINCT ?object) AS ?values)
2 WHERE {
3 ?instance a <http://dbpedia.org/ontology/
Insect> ;
4 ?property ?object
5 } GROUP BY ?property
schemaandhighlightstheseinconsistenciesduringexploration
tohelpusersspotthem.
Forinstance,Listing2showstheSPARQLquerytoretrieveall
facetsforclassInsectinDBpedia.Similarqueriesarealsoused
toimplementtheotherfeaturessupportingtheZoomandFilter
task. More details are available from the RhizomerAPI GitHub
repository.
LikeinthecaseofOverview,Rhizomer’sfeaturessupporting
theZoomandFiltertasksmakeuseoftheontologiesthedatais
basedoniftheyareavailable.Inthiscase,forthemoment,they
arejustusedtoretrieveproperties,rangesandvalueslabels.
Details-on-demand
Afterzoomingandfiltering,theuserarrivesattheresources
of interest. All properties and values are shown for every se-
lectedresource.Userscanalsobrowseresourceslinkeddirectly
orthroughreversefacets,asshowninFig.4.
Regardinglinkedresources,itisalsoimportanttonotethat
Rhizomergoesbeyondtheexplorationofacloseddataset.Ifthe
retrievedgraphdatausesexternalURLsfromwhichadditional
datacanberetrieved,Rhizomeralsobehavesaswhatiscalled
a Linked Data browser [15]. This makes it easy to reuse and
integrateexistingdata.
AnexampleofthisisthereuseoftheURLsidentifyingthe
GameofThronesbooksinDBpedia 1inacustomGameofThrones
dataset.Forinstance,tocaptureinwhichofthebooksagiven
characterappears.InadditiontoexploringthroughRhizomerall
the dataset data, the user can click these URLs for the books
and, transparently, all the data available from these URLs will
be presented to the user. Just like if it was captured in the
custom dataset, but without requiring the dataset creators to
copyorwritethemselvesthedetailsabouteachbook.Andthe
benefitsofLinkedDatadonotendthere,theexplorationprocess
cancontinuebyfollowinglinks,forinstance,thebook’sauthors’
details,detailsabouttheirbirthplace,etc. 2
Architecture
Toprovidethepreviousfunctionalitywhilekeepingagood
UserExperience,Rhizomerisbasedonaclient/serverarchitecture
showninFig.5.Thefrontend,calledRhizomerEye,isbasedonthe
Angularframework,whichprovidesahigherlevelofinteractivity
on the user side as it is based on the Single Page Application
paradigm[16].
On the other hand, the backend, RhizomerAPI, is based on
theSpringframeworkandtakescareoftheresource-intensive
tasksofdealingwiththegraphdatabasesthroughtheirSPARQL
endpoints.ItsAPIisolatesthefrontendfromthegenerationof
the required SPARQL queries to extract the classes or facets
fromtheunderlyinggraphdata.Thisincludestakingcareofthe
particularitiesofsomegraphstores,enrichingquerieswithlabels
in different languages when they are available or caching the
1 DBpediaistheLinkedDataversionofWikipedia,https://dbpedia.org.
2 https://rhizomer.rhizomik.net/datasets/got/dbo:Book
4

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Fig.3. Facetedview,onlineinteractiveversionhttps://tinyurl.com/ycktrcka.
resultsinarelationaldatabasetospeedupfutureinteractions.
ThedocumentationoftheRhizomerAPIisavailableonline. 3
ItisalsoimportanttonotethatRhizomergoesbeyondthe
explorationofdatasetsavailablefromoneormoreSPARQLend-
points.ItisalsopossibletofetchgraphdatafromtheWebifitis
availableasLinkedData.Aspointedoutpreviously,thismakesit
easytoreuseandintegrateexistingdata.
AnotherfeaturesofRhizomer,facilitatedbyitsclient/server
architecture,arethatdeploymentisnottiedtoaparticulargraph
database and is a multiuser tool. Each user can interactively
configurethedatasetstheywanttoexplore.Thisway,anyone
cantryRhizomerbyrequestingauseraccountforanexisting
deployment.Tomakeiteveneasierforuserswithoutsemantic
graphtechnologiesexperience,itisalsopossibletocreategraphs
andloaddataintotheminteractivelythroughRhizomerWebuser
interface.
Usage
ThefirststeptouseRhizomer,afterinstallingbothfrontend
and backend or if using an existing deployment like https://
rhizomer.rhizomik.net,istocreateanewdatasetandconfigure
it.First,inadditiontothedatasetnameandifitcanbeexplored
publiclyorremainsprivate,theusershouldchoosebetween‘‘De-
tailed’’or‘‘Optimized’’exploration.‘‘Detailed’’isrecommended
becauseittakesintoaccountdifferentfacetrangesandenables
3 https://rhizomer-api.rhizomik.net/swagger-ui.html
theNetworkoverview.However,forbigdatasetslikeDBpedia
or to simplify the user experience, it might be better to use
‘‘Optimized’’ exploration, which treats all facets ranges as text
literalsandusedWordCloudtogeneratetheoverview.
The next step in the configuration process is to define the
SPARQLendpointwherethedatatobeexploredislocated.Aform
liketheoneshownontheleftsideofFig.6isusedtodefinethe
kindofSPARQLserver,theURLoftheendpointandifitispass-
wordprotectedorwritable.Inthelattercase,separateendpoint
addressesorcredentialsaresupportedforwriteoperations.Addi-
tionally,itispossibletoenableinferencingfortheexploreddata
basedonthecorrespondingontologies,aspreviouslydetailedfor
theInferencefeatureintheSoftwaredescriptionsection.
The final step of the configuration process is to select the
datagraphsavailablefromtheSPARQLendpointtobeexplored.
It is possible to combine many graphs to explore all of them
together. This is very useful to retain data provenance or to
integrate different data sources. The form used for managing
datasetgraphsisshownontherightsideofFig.6.IftheSPARQL
endpointiswritable,italsoallowsthecreationofnewgraphsin
thecorrespondingendpointandtheloadingofexistingRDFdata
filesintothem.Eachgraphcanbeselectedtobeusedasdatato
beexplored,asasourceforontologicalknowledgeorboth,ifthe
ontologyisalsotobeexplored.Beingabletodefineontologies,
whichshouldbeloadedintothecorrespondinggraph,enables
featureslikeMultilingualSupportorInference.
Oncetheconfigurationiscompleted,theexplorationprocess
startsbygeneratingthecorrespondingOverview.Thismighttake
from just seconds for datasets with thousands of statements
5

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Fig.4. Detailsview,onlineinteractiveversionhttps://rhizomer.rhizomik.net/datasets/dbpedia/dbo:Person/resource?uri=http:%2F%2Fdbpedia.org%2Fresource%2FNikola_
Tesla.
Fig.5. Rhizomer’sarchitecture.
(triples) to some minutes for bigger datasets, with millions of
triples,especiallyifa‘‘Detailed’’explorationisintended.Itwill
largelydependonthedatasetsizeandtheSPARQLendpointper-
formance.Inanycase,thisisdonejustthefirsttimethedatasetis
exploredafterconfiguration.Thedatastructuresrequiredtobuild
theoverviewsarecachedinRhizomerAPI.Thesamehappensfor
classes’facetedviews,theyarecomputedthefirsttimetheyare
requiredandthencached.
Impact
Rhizomerhelpsresearchersdiscoverthestructureofexisting
graphdatasetstheymightbeinterestedinreusing,aslongas
6

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Fig.6. ConfiguringtheSPARQLendpointforadataset(left)andtheendpoint’sgraphstoexploreasdataorontology.
theyareavailableorconvertedintotheRDFstandard.Moreover,
Rhizomer also assists researchers in generating data modelled
asagraphusingRDF.Inthiscase,researchersuseRhizomerto
inspectthedatatheyaregenerating,itsshape,potentialmissing
values,existingoutliers,etc.
WithoutRhizomer,usersinterestedindiscoveringthestruc-
tureofanRDFdatasethavetorelyonSPARQL[13],thestandard
querylanguageforgraphdatabases.However,thisisacumber-
someprocessthatprovidesafragmenteddatasetoverview,made
by the results of each query used to inspect the dataset. For
instance,thelistofmainclassesorthepropertiesusedtodescribe
aparticularclass.
There are other tools that, like Rhizomer, also provide vi-
sual interfaces to explore graph data and hide the particulari-
tiesofSPARQL.However,theirfocusisonhelpingexplorethe
data building easier but not trivial query notations, including
graphical notations like RDF Explorer [17], or through faceted
views combined with a list of all available classes, like RDF
Surveyor[18].
Tothebestofourknowledge,noneofthem,despiteproviding
detailedorfacetedviews,combinebothwithusableoverviews
ofthedatasetlikeawordcloudoranetworkdiagram.Without
them,usersrequiresomeaprioriknowledgeofthedatastructure
toknowwheretostart.Iftheentrypointisasearchformthat
allowslookingforaspecificclassofentitiesinthedataset,for
instance,Insect,theuserneedstoknowwhattotype,evenifthere
is autocomplete assistance. On the other hand, presenting the
listofallavailableclassescanbeoverwhelmingformostusers,
especiallyforbigdatasetsandevenforexperts.
AnotherimportantfeatureofRhizomeristhatitiseasierto
use than most alternatives. Usually, similar tools are deployed
andtiedtoaspecificdataset.End-usersarenotallowedtocon-
figuretheirdatasets.WithRhizomer,theydonotevenneedtheir
deployment.Userscanrequestauseraccountandinteractively
configuretheirdatasetthroughWebforms.
Formoreadvancedusers,itisalsopossibletodeployyour
copyofRhizomer.ThereareprebuiltDockerimagesforboththe
frontendandthebackendavailablefromtheDockerHubpublic
registry:
• RhizomerEye’sDockerimageforthefrontend,ithasmore
than1200pulls(downloads)fromDockerHub. 4
4 https://hub.docker.com/repository/docker/rhizomik/rhizomer-eye
• RhizomerAPI’s Docker image for the backend, more than
1100pullsfromDockerHub. 5
Rhizomeristheresultofmanyyearsofresearchanddevelop-
mentandpromisingresultsalongthispath.In2013,Rhizomer
won the Intelligent Exploration of Semantic Data (IESD) Chal-
lenge.6In2015,RhizomerwontheVIVOLinkedOpenDataCon-
test.7withitsapplicationtofacilitatetheexplorationofscholarly
databasedontheVIVOOntologyandavailableonline 8
Inadditiontotheseprizes,weareawareofthefollowingpast
researchprojectsthatusedRhizomer:
• MediaMixer9 aimwastofacilitatemediareuse.Rhizomer
providedthemeanstoexplorethesemanticdatagenerated
aftermediasegmentationandannotation.
• InVID10targetedthenewsindustry,facilitatingsocialmedia
verificationandreusenegotiationforjournalisticpurposes.
Thereuseconditionsweremodelledusingsemantictech-
nologies and available for system administrators through
Rhizomer.
• MediSys monitors the media for potential plant health
threatsusingknowledgecapturedfromdomainexpertsand
representedusingsemantictechnologies[19].Rhizomerfa-
cilitatedtheinteractionwiththecapturedknowledgewhich
isavailableonline. 11
• TheDiabetesDatasetisanontologythatmodelsthediabetes
domain from an existing open dataset of around 70,000
diabeticpatients[20].Thedatasetispublishedandcanbe
exploredusingRhizomer. 12
• WikidataSubsettingisaprojectthatdealswiththeenor-
moussizeoftheWikidatadataset(about1.5billionstate-
ments) by providing mechanisms to extract subsets [21].
Rhizomerisproposedtoexplorethequalityofthegenerated
subsets,forinstanceforCOVID19-relateddata. 13
5 https://hub.docker.com/repository/docker/rhizomik/rhizomer-api
6 http://imash.leeds.ac.uk/event/2013/challenge.html
7 https://twitter.com/rogargon/status/649162786510086144
8 https://rhizomer.rhizomik.net/datasets/linkedudl
9 https://www.mediamixer.eu
10 https://www.invid-project.eu
11 https://rhizomer.rhizomik.net/datasets/PlantHealthThreats
12 https://rhizomer.rhizomik.net/datasets/diabetes
13 https://rhizomer.rhizomik.net/datasets/covid19
7

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
Additionally,Rhizomerisalsousedforteachingasitmakes
iteasierforstudentstoexploreandinteractwiththedatathat
theygenerate.Forinstance,intheWebofDatasubject,groupsof
studentsdeveloptheirprojectsbasedonsemanticdata.Semantic
technologies facilitate the integration of different data sources
andthefinalresultsaremadeavailablethroughRhizomer.
Regarding commercial projects, Rhizomer has been used in
collaborationwithAmazonWebServicestoillustratethefeatures
oftheirgraphdatabaseoffering,theNeptunedatabase.There-
sultsofthiscollaborationaredetailedinanAWSDatabaseBlog
post.14
Beforethat,Rhizomerwaspromotedincollaborationwiththe
ITServicesandConsultingfirmGFTatCODE_n, 15aglobalcross-
industryinnovationplatformfordigitalpioneers,startups,and
corporations.Additionally,ithasbeenexploredwiththemedia
servicescompanyNueMetatohelpcommunicatetoitsclientsthe
valueofthesemanticdatageneratedforthem[22].
TheongoingresearchprojectsusingRhizomerare:
• ANGLIRU(ApplyingkNowledgeGraphstoresearchdatain-
teroperabiLItyandReUsability)aimstomakeresearchdata
easiertofind,access,integrate,andreusebyusingsemantic
knowledgegraphtechnologies.Onceconvertedintoseman-
ticgraphform,researcherswilluseRhizomertoexplorethe
data.
• UdL Experts is the experts portal used by Universitat de
Lleida to promote the expertise of its researchers. After
mappingandintegratinglegacydataintothesemanticform,
interestedpartiescanuseRhizomertosearchforexperts
andgettoknowtheirresearchtopicsandoutputs. 16
Conclusionsandfuturework
AsdetailedintheImpactsection,Rhizomerhasbeenusedina
widerangeofscenarios,fromresearchorcommercialprojectsto
teaching.Ithasshownitsusefulnesswhenexploringknowledge
graphsavailableassemanticdata.Userscangetboththeoverall
structureandintricaciesofthedataset,eveniftheydonothave
prior knowledge about the dataset at hand or the underlying
semantictechnologies.
Rhizomer’sversatility,beingcapableofexploringdatabothat
theglobalanddetailedlevel,isattainedbyperformingthethree
typicaldataanalysistasks:getanoverview,zoomandfilter,and
details-on-demand.Thesecapabilitiesmakeitusefulforbothdata
reusers,whowanttoknowaboutthereuseopportunitiesofa
givendataset,andforsemanticknowledgegraphcreators,who
cancheckifthegenerateddatasetfollowstheirexpectations.
Futureworkfocusesonincludingadditionalmechanismsfor
data exploration that make use of the underlying ontologies,
like Treemaps [14], or tailored to specific kinds of data, like
chartsfornumericdata,timelinesforchronologicalinformation
ormapsforgeolocatedresources.Additionaleffortsareplanned
to improve the performance of Rhizomer when exploring big
datasets,especiallyinvolvingfeaturesinvolvingtextsearch.To
thisend,Rhizomerisbeingtailoredtothemechanismsprovided
bydifferentSPARQLenginesregardingtextindexing.
Declarationofcompetinginterest
Theauthorsdeclarethattheyhavenoknowncompetingfinan-
cialinterestsorpersonalrelationshipsthatcouldhaveappeared
toinfluencetheworkreportedinthispaper.
14 AWSBlogDatabaseRhizomer
15 https://vimeo.com/60635390
16 https://experts.udl.cat
Dataavailability
AllthedataandcodeisavailablefromGitHubthroughthe
providedlinks.
Acknowledgements
Thisworkwaspartiallysupportedbyproject‘‘ANGRU:Apply-
ingkNowledgeGraphstoresearchdataReUsability’’withrefer-
ence PID2020-117912RB-C22 and funded by MCIN/AEI/
10.13039/501100011033. Additionally, we would like to thank
everyonewhohasparticipatedinthedevelopmentofRhizomer,
anditscurrentorpreviousversions,namely:OriolAguilar,Gil
Grau,JuanManuelGimeno,DavidCastellà,JosepMariaBrunetti,
andJoanManelGiménez.
Illustrativeexamples
ExplanatoryvideosshowinghowRhizomercanbeusedtoex-
ploredifferentsemanticknowledgegraphsareavailablefromht
tps://www.youtube.com/playlist?list=PLJ0YJaEOtqlkgZv7OgI_okB
ttWqTflGDC.
References
[1] Berners-Lee T, Hendler J. Publishing on the Semantic Web. Nature
2001;410(6832):1023–4.
[2] Angrosh M, Cranefield S, Stanger N. Contextual information retrieval in
research articles: Semantic publishing tools for the research community.
SemanticWeb2014;5(4):261–93.
[3] KirchbergM,LeonardiE,TanYS,LinkS,KoRKL,LeeBS.Formalconcept
discovery in Semantic Web Data. In: Domenach F, Ignatov DI, Poel-
mansJ,editors.Formalconceptanalysis.Berlin,Heidelberg:SpringerBerlin
Heidelberg;2012,p.164–79.
[4] Pandat A, Gupta N, Bhise M. Load balanced Semantic aware distributed
RDF graph. In: 25th international database engineering & applications
symposium. New York, NY, USA: Association for Computing Machinery;
2021,p.127–33.http://dx.doi.org/10.1145/3472163.3472167.
[5] PadiyaT,BhiseM,VasaniS,PandeyM.QueryexecutionforRDFdataon
row and column store. In: Natarajan R, Barua G, Patra MR, editors. Dis-
tributedcomputingandinternettechnology.Cham:SpringerInternational
Publishing;2015,p.403–8.
[6] KirraneS,SabouM,FernándezJD,OsborneF,RobinC,BuitelaarP,etal.A
decadeofSemanticWebresearchthroughthelensesofamixedmethods
approach.SemanticWeb2020;11(6):979–1005.
[7] Charalampidis CC, Keramopoulos EA. Semantic Web user interfaces – A
modelandareview.DataKnowlEng2018;115:214–27.http://dx.doi.org/
10.1016/j.datak.2018.04.003.
[8] Pesquita C, Ivanova V, Lohmann S, Lambrix P. A framework to conduct
and report on empirical user studies in Semantic web contexts. In:
Faron Zucker C, Ghidini C, Napoli A, Toussaint Y, editors. Knowledge
engineering and knowledge management. Cham: Springer International
Publishing;2018,p.567–83.
[9] NečaskýM,StenchlákŠtěpán.Interactiveanditerativevisualexplorationof
knowledgegraphsbasedonshareableandreusablevisualconfigurations.
J Web Semant 2022;73:100713. http://dx.doi.org/10.1016/j.websem.2022.
100713.
[10] Tablan V, Bontcheva K, Roberts I, Cunningham H. Mímir: An open-
source Semantic search framework for interactive information seeking
and discovery. J Web Semant 2015;30:52–68. http://dx.doi.org/10.1016/j.
websem.2014.10.002,SemanticSearch.
[11] Hitzler P. A review of the Semantic Web field. Commun ACM
2021;64(2):76–83.
[12] Shneiderman B. The eyes have it: A task by data type taxonomy for
information visualizations. In: Proceedings of the IEEE symposium on
visual languages. Boulder, CO, USA: IEEE; 1996, p. 336–43. http://dx.doi.
org/10.1109/VL.1996.545307.
[13] DuCharmeB.LearningSPARQL:queryingandupdatingwithSPARQL1.1.
2nded..Sebastopol,CA:O’ReillyMedia;2013.
[14] Shneiderman B. Tree visualization with tree-maps: 2-D space-filling
approach. ACM Trans Graph 1992;11(1):92–9. http://dx.doi.org/10.1145/
102377.115768.
[15] HeathT,BizerC.Linkeddata:evolvingthewebintoaglobaldataspace.
1sted..Morgan&ClaypoolPublishers;2011.
8

Roberto García, Juan-Miguel López-Gil and Rosa Gil SoftwareX 20 (2022) 101235
[16] Jadhav MA, Sawant BR, Deshmukh A. Single page application using
AngularJS.IntJComputSciInfTechnol2015;6(3):2876–9.
[17] VargasH,Buil-ArandaC,HoganA,LópezC.RDFexplorer:AvisualSPARQL
query builder. In: Ghidini C, Hartig O, Maleshkova M, Svátek V, Cruz I,
Hogan A, et al., editors. The Semantic Web. Lecture notes in computer
science, Cham: Springer International Publishing; 2019, p. 647–63. http:
//dx.doi.org/10.1007/978-3-030-30793-6_37.
[18] Vega-Gorgojo G, Slaughter L, Von Zernichow BM, Nikolov N, Ro-
man D. Linked data exploration with RDF surveyor. IEEE Access
2019;7:172199–213.http://dx.doi.org/10.1109/ACCESS.2019.2956345.
[19] Alomar O, Batlle A, Brunetti J, García R, Gil R, Granollers A, Jiménez S,
et al. Development and testing of the media monitoring tool MedISys
for early identification and reporting of existing and emerging plant
health threats. EPPO Bull 2015;45(2):288–93. http://dx.doi.org/10.1111/
epp.12209.
[20] SubiratsL,GilR,GarcíaR.PersonalizationofOntologiesVisualization:Use
CaseofDiabetes.In:Alor-HernándezG,Sánchez-CervantesJL,Rodríguez-
González A, Valencia-García R, editors. Current trends in semantic web
technologies: theory and practice. Studies in computational intelligence,
Cham,Switzerland:SpringerInternationalPublishing;2019,p.3–24.http:
//dx.doi.org/10.1007/978-3-030-06149-4_1.
[21] Labra-GayoJE,HeviaAG,ÁlvarezDF,AmmarA,BrickleyD,GrayAJG,etal.
KnowledgegraphsandWikidatasubsetting.Tech.rep.,BioHackrXiv;2021,
http://dx.doi.org/10.37044/osf.io/wu9et.
[22] García R, Sincaglia N. Semantic Web Technologies for User Generated
Content and Digital Distribution Copyright Management. In: Polleres A,
Garcia A, Benjamins R, editors. Proceedings of the industry track at the
international semantic web conference 2014, vol. 1383. Riva del Garda,
Italy:CEURWorkshopProceedings;2014,p.2,URLhttp://ceur-ws.org/Vol-
1383/paper14.pdf.
9
