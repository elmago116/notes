 import csv
import re
import os
from thefuzz import fuzz, process

def read_schema_from_csv(filepath):
    """Reads the schema from the CSV file into a dictionary of entities and their properties."""
    schema = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                entity, prop = row
                if entity not in schema:
                    schema[entity] = []
                schema[entity].append(prop)
        print("SUCCESS: Read schema from schema_inventory.csv")
        return schema
    except FileNotFoundError:
        print(f"ERROR: Schema file not found at {filepath}")
        return None

def find_best_match(query, choices, score_cutoff=60):
    """Finds the best fuzzy match for a query from a list of choices."""
    if not choices:
        return None
    match, score = process.extractOne(query, choices, scorer=fuzz.token_set_ratio)
    if score >= score_cutoff:
        return match
    return None

def process_data_dictionary(dd_content, schema):
    """
    Processes the data dictionary content by following the manual guide's logic.
    FIXED: Now accounts for escaped underscores in the markdown.
    """
    updated_content = ""
    # Split the document into sections based on the "Entidad" headers.
    entity_sections = re.split(r'(# Entidad \*[^\*]+\*|# \[NOVA\] Entidad \*[^\*]+\*)', dd_content)
    
    # The first element is anything before the first header.
    updated_content += entity_sections[0]

    # Process each entity section (header + content block)
    for i in range(1, len(entity_sections), 2):
        header = entity_sections[i]
        content_block = entity_sections[i+1]
        updated_content += header

        entity_name_match = re.search(r'\*([^\*]+)\*', header)
        if not entity_name_match:
            updated_content += content_block
            continue
        
        dd_entity_name = entity_name_match.group(1).strip()
        print(f"\n--- Processing Entity: {dd_entity_name} ---")

        # Find the corresponding entity in the diagram schema
        schema_entity_name = find_best_match(dd_entity_name, schema.keys())
        if not schema_entity_name:
            print(f"  - No matching entity found in schema. Skipping.")
            updated_content += content_block
            continue
        
        print(f"  - Matched with schema entity: '{schema_entity_name}'")
        schema_properties = schema[schema_entity_name]
        
        # Process the content of this section, block by block (tables, paragraphs, etc.)
        processed_blocks = []
        # Split by double newline, which typically separates markdown elements.
        for block in content_block.split('\n\n'):
            # FIXED: Check if the block is a property table we need to modify.
            # Now looking for escaped underscores: nombre\_del\_atributo
            if block.strip().startswith('| nombre\\_del\\_atributo'):
                table_lines = block.strip().split('\n')
                # FIXED: Updated regex pattern to match escaped underscores
                prop_name_match = re.search(r'\|\s*nombre\\_del\\_atributo\s*\|\s*(.*?)\s*\|', table_lines[0])
                
                if prop_name_match:
                    dd_prop_name = prop_name_match.group(1).strip()
                    best_prop_match = find_best_match(dd_prop_name, schema_properties, score_cutoff=50)
                    
                    if best_prop_match:
                        print(f"    - Found property '{dd_prop_name}'. Matched to '{best_prop_match}'. Injecting row.")
                        new_row = f"| **posible name property desde los diagramas** | {best_prop_match} |"
                        
                        # Insert the new row before the "Equivalencias" line, or at the end.
                        insert_index = len(table_lines)
                        for j, line in enumerate(table_lines):
                            if "Equivalencias con otros esquemas" in line:
                                insert_index = j
                                break
                        table_lines.insert(insert_index, new_row)
                        processed_blocks.append('\n'.join(table_lines))
                    else:
                        print(f"    - Found property '{dd_prop_name}'. No match in schema.")
                        processed_blocks.append(block) # No match, add original block
                else:
                    print(f"    - Found property table but couldn't extract property name.")
                    processed_blocks.append(block) # Not a valid prop table, add original block
            else:
                processed_blocks.append(block) # Not a table, add original block

        updated_content += '\n\n'.join(processed_blocks)

    return updated_content

def main():
    """Main function."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    schema_csv_path = os.path.join(script_dir, 'schema_inventory.csv')
    dd_md_path = os.path.join(script_dir, 'CELIRU_diccionariDeDades-vDef-20220729.docx.md')
    output_md_path = os.path.join(script_dir, 'CELIRU_diccionariDeDades-vDef-20220729_FINAL.md')

    schema = read_schema_from_csv(schema_csv_path)
    if not schema:
        return

    try:
        with open(dd_md_path, 'r', encoding='utf-8') as f:
            dd_content = f.read()
    except FileNotFoundError:
        print(f"ERROR: Data dictionary file not found at {dd_md_path}")
        return

    updated_dd = process_data_dictionary(dd_content, schema)

    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(updated_dd)

    print(f"\nSUCCESS: Script finished. New file created at:\n{output_md_path}")
    print("This time it should actually work - the escaped underscores were the problem!")

if __name__ == "__main__":
    main() 