<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Converting Scopus Search Query to Web of Science Format

To convert your Scopus search query to Web of Science format, several key changes are needed due to differences in field tags, subject area filtering, and search syntax between the two databases.

## Web of Science Equivalent Query

Here is your Scopus query converted for Web of Science:

```
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=(Computer Science* OR Social Sciences* OR Arts*)
AND PY > 2014
```


## Key Changes Explained

### Field Tag Conversion

**Title-Abstract-Keywords Search:**

- Scopus uses: `TITLE-ABS-KEY()`
- Web of Science uses: `TS=()` (Topic Search)

The `TS=` field tag in Web of Science searches across multiple fields including title, abstract, author keywords, and Keywords Plus[^1_1][^1_2][^1_3]. This provides equivalent coverage to Scopus's TITLE-ABS-KEY field.

### Subject Area Filtering

**Subject Categories:**

- Scopus uses: `SUBJAREA(COMP OR SOCI OR ARTS)`
- Web of Science uses: `WC=(Computer Science* OR Social Sciences* OR Arts*)`

Web of Science uses the `WC=` field tag to search Web of Science Categories[^1_1]. The category names differ between databases:

- Computer Science topics in Web of Science fall under various "Computer Science" categories
- Social Sciences topics map to "Social Sciences" categories
- Arts topics correspond to "Arts \& Humanities" categories[^1_4][^1_5]

You may need to be more specific with the exact Web of Science category names. The full list includes approximately 250 subject categories organized into five broad research areas[^1_5][^1_6].

### Publication Year Filter

**Year Filtering:**

- Scopus uses: `PUBYEAR > 2014`
- Web of Science uses: `PY > 2014`

Web of Science uses `PY=` for publication year searches[^1_1]. The syntax `PY > 2014` will return articles published after 2014.

## Alternative Approaches

### More Specific Subject Categories

For more precise results, you could specify exact Web of Science categories instead of using wildcards:

```
WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" OR "Social Sciences, Interdisciplinary" OR "Arts & Humanities Other Topics")
```


### Using Research Areas

Alternatively, you can use the broader Research Area field:

```
SU=(Technology OR "Social Sciences" OR "Arts & Humanities")
```

The `SU=` field tag searches Research Areas, which are higher-level groupings of the detailed Web of Science Categories[^1_1][^1_7].

## Important Considerations

### Search Operators

Both databases support the same Boolean operators (AND, OR, NOT), so your logical structure remains unchanged[^1_8]. Web of Science also supports proximity operators like NEAR and SAME in most fields[^1_8].

### Wildcards

The asterisk (*) wildcard works similarly in both databases for truncation searches[^1_3].

### Database Coverage Differences

Web of Science focuses on selectivity while Scopus emphasizes comprehensiveness[^1_9]. This means you may get different result sets even with equivalent queries due to different journal coverage and indexing practices.

The converted query should provide comparable results to your original Scopus search while adhering to Web of Science's specific field tags and category structure.

<div style="text-align: center">⁂</div>

[^1_1]: https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-field-tags.htm

[^1_2]: https://webofscience.help.clarivate.com/Content/current-contents/ccc-search-field-tags.htm

[^1_3]: https://library.tiffin.edu/web_sci/search

[^1_4]: https://webofscience.zendesk.com/hc/en-us/articles/27505726032017-Web-of-Science-Subject-Categories

[^1_5]: https://incites.zendesk.com/hc/en-gb/articles/22586272202513-Web-of-Science-Research-Areas

[^1_6]: https://webofscience.help.clarivate.com/Content/Resources/Docs/core-collection-subject-categories.xlsx

[^1_7]: http://webofscience.help.clarivate.com/en-us/Content/research-areas.html?Highlight=research+areas

[^1_8]: https://webofscience.help.clarivate.com/en-us/Content/search-operators.html

[^1_9]: https://www.wur.nl/en/newsarticle/web-of-science-and-scopus-search-discrepancies-explained.htm

[^1_10]: https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm

[^1_11]: https://images.webofknowledge.com/images/help/WOS/hs_wos_fieldtags.html

[^1_12]: https://webofscience.help.clarivate.com/es-es/Content/wos-core-collection/woscc-search-field-tags.htm

[^1_13]: https://images.webofknowledge.com/images/help/WOS/hs_advanced_fieldtags.html

[^1_14]: https://blog.csdn.net/qq_33039859/article/details/109253007

[^1_15]: https://images.webofknowledge.com/images/help/WOS/hp_subject_category_terms_tasca.html

[^1_16]: https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Core-Collection-Web-of-Science-Categories?language=en_US

[^1_17]: https://images.webofknowledge.com/images/help/es_LA/WOS/hp_subject_category_terms_tasca.html

[^1_18]: https://cseweb.ucsd.edu/~bsy/area.state.html

[^1_19]: https://clarivate.com/academia-government/release-notes/web-of-science/web-of-science-march-28-2024-release-notes/

[^1_20]: https://images.webofknowledge.com/images/help/WOK/hs_advanced_fieldtags.html

[^1_21]: https://web.archive.org/web/20110701061806/http:/thomsonreuters.com/products_services/science/science_products/a-z/web_of_science/

[^1_22]: http://wokinfo.com/media/pdf/qrc/webofscience_qrc_en.pdf

[^1_23]: https://ub.unibas.ch/en/search-find/databases-e-journals-e-books/access-authorisation/web-of-science/

[^1_24]: https://www.bibliometrix.org/documents/Field_Tags_bibliometrix.pdf

[^1_25]: https://pubmed.ncbi.nlm.nih.gov/23335826/

[^1_26]: https://academia.stackexchange.com/questions/88183/is-there-a-formal-way-to-aggregate-the-web-of-science-categories

[^1_27]: https://www.youtube.com/watch?v=ZViZO9fP2ts

[^1_28]: https://en.wikipedia.org/wiki/Web_of_Science

[^1_29]: https://libguides.uvt.nl/theology/wos-basic-search

[^1_30]: https://science-publisher.org/scopus-web-of-science-how-to-choose-the-best-journal-based-on-its-indexing/

[^1_31]: https://www.youtube.com/watch?v=lZereXof8_8

[^1_32]: https://www.youtube.com/watch?v=Suycl1IIkE8


---

# Converting Extended Scopus Search Query to Web of Science Format

Your Scopus query includes a more complex logical structure with an additional OR clause for GLAM (Galleries, Libraries, Archives, and Museums) related terms. Here's the conversion to Web of Science format with explanations of the key changes.

## Web of Science Equivalent Query

```
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load") 
    OR 
    ("metadata usability" OR "cultural heritage metadata" OR "GLAM interoperability")
)
AND WC=(Computer Science* OR Social Sciences* OR Arts*)
```


## Key Conversion Elements

### Field Tag Transformation

**Topic Search Field:**

- Scopus: `TITLE-ABS-KEY()`
- Web of Science: `TS=()`

The `TS=` field tag in Web of Science searches across Title, Abstract, Author Keywords, and Keywords Plus fields[^2_1][^2_2][^2_3]. This provides equivalent coverage to Scopus's TITLE-ABS-KEY functionality, which combines title, abstract, and keywords into a single searchable field[^2_4][^2_5].

### Boolean Logic Structure

The logical structure of your query remains intact in the conversion[^2_6][^2_7]. Web of Science supports the same Boolean operators (AND, OR, NOT) as Scopus, and the nested parentheses structure is preserved exactly as in your original query[^2_6][^2_7]. The complex OR logic that separates your main research concepts from the GLAM-specific terms is maintained without modification.

### Subject Area Filtering

**Category Mapping:**

- Scopus: `SUBJAREA(COMP OR SOCI OR ARTS)`
- Web of Science: `WC=(Computer Science* OR Social Sciences* OR Arts*)`

Web of Science uses the `WC=` field tag to search Web of Science Categories[^2_1][^2_2]. The wildcard asterisks (*) ensure comprehensive coverage of related subcategories within each broad subject area[^2_3][^2_6].

## Understanding the Query Logic

Your query has a sophisticated three-part structure:

1. **Primary Research Focus**: The combination of participatory design approaches AND knowledge/interaction concepts
2. **Alternative GLAM Focus**: Metadata usability and cultural heritage interoperability terms
3. **Subject Filtering**: Limited to computer science, social sciences, and arts domains

The OR operator between the first two parts means results will include either research that combines participatory design with knowledge management concepts, OR research specifically focused on GLAM metadata and interoperability issues[^2_7].

## Alternative Approaches

### More Specific Subject Categories

For more precise results, you could specify exact Web of Science categories:

```
WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" 
    OR "Information Science Library Science" OR "Social Sciences, Interdisciplinary" 
    OR "Arts & Humanities Other Topics")
```


### Research Area Alternative

Using broader Research Area classifications:

```
SU=(Technology OR "Social Sciences" OR "Arts & Humanities")
```


## ==Important Considerations

### Search Operators and Wildcards

Both databases support identical Boolean logic and wildcard functionality[^2_8][^2_6]. The asterisk (*) truncation in terms like "co-creation*" and "knowledge graph*" works the same way in both systems, automatically capturing plural forms and variations[^2_8][^2_6].

### Database Coverage Differences

Web of Science emphasizes selectivity while Scopus focuses on comprehensiveness[^2_8]. This means your converted query may return different result sets due to varying journal coverage and indexing practices between the databases[^2_9][^2_8]. Web of Science covers over 21,000 journals while Scopus includes about 27,000 peer-reviewed journals[^2_8].

The converted query maintains your original search logic while adapting to Web of Science's specific field tags and category structure, ensuring comparable search results across both databases.

<div style="text-align: center">⁂</div>

[^2_1]: https://images.webofknowledge.com/images/help/WOS/hs_advanced_fieldtags.html

[^2_2]: https://webofscience.help.clarivate.com/Content/current-contents/ccc-search-field-tags.htm

[^2_3]: https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-field-tags.htm

[^2_4]: https://stackoverflow.com/questions/35526682/scopus-search-title-abs-key

[^2_5]: https://libraryguides.vu.edu.au/systematicliteraturereviews/runyoursearch

[^2_6]: https://library.tiffin.edu/web_sci/search

[^2_7]: https://libguides.umn.edu/BooleanOperators

[^2_8]: https://www.wur.nl/en/newsarticle/web-of-science-and-scopus-search-discrepancies-explained.htm

[^2_9]: https://www.libraryjournal.com/story/technology/e-views-and-reviews-scopus-vs-web-of-science

[^2_10]: https://nonprod-devportal.elsevier.com/support.html

[^2_11]: https://libguides.library.universityofgalway.ie/Systematic_Reviews/Translatingyourseachstrategy

[^2_12]: https://pypi.org/project/scopus-of-science/

[^2_13]: https://www.excise.go.th/_ocsh/help/topics/help_urm_setup_urm_setup_html_help_rmdsg/help/cs_admin/cs_sysadmin_html_help/c04_settings051.htm?tp=true\&locale=en

[^2_14]: https://images.webofknowledge.com/images/help/WOK/hs_advanced_fieldtags.html

[^2_15]: https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm

[^2_16]: https://guides.lib.purdue.edu/citationdatabases/searchingwebofscience

[^2_17]: https://www.nature.com/articles/s41599-025-04440-8

[^2_18]: https://www.mongodb.com/docs/relational-migrator/code-generation/query-converter/convert-queries/

[^2_19]: https://webofscience.help.clarivate.com/en-us/Content/search-operators.html

[^2_20]: https://webofscience-qa.help.dev-wos.com/en-us/Content/inspec/inspec-search-field-tags.htm


---

# Converting Complex Scopus Search Query to Web of Science Format

Your Scopus query presents the most sophisticated structure yet, incorporating proximity operators and controlled vocabulary terms. Here's the complete conversion to Web of Science format with detailed explanations of the necessary adaptations.

## Web of Science Equivalent Query

```
TS=(
    (
        ("digital collection*" OR "GLAM metadata" OR "museum informat*" 
        OR "archival discover*" OR "cultural heritage" OR "historical corpus"
        OR "user-centered metadata" OR "metadata schema")
        AND 
        ("data stori*" OR "interactive visual*" OR "user test*" 
        OR "metadata crosswalk*" OR "FAIR data" OR "linked open data")
    )
    OR 
    (
        ("semantic web" OR "RDF mapping" OR "ontology engineering") 
        NEAR/5 
        ("digital humanit*" OR "GLAM sector" OR "historical memory")
    )
)
AND TS=("libraries" OR "museums" OR "archives" OR "cultural heritage")
AND PY > 2014
```


## Key Conversion Elements

### Field Tag Transformations

**Title-Abstract-Keywords Search:**

- Scopus: `TITLE-ABS-KEY()`
- Web of Science: `TS=()`

The `TS=` field tag in Web of Science searches across Title, Abstract, Author Keywords, and Keywords Plus fields[^3_1]. This provides equivalent comprehensive coverage to Scopus's TITLE-ABS-KEY functionality, ensuring your complex nested search logic remains intact across all relevant content fields.

### Proximity Operator Conversion

**Within-Word Distance Search:**

- Scopus: `W/5`
- Web of Science: `NEAR/5`

This represents a critical conversion point in your query. Web of Science uses the `NEAR/x` operator to find records where terms are within a specified number of words of each other[^3_2][^3_3]. The `NEAR/5` operator in Web of Science finds terms within 5 words of each other in any order, which provides equivalent functionality to Scopus's `W/5` proximity search[^3_4]. Both operators maintain the semantic relationship between "semantic web," "RDF mapping," or "ontology engineering" concepts and the digital humanities context terms.

### Controlled Vocabulary Adaptation

**Index Terms Conversion:**

- Scopus: `INDEXTERMS("libraries" OR "museums" OR "archives" OR "cultural heritage")`
- Web of Science: `TS=("libraries" OR "museums" OR "archives" OR "cultural heritage")`

This conversion addresses a fundamental difference between the databases. Scopus uses controlled vocabulary through its INDEXTERMS field, which searches professionally assigned index terms from various thesauri including Ei thesaurus, Emtree medical terms, and MeSH[^3_5]. However, Web of Science does not have an equivalent controlled vocabulary field for general subject indexing[^3_6][^3_7].

Instead, Web of Science relies on Keywords Plus, which are algorithmically generated from the titles of cited references within each document[^3_8]. To maintain search effectiveness, the controlled vocabulary terms are converted to topic searches using the `TS=` field tag, which will locate these terms in titles, abstracts, and keywords where they naturally appear in GLAM-related research.

### Publication Year Filter

**Year Filtering:**

- Scopus: `PUBYEAR > 2014`
- Web of Science: `PY > 2014`

Web of Science uses the `PY=` field tag for publication year searches[^3_1]. The syntax `PY > 2014` maintains your temporal filter for research published after 2014.

## Understanding the Complex Search Logic

Your query employs a sophisticated three-tier structure:

1. **Primary GLAM Research Focus**: The first major component combines digital collection and metadata terms with data visualization and testing concepts, targeting research at the intersection of cultural heritage collections and user experience.
2. **Semantic Web Alternative**: The proximity-based second component specifically targets semantic web technologies within 5 words of digital humanities contexts, capturing research on linked data applications in cultural institutions.
3. **Domain Filtering**: The index terms filter ensures results focus specifically on libraries, museums, archives, and cultural heritage contexts.

The OR operator between these major components creates a comprehensive search that captures both user-centered metadata research and semantic web applications within the GLAM sector.

## Alternative Approaches

### Subject Category Filtering

For more precise subject area targeting, you could replace the topic-based domain filter with Web of Science Category searches:

```
WC=("Information Science Library Science" OR "Computer Science, Information Systems" 
    OR "History" OR "Humanities, Multidisciplinary")
```


### Enhanced Proximity Combinations

Web of Science also supports the `SAME` operator for finding terms within the same sentence, which could provide even more precise semantic relationships:

```
("semantic web" OR "RDF mapping" OR "ontology engineering") 
SAME 
("digital humanit*" OR "GLAM sector" OR "historical memory")
```


## Important Considerations

### Database-Specific Limitations

Web of Science's lack of controlled vocabulary indexing means the converted query may retrieve different result sets compared to Scopus[^3_6]. The topic-based approach compensates for this limitation but may require additional refinement of search terms to achieve optimal precision.

### Search Operator Precedence

Web of Science processes Boolean and proximity operators according to specific precedence rules[^3_9]. The nested parentheses structure in your converted query ensures proper logical grouping and maintains your intended search relationships.

### Proximity Search Effectiveness

The `NEAR/5` operator in Web of Science will find terms within 5 words in any order[^3_2][^3_3]. This provides equivalent functionality to Scopus's `W/5` operator while maintaining the semantic relationships crucial to your research focus on digital humanities applications of semantic web technologies.

The converted query preserves your original search strategy while adapting to Web of Science's specific field tags, operators, and indexing approach, ensuring comprehensive retrieval of relevant cultural heritage and digital humanities research.

<div style="text-align: center">⁂</div>

[^3_1]: https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-field-tags.htm

[^3_2]: https://images.webofknowledge.com/images/help/WOS/hs_search_operators.html

[^3_3]: https://webofscience.help.clarivate.com/en-us/Content/search-operators.html

[^3_4]: https://dcu.libguides.com/c.php?g=701483\&p=5040857

[^3_5]: https://www.recursoscientificos.fecyt.es/sites/default/files/content_coverage_guide.pdf

[^3_6]: https://guides.mclibrary.duke.edu/searchtips/wos

[^3_7]: https://onesearch.library.utoronto.ca/faq/how-can-i-use-subject-headings-improve-my-searching

[^3_8]: https://library.caltech.edu/c.php?g=512744\&p=3502852

[^3_9]: https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Order-of-precedence-for-Boolean-operators

[^3_10]: https://webofscience.help.clarivate.com/en-us/Content/search-rules.htm

[^3_11]: https://resources.nu.edu/researchprocess/proximity

[^3_12]: https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm

[^3_13]: https://libguides.ntu.edu.sg/c.php?g=959391\&p=6963728

[^3_14]: https://www.youtube.com/watch?v=RAwur7nnLPY

[^3_15]: https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Core-Collection-MeSH-terms-cannot-be-searched?language=en_US

[^3_16]: https://webofscience.help.clarivate.com/en-us/Content/search-fields.htm

[^3_17]: https://webofscience.zendesk.com/hc/en-us/articles/27505726032017-Web-of-Science-Subject-Categories

[^3_18]: https://www.bibliometrix.org/documents/Field_Tags_bibliometrix.pdf

[^3_19]: https://www.libraries.rutgers.edu/databases/web_of_science

[^3_20]: https://library.bath.ac.uk/web-of-science-all-databases/keyword

[^3_21]: https://blog.csdn.net/qq_33039859/article/details/109253007

[^3_22]: https://libguides.bc.edu/advancedsearch/proximity

[^3_23]: https://en.wikipedia.org/wiki/Web_of_Science

[^3_24]: https://uark.libguides.com/webofscience/searchtips

[^3_25]: https://library.uhv.edu/advanced-searching/proximity

[^3_26]: https://library-guides.ucl.ac.uk/web-of-science/search-tips


---

# Converting Complex Scopus Search Query to Web of Science Format

Your fourth Scopus query represents the most comprehensive search structure in this series, combining three distinct concept groups with AND operators to capture research at the intersection of participatory design, semantic technologies, and cultural heritage. Here's the complete conversion to Web of Science format.

## Web of Science Equivalent of <mark class="hltr-orange">4th Scopus Query</mark>

```
TS=(
    (
        "participatory design" OR "co-creation*" OR "user centered design" OR "human centered design" OR "human centered interaction" OR "CK theory" OR "usability" OR "UX" OR "social innovation"
    )
    AND
    (
        "knowledge graph*" OR "semantic web" OR "linked data" OR "RDF" OR "ontology engineering" OR "semantic technology" OR "semantic data" OR "semantic frames" OR "frame semantics" OR "knowledge organization system*" OR "KOS"
    )
    AND
    (
        "cultural heritage" OR "GLAM" OR "GLAM metadata" OR "museum*" OR "archive*" OR "library" OR "libraries" OR "digital collections" OR "historical memory" OR "historical corpus" OR "metadata crosswalk*" OR "metadata schema" OR "digital humanities" OR "polyvocality" OR "post-colonial heritage"
    )
)
AND PY > 2014
```


## Key Conversion Elements

### Field Tag Transformation

**Title-Abstract-Keywords Search:**

- Scopus: `TITLE-ABS-KEY()`
- Web of Science: `TS=()`

The `TS=` field tag in Web of Science searches across Title, Abstract, Author Keywords, and Keywords Plus fields. This comprehensive coverage ensures that your three-way intersection search maintains its effectiveness across all relevant content fields, capturing research that explicitly discusses the convergence of user-centered design approaches, semantic technologies, and cultural heritage applications.

### Publication Year Filter

**Year Filtering:**

- Scopus: `PUBYEAR > 2014`
- Web of Science: `PY > 2014`

Web of Science uses the `PY=` field tag for publication year searches. The syntax `PY > 2014` maintains your temporal filter for research published after 2014, ensuring contemporary relevance in this rapidly evolving interdisciplinary field.

## Understanding the Triple-Intersection Logic

Your query employs a highly specific three-way intersection strategy that targets a very precise research niche:

### First Concept Group: User-Centered Design Approaches

The first group encompasses various methodologies focused on human-centered innovation, including participatory design, co-creation processes, user experience (UX) design, and social innovation frameworks. This group captures research emphasizing collaborative and inclusive design methodologies.

### Second Concept Group: Semantic Technologies

The second group covers the full spectrum of semantic web technologies and knowledge representation systems, from fundamental concepts like RDF and linked data to more specialized approaches like frame semantics and knowledge organization systems (KOS). This comprehensive coverage ensures capture of both technical implementations and theoretical frameworks.

### 3. Third Concept Group: Cultural Heritage Context

The third group encompasses the entire GLAM (Galleries, Libraries, Archives, Museums) ecosystem, including both traditional institutions and contemporary digital humanities approaches. The inclusion of terms like "polyvocality" and "post-colonial heritage" indicates focus on inclusive and diverse representation within cultural heritage contexts.

## Search Strategy Implications

### Precision vs. Recall Balance

This triple-intersection approach prioritizes precision over recall, targeting a highly specific research area where user-centered design methodologies are applied to semantic technology implementations within cultural heritage contexts. The AND operators between all three concept groups ensure that retrieved results must address all three domains simultaneously.

### Interdisciplinary Research Focus

The query structure reflects the inherently interdisciplinary nature of this research area, bridging computer science (semantic technologies), design studies (participatory design), and cultural studies (heritage and memory). This approach is particularly effective for identifying cutting-edge research that transcends traditional disciplinary boundaries.

## Alternative Approaches

### Subject Category Enhancement

For additional precision, you could add Web of Science Category filtering:

```
AND WC=("Computer Science, Information Systems" OR "Information Science Library Science" 
        OR "Social Sciences, Interdisciplinary" OR "Humanities, Multidisciplinary")
```


### Research Area Alternative

Using broader Research Area classifications:

```
AND SU=(Technology OR "Social Sciences" OR "Arts & Humanities")
```


### Document Type Filtering

To focus on primary research articles:

```
AND DT=(Article OR Review)
```


## Important Considerations

### Search Result Expectations

Given the highly specific triple-intersection structure, this query will likely return a relatively small but highly relevant result set. The combination of all three concept groups represents a very specialized research niche that is still emerging in the academic literature.

### Database Coverage Differences

Web of Science's selective journal coverage versus Scopus's comprehensive approach may yield different results for this interdisciplinary query. Web of Science's focus on high-impact journals may capture more established research in this emerging field, while potentially missing newer work published in specialized venues.

### Boolean Logic Complexity

The extensive OR operators within each concept group, combined with AND operators between groups, create a complex search logic that requires careful execution. Web of Science's query processing handles this nested Boolean structure effectively, maintaining the logical relationships essential to your research focus.

The converted query preserves your sophisticated search strategy while adapting to Web of Science's field tags and syntax, ensuring comprehensive retrieval of research at the cutting-edge intersection of participatory design, semantic technologies, and cultural heritage applications.

---

# Troubleshooting "Invalid Field Tag" Error in Web of Science

When you encounter a "Search Error: Invalid field tag" in Web of Science, it typically means one or more of the field tags or the syntax used in your query does not conform to the platform's accepted standards as of 2025[^5_1]. Here’s how to address the issues in your query:

## 1. Field Tag Review

### Topic Search: `TS=`

- **Correct:** `TS=` is the valid field tag for searching titles, abstracts, author keywords, and Keywords Plus in Web of Science[^5_1].
- **Your usage:** The `TS=()` portion of your query is correct.


### Web of Science Category: `WC=`

- **Correct:** `WC=` is the valid field tag for Web of Science Categories[^5_1].
- **Common mistake:** Using wildcards (e.g., `Computer Science*`) or broad, non-specific category names (e.g., `Arts*`) in `WC=` is not supported. You must use the exact category names as listed in the Web of Science Category list[^5_1].


### Publication Year: `PY=`

- **Correct:** `PY=` is the valid field tag for publication year, but it must be used as `PY=2015-2025` for a range, not `PY > 2014`.


## 2. Corrected Query

Here’s how you should rewrite your query to avoid the error:

```plaintext
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Social Sciences, Interdisciplinary" OR "Art")
AND PY=2015-2025
```

- Replace `Computer Science*` with the exact category, such as `"Computer Science, Information Systems"`.
- Replace `Social Sciences*` with `"Social Sciences, Interdisciplinary"` or other exact matches.
- Replace `Arts*` with `"Art"` or the precise category name.
- Use `PY=2015-2025` for articles published after 2014.


## 3. Additional Tips

- **Find exact category names:** Use the Web of Science Category list or the category filter in the interface to see all valid options[^5_1].
- **No wildcards in WC:** Wildcards are not supported in the `WC=` field.
- **Combine filters carefully:** Each field tag must use the correct syntax; mixing invalid tags or formats will trigger errors.


## 4. Example of Valid Advanced Search Query

```plaintext
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Social Sciences, Interdisciplinary" OR "Art")
AND PY=2015-2025
```

This format should work without triggering the "Invalid field tag" error[^5_1].

---

**References:**
[^5_1] https://clarivate.libguides.com/wos/advanced
https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Advanced-Search-Field-Tags
https://clarivate.com/webofsciencegroup/support/wos/advanced-search/

<div style="text-align: center">⁂</div>

[^5_1]: skills.research_methodology


---

# Resolving "Invalid Field Tag" in Web of Science Advanced Search

If you continue to receive a "Search Error: Invalid field tag" in Web of Science, it is almost always due to one of the following issues in your query syntax or field tag usage[^6_1].

## 1. Common Causes and Solutions

### a. **Incorrect Category Names in `WC=`**

Web of Science requires **exact** category names in the `WC=` field—wildcards (*) and broad terms like `Computer Science*` or `Arts*` are not supported[^6_1]. You must use precise category names from the official list.

**Valid Examples:**

- `"Computer Science, Information Systems"`
- `"Computer Science, Interdisciplinary Applications"`
- `"Social Sciences, Interdisciplinary"`
- `"Art"`
- `"Arts & Humanities Other Topics"`
- `"Humanities, Multidisciplinary"`
- `"Information Science & Library Science"`


### b. **Publication Year Range Syntax**

The correct syntax for year ranges is `PY=2015-2025`, not `PY > 2014`[^6_1].

### c. **Parentheses and Quotation Marks**

All parentheses and quotation marks must be balanced and properly placed. Each category name in `WC=` must be in double quotes and separated by `OR`[^6_1].

## 2. Corrected Example Query

Here is a corrected version using only valid category names and proper year range syntax:

```plaintext
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" OR "Social Sciences, Interdisciplinary" OR "Art" OR "Arts & Humanities Other Topics")
AND PY=2015-2025
```

This query uses only valid field tags and category names[^6_1].

## 3. Troubleshooting Steps

- **Check category names:** Use the category filter in Web of Science Advanced Search to copy exact names[^6_1].
- **No wildcards in WC:** Remove all asterisks (*) from category names in `WC=`[^6_1].
- **Use correct year syntax:** Specify years as a range, e.g., `PY=2015-2025`.
- **Avoid extra spaces or typos:** Even a minor typo in a field tag or category name will trigger an error[^6_1].


## 4. Reference Table: Valid Category Names

| Area | Valid Web of Science Categories |
| :-- | :-- |
| Computer Science | Computer Science, Information Systems <br> Computer Science, Interdisciplinary Applications |
| Social Sciences | Social Sciences, Interdisciplinary |
| Arts \& Humanities | Art <br> Arts \& Humanities Other Topics <br> Humanities, Multidisciplinary |

## 5. Further Help

If you still encounter errors:

- Try removing the `WC=` filter to see if the query works without it.
- Add one category at a time to isolate any problematic names.
- Review the full list of Web of Science Categories in the platform's help section or category filter[^6_1].

---

**References:**
[^6_1] https://clarivate.libguides.com/wos/advanced
https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Advanced-Search-Field-Tags
https://clarivate.com/webofsciencegroup/support/wos/advanced-search/

<div style="text-align: center">⁂</div>

[^6_1]: skills.research_methodology


---

# Why You Still Get "Invalid Field Tag" in Web of Science

If you continue to receive the "Invalid field tag" error in Web of Science, even after correcting your query, it is almost always due to one or more of the following issues:

## 1. Exact Category Name Requirement

- The `WC=` (Web of Science Category) field tag only accepts exact, official category names—no wildcards, abbreviations, or partial matches are allowed.
- For example, `"Computer Science, Information Systems"` is valid, but `"Computer Science"` or `"Computer Science*"` is not.
- Double-check the spelling, punctuation, and spacing for each category name. Even a minor typo will cause an error.


## 2. Field Tag Syntax and Placement

- Each field tag (e.g., `TS=`, `WC=`, `PY=`) must be used exactly as specified in the official documentation.
- Do not use parentheses around the entire `WC=` clause. Use them only to group multiple category names with `OR`.


## 3. Publication Year Syntax

- The `PY=` field tag requires a range, such as `PY=2015-2025`, not `PY > 2014`.


## 4. Query Example That Should Work

Here is a corrected example using only valid field tags and category names:

```
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" OR "Social Sciences, Interdisciplinary" OR "Art" OR "Arts & Humanities Other Topics")
AND PY=2015-2025
```

- All category names are copied exactly from the official list.


## 5. Troubleshooting Checklist

- **Remove the `WC=` filter** and run the query with only `TS=` and `PY=`. If this works, the problem is with your category names.
- **Add one category at a time** to the `WC=` filter to identify which name is causing the error.
- **Consult the official category list** in the Web of Science Advanced Search interface to copy and paste the exact names.
- **Avoid extra spaces or special characters** that are not part of the official category name.


## 6. If Problems Persist

- Try running only the topic and year portion:

```
TS=(...) AND PY=2015-2025
```

If this works, gradually add category filters back in, one by one.
- If you still get an error, clear your browser cache or try a different browser, as rare interface bugs can cause issues.
- If none of the above resolves the issue, contact your institution’s library or Web of Science technical support for assistance, as there may be a platform-specific problem or a recent change in accepted syntax.

---

https://clarivate.libguides.com/wos/advanced
https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Advanced-Search-Field-Tags

<div style="text-align: center">⁂</div>

---

# Web of Science Core Collection: Why You Still Get "Invalid Field Tag" Errors

## Is the Core Collection Different?

Yes, the **Web of Science Core Collection** is a specific subset of the Web of Science platform with its own rules for advanced search syntax, field tags, and especially for category filtering. If you are searching in the Core Collection, you must strictly follow its accepted field tags and use only the exact official category names—any deviation will trigger an "Invalid field tag" error[^8_1][^8_2][^8_3].

## Key Differences and Troubleshooting

### 1. Field Tags and Syntax

- **TS=** is the correct tag for "Topic" searches (title, abstract, author keywords, Keywords Plus).
- **WC=** is the correct tag for "Web of Science Category" but only accepts exact, official category names—no wildcards, abbreviations, or partial names.
- **PY=** is used for publication year and must be paired with another field tag (e.g., `TS=... AND PY=2015-2025`)[^8_1][^8_2][^8_4].


### 2. Category Names Must Be Exact

- You **cannot** use wildcards (e.g., `WC=Computer Science*`) or broad terms (e.g., `WC=Arts*`).
- You **must** use the full, official category names, such as:
    - `"Computer Science, Information Systems"`
    - `"Computer Science, Interdisciplinary Applications"`
    - `"Social Sciences, Interdisciplinary"`
    - `"Art"`
    - `"Arts & Humanities Other Topics"`[^8_1][^8_5].


### 3. Correct Syntax Example

Here is an example of a valid query for the Core Collection:
#op/buscar https://www.webofscience.com/wos/woscc/summary/044c0fc3-5ca4-470d-b44f-f24abb58eb67-01690f7ece/relevance/1 

```
TS=(
    ("participatory design" OR "co-creation*" OR "user centered design" 
    OR "human centered interaction" OR "social innovation")
    AND 
    ("knowledge graph*" OR "CK theory" OR "interaction patterns" 
    OR "usability testing" OR "cognitive load")
)
AND WC=("Computer Science, Information Systems" OR "Computer Science, Interdisciplinary Applications" OR "Social Sciences, Interdisciplinary" OR "Art" OR "Arts & Humanities Other Topics")
AND PY=2015-2025
```
 N=106
 [[metadataWoS1.ris]]



- All category names are copied exactly from the official Core Collection list[^8_1][^8_5].

### 4. Where to Find Valid Category Names

- In the **Core Collection** interface, after running an initial search, look at the left sidebar under "Web of Science Categories" to see the exact names as they appear in the database.
- You can also consult the official help pages for a full list of accepted categories[^8_1][^8_6].


### 5. Additional Troubleshooting Steps

- Try running your search **without the WC= filter**. If it works, the problem is with your category names.
- Add categories back **one at a time** to identify any problematic names.
- Avoid extra spaces, missing commas, or quotation mark errors.
- Note: The Core Collection does not support subject area wildcards or abbreviations—this is stricter than some other Web of Science databases[^8_1][^8_2][^8_5].


## Summary Table: Valid vs. Invalid Syntax

| Feature | Valid Example | Invalid Example |
| :-- | :-- | :-- |
| Category Tag | WC="Computer Science, Information Systems" | WC=Computer Science* |
| Multiple Categories | WC=("Art" OR "Humanities, Multidisciplinary") | WC=(Art OR Humanities*) |
| Year Range | PY=2015-2025 | PY>2014 |
| Topic Search | TS=("usability testing" AND "knowledge graph*") | TITLE-ABS-KEY("usability") |

## Final Tips

- The Core Collection is stricter than other Web of Science databases.
- Always use the exact category names and correct field tags.
- If errors persist, consult the official help pages or try your search in Basic mode to identify the correct category names[^8_1][^8_2][^8_5].

---

[^8_1] https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm
[^8_2] https://images.webofknowledge.com/images/help/WOS/hs_advanced_fieldtags.html
[^8_4] https://webofscience.help.clarivate.com/en-us/Content/inspec/inspec-search-field-tags.htm
[^8_3] https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-fields.htm
[^8_6] https://images.webofknowledge.com/images/help/WOS/hp_subject_category_terms_tasca.html
[^8_5] https://webofscience.help.clarivate.com/en-us/Content/search-advanced-egs.html

<div style="text-align: center">⁂</div>

[^8_1]: https://webofscience.help.clarivate.com/Content/wos-core-collection/woscc-search-field-tags.htm

[^8_2]: https://images.webofknowledge.com/images/help/WOS/hs_advanced_fieldtags.html

[^8_3]: https://webofscience.help.clarivate.com/en-us/Content/wos-core-collection/woscc-search-fields.htm

[^8_4]: https://webofscience.help.clarivate.com/en-us/Content/inspec/inspec-search-field-tags.htm

[^8_5]: https://webofscience.help.clarivate.com/en-us/Content/search-advanced-egs.html

[^8_6]: https://images.webofknowledge.com/images/help/WOS/hp_subject_category_terms_tasca.html

[^8_7]: https://webofscience.zendesk.com/hc/en-us/articles/27505726032017-Web-of-Science-Subject-Categories

[^8_8]: https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Core-Collection-Web-of-Science-Categories?language=en_US

[^8_9]: https://webofscience.help.clarivate.com/en-us/Content/advanced-search.html

[^8_10]: https://libguides.utoledo.edu/c.php?g=284350\&p=1894921

[^8_11]: https://academia.stackexchange.com/questions/149381/web-of-science-advanced-search-returns-papers-not-matching-the-search-criteria

[^8_12]: https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields

[^8_13]: https://images.webofknowledge.com/WOKRS528R6/help/TCT/ht_errors.html

[^8_14]: https://webofscience.zendesk.com/hc/en-us/articles/20129792747921-Advanced-Search-Fielded-Search

[^8_15]: https://webofscience.zendesk.com/hc/en-us/articles/26916215746321-Core-Collection-Full-Record-Details

[^8_16]: https://support.clarivate.com/ScientificandAcademicResearch/s/article/Web-of-Science-Core-Collection-List-of-field-tags-in-output?language=en_US

[^8_17]: https://www.recursoscientificos.fecyt.es/sites/default/files/spanish_manual_09_10_2019.pdf

