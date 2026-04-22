# Strategic Diagram Lessons Learned

**Date Created:** 2025-08-04  
**Source:** Conversation about strategic diagram corrections and implementation challenges

## 🚨 **Critical Lessons Learned**

### **1. Axes Configuration is Critical**
**Lesson:** The axes configuration in strategic diagrams must follow the Strategic_Diagrams_Rules.md exactly.

**❌ WRONG Approach:**
- Assuming X-axis = Centrality, Y-axis = Density
- Not checking the rules document carefully

**✅ CORRECT Approach:**
- **X-axis (horizontal):** Density (0.0 - 1.0)
- **Y-axis (vertical):** Centrality (0.0 - 1.0)
- Always verify against Strategic_Diagrams_Rules.md

**Impact:** Wrong axes configuration leads to incorrect strategic quadrant positioning and misinterpretation of results.

### **2. Density Formula Must Follow Original SciMAT**
**Lesson:** The density calculation must use the original SciMAT formula exactly.

**❌ WRONG Implementation:**
```python
return 1000 * sum_internal  # Missing division by cluster size
```

**✅ CORRECT Implementation:**
```python
return 100 * (sum_internal / cluster_size)  # Original SciMAT formula
```

**Impact:** Wrong density formula leads to unrealistic values and incorrect strategic positioning.

### **3. Zero Centrality is Academically Valid**
**Lesson:** Some clusters having zero centrality is normal and academically valid.

**❌ WRONG Assumption:**
- Assuming all clusters should have non-zero centrality
- Thinking zero centrality indicates an error

**✅ CORRECT Understanding:**
- **6 out of 43 clusters** have zero centrality (14%)
- **Basic themes** should have low centrality (including zero)
- Zero centrality indicates specialized, isolated clusters

**Impact:** Misinterpreting zero centrality as an error leads to unnecessary corrections and confusion.

### **4. Strategic Quadrant Interpretation Must Be Precise**
**Lesson:** Strategic quadrant positioning must follow the exact rules.

**✅ CORRECT Strategic Quadrants:**
- **Motor Themes:** High Centrality + High Density (top right)
- **Basic Themes:** Low Centrality + High Density (top left)
- **Specialized Themes:** High Centrality + Low Density (bottom right)
- **Emerging/Declining:** Low Centrality + Low Density (bottom left)

**Impact:** Incorrect quadrant interpretation leads to wrong research conclusions.

### **5. Original SciMAT Code Analysis is Essential**
**Lesson:** Always verify against the original SciMAT Java code for correct formulas.

**✅ CORRECT Process:**
- Analyze original SciMAT Java code
- Extract exact formulas for centrality and density
- Implement Python version that matches exactly
- Validate against academic standards

**Impact:** Without original code analysis, implementations may deviate from the intended methodology.

### **6. File Organization Rules Prevent Confusion**
**Lesson:** All scripts and files must be organized in the correct folder structure.

**❌ WRONG Approach:**
- Creating files in multiple nested folders
- Creating `results/`, `SciMAT-v1.1.04/`, multiple `scripts/` folders

**✅ CORRECT Approach:**
- All files go directly in `scripts/` folder
- Use relative paths: `../results/data/` for input
- Save output files in current directory (`scripts/`)

**Impact:** Poor file organization leads to confusion and lost files.

### **7. Quality Control Checkpoints Are Essential**
**Lesson:** Implement quality control checkpoints at each step.

**✅ CORRECT Checkpoints:**
1. **Verify output file exists and has content**
2. **Check file sizes are reasonable** (not 0 bytes)
3. **Validate data format** (CSV structure, field names)
4. **Update master plan immediately** with results
5. **Document any issues** in the execution log

**Impact:** Missing checkpoints leads to undetected errors and incorrect results.

### **8. Documentation Sync is Critical**
**Lesson:** Update documentation immediately after each step.

**❌ WRONG Approach:**
- Delaying documentation updates
- Not updating master plan with current results

**✅ CORRECT Approach:**
- Update master plan immediately after each step
- Document current results and any issues
- Keep version history updated

**Impact:** Outdated documentation leads to confusion and incorrect assumptions.

### **9. User Feedback Must Be Taken Seriously**
**Lesson:** When users point out issues, investigate thoroughly instead of insisting everything is correct.

**❌ WRONG Approach:**
- Insisting everything is correct when user reports issues
- Not investigating user concerns thoroughly

**✅ CORRECT Approach:**
- Take user feedback seriously
- Investigate issues thoroughly
- Admit mistakes and correct them
- Thank users for catching errors

**Impact:** Ignoring user feedback leads to persistent errors and frustration.

### **10. Academic Validation is Essential**
**Lesson:** All results must be validated against academic standards.

**✅ CORRECT Validation:**
- Check against original SciMAT methodology
- Verify strategic quadrant definitions
- Validate centrality and density ranges
- Confirm academic citations and standards

**Impact:** Without academic validation, results may not meet research standards.

## 📋 **Prevention Strategies**

### **Before Starting Any Analysis:**
1. **Read Strategic_Diagrams_Rules.md** thoroughly
2. **Analyze original SciMAT code** for correct formulas
3. **Set up proper file organization** structure
4. **Plan quality control checkpoints** for each step

### **During Implementation:**
1. **Follow step-by-step process** exactly
2. **Verify each step** before proceeding
3. **Update documentation** immediately
4. **Take user feedback** seriously

### **After Completion:**
1. **Validate results** against academic standards
2. **Check strategic quadrant** positioning
3. **Verify axes configuration** is correct
4. **Document lessons learned** for future reference

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

These lessons learned provide a comprehensive guide for avoiding common mistakes in strategic diagram implementation and ensuring academic rigor in bibliometric analysis. 