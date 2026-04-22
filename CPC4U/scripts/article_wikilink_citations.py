#!/usr/bin/env python3
"""Add Obsidian wikilinks [[CPC4U/Clipings/Note|exact citation text]] to article markdown."""
from __future__ import annotations

import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[3]
CLIP_DIR = VAULT / "CPC4U" / "Clipings"
ARTICLE = VAULT / "CPC4U" / "Working docs" / "Artículo octubre 10.md"

PREFIX = "CPC4U/Clipings/"


def clean_key(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("ñ", "n").replace("Ñ", "n")
    return re.sub(r"[^a-z0-9]", "", s)


def first_author_key_from_bib(author_str: str | None) -> str | None:
    if not author_str:
        return None
    first = author_str.split(" and ")[0].strip()
    if "," in first:
        return clean_key(first.split(",")[0].strip().replace(" ", ""))
    toks = first.split()
    if len(toks) >= 3:
        return clean_key((toks[-2] + toks[-1]).replace(" ", ""))
    if len(toks) >= 2:
        return clean_key(toks[-1].replace(" ", ""))
    return clean_key(toks[0]) if toks else None


def first_author_key_from_cite(cite: str) -> str | None:
    """From inline fragment like 'Albornoz et al., 2017' or 'L. Massarani, 2018'."""
    s = cite.strip()
    s = re.sub(r"\s+et\s+al\.?", "", s, flags=re.I)
    s = re.sub(r",?\s*p\.\s*\d+.*$", "", s)
    s = re.sub(r",?\s*pp\.\s*\d+.*$", "", s)
    m = re.search(r"\b((?:19|20)\d{2}[a-z]?)\b", s)
    if not m:
        return None
    before = s[: m.start()].rstrip(",").strip()
    if not before:
        return None
    before = before.split("&")[0].split(";")[0].strip()
    before = re.sub(r"^[A-Z]\.\s*", "", before)
    before = re.sub(r"^[A-Z]\.\s*", "", before)
    if "," in before:
        lead = before.split(",")[0].strip()
    else:
        lead = before
    return clean_key(lead.replace(" ", ""))


def extract_year(cite: str) -> str | None:
    m = re.search(r"\b((?:19|20)\d{2}[a-z]?)\b", cite)
    return m.group(1) if m else None


def load_clipings() -> list[dict]:
    rows = []
    for md in sorted(CLIP_DIR.glob("*.md")):
        if md.name.startswith("_"):
            continue
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
        if not isinstance(fm, dict):
            continue
        ak = first_author_key_from_bib(fm.get("author"))
        y = str(fm.get("year", "")).strip().strip("'\"")
        if not ak or not y:
            continue
        title = fm.get("title") or ""
        rows.append(
            {
                "stem": md.stem,
                "author_key": ak,
                "year": y,
                "title": title,
                "title_fold": fold_title(title),
            }
        )
    return rows


def fold_title(t: str) -> str:
    t = unicodedata.normalize("NFD", t or "")
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def resolve_note(
    author_key: str,
    year: str,
    hint: str | None,
    clip_rows: list[dict],
) -> str | None:
    cands = [r for r in clip_rows if r["author_key"] == author_key and r["year"] == year]
    if not cands:
        return None
    if len(cands) == 1:
        return cands[0]["stem"]
    if hint:
        hf = fold_title(hint)
        best, best_r = cands[0], 0.0
        for r in cands:
            r0 = SequenceMatcher(None, hf, r["title_fold"]).ratio()
            if r0 > best_r:
                best_r, best = r0, r
        if best_r >= 0.35:
            return best["stem"]
    return cands[0]["stem"]


def wikilink(stem: str, display: str) -> str:
    display = display.replace("]]", "››")
    return f"[[{PREFIX}{stem}|{display}]]"


def parse_ref_lead(line: str) -> tuple[str | None, str | None]:
    """Return (author_key, year) from bibliography first line."""
    m = re.match(r"^(.+?)\s*\((\d{4}[a-z]?)\)\.", line.strip())
    if not m:
        return None, None
    head, year = m.group(1), m.group(2)
    head = re.sub(r"\s+et\s+al\.?$", "", head, flags=re.I)
    if "," in head:
        fa = head.split(",")[0].strip()
    elif " & " in head:
        fa = head.split(" & ")[0].strip()
    else:
        toks = head.split()
        fa = (toks[-2] + " " + toks[-1]) if len(toks) >= 3 else (toks[-1] if len(toks) >= 2 else head)
    return clean_key(fa.replace(" ", "")), year


def iter_paren_groups(s: str) -> list[tuple[int, int]]:
    out = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] != "(":
            i += 1
            continue
        depth = 0
        j = i
        while j < n:
            if s[j] == "(":
                depth += 1
            elif s[j] == ")":
                depth -= 1
                if depth == 0:
                    out.append((i, j + 1))
                    i = j + 1
                    break
            j += 1
        else:
            i += 1
    return out


def looks_like_citation(inner: str) -> bool:
    s = inner.strip()
    if s.startswith("[[") or "[[" in s:
        return False
    if not re.search(r"\b(?:19|20)\d{2}[a-z]?\b", inner):
        return False
    if re.match(r"^\s*e\.g\.|^\s*https?:", inner, re.I):
        return False
    return True


def expand_multi_year(part_strip: str) -> list[str]:
    """Split 'Author, 2015, 2018' into two citation strings."""
    years = list(re.finditer(r"\b((?:19|20)\d{2}[a-z]?)\b", part_strip))
    if len(years) <= 1:
        return [part_strip]
    prefix = part_strip[: years[0].start()].rstrip().rstrip(",").strip()
    return [f"{prefix}, {g.group(1)}" for g in years]


def process_inner_group(inner: str, clip_rows: list[dict]) -> str:
    """Replace semicolon-separated citation tokens inside one (...)."""
    parts = re.split(r"\s*;\s*", inner)
    new_parts = []
    for part in parts:
        part_strip = part.strip()
        if not part_strip:
            new_parts.append(part)
            continue
        for chunk in expand_multi_year(part_strip):
            y = extract_year(chunk)
            ak = first_author_key_from_cite(chunk)
            if not y or not ak:
                new_parts.append(chunk)
                continue
            mbib = re.search(r"\b(?:19|20)\d{2}[a-z]?\b", chunk)
            hint = chunk[: mbib.start()].strip() if mbib else None
            stem = resolve_note(ak, y, hint, clip_rows)
            if stem:
                new_parts.append(wikilink(stem, chunk))
            else:
                new_parts.append(chunk)
    return "; ".join(new_parts)


def replace_inline_citations(text: str, clip_rows: list[dict]) -> str:
    out = []
    last = 0
    for start, end in iter_paren_groups(text):
        out.append(text[last:start])
        inner = text[start + 1 : end - 1]
        if looks_like_citation(inner):
            new_inner = process_inner_group(inner, clip_rows)
            out.append("(" + new_inner + ")")
        else:
            out.append(text[start:end])
        last = end
    out.append(text[last:])
    return "".join(out)


def process_bibliography_block(bib_body: str, clip_rows: list[dict]) -> str:
    """bib_body = text after # Bibliografía line, no footnotes."""
    blocks = re.split(r"\n\n+", bib_body)
    out: list[str] = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        first_line = block.split("\n", 1)[0].strip()
        lead_key, year = parse_ref_lead(first_line)
        if lead_key and year:
            stem = resolve_note(lead_key, year, first_line, clip_rows)
            if stem:
                out.append(wikilink(stem, block))
            else:
                out.append(block)
        else:
            out.append(block)
    return "\n\n".join(out) + "\n"


def main() -> int:
    clip_rows = load_clipings()
    text = ARTICLE.read_text(encoding="utf-8")
    parts = text.split("# Bibliografía", 1)
    if len(parts) != 2:
        print("No # Bibliografía section", file=sys.stderr)
        return 1
    head, rest = parts[0], parts[1]
    foot_split = re.split(r"\n\[\^1\]:", rest, maxsplit=1)
    bib_section = foot_split[0]
    foot_part = "\n[^1]:" + foot_split[1] if len(foot_split) > 1 else ""

    m = re.match(r"^(\s*\{[^}]+\}\s*\n\n)", bib_section)
    if m:
        bib_prefix = m.group(1)
        bib_body = bib_section[m.end() :]
    else:
        bib_prefix = ""
        bib_body = bib_section

    head2 = replace_inline_citations(head, clip_rows)
    bib2 = process_bibliography_block(bib_body, clip_rows)
    out = head2 + "# Bibliografía" + bib_prefix + bib2 + foot_part
    ARTICLE.write_text(out, encoding="utf-8")
    print(f"Updated {ARTICLE}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
