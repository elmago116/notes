#!/usr/bin/env python3
"""Apply ordered replacements for common Qiqqa/BibTeX → UTF-8 mojibake patterns in markdown."""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Longest / most specific first to avoid partial overlaps.
REPLACEMENTS: list[tuple[str, str]] = [
    # LaTeX-style broken accents (from BibTeX export)
    (r"Mart'\\inez", "Martínez"),
    (r"Mart'\\in ", "Martín "),
    (r"Ort'\\iz", "Ortíz"),
    (r"Ram'\\irez", "Ramírez"),
    (r"tecnolog'\\ia", "tecnología"),
    (r"bater'\\ia", "batería"),
    (r"medici'\\on", "medición"),
    # Greek omicron (U+03BF) mistaken for Latin o + acute in author names / words
    ("Lόpez", "López"),
    ("Quirόs", "Quirós"),
    ("Delgado-Quirόs", "Delgado-Quirós"),
    ("Castrillόn", "Castrillón"),
    ("Barbosa-Gόmez", "Barbosa-Gómez"),
    ("mediciόn", "medición"),
    ("apropiaciόn", "apropiación"),
    ("Comerόn", "Comerón"),
    ("Histόria", "Historia"),
    # Title fragments where UTF-8 was split / truncated
    ("cientcomo", "científica como"),
    ("Divulgacion cienten", "Divulgación científica en"),
    ("La cultura cienten los", "La cultura científica en los"),
    ("Fomento de la cultura cienten las", "Fomento de la cultura científica en las"),
    ("tecnologe innovacion en la polpublica", "tecnología y la innovación en la política pública"),
    ("tecnology la innovacion", "tecnología y la innovación"),
    ("tecnology", "tecnología"),
    ("polpublica colombiana", "política pública colombiana"),
    ("polpublica", "política pública"),
    ("PolPublicas", "Políticas públicas"),
    ("analde la gobernanza", "analítica de la gobernanza"),
    ("perioden los procesos", "periódicas en los procesos"),
    ("baterde indicadores", "batería de indicadores"),
    ("Secretarde Ciencia y Tecnologde", "Secretaría de Ciencia y Tecnología de"),
    ("tecnologen una universidad", "tecnología en una universidad"),
    ("tecnologen el ", "tecnología en el "),
    ("Esquema analítica de la gobernanza", "Esquema analítico de la gobernanza"),
    ("del conocimiento científica como", "del conocimiento científico como"),
    ("humaños", "humanos"),
    ("Mart'\\in-Mart'\\in", "Martín-Martín"),
    ("López-Cόzar", "López-Cózar"),
    ("Tecnologcomo alternativa", "Tecnología como alternativa"),
    ("comunicacion cient", "comunicación científica"),
    ("poluniversitaria ly", "política universitaria y"),
    ("tecnolog propuesta", "tecnología: propuesta"),
    ("cientiificas", "científicas"),
    ("cientiifica", "científica"),
    ("desafpara", "desafíos para"),
    (" perspectiva cr", " perspectiva crítica"),
    # Phrases before generic comunicacion → comunicación
    ("comunicacion publica", "comunicación pública"),
    ("Comunicacion publica", "Comunicación pública"),
    # Generic Spanish accents (ASCII forms from BibTeX)
    ("comunicacion ", "comunicación "),
    ("comunicacion,", "comunicación,"),
    ("comunicacion.", "comunicación."),
    ("Comunicacion ", "Comunicación "),
    ("divulgacion ", "divulgación "),
    ("Divulgacion ", "Divulgación "),
    ("Produccion ", "Producción "),
    ("vinculacion ", "vinculación "),
    ("apropiacion ", "apropiación "),
    ("Apropiacion ", "Apropiación "),
    ("innovacion ", "innovación "),
    ("evaluacion", "evaluación"),
    ("gestion ", "gestión "),
    ("formacion ", "formación "),
    ("investigacion ", "investigación "),
    ("representacion ", "representación "),
    ("visibilizacion ", "visibilización "),
    ("problematicas ", "problemáticas "),
    ("metodologica ", "metodológica "),
    ("academicas", "académicas"),
    ("academico", "académico"),
    ("articulos ", "artículos "),
    ("practicas ", "prácticas "),
    ("practica ", "práctica "),
    ("practica,", "práctica,"),
    ("politicas ", "políticas "),
    ("tecnologia ", "tecnología "),
    ("tecnologia,", "tecnología,"),
    ("tecnologia.", "tecnología."),
    (" la tecnologia", " la tecnología"),
    ("tecnologia y", "tecnología y"),
    ("America Latina", "América Latina"),
    ("Iberoamerica", "Iberoamérica"),
    (" Latinoamerica.", " Latinoamérica."),
    (" Latinoamerica ", " Latinoamérica "),
    ("anos ", "años "),
    ("anos.", "años."),
    ("anos,", "años,"),
    ("anos entre", "años entre"),
    ("anos de", "años de"),
    ("cuarenta anos", "cuarenta años"),
    ("25 anos", "25 años"),
    ("Diez anos", "Diez años"),
    ("publica de la", "pública de la"),
    ("publica y", "pública y"),
    ("Servicio Publico", "Servicio Público"),
    ("Universidades Publicas", "Universidades Públicas"),
    ("extension universitaria", "extensión universitaria"),
    ("Guias para", "Guías para"),
    ("medicion ", "medición "),
    ("Bogota ", "Bogotá "),
    ("Bogota,", "Bogotá,"),
    ("Medellin", "Medellín"),
    (" critica ", " crítica "),
    (" arqueologico", " arqueológico"),
    (" arqueologico.", " arqueológico."),
    # Trailing truncated tecnolog in wikilink paths
    ("y la tecnolog|", "y la tecnología|"),
    ("ciencia y la tecnolog|", "ciencia y la tecnología|"),
    ("y la tecnolog]", "y la tecnología]"),
    (" cienten ", " científica en "),
    ("cientifica ", "científica "),
    ("cientifica.", "científica."),
    ("cientifico ", "científico "),
    ("conocimiento cientifico|", "conocimiento científico|"),
    ("cientificos ", "científicos "),
    ("CPC4U/Cliping/", "CPC4U/Clipings/"),
]


def apply(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]] or [
        Path(__file__).resolve().parents[3] / "CPC4U" / "Working docs" / "24 de marzo.md"
    ]
    for path in paths:
        raw = path.read_text(encoding="utf-8")
        fixed = apply(raw)
        path.write_text(fixed, encoding="utf-8")
        print(f"Updated {path}")


if __name__ == "__main__":
    main()
