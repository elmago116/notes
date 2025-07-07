import xml.etree.ElementTree as ET
import re
from collections import namedtuple, defaultdict
import os
import html
import json

# Data structures to hold schema information
Table = namedtuple('Table', ['id', 'name', 'columns', 'is_associative'])
Column = namedtuple('Column', ['id', 'name', 'type'])
ObjectProperty = namedtuple('ObjectProperty', ['name', 'domain', 'range', 'inverse_of'])

def to_camel_case(s, upper=True):
    s = re.sub(r'[,\.\(\)]', '', s)  # Remove special chars
    s = re.sub(r"(_|-)+", " ", str(s)).title().replace(" ", "")
    if not s:
        return "Unnamed"
    if not upper:
        return s[0].lower() + s[1:]
    return s

def clean_value(value):
    if not value:
        return ""
    clean = re.sub('<.*?>', '', value)
    clean = html.unescape(clean)
    return clean.strip()

def parse_drawio(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    mx_graph_model = root.find('.//mxGraphModel')
    if mx_graph_model is None:
        return []

    cells = {cell.get('id'): cell for cell in mx_graph_model.findall('.//mxCell')}
    
    children_map = defaultdict(list)
    for c_id, cell in cells.items():
        parent_id = cell.get('parent')
        if parent_id and parent_id in cells:
            children_map[parent_id].append(cell)

    tables = []
    table_cells = [c for c in cells.values() if c.get('style') and 'shape=table' in c.get('style') and c.get('value')]

    for table_cell in table_cells:
        table_id = table_cell.get('id')
        table_name = clean_value(table_cell.get('value'))
        columns = []
        
        row_cells = [c for c in children_map.get(table_id, []) if c.get('style') and 'shape=tableRow' in c.get('style')]

        for row_cell in row_cells:
            row_id = row_cell.get('id')
            row_children = children_map.get(row_id, [])
            
            col_type = ''
            col_name = ''

            if row_children:
                row_children.sort(key=lambda c: int(c.find('./mxGeometry').get('x', 0)))
                
                type_cell = row_children[0]
                type_cell_value = clean_value(type_cell.get('value'))
                
                name_cell = row_children[1] if len(row_children) > 1 else None

                if type_cell_value in ['PK', 'FK']:
                    col_type = type_cell_value
                    if name_cell is not None:
                        col_name = clean_value(name_cell.get('value'))
                elif name_cell is not None:
                    col_name = clean_value(name_cell.get('value'))
                elif type_cell_value:
                    col_name = type_cell_value
            
            if col_name:
                columns.append(Column(id=row_id, name=col_name, type=col_type))
        
        fk_count = sum(1 for col in columns if col.type == 'FK')
        is_associative = len(columns) > 0 and fk_count >= 2 and (fk_count / len(columns)) > 0.5
        
        tables.append(Table(id=table_id, name=table_name, columns=columns, is_associative=is_associative))
        
    return tables

def find_pk_for_fk(fk_col, schema, tables_by_pk):
    fk_name_base = to_camel_case(fk_col.name, upper=False).lower().replace("fk", "").replace("id", "")
    
    best_match = None
    max_match_len = 0

    for pk, table in tables_by_pk.items():
        if pk in fk_name_base:
            if len(pk) > max_match_len:
                max_match_len = len(pk)
                best_match = table

    if best_match:
        return best_match

    if fk_name_base in tables_by_pk:
        return tables_by_pk[fk_name_base]

    return None

def generate_markdown(schema, output_path):
    tables_by_pk = {}
    for table in schema:
        if not table.is_associative:
            for col in table.columns:
                if col.type == 'PK':
                    pk_base_name = to_camel_case(col.name, upper=False).lower().replace("id", "")
                    tables_by_pk[pk_base_name] = table

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Inventario de transformaciones SIDBRINT\n\n")

        f.write("## Inventario de transformaciones (Nivel columna)\n\n")
        f.write("| Tabla | Atributo | Tipo de atributo | Regla de transformación | Cómo se aplica | Ejemplo Turtle (TTL) |\n")
        f.write("|-------|----------|------------------|------------------------|----------------|----------------------|\n")
        
        for table in schema:
            class_name = to_camel_case(table.name)
            if table.is_associative:
                 f.write(f"| {table.name} | - | Tabla asociativa | Regla 2 | Se transforma en owl:ObjectProperty inversa. | ... |\n")
            else:
                for col in table.columns:
                    prop_name = to_camel_case(col.name, upper=False)
                    if col.type == 'PK':
                        f.write(f"| {table.name} | {col.name} | Clave primaria | Regla 1 | Se usa como identificador de la clase :{class_name}. | :{class_name} a owl:Class . |\n")
                    elif col.type == 'FK':
                        referenced_table = find_pk_for_fk(col, schema, tables_by_pk)
                        range_class = to_camel_case(referenced_table.name) if referenced_table else "Thing"
                        f.write(f"| {table.name} | {col.name} | Clave foránea | Regla 3 | Se transforma en owl:ObjectProperty. | :{prop_name} a owl:ObjectProperty ; rdfs:domain :{class_name} ; rdfs:range :{range_class} . |\n")
                    else:
                        f.write(f"| {table.name} | {col.name} | Regular | Regla 4 | Se transforma en owl:DatatypeProperty. | :{prop_name} a owl:DatatypeProperty ; rdfs:domain :{class_name} ; rdfs:range xsd:string . |\n")
        f.write("\n")

        f.write("## Tabla 1: Clases\n\n")
        f.write("| Clase | Expresión Turtle |\n")
        f.write("| - | - |\n")
        for table in schema:
            if not table.is_associative:
                class_name = to_camel_case(table.name)
                f.write(f"| {class_name} | :{class_name} a owl:Class . |\n")
        f.write("\n")

        f.write("## Tabla 2: owl:DatatypeProperty de cada clase\n\n")
        f.write("| Clase | DatatypeProperty | Expresión Turtle |\n")
        f.write("| - | - | - |\n")
        for table in schema:
            if not table.is_associative:
                class_name = to_camel_case(table.name)
                for col in table.columns:
                    if not col.type:
                        prop_name = to_camel_case(col.name, upper=False)
                        f.write(f"| {class_name} | {prop_name} | :{prop_name} a owl:DatatypeProperty ; rdfs:domain :{class_name} ; rdfs:range xsd:string . |\n")
        f.write("\n")

        object_properties = []
        for table in schema:
            if not table.is_associative:
                domain_class = to_camel_case(table.name)
                for col in table.columns:
                    if col.type == 'FK':
                        referenced_table = find_pk_for_fk(col, schema, tables_by_pk)
                        if referenced_table:
                            prop_name = f"has{to_camel_case(referenced_table.name)}"
                            range_class = to_camel_case(referenced_table.name)
                            inverse_name = f"is{to_camel_case(referenced_table.name)}Of"
                            object_properties.append(ObjectProperty(prop_name, domain_class, range_class, inverse_name))
                            object_properties.append(ObjectProperty(inverse_name, range_class, domain_class, prop_name))


        for table in schema:
            if table.is_associative:
                fks = [c for c in table.columns if c.type == 'FK']
                if len(fks) == 2:
                    t1_fk, t2_fk = fks
                    table1 = find_pk_for_fk(t1_fk, schema, tables_by_pk)
                    table2 = find_pk_for_fk(t2_fk, schema, tables_by_pk)
                    if table1 and table2:
                        class1 = to_camel_case(table1.name)
                        class2 = to_camel_case(table2.name)
                        prop1_name = f"has{class2}"
                        prop2_name = f"has{class1}"
                        object_properties.append(ObjectProperty(prop1_name, class1, class2, prop2_name))
                        object_properties.append(ObjectProperty(prop2_name, class2, class1, prop1_name))

        unique_object_properties = {op.name: op for op in object_properties}.values()

        f.write("## Tabla de Relaciones (owl:ObjectProperty)\n\n")
        f.write("| Relación | Dominio | Rango | Es inversa de | Expresión Turtle |\n")
        f.write("| - | - | - | - | - |\n")
        for prop in unique_object_properties:
            f.write(f"| {prop.name} | {prop.domain} | {prop.range} | {prop.inverse_of} | :{prop.name} a owl:ObjectProperty ; rdfs:domain :{prop.domain} ; rdfs:range :{prop.range} . |\n")
        f.write("\n")

        f.write("## Tabla de Inferencias\n\n")
        f.write("| Inferencia | Tipo | Explicación | Expresión Turtle (TTL) |\n")
        f.write("| - | - | - | - |\n")
        for prop in unique_object_properties:
            if prop.inverse_of:
                 f.write(f"| Si un {prop.domain} {prop.name} un {prop.range}, entonces ese {prop.range} {prop.inverse_of} ese {prop.domain} | Implícita | Por las propiedades inversas owl:inverseOf entre {prop.name} y {prop.inverse_of} | :{prop.name} owl:inverseOf :{prop.inverse_of} . |\n")
        f.write("\n")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    drawio_file = os.path.join(script_dir, '..', 'Dissenys ER', 'SIDBRINT.drawio')
    output_md_file = os.path.join(script_dir, 'inventario de transformaciones SIDBRINT.md')
    
    schema = parse_drawio(drawio_file)
    generate_markdown(schema, output_md_file)
    print(f"Markdown file '{output_md_file}' generated successfully.")

if __name__ == '__main__':
    main() 