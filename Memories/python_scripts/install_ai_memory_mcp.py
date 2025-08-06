#!/usr/bin/env python3
"""
AI Memory MCP Server Installation Script
Date of Creation: January 15, 2025

This script installs and configures the AI Memory MCP server for use with Cursor.
It handles dependency installation, server setup, and MCP configuration.
"""

import os
import sys
import subprocess
import json
import shutil
from pathlib import Path

def print_step(message):
    """Print a formatted step message"""
    print(f"\n{'='*60}")
    print(f"STEP: {message}")
    print(f"{'='*60}")

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\nExecuting: {description}")
    print(f"Command: {' '.join(command)}")
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ Success: {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print_step("Checking Python version")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Error: Python 3.8+ required, found {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install required Python dependencies"""
    print_step("Installing Python dependencies")
    
    # Install MCP SDK
    if not run_command([sys.executable, "-m", "pip", "install", "mcp-server-sdk"], 
                      "Installing MCP Server SDK"):
        return False
    
    # Install additional dependencies for development
    if not run_command([sys.executable, "-m", "pip", "install", "pytest", "black", "flake8"], 
                      "Installing development dependencies"):
        return False
    
    return True

def create_mcp_config():
    """Create or update MCP configuration for Cursor"""
    print_step("Configuring MCP for Cursor")
    
    # Get the current script directory
    script_dir = Path(__file__).parent.absolute()
    server_path = script_dir / "ai_memory_mcp_server.py"
    
    # Ensure the server file exists
    if not server_path.exists():
        print(f"❌ Error: Server file not found at {server_path}")
        return False
    
    # Read existing MCP config
    mcp_config_path = Path.home() / ".cursor" / "mcp.json"
    
    if mcp_config_path.exists():
        with open(mcp_config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}
    
    # Add AI Memory MCP server configuration
    config["mcpServers"]["ai-memory"] = {
        "command": sys.executable,
        "args": [str(server_path)],
        "env": {
            "PYTHONPATH": str(script_dir),
            "AI_MEMORY_DB_PATH": str(script_dir / "ai_memory.db")
        }
    }
    
    # Ensure .cursor directory exists
    mcp_config_path.parent.mkdir(exist_ok=True)
    
    # Write updated configuration
    with open(mcp_config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ MCP configuration updated at {mcp_config_path}")
    return True

def test_server():
    """Test the MCP server"""
    print_step("Testing MCP server")
    
    script_dir = Path(__file__).parent.absolute()
    server_path = script_dir / "ai_memory_mcp_server.py"
    
    # Test if the server can be imported
    try:
        import sys
        sys.path.insert(0, str(script_dir))
        
        # Test basic import
        import ai_memory_mcp_server
        print("✅ Server imports successfully")
        
        # Test database initialization
        from ai_memory_mcp_server import MemoryDatabase
        db = MemoryDatabase("test_memory.db")
        print("✅ Database initialization successful")
        
        # Clean up test database
        if os.path.exists("test_memory.db"):
            os.remove("test_memory.db")
        
        return True
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

def create_example_usage():
    """Create example usage documentation"""
    print_step("Creating example usage documentation")
    
    example_content = """# AI Memory MCP Server - Example Usage

## Available Tools

### 1. Create Memory
Store a new memory entry:
```python
create_memory(
    content="User prefers step-by-step explanations",
    memory_type="user_preference",
    confidence=0.95,
    tags=["explanation_style", "user_behavior"]
)
```

### 2. Retrieve Memories
Search for memories:
```python
retrieve_memories(
    query="step-by-step",
    memory_type="user_preference",
    limit=5
)
```

### 3. Store Research Context
For academic research:
```python
store_research_context(
    context="Analyzing Spanish Civil War documents",
    research_topic="Spanish Civil War",
    session_id="research_session_123"
)
```

### 4. Get User Preferences
Retrieve stored preferences:
```python
get_user_preferences()
```

### 5. Memory Statistics
Get database statistics:
```python
get_memory_statistics()
```

## Memory Types

- `user_preference`: User preferences and behaviors
- `research_context`: Academic research context
- `conversation`: Chat history and interactions
- `general`: General information and facts

## Database Location

The memory database is stored at: `python_scripts/ai_memory.db`

## Restart Cursor

After installation, restart Cursor to load the new MCP server.
"""
    
    example_file = Path(__file__).parent / "example_usage.md"
    with open(example_file, 'w') as f:
        f.write(example_content)
    
    print(f"✅ Example usage created at {example_file}")
    return True

def main():
    """Main installation process"""
    print("AI Memory MCP Server Installation")
    print("Date: January 15, 2025")
    print("Academic Context: Digital Humanities, Knowledge Management")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Configure MCP
    if not create_mcp_config():
        print("❌ Failed to configure MCP")
        sys.exit(1)
    
    # Test server
    if not test_server():
        print("❌ Server test failed")
        sys.exit(1)
    
    # Create examples
    create_example_usage()
    
    print("\n" + "="*60)
    print("🎉 AI Memory MCP Server Installation Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Restart Cursor to load the new MCP server")
    print("2. The server will be available as 'ai-memory' in your MCP tools")
    print("3. Check example_usage.md for usage examples")
    print("4. Database will be created automatically at: python_scripts/ai_memory.db")
    print("\nAcademic applications:")
    print("- Store research context across sessions")
    print("- Remember user preferences for personalized assistance")
    print("- Maintain conversation history for continuity")
    print("- Track research findings and insights")

if __name__ == "__main__":
    main() 