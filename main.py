#!/usr/bin/env python3
"""One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16).

Writes exactly one word to /output/entry.txt: the single word
grandma would text about AI.

The word is "Al": grandma heard everyone talking about AI and is
quite sure it is a nice young man called Al.
"""

import os

WORD = "Al"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
