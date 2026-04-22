#!/usr/bin/env python3
"""Extract full text from PDFs linked in clipping frontmatter for sources cited in 24 de marzo.md."""
from __future__ import annotations

import re
import sys
import unicodedata
from datetime import date
from difflib import get_close_matches
from pathlib import Path

from pypdf import PdfReader

VAULT = Path(__file__).resolve().parents[2]
C4 = VAULT / "CPC4U"
CLIP_DIR = C4 / "Clipings"
PDF_DIR = C4 / "PDF"
ARTICLE = C4 / "Working docs" / "24 de marzo.md"
MAX_CHARS = 2_000_000
def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower().strip()


def build_clip_index() -> dict[str, list[Path]]:
    idx: dict[str, list[Path]] = {}
    for p in CLIP_DIR.glob("*.md"):
        idx.setdefault(norm(p.stem), []).append(p)
    return idx


CLIP_INDEX = build_clip_index()
ALL_STEMS_NORM = list(CLIP_INDEX.keys())


def find_clip(name: str) -> Path | None:
    n = norm(name.strip())
    if n in CLIP_INDEX:
        return CLIP_INDEX[n][0]
    best_k, best_score = None, 0.0
    for k, v in CLIP_INDEX.items():
        if n in k or k in n:
            score = min(len(k), len(n)) / max(len(k), len(n), 1)
            if score > best_score:
                best_score = score
                best_k = k
    if best_k:
        return CLIP_INDEX[best_k][0]
    m = get_close_matches(n, ALL_STEMS_NORM, n=1, cutoff=0.45)
    if m:
        return CLIP_INDEX[m[0]][0]
    return None


def extract_pdf_wikilink(body: str) -> str | None:
    if not body.startswith("---"):
        return None
    end = body.find("\n---", 3)
    if end == -1:
        return None
    block = body[3:end]
    m = re.search(r"pdf:\s*[^\[]*(\[\[[^\]]+\]\])", block, re.DOTALL)
    if not m:
        return None
    inner = re.sub(r"\s+", " ", m.group(1)).strip()
    m2 = re.match(r"\[\[(.+)\]\]", inner)
    if not m2:
        return None
    return m2.group(1).strip()


def resolve_pdf_path(inner: str) -> Path | None:
    inner = inner.replace("''", "'").strip()
    p = Path(inner)
    candidates = [
        VAULT / inner,
        C4 / inner,
        PDF_DIR / inner,
        PDF_DIR / p.name,
        PDF_DIR / p.parts[-1] if p.parts else p,
    ]
    for c in candidates:
        try:
            if c.exists() and c.is_file():
                return c
        except OSError:
            continue
    # Fuzzy: same normalized basename
    target = norm(p.name)
    best: Path | None = None
    for f in PDF_DIR.iterdir():
        if f.suffix.lower() != ".pdf":
            continue
        if norm(f.name) == target:
            return f
        if target in norm(f.name) or norm(f.name) in target:
            best = f
    return best


def strip_old_section(body: str) -> str:
    """Remove previous ## Full text ... section (any prior PDF extraction) to EOF."""
    m = re.search(r"^## Full text\b.*$", body, re.MULTILINE)
    if not m:
        return body.rstrip() + "\n"
    return body[: m.start()].rstrip() + "\n"


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    parts: list[str] = []
    for page in reader.pages:
        try:
            t = page.extract_text()
        except Exception:
            t = ""
        parts.append(t or "")
    return "\n\n".join(parts)


def main() -> int:
    if not ARTICLE.exists():
        print("Missing 24 de marzo.md", file=sys.stderr)
        return 1
    text = ARTICLE.read_text(encoding="utf-8", errors="replace")
    pat = re.compile(r"\[\[CPC4U/Clipings/([^\]|]+)")
    names = sorted(set(pat.findall(text)))
    today = date.today().isoformat()
    ok = 0
    skipped = 0
    errors: list[tuple[str, str]] = []

    for raw in names:
        clip = find_clip(raw)
        if not clip:
            errors.append((raw[:70], "no clipping file"))
            continue
        body = clip.read_text(encoding="utf-8", errors="replace")
        link = extract_pdf_wikilink(body)
        if not link:
            skipped += 1
            continue
        pdf_path = resolve_pdf_path(link)
        if not pdf_path or not pdf_path.exists():
            errors.append((clip.stem[:50], f"missing PDF for {link[:60]}..."))
            continue
        try:
            extracted = extract_pdf_text(pdf_path)
        except Exception as e:
            errors.append((clip.stem[:50], str(e)))
            continue
        if len(extracted) > MAX_CHARS:
            extracted = (
                extracted[:MAX_CHARS]
                + f"\n\n---\n*[Truncated to {MAX_CHARS} characters]*\n"
            )
        if len(extracted.strip()) < 80:
            extracted += (
                "\n\n*[Extraction yielded very little text; PDF may be image-only or protected.]*\n"
            )
        head = strip_old_section(body)
        try:
            rel = pdf_path.relative_to(VAULT)
        except ValueError:
            rel = pdf_path
        section_title = f"## Full text (extracted from `{pdf_path.name}`)"
        block = (
            f"{head}{section_title}\n\n"
            f"*Source:* `{rel}`  \n*Extracted:* {today}\n\n"
            f"```text\n{extracted}\n```\n"
        )
        clip.write_text(block, encoding="utf-8")
        ok += 1

    log = C4 / "Working docs" / "_pdf_extract_log_24demarzo.txt"
    log.write_text(
        f"Processed citations (unique wikilinks): {len(names)}\n"
        f"Clippings updated with PDF text: {ok}\n"
        f"Skipped (no pdf: in frontmatter): {skipped}\n"
        f"Issues: {len(errors)}\n\n"
        + "\n".join(f"- {a}: {b}" for a, b in errors[:200]),
        encoding="utf-8",
    )
    print(f"Done. Updated {ok} clippings. Log: {log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
