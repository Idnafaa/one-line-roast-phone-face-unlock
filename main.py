#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (1-200 characters) to
/output/entry.txt, where the make.fun program/v1 harness reads it.
No network, no input, fully deterministic.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

ROAST = (
    "My phone's face unlock recognises my cat, my pillow and a photo "
    "of me \u2014 everyone except me before coffee."
)


def main() -> None:
    text = ROAST.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"roast must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
