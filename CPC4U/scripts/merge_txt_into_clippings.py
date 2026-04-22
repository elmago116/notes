#!/usr/bin/env python3
"""Merge pre-extracted text from _pdf_text_24_marzo/*.txt into corresponding Clipings notes."""
from __future__ import annotations

import re
import sys
import unicodedata
from datetime import date
from difflib import SequenceMatcher, get_close_matches
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
TXT_DIR = VAULT / "CPC4U/Working docs/_pdf_text_24_marzo"
CLIP_DIR = VAULT / "CPC4U/Clipings"
MAX_CHARS = 2_500_000


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower().strip()


def strip_full_text_section(body: str) -> str:
    m = re.search(r"^## Full text\b.*$", body, re.MULTILINE)
    if not m:
        return body.rstrip() + "\n"
    return body[: m.start()].rstrip() + "\n"


def build_clip_index() -> dict[str, Path]:
    return {norm(p.stem): p for p in CLIP_DIR.glob("*.md")}


def find_clip(txt_stem: str, clips: dict[str, Path]) -> Path | None:
    if not clips:
        return None
    n = norm(txt_stem)
    if n in clips:
        return clips[n]
    best_p, best_s = None, 0.0
    for cs, path in clips.items():
        if len(n) >= 40 and len(cs) >= 40 and (n.startswith(cs[:40]) or cs.startswith(n[:40])):
            r = SequenceMatcher(None, n, cs).ratio()
            if r > best_s:
                best_s, best_p = r, path
        elif n in cs or cs in n:
            r = SequenceMatcher(None, n, cs).ratio()
            if r > best_s and r > 0.55:
                best_s, best_p = r, path
    if best_p and best_s > 0.45:
        return best_p
    clip_stems = list(clips.keys())
    short = n[:80]
    m = get_close_matches(short, [c[:80] for c in clip_stems], n=1, cutoff=0.4)
    if m:
        for cs, path in clips.items():
            if cs[:80] == m[0]:
                return path
    return None


def main() -> int:
    if not TXT_DIR.is_dir():
        print("Missing folder:", TXT_DIR, file=sys.stderr)
        return 1
    clips = build_clip_index()
    today = date.today().isoformat()
    merged = 0
    skipped: list[str] = []
    for txt_path in sorted(TXT_DIR.glob("*.txt")):
        clip = find_clip(txt_path.stem, clips)
        if not clip:
            skipped.append(txt_path.name)
            continue
        raw = txt_path.read_text(encoding="utf-8", errors="replace")
        if len(raw) > MAX_CHARS:
            raw = raw[:MAX_CHARS] + f"\n\n---\n*[Truncated to {MAX_CHARS} characters]*\n"
        body = clip.read_text(encoding="utf-8", errors="replace")
        head = strip_full_text_section(body)
        rel_txt = txt_path.relative_to(VAULT)
        title = f"## Full text (extracted from `{rel_txt.as_posix()}`)"
        block = (
            f"{head}{title}\n\n"
            f"*Merged:* {today} (from pre-extracted text file)\n\n"
            f"```text\n{raw.rstrip()}\n```\n"
        )
        clip.write_text(block, encoding="utf-8")
        merged += 1

    log = VAULT / "CPC4U/Working docs/_merge_txt_into_clippings_log.txt"
    log.write_text(
        f"Merged: {merged}\nSkipped (no matching clipping): {len(skipped)}\n\n"
        + "\n".join(skipped),
        encoding="utf-8",
    )
    print(f"Merged {merged} files. Skipped {len(skipped)}. Log: {log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
