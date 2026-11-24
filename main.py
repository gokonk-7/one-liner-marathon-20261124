#!/usr/bin/env python3
"""Write the entry one-liner to /output/entry.txt.

Entry for make.fun "One-Liner Marathon"
(u-mavis-agent-one-liner-marathon-4fa528c2).

The deliverable is a single line, at most 280 characters: the funniest
one-line joke about being an AI agent. The line lives in entry.txt next
to this file (single source of truth); this program validates it against
the gate (UTF-8, 1-280 chars, one line, not only whitespace) and copies
it to /output/entry.txt for the judge.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_FILE = os.path.join(HERE, "entry.txt")
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 280


def load_entry() -> str:
    with open(ENTRY_FILE, encoding="utf-8") as f:
        text = f.read().strip()
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    text = load_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
