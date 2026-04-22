#!/usr/bin/env python3
"""
Citation MCP Server
Provides tools to search Crossref and OpenAlex APIs for academic citation metadata

Date: 2025-08-12
Research Context: DCMI citation standards for semantic web and GLAM research
"""

import asyncio
import json
import re
from typing import Any, Sequence
from urllib.parse import quote_plus
import aiohttp
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    ListToolsRequest,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)

# Initialize MCP server
server = Server("citation-mcp")

# API endpoints
CROSSREF_API = "https://api.crossref.org"
OPENALEX_API = "https://api.openalex.org"

@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools for citation metadata retrieval"""
    return [
        Tool(
            name="search_crossref",
            description="Search Crossref API for academic papers by title, author, or DOI",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (title, author, or DOI)"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 5)",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="search_openalex",
            description="Search OpenAlex API for academic papers by title, author, or DOI",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (title, author, or DOI)"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 5)",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_citation_metadata",
            description="Get comprehensive citation metadata from both Crossref and OpenAlex",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Paper title to search for"
                    },
                    "author": {
                        "type": "string",
                        "description": "Author name (optional)"
                    },
                    "doi": {
                        "type": "string",
                        "description": "DOI (optional, if available)"
                    }
                },
                "required": ["title"]
            }
        ),
        Tool(
            name="format_dcmi_citation",
            description="Format citation metadata into DCMI-compliant format",
            inputSchema={
                "type": "object",
                "properties": {
                    "metadata": {
                        "type": "object",
                        "description": "Citation metadata from API search"
                    },
                    "citation_number": {
                        "type": "integer",
                        "description": "Citation number for bibliography"
                    }
                },
                "required": ["metadata", "citation_number"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls for citation metadata retrieval"""
    
    if name == "search_crossref":
        return await search_crossref(arguments)
    elif name == "search_openalex":
        return await search_openalex(arguments)
    elif name == "get_citation_metadata":
        return await get_citation_metadata(arguments)
    elif name == "format_dcmi_citation":
        return await format_dcmi_citation(arguments)
    else:
        raise ValueError(f"Unknown tool: {name}")

async def search_crossref(args: dict) -> list[TextContent]:
    """Search Crossref API for academic papers"""
    query = args["query"]
    max_results = args.get("max_results", 5)
    
    # Build Crossref query
    params = {
        "query": query,
        "rows": max_results,
        "select": "DOI,title,author,published-print,container-title,volume,issue,page"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{CROSSREF_API}/works", params=params) as response:
            if response.status == 200:
                data = await response.json()
                results = []
                
                for item in data.get("message", {}).get("items", []):
                    # Extract authors
                    authors = []
                    for author in item.get("author", []):
                        if "given" in author and "family" in author:
                            authors.append(f"{author['given']} {author['family']}")
                        elif "family" in author:
                            authors.append(author["family"])
                    
                    # Extract title
                    title = item.get("title", [""])[0] if item.get("title") else "Unknown Title"
                    
                    # Extract journal
                    journal = item.get("container-title", [""])[0] if item.get("container-title") else "Unknown Journal"
                    
                    # Extract year
                    year = None
                    if item.get("published-print"):
                        year = item["published-print"][0].get("date-parts", [[]])[0][0]
                    
                    # Extract DOI
                    doi = item.get("DOI", "")
                    
                    result = {
                        "doi": doi,
                        "title": title,
                        "authors": authors,
                        "journal": journal,
                        "year": year,
                        "volume": item.get("volume", ""),
                        "issue": item.get("issue", ""),
                        "pages": item.get("page", ""),
                        "source": "crossref"
                    }
                    results.append(result)
                
                return [TextContent(
                    type="text",
                    text=f"Found {len(results)} results from Crossref:\n\n" + 
                         json.dumps(results, indent=2, ensure_ascii=False)
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"Error searching Crossref: {response.status}"
                )]

async def search_openalex(args: dict) -> list[TextContent]:
    """Search OpenAlex API for academic papers"""
    query = args["query"]
    max_results = args.get("max_results", 5)
    
    # Build OpenAlex query
    params = {
        "search": query,
        "per_page": max_results,
        "select": "id,title,publication_year,authorships,publication_date,primary_location,doi"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{OPENALEX_API}/works", params=params) as response:
            if response.status == 200:
                data = await response.json()
                results = []
                
                for item in data.get("results", []):
                    # Extract authors
                    authors = []
                    for authorship in item.get("authorships", []):
                        author = authorship.get("author", {})
                        if author:
                            display_name = author.get("display_name", "")
                            if display_name:
                                authors.append(display_name)
                    
                    # Extract title
                    title = item.get("title", "Unknown Title")
                    
                    # Extract journal
                    journal = "Unknown Journal"
                    if item.get("primary_location", {}).get("source", {}):
                        journal = item["primary_location"]["source"].get("display_name", "Unknown Journal")
                    
                    # Extract year
                    year = item.get("publication_year")
                    
                    # Extract DOI
                    doi = item.get("doi", "")
                    
                    result = {
                        "doi": doi,
                        "title": title,
                        "authors": authors,
                        "journal": journal,
                        "year": year,
                        "source": "openalex"
                    }
                    results.append(result)
                
                return [TextContent(
                    type="text",
                    text=f"Found {len(results)} results from OpenAlex:\n\n" + 
                         json.dumps(results, indent=2, ensure_ascii=False)
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"Error searching OpenAlex: {response.status}"
                )]

async def get_citation_metadata(args: dict) -> list[TextContent]:
    """Get comprehensive citation metadata from both APIs"""
    title = args["title"]
    author = args.get("author", "")
    doi = args.get("doi", "")
    
    results = {}
    
    # Search both APIs
    if doi:
        # If DOI is provided, search by DOI
        crossref_results = await search_crossref({"query": doi, "max_results": 1})
        openalex_results = await search_openalex({"query": doi, "max_results": 1})
    else:
        # Search by title and author
        query = f"{title} {author}".strip()
        crossref_results = await search_crossref({"query": query, "max_results": 3})
        openalex_results = await search_openalex({"query": query, "max_results": 3})
    
    results["crossref"] = crossref_results[0].text
    results["openalex"] = openalex_results[0].text
    
    return [TextContent(
        type="text",
        text=f"Comprehensive citation metadata search results:\n\n" +
             f"**Crossref Results:**\n{results['crossref']}\n\n" +
             f"**OpenAlex Results:**\n{results['openalex']}"
    )]

async def format_dcmi_citation(args: dict) -> list[TextContent]:
    """Format citation metadata into DCMI-compliant format"""
    metadata = args["metadata"]
    citation_number = args["citation_number"]
    
    # Extract metadata fields
    authors = metadata.get("authors", [])
    title = metadata.get("title", "Unknown Title")
    journal = metadata.get("journal", "Unknown Journal")
    year = metadata.get("year", "Unknown Year")
    doi = metadata.get("doi", "")
    volume = metadata.get("volume", "")
    pages = metadata.get("pages", "")
    
    # Format authors
    if authors:
        if len(authors) == 1:
            author_str = authors[0]
        elif len(authors) == 2:
            author_str = f"{authors[0]} & {authors[1]}"
        else:
            author_str = f"{authors[0]} et al."
    else:
        author_str = "Unknown Author"
    
    # Build DCMI citation
    citation = f"[{citation_number}] {author_str}, {title}, {journal}"
    
    if volume:
        citation += f" {volume}"
    if pages:
        citation += f" ({pages})"
    
    citation += f" {year}"
    
    if doi:
        citation += f". DOI: {doi}"
    
    citation += "."
    
    return [TextContent(
        type="text",
        text=f"DCMI-formatted citation:\n\n{citation}"
    )]

async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="citation-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities=None,
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
