---
title: How do authors select keywords? A preliminary study of author keyword selection behavior
source: https://www.sciencedirect.com/science/article/pii/S1751157720300134?pes=vor&utm_source=scopus&getft_integrator=scopus
author: 
published: 
created: 2025-04-11
description: Author keywords for scientific literature are terms selected and created by authors. Although most studies have focused on how to apply author keyword…
tags:
  - research_method
  - bibliometrics/KW
---
- [View **PDF**](https://www.sciencedirect.com/science/article/pii/S1751157720300134/pdfft?md5=6bdc43c3d7f970e3a355f7cd76f84e70&pid=1-s2.0-S1751157720300134-main.pdf)

## Journal of Informetrics

[Volume 14, Issue 4](https://www.sciencedirect.com/journal/journal-of-informetrics/vol/14/issue/4 "Go to table of contents for this volume/issue"), November 2020, 101066

## How do authors select keywords? A preliminary study of author keyword selection behavior

[https://doi.org/10.1016/j.joi.2020.101066](https://doi.org/10.1016/j.joi.2020.101066 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S1751157720300134&orderBeanReset=true)

Full text access

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S175115771930166X)

## Keywords

Author keywords

author keywords selection behavior

automatic keyword extraction

citation behavior

citation

scientometrics

## 3\. Methodology

The framework of this study is shown in . First, we define AK selection behavior and three influencing channels. Then, the data are collected from the ACM digital library proceeding collections, the fields of which include title, author, author\_id, abstract, AKs, citation counts, and references. Additionally, the dataset is stored in the database and preprocessed. Next, the percentages of AKs appearing in the three corresponding channels are calculated. Moreover, we investigate the differences of distributions of the three channels between core and non-core authors. Finally, the relationships between the distributions of the three channels and citation counts are examined.

![Fig. 1](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr1.jpg)

Download: Download high-res image (629KB)

### 3.2. Data and processing

In this study, we first manually collected 295,561 academic papers from the ACM digital library proceeding collections during December 2018 and January 2019, and excluded papers without keywords and abstracts. Finally, there were 196,142 academic papers, including 854,206 keywords and 261,023 distinct authors. As shown in , it can be seen that most of the papers (98.49%) were published after 2000 and the range of AKs for most (95.93%) of the papers varied from 2 to 8 with the average number 4.36. In , 48.59% of papers have received at least one citation and most authors (96.32%) have published fewer than 10 papers. It is worth noting that only papers in the dataset that comprised references were included to compute the percentages of AKs appearing in the references, the size of which equals 124,100. In addition, the size of references of the papers is 521,892.

![Fig. 2](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr2.jpg)

Download: Download high-res image (290KB)

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr3.jpg)

Download: Download high-res image (215KB)

The of the dataset, including titles, authors, author\_ids, abstracts, AKs, citation counts, and references were obtained from the ACM digital library proceeding collections. The author\_id is unique, which can be utilized to distinguish different authors. Subsequently, an in-house database was established by using MySQL.

### 3.3. Selection of high-frequency keywords

To reveal the distribution of AKs appearing in high-frequency keywords, the frequency of each AK in the entire dataset was counted, and #bibliometrics/indicator  growth analysis () was employed to identify the high-frequency keywords set. <mark class="hltr-orange">Growth score is calculated using: $Growth=∑i=1n-1(fi+1-fi)fi$, where $fi$ is frequency of a keyword in the $ith$ time segment</mark>. The time span of our dataset range from 1969 to 2018, thus we divided the dataset into ten time slots based on the publication year. <mark class="hltr-yellow">Keywords occured in less than two contigous time segements was omitted since these keywords cannot be included with the criterion of growth analysis. According to , we choose keywords scoring within the top 20% of valid keywords as high-frequency keywords, and the size of high-frequency keywords set is 7,917.</mark>

### 3.4. Classification of core and non-core authors

This research will investigate whether differences in the distributions of the three channels exist among papers written by different research productivity. In this study, the Price Law was employed to select core authors in the dataset. The Price Law () holds that half of the papers were written by a group of highly productive authors, whose number is approximately equal to the square root of the total number of authors. <mark class="hltr-yellow">The Price Law can be expressed as the following equation: $M=0.749*Nmax$, where *Nmax* is the largest number of papers published by the same author in the dataset. If the number of papers published by an author is greater than *M*, the author is a core author; whereas, if the number of papers published by an author is less than *M*, the author is a non-core author</mark>. In the present research, *Nmax* equals 176. This yields 9,598 core and 251,425 non-core authors.

> [Price law](https://en.wikipedia.org/wiki/Price%27s_law)

### 3.5. Measurement calculation and annotations

To investigate the impact of the three channels on AKs selection, the percentages of AKs appearing in the three channels were computed and visualized, respectively. At first, we used PorterStemmer #bibliometrics/indicator  to stem the words in AKs and the three channels. We then matched the AKs with the three channels for each paper, and calculated the ratio of the number of matched keywords to the number of AKs of the paper. The indicators calculated in this paper are shown in . Finally, we computed average percentage of different channels: $Avg=(∑i=1npi)/n$, where $pi$ is the percentage of keywords of paper $i$ appearing in the three channels and $n$ is the total number of papers.

Table 1. The descriptions of indicators in this paper.

| Indicator | Description | Indicator | Description |
| --- | --- | --- | --- |
| *ktp* | The percentage of AKs appearing in the title of a paper. | *krtakp* | The percentage of AKs appearing in titles, abstracts, and AKs of references of a paper. |
| *kap* | The percentage of AKs appearing in the abstract of a paper. | *khp* | The percentage of AKs of a paper appearing in high-frequency keywords. |
| *ktap* | The percentage of AKs appearing in the title and the abstract of a paper. | *avg\_per\_title* | The average of *ktp*. |
| *krtp* | The percentage of AKs appearing in titles of references of a paper. | *avg\_per\_abstract* | The average of *kap*. |
| *krap* | The percentage of AKs appearing in abstracts of references of a paper. | *avg\_per\_title\_abstract* | The average of *ktap*. |
| *krkp* | The percentage of AKs appearing in AKs of references of a paper. | *avg\_per\_reference* | The average of *krtakp*. |

## 4\. Results

### 4.1. Overview of AK selection behavior

#### 4.1.1. Distribution of keywords appearing in the content channel

presents the mean, median, and standard deviation of *ktp* and *kap* from 2000-2018. It can be observed that the mean of *ktp* and *kap* tend to increase from 2000-2018, which means that increasing numbers of AKs appear in titles and abstracts. On the other hand, the standard deviations of *ktp* and *kap* are relatively stable from 2000-2018, which suggests that the changes of *ktp* and *kap* among different papers in each year are relatively stable.

![Fig. 5](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr5.jpg)

Download: Download high-res image (332KB)

#### 4.1.4. The Interactions among three channels

Usually, an overlap exists among keywords from the channels. To reveal the interactions among the three channels, we computed percentages of keywords appearing in two or three channels, respectively. As shown in , the mean and median of percentages of keywords in content channel and prior knowledge channel are 70.3% and 75%, which are 13.6% and 15% higher than those of percentages of keywords appearing in content channel, respectively. Besides, there are 78.1% of keywords appearing in content channel and background channel, with 21.4% higher than that of content channel. Moreover, keywords appearing in content channel, prior knowledge channel, and background channel account for 82.4%, which is 25.7% higher than that of content channel.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr8.jpg)

Download: Download high-res image (114KB)

### 4.2. AK selection behavior of core vs. non-core authors

Different types of authors may possess different writing styles. For example, found that differences exist between authors from different ethnic backgrounds concerning the linguistic complexity of scientific writing. Since AKs constitute a core element of a paper, it seems important to determine if different types of authors exhibit differences in the distributions of the three channels.

#### 4.2.1. Differences between core and non-core authors in the content channel

As shown in , one can see that the mean *ktp* of core authors is smaller than that of non-core authors. However, the standard deviation of *ktp* of core authors is higher than that of non-core authors. Similarly, the mean of *kap* of core authors is smaller than that of non-core authors, and the standard deviation of *kap* of core authors is higher than that of non-core authors. We employed a double-tailed t-test to verify the differences of the distributions of content channel between core and non-core authors. The tests identified a statistically significant difference between core and non-core authors at the 0.001 level. From , , it can be seen that fewer AKs of paper written by core authors appear in titles and abstracts; however, authors among them may exhibit some differences. More AKs of papers written by non-core authors generally appear in titles and abstracts, and the distribution is relatively stable. This is probably because core authors possess more domain knowledge and have different strategies for keyword selection.

![Fig. 9](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr9.jpg)

Download: Download high-res image (138KB)

![Fig. 10](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr10.jpg)

Download: Download high-res image (135KB)

#### 4.2.2. Differences between core and non-core authors in the prior knowledge channel

The differences of the distributions of prior knowledge channel between core and non-core authors are presented in , from which it can be observed that the mean and median of *krtakp* of core authors are higher than those of non-core authors. Similarly, the standard deviation of *krtakp* of core authors is higher than that of non-core authors. We performed a double-tailed t-test to verify the differences of the distributions of prior knowledge channel between core and non-core authors. The test revealed a statistically significant difference between core and non-core authors at the 0.001 level, which indicates that, in general, more AKs of papers written by core authors appear in the references of papers. However, the distribution of prior knowledge channel of non-core authors is more stable than that of core authors.

![Fig. 11](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr11.jpg)

Download: Download high-res image (147KB)

#### 4.2.3. Differences between core and non-core authors in the background channel

shows that the mean and median of *khp* of core authors are higher than those of non-core authors. Similarly, the standard deviation of *khp* of core authors is higher than that of non-core authors. We conducted a double-tailed t-test to confirm the differences of distributions of the background channel between core and non-core authors. The test identified a statistically significant difference between core and non-core authors at the 0.001 level. Overall, slightly more AKs of papers written by core authors appear in high-frequency keywords than that of non-core authors; whereas, the distribution of background channel of core authors exhibit greater differences than that of non-core authors.

![Fig. 12](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr12.jpg)

Download: Download high-res image (141KB)

### 4.3. AK selection behavior and citation counts

In recent decades, citation counts have become a major indicator of the impact of a paper, and thus has drawn intense attention from scholars. Researchers have investigated a variety of factors that influence the citation counts of paper, including scientific quality and abstract readability (; ). In addition, studied the impact of several statistical properties of author-selected keywords and the network attributes of their co-occurrence networks on citation counts.<mark class="hltr-yellow"> They reported that the choice of keywords has a significant relationship to citation counts</mark>. This paper will investigate the relationships between distributions of the three channels and citation counts.

To investigate the relationships between distributions of the three channels and citation counts, we drew the complementary cumulative distribution functions of citation counts and average percentages. Note that citation counts of most papers (99.8%) is no more than 100, and the number of papers with more than 100 citations is too limited, which may lead to the randomness of relationships between distributions of the three channels and citation counts, and thus we mainly analysed the papers with citation counts no more than 100. The relationships between distributions of the three channels and citation counts of all papers are shown in the Appendix A. Moreover, there are some overlapping keywords among content channel, prior knowledge channel, and background channel, and there might be partial correlation between a pair of content channels in regards to the number of keywords they contain. Therefore, we separated them and explore their impact on citation counts, respectively.

#### 4.3.2. The relationship between keyword selection behavior and citation counts in the prior knowledge channel

According to the number of keywords containing in the prior knowledge channel, the relationships between keyword selection behavior and citation counts in the prior knowledge channel can be divided into four situations, which are keywords appearing in prior knowledge channel, keywords appearing in prior knowledge channel excluding the overlapping keywords between prior knowledge channel and content channel, between prior knowledge channel and background channel, and among prior knowledge channel, content channel, and background channel, respectively.

![Fig. 14](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr14.jpg)

Download: Download high-res image (195KB)

![Fig. 15](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr15.jpg)

Download: Download high-res image (184KB)

#### 4.3.4. The relationship between keyword selection behavior and citation counts in the overlaps among the three channels

The overlaps among the three channels can be divided into four situations, which are the overlaps between content channel and prior knowledge channel, between content channel and background channel, and among content channel, prior knowledge channel, and background channel. As shown in , it can be observed that the average percentages of keywords appearing in the overlapping keywords among the three channels increases when the citation counts are less than 10, and tend to be stable when it is greater than 10. Besides, the rising range of mean of percentages of keywords appearing in the overlapping keywords between prior knowledge channel and background channel is largest. In addition, the percentages of overlapping keywords between background channel and the other two channels are both about 0.4, with about 0.1 higher than that between content channel and prior knowledge channel, which indicates that AKs usually appear in high-frequency keywords, while fewer keywords appear in the titles, abstracts, and keywords of references.

![Fig. 16](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr16.jpg)

Download: Download high-res image (179KB)

The overlapping keywords among the three channels essentially indicate the keywords appearing in at least one channel. The three channels represent different sources and different channels are complementary, which may improve the visibility of papers, and thus the papers can gain more citations.

## Author contributions

**Wei Lu:** Conceived and designed the analysis, contributed data or analysis tools, and performed the analysis.

**Zhifeng Liu:** Conceived and designed the analysis, contributed data or analysis tools, performed the analysis, and wrote the paper.

**Yong Huang:** Conceived and designed the analysis, performed the analysis, and wrote the paper.

**Yi Bu:** Performed the analysis and wrote the paper.

**Xin Li:** Conceived and designed the analysis, and performed the analysis.

**Qikai Cheng:** Conceived and designed the analysis, contributed data or analysis tools, and performed the analysis.

## Appendix A. The relationships between keyword selection behaviors and citation counts of all papers

, , ,

![Fig. A1](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr17.jpg)

Download: Download high-res image (209KB)

![Fig. A2](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr18.jpg)

Download: Download high-res image (233KB)

![Fig. A3](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr19.jpg)

Download: Download high-res image (220KB)

![Fig. A4](https://ars.els-cdn.com/content/image/1-s2.0-S1751157720300134-gr20.jpg)

Download: Download high-res image (214KB)

## References

Wei Lu and Zhifeng Liu contributed equally to this work.

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S1751157720300134)