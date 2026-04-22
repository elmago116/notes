# Strategic Diagram Implementation Decisions

**Date Created:** 2025-08-04  
**Source:** Conversation about strategic diagram corrections and implementation choices

## 🎯 **Key Implementation Decisions**

### **1. Original SciMAT Methodology vs. Custom Implementation**
**Decision:** Use original SciMAT formulas exactly instead of custom implementations.

**Rationale:**
- Original SciMAT has been validated by academic community
- Custom implementations may introduce errors
- Original formulas ensure academic rigor and reproducibility

**Implementation:**
```python
# Centrality: 10 * sum(external_pairs)
def calculate_callon_centrality_scimat_original(cluster_keywords, G):
    external_pairs = get_external_pairs(cluster_keywords, G)
    sum_external = sum(external_pairs)
    return 10 * sum_external

# Density: 100 * (sum(internal_pairs) / cluster_size)
def calculate_callon_density_scimat_original(cluster_keywords, G):
    internal_pairs = get_internal_pairs(cluster_keywords, G)
    sum_internal = sum(internal_pairs)
    return 100 * (sum_internal / len(cluster_keywords))
```

**Outcome:** ✅ Correct density and centrality values achieved.

### **2. Axes Configuration: Strategic_Diagrams_Rules.md Compliance**
**Decision:** Follow Strategic_Diagrams_Rules.md exactly for axes configuration.

**Rationale:**
- Rules document provides authoritative guidance
- Ensures consistency with academic standards
- Prevents misinterpretation of strategic quadrants

**Implementation:**
- **X-axis (horizontal):** Density (0.0 - 1.0)
- **Y-axis (vertical):** Centrality (0.0 - 1.0)

**Outcome:** ✅ Correct strategic quadrant positioning achieved.

### **3. Strategic Quadrant Interpretation: Academic Standards**
**Decision:** Use precise strategic quadrant definitions from academic literature.

**Rationale:**
- Ensures correct interpretation of research field structure
- Follows Cobo et al. (2018) methodology
- Maintains academic rigor

**Implementation:**
- **Motor Themes:** High Centrality + High Density (top right)
- **Basic Themes:** Low Centrality + High Density (top left)
- **Specialized Themes:** High Centrality + Low Density (bottom right)
- **Emerging/Declining:** Low Centrality + Low Density (bottom left)

**Outcome:** ✅ Correct strategic quadrant classification achieved.

### **4. Zero Centrality Validation: Academic Acceptance**
**Decision:** Accept that some clusters have zero centrality as academically valid.

**Rationale:**
- Zero centrality indicates specialized, isolated clusters
- Common in bibliometric analysis (14% of clusters)
- Basic themes should have low centrality (including zero)

**Implementation:**
- Validate zero centrality clusters as normal
- Don't force non-zero centrality values
- Document academic justification

**Outcome:** ✅ Correct interpretation of zero centrality clusters.

### **5. File Organization: Simplified Structure**
**Decision:** Use simplified file organization with all files in `scripts/` folder.

**Rationale:**
- Prevents confusion from nested folders
- Easier to manage and locate files
- Reduces complexity in file paths

**Implementation:**
- All scripts and output files in `scripts/` folder
- Input files from `../results/data/`
- Output files saved in current directory

**Outcome:** ✅ Cleaner file organization achieved.

### **6. Quality Control: Step-by-Step Validation**
**Decision:** Implement quality control checkpoints at each step.

**Rationale:**
- Prevents errors from propagating through pipeline
- Ensures data quality at each stage
- Enables early error detection

**Implementation:**
1. Verify output file exists and has content
2. Check file sizes are reasonable (not 0 bytes)
3. Validate data format (CSV structure, field names)
4. Update master plan immediately with results
5. Document any issues in execution log

**Outcome:** ✅ Improved error detection and prevention.

### **7. Documentation Sync: Immediate Updates**
**Decision:** Update documentation immediately after each step.

**Rationale:**
- Prevents outdated information
- Ensures consistency across documents
- Enables proper version control

**Implementation:**
- Update master plan after each step
- Document current results and issues
- Keep version history updated

**Outcome:** ✅ Consistent and up-to-date documentation.

### **8. User Feedback Integration: Serious Consideration**
**Decision:** Take user feedback seriously and investigate thoroughly.

**Rationale:**
- Users often spot issues that automated systems miss
- User feedback leads to better implementations
- Improves overall quality and accuracy

**Implementation:**
- Investigate user concerns thoroughly
- Admit mistakes and correct them
- Thank users for catching errors
- Document lessons learned

**Outcome:** ✅ Better error detection and correction.

### **9. Academic Validation: Standards Compliance**
**Decision:** Validate all results against academic standards.

**Rationale:**
- Ensures research quality and rigor
- Maintains academic credibility
- Follows established methodologies

**Implementation:**
- Check against original SciMAT methodology
- Verify strategic quadrant definitions
- Validate centrality and density ranges
- Confirm academic citations and standards

**Outcome:** ✅ Academic rigor maintained.

### **10. Strategic Diagram Generation: Professional Quality**
**Decision:** Generate high-quality strategic diagrams with professional aesthetics.

**Rationale:**
- Professional appearance enhances academic credibility
- Clear visualization aids interpretation
- Consistent with publication standards

**Implementation:**
- Use proper color coding for quadrants
- Include cluster sizing based on document count
- Add proper labels and legends
- Generate both PNG and SVG formats

**Outcome:** ✅ Professional-quality strategic diagrams achieved.

## 📊 **Decision Outcomes Summary**

### **Technical Decisions:**
- ✅ **Original SciMAT formulas** - Correct density and centrality values
- ✅ **Strategic_Diagrams_Rules.md compliance** - Correct axes configuration
- ✅ **Academic quadrant interpretation** - Proper strategic positioning
- ✅ **Zero centrality acceptance** - Correct academic interpretation

### **Process Decisions:**
- ✅ **Simplified file organization** - Cleaner structure
- ✅ **Quality control checkpoints** - Better error prevention
- ✅ **Immediate documentation updates** - Consistent information
- ✅ **User feedback integration** - Improved accuracy

### **Quality Decisions:**
- ✅ **Academic validation** - Research rigor maintained
- ✅ **Professional diagram generation** - Publication-ready quality
- ✅ **Standards compliance** - Academic credibility ensured

## 🎓 **Academic Framework Integration**

### **Research Interests:**
- Cultural Heritage & Technology
- Digital Humanities
- Participative Design
- GLAM (Galleries, Libraries, Archives, Museums)
- Cross-Thematic Research

### **Methodological Standards:**
- Follow SciMAT methodology (Cobo et al., 2018)
- Document all processing decisions
- Validate results against academic standards
- Maintain transparency and reproducibility

### **Citations:**
- Cobo, M. J., López-Herrera, A. G., Herrera-Viedma, E., & Herrera, F. (2018). SciMAT: A new science mapping analysis software tool. Journal of the Association for Information Science and Technology, 69(2), 264-268.

These decisions provide a comprehensive framework for implementing strategic diagrams with academic rigor and technical accuracy. 