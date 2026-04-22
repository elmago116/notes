#!/usr/bin/env python3
"""
Extract text from UBXAT PDF files and save as markdown files in Clippings folder.
"""

import os
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: pypdf library not found.")
    print("Installing pypdf...")
    import subprocess
    # Try multiple installation methods
    methods = [
        [sys.executable, "-m", "pip", "install", "--user", "pypdf"],
        [sys.executable, "-m", "pip", "install", "--break-system-packages", "pypdf"],
    ]
    
    installed = False
    for method in methods:
        result = subprocess.run(method, capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ pypdf installed successfully")
            installed = True
            break
    
    if not installed:
        print("Failed to install pypdf automatically.")
        print("Please install manually with one of these commands:")
        print("  pip3 install --user pypdf")
        print("  pip3 install --break-system-packages pypdf")
        print("  brew install python-pypdf (if available)")
        sys.exit(1)
    
    # Reload after installation
    import importlib
    import pypdf
    importlib.reload(pypdf)
    from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract all text from a PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text_parts = []
        
        print(f"  📄 Processing {len(reader.pages)} pages...")
        
        for i, page in enumerate(reader.pages, 1):
            try:
                text = page.extract_text()
                if text.strip():
                    text_parts.append(text)
            except Exception as e:
                print(f"    ⚠️  Warning: Could not extract text from page {i}: {e}")
        
        return "\n\n".join(text_parts)
    except Exception as e:
        print(f"  ❌ Error reading PDF: {e}")
        return None

def sanitize_filename(filename):
    """Convert PDF filename to a clean markdown filename."""
    # Remove .pdf extension
    name = filename.replace('.pdf', '')
    # Replace special characters that might cause issues
    name = name.replace('/', '-').replace('\\', '-')
    # Remove or replace problematic characters
    name = name.replace(':', '-').replace('?', '').replace('*', '')
    return name + '.md'

def main():
    # Define paths
    base_dir = Path(__file__).parent
    pdf_dir = base_dir / "PDF" / "Peninsula"
    clippings_dir = base_dir / "Clippings"
    
    # PDF files to extract
    pdf_files = [
        "UBXAT - General Platform Overview (EN).pdf",
        "UBXAT - Readme (EN).pdf",
        "UBXAT - Resumen Fase de DisenÞo(DCU).pdf",
        "UBXAT API Module (EN).pdf",
        "UBXAT SPARQL (EN).pdf"
    ]
    
    print(f"{'='*60}")
    print("UBXAT PDF Text Extraction")
    print(f"{'='*60}\n")
    
    if not pdf_dir.exists():
        print(f"❌ Error: PDF directory not found: {pdf_dir}")
        return
    
    if not clippings_dir.exists():
        print(f"⚠️  Creating Clippings directory: {clippings_dir}")
        clippings_dir.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    for pdf_filename in pdf_files:
        pdf_path = pdf_dir / pdf_filename
        
        if not pdf_path.exists():
            print(f"⚠️  File not found: {pdf_filename}")
            continue
        
        print(f"\n📖 Extracting: {pdf_filename}")
        
        # Extract text
        text = extract_text_from_pdf(pdf_path)
        
        if text is None or not text.strip():
            print(f"  ❌ No text extracted from {pdf_filename}")
            continue
        
        # Create markdown filename
        md_filename = sanitize_filename(pdf_filename)
        md_path = clippings_dir / md_filename
        
        # Check if file already exists
        if md_path.exists():
            print(f"  ⚠️  File already exists: {md_filename}")
            print(f"  🔄 Overwriting existing file...")
            # Auto-overwrite in non-interactive mode
            # Uncomment the following lines if you want to skip instead:
            # print(f"  ⏭️  Skipping {pdf_filename}")
            # continue
        
        # Create markdown content with YAML frontmatter
        md_content = f"""---
title: {pdf_filename.replace('.pdf', '')}
source: {pdf_filename}
type: PDF extraction
---

{text}
"""
        
        # Write markdown file
        try:
            md_path.write_text(md_content, encoding='utf-8')
            print(f"  ✅ Created: {md_filename}")
            print(f"     Size: {len(text)} characters, {len(text.split())} words")
            success_count += 1
        except Exception as e:
            print(f"  ❌ Error writing file: {e}")
    
    print(f"\n{'='*60}")
    print(f"Extraction complete: {success_count}/{len(pdf_files)} files processed")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

