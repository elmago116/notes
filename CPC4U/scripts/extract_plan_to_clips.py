#!/usr/bin/env python3
"""Extract full text from PDFs/DOCs referenced by CPC4U/Working docs/Plan.md into matching Clipings notes."""
from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parents[3]
PLAN = VAULT / "CPC4U" / "Working docs" / "Plan.md"
CLIP_DIR = VAULT / "CPC4U" / "Clipings"
PDF_DIR = VAULT / "CPC4U" / "PDF"

MARK_START = "<!-- auto-extract-plan:start -->"
MARK_END = "<!-- auto-extract-plan:end -->"

# Minimum similarity to attach a Plan link to a PDF filename
RATIO_PDF_MIN = 0.52
# Minimum to attach Plan link to a clipping note title (stem)
RATIO_CLIP_MIN = 0.72


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def loose(s: str) -> str:
    s = fold(norm(s))
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    return s


def parse_plan_links(text: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for m in re.finditer(r"\[\[([^\]]+)\]\]", text):
        raw = m.group(1).strip()
        if "|" in raw:
            raw = raw.split("|", 1)[0].strip()
        if not raw or raw in seen:
            continue
        seen.add(raw)
        out.append(raw)
    return out


def list_source_files() -> list[Path]:
    files: list[Path] = []
    for pat in ("*.pdf", "*.doc", "*.docx"):
        files.extend(PDF_DIR.glob(pat))
    return files


def best_pdf_for_link(link: str, sources: list[Path]) -> tuple[Path | None, float]:
    # Strip .pdf/.doc/.docx from link so "file.doc" still matches "file.pdf"
    link_base = re.sub(r"\.(pdf|docx?)$", "", link, flags=re.I)
    ll = loose(link_base)
    scored: list[tuple[Path, float]] = []
    for p in sources:
        pb = re.sub(r"\.(pdf|docx?)$", "", p.name, flags=re.I)
        r = SequenceMatcher(None, ll, loose(pb)).ratio()
        scored.append((p, r))
    if not scored:
        return None, 0.0
    max_r = max(t[1] for t in scored)
    if max_r < RATIO_PDF_MIN:
        return None, 0.0
    top = [t for t in scored if t[1] >= max_r - 1e-6]
    # Prefer .pdf over .doc/.docx when scores tie (same stem, different format)
    def sort_key(item: tuple[Path, float]) -> tuple:
        p, r = item
        ext = p.suffix.lower()
        pref = 0 if ext == ".pdf" else 1
        return (-r, pref, len(p.name))

    top.sort(key=sort_key)
    return top[0][0], top[0][1]


def yaml_title_and_pdf(md_path: Path) -> tuple[str | None, str | None]:
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None, None
    title = fm.get("title")
    if title is not None and not isinstance(title, str):
        title = str(title)
    pdf_val = fm.get("pdf")
    pdf_s = None
    if isinstance(pdf_val, str):
        m = re.search(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", pdf_val)
        if m:
            pdf_s = m.group(1).strip().split("/")[-1]
    return title, pdf_s


def clip_for_link_and_pdf(
    link: str,
    pdf_path: Path | None,
    clips: list[Path],
) -> tuple[Path | None, float]:
    ll = loose(link)
    best: tuple[Path | None, float] = (None, 0.0)
    pdf_name = pdf_path.name.lower() if pdf_path else ""

    pdf_matches: list[tuple[Path, str | None]] = []
    for md in clips:
        title, pdf_field = yaml_title_and_pdf(md)
        if pdf_path and pdf_field and pdf_field.lower() == pdf_name:
            pdf_matches.append((md, title))
    if pdf_matches:
        best_md, best_tr = pdf_matches[0], 0.0
        for md, title in pdf_matches:
            ta = title or md.stem
            tr = SequenceMatcher(None, ll, loose(ta)).ratio()
            if tr > best_tr:
                best_tr, best_md = tr, md
        return best_md, 1.0

    for md in clips:
        title, pdf_field = yaml_title_and_pdf(md)
        if title:
            r = SequenceMatcher(None, ll, loose(title)).ratio()
            if r > best[1]:
                best = (md, r)
        stem = md.stem
        r2 = SequenceMatcher(None, ll, loose(stem)).ratio()
        if r2 > best[1]:
            best = (md, r2)

    if best[1] >= RATIO_CLIP_MIN:
        return best
    return None, 0.0


def extract_text(path: Path) -> str:
    suf = path.suffix.lower()
    if suf == ".pdf":
        r = subprocess.run(
            ["pdftotext", "-layout", str(path), "-"],
            capture_output=True,
            text=True,
            timeout=600,
        )
        if r.returncode != 0:
            return f"[pdftotext error: {r.stderr[:500]}]"
        return r.stdout.strip()
    if suf == ".docx":
        r = subprocess.run(
            ["pandoc", "-f", "docx", "-t", "plain", str(path)],
            capture_output=True,
            text=True,
            timeout=600,
        )
        if r.returncode != 0:
            return f"[pandoc error: {r.stderr[:500]}]"
        return r.stdout.strip()
    if suf == ".doc":
        r = subprocess.run(
            ["textutil", "-convert", "txt", "-stdout", str(path)],
            capture_output=True,
            text=True,
            timeout=600,
        )
        if r.returncode != 0:
            return f"[textutil error: {r.stderr[:500]}]"
        return r.stdout.strip()
    return f"[unsupported type: {suf}]"


def inject_extract(body: str, extract: str, source_name: str) -> str:
    block = (
        f"\n\n{MARK_START}\n"
        f"## Full text (extracted from `{source_name}`)\n\n"
        f"{extract}\n"
        f"{MARK_END}\n"
    )
    if MARK_START in body and MARK_END in body:
        pre, _, rest = body.partition(MARK_START)
        _, _, post = rest.partition(MARK_END)
        return pre.rstrip() + block + post.lstrip()
    return body.rstrip() + block


def main() -> int:
    if not PLAN.is_file():
        print(f"Missing {PLAN}", file=sys.stderr)
        return 1

    plan_text = PLAN.read_text(encoding="utf-8")
    links = parse_plan_links(plan_text)
    sources = list_source_files()
    clips = sorted(CLIP_DIR.glob("*.md"))

    report: list[str] = []
    done_clips: set[Path] = set()
    for link in links:
        pdf_path, pr = best_pdf_for_link(link, sources)
        if not pdf_path:
            report.append(f"SKIP (no PDF match ≥{RATIO_PDF_MIN}): {link!r}")
            continue

        clip_md, cr = clip_for_link_and_pdf(link, pdf_path, clips)
        if not clip_md:
            report.append(
                f"SKIP (no clip ≥{RATIO_CLIP_MIN}): PDF={pdf_path.name!r} link={link!r}"
            )
            continue
        if clip_md in done_clips:
            report.append(f"DEDUPE skip clip={clip_md.name} (already filled this run)")
            continue

        try:
            text = extract_text(pdf_path)
        except Exception as e:
            report.append(f"EXTRACT FAIL {pdf_path.name}: {e}")
            continue

        raw = clip_md.read_text(encoding="utf-8")
        if raw.startswith("---"):
            parts = raw.split("---", 2)
            if len(parts) >= 3:
                fm, body = parts[1], parts[2]
                new_body = inject_extract(body, text, pdf_path.name)
                clip_md.write_text(f"---{fm}---{new_body}", encoding="utf-8")
                done_clips.add(clip_md)
                report.append(
                    f"OK  clip={clip_md.name}  pdf={pdf_path.name}  match_pdf={pr:.3f} match_clip={cr:.3f} chars={len(text)}"
                )
                continue
        report.append(f"SKIP (no YAML frontmatter): {clip_md.name}")

    print("\n".join(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
