# README - Ensayos Folder

## 📋 Overview

This folder contains experimental drafts and comparative analyses of database transformations for the HerStory project. The documents here serve as working prototypes for understanding different approaches to knowledge graph construction.

---

## 🔄 Recent Changes - Version Update

### **Modified Files:**

#### `Censura digram replica.md` - Major Update

**Previous Version:**
- Single Mermaid diagram with Cultura y Censura database only
- 23 entities focused on censorship documentation
- Linear ER diagram without sectioning

**New Version:**
- **Comprehensive dual-database documentation**
- **Structured format** with clear sections and comparative analysis
- **Complete database coverage** of both historical projects

---

## 📊 Detailed Changes

### **1. Document Structure Enhancement**

#### **Added:**
- **Main title**: "Diagrama ER Combinado - Cultura y Censura + SIDBRINT"
- **Section headers**: 
  - "## Base de Datos Cultura y Censura"
  - "## Base de Datos SIDBRINT"
- **Organized layout** with clear separation between databases

#### **Enhanced:**
- **Documentation comments** (`%% ===== DATABASE SECTIONS =====`)
- **Relationship grouping** with clear visual separation
- **Professional formatting** for academic/technical reference

### **2. Database Coverage Expansion**

#### **SIDBRINT Database Addition:**
- **26 new entities** covering International Brigade documentation
- **Central entity**: `BRIGADISTES` with comprehensive biographical data
- **Multi-dimensional relationships** across 6 thematic areas:

| **Theme** | **Entities** | **Purpose** |
|-----------|--------------|-------------|
| **Personal Identity** | `BRIGADISTES`, `PROFESSIONS`, `PROCEDENCIA_RELIGIO_ETNIA` | Individual characteristics |
| **Political Context** | `IDEOLOGIES_POLITIQUES`, `ORGANITZACIONS`, `MOVIMENTS` | Political affiliations |
| **Historical Events** | `ESDEVENIMENTS`, `PRESONS_CAMPS`, `ESPAIS_SANITARIS` | Life experiences |
| **Documentary Sources** | `FONTS`, `IDIOMES`, `ENFOCAMENTS`, `TIPUS_DOCUMENTAL` | Source documentation |
| **Cultural Context** | `CULTURA`, `LITERATURA_MITJANS_COMUNICACIO` | Cultural references |
| **Operational Structure** | `ESTRUCTURES` | Military organization |

#### **Relationship Mapping:**
- **67 new relationships** with descriptive labels in Catalan
- **Hub-and-spoke pattern** with `BRIGADISTES` as central node
- **Many-to-many relationships** through junction tables

### **3. Comparative Analysis Integration**

#### **Database Comparison:**

| **Aspect** | **Cultura y Censura** | **SIDBRINT** |
|------------|----------------------|--------------|
| **Entities** | 23 | 26 |
| **Focus** | Administrative processes | Biographical documentation |
| **Complexity** | Linear workflows | Multi-dimensional relationships |
| **Entity Types** | Documents, roles, institutions | People, contexts, sources |
| **Relationships** | Process-driven | Attribute-driven |
| **Language** | Spanish | Catalan |
| **Time Period** | Franco dictatorship | Spanish Civil War |

---

## 🎯 Technical Improvements

### **1. Mermaid Syntax Enhancement**
- **Proper sectioning** with comment blocks
- **Consistent formatting** across both diagrams
- **Improved readability** with organized entity definitions
- **Professional relationship labeling** with descriptive names

### **2. Data Modeling Accuracy**
- **Complete field mapping** from DrawIO source files
- **Accurate foreign key relationships** 
- **Proper primary key identification** with "PK" notation
- **Consistent naming conventions** within each database

### **3. Documentation Standards**
- **Academic-quality formatting** suitable for research documentation
- **Bilingual support** (Spanish for Censura, Catalan for SIDBRINT)
- **Clear visual hierarchy** with proper markdown structure
- **Version control ready** with structured changes

---

## 🔍 Impact Analysis

### **Research Value:**
- **Comprehensive comparison** of two historical documentation approaches
- **Methodological insights** for knowledge graph construction
- **Template for future** database integration projects

### **Technical Value:**
- **Reusable Mermaid diagrams** for presentations and documentation
- **Complete entity mapping** for data migration projects
- **Relationship modeling** examples for complex historical databases

### **Educational Value:**
- **Practical examples** of different database design philosophies
- **Historical context** for understanding documentation challenges
- **Comparative methodology** for evaluating database approaches

---

## 📝 Files in This Folder

| **File** | **Purpose** | **Status** |
|----------|-------------|------------|
| `Censura digram replica.md` | **Updated** - Combined database diagrams | ✅ Current |
| `Inventario de transformaciones Censura.md` | UB transformation rules for Censura | 📋 Reference |
| `Inventario de transformaciones SIDBRINT.md` | UB transformation rules for SIDBRINT | 📋 Reference |
| `UB-Peninsula firsts drafts.md` | Comparative entity mapping | 📋 Reference |
| `README.md` | **New** - This documentation file | 📋 Current |

---

## 🚀 Next Steps

1. **Validation**: Verify diagram accuracy against source databases
2. **Integration**: Consider cross-database relationship possibilities
3. **Documentation**: Expand comparative analysis with Peninsula mappings
4. **Optimization**: Streamline diagram rendering for large datasets

---

## 📧 Contact

For questions about these changes or the database comparison methodology, refer to the main HerStory project documentation.

**Last Updated**: January 2025  
**Version**: 2.0 - Dual Database Integration 