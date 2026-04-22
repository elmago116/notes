# Quarto + Obsidian Quick Start Guide

## Why Quarto?

Your current workflow uses Python scripts to convert Obsidian links to APA citations. Quarto adds:

✅ **Native citation management** (BibTeX/CSL)  
✅ **Automatic cross-references** (figures, tables, sections)  
✅ **Multiple output formats** (PDF, HTML, Word) from one source  
✅ **Better academic database integration** via MCP  
✅ **Professional typography** and layout control  
✅ **Code execution** for reproducible research  

## Quick Start (3 Steps)

### Step 1: Generate BibTeX from Clippings

```bash
cd Drafts/Scripts
python3 clippings_to_bibtex.py
```

This creates `bibliography.bib` in your project root with all your Clippings metadata.

### Step 2: Convert Obsidian Draft to Quarto

```bash
python3 obsidian_to_quarto.py "../Digital libraries/Propuesta_Comunicacion_18JCID.md"
```

This creates a `.qmd` file with Quarto citation syntax.

### Step 3: Render to PDF/HTML/Word

```bash
cd ../..
quarto render "Drafts/Digital libraries/Propuesta_Comunicacion_18JCID.qmd"
```

Output files appear in `output/` folder.

## Conversion Examples

| Your Obsidian Format | Quarto Format |
|---------------------|---------------|
| `[[Clippings/file\|Vohland et al., 2021]]` | `@vohland2021` |
| `[[file.pdf#page=45\|Vohland et al., 2021]]` | `@vohland2021 [p. 45]` |
| `[[Clippings/file\|X]]` | `@citekey` (auto-resolved) |

## Workflow Comparison

### Current Workflow
```
Obsidian Draft (.md) 
  → Python Script 
    → APA Export (.md)
      → Manual formatting
```

### Quarto Workflow
```
Obsidian Draft (.md)
  → Python Script
    → Quarto (.qmd)
      → quarto render
        → PDF/HTML/Word (automatic)
```

## Key Benefits

1. **Keep Writing in Obsidian**: No need to change your writing process
2. **Better Citations**: Native BibTeX support with automatic formatting
3. **Cross-References**: Automatic figure/table numbering and linking
4. **Multiple Formats**: One source, multiple outputs
5. **Academic Integration**: Better MCP support for metadata enrichment

## Next Steps

1. **Test with one draft**: Convert a small draft first
2. **Compare outputs**: Check Quarto PDF vs your current APA export
3. **Customize format**: Edit `_quarto.yml` for your journal requirements
4. **Enrich bibliography**: Use MCP scripts to add missing metadata

## Files Created

- `clippings_to_bibtex.py` - Converts Clippings to BibTeX
- `obsidian_to_quarto.py` - Converts Obsidian links to Quarto citations
- `_quarto.yml` - Quarto project configuration
- `quarto_template.qmd` - Template for new documents
- `QUARTO_OBSIDIAN_INTEGRATION.md` - Full documentation

## Troubleshooting

**Citations not appearing?**
- Run `clippings_to_bibtex.py` first to generate bibliography.bib
- Check BibTeX keys match citation syntax

**Page numbers missing?**
- Use format: `@citekey [p. 45]` in Quarto

**Need APA 7th style?**
- Download `apa.csl` from https://github.com/citation-style-language/styles
- Add `csl: apa.csl` to `_quarto.yml`

## Resources

- [Quarto Guide](https://quarto.org/docs/guide/)
- [Quarto Citations](https://quarto.org/docs/authoring/footnotes-and-citations.html)
- Full integration guide: `QUARTO_OBSIDIAN_INTEGRATION.md`
