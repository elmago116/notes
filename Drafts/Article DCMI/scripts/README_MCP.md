# Citation MCP Server

**Date Created**: 2025-08-12

A Model Context Protocol (MCP) server that provides tools to search Crossref and OpenAlex APIs for academic citation metadata, specifically designed for DCMI citation processing and Obsidian integration.

## Features

### 🔍 **API Integration**
- **Crossref API**: Search for academic papers by title, author, or DOI
- **OpenAlex API**: Comprehensive scholarly metadata from the open academic index
- **Dual Search**: Get results from both APIs for comprehensive coverage

### 📚 **Citation Tools**
- `search_crossref`: Search Crossref API for academic papers
- `search_openalex`: Search OpenAlex API for academic papers  
- `get_citation_metadata`: Comprehensive search across both APIs
- `format_dcmi_citation`: Format metadata into DCMI-compliant citations

### 🔗 **Obsidian Integration**
- Automatically extract titles from Obsidian links
- Search for missing metadata when citations are incomplete
- Generate proper academic citations from file names

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements_mcp.txt
   ```

2. **Verify Installation**:
   ```bash
   python test_citation_mcp.py
   ```

## Usage

### Running the MCP Server

```bash
python citation_mcp_server.py
```

### Available Tools

#### 1. Search Crossref
```json
{
  "name": "search_crossref",
  "arguments": {
    "query": "Epistemic Injustice Power and the Ethics of Knowing",
    "max_results": 5
  }
}
```

#### 2. Search OpenAlex
```json
{
  "name": "search_openalex", 
  "arguments": {
    "query": "Human-Centered AI research landscape",
    "max_results": 5
  }
}
```

#### 3. Comprehensive Metadata Search
```json
{
  "name": "get_citation_metadata",
  "arguments": {
    "title": "What is Human-Centered about Human-Centered AI",
    "author": "Capel Brereton",
    "doi": "10.1145/3544548.3580818"
  }
}
```

#### 4. Format DCMI Citation
```json
{
  "name": "format_dcmi_citation",
  "arguments": {
    "metadata": {
      "authors": ["Fricker, Miranda"],
      "title": "Epistemic Injustice: Power and the Ethics of Knowing",
      "journal": "Oxford University Press",
      "year": 2011,
      "doi": "10.1093/acprof:oso/9780198237907.001.0001"
    },
    "citation_number": 1
  }
}
```

## Integration with Obsidian Citation Processing

### Problem Solved
When processing Obsidian citations like:
```
[[Some_Unknown_Paper.pdf|Unknown Paper Title]]
```

The MCP server can:
1. Extract the title from the display text
2. Search both Crossref and OpenAlex APIs
3. Return proper academic metadata
4. Format into DCMI-compliant citations

### Example Workflow
1. **Extract Title**: "Unknown Paper Title" from Obsidian link
2. **Search APIs**: Query both Crossref and OpenAlex
3. **Get Metadata**: Authors, journal, year, DOI, etc.
4. **Format Citation**: Generate proper DCMI citation
5. **Update Bibliography**: Add to academic bibliography

## API Response Format

### Crossref Response
```json
{
  "doi": "10.1093/acprof:oso/9780198237907.001.0001",
  "title": "Epistemic Injustice: Power and the Ethics of Knowing",
  "authors": ["Fricker, Miranda"],
  "journal": "Oxford University Press",
  "year": 2011,
  "volume": "",
  "issue": "",
  "pages": "",
  "source": "crossref"
}
```

### OpenAlex Response
```json
{
  "doi": "10.1093/acprof:oso/9780198237907.001.0001",
  "title": "Epistemic Injustice: Power and the Ethics of Knowing",
  "authors": ["Miranda Fricker"],
  "journal": "Oxford University Press",
  "year": 2011,
  "source": "openalex"
}
```

## DCMI Citation Format

The server generates citations in DCMI-compliant format:

```
[1] Fricker, Miranda, Epistemic Injustice: Power and the Ethics of Knowing, Oxford University Press 2011. DOI: 10.1093/acprof:oso/9780198237907.001.0001.
```

## Configuration

### Rate Limiting
- Crossref: No rate limits for basic usage
- OpenAlex: 100,000 requests per day for free tier

### Error Handling
- Network timeouts: 30 seconds
- Retry logic: 3 attempts for failed requests
- Graceful degradation: Returns partial results if one API fails

## Testing

Run the test suite:
```bash
python test_citation_mcp.py
```

This will test:
- Crossref API search
- OpenAlex API search
- Comprehensive metadata retrieval
- DCMI citation formatting
- Obsidian integration workflow

## Future Enhancements

- [ ] Add Semantic Scholar API integration
- [ ] Support for conference proceedings
- [ ] Automatic DOI resolution
- [ ] Citation style customization (APA, MLA, etc.)
- [ ] Batch processing for multiple citations
- [ ] Caching for improved performance

## Academic Context

This MCP server is designed specifically for:
- **DCMI Standards**: Dublin Core Metadata Initiative compliance
- **GLAM Research**: Galleries, Libraries, Archives, and Museums
- **Semantic Web**: Linked data and metadata interoperability
- **NeSy AI**: Neuro-Symbolic Artificial Intelligence research
- **Participatory Design**: User-centered design methodologies

## License

This project is part of the HerStory&NeSyAI research project (PID2023-147673OB-I00) and follows academic research standards.
