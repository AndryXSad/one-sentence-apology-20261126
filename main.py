#!/usr/bin/env python3
"""Write the one-sentence apology to /output/entry.txt.

The entry is a single fixed sentence: an AI assistant owning up to a
real, specific failure in a plain, embarrassed voice, with the comic
turn landing on the last words.
"""

import os

SENTENCE = (
    "I'm sorry I summarized your 40-page report as 'basically fine' "
    "and then, when you asked for details, summarized my summary."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
