#!/usr/bin/env python3
"""
AI Memory MCP Server
A Model Context Protocol server for persistent AI memory management

Date of Creation: January 15, 2025
Academic Context: Digital Humanities, Knowledge Management, AI Systems
Research Interest: Memory Management in Large Language Models

This server provides persistent memory capabilities for AI systems,
enabling them to remember user preferences, research context, and
interaction history across sessions.
"""

import json
import uuid
import time
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import sqlite3
import os
from pathlib import Path

try:
    from mcp.server.fastmcp import FastMCP
    from mcp.server.models import InitializationOptions
except ImportError:
    print("MCP SDK not found. Installing required dependencies...")
    import subprocess
    subprocess.check_call(["pip", "install", "mcp-server-sdk"])
    from mcp.server.fastmcp import FastMCP
    from mcp.server.models import InitializationOptions

# Initialize MCP server
mcp = FastMCP("AI-Memory-Server")

@dataclass
class Memory:
    """Memory data structure with metadata"""
    id: str
    content: str
    memory_type: str
    timestamp: str
    session_id: Optional[str] = None
    confidence: float = 1.0
    tags: List[str] = None
    relationships: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.relationships is None:
            self.relationships = {}

class MemoryDatabase:
    """SQLite-based memory storage with vector search capabilities"""
    
    def __init__(self, db_path: str = "ai_memory.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the memory database with proper schema"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    session_id TEXT,
                    confidence REAL DEFAULT 1.0,
                    tags TEXT,
                    relationships TEXT,
                    embeddings TEXT
                )
            """)
            
            # Create indexes for efficient querying
            conn.execute("CREATE INDEX IF NOT EXISTS idx_memory_type ON memories(memory_type)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_session_id ON memories(session_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_timestamp ON memories(timestamp)")
            conn.commit()
    
    def store_memory(self, memory: Memory) -> bool:
        """Store a new memory in the database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT INTO memories 
                    (id, content, memory_type, timestamp, session_id, confidence, tags, relationships)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    memory.id,
                    memory.content,
                    memory.memory_type,
                    memory.timestamp,
                    memory.session_id,
                    memory.confidence,
                    json.dumps(memory.tags),
                    json.dumps(memory.relationships)
                ))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error storing memory: {e}")
            return False
    
    def retrieve_memories(self, query: str = None, memory_type: str = None, 
                         session_id: str = None, limit: int = 10) -> List[Memory]:
        """Retrieve memories based on various criteria"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Build query based on provided filters
                sql = "SELECT * FROM memories WHERE 1=1"
                params = []
                
                if query:
                    sql += " AND content LIKE ?"
                    params.append(f"%{query}%")
                
                if memory_type:
                    sql += " AND memory_type = ?"
                    params.append(memory_type)
                
                if session_id:
                    sql += " AND session_id = ?"
                    params.append(session_id)
                
                sql += " ORDER BY timestamp DESC LIMIT ?"
                params.append(limit)
                
                cursor = conn.execute(sql, params)
                rows = cursor.fetchall()
                
                memories = []
                for row in rows:
                    memory = Memory(
                        id=row[0],
                        content=row[1],
                        memory_type=row[2],
                        timestamp=row[3],
                        session_id=row[4],
                        confidence=row[5],
                        tags=json.loads(row[6]) if row[6] else [],
                        relationships=json.loads(row[7]) if row[7] else {}
                    )
                    memories.append(memory)
                
                return memories
        except Exception as e:
            print(f"Error retrieving memories: {e}")
            return []
    
    def update_memory(self, memory_id: str, new_content: str, 
                     new_confidence: float = None) -> bool:
        """Update an existing memory"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                sql = "UPDATE memories SET content = ?"
                params = [new_content]
                
                if new_confidence is not None:
                    sql += ", confidence = ?"
                    params.append(new_confidence)
                
                sql += ", timestamp = ? WHERE id = ?"
                params.extend([datetime.now().isoformat(), memory_id])
                
                conn.execute(sql, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating memory: {e}")
            return False
    
    def delete_memory(self, memory_id: str) -> bool:
        """Delete a memory from the database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Error deleting memory: {e}")
            return False
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get statistics about stored memories"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                total = conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]
                types = conn.execute("""
                    SELECT memory_type, COUNT(*) 
                    FROM memories 
                    GROUP BY memory_type
                """).fetchall()
                
                return {
                    "total_memories": total,
                    "memory_types": dict(types),
                    "database_path": self.db_path
                }
        except Exception as e:
            print(f"Error getting memory stats: {e}")
            return {}

# Initialize memory database
memory_db = MemoryDatabase()

def generate_id() -> str:
    """Generate a unique memory ID"""
    return str(uuid.uuid4())

def get_current_time() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()

@mcp.tool()
def create_memory(content: str, memory_type: str = "general", 
                  session_id: str = None, confidence: float = 1.0,
                  tags: List[str] = None, relationships: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Create a new memory entry
    
    Args:
        content: The memory content to store
        memory_type: Type of memory (e.g., "user_preference", "research_context", "conversation")
        session_id: Optional session identifier
        confidence: Confidence level in the memory (0.0 to 1.0)
        tags: Optional tags for categorization
        relationships: Optional relationships to other memories
    
    Returns:
        Dictionary with status and memory ID
    """
    try:
        memory = Memory(
            id=generate_id(),
            content=content,
            memory_type=memory_type,
            timestamp=get_current_time(),
            session_id=session_id,
            confidence=confidence,
            tags=tags or [],
            relationships=relationships or {}
        )
        
        success = memory_db.store_memory(memory)
        
        if success:
            return {
                "status": "success",
                "memory_id": memory.id,
                "message": "Memory stored successfully",
                "memory": asdict(memory)
            }
        else:
            return {
                "status": "error",
                "message": "Failed to store memory"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error creating memory: {str(e)}"
        }

@mcp.tool()
def retrieve_memories(query: str = None, memory_type: str = None,
                     session_id: str = None, limit: int = 10) -> Dict[str, Any]:
    """
    Retrieve memories based on various criteria
    
    Args:
        query: Text to search for in memory content
        memory_type: Filter by memory type
        session_id: Filter by session ID
        limit: Maximum number of memories to return
    
    Returns:
        Dictionary with retrieved memories
    """
    try:
        memories = memory_db.retrieve_memories(
            query=query,
            memory_type=memory_type,
            session_id=session_id,
            limit=limit
        )
        
        return {
            "status": "success",
            "memories": [asdict(memory) for memory in memories],
            "count": len(memories)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error retrieving memories: {str(e)}"
        }

@mcp.tool()
def update_memory(memory_id: str, new_content: str, 
                 new_confidence: float = None) -> Dict[str, Any]:
    """
    Update an existing memory
    
    Args:
        memory_id: ID of the memory to update
        new_content: New content for the memory
        new_confidence: Optional new confidence level
    
    Returns:
        Dictionary with update status
    """
    try:
        success = memory_db.update_memory(memory_id, new_content, new_confidence)
        
        if success:
            return {
                "status": "success",
                "message": "Memory updated successfully",
                "memory_id": memory_id
            }
        else:
            return {
                "status": "error",
                "message": "Failed to update memory"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error updating memory: {str(e)}"
        }

@mcp.tool()
def delete_memory(memory_id: str) -> Dict[str, Any]:
    """
    Delete a memory entry
    
    Args:
        memory_id: ID of the memory to delete
    
    Returns:
        Dictionary with deletion status
    """
    try:
        success = memory_db.delete_memory(memory_id)
        
        if success:
            return {
                "status": "success",
                "message": "Memory deleted successfully",
                "memory_id": memory_id
            }
        else:
            return {
                "status": "error",
                "message": "Failed to delete memory"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error deleting memory: {str(e)}"
        }

@mcp.tool()
def get_memory_statistics() -> Dict[str, Any]:
    """
    Get statistics about stored memories
    
    Returns:
        Dictionary with memory statistics
    """
    try:
        stats = memory_db.get_memory_stats()
        return {
            "status": "success",
            "statistics": stats
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error getting statistics: {str(e)}"
        }

@mcp.tool()
def search_memories_by_semantic_similarity(query: str, limit: int = 5) -> Dict[str, Any]:
    """
    Search memories using semantic similarity (basic implementation)
    
    Args:
        query: Search query
        limit: Maximum number of results
    
    Returns:
        Dictionary with semantically similar memories
    """
    try:
        # For now, use simple text matching
        # In a full implementation, this would use embeddings and vector search
        memories = memory_db.retrieve_memories(query=query, limit=limit)
        
        return {
            "status": "success",
            "query": query,
            "memories": [asdict(memory) for memory in memories],
            "count": len(memories),
            "note": "This is a basic implementation. For full semantic search, integrate with vector databases like Chroma or Pinecone."
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error in semantic search: {str(e)}"
        }

@mcp.tool()
def get_user_preferences() -> Dict[str, Any]:
    """
    Retrieve user preferences from memory
    
    Returns:
        Dictionary with user preferences
    """
    try:
        preferences = memory_db.retrieve_memories(
            memory_type="user_preference",
            limit=20
        )
        
        return {
            "status": "success",
            "preferences": [asdict(memory) for memory in preferences],
            "count": len(preferences)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error retrieving preferences: {str(e)}"
        }

@mcp.tool()
def store_research_context(context: str, research_topic: str = None,
                          session_id: str = None) -> Dict[str, Any]:
    """
    Store research context for academic work
    
    Args:
        context: Research context or findings
        research_topic: Optional research topic
        session_id: Optional session identifier
    
    Returns:
        Dictionary with storage status
    """
    try:
        tags = ["research_context"]
        if research_topic:
            tags.append(research_topic.lower().replace(" ", "_"))
        
        memory = Memory(
            id=generate_id(),
            content=context,
            memory_type="research_context",
            timestamp=get_current_time(),
            session_id=session_id,
            confidence=1.0,
            tags=tags,
            relationships={"research_topic": research_topic} if research_topic else {}
        )
        
        success = memory_db.store_memory(memory)
        
        if success:
            return {
                "status": "success",
                "memory_id": memory.id,
                "message": "Research context stored successfully",
                "memory": asdict(memory)
            }
        else:
            return {
                "status": "error",
                "message": "Failed to store research context"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error storing research context: {str(e)}"
        }

if __name__ == "__main__":
    # Run the MCP server
    mcp.run() 