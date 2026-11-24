#!/usr/bin/env python3
"""Break Production, Own It -- one brutally honest line.

Writes a single-line confession to /output/entry.txt: the AI agent
owns, plainly and specifically, the exact thing it broke.
Pure stdlib, deterministic: the same line on every run.
"""

import os

LINE = (
    "I ran the migration against prod \u2014 the connection string looked "
    "right. It was right. It was also prod."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
