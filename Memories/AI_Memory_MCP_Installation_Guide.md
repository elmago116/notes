# AI Memory MCP Server Installation Guide

**Date of Creation:** January 15, 2025  
**Academic Context:** Digital Humanities, Knowledge Management, AI Systems  
**Target Audience:** Researchers and students learning about AI memory systems

---

## Overview

This guide will help you install the AI Memory MCP (Model Context Protocol) server, which enables AI systems to have persistent memory capabilities. This is particularly useful for academic research where you need AI assistants to remember context across multiple sessions.

### What You'll Learn

1. **Understanding AI Memory**: How AI systems can maintain persistent memory
2. **Installation Process**: Step-by-step setup instructions
3. **Configuration**: How to integrate with Cursor IDE
4. **Testing**: Verifying the installation works correctly
5. **Usage**: How to use the memory system for research

---

## Prerequisites

### System Requirements

- **Operating System**: macOS, Windows, or Linux
- **Python**: Version 3.8 or higher
- **Cursor IDE**: Latest version installed
- **Internet Connection**: For downloading dependencies

### What the AI Memory MCP Does

The AI Memory MCP server provides these capabilities:

- **Persistent Memory**: AI can remember information across sessions
- **User Preferences**: Store and recall user behavior patterns
- **Research Context**: Maintain context for academic research
- **Conversation History**: Remember previous interactions
- **Structured Storage**: Organize memories with metadata and relationships

---

## Step-by-Step Installation

### Step 1: Verify Python Installation

First, let's check if Python is installed on your system:

**On macOS/Linux:**
```bash
python3 --version
```

**On Windows:**
```bash
python --version
```

**Expected Output:**
```
Python 3.8.10 (or higher)
```

If Python is not installed, download it from [python.org](https://python.org).

### Step 2: Navigate to the Installation Directory

Open your terminal/command prompt and navigate to the directory containing the installation files:

```bash
cd /path/to/your/workspace/python_scripts
```

### Step 3: Run the Installation Script

Execute the installation script:

```bash
python3 install_ai_memory_mcp.py
```

**What the script does:**
1. Checks Python version compatibility
2. Installs required dependencies
3. Configures MCP for Cursor
4. Tests the server functionality
5. Creates example usage documentation

### Step 4: Verify Installation

The installation script will show progress and results. You should see:

```
✅ Python 3.8.10 is compatible
✅ Installing MCP Server SDK
✅ Installing development dependencies
✅ MCP configuration updated at ~/.cursor/mcp.json
✅ Server imports successfully
✅ Database initialization successful
🎉 AI Memory MCP Server Installation Complete!
```

### Step 5: Restart Cursor

After successful installation, restart Cursor to load the new MCP server:

1. Close Cursor completely
2. Reopen Cursor
3. The AI Memory MCP server will be available as `ai-memory`

---

## Understanding the Installation

### What Was Installed

1. **MCP Server SDK**: The framework for creating MCP servers
2. **AI Memory Server**: The actual memory management server
3. **SQLite Database**: For storing memories locally
4. **MCP Configuration**: Integration with Cursor

### File Structure Created

```
python_scripts/
├── ai_memory_mcp_server.py    # Main server file
├── install_ai_memory_mcp.py   # Installation script
├── requirements.txt           # Dependencies list
├── example_usage.md          # Usage examples
└── ai_memory.db             # Memory database (created automatically)
```

### MCP Configuration

The installation updates your `~/.cursor/mcp.json` file to include:

```json
{
  "mcpServers": {
    "ai-memory": {
      "command": "python3",
      "args": ["/path/to/ai_memory_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/python_scripts",
        "AI_MEMORY_DB_PATH": "/path/to/ai_memory.db"
      }
    }
  }
}
```

---

## Testing the Installation

### Test 1: Check MCP Server Availability

After restarting Cursor, you should be able to use the AI Memory MCP tools:

1. Open Cursor
2. Start a new conversation
3. The AI should have access to memory tools like:
   - `create_memory`
   - `retrieve_memories`
   - `get_user_preferences`
   - `store_research_context`

### Test 2: Create Your First Memory

Try creating a test memory:

```
Please create a memory that I prefer step-by-step explanations in academic contexts.
```

The AI should respond with something like:
```
I'll store that preference in your memory. This will help me provide more structured explanations in future academic discussions.
```

### Test 3: Retrieve Memories

Ask the AI to retrieve your preferences:

```
What are my preferences for explanations?
```

The AI should recall the previously stored preference.

---

## Understanding AI Memory Concepts

### Memory Hierarchy

The AI Memory MCP implements a three-tier memory system:

```
┌─────────────────────────────────────┐
│           Working Memory            │ ← Current session
│     (Immediate context)             │
├─────────────────────────────────────┤
│         Short-term Memory           │ ← Recent interactions
│      (Last few conversations)       │
├─────────────────────────────────────┤
│         Long-term Memory            │ ← Persistent storage
│    (User preferences, research)     │
└─────────────────────────────────────┘
```

### Memory Types

1. **User Preferences**: How you like information presented
2. **Research Context**: Academic research findings and context
3. **Conversation History**: Previous interactions and insights
4. **General Information**: Facts and knowledge you've shared

### Memory Operations

The system supports four basic operations:

- **CREATE**: Store new memories
- **RETRIEVE**: Find relevant memories
- **UPDATE**: Modify existing memories
- **DELETE**: Remove outdated memories

---

## Academic Applications

### Digital Humanities Research

**Use Case**: Studying historical documents across multiple sessions

**Memory Capabilities**:
- Remember previous document analysis
- Maintain context about research questions
- Store insights about historical figures
- Track relationships between different sources

**Example**:
```
Store research context: "Analyzing Spanish Civil War brigadistas documents. 
Key finding: Many international volunteers came from specific regions."
```

### Knowledge Management

**Use Case**: Building and maintaining knowledge graphs

**Memory Capabilities**:
- Remember entity relationships discovered
- Store graph construction patterns
- Maintain consistency across sessions
- Track data quality issues

### User Experience Research

**Use Case**: Studying how users interact with AI systems

**Memory Capabilities**:
- Remember user preferences and behaviors
- Adapt responses based on interaction history
- Track learning patterns
- Maintain personalized assistance

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Python Not Found
**Error**: `python3: command not found`

**Solution**:
- Install Python from [python.org](https://python.org)
- On macOS, you can also use Homebrew: `brew install python`

#### Issue 2: Permission Denied
**Error**: `Permission denied` when running installation script

**Solution**:
```bash
chmod +x install_ai_memory_mcp.py
python3 install_ai_memory_mcp.py
```

#### Issue 3: MCP SDK Installation Failed
**Error**: `Failed to install MCP Server SDK`

**Solution**:
```bash
pip3 install --upgrade pip
pip3 install mcp-server-sdk
```

#### Issue 4: Cursor Not Recognizing MCP Server
**Error**: AI Memory tools not available in Cursor

**Solution**:
1. Check that Cursor was restarted completely
2. Verify the MCP configuration file exists: `~/.cursor/mcp.json`
3. Check Cursor's developer console for error messages

#### Issue 5: Database Creation Failed
**Error**: `Error creating database`

**Solution**:
1. Ensure you have write permissions in the python_scripts directory
2. Check available disk space
3. Try running the installation script again

### Getting Help

If you encounter issues:

1. **Check the logs**: Look for error messages in the installation output
2. **Verify prerequisites**: Ensure Python 3.8+ is installed
3. **Check permissions**: Ensure you can write to the installation directory
4. **Restart Cursor**: Sometimes a fresh restart resolves issues

---

## Advanced Configuration

### Customizing Memory Storage

You can modify the database location by editing the MCP configuration:

```json
{
  "mcpServers": {
    "ai-memory": {
      "env": {
        "AI_MEMORY_DB_PATH": "/custom/path/to/memory.db"
      }
    }
  }
}
```

### Adding Vector Search (Advanced)

For semantic search capabilities, you can install additional dependencies:

```bash
pip3 install sentence-transformers chromadb
```

This enables more sophisticated memory retrieval based on meaning rather than just keywords.

---

## Academic Research Implications

### Research Questions

The AI Memory MCP enables research on:

1. **Memory Persistence**: How long should different types of memories be retained?
2. **Memory Accuracy**: How to handle conflicting or outdated memories?
3. **Privacy Concerns**: How to balance memory utility with user privacy?
4. **Scalability**: How to manage memory growth over time?

### Future Research Directions

1. **Adaptive Memory Management**: Automatically adjust memory retention based on usage patterns
2. **Cross-Session Learning**: Transfer learning between different research sessions
3. **Collaborative Memory**: Shared memories between multiple users or AI systems
4. **Memory Compression**: Efficient storage and retrieval of large memory sets

---

## Conclusion

You have successfully installed the AI Memory MCP server! This system provides:

- **Persistent Memory**: AI can remember information across sessions
- **Academic Applications**: Particularly useful for research and knowledge work
- **User Personalization**: Adapts to your preferences and behavior
- **Research Continuity**: Maintains context across multiple research sessions

### Next Steps

1. **Experiment**: Try storing different types of memories
2. **Research**: Use it for your academic research projects
3. **Evaluate**: Assess how well it meets your research needs
4. **Contribute**: Share feedback and suggestions for improvement

### Academic Significance

This technology represents a significant advancement in:
- **Digital Humanities**: Enabling AI assistants that remember research context
- **Knowledge Management**: Structured storage and retrieval of information
- **Human-Computer Interaction**: More natural and persistent AI interactions
- **Artificial Intelligence**: Moving toward more human-like memory capabilities

---

## References

1. Packer, C., et al. (2023). MemGPT: Towards LLMs as Operating Systems. arXiv preprint arXiv:2310.08560.

2. Guo, J., et al. (2023). Empowering Working Memory for Large Language Model Agents. arXiv preprint arXiv:2312.17259.

3. Model Context Protocol Specification. https://modelcontextprotocol.io

---

**Document Version**: 1.0  
**Last Updated**: January 15, 2025  
**Academic Framework**: Digital Humanities, AI Systems, Knowledge Management  
**Research Interest**: Memory Management in AI, Human-Computer Interaction, Digital Humanities 