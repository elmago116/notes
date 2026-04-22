#!/usr/bin/env python3
"""
Keyword Normalization Script for RIS files.
Normalizes keywords to ensure consistent formatting.
"""

import re
import os
import shutil

class KeywordNormalizer:
    def __init__(self):
        # Hyphenation rules for common terms
        self.hyphenation_rules = {
            'human computer interaction': 'Human-Computer Interaction',
            'user centered design': 'User-Centered Design',
            'user centred design': 'User-Centred Design', 
            'human centered design': 'Human-Centered Design',
            'decision making': 'Decision-Making',
            'machine learning': 'Machine Learning',
            'deep learning': 'Deep Learning',
            'natural language processing': 'Natural Language Processing',
            'information retrieval': 'Information Retrieval',
            'semantic web': 'Semantic Web',
            'linked data': 'Linked Data',
            'cultural heritage': 'Cultural Heritage',
            'digital humanities': 'Digital Humanities',
            'data mining': 'Data Mining',
            'virtual reality': 'Virtual Reality',
            'augmented reality': 'Augmented Reality',
            'web based': 'Web-Based',
            'open source': 'Open-Source',
            'end users': 'End-Users',
            'eye tracking': 'Eye-Tracking',
            'question answering': 'Question Answering',
            'knowledge graph': 'Knowledge Graph',
            'knowledge graphs': 'Knowledge Graphs'
        }

    def normalize_keyword(self, keyword):
        """Normalize a single keyword."""
        # Clean whitespace
        keyword = ' '.join(keyword.split())
        
        # Check hyphenation rules first (case-insensitive)
        keyword_lower = keyword.lower()
        if keyword_lower in self.hyphenation_rules:
            return self.hyphenation_rules[keyword_lower]
        
        # Apply title case
        return self.smart_title_case(keyword)

    def smart_title_case(self, text):
        """Apply title case with smart handling."""
        small_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'if', 'in', 
                      'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet', 'with'}
        
        words = text.split()
        result = []
        
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word.lower() not in small_words:
                result.append(word.capitalize())
            else:
                result.append(word.lower())
        
        return ' '.join(result)

    def normalize_ris_file(self, input_file):
        """Normalize keywords in a RIS file."""
        if not os.path.exists(input_file):
            print(f"❌ File not found: {input_file}")
            return 0, 0
        
        # Create backup
        backup_file = input_file + '.backup_keywords'
        shutil.copy2(input_file, backup_file)
        print(f"📦 Created backup: {backup_file}")
        
        normalized_count = 0
        total_keywords = 0
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            normalized_lines = []
            
            for line in lines:
                if line.startswith('KW  - '):
                    keyword = line[6:].strip()
                    total_keywords += 1
                    
                    normalized_keyword = self.normalize_keyword(keyword)
                    
                    if normalized_keyword != keyword:
                        normalized_count += 1
                        print(f"  ✏️  '{keyword}' → '{normalized_keyword}'")
                    
                    normalized_lines.append(f"KW  - {normalized_keyword}\n")
                else:
                    normalized_lines.append(line)
            
            # Write normalized content
            with open(input_file, 'w', encoding='utf-8') as f:
                f.writelines(normalized_lines)
            
            print(f"✅ Processed {total_keywords} keywords, normalized {normalized_count}")
            return normalized_count, total_keywords
            
        except Exception as e:
            print(f"❌ Error processing {input_file}: {e}")
            if os.path.exists(backup_file):
                shutil.copy2(backup_file, input_file)
            return 0, 0

def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python normalize_keywords.py <filename>")
        return
    
    file_path = sys.argv[1]
    print(f"🔄 Normalizing keywords in: {os.path.basename(file_path)}")
    
    normalizer = KeywordNormalizer()
    normalized, total = normalizer.normalize_ris_file(file_path)
    
    print(f"📊 Summary: {normalized}/{total} keywords normalized ({(normalized/total)*100:.1f}%)")

if __name__ == "__main__":
    main()
