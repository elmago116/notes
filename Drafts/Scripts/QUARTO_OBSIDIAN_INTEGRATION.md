# Quarto + Obsidian Academic Writing Integration

## Overview

This guide explains how to enhance your academic writing workflow by integrating Quarto with your existing Obsidian setup. Quarto provides native citation management, cross-references, multiple output formats, and better integration with academic databases while preserving your Obsidian-based writing process.

## Benefits of Quarto Integration

1. **Native Citation Management**: BibTeX/CSL support with automatic bibliography generation
2. **Cross-References**: Automatic numbering and linking of figures, tables, equations, sections
3. **Multiple Output Formats**: PDF, HTML, Word, LaTeX from a single source
4. **Code Execution**: Reproducible research with embedded Python/R/Julia code
5. **Academic Database Integration**: Better MCP integration for metadata enrichment
6. **Professional Formatting**: Advanced typography and layout control
7. **Version Control Friendly**: Markdown-based with clean diffs

## Architecture: Obsidian → Quarto Workflow

```
Obsidian (Writing) → Conversion Script → Quarto (.qmd) → Multiple Outputs
     ↓                      ↓                    ↓
Clippings/          BibTeX Export         PDF/HTML/Word
(Draft .md)         (bibliography.bib)
```

## Phase 1: Convert Clippings to BibTeX

### Script: `clippings_to_bibtex.py`

Converts your existing Clippings YAML metadata to BibTeX format for Quarto's native citation system.

**Features:**
- Reads all `.md` files from `Clippings/` folder
- Extracts YAML frontmatter metadata
- Generates BibTeX entries with proper entry types
- Handles multiple authors, DOIs, URLs, page numbers
- Creates `bibliography.bib` in your project root

**Usage:**
```bash
cd Drafts/Scripts
python3 clippings_to_bibtex.py
```

**Output:** `bibliography.bib` with entries like:
```bibtex
@book{vohland2021,
  title = {The Science of Citizen Science},
  author = {Vohland, Katrin and Land-Zandstra, Anne and Ceccaroni, Luisa},
  year = {2021},
  publisher = {Springer},
  doi = {10.1007/978-3-030-58278-4},
  type = {book}
}
```

## Phase 2: Convert Obsidian Links to Quarto Citations

### Script: `obsidian_to_quarto.py`

Converts Obsidian-style links to Quarto citation syntax while preserving your writing workflow.

**Conversion Patterns:**

| Obsidian Format | Quarto Format | Notes |
|----------------|---------------|-------|
| `[[Clippings/file\|Vohland et al., 2021]]` | `@vohland2021` | Direct citation |
| `[[file.pdf#page=45\|Vohland et al., 2021]]` | `@vohland2021 [p. 45]` | With page number |
| `[[Clippings/file\|X]]` | `@citekey` | Placeholder resolved |
| `[[file.pdf#page=45]]` | `@citekey [p. 45]` | PDF link with page |

**Usage:**
```bash
python3 obsidian_to_quarto.py "Draft File.md" --bibliography bibliography.bib
```

**Output:** Creates `.qmd` file ready for Quarto rendering

## Phase 3: Quarto Document Structure

### Basic Quarto Document Template

Create `_quarto.yml` in your project root:

```yaml
project:
  type: default
  output-dir: output

bibliography: bibliography.bib
csl: apa.csl  # APA 7th edition style

format:
  pdf:
    documentclass: article
    citation-style: apa
    fig-dpi: 300
    keep-tex: true
  html:
    theme: cosmo
    citation-style: apa
    toc: true
  docx:
    citation-style: apa
```

### Example Quarto Document (.qmd)

```markdown
---
title: "Your Paper Title"
author: "Elena Gómez, Nuria Ferrán-Ferrer, Miquel Centelles"
date: today
format:
  pdf:
    documentclass: article
    citation-style: apa
---

## Introduction

This study analyzes user integration in semantic AI systems @vohland2021.

Previous research shows [@delgado2023; @capel2023] that participatory design...

## Methodology

As shown in @fricker2007 [p. 15], epistemic justice requires...

## References
```

## Phase 4: Enhanced Features

### 1. Cross-References

Quarto automatically numbers and links figures, tables, equations:

```markdown
#| label: fig-methodology
#| fig-cap: "Analytical Framework"

![Methodology Diagram](path/to/figure.png)

As shown in @fig-methodology, the framework consists of four dimensions.
```

### 2. Code Execution

Embed reproducible analysis:

````markdown
```{python}
#| label: fig-bibliometric
#| fig-cap: "Bibliometric Analysis Results"

import matplotlib.pyplot as plt
# Your analysis code here
```
````

### 3. Academic Database Integration

Use MCP servers (arXiv, Crossref) to enrich BibTeX:

```python
# Script: enrich_bibliography_mcp.py
# Uses arXiv MCP to fetch metadata for papers
# Updates bibliography.bib with complete information
```

## Phase 5: Workflow Integration

### Hybrid Workflow

1. **Write in Obsidian** (Drafts folder)
   - Use Obsidian links: `[[Clippings/file|Vohland et al., 2021]]`
   - Keep your existing workflow
   - Link to PDFs, notes, etc.

2. **Convert to Quarto** (when ready to render)
   ```bash
   python3 obsidian_to_quarto.py "Draft.md"
   ```

3. **Render with Quarto**
   ```bash
   quarto render "Draft.qmd"
   ```

4. **Output Formats**
   - PDF: `output/Draft.pdf`
   - HTML: `output/Draft.html`
   - Word: `output/Draft.docx`

## File Structure

```
Documents/
├── PDF/                          # PDF files (unchanged)
├── Clippings/                     # Obsidian notes (unchanged)
│   └── [document-name].md
├── Drafts/                        # Working drafts
│   ├── [draft].md                # Obsidian format
│   ├── [draft].qmd               # Quarto format (generated)
│   └── Scripts/
│       ├── clippings_to_bibtex.py
│       ├── obsidian_to_quarto.py
│       └── QUARTO_OBSIDIAN_INTEGRATION.md
├── bibliography.bib               # Generated from Clippings
├── _quarto.yml                    # Quarto project config
└── output/                        # Rendered documents
    ├── [draft].pdf
    ├── [draft].html
    └── [draft].docx
```

## Advanced: Academic Database Enrichment

### MCP Integration Script

Enhance your bibliography using MCP servers:

```python
# enrich_with_mcp.py
# 1. Reads bibliography.bib
# 2. For entries with arXiv IDs, fetches metadata via arXiv MCP
# 3. For entries with DOIs, enriches via Crossref MCP
# 4. Updates bibliography.bib with complete metadata
```

**Benefits:**
- Automatic metadata completion
- DOI resolution
- Author disambiguation
- Journal information
- Abstract retrieval

## Citation Styles

Quarto supports CSL (Citation Style Language) files:

1. **Download APA 7th CSL**: https://github.com/citation-style-language/styles
2. Place `apa.csl` in project root
3. Reference in `_quarto.yml`:
   ```yaml
   csl: apa.csl
   ```

## Best Practices

### 1. Maintain Obsidian Links in Drafts

Keep using Obsidian syntax while writing:
- `[[Clippings/file|Author, Year]]` for readability
- Convert only when rendering

### 2. BibTeX Key Naming Convention

Use consistent keys: `authorlastnameYYYY`
- `vohland2021`
- `fricker2007`
- `delgado2023`

### 3. Version Control

- Commit `.md` files (source)
- Commit `.bib` files (bibliography)
- Ignore `output/` folder
- Ignore `.qmd` files (can be regenerated)

### 4. Metadata Synchronization

Keep Clippings YAML and BibTeX synchronized:
```bash
# Regenerate BibTeX when Clippings change
python3 clippings_to_bibtex.py
```

## Migration Strategy

### Step 1: Generate BibTeX
```bash
python3 clippings_to_bibtex.py
```

### Step 2: Test Conversion
```bash
python3 obsidian_to_quarto.py "Test Draft.md"
```

### Step 3: Render Sample
```bash
quarto render "Test Draft.qmd"
```

### Step 4: Compare Outputs
- Compare Quarto PDF with your current APA export
- Verify citation formatting
- Check bibliography completeness

### Step 5: Full Migration
- Convert all drafts gradually
- Keep Obsidian workflow for writing
- Use Quarto for final rendering

## Troubleshooting

### Citations Not Appearing

1. Check BibTeX keys match citation syntax
2. Verify `bibliography.bib` path in `_quarto.yml`
3. Ensure BibTeX entries are valid (use `pandoc-citeproc --check bibliography.bib`)

### Page Numbers Missing

Quarto handles page numbers differently:
- Use: `@citekey [p. 45]` (not in BibTeX)
- Or: `@citekey, p. 45`

### Obsidian Links Not Converting

- Check link format matches expected patterns
- Verify Clippings file exists
- Check BibTeX key generation logic

## Future Enhancements

1. **Live Preview**: Quarto preview while writing in Obsidian
2. **Auto-Conversion**: Watch mode for automatic `.md` → `.qmd` conversion
3. **MCP Integration**: Real-time metadata enrichment from academic databases
4. **Template Library**: Pre-configured templates for different journal formats
5. **Collaborative Editing**: Quarto + Git for version control

## Resources

- [Quarto Documentation](https://quarto.org/docs/guide/)
- [Quarto Citations](https://quarto.org/docs/authoring/footnotes-and-citations.html)
- [CSL Styles](https://github.com/citation-style-language/styles)
- [Pandoc Citation Processing](https://pandoc.org/MANUAL.html#citations)

## Example: Complete Workflow

```bash
# 1. Generate BibTeX from Clippings
cd Drafts/Scripts
python3 clippings_to_bibtex.py

# 2. Convert Obsidian draft to Quarto
python3 obsidian_to_quarto.py "../Digital libraries/Propuesta_Comunicacion_18JCID.md"

# 3. Render to PDF
cd ../..
quarto render "Drafts/Digital libraries/Propuesta_Comunicacion_18JCID.qmd"

# 4. Open output
open "output/Propuesta_Comunicacion_18JCID.pdf"
```

## Integration with Existing Scripts

Your existing `export_to_apa.py` can be enhanced to also generate Quarto format:

```python
# In export_to_apa.py, add:
def export_to_quarto(md_file, bib_file):
    """Export to Quarto .qmd format"""
    # Convert Obsidian links to @citekey format
    # Preserve structure
    # Generate .qmd file
```

This allows you to generate both APA export (for Word) and Quarto format (for PDF/HTML) from the same source.
