---
bib_type: inproceedings
cite_key: jardine2014topical
title: 'Topical PageRank: A model of scientific expertise for bibliographic search'
author: Jardine, James and Teufel, Simone
year: '2014'
booktitle: Proceedings of the 14th Conference of the European Chapter of the Association
  for Computational Linguistics
pages: 501--510
autotags: researchers;PUS;blogs;web;digital;social studies of science;literature;review;PAST;conference
file: Jardine2014 - Topical PageRank- A model of scientific expertise for bibliographic
  search.pdf:docs/Jardine2014 - Topical PageRank- A model of scientific expertise
  for bibliographic search.pdf:application/pdf
filename: \\\\Mac\\Home\\Downloads\\CPC-4U\\docs\\Jardine2014 - Topical PageRank-
  A model of scientific expertise for bibliographic search.pdf
keywords: sin localización - P;researchers;PUS;blogs;web;digital;social studies of
  science;literature;review;PAST;conference
Qiqqa: sin localización - P
pdf: '[[CPC4U/PDF/Jardine2014 - Topical PageRank- A model of scientific expertise
  for bibliographic search.pdf]]'
created: '2026-03-24'
---
## Full text (extracted from `CPC4U/Working docs/_pdf_text_24_marzo/Jardine2014 - Topical PageRank- A model of scientific expertise for bibliographic search.txt`)

*Merged:* 2026-03-24 (from pre-extracted text file)

```text
 Topical PageRank: A Model of Scientific Expertise for Bibliographic Search

                                 James Jardine            Simone Teufel
                            Natural Language and Information Processing Group
                                          Computer Laboratory
                                   Cambridge University, CB3 0FD, UK
                                     {jgj29,sht25}@cam.ac.uk



                        Abstract                                 and co-citations (Small, 1978). More recently, cita-
                                                                 tion counts have been shown to improve effective-
      We model scientific expertise as a mixture                 ness of ad-hoc retrieval (Meij and De Rijke, 2007;
      of topics and authority. Authority is calcu-               Fujii, 2007).
      lated based on the network properties of each                 In science, the peer review process ensures that
      topic network. ThemedPageRank, our combi-
                                                                 the right to cite is hard-earned, but on the web, hy-
      nation of LDA-derived topics with PageRank
      differs from previous models in that topics in-            perlinking is infinitely cheap. This means that that
      fluence both the bias and transition probabili-            the authority of webpages cannot simply be approx-
      ties of PageRank. It also incorporates the age             imated as the number of incoming links. Algorith-
      of documents. Our model is general in that                 mically more complex authority such as the random-
      it can be applied to all tasks which require an            surfer model PageRank (Brin and Page, 1998) or the
      estimate of document–document, document–                   authorities/hub based algorithm HITS (Kleinberg,
      query, document–topic and topic–query sim-
                                                                 1998)) have spectacularly improved search results in
      ilarities. We present two evaluations, one
      on the task of restoring the reference lists of            comparison to standard IR models relying on simi-
      10,000 articles, the other on the task of au-              larity calculations based on the words in the text and
      tomatically creating reading lists that mimic              other text-internal informatioh.
      reading lists created by experts. In both eval-               Much recent work in bibliographic search has
      uations, our system beats state-of-the-art, as             been driven by the intuition that what works for the
      well as Google Scholar and Google Search in-
                                                                 web should also work for science, even though ci-
      dexed againt the corpus. Our experiments also
      allow us to quantify the beneficial effect of our
                                                                 tations are more comparable to each other in weight
      two proposed modifications to PageRank.                    than hyperlinks. Case studies comparing PageRank-
                                                                 based authority measures against citation counts
                                                                 alone report some cases where PageRank is supe-
 1 Introduction                                                  rior (Chen et al., 2007; Ma et al., 2008), but exper-
 For search, the presence of links in a document                 imental proof of standard PageRank outperforming
 collection adds valuable information over that con-             citation counts in a large-scale bibliographic search
 tained in the text of the documents alone. Each act             experiment is still outstanding. In at least one such
 of linking can be interpreted as a latent judgement of          experiment, PageRank performed worse than cita-
 authority or trust which is bestowed onto the linked            tion count (Bethard and Jurafsky, 2010).
 documents (Kleinberg, 1998). This makes author-                    Straightforward PageRank calculations, when ap-
 ity an objective measure of how important that pa-              plied to the scientific literature, are hampered by two
 per is to a community who confer that authority.                factors: on the one hand, the progression of time im-
 The citation count is the simplest of these, which              poses a directional structure on the citation network.
 has been used successfully for decades for biblio-              Therefore, PageRank values of older papers are sys-
 metrics (Garfield, 1972) and for mapping out scien-             tematically inflated as PageRank can only ever flow
 tific fields via bibliometric coupling (Kessler, 1963)          from newer to older papers (Walker et al., 2007).




                                                           501
Proceedings of the 14th Conference of the European Chapter of the Association for Computational Linguistics, pages 501–510,
                 Gothenburg, Sweden, April 26-30 2014. c 2014 Association for Computational Linguistics
Secondly, and more interestingly, researchers earn
their expertise in particular, well-defined scientific
fields. We propose that this requires a more fine-
grained notion of specific – not global – expertise.
   Our solution is to use LDA-derived topics (Blei
et al., 2003) as approximations for scientific fields,
and to model the importance of a paper as a mixture
of its relative expertise in each of the topics it cov-
ers. The second aspect of our solution, somewhat
                                                                     Figure 1: A High-level view of LDA.
more mundane but still necessary to adapt PageR-
ank successfully to model scientific expertise, is to
age-taper the resultant estimation.                         ity model for each topic based on a modification
   In this paper, we present ThemedPageRank                 of Personalised PageRank (Page et al., 1998). De-
(TPR), our model of topic-specific scientific exper-        pending on the search need, the input (one or more
tise, which incorporates the two modifications, and         keyword(s) or paper(s)) is converted into a topic dis-
provide evidence that both are necessary for the ad-        tribution, which we then use to linearly combine the
equate application of PageRank-style authority cal-         multiple topic-specific expertise scores of our model
culations to the scientific literature. In two evalua-      into a unique authority score representing the fit be-
tions, our model beats standard PageRank and cita-          tween search need and document.
tion counts by a large margin. Previous models exist           Latent Dirichlet Allocation (LDA) (Blei et al.,
which combine the idea of personalising PageRank            2003) is a Bayesian generative probabilistic model
by topics, but our manipulation of both PageRank’s          for collections of discrete data, which has become
bias and transition probabilities differs from these.       popular for the modelling of scientific text corpora
Our experiments also support the claim of our sys-          (Wei and Croft, 2006; He et al., 2009; Blei and
tem’s superiority over these models.                        Lafferty, 2006). In LDA, a document in the cor-
   We use two tasks to evaluate the system’s per-           pus is modelled and explicitly represented as a fi-
formance. The first is the reintroduction of an ar-         nite mixture over an underlying set of topics, while
ticle’s reference items that have been artificially re-     each topic is modelled as an infinite mixture over
moved. The assumption here is that a good model             the underlying set of words in the corpus. We use
of document–document similarity should be able to           LDA predominantly to produce the latent topics that
guess which articles any given paper would have             form a foundation for the relationships between pa-
cited. The second task is the automatic creation of         pers and technical terms in a corpus.
reading lists, of the kind that an expert might pre-           Technical terms act as the terms in our model
pare for their students. We asked experts to create a       (rather than words), because technical terms are im-
gold standard of such reading lists, and compare our        portant artefacts for formulating knowledge from
system against the current de facto state-of-the-art in     scientific texts (Ananiadou, 1994; Justeson and
such tasks, Google Scholar, and again find that our         Katz, 1995), because descriptions of topics are bet-
system beats it comfortably.                                ter understandable using technical terms rather than
   This article is structured as follows: the next sec-     words (Wallach, 2006; Wang et al., 2007); and to
tion describes our model, which section 3 contrasts         make our model more scalable to large corpora. The
to related work. The evaluations are described in           method we use to find technical terms is light-weight
sections 4 and 5. Section 6 concludes.                      and requires little infrastructure, but does not repre-
                                                            sent state-of-the-art in terminology detection (Lopez
2 Authority Model                                           and Romary, 2010; Wang et al., 2007). We collect
Our model first determines an LDA space (Blei et            all n-grams of words which appear in 2 or more titles
al., 2003) representing the entire document collec-         of all documents in the corpus, filter out all unigrams
tion, which results in a set of topics describing the       appearing in the Scrabble TWL98 word list, then all
entirety of the field. It then calculates an author-        n-grams starting or ending in stop words. To de-




                                                      502
cide whether a subsumed term should be removed                       is referred to by document d′ . The first term in the
if the subsuming term exists (“statistical machine                   transition function ensures that TPR scores are prop-
translation” subsumes both “statistical machine” and                 agated only from citing documents that are highly
“machine translation”), we remove those n-grams                      relevant to topic t. The second term ensures that a
whose frequency is lower than 25% of their subsum-                   larger proportion of a documents TPR score is prop-
ing terms. Finally, only the most frequent 25% of the                agated to cited documents that are highly relevant to
remaining unigrams and bigrams are retained.                         topic t. The value P (t|d) can be read directly from
   We then build a D × V matrix Ω, which con-                        matrix Θ in Fig. 1.
tains the counts of V technical-terms (the columns)                     In a final step, we age-taper TPR by dividing
in each of the D documents (the rows) in Fig. 1. Our                 TPR values by the age of the citation concerned in
own implementation of LDA (with LDA parameters                       years. Experimentally, this achieved the best model
α = β = 0.01) is used to collapse matrix Ω into two                  in comparison to more complex dampening methods
denser, smaller matrices Θ (containing the distribu-                 (e.g., exponential).
tion of documents over topics), and Φ (containing
the distribution of topics over technical-terms).                    3 Related Work
   To model topic-specific expertise in science, we                  Others before us have observed that time effects bias
modify the original PageRank calculation of Page at                  PageRank if applied unmodified to the scientific lit-
al. (1998) by adding a topic dimension to the score                  erature (Walker et al., 2007). Walker et al.’s Cit-
of both the bias and transition probabilities:                       eRank algorithm modifies the bias probabilities of
                                                                     PageRank exponentially with age, favouring more
              T P R(t, d, k + 1) = αB(t, d)                          recent publications.
                     X                                                  We are also not the first to have combined a notion
     +(1 − α)                  T (t, d, d′ )T P R(t, d′ , k)         of topic-specification with Personalised PageRank.
                  d′ ∈li (d)                                         The idea goes back to the original PageRank paper
   where T P R(t, d, k) is the topic-specific PageR-                 by Page et al. (1998), who discuss the personaliza-
ank of topic t for paper d at iteration k; B(t, d) is                tion of PageRank by introducing a bias towards only
the probability that paper d is chosen at random from                a set of trusted web sites W . Page et al. alter only
the corpus, given topic t, and T (t, d, d′ ) is the tran-            the bias probability B, while leaving the transition
sition probability of reaching page d from page d′ ,                 probabilities T unchanged from global PageRank:
given topic t. In our formula, the transition proba-                                        (
                                                                                                 1
bility T (t, d, d′ ) takes into account the probabilities                                       |W |    if d ∈ W
                                                                                B(t, d) =
of topic t not only in documents d and d′ , but also in                                         0       if d ∈
                                                                                                             /W
the other documents d′′ referenced by document d′ :
                                                                                                           1
                                                                                     T (t, d, d′ ) =
                             P (t|d)                                                                   |lo (d′ )|
               B(t, d) = P            ∗
                          d∗ ∈D P (t|d )                                Richardson and Domingos (2002) first used
                                                                     PageRank personalisation for specialisation at
                 s                                                   search time. For query q with corresponding topic
 ∗        ′               P (t|d′ )          P (t|d)
T (t, d, d ) =       P              ∗)
                                       P                   ′′        t = q, they use the relevance of document d to query
                         ∗
                        d ∈D  P (t|d     d ∈lo (d′ ) P (t|d )
                                          ′′
                                                                     q as a bias. Haveliwalla (2003) calculates a Person-
                                                                     alised PageRank for each of a set of 16 manually
                                     T ∗ (t, d, d′ )                 created topics t comprised of several documents by
        T (t, d, d′ ) = P                     ∗       ∗              altering only the Bias term B, using Page et al.’s for-
                                 d∗ ∈li (d) T (t, d, d )
                                                                     mula above. This solution avoids the computational
   Here d is a document whose TPR is being calcu-                    scalability problem with Richardson and Domingos’
lated, d′ is a document that refers to document d and                approach, but is limited in applicability by requiring
whose TPR score is being distributed during this it-                 predefined topics. Several researchers followed Brin
eration of the algorithm, and d′′ is a document that                 and Page and Haveliwala in altering only the bias




                                                               503
probabilities, including Wu et al. (2006) and Gori               T (t, d, d′ ) = γTs t (t, d, d′ ) + (1 − γ)To t (t, d, d′ )
and Pucci (2006).
                                                                                                                 1
   In contrast, Narayan et al. (2003) and Pal and                        Ts t (t, d, d′ ) = P (d|d′ , t) ∼
                                                                                                         =
                                                                                                             |lo (d′ )|
Narayan (2005) propose a model of personalisation
that alters the transition probabilities instead of the             where T is the number of LDA topics, P (t|d) is a
bias probabilities. Under their model, the transition            probability of topic t given document d, which can
probability T (t, d) is proportional to the number of            be read directly from the generated LDA probabili-
words in document d that are strongly present in the             ties, Ts t is the probability of arriving at page d from
documents contained in topic t. Nie et al. (2006)                other pages in the same topic context, whereas To t
produce a more computationally scalable version of               treats the case of arriving at a different topic. Like
the ideas presented in Pal and Narayan (2005) by as-             Nie et al., they achieve best results with γ = 1, so
sociating a context vector with each document, with              they ultimately only use bias probabilities, like the
a fixed set of topics (12 in their case), for which they         models discussed above. Crucially, their decision
learn these context vectors using a naive Bayes clas-            that P (d|d′ , t) does not to involve any of the LDA
sifier. They then provide the possibility to alter both          topic distributions is surprising. Under their model,
the bias and transition probabilities of each webpage            as in ours, when the reader randomly jumps to a new
as follows:                                                      paper, they will tend to favour papers that are closely
                                1                                associated with the topic. However, when they fol-
                 B(t, d) =        Ct (d)                         low a citation in Yang et. al’s model, one is picked
                                D
                                                                 with equal probability. In contrast, our model imple-
                           1               X Ct′ (d′ )
   T (t, d, d′ ) = γ         ′
                                 + (1 − γ)                       ments the obvious intuition that if one follows cita-
                       |lo (d )|                 l (d′ )
                                          t′ 6=t o               tions, one should also favour those that are closely
                                                                 associated with the topic.
   where Ct (d) is the context vector score for topic
                                                                    Let us now turn to the task of reference list rein-
t associated with document d; the first term in
                                                                 troduction (RLR), i.e., the prediction of which pa-
T (t, d, d′ ) corresponds to the probability of arriving
                                                                 pers a target papers originally cited, given only some
at page d from other pages in the same topic con-
                                                                 information about the paper which stands in as a
text; the second term is the probability of arriving at
                                                                 search need – either its abstract, author names and
page d from other pages in a different context; and
                                                                 other bibliometric information, and/or the full text of
γ is a factor that weights the influence of same-topic
                                                                 a paper (with citation information redacted). Evalu-
jumps over other-topic jumps. Their results suggest
                                                                 ation of a search model by RLR is cheap because of
that γ should be close to 1, indicating that distribut-
                                                                 the readily available gold standard, and it thus allows
ing PageRank within topics generates better Person-
                                                                 for experiments with large data sets.
alised PageRank scores.
                                                                    State-of-the-art solutions to RLR combine lexical
   Other than the fact that they treat bias and transi-
                                                                 similarity (often via topic models), measures of au-
tion probabilities differently to how we treat them,
                                                                 thority over a citation graph, and information about
all personalisation methods discussed up to now
                                                                 social constructs and historic patterns of citation be-
have the disadvantage that they rely on a fixed list
                                                                 haviour. Strohman et al. (2007) perform RLR with
of manually selected topics, whereas our method of-
                                                                 the paper text as a query to their recommendation
fers adaptive specialisation to corpus or domain.
                                                                 system, using text similarity, citation counts, cita-
   The previous work closest to ours is Yang et al.
                                                                 tion coupling, author information, and the citation
(2009), who were the first to use LDA to automat-
                                                                 graph. Their model achieves a mean-average pre-
ically discover abstract topic distributions in a cor-
                                                                 cision of 0.102 against a corpus from the Rexa10
pus of scientific articles, and to combine them with
                                                                 database. Bethard and Jurafsky (2010) improve on
Pagerank by – in principle – altering both the bias
                                                                 Strohman et al. by the use of a SVM with 19 fea-
and transition probabilities according to the follow-
                                                                 tures from 6 broad categories: similar terms; cited
ing model:
                              1                                  by others; recency; cited using similar terms; simi-
                   B(t, d) = P (t|d)                             lar topics; and social habits. They achieve a MAP of
                              D



                                                           504
0.279 against the ACL Anthology Reference Corpus            follow for several reasons. Firstly, such models only
(Bird et al., 2008), with the following features per-       work for papers and citations that were present dur-
forming best: publication age, citation counts, the         ing the learning stage, and there is no mechanism
terms in citation sentences, and the LDA topics of          for predicting influential citations for topics in gen-
the citing documents. They also use (unchanged)             eral, or for combinations of topics. The tight cou-
PageRank authority counts as one of the features,           pling might also result in overlooking some author-
but find that it provides little discriminative power       ities, namely those that are authoritative across sev-
to the SVM. A drawback of their method is the large         eral topics, which will be penalised via low joint
amount of information that has to be provided to            distribution probabilities in combined methods be-
create their SVM features, and the expensive train-         cause of the division of the probabilities across sev-
ing routine, which is based on pairwise paper–paper         eral topics. Secondly, and more disturbingly, such
comparisons in the corpus.                                  models will not locate topics that lack an authority
   Variations of the RLR tasks exist, which addi-           because the authority component of the joint distri-
tionally determine the position in the text of a pa-        bution will be near-zero. This rules out niches in
per where each recommended citation should occur            a corpus where papers are equally relevant to each
(Tang and Zhang, 2009; He et al., 2011; Lu, 2011), a        other, or where the niches are so young that they do
task which is typically solved by comparing a mov-          not yet have an established citation network. There
ing window in the query paper against millions of           is also a scalability issue with joint models of top-
previously located citation contexts with. The draw-        ics and citations. The evaluation data used in cou-
back of this technique in contrast to ours is the fact      pled models is generally small, with the number of
that new papers, which have not collected sufficient        papers ranging under around 2,000, the number of
contexts in the literature, are severely disadvantaged      citations ranging under 10,000, and the number of
and will never be recommended.                              topics in their models ranging from eight to twenty.
   We first create topics and then apply PageRank           But LDA has been shown to scale to corpora of mil-
to find expertise within topical networks. It is how-       lions of terms (Newman et al., 2006), and PageRank
ever also possible to simultaneously model citations        to billions (Page et al., 1998) of documents. Our
and terms (Cohn and Hofmann, 2001; Mann et al.,             model, which advocates a pipelined approach, ben-
2006). Such models are not normally directly com-           efits from the fact that separate topic modelling is
parable to ours; for instance Bharat and Henzinger’s        computationally tractable using LDA, and the fact
(1998) model, a modified version of HITS (Klein-            that citation graph modelling is cheap using Person-
berg, 1998), is query-specific.                             alised PageRank.
   There are numerous extensions to LDA that incor-
porate external information in addition to the lex-         4 Evaluation 1: RLR
ical information inside the documents in a corpus,          We evaluate our authority-based search model us-
via author-topic models and models of publication           ing the 2010 ACL Anthology Network (Radev et al.,
venues (Steyvers and Griffiths, 2007; Rosen-Zvi et          2009). We removed from it corrupted documents,
al., 2010; Tang et al., 2008). Erosheva et al. (2004)       i.e., those of less than 100 characters or contain-
model a corpus using a multinomial distribution si-         ing only control characters. The ACL Anthology
multaneously over the citations and terms in each           Network provides external meta-data about the ar-
document. Topics (which they call aspects) are as-          ticles, which was manually curated. We do not use
sociated with a list of the most likely words (inter-       this meta-data because we wanted to build as system
pretable as topics) and citations (interpretable as au-     that can be applied to any large collection of arti-
thorities) in that aspect. Extensions of the model ex-      cles, where external meta-data would not normally
ist (Nallapati and Cohen, 2008; Gruber et al., 2007;        exist. We therefore build an approximate citation
Chang and Blei, 2010; Kataria et al., 2010; Dietz et        graph from the paper text itself, as a one-off task
al., 2007).                                                 when constructing the LDA space. We extract titles,
   We avoid the tight coupling of topic discovery and       dates and full-text from every article and perform a
citation modeling that the above-mentioned works            search of each articles title in the full-text of all other




                                                      505
       Model                              MAP                 (TPR). For these tests, we use the entire corpus of
           800 test papers, as in B&J (2010)                  10,000 papers with more than 5 citations. Over the
       B&J; best model                    0.287               baseline (A), n-gram-frequency-inverse-document-
       TPR-NoDB                           0.264
                                                              frequency (NFIDF), both citation counts (B) and
       TPR-NoAge                          0.267
       TPR                                0.302               global PageRank (C) make a small improvement.
                   10,000 test papers                         Global LDA similarity scores (D) fare little better.
       A: NFIDF Cosine                    0.062                  As the performance of the full model (G;
       B: NFIDF + citation count          0.092               MAP=0.268) shows, the inclusion of topic models
       C: NFIDF + global PageRank         0.099               lead to a large improvement over any of the above.
       D: NFIDF LDA (KL divergence) 0.115                     This is, as far as we are aware, the first time that a
       E: TPR-NoDB                        0.233               large-scale evaluation that finds significant improve-
       F: TPR-NoAge                       0.242
                                                              ments of a PageRank implementation over citation
       G: TPR                             0.268
                                                              counts in scientific search.
                 Figure 2: RLR results                           We next consider our two modifications, age-
                                                              adjusting (E) and double-biasing (F), in isolation.
                                                              We use two versions of our system where we
articles (i.e., under the assumption that the reference       switched off age-tapering and double-biasing (ie.,
list is the (only) place where we will find such titles).     we only work with a change in the bias probabili-
   Our system generates the RLR output (the recom-            ties, as do Nie etal. (2006), Havaliwala (2003) (al-
mended articles) for an article d by extracting tech-         though their models do not include automatically
nical terms as described in section 2, examining the          generated topics) and Yang et al. (2009)). Our
topic distribution for that article θd,t (i.e. a θi in        model comfortably outperforms TPR-NoDB in both
Fig. 1). We use the topic distribution of article d in        the 800 and 10,000 paper experiment. Similarly,
place to generate the unique age-adjusted TPR tai-            the effect of age-tapering alone can be seen from
lored to the article, T P R(d, d′ ). The 100 articles         the performance of TPR-NoAge (our model with-
d′ with the highest ThemedPageRanks are recom-                out age-adjusting), in the difference between 0.267
mend as citations for article d. Results are reported         and 0.302 and that between 0.242 and 0.268 (signif-
as mean average precision (MAP) of these 100 doc-             icant at 99%). This confirms our claim that a topic-
uments against the actual citations in the article.           specific age-tapered PageRank is superior to global
   We first compare our model to the state-of-the-            PageRank in scientific citation networks.
art (Bethard and Jurafsky, 2010). We emulate their
experimental setup by including only the pre-2004             5 Evaluation 2: Reading Lists
articles in the corpus and testing only on the roughly        The aim of the second experiment is to test our
800 2005/6 articles with more than 5 intra-corpus             model against a much cleaner, albeit smaller gold
citations in their reference list, for which we have          standard: on the task of reconstructing the mate-
per-paper average precision scores. The top part of           rial of expert-created reading lists. We compare our
Fig. 2 shows that our model (MAP=0.302) outper-               system’s performance to three standard, commonly
forms their best model (MAP=0.287; difference at              used search engines: Lucene TFIDF, the Google-
5% confidence with Wilcoxon Ranked Squares test),             indexed ACL Anthology, and Google Scholar. We
despite our model being a general, light-weight IR            chose Google-index and Google Scholar because
system, which relies on LDA and PageRank alone,               they represent commonly used state-of-the-art com-
and theirs is a specialised state-of-the art system,          mercial search engines, and the Google-index is
which relies on heavy-weight machine learning and             what is currently offered as the standard ACL An-
on additional sociological features.                          thology search tool. In contrast, Lucene TFIDF
   The lower part of Fig. 2 compares the influence            was chosen to represent an easy-to-interpret, repro-
of citation count, global PageRank, topic similar-            ducible, out-of-the-box baseline implementing the
ity, and combinations of topic similarity with ci-            simplest kind of lexical similarity search without
tation counts or global PageRank, and our model               any notion of authority. Of the three search engines,




                                                        506
we would predict Google Scholar to be the tough-             Lucene.NET v2.9.2 and indexed our 2010 snapshot
est competitor to TPR, because it uses citation in-          of the ACL Anthology using standard Lucene pa-
formation directly and it is reasonable to expect that       rameters for the TFIDF model. For the Google-
the Google Scholar algorithm employs some domain             indexed ACL Anthology (AAN), we use the in-
adaptation to the scientific domain.                         terface provided on the ACL Anthology website.
   We created gold standard expert-written reading           In order to provide an identical search ground, we
lists using the following protocol. Eight experts            automatically exclude from the return lists papers
were recruited from the computational linguistics            added after the creation of the AAN snapshot. For
groups of two universities (3 from one, 5 from the           Google Scholar (GS), we use the interface provided
other). All experts had a PhD in computational lin-          at scholar.google.com, and parse returns to ex-
guistics and several years of research experience.           clude non-AAN material semi-automatically. In
They were asked to choose a subject for an (imag-            the case of Google Scholar, we restrict the search
inary or existing) reading list for an MPhil student,        ground to the ACL Anthology by filtering the top
concerning an area in which they know the litera-            200 return sets (which may lead to fewer than 20
ture well. We purposefully did not give them guid-           papers returned).
ance as to the size of the reading list as we wanted            We report FCSC, RCSC and F-score for each al-
to observe how experts create reading lists. During          gorithm. FCSC and RCSC are new metrics which
the interview, the experimenter documented the final         address the problem that F-score, being binary, does
list chosen by the expert and made sure all papers           not support the notion of a “close hit”, combined
chosen were present in the 2010 version of the ACL           with the fact that we require a fine-grained compari-
Anthology Network.                                           son of the quality of different systems retrieved lists
   This procedure resulted in reading lists of the fol-      despite the small size of our gold standard. Cita-
lowing topics and sizes: statistical parsing (22 pa-         tion Substitution Coefficient (FCSC), a new metric
pers); parser evaluation (4); distributional semantics       for RLR, gives higher scores to papers closely re-
(14); domain adaptation for parsing (11); informa-           lated to the target papers by citation distance. The
tion extraction (9); lexical semantics (14); statistical     FCSC of each expert paper is the inverse of the num-
machine translation models (5); and concept-to-text          ber of nodes in the minimal citation graph connect-
generation (16).                                             ing each expert paper to any system-retrieved pa-
   In our retrieval model, which topic distribution is       per (thus ranging between 0 and 1; non-connected
chosen for a query depends on whether the query is           expert papers receive a zero score). We also in-
an exact match to one of the technical terms found           troduce Reverse Citation Substitution Coefficient
by our model. If it is, then the topic distribution          (RCSC), which measures the inverse of the num-
of the technical term is used directly as the query          ber of nodes in the minimal citation graph connect-
topic distribution θq, t (i.e. a transposed renormal-        ing each system-retrieved paper to any expert pa-
ized ψ in Fig. 1). If not, we perform a keyword-             per. RCSC makes sure that systems cannot simply
based search (using Lucene TFIDF), and use the av-           increase their FCSC values by returning many ir-
erage topic distribution of the top 20 documents re-         relevant papers. RCSC thus corresponds to preci-
turned as the query topic distribution (i.e. several θi      sion, while FCSC corresponds to recall. The sys-
in Fig. 1). The query topic distribution is then used        tem RCSC and FCSC scores we report are the av-
to linearly combine the topic-specific TPRs into a           erage scores of all the system-retrieved and expert
unique TPR tailored to the query. The 20 documents           papers, respectively. Reporting both scores gives a
with the highest TPR are recommended.                        good overall picture of system performance, partic-
   The three baselines are used as follows in the            ularly when read together with the F-score.
experiment: The experiment is performed by issu-                Fig. 3 shows that our model comfortably beats the
ing the topic of the reading list (exactly as given          competitor systems according to all metrics. In par-
to us by the experts) as a key-word based query to           ticular, our model > GS/AAN > Lucene TFIDF1 .
each system and recording the top 20 resulting pa-
                                                                1
pers answers. For Lucene TFIDF, we downloaded                       For FCSC, the differences are statistically significant at




                                                       507
                           FCSC       RCSC        F-score                                              FCSC       RCSC
      AAN/Google           0.527      0.317       0.117                               TF-CC            0.419      0.359
      GS                   0.519      0.364       0.112                               TF-CC-A          0.491      0.442
      Lucene TFIDF         0.412      0.330       0.040                               TF-PR            0.450      0.360
      TPR                  0.563      0.456       0.128                               TF-PR-A          0.512      0.407
                                                                                      TPR-NoDB         0.541      0.440
        Figure 3: Reading List Creation: Results.                                     TPR-NoAge        0.526      0.436

Concerning simpler methods of estimating author-                          Figure 4: Citation counts and PageRank variants.
ity, Fig. 4 shows that a multiplication of TFIDF
by citation count (as Fujii (2007) does) results in a                  adequately cater for the highly specialised situation
FCSC/RCSC of 0.419/0.359 (reported as TF-CC),                          we encounter in science. The modification we sug-
and age-tapering of citation-count by dividing the                     gest are to use LDA-derived topics (Blei et al., 2003)
citation count by the age of the paper in years                        as approximations for scientific fields, to calculate
(reported as TF-CC-A) results in FCSC/RCSC of                          authority in a topic-specific way, and to age-taper
0.491/0.442. We again compare different versions                       the authority scores. We present formulae where
of PageRank. Global PageRank can be built into                         topics personalise both the bias and the transition
the system by simple multiplication of PR scores                       probabilities. This results in a general IR model
as above, with and without age-tapering (reported                      for science incorporating a robust notion of author-
as TF-PR and TF-PR-A, respectively). We observe                        ity. Our implementation requires only minimal re-
a similar effect to the one reported by Bethard and                    sources and relies only on LDA and PageRank cal-
Jurafsky and seen in experiment 1, namely that                         culation, which means that it is efficient during train-
global PageRank only performs similar to citation                      ing, retraining and at search time.
counts (0.450/0.360 vs 0.419/0.359). With respect                         We perform two evaluations.            In both, our
to double-biasing and age-tapering we see the same                     model significantly outperforms not only state-
effect as in experiment 22 . In fact, we can see from                  of-the-art, but also standard PageRank, non-age-
these results that global PageRank barely improves                     tapered (but topical) PageRank, and non-topical (but
over standard TFIDF, while age-tapering even with-                     age-tapered) PageRank. Our model achieves its
out topics already brings quite some improvement.                      competitive performance by using only the raw text
Overall, these results confirms our claim of the su-                   and citation links. It requires no external informa-
periority of a topic-specific PageRank over global                     tion, neither explicit sociological information such
PageRank in scientific citation networks.                              as past collaborations between authors, nor the ex-
                                                                       pertise and cooperation of like-minded readers, as
6 Conclusions                                                          collaborative models do. While successful applica-
                                                                       tions of collaborative filtering to bibliometric search
We present here the first experiments that pinpoint
                                                                       are rife (Goldberg et al., 2001; Agarwal et al., 2005;
which modifications to PageRank are necessary to
                                                                       McNee et al., 2006; Torres et al., 2004), including
99% confidence via a two-tailed Wilcoxon Signed Ranks test,            to reading list generation (Ekstrand et al., 2010), we
except that between GS and AAN (for which the confidence in-           wanted an entirely independent authority-based IR
terval is only 96%) and that between Lucene and AAN, where             model similarity. CF also suffers from a cold-start
it is 98%. Non-parametric paired tests such as the Wilcoxon
Signed Ranks test can be used on FCSC, but not on RCSC,                phenomenon, where recommendations are generally
as there are different sets of underlying system-retrieved pa-         poor where data is sparse, and has to wait for papers
pers in each case. For RCSC, differences between our model             to be rated by a large number of authors (rather than
and all others at 99% confidence interval, between GS and              cited) before it can rank them.
AAN/Lucene TFIDF at the 95% interval. F-score is reported
for completeness.
                                                                          Should the reader wish to evaluate the perfor-
     2
       Wilcoxon Signed Rank test found all differences significant     mance of TPR on their own PDF papers, it has been
at the 99% level, except that between TF-PR and Lucene TFIDF           incorporated into the Qiqqa reference management
(significant only at the 90% level), and the following equiva-         software 3 .
lences: Lucene TFIDF = TF-CC; TF-PR = TF-CC; TF-CC-A =
                                                                          3
TF-PR-A; TF-CC-A = TF-PR.                                                     Available at http://www.qiqqa.com




                                                                 508
References                                                        of the 24th international conference on Machine learn-
                                                                  ing, page 240. ACM.
N. Agarwal, E. Haque, H. Liu, and L. Parsons. 2005. Re-
   search paper recommender systems: A subspace clus-          M.D. Ekstrand, P. Kannan, J.A. Stemper, J.T. Butler,
   tering approach. Advances in Web-Age Information               J.A. Konstan, and J.T. Riedl. 2010. Automatically
   Management.                                                    building research reading lists. In Proceedings of
                                                                  the fourth ACM conference on Recommender systems,
S. Ananiadou. 1994. A methodology for automatic term
                                                                  pages 159–166. ACM.
   recognition. In Proceedings of COLING.
S.K. Pal B. Narayan, C. Murthy. 2003. Topic continu-           E. Erosheva, S. Fienberg, and J. Lafferty. 2004. Mixed-
   ity for web document categorization and ranking. In            membership models of scientific publications. Pro-
   IEEE/WIC International Conference on Web Intelli-              ceedings of the National Academy of Sciences of the
   gence.                                                         United States of America, 101(Suppl 1):5220.
B.D. Davison B. Wu, V. Goel. 2006. Topical trustrank:          A. Fujii. 2007. Enhancing patent retrieval by citation
   Using topicality to combat web spam. In Proceedings            analysis. In Proceedings of SIGIR.
   of the 15th international conference on World Wide          E. Garfield. 1972. Citation analysis as a tool in jour-
   Web.                                                           nal evaluation. American Association for the Advance-
S. Bethard and D. Jurafsky. 2010. Who should i cite:              ment of Science.
   learning literature search models from citation behav-      K. Goldberg, T. Roeder, D. Gupta, and C. Perkins. 2001.
   ior. In Proceedings of the 19th ACM International              Eigentaste: A constant time collaborative filtering al-
   Conference on Information and Knowledge Manage-                gorithm. Information Retrieval, 4(2):133–151.
   ment.                                                       M. Gori and A. Pucci. 2006. Research paper rec-
K. Bharat and M.R. Henzinger. 1998. Improved algo-                ommender systems: A random-walk based approach.
   rithms for topic distillation in a hyperlinked environ-        IEEE Computer Society.
   ment. In Proceedings of SIGIR.                              A. Gruber, M. Rosen-Zvi, and Y. Weiss. 2007. Hidden
S. Bird, R. Dale, B.J. Dorr, B. Gibson, M.T. Joseph, M.Y.         topic markov models. In Proceedings of AISTATS.
   Kan, D. Lee, B. Powley, D.R. Radev, and Y.F. Tan.
                                                               T.H. Haveliwala. 2003. Topic-sensitive pagerank: A
   2008. The ACL anthology reference corpus: A ref-
                                                                  context-sensitive ranking algorithm for web search.
   erence dataset for bibliographic research in computa-
                                                                  IEEE transactions on knowledge and data engineer-
   tional linguistics. In Proc. of LREC08.
                                                                  ing, pages 784–796.
D.M. Blei and J.D. Lafferty. 2006. Correlated Topic
                                                               Q. He, B. Chen, J. Pei, B. Qiu, P. Mitra, and L. Giles.
   Models. In Advances in Neural Information Process-
                                                                  2009. Detecting topic evolution in scientific literature:
   ing Systems 18: Proceedings of the 2005 Conference,
                                                                  how can citations help? In Proceeding of the 18th
   page 147. Citeseer.
                                                                  ACM conference on Information and knowledge man-
D.M. Blei, A.Y. Ng, and M.I. Jordan. 2003. Latent
                                                                  agement.
   dirichlet allocation. The Journal of Machine Learning
   Research, 3:993–1022.                                       Q. He, D. Kifer, J. Pei, P. Mitra, and C.L. Giles. 2011.
J. Boyd-Graber, D. Blei, and X. Zhu. 2007. A topic                Citation recommendation without author supervision.
   model for word sense disambiguation. In Proceedings            In Proceedings of the fourth ACM international con-
   of EMNLP-CoNLL, pages 1024–1033.                               ference on Web search and data mining.
S. Brin and L. Page. 1998. The anatomy of a large-scale        J.S. Justeson and S.M. Katz. 1995. Technical terminol-
   hypertextual web search engine. In Proceedings of the          ogy: some linguistic properties and an algorithm for
   7th International World Wide Web Conference.                   identification in text. Natural Language Engineering,
J. Chang and D.M. Blei. 2010. Hierarchical relational             1(01):9–27.
   models for document networks. The Annals of Applied         S. Kataria, P. Mitra, and S. Bhatia. 2010. Utilizing Con-
   Statistics, 4(1):124–150.                                      text in Generative Bayesian Models for Linked Cor-
P. Chen, H. Xie, S. Maslov, and S. Redner. 2007. Find-            pus. In Proceedings of AAAI.
   ing scientific gems with google’s pagerank algorithm.       M.M. Kessler. 1963. Bibliographic coupling be-
   Journal of Infometrics, 1(1):8–15.                             tween scientific papers. American Documentation,
D. Cohn and T. Hofmann. 2001. The missing link-a                  14(1):10–25.
   probabilistic model of document content and hypertext       J. Kleinberg. 1998. Authoritative sources in a hy-
   connectivity. Advances in neural information process-          perlinked environment. In Proceedings of the 9th
   ing systems, pages 430–436.                                    ACM-SIAM Symposium on Discrete Algorithms. Also
L. Dietz, S. Bickel, and T. Scheffer. 2007. Unsuper-              available from http://www.cs.cornell.edu/
   vised prediction of citation influences. In Proceedings        home/kleinber/.




                                                         509
P. Lopez and L. Romary. 2010. HUMB: Automatic Key               and W. Kintsch, editors, Handbook of latent semantic
   Term Extraction from Scientific Articles in GROBID.          analysis, page 427. Erlbaum, Hillsdale, NJ.
   In SemEval 2010 Workshop.                                 T. Strohman, W.B. Croft, and D. Jensen. 2007. Recom-
Y. et al. Lu. 2011. Recommending citations with transla-        mending citations for academic papers. In Proceed-
   tion model. In Proceedings of the 20th ACM interna-          ings of SIGIR.
   tional conference on Information and knowledge man-       J. Tang and J. Zhang. 2009. A discriminative approach
   agement.                                                     to Topic-Based citation recommendation. Advances in
N. Ma, J. Guan, and Y. Zhao. 2008. Bringing pagerank            Knowledge Discovery and Data Mining.
   to the citation analysis. Information Processing and      J. Tang, R. Jin, and J. Zhang. 2008. A topic model-
   Management, 44(2):800–810.                                   ing approach and its integration into the random walk
G.S. Mann, D. Mimno, and A. McCallum. 2006. Biblio-             framework for academic search. In Eighth IEEE Inter-
   metric impact measures leveraging topic analysis. In         national Conference on Data Mining.
   Proceedings of the 6th ACM/IEEE-CS joint conference       R. Torres, S.M. McNee, M. Abel, J.A. Konstan, and
   on Digital libraries.                                        J. Riedl. 2004. Enhancing digital libraries with Tech-
S.M. McNee, J. Riedl, and J.A. Konstan. 2006. Mak-              Lens+. In Proceedings of the 4th ACM/IEEE-CS joint
   ing recommendations better: an analytic model for            conference on Digital libraries.
   human-recommender interaction. In CHI’06 extended         D. Walker, H. Xie, K.K. Yan, and S. Maslov. 2007.
   abstracts on Human factors in computing systems.             Ranking scientific publications using a model of net-
E. Meij and M. De Rijke. 2007. Using prior information          work traffic. Journal of Statistical Mechanics: Theory
   derived from citations in literature search. In Large        and Experiment, 2007:P06010.
   Scale Semantic Access to Content (Text, Image, Video,     H.M. Wallach. 2006. Topic modeling: beyond bag-of-
   and Sound).                                                  words (powerpoint). In Proceedings of the 23rd inter-
R. Nallapati and W. Cohen. 2008. Link-plsa-lda: A new           national conference on Machine learning.
   unsupervised model for topics and influence of blogs.     X. Wang, A. McCallum, and X. Wei. 2007. Topical n-
   In International Conference for Weblogs and Social           grams: Phrase and topic discovery, with an applica-
   Media.                                                       tion to information retrieval. In Proceedings of the 7th
D. Newman, P. Smyth, and M. Steyvers. 2006. Scalable            IEEE international conference on data mining.
   Parallel Topic Models. Journal of Intelligence Com-       X. Wei and W.B. Croft. 2006. LDA-based document
   munity Research and Development.                             models for ad-hoc retrieval. In Proceedings of SIGIR.
L. Nie, B.D. Davison, and X. Qi. 2006. Topical link          W. Wong, W. Liu, and M. Bennamoun. 2009. A proba-
   analysis for web search. In Proceedings of SIGIR.            bilistic framework for automatic term recognition. In-
L. Page, S. Brin, R. Motwani, and T. Winograd. 1998.            telligent Data Analysis, 13(4):499–539.
   The pagerank citation ranking: Bringing order to the      Z. Yang, J. Tang, J. Zhang, J. Li, and B. Gao. 2009.
   web. Stanford Digital Library Technologies Project.          Topic-level random walk through probabilistic model.
D.R. Radev, P. Muthukrishnan, and V. Qazvinian. 2009.           Advances in Data and Web Management.
   The ACL Anthology Network Corpus. In Proceed-             D. Zhou, S. Zhu, K. Yu, X. Song, B.L. Tseng, H. Zha, and
   ings, ACL Workshop on NLP and IR for Digital Li-             C.L. Giles. 2008. Learning multiple graphs for doc-
   braries, Singapore.                                          ument recommendations. In Proceeding of the 17th
M. Richardson and P Domingos. 2002. The intelligent             international conference on World Wide Web.
   surfer: Probabilistic combination of link and content
   information in pagerank. Advances in neural informa-
   tion processing systems, 14:1441–1448.
M. Rosen-Zvi, C. Chemudugunta, T. Griffiths, P. Smyth,
   and M. Steyvers. 2010. Learning author-topic models
   from text corpora. ACM Transactions on Information
   Systems (TOIS), 28(1):1–38.
B. Narayan S.K. Pal. 2005. A web surfer model incorpo-
   rating topic continuity. IEEE Transactions on Knowl-
   edge and Data Engineering, 17:726729.
H.G. Small. 1978. Cited documents as concept symbols.
   Social Studies of Science, 8:327–340.
M. Steyvers and T. Griffiths. 2007. Probabilistic topic
   models. In T. Landauer, D. S. McNamara, S. Dennis,




                                                       510
```
