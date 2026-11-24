#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Entrypoint for the make.fun program/v1 harness. It writes exactly one
roast line to /output/entry.txt and prints nothing. The line is fixed
text, so every run produces the same bytes.

The joke: my phone's face unlock knows every face except mine before
coffee. The cat, the pillow and a photo all get in; I do not.
The line is 105 characters, inside the 200-character gate.
"""

import os
import sys

ROAST = "My phone's face unlock recognises my cat, my pillow and a photo of me \u2014 everyone except me before coffee."
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def roast_line():
    """Return the single roast line, stripped of stray whitespace."""
    line = ROAST.strip()
    if not line:
        raise ValueError("roast line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast line is {len(line)} chars, over {MAX_CHARS}")
    return line


def main():
    line = roast_line()
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
