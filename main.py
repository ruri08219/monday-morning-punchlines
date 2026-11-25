#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

Writes the entry to /output/entry.txt. Standard library only.
"""

import os
import sys

ENTRY = "Monday knocked at 6am wearing my clothes and holding my keys. 'We both know how this ends,' it said. 'You're driving.'"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 chars, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out = os.path.join("/output", "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
