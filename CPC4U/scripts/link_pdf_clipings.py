#!/usr/bin/env python3
"""Match CPC4U/PDF/*.pdf to Clipings notes via BibTeX `file` / `filename` and add `pdf` wikilink."""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import yaml

# scripts/link_pdf_clipings.py → vault root is parents[3] (…/Documents)
VAULT = Path(__file__).resolve().parents[3]
CLIP_DIR = VAULT / "CPC4U" / "Clipings"
PDF_DIR = VAULT / "CPC4U" / "PDF"

RATIO_MIN = 0.86


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s


def fold_accents(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def loose(s: str) -> str:
    s = norm(s)
    s = s.replace("\u03cc", "o")
    s = re.sub(r"-'-\s*", "", s)
    s = re.sub(r"\\['`^]?", "", s)
    s = re.sub(r"[`´']", "", s)
    s = re.sub(r"\s+", " ", s)
    return fold_accents(s)


def pdf_from_file_field(file_val: str | None) -> str | None:
    if not file_val:
        return None
    first = file_val.split(":", 1)[0].strip()
    if first.lower().endswith(".pdf"):
        return first
    return None


def tail_from_filename_field(fn: str | None) -> str | None:
    if not fn:
        return None
    fn = fn.replace("\\\\", "/").replace("\\", "/")
    parts = [p for p in fn.split("/") if p]
    if not parts:
        return None
    last = parts[-1]
    if last.lower().endswith(".pdf"):
        return last
    return None


def lead_token(loose_name: str) -> str:
    if " - " in loose_name:
        return loose_name.split(" - ", 1)[0]
    return loose_name.removesuffix(".pdf")


def load_clippings() -> list[tuple[Path, str]]:
    out: list[tuple[Path, str]] = []
    for md in CLIP_DIR.glob("*.md"):
        text = md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
        except Exception:
            continue
        name = pdf_from_file_field(fm.get("file"))
        if not name:
            name = tail_from_filename_field(fm.get("filename"))
        if name:
            out.append((md, name))
    return out


def build_lead_index(
    clips: list[tuple[Path, str]],
) -> dict[str, list[tuple[Path, str]]]:
    by_lead: dict[str, list[tuple[Path, str]]] = defaultdict(list)
    for md, n in clips:
        by_lead[lead_token(loose(n))].append((md, n))
    return by_lead


def best_match(
    pdf_name: str,
    clips: list[tuple[Path, str]],
    by_lead: dict[str, list[tuple[Path, str]]],
) -> tuple[float, Path | None]:
    pl = loose(pdf_name)
    lk = lead_token(pl)
    bucket = by_lead.get(lk, [])

    def scan(items: list[tuple[Path, str]]) -> tuple[float, Path | None]:
        best_r, best_md = 0.0, None
        for md, n in items:
            bl = loose(n)
            r = SequenceMatcher(None, pl, bl).ratio()
            if r > best_r:
                best_r, best_md = r, md
        return best_r, best_md

    br, bm = scan(bucket if bucket else clips)
    if br < RATIO_MIN and bucket:
        br, bm = scan(clips)
    return br, bm


def insert_pdf_property(body: str, wikilink: str) -> str:
    parts = body.split("---", 2)
    if len(parts) < 3:
        return body
    fm = yaml.safe_load(parts[1])
    if not isinstance(fm, dict):
        return body
    if fm.get("pdf") == wikilink:
        return body
    fm.pop("pdf", None)
    out: dict = {}
    inserted = False
    for k, v in fm.items():
        if k == "created":
            out["pdf"] = wikilink
            inserted = True
        out[k] = v
    if not inserted:
        out["pdf"] = wikilink
    dump = yaml.safe_dump(
        out,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{dump}---{parts[2]}"


def main() -> int:
    clips = load_clippings()
    by_lead = build_lead_index(clips)

    linked = 0
    no_match: list[str] = []
    duplicate_note: list[str] = []

    clip_to_pdf: dict[Path, str] = {}

    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        wikilink = f"[[CPC4U/PDF/{pdf.name}]]"
        match_md: Path | None = None
        for md, bn in clips:
            if norm(bn) == norm(pdf.name):
                match_md = md
                break
        score = 1.0
        if match_md is None:
            score, match_md = best_match(pdf.name, clips, by_lead)
            if match_md is None or score < RATIO_MIN:
                no_match.append(f"{score:.3f}\t{pdf.name}")
                continue

        if match_md in clip_to_pdf:
            duplicate_note.append(
                f"{match_md.name}\talready:{clip_to_pdf[match_md]}\tskipped:{pdf.name}\t{score:.3f}"
            )
            continue

        clip_to_pdf[match_md] = pdf.name

        text = match_md.read_text(encoding="utf-8")
        new_text = insert_pdf_property(text, wikilink)
        if new_text != text:
            match_md.write_text(new_text, encoding="utf-8")
            linked += 1

    print(f"Updated notes (pdf link added): {linked}", file=sys.stderr)
    print(f"No match ({len(no_match)} PDFs)", file=sys.stderr)
    rpt = CLIP_DIR / "_pdf_link_report.txt"
    lines = ["=== NO MATCH ===", *no_match, "", "=== DUPLICATE NOTE (same clipping, multiple PDFs) ===", *duplicate_note]
    rpt.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {rpt}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
