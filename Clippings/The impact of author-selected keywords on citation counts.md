---
title: "The impact of author-selected keywords on citation counts"
source: "https://www-sciencedirect-com.sire.ub.edu/science/article/pii/S1751157716301146?via%3Dihub"
author:
published:
created: 2025-04-11
description: "A number of bibliometric studies have shown that many factors impact citation counts besides the scientific quality. This paper used a large bibliomet…"
tags:
  - "research_method"
  - "bibliometrics/KW"
---
- [View **PDF**](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/S1751157716301146/pdfft?md5=dd1436d8ed8d17ed0a633c84a76dee23&pid=1-s2.0-S1751157716301146-main.pdf)

## Journal of Informetrics

[Volume 10, Issue 4](https://www-sciencedirect-com.sire.ub.edu/journal/journal-of-informetrics/vol/10/issue/4 "Go to table of contents for this volume/issue"), November 2016, Pages 1166-1177

## The impact of author-selected keywords on citation counts

[https://doi.org/10.1016/j.joi.2016.10.004](https://doi.org/10.1016/j.joi.2016.10.004 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S1751157716301146&orderBeanReset=true)

Full text access

- [Next article in issue](https://www-sciencedirect-com.sire.ub.edu/science/article/pii/S1751157716302036)

## Keywords

Citation counts

Keyword growth

Keyword diversity

Network centrality

## 4\. Research methods

### 4.1. Data source

Journal articles from the obesity research domain (a multidisciplinary research field) were considered to explore each of the six research questions. The obesity domain, a vast research area, was selected for this research, as it comprises many subtopics that have significantly interacted and evolved in recent decades. Extensive research has been conducted to determine the cause of and solutions to obesity () and tremendous progress has been made in defining the complex pathways that explain obesity ().

A two-step procedure was then used to remove ambiguity from the downloaded dataset. The first step of the two-step procedure examined the dataset for formatting inconsistencies such as encoding errors and incomplete data in the downloaded raw files. Because of the large size of the data and considerable amount of inconsistencies to check, it was not possible to do the data-cleaning manually. Therefore, a custom software using.Net framework was developed to complete the majority of data preparation, transfer as well as the analysis tasks. This custom software was programmed to search for and fix various spelling inconsistencies, including different presentations of the same keyword (e.g., Brasil and Brazil) and different spellings of keywords (e.g., eating behaviour and eating behavior). Articles that did not include the required information (e.g., publication years or citation counts) were excluded at this stage of the study. The data were then transferred by the software to a for data analysis.

The second step of the two-step procedure examined sets of keywords where each set comprised a list of keywords with different spellings often due to misspellings and compounding of multiple words but have the same meaning. Some keywords are given different names by their relevant scientific communities; for example, the keywords , calcidiol, 25-hydroxyvitamin D, 25-hydroxy and 25 (OH) vitamin D all refer to the same chemical, but are lexicographically different from a software perspective. These keyword sets were checked manually before each keyword of a set was programmatically replaced with an appropriate name at all instances. The software also used to merge the keywords that looked different due to leading or trailing (e.g., hypertension and hyper-tension). Finally, only those articles were considered that contained information about the author-provided keywords. and set out the statistics of the research dataset.

![Fig. 1](https://ars-els-cdn-com.sire.ub.edu/content/image/1-s2.0-S1751157716301146-gr1.jpg)

Download: Download high-res image (329KB)

Table 1. Description of research variables.

<table><thead><tr><th>Variables</th><td><span>Empty Cell</span></td><th>N</th><th>Min</th><th>Max</th><th>Mean</th><th>Std. Dev.</th></tr></thead><tbody><tr><td>Dependent</td><td>Citation count (logged)</td><td>24337</td><td>−1.69</td><td>4.78</td><td>1.04</td><td>0.99</td></tr><tr><td colspan="7"><br></td></tr><tr><td>Independent</td><td>Keyword growth</td><td>28210</td><td>−0.03</td><td>0.91</td><td>0.16</td><td>0.08</td></tr><tr><td></td><td>Keyword diversity</td><td>25859</td><td>0.00</td><td>1.00</td><td>0.22</td><td>0.11</td></tr><tr><td></td><td>Number of keywords</td><td>28105</td><td>0.33</td><td>1.00</td><td>0.51</td><td>0.14</td></tr><tr><td></td><td>Percentage of new keywords</td><td>28218</td><td>0.00</td><td>1.00</td><td>0.19</td><td>0.23</td></tr><tr><td></td><td>Network centrality</td><td>28219</td><td>0.00</td><td>1.00</td><td>0.42</td><td>0.11</td></tr><tr><td colspan="7"><br></td></tr><tr><td>Moderating</td><td>Number of author</td><td>28157</td><td>1</td><td>272</td><td>5.88</td><td>4.46</td></tr><tr><td></td><td>Length of article</td><td>27456</td><td>1</td><td>45</td><td>7.52</td><td>2.98</td></tr><tr><td></td><td>Impact factor</td><td>5146</td><td>0.33</td><td>16.11</td><td>3.67</td><td>1.56</td></tr><tr><td></td><td>Length of title</td><td>28228</td><td>9</td><td>426</td><td>92.80</td><td>33.06</td></tr></tbody></table>

All independent variables have been converted into a range of \[0,1\].

### 4.4. Control variables

This study considered four control variables to control their effects in exploring the proposed research questions. The four control variables were: (i) the length of an article; (ii) the number of author(s); (iii) journal quality; and (iv) the length of an article’s title.

The number of pages of an article was used to quantify the first control variable (i.e., the length of an article). The name of the second control variable (i.e., the number of authors) reflects its explicit meaning. The journal impact factor in which an article was published was used to measure the third control variable for each article. This information was collected manually from the website of each journal of our research dataset. Finally, the number of characters (without spaces) of the title of an article was used to calculate the fourth control variable (i.e., the length of each article’s title). These four measures were selected as control variables in this study based on previous research. Each measure was found to have a significant impact on citation counts (, ).

### 4.5. Data analysis procedure

The following procedures were used to calculate the independent and dependent measures of interest for all articles published in a specific year (e.g., 2012). First, *keyword growth* was calculated for all keywords available in all the articles published in that year (e.g., 2012) based on all the keywords available in the published articles from the previous 10 years (e.g., 2002–2011 (inclusive)). Second, a keyword co-occurrence network was constructed for the year (e.g., 2012) based on the keyword co-occurrence statistics of the previous 10 years (e.g., 2002–2011 inclusive). From this network, three network centrality values (i.e., degree, closeness and betweenness) and their averages for each keyword of that year (e.g., 2012) were calculated. Third, the values for each of the five independent variables (i.e., *keyword growth*, *keyword diversity*, *number of keywords*, *percentage of new keywords* and *network centrality*) were quantified for each article in that year (e.g., 2012). The five independent variables had different ranges of values; for example, *number of keyword* had a range of \[3,9\] and *keyword diversity* had a range of \[0,7\]. For this reason, the five independent variables were converted into a range of \[0,1\] by dividing each value of each variable by the range width of that variable. For example, each *keyword diversity* value was divided by seven which is the range width value (7−0=7) of the *keyword diversity* variable. Finally, normalised citation counts were measured for all articles published in the year (e.g., 2012) by following the steps described in the ‘Citation count’ section. The citation count variable ranged from 0 to 119.60. These procedures were followed for all articles published between 2008 and 2012 (inclusive). Thus, the research questions were investigated in relation to articles published from 2008 to 2012 (inclusive). However, it should be noted that data was used from 1998 to measure values for the independent variables. In relation to control variables, the length of an article, the number of author(s) of an article, journal quality and the length of an article’s title were considered.

In addition to the correlation analysis, this study followed the to investigate the relation between different keyword measures and citation counts. To confirm that the data analysis met different assumptions (i.e., independence of error and normally distributed error) under the regression method, the citation count values were logged (natural) before the required data analysis was conducted. These logged values of citation counts are found normally distributed.

## 5\. Results

Table 2. Basic information of the research dataset in relation to its keyword statistics (the period of 2008–2012 has been considered in this table since research questions of this study were investigated in relation to the articles published in this period).

<table><thead><tr><td><span>Empty Cell</span></td><th>2008</th><th>2009</th><th>2010</th><th>2011</th><th>2012</th><th><u>Total</u></th></tr></thead><tbody><tr><td colspan="7"># of articles having:</td></tr><tr><td>3 keywords</td><td>971</td><td>983</td><td>1191</td><td>1408</td><td>1491</td><td>6044</td></tr><tr><td>4 keywords</td><td>1446</td><td>1499</td><td>1809</td><td>2077</td><td>2349</td><td>9180</td></tr><tr><td>5 keywords</td><td>1237</td><td>1417</td><td>1501</td><td>1700</td><td>1935</td><td>7790</td></tr><tr><td>6 keywords</td><td>508</td><td>581</td><td>624</td><td>708</td><td>843</td><td>3264</td></tr><tr><td>7 keywords</td><td>206</td><td>218</td><td>229</td><td>287</td><td>314</td><td>1254</td></tr><tr><td>8 keywords</td><td>79</td><td>95</td><td>133</td><td>144</td><td>128</td><td>579</td></tr><tr><td>9 keywords</td><td>36</td><td>43</td><td>43</td><td>75</td><td>65</td><td>262</td></tr><tr><td><strong>Total</strong></td><td>4483</td><td>4836</td><td>5530</td><td>6399</td><td>7125</td><td><strong>28373</strong></td></tr></tbody></table>

Table 3. Pair wise values between study variables.

\*\*

Correlation are significant at 0.01 level.

\*

values are significant at 0.05 level.

The relation between five independent variables and citation counts was then modelled using a multiple regression model. In addition to showing the direction of the relationships (similar to the correlation analysis), this regression model quantified how a unit change in any of the independent variables affects citation counts (see ).

Table 4. The results from the first multiple regression model (R <sup>2</sup> =0.066) which considered only independent variables.

<table><thead><tr><th colspan="6">Coefficients statistics from the model (Dependent variable: Log (Citation count))</th></tr><tr><th>Model parameters</th><th>β</th><th>t</th><th>Significant</th><th colspan="2">Collinearity Statistics</th></tr><tr><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><th>Tolerance</th><th>VIF</th></tr></thead><tbody><tr><td>(Constant)</td><td>−0.24</td><td>−5.32</td><td>0.00</td><td></td><td></td></tr><tr><td>Keyword growth</td><td>2.03</td><td>25.05</td><td>0.00</td><td>0.86</td><td>1.16</td></tr><tr><td>Keyword diversity</td><td>0.38</td><td>6.04</td><td>0.00</td><td>0.89</td><td>1.13</td></tr><tr><td>Number of keywords</td><td>0.55</td><td>12.26</td><td>0.00</td><td>0.99</td><td>1.01</td></tr><tr><td>Percentage of new keywords</td><td>−0.84</td><td>−24.68</td><td>0.00</td><td>0.89</td><td>1.13</td></tr><tr><td>Network centrality</td><td>1.62</td><td>21.34</td><td>0.00</td><td>0.85</td><td>1.18</td></tr></tbody></table>

Since significant correlations between some pairs of the independent variables were found (see ), a collinearity test had been conducted while modelling the research data using a multiple regression model. Multi-collinearity exists in a regression model if there is a strong correlation between two or more of the model’s independent variables and those strong relationships affect the of the model. Collinearity tests report two statistics: (i) a variance of factor (VIF); and (ii) a tolerance that is the inverse of the VIF (i.e., 1/VIF). In general, there is cause for concern if the largest VIF for a variable is greater than 10. Further, the regression may be biased if the average VIF for all variables is substantially greater than 1. In relation to tolerance statistics, there is cause for concern if the smallest value is less than 0.2 and/or the average value is less than 0.1 (). The last two columns of set out the results of the collinearity tests in relation to the research data. In this study, the VIF had a maximum value of 1.18 and an average value of 1.12, while the tolerance values had a minimum value of 0.85 and an average value of 0.90. Thus, collinearity was not an issue in the proposed multiple regression model of .

Finally, another multiple regression model was developed to control the effects of four control variables (i.e., the number of article authors, the length of an article, the quality of the journal in which the article was published and the length of the title of an article) on the relations found between independent variables and the (as illustrated in ). After this control, only four independent variables (out of five) were found to have significant relations with citation counts. Keyword growth, number of keywords and network centrality showed a positive relation with citation counts (). On the other side, percentage of new keywords showed a negative relation with citation counts. Out of four control variables, three of them (i.e., journal impact factor, length of an article and number of authors) showed significant positive relations with citation counts (). As per the VIF and tolerance values of , collinearity was not an issue in the proposed multiple regression model.

Table 5. The results from the second multiple regression model (R <sup>2</sup> =0.163) which was developed to control the effect of control variables on the relations found in .

<table><thead><tr><th colspan="6">Coefficients statistics from the model (Dependent variable: Log (Citation count))</th></tr><tr><th>Model parameters</th><th>β</th><th>t</th><th>Significant</th><th colspan="2">Collinearity Statistics</th></tr><tr><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><th>Tolerance</th><th>VIF</th></tr></thead><tbody><tr><td>(Constant)</td><td>−0.95</td><td>−8.69</td><td>0.00</td><td></td><td></td></tr><tr><td>Journal impact factor</td><td>0.11</td><td>13.39</td><td>0.00</td><td>0.92</td><td>1.08</td></tr><tr><td>Length of title</td><td>0.00</td><td>1.49</td><td>0.14</td><td>0.96</td><td>1.05</td></tr><tr><td>Number of authors</td><td>0.02</td><td>4.72</td><td>0.00</td><td>0.94</td><td>1.06</td></tr><tr><td>Length of an article</td><td>0.07</td><td>13.29</td><td>0.00</td><td>0.92</td><td>1.09</td></tr><tr><td>Keyword growth</td><td>1.97</td><td>12.02</td><td>0.00</td><td>0.83</td><td>1.21</td></tr><tr><td>Keyword diversity</td><td>0.04</td><td>0.30</td><td>0.76</td><td>0.92</td><td>1.09</td></tr><tr><td>Number of keywords</td><td>0.20</td><td>2.31</td><td>0.02</td><td>0.98</td><td>1.02</td></tr><tr><td>Percentage of new keywords</td><td>−0.89</td><td>−11.96</td><td>0.00</td><td>0.88</td><td>1.17</td></tr><tr><td>Network centrality</td><td>1.44</td><td>8.48</td><td>0.00</td><td>0.86</td><td>1.17</td></tr></tbody></table>

## Authors contribution

**Shahadat Uddin**: Conceived and designed the analysis; Developed original research plan, Collected the data; Designed how to collect data from online source, Contributed data or analysis tools, Performed the analysis, Wrote the paper, Other contribution; Overally, guided the second author (my PhD student) in conducting this research.

**Arif Khan**: Collected the data; Design how to collect data from online source, Contributed data or analysis source, Performed the analysis, Wrote the paper.

## References

[View Abstract](https://www-sciencedirect-com.sire.ub.edu/science/article/abs/pii/S1751157716301146)