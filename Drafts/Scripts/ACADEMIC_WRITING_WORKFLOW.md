# Academic Writing Workflow

## Overview

This workflow supports academic writing from PDF acquisition to final APA-formatted export. It transforms Obsidian links into proper APA 7th edition citations with a complete references section.

## Workflow Phases

### Phase 1: PDF Acquisition & Note Creation

1. **Download PDFs** to the `PDF/` folder
2. **Auto-create corresponding `.md` files** in `Clippings/` folder with:
   - YAML frontmatter containing:
     - `title`: Document title
     - `apa_citation`: Canonical APA in-text citation (e.g., `Vohland et al., 2021`)
     - `authors`: List of authors
     - `year`: Publication year
     - `type`: Document type (article, book, conference, etc.)
     - `journal`: Journal name (if applicable)
     - `publisher`: Publisher name (if applicable)
     - `doi`: DOI identifier (if available)
     - `url`: Source URL (if available)
     - Other relevant metadata
   - Link to PDF file(s) using Obsidian wikilink syntax
   - Tags and metadata for organization

**Example Clippings file structure:**
```yaml
---
title: The Science of Citizen Science
apa_citation: Vohland et al., 2021
authors:
  - Vohland, Katrin
  - Land-Zandstra, Anne
year: 2021
type: book
publisher: Springer
doi: 10.1007/978-3-030-58278-4
tags:
  - themes/citizenScience
---

[[The Science of Citizen Science.pdf]]
```

### Phase 2: Draft Writing

Work in the `Drafts/` folder using Obsidian-style links to reference your sources:

- **Basic link**: `[[filename|X]]` - Links with placeholder markers
- **PDF link**: `[[PDF/filename.pdf]]` - Direct PDF links
- **Clippings link**: `[[Clippings/filename]]` - Link to Clippings file
- **PDF with page**: `[[filename.pdf#page=45|display text]]` - PDF links with page numbers
- **Clippings with display**: `[[Clippings/filename|Display Text]]` - Links with custom display text
- **Using the APA citation label**: If the Clippings note has `apa_citation`, replace `|X` with that label: `[[Clippings/filename|Vohland et al., 2021]]` (page numbers still go in the link fragment or display text).

**Example usage in drafts:**
```markdown
This study presents a methodological analysis [[Participatory_design_A_systematic_review|X]] 
integrated by qualitative methods [[Literature ReviewsModern Methods for Investigating Scientific and Technological Knowledge.pdf|X]].
```

Links preserve connection to source material and can be navigated directly in Obsidian.

### Phase 3: Citation Export

Convert all Obsidian links to APA 7th edition citations and generate a complete references section.

**Usage:**
```bash
cd Drafts/Scripts
python3 export_to_apa.py "General Methodological context and theoretic framework.md"
```

**Output:**
- Creates new file: `[original-filename] - APA Export.md`
- Original file remains unchanged
- All resolvable links converted to APA citations
- Complete `## References` section appended

## File Structure

```
Documents/
├── PDF/                          # PDF files stored here
├── Clippings/                    # Markdown notes with metadata
│   └── [document-name].md
└── Drafts/                       # Working drafts
    ├── [your-draft].md          # Original draft with links
    ├── [your-draft] - APA Export.md  # Exported version
    └── Scripts/
        ├── export_to_apa.py     # Export script
        └── ACADEMIC_WRITING_WORKFLOW.md  # This file
```

## Link Resolution Strategy

The export script resolves links using a multi-stage matching approach:

1. **Exact filename match** - Match by exact stem of Clippings file
2. **PDF basename matching** - Match PDF filename to Clippings file
3. **Title matching** - Match link text to YAML `title` field
4. **Word overlap fallback** - Fuzzy matching based on word similarity (60% threshold)

Links that cannot be resolved are preserved as-is with a warning in the output.

## APA Citation Format

### In-Text Citations

- **Single author**: `(Smith, 2023)`
- **Two authors**: `(Smith & Jones, 2023)` - **Both authors must appear** (APA 7th edition requirement)
- **Three+ authors**: `(Smith et al., 2023)`
- **With page number**: `(Smith, 2023, p. 45)`
- **Multiple citations**: `(Smith, 2023; Jones, 2022)`

**Important**: For works with exactly two authors, APA 7th edition requires both authors to be listed in every citation. The format is `(Author1 & Author2, Year)` with an ampersand (`&`) and no comma before it.

### References Section Format

**Journal Article:**
```
Author, A. A. (Year). Title of article. *Journal Name*, Volume(Issue), Pages. https://doi.org/XX
```

**Book:**
```
Author, A. A. (Year). *Title of book*. Publisher Name.
```

**Conference Paper:**
```
Author, A. A. (Year). Title of paper. In *Conference Proceedings* (pp. XX-XX). Publisher.
```

**Book Chapter:**
```
Author, A. A. (Year). Title of chapter. In E. Editor (Ed.), *Title of book* (pp. XX-XX). Publisher.
```

## Usage Instructions

### Basic Export

1. Ensure your draft file is in the `Drafts/` folder
2. All referenced sources have corresponding files in `Clippings/` with proper YAML metadata
3. Run the export script:
   ```bash
   cd Drafts/Scripts
   python3 export_to_apa.py "Your Draft File.md"
   ```
4. Find the exported file: `Your Draft File - APA Export.md` in the `Drafts/` folder

### Handling Placeholder Markers

Prefer replacing `|X` with the `apa_citation` label from the Clippings YAML to improve readability in Drafts:
- `[[Clippings/filename|Vohland et al., 2021]]` → already human-readable; export still converts to `(Vohland et al., 2021)`
- If no label is present, `|X` is still supported and will convert as before.
Page numbers remain per-link (e.g., `[[file.pdf#page=45|Vohland et al., 2021]]` will render `(Vohland et al., 2021, p. 45)`).

### Custom Display Text

Links with custom display text are resolved using the display text:
- `[[Clippings/filename|Custom Display Text]]` - Uses "Custom Display Text" for matching
- Recommended: use the `apa_citation` label (e.g., `Author, Year`) as the display text for clarity in Drafts.

## Troubleshooting

### Unresolved Links

If links cannot be resolved, they are preserved as-is in the export. Common reasons:
- **Missing Clippings file**: Create a corresponding `.md` file in `Clippings/` folder
- **Filename mismatch**: Check exact filename (case-sensitive on some systems)
- **Missing metadata**: Ensure YAML frontmatter has `title`, `authors`, and `year` fields
- **Missing `apa_citation`**: Export still works via metadata; add it later for readability.

### Missing Author Information

Citations require at least one author in the YAML metadata. If missing:
- Check the `authors` field in Clippings file
- Ensure it's formatted as a list: `authors: - Author Name`
- If `apa_citation` is present but authors are missing, update authors to keep `apa_citation` consistent.

### Page Numbers Not Appearing

Page numbers are extracted from:
- PDF link fragments: `[[file.pdf#page=45]]`
- Display text: `[[file.pdf|p. 45]]`

Ensure page information is present in one of these formats.

### References Not Appearing

References section requires:
- At least one resolvable link
- Complete metadata (authors, year, title)
- Valid YAML frontmatter in Clippings files
- `apa_citation` is optional for export, but recommended for Draft readability.

## Best Practices

1. **Consistent Naming**: Use consistent naming between PDF files and Clippings files
2. **Complete Metadata**: Fill in all relevant YAML fields in Clippings files
3. **Add `apa_citation`**: Store the canonical in-text citation (Author, Year) in YAML and reuse it as the link display text in Drafts.
4. **Two-Author Format**: Ensure works with exactly two authors list both in `apa_citation` (e.g., `Smith & Jones, 2023`), not `Smith et al.`
5. **Regular Backups**: Original files are preserved, but consider backing up before large exports
6. **Validate Citations**: Always review the exported file for accuracy
7. **Test Links**: Verify links resolve correctly before final export

## Data Integrity Notes for `apa_citation`
- Treat `apa_citation` in Clippings YAML as the single source of the in-text label.
- Keep `apa_citation` synchronized with `authors` and `year`; update it when metadata changes.
- **Two-author requirement**: For works with exactly two authors, `apa_citation` must list both authors (e.g., `Smith & Jones, 2023`), not `Smith et al., 2023`. The replacement script automatically ensures this format.
- Page numbers remain per-link in Drafts (via fragment `#page=` or display text); do not store page numbers in `apa_citation`.
- If `apa_citation` is absent, the export still resolves citations from metadata—no data loss.

## Future Enhancements

- Batch processing for multiple draft files
- Export to Word (.docx) format
- Citation style options (beyond APA 7th)
- Link validation before export
- Metadata enrichment for missing fields
- Integration with reference management software
- Integration with academic MCPS such as Open Alex, ArXib

## Examples

### Before Export

```markdown
This study uses participatory design methods [[Participatory_design_A_systematic_review|X]] 
and citizen science approaches [[The Science of Citizen Science|X]] to explore 
user engagement [[Embedding Citizen Science in GLAMs|X]].
```

### After Export

```markdown
This study uses participatory design methods (Author1 & Author2, 2023) 
and citizen science approaches (Vohland et al., 2021) to explore 
user engagement (Smith, 2022, p. 15).

## References

Author1, A. & Author2, B. (2023). Participatory design: A systematic review. *Journal Name*, 10(2), 123-145.

Smith, J. (2022). Embedding Citizen Science in GLAMs. *Library Quarterly*, 92(1), 15-30.

Vohland, K., Land-Zandstra, A., & Ceccaroni, L. (2021). *The Science of Citizen Science*. Springer.
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your file structure matches the expected format
3. Review the Clippings files for complete metadata
4. Check script output for warning messages

