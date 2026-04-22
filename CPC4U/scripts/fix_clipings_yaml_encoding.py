#!/usr/bin/env python3
"""
Normalize LaTeX-style escapes in Obsidian clipping YAML frontmatter (Qiqqa, autotags, keywords, etc.).
Does not modify body content below the closing ---.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ACCENT_LOWER = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú",
}
ACCENT_UPPER = {
    "A": "Á",
    "E": "É",
    "I": "Í",
    "O": "Ó",
    "U": "Ú",
}
TILDE = {
    "n": "ñ",
    "N": "Ñ",
    "a": "ã",
    "o": "õ",
    "A": "Ã",
    "O": "Õ",
}


def fix_latex_escapes(s: str) -> str:
    if not s:
        return s

    # Ampersand in journal titles (LaTeX \\& first, then \&)
    s = s.replace(r"\\&", "&")
    s = s.replace(r"\&", "&")

    # Common malformed title: tecnolog\''ia -> tecnología; am\''erica -> américa
    s = re.sub(r"\\'\'ia", "ía", s)
    s = re.sub(r"\\'\'io", "ío", s)
    s = re.sub(r"\\'\'ie", "íe", s)

    def sub_double_accent(m: re.Match) -> str:
        ch = m.group(1)
        return ACCENT_LOWER.get(ch, ACCENT_UPPER.get(ch, m.group(0)))

    # \''e -> é (e.g. am\''erica) after specific triples above
    s = re.sub(r"\\'\'([aeiouAEIOU])", sub_double_accent, s)

    # Two backslashes before 'vowel' (e.g. Am\\'erica, cient\\'ifica in quoted Qiqqa)
    s = re.sub(r"\\\\'([aeiouAEIOU])", sub_double_accent, s)

    def sub_single_accent(m: re.Match) -> str:
        ch = m.group(1)
        return ACCENT_LOWER.get(ch, ACCENT_UPPER.get(ch, m.group(0)))

    # Single backslash (e.g. tecnolog\'ia, p\'ublica)
    s = re.sub(r"\\'([aeiouAEIOU])", sub_single_accent, s)

    # \'Capital for names like \'Alvarez -> Álvarez (single backslash only; double handled above)
    def sub_upper_name(m: re.Match) -> str:
        ch = m.group(1)
        return ACCENT_UPPER.get(ch, m.group(0))

    s = re.sub(r"\\'([AEIOU])", sub_upper_name, s)

    # Repair paths where \\'A was matched by single-backslash rule (docs\Álvarez -> docs\\Álvarez)
    s = re.sub(r"docs\\(Álvarez)", r"docs\\\\Álvarez", s)

    # BibTeX/Mendeley export: \' + \ + syllable (e.g. Mar\'\ia, Mart\'\inez)
    for pat, rep in (
        (r"\\'\\inez", "ínez"),
        (r"\\'\\irez", "írez"),
        (r"\\'\\ia", "ía"),
        (r"\\'\\io", "ío"),
        (r"\\'\\in", "ín"),
        (r"\\'\\it", "ít"),
        (r"\\'\\if", "íf"),
        (r"\\'\\ic", "íc"),
        (r"\\'\\is", "ís"),
        (r"\\'\\im", "ím"),
        (r"\\'\\iz", "íz"),
        (r"\\'\\ix", "íx"),
    ):
        s = s.replace(pat, rep)

    # Tilde: \~n -> ñ (Espa\~na). Try double backslash first.
    def sub_tilde(m: re.Match) -> str:
        ch = m.group(1)
        return TILDE.get(ch, m.group(0))

    s = re.sub(r"\\\\~([a-zA-Z])", sub_tilde, s)
    s = re.sub(r"\\~([a-zA-Z])", sub_tilde, s)

    # Remaining common TeX
    s = s.replace(r"\_", "_")
    s = s.replace(r"\%", "%")
    s = s.replace(r"\#", "#")
    s = s.replace(r"\$", "$")

    # BibTeX braced accents: Garc{\'\i}a -> García
    s = re.sub(r"\{\\'\\i\}([a-z])", lambda m: "í" + m.group(1), s)
    s = re.sub(r"\{\\'\\e\}([a-z])", lambda m: "é" + m.group(1), s)
    s = re.sub(r"\{\\'\\a\}([a-z])", lambda m: "á" + m.group(1), s)
    s = re.sub(r"\{\\'\\o\}([a-z])", lambda m: "ó" + m.group(1), s)
    s = re.sub(r"\{\\'\\u\}([a-z])", lambda m: "ú" + m.group(1), s)

    return s


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\r?\n", text)
    if not m:
        return None, text
    start = m.end()
    close = re.search(r"\r?\n---\r?\n", text[start:])
    if not close:
        close2 = re.search(r"\r?\n---\s*$", text[start:])
        if not close2:
            return None, text
        fm = text[start : start + close2.start()]
        body = text[start + close2.end() :]
        return fm, body
    fm = text[start : start + close.start()]
    body = text[start + close.end() :]
    return fm, body


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(raw)
    if fm is None:
        return False
    new_fm = fix_latex_escapes(fm)
    if new_fm == fm:
        return False
    # Preserve original line endings in body
    out = "---\n" + new_fm.rstrip() + "\n---\n" + body
    path.write_text(out, encoding="utf-8")
    return True


def main() -> int:
    root = Path(__file__).resolve().parent.parent / "Clipings"
    if not root.is_dir():
        print("Clipings folder not found", file=sys.stderr)
        return 1
    n = 0
    for p in sorted(root.glob("*.md")):
        try:
            if process_file(p):
                n += 1
                print(p.name)
        except OSError as e:
            print(f"SKIP {p}: {e}", file=sys.stderr)
    print(f"Updated {n} files.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
