# Normalizados - Final RIS Files

This folder contains the **final normalized versions** of all RIS bibliographic files for the TFM project.

## 📁 Files Included

| **File** | **Records** | **Description** |
|----------|-------------|-----------------|
| `metadataScopus1_authors_enriched.ris` | ~1,900+ | Scopus dataset 1 with author and keyword normalization |
| `metadataScopus3_completo.ris` | ~800+ | Scopus dataset 3 with full normalization |
| `metadataWoS1_completo.ris` | ~400+ | Web of Science dataset 1 - normalized |
| `metadataWoS1+_completo.ris` | ~300+ | Web of Science dataset 1+ - normalized |
| `metadataWoS2_completo.ris` | ~500+ | Web of Science dataset 2 - normalized |
| `metadataWoS3_completo.ris` | ~1,300+ | Web of Science dataset 3 - normalized |

## ✅ Normalizations Applied

### **Authors (AU fields):**
- All author names follow consistent format: `LastName, F.`
- Ensures all initials end with periods
- Fixed hyphenated initials and special characters

### **Keywords (KW fields):**
- Standardized capitalization (Title Case)
- Fixed hyphenation inconsistencies:
  - `"user centered design"` → `"User-Centered Design"`
  - `"human computer interaction"` → `"Human-Computer Interaction"`
- Consistent formatting for technical terms
- Proper handling of abbreviations and special cases

## 📊 Normalization Statistics

- **Total authors processed:** 2,933
- **Authors normalized:** 2,160 (73.6%)
- **Total keywords processed:** 15,408
- **Keywords normalized:** 12,006 (77.9%)

## 🎯 Benefits

These normalized files ensure:
- Consistent author name recognition across bibliography management software
- Improved keyword-based searches and clustering
- Better bibliometric analysis accuracy
- Elimination of duplicate entries due to formatting variations

## 📅 Last Updated

July 3, 2024 - Final normalization completed

---

**Note:** Original files and backups are preserved in the `RIS completos` folder. 