---
title: Detecting research topic trends by author-defined keyword frequency
source: https://www.sciencedirect.com/science/article/pii/S0306457321000935?pes=vor&utm_source=scopus&getft_integrator=scopus
author: 
published: 
created: 2025-04-11
description: Detecting research trends helps researchers and decision makers to promptly identify and analyze research topics. However, due to citation and publica…
tags:
  - research_method
---
- [View **PDF**](https://www.sciencedirect.com/science/article/pii/S0306457321000935/pdfft?md5=7b98408f58271ac9425ea22ee1f2dc5d&pid=1-s2.0-S0306457321000935-main.pdf)

[[detecting research topics trends by author defined keywords.pdf]]
## Information Processing & Management

[Volume 58, Issue 4](https://www.sciencedirect.com/journal/information-processing-and-management/vol/58/issue/4 "Go to table of contents for this volume/issue"), July 2021, 102594

## Detecting research topic trends by author-defined keyword frequency

[https://doi.org/10.1016/j.ipm.2021.102594](https://doi.org/10.1016/j.ipm.2021.102594 "Persistent link using digital object identifier") [Get rights and content](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S0306457321000935&orderBeanReset=true)

Full text access

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S0306457321000844)

## Keywords

Scientometrics

Bibliometrics

Deep learning

Word frequency prediction

## 4\. Experiments

### 4.1. Data

The ACM Digital Library is the world's most comprehensive database in computer science field. We collected literatures in the ACM Digital Library from 1969 to 2018 comprising 201,394 articles. After data pre-processing, there are in total 231,384 AKs, 265,371 authors and 7605 institutions. The abbreviation database was automatically built based on regular expression match. The database comprises 3247 key value pairs, in which the key is the abbreviation of the AK and the value is the full name of the AK. The distribution of publications, keywords, authors, and institutions in the ACM data set is shown in (a-d).

![Fig 2](https://ars.els-cdn.com/content/image/1-s2.0-S0306457321000935-gr2.jpg)

Download: Download high-res image (463KB)

Table 1. Summary of indicators employed in this research.

| Category | Sub-indicator | Indicator definition |
| --- | --- | --- |
| Temporal feature | $trelative$ | The inverse of PDY |
|  | $tabsolute$ | Current time ($t$) |
| Persistence | $nt$ | Keyword frequency in time $t$ |
| Community size | $at$ | Number of authors using this keyword in time $t$ |
|  | $it$ | Number of institutions using this keyword in time $t$ |
| Community | $pat$ | The cumulative number of papers published by authors who use this keyword in time $t$ |
| development potential | $pit$ | The cumulative number of papers published by institutions which use this keyword in time $t$ |

Note: Z-score method is adopted to standardize $pat$ and $pit$ of AKs within one year, respectively.

This abbreviation database is not reported here in its entirety owing to lack of space, but part of it is shown as . There are one-to-many mapping relationships between the abbreviated and original forms, because some keywords have the same abbreviations. But this rare case only accounts for 16.97% (551) in the database, and only 0.24% in all keywords. For simplicity, this research removed this case from the data set. Finally, we got 231,384 keywords. For each keyword, we extracted the features from the metadata of the articles. The features were then used to build the training set and test set of the AKFP in the following experiments. It is worth noting that, due to the large number of literatures collected from the ACM Digital Library, it is difficult to unify synonyms in articles. We assume that synonyms obey similar keyword count trajectories, so this phenomenon should not greatly affect the performance of the AKFP.

## 5\. Experiment setup

### 5.1. Training set

To verify the feasibility of short-, medium- and long-term prediction of keyword frequency, in this study, $m$ was set as 3, and $n$ was set as 2, 4 and 7, respectively. For simplicity, we denote these AKFPs with different $n$ as the AKFP (*m*  +  *n*) (i.e. AKFP 5, AKFP 7, and AKFP 10).

The above preprocessed AKs are used to construct the training set for these AKFPs. However, there are typically a small number of keywords that are used frequently and a much larger number of keywords that are utilized infrequently (; ; ; ). To build a balanced and sufficient data set for these AKFPs, we roughly divided the keywords into four levels according to the cumulative word frequency, followed by randomly sampling in each level. We then utilized the sliding window method to build the data set. Finally, the data set was split into training set, verification set and test set at a ratio of 8:1:1. These steps are detailed in (1) and (2) below.
- (1)
	Keyword selection: Since the statistics for the AKs published after 2014 cover less than five years, we got rid of them to avoid any boundary effect. There are 168,842 keywords left. According to the word frequency distribution, we simply divided these keywords into four intervals, as shown in below. The of 157,882 keywords is less than 10 and only 962 keywords are more than 99. To build a relatively balanced data set, we randomly selected 1000 keywords from the frequency range of 0–9 as well as 10–49 and retained 2191 keywords with a frequency of more than 50. Finally, a subset of 4191 keywords was obtained.
	Table 3. Keyword frequency distribution.
	| Threshold | 0–9 | 10–49 | 50–99 | 100- | Total |
	| --- | --- | --- | --- | --- | --- |
	| Number of keywords | 157,882 | 8768 | 1229 | 962 | 168,842 |
- (2)
	Sliding window method: To make full use of the historical information of each keyword, a sliding window with the fixed step size in $m$ is designed to build the data set, which is similar to . Taking “machine learning” as an example, it was first published in 1989, so we generated the training pairs as shown in . The first three columns ($x1,x2$ and $x3$) are the proposed indicators for three consecutive years, which can immediately be calculated from the ACM data set. The four to six columns ($y2,y4$ and $y7$) denote the actual word frequency as output variables. Taking the first row of as an example, $feature1989$ is features of the first year, $feature1990$ and $feature1991$ are the features of the second and third years respectively, while $frequency1993$, $frequency1995$ and $frequency1998$ indicate the actual word frequency in the following two, four and seven years, respectively. Then we slid the window forward one year in turn, to build the remaining rows. It should be noted that, since our collected ACM data set goes up to 2018, the samples that could not be obtained due to the boundary effect were denoted as “ **\*** ” **(star)**. The sliding window method built a one-to-many relationship between the keyword and its samples. We then applied the method to 4191 keywords. Finally, three sample sets for AKFP 5, AKFP 7, and AKFP 10 were obtained, as shown in .
	Table 4. “machine learning” for *m*  = 3, *n* = 2, 4 and 7.
	| Empty Cell | $x2$ | $x3$ | $y2$ | $y4$ | $y7$ |
	| --- | --- | --- | --- | --- | --- |
	| $feature1989$ | $feature1990$ | $feature1991$ | $frequency1993$ | $frequency1995$ | $frequency1998$ |
	| $feature1990$ | $feature1991$ | $feature1992$ | $frequency1994$ | $frequency1996$ | $frequency1999$ |
	| … | … | … | … | … | … |
	| $feature2013$ | $feature2014$ | $feature2015$ | $frequency2017$ | \* | \* |
	| $feature2014$ | $feature2015$ | $feature2016$ | $frequency2018$ | \* | \* |
	Table 5. Sample size of AKFPs.
	| Task | Sample size |
	| --- | --- |
	| AKFP 5 | 59,748 |
	| AKFP 7 | 51,456 |
	| AKFP 10 | 39,850 |

Due to the different time spans ($n$) of these AKFPs, the sample set of the AKFP with larger $n$ contains fewer samples. These samples that cannot be constructed are shown as \* in . Each constitutes time-series data with a dimension (time step, number of indicators), in which the time step is 3 and the number of indicators is 7.

### 5.3. Parameters

In the training process of a neural network, the determination of hyper parameters is more like an art than a science, and an appropriate can dramatically improve the performance. The , optimizer, and other parameters settings are shown in .

Table 7. Parameters of the .

| Parameters | Empty Cell | Values | Empty Cell |
| --- | --- | --- | --- |
| AKFP | AKFP 5 | AKFP 7 | AKFP 10 |
| Number of units in each layer | 256, 512, and 1 | 256, 512, and 1 | 256, 512 (2), and 1 |
| LSTM layer | One layer | One layer | Two layers |
| Activation function | ReLU | ReLU | ReLU |
| Initial learning rate | 1e-1 | 1e-1 | 1e-1 |
| Optimizer | Adadelta | Adadelta | Adadelta |
| Batch size | 64 | 64 | 64 |
| Epochs | 300 | 300 | 300 |

The transforms the input into a nonlinear output, which enhances nonlinear of the neural network. In this research, “Rectified Linear Unit” (ReLU) was adopted as the activation function and its formula is as follows: $f(x)=max(0,x)$. This function is widely used in the field of and performs well in various neural network tasks ().

The is vital to the performance of the neural network algorithms. The high learning rate not only accelerates the training process and stops the neural network from dropping into the locally optimal solution, but also results in non-convergence of parameters. In contrast, the low learning rate helps the model fine tune around the optimal parameter values to achieve the optimal fitting results, but takes more time. To balance the training speed and performance of the neural network, an learning rate is employed. Specifically, the of the learning rate is set to 0.1, and decays exponentially with 0.9 in every 3000 batches. Because of the large initial learning rate, epochs are set to 300, so that the neural network will fine tune the parameters in the latter phases of training.

The choice of optimizer also play an important role in the performance of the neural network. Compared with the traditional which easily falls into the local optimal, the Adadelta () is adopted. As an optimization algorithm, on the one hand, it allows each dimension of a parameter to have its own dynamic learning rate; on the other hand, it ensures that the units of the update match the units of the parameters. And it only uses first-order information and an to the diagonal Hessian, which means it has high computing efficiency. It is worth mentioning that, although the Adadelta optimizer require no manual tuning of a learning rate, the learning rate achieves better performance in our empirical experiments. Finally, we set the batch size to 64, and used a "tensorflow" framework to implement . The neural network settings are shown in .

### 5.4. Prediction results

The sliding window method proposed above was utilized to predict keyword frequency. The black curve is the actual keyword frequency curve, and the red curve nearest to it denotes predicted results of AKFP 5, closely followed by the green curve, which indicates predicted results of AKFP 7. The blue curve predicted by AKFP 10 has the lowest accuracy. These results are consistent with the MSE variation on the test set; that is, the longer the time span is, the lower the accuracy of the corresponding AKFP. Therefore, the AKFP is a prediction task that pursues the tradeoff between timeliness and accuracy. For these high-frequency keywords shown in (a-i), these prediction results are satisfactory. The predicted curves keep the track similar to the actual black curve, although occasionally there is a little lag phenomenon. For these keywords with lower frequency (j-l), these prediction curves are more oscillatory due to the randomness of actual word frequency, and this phenomenon is more significant with the decrease of keyword frequency.

### 5.5. Feature importance

To analyze the importance of the features employed in this study, we dropped one category of feature from input variables one by one and used the remaining features to train the neural network (“leave-one-out model”), after which the MSE on the test set was calculated. Specifically, we randomly divided the data 10 times at the ratio of 8:1:1, and 10 groups of training set, validation set and test set were obtained for AKFP 5, 7, and 10, respectively. Then, leave-one-out models and the full features model were trained on each training set. For example, AKFP 5 has 10 groups of results and each group contains a full model and four leave-one-out models. Subsequently, we calculated the difference of the MSE on the test set between the leave-one-out model and corresponding full features model, and used a paired *t* \-test to test the of these features on the prediction performance of the AKFP.

The experiment results are shown in below. The third column of the table denotes the average difference of MSE on the test set. It shows that the MSE of the AKFP (5, 7, and 10) increases significantly if the temporal feature is dropped, which indicates that the temporal feature is an un-ignorable factor in the AKFP. Indeed, the explosive growth of scientific publications leads to more new keywords and more high-frequency keywords. Therefore, the characteristics of publications distribution make the temporal feature become a key factor to determine the topic trends. Although the persistence should have worked as the core feature, its information may be included by the community size, to a certain extent. In fact, there is a strong between persistence and community size, because high-frequency keywords are generally adopted by more authors and institutions, while this is not the case for low-frequency keywords. Therefore, simply dropping one of persistence and community size may not have a significant impact on the performance of the model. However, we still identified that, with the increase in time span ($n$) of the AKFP, the results change from being significant for only one feature to not significant for both, which indicates that the influence of persistence and community size on future keyword frequency is gradually decreasing. In order to further analyze the effect of persistence and community size on the AKFP, the case of dropping both was trained. As expected, we found that persistence and community size significantly affect the MSE of AKFP 5, 7, and 10, but have the lowest impact (4.8506) on AKFP 10, which is consistent with the previous conclusion. Therefore, Persistence & Community size are the dominant factors in the short- and medium-term word frequency prediction. Finally, the effect of community development influential on AKFP 5 is very weak (0.7175), but with the expansion in time span ($n$) of the AKFP, its impact gradually rises. Just as in AKFP 10, the effect of community development influential on MSE rises to 6.1537, which is about nine times as much as that of AKFP 5. Community development potential becomes the most important factor in long-term word frequency prediction. Hence, the scientific research capacity of authors and institutions will significantly affect the long-term development of the topics. For the sake of clarity, we ranked the importance ranking of these features in .

Table 8. Difference between each ‘leave-one-out’ model and the full features model.

| Time span | Dropped feature | Difference in test MSE |
| --- | --- | --- |
|  | Temporal feature | 1.8384 |
|  | Persistence | −0.2276 |
| 5 | Community size | −0.8208 |
|  | Community development potential | 0.7175 |
|  | Persistence & Community size | 5.8060 |
|  | Temporal feature | 1.1853 |
|  | Persistence | 0.6374 |
| 7 | Community size | 0.1541 |
|  | Community development potential | 1.3966 |
|  | Persistence & Community size | 6.3894 |
|  | Temporal feature | 2.2322 |
|  | Persistence | 0.1967 |
| 10 | Community size | −1.3125 |
|  | Community development potential | 6.1537 |
|  | Persistence & Community size | 4.8506 |

Notes:.

⁎

indicates *p* <0.05,.

⁎⁎

indicates *p* <0.01,.

⁎⁎⁎

indicates *p* < 0.001.

### 5.6. Comparisons

The fitting and prediction performances of the baseline models and the LSTM model are shown in . Compared with baselines, the LSTM model is slightly less effective on the training set than XGB and , but the fitting performance is significantly better than LR. The LSTM model exceeds all baselines on the test set. More specifically, in AKFP 5, the MSE of the LSTM on the test set is lower than 14.14% for XGB, 15.11% for RF, 24.95% for KNN, and 23.04% for LR. In AKFP 7, the MSE of the LSTM on the test set is reduced by 8.47% for XGB, 4.98% for RF, 12.41% for KNN, and 17.97% for LR. In AKFP 10, the MSE of the LSTM on the test set is decreased by 13.32% compared with XGB, 4.90% with RF, 17.58% with KNN, and 23.32% with LR. In addition, R <sup>2</sup> of the LSTM model achieves the best effect on the test set in AKFP 5, 7, and 10, which are 0.822, 0.679, and 0.624, respectively, illustrating that the LSTM neural network fits the developing process of keywords well and has better generalization capabilities than baseline models.

Table 9. Fitting and prediction performances for different models.

<table><thead><tr><th>Time span</th><th>Models</th><th colspan="3">Train</th><th colspan="3">Test</th></tr><tr><td><span>Empty Cell</span></td><td><span>Empty Cell</span></td><th>MSE</th><th>MAE</th><th><span><math><msup is="true"><mi is="true">R</mi> <mn is="true">2</mn></msup></math></span></th><th>MSE</th><th>MAE</th><th><span><math><msup is="true"><mi is="true">R</mi> <mn is="true">2</mn></msup></math></span></th></tr></thead><tbody><tr><td></td><td>LR</td><td>38.275</td><td>2.837</td><td>0.760</td><td>39.650</td><td>2.921</td><td>0.769</td></tr><tr><td></td><td>KNN</td><td>/</td><td>/</td><td>/</td><td>40.655</td><td>2.830</td><td>0.763</td></tr><tr><td>5</td><td>RF</td><td>25.544</td><td>2.409</td><td>0.840</td><td>35.945</td><td>2.665</td><td>0.790</td></tr><tr><td></td><td>XGB</td><td><strong>22.812</strong></td><td><strong>2.382</strong></td><td><strong>0.857</strong></td><td>35.652</td><td>2.662</td><td>0.792</td></tr><tr><td></td><td>LSTM</td><td>28.034</td><td>2.449</td><td>0.824</td><td><strong>30.513</strong></td><td><strong>2.629</strong></td><td><strong>0.822</strong></td></tr><tr><td></td><td>LR</td><td>69.505</td><td>3.791</td><td>0.612</td><td>62.455</td><td>3.712</td><td>0.609</td></tr><tr><td></td><td>KNN</td><td>/</td><td>/</td><td>/</td><td>58.489</td><td>3.477</td><td>0.634</td></tr><tr><td>7</td><td>RF</td><td>51.649</td><td>3.198</td><td>0.712</td><td>53.913</td><td>3.335</td><td>0.663</td></tr><tr><td></td><td>XGB</td><td><strong>42.481</strong></td><td><strong>3.103</strong></td><td><strong>0.763</strong></td><td>55.976</td><td>3.367</td><td>0.650</td></tr><tr><td></td><td>LSTM</td><td>54.527</td><td>3.214</td><td>0.694</td><td><strong>51.230</strong></td><td><strong>3.300</strong></td><td><strong>0.679</strong></td></tr><tr><td></td><td>LR</td><td>116.098</td><td>5.135</td><td>0.429</td><td>93.338</td><td>5.023</td><td>0.509</td></tr><tr><td></td><td>KNN</td><td>/</td><td>/</td><td>/</td><td>86.828</td><td>4.650</td><td>0.543</td></tr><tr><td>10</td><td>RF</td><td>87.452</td><td><strong>4.357</strong></td><td>0.570</td><td>75.253</td><td>4.415</td><td>0.604</td></tr><tr><td></td><td>XGB</td><td><strong>83.217</strong></td><td>4.428</td><td><strong>0.591</strong></td><td>82.571</td><td>4.478</td><td>0.566</td></tr><tr><td></td><td>LSTM</td><td>86.025</td><td>4.205</td><td>0.581</td><td><strong>71.567</strong></td><td><strong>4.270</strong></td><td><strong>0.624</strong></td></tr></tbody></table>

## CRediT authorship contribution statement

**Wei Lu:** Conceptualization, Methodology, Formal analysis, Supervision. **Shengzhi Huang:** Conceptualization, Methodology, Writing – original draft. **Jinqing Yang:** Data curtion, Formal analysis. **Yi Bu:** Investigation, Writing – original draft. **Qikai Cheng:** Data curtion, Writing – review & editing. **Yong Huang:** Conceptualization, Writing – original draft, Writing – review & editing.

## Declaration of competing interest

The authors declare no competing interests.

## References

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S0306457321000935)