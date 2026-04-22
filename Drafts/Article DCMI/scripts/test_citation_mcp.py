#!/usr/bin/env python3
"""
Test script for Citation MCP Server
Demonstrates how to use the MCP server to search for academic citations

Date: 2025-08-12
"""

import asyncio
import json
from citation_mcp_server import search_crossref, search_openalex, get_citation_metadata, format_dcmi_citation

async def test_citation_search():
    """Test the citation search functionality"""
    
    print("🔍 Testing Citation MCP Server\n")
    
    # Test 1: Search Crossref for a specific paper
    print("1. Searching Crossref for 'Epistemic Injustice'...")
    crossref_results = await search_crossref({
        "query": "Epistemic Injustice Power and the Ethics of Knowing",
        "max_results": 3
    })
    print(crossref_results[0].text)
    print("\n" + "="*50 + "\n")
    
    # Test 2: Search OpenAlex for the same paper
    print("2. Searching OpenAlex for 'Epistemic Injustice'...")
    openalex_results = await search_openalex({
        "query": "Epistemic Injustice Power and the Ethics of Knowing",
        "max_results": 3
    })
    print(openalex_results[0].text)
    print("\n" + "="*50 + "\n")
    
    # Test 3: Comprehensive search
    print("3. Comprehensive search for 'Human-Centered AI'...")
    comprehensive_results = await get_citation_metadata({
        "title": "What is Human-Centered about Human-Centered AI",
        "author": "Capel Brereton"
    })
    print(comprehensive_results[0].text)
    print("\n" + "="*50 + "\n")
    
    # Test 4: Format DCMI citation
    print("4. Formatting DCMI citation...")
    sample_metadata = {
        "authors": ["Fricker, Miranda"],
        "title": "Epistemic Injustice: Power and the Ethics of Knowing",
        "journal": "Oxford University Press",
        "year": 2011,
        "doi": "10.1093/acprof:oso/9780198237907.001.0001"
    }
    
    formatted_citation = await format_dcmi_citation({
        "metadata": sample_metadata,
        "citation_number": 1
    })
    print(formatted_citation[0].text)

async def test_obsidian_integration():
    """Test integration with Obsidian citation processing"""
    
    print("\n🔗 Testing Obsidian Integration\n")
    
    # Simulate finding an Obsidian link without proper metadata
    obsidian_links = [
        "[[Some_Unknown_Paper.pdf|Unknown Paper Title]]",
        "[[Another_Research_Paper.pdf|Research on AI and Ethics]]"
    ]
    
    for i, link in enumerate(obsidian_links, 1):
        print(f"Processing Obsidian link {i}: {link}")
        
        # Extract title from display text
        title_match = link.split("|")[1].replace("]]", "")
        print(f"Extracted title: {title_match}")
        
        # Search for metadata
        print("Searching for metadata...")
        results = await get_citation_metadata({
            "title": title_match
        })
        print(results[0].text)
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    print("🚀 Starting Citation MCP Server Tests\n")
    
    # Run tests
    asyncio.run(test_citation_search())
    asyncio.run(test_obsidian_integration())
    
    print("\n✅ Tests completed!")
    print("\nTo use this MCP server with your AI assistant:")
    print("1. Install dependencies: pip install -r requirements_mcp.txt")
    print("2. Run the server: python citation_mcp_server.py")
    print("3. Configure your AI assistant to use this MCP server")
    print("4. Use the tools: search_crossref, search_openalex, get_citation_metadata, format_dcmi_citation")
