# ArXiv MCP Server Installation Guide

**Project:** ArXiv MCP Server Installation  
**Date:** January 2025  
**Guide Type:** Step-by-Step Installation Instructions

## 1. Prerequisites Check

Before installing the ArXiv MCP Server, let's verify your system has the necessary prerequisites:

### 1.1 System Requirements
- **Operating System**: macOS, Linux, or Windows
- **Python**: 3.8 or higher
- **Node.js**: 18 or higher (for some MCP clients)
- **Docker**: Optional, for containerized deployment

### 1.2 Check Your Current Setup

Let's first check what you have installed:

## 2. Installation Steps

### 2.1 Prerequisites Verification

✅ **Python 3.13.3** - Installed and working  
✅ **Node.js v24.2.0** - Installed and working  
✅ **uv 0.8.3** - Installed via Homebrew  

### 2.2 ArXiv MCP Server Installation

✅ **Installation Command:**
```bash
uv tool install arxiv-mcp-server
```

✅ **Path Configuration:**
```bash
export PATH="/Users/elenagomez/.local/bin:$PATH"
```

✅ **Storage Directory Created:**
```bash
mkdir -p ~/.arxiv-mcp-server/papers
```

### 2.3 Cursor Configuration

✅ **MCP Configuration Updated:**
```json
{
  "mcpServers": {
    "drawio": {
      "command": "/opt/homebrew/bin/npx",
      "args": ["-y", "drawio-mcp-server"]
    },
    "arxiv": {
      "command": "arxiv-mcp-server",
      "args": [],
      "env": {
        "ARXIV_STORAGE_PATH": "/Users/elenagomez/.arxiv-mcp-server/papers"
      }
    }
  }
}
```

## 3. Installation Verification

### 3.1 Server Status
✅ **ArXiv MCP Server** - Successfully installed and configured  
✅ **Cursor Integration** - Configuration updated and ready  
✅ **Storage Path** - Papers will be saved to `~/.arxiv-mcp-server/papers`

### 3.2 Available Tools
The ArXiv MCP Server provides the following tools in Cursor:

- **`search_papers`** - Search arXiv for papers with filters
- **`download_paper`** - Download specific papers by arXiv ID
- **`list_papers`** - View all locally stored papers
- **`read_paper`** - Access content of downloaded papers

## 4. Usage Examples

### 4.1 Basic Paper Search
```
"Search for papers about transformer architecture"
```

### 4.2 Download Specific Paper
```
"Download paper 2401.12345"
```

### 4.3 List Downloaded Papers
```
"Show me all the papers I've downloaded"
```

## 5. Next Steps

1. **Restart Cursor** - The ArXiv MCP Server is now ready to use
2. **Test Functionality** - Try searching for papers in Cursor chat
3. **Explore Features** - Use the deep analysis prompts for research

**Installation Complete!** 🎉