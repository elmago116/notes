#!/usr/bin/env python3
"""
Translator MCP Server (DeepL)

- Tools:
  - translate_text: Translate text with optional source/target langs
  - detect_language: Detect language of a text
  - supported_languages: List supported target/source languages

Env:
- DEEPL_API_KEY: Your DeepL API key (free or pro)

Date: 2025-08-13
"""

from __future__ import annotations

import asyncio
import os
from typing import List

try:
    import deepl  # type: ignore
except Exception as e:
    deepl = None  # Will error at runtime if not installed

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


server = Server("translator-mcp")


def require_deepl_translator() -> "deepl.Translator":
    if deepl is None:
        raise RuntimeError("deepl package not installed. pip install deepl")
    api_key = os.environ.get("DEEPL_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPL_API_KEY environment variable not set")
    return deepl.Translator(api_key)


@server.list_tools()
async def list_tools() -> List[Tool]:
    return [
        Tool(
            name="translate_text",
            description="Translate text using DeepL (set DEEPL_API_KEY)",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "target_lang": {"type": "string", "description": "e.g., ES, EN-GB, FR"},
                    "source_lang": {"type": "string", "description": "optional source language code"}
                },
                "required": ["text", "target_lang"]
            }
        ),
        Tool(
            name="detect_language",
            description="Detect language of a text via DeepL",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="supported_languages",
            description="List DeepL supported languages",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> List[TextContent]:
    if name == "translate_text":
        return await translate_text(arguments)
    if name == "detect_language":
        return await detect_language(arguments)
    if name == "supported_languages":
        return await supported_languages(arguments)
    raise ValueError(f"Unknown tool: {name}")


async def translate_text(args: dict) -> List[TextContent]:
    text: str = args["text"]
    target_lang: str = args["target_lang"]
    source_lang: str | None = args.get("source_lang")
    translator = require_deepl_translator()

    def _run():
        return translator.translate_text(text, target_lang=target_lang, source_lang=source_lang)

    result = await asyncio.to_thread(_run)
    out = result.text if hasattr(result, "text") else str(result)
    return [TextContent(type="text", text=out)]


async def detect_language(args: dict) -> List[TextContent]:
    text: str = args["text"]
    translator = require_deepl_translator()

    def _run():
        return translator.detect_language(text)

    result = await asyncio.to_thread(_run)
    out = f"{result.language} (confidence={getattr(result, 'confidence', 'n/a')})"
    return [TextContent(type="text", text=out)]


async def supported_languages(_: dict) -> List[TextContent]:
    translator = require_deepl_translator()

    def _run():
        targets = translator.get_target_languages()
        sources = translator.get_source_languages()
        return targets, sources

    targets, sources = await asyncio.to_thread(_run)
    tgt = "\n".join([f"{l.code}\t{l.name}" for l in targets])
    src = "\n".join([f"{l.code}\t{l.name}" for l in sources])
    text = f"Supported target languages:\n{tgt}\n\nSupported source languages:\n{src}"
    return [TextContent(type="text", text=text)]


async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="translator-mcp",
                server_version="1.0.0",
                capabilities=server.get_capabilities(),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())


