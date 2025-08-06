# SciMAT Analysis Implementation Plan

**Date Created:** 2025-08-04  
**Source:** Conversation about SciMAT analysis implementation and strategic diagram corrections

## 🎯 **Implementation Strategy**

### **Pre-Implementation Checklist**
Before starting any step, verify:
- ✅ **Script versions:** Use enhanced scripts (773-line `normalize_ris.py`, not empty versions)
- ✅ **Data quality:** Check source data limitations (58.7% keyword coverage is normal)
- ✅ **Field preservation:** Ensure SRC fields are maintained throughout pipeline
- ✅ **Documentation sync:** Update master plan immediately after each step

### **Step-by-Step Implementation with Error Prevention**

#### **Step 1: Keyword Extraction**
```bash
# ✅ CORRECT APPROACH
python3 extract_keywords_by_period.py "TFM1.ris" keywords_by_period.json
```
**Prevention measures:**
- Verify TFM1.ris exists and has SRC fields preserved
- Check keyword coverage (expect ~58.7% from source data quality)
- Don't assume 100% keyword coverage is possible

#### **Step 2: Co-occurrence Networks**
```bash
# ✅ CORRECT APPROACH
python3 build_cooccurrence_networks.py keywords_by_period.json cooccurrence_
```
**Prevention measures:**
- Verify inclusion index normalization is applied
- Check network sizes increase over time (19KB → 1.3MB → 6.0MB)
- Ensure proper keyword quoting for commas in keyword names

#### **Step 3: Clustering**
```bash
# ✅ CORRECT APPROACH
python3 cluster_networks.py cooccurrence_ clusters_by_period.csv
```
**Prevention measures:**
- Use simple centers algorithm as specified
- Expect 20 clusters per period (max constraint)
- Verify center selection and distance calculations
- Check cluster size constraints (min 3, max 12 nodes)

#### **Step 4: Strategic Measures**
```bash
# ✅ CORRECT APPROACH
python3 calculate_strategic_measures_scimat_original.py
```
**Prevention measures:**
- Use corrected density calculation (100 × (sum_internal / cluster_size))
- Verify density values range from 300-6600 (proper SciMAT scale)
- Apply corrected strategic interpretation (Cobo et al., 2018)
- Check for zero centrality issues (common mistake)

### **Quality Control Checkpoints**

#### **After Each Step:**
1. **Verify output file exists and has content**
2. **Check file sizes are reasonable** (not 0 bytes)
3. **Validate data format** (CSV structure, field names)
4. **Update master plan immediately** with results
5. **Document any issues** in the execution log

#### **Common Error Prevention:**
- **Regex patterns:** Test with actual data, handle 3-character field codes
- **Source tracking:** Preserve SRC fields throughout pipeline
- **Data quality:** Distinguish processing errors from source limitations
- **Script versions:** Use enhanced scripts with comprehensive features

### **Strategic Diagram Generation**

#### **Correct Configuration:**
- **X-axis (horizontal):** Density (0.0 - 1.0)
- **Y-axis (vertical):** Centrality (0.0 - 1.0)
- **Strategic quadrants:** Follow Strategic_Diagrams_Rules.md exactly

#### **Strategic Quadrant Positioning:**
- **Motor Themes:** High Centrality + High Density (top right)
- **Basic Themes:** Low Centrality + High Density (top left)
- **Specialized Themes:** High Centrality + Low Density (bottom right)
- **Emerging/Declining:** Low Centrality + Low Density (bottom left)

### **Expected Results**

#### **Strategic Measures Distribution:**
- **Previous_2013:** 3 clusters (1 Motor, 0 Basic, 1 Specialized, 1 Emerging/Declining)
- **2014-2019:** 20 clusters (2 Motor, 4 Basic, 13 Specialized, 1 Emerging/Declining)
- **2020-2025:** 20 clusters (0 Motor, 7 Basic, 12 Specialized, 1 Emerging/Declining)
- **Total:** 43 clusters (3 Motor, 11 Basic, 26 Specialized, 3 Emerging/Declining)

#### **Centrality Zero Validation:**
- **6 out of 43 clusters** have zero centrality (14%)
- **This is academically valid** - indicates specialized, isolated clusters
- **Basic themes** should have low centrality (including zero)

### **Academic Framework Integration**

#### **Research Interests:**
- Cultural Heritage & Technology
- Digital Humanities
- Participative Design
- GLAM (Galleries, Libraries, Archives, Museums)
- Cross-Thematic Research

#### **Methodological Rigor:**
- Follow SciMAT methodology (Cobo et al., 2018)
- Document all processing decisions
- Validate results against academic standards
- Maintain transparency and reproducibility

## 🚀 **Ready to Implement**

With this knowledge-based approach, you can:
1. **Avoid common mistakes** identified in lessons learned
2. **Follow proven workflows** from successful implementations
3. **Maintain quality control** at each step
4. **Document progress** for academic rigor
5. **Achieve reproducible results** for TFM analysis

The extracted knowledge provides a comprehensive roadmap for successful implementation without repeating the mistakes encountered during the original development process. 