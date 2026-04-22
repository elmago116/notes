#!/usr/bin/env python3
"""Resolve PDFs from citations in 24 de marzo.md and extract text with pdftotext."""
import re
import subprocess
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
DOC = VAULT / "CPC4U/Working docs/24 de marzo.md"
PDF_DIR = VAULT / "CPC4U/PDF"
CLIP = VAULT / "CPC4U/Clipings"
OUT_DIR = VAULT / "CPC4U/Working docs/_pdf_text_24_marzo"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def find_note(rel: str) -> Path | None:
    name = rel.split("/", 2)[-1].strip()
    exact = VAULT / f"{rel}.md"
    if exact.exists():
        return exact
    # strip Obsidian truncation
    if name.endswith("..."):
        name = name[:-3].strip()
    n = norm(name)
    best = None
    best_score = 0.0
    for p in CLIP.glob("*.md"):
        sn = norm(p.stem)
        if sn == n:
            return p
        ratio = SequenceMatcher(None, n[: min(80, len(n))], sn[:120]).ratio()
        if n[:40] in sn or sn[:40] in n:
            ratio = max(ratio, 0.85)
        if ratio > best_score:
            best_score = ratio
            best = p
    if best and best_score >= 0.65:
        return best
    return None


def extract_pdf_link(fm_block: str) -> str | None:
    # Multiline wiki link: pdf: '[[CPC4U/PDF/Foo\n  bar.pdf]]'
    m = re.search(
        r"pdf:\s*(?:'|\")?\s*\[\[([\s\S]*?)\]\]",
        fm_block,
        re.IGNORECASE,
    )
    if m:
        inner = re.sub(r"\s+", " ", m.group(1).strip())
        return inner
    # Zotero-style file: ... .pdf:docs/...
    m = re.search(
        r"(?:^|\n)filename:\s*(.+?\.pdf)",
        fm_block,
        re.MULTILINE | re.DOTALL,
    )
    if m:
        fn = Path(m.group(1).strip().splitlines()[0].strip()).name
        if fn.endswith(".pdf"):
            return fn
    return None


def resolve_pdf_link(link: str) -> Path | None:
    if not link:
        return None
    link = link.replace("\\'", "'")
    if link.startswith("CPC4U/PDF/"):
        p = VAULT / link
        if p.exists():
            return p
    fn = Path(link).name
    # exact
    for base in (PDF_DIR, CLIP):
        p = base / fn
        if p.exists():
            return p
    # fuzzy: same end of filename
    stem = fn.replace(".pdf", "")[:50]
    for base in (PDF_DIR,):
        for p in base.glob("*.pdf"):
            if stem in p.name or fn[-30:] in p.name:
                return p
    # Parejo-style odd quotes
    key = re.sub(r"[^a-zA-Z0-9áéíóúñÁÉÍÓÚÑ]+", "", stem)[:30]
    if key:
        for p in PDF_DIR.glob("*.pdf"):
            if key in re.sub(r"[^a-zA-Z0-9áéíóúñ]+", "", p.name):
                return p
    return None


def main():
    text = DOC.read_text(encoding="utf-8", errors="replace")
    paths = sorted(set(re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", text)))
    clip_paths = [x for x in paths if "CPC4U/Clipings" in x]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    seen_pdf: set[Path] = set()

    for rel in clip_paths:
        note = find_note(rel)
        if not note:
            rows.append((rel, None, None, "missing_note"))
            continue
        raw = note.read_text(encoding="utf-8", errors="replace")
        if not raw.startswith("---"):
            rows.append((rel, str(note), None, "no_yaml"))
            continue
        end = raw.find("\n---", 3)
        if end == -1:
            rows.append((rel, str(note), None, "bad_yaml"))
            continue
        fm = raw[3:end]
        plink = extract_pdf_link(fm)
        if not plink:
            rows.append((rel, str(note), None, "no_pdf_field"))
            continue
        p = resolve_pdf_link(plink)
        if not p:
            rows.append((rel, str(note), plink, "pdf_not_found"))
            continue
        rows.append((rel, str(note), str(p), "ok"))
        seen_pdf.add(p.resolve())

    # extract
    index_lines = [
        "---",
        "title: Extractos PDF — citas en «24 de marzo»",
        "date: 2026-03-24",
        "tags:",
        "  - op/process",
        "---",
        "",
        f"Fuente de citas: [[24 de marzo]]. Texto extraído con `pdftotext` (poppler-utils).",
        "",
        "**Nota:** Algunas notas de clipping pueden carecer de `pdf:` o de archivo en `CPC4U/PDF` (p. ej. UPB cuento, Orozco políticas México, taller UNSJ); esas quedan listadas al final como `no_pdf_field`.",
        "",
    ]
    for pdf in sorted(seen_pdf, key=lambda x: x.name):
        safe = re.sub(r"[^\w\-. ]+", "_", pdf.stem)[:120]
        out_txt = OUT_DIR / f"{safe}.txt"
        try:
            subprocess.run(
                ["/opt/homebrew/bin/pdftotext", "-layout", str(pdf), str(out_txt)],
                check=True,
                capture_output=True,
                timeout=120,
            )
            index_lines.append(f"- **{pdf.name}** → [[_pdf_text_24_marzo/{out_txt.name}|texto extraído]]")
        except Exception as e:
            index_lines.append(f"- **{pdf.name}** ERROR: {e}")

    # report
    rep = OUT_DIR / "_index.md"
    index_lines.append("")
    index_lines.append("## Estado por cita")
    index_lines.append("")
    for rel, note, pdf, st in rows:
        index_lines.append(f"- `{st}` — `{rel.split('/')[-1][:70]}`")
    rep.write_text("\n".join(index_lines), encoding="utf-8")

    print(f"Unique PDFs extracted: {len(seen_pdf)}")
    print(f"Index: {rep}")


if __name__ == "__main__":
    main()
