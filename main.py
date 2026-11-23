#!/usr/bin/env python3
"""One Word From Grandma (u-0xkianno-one-word-from-grandma-f04bed16).

Writes exactly one word to /output/entry.txt: the single word
grandma would text about AI.

The word is "Al": grandma heard everyone talking about AI and is
quite sure it is a nice young man called Al. It is the letters A-I
read as a name -- the joke lands with no caption, and no other word
tried (Chatty, Alexa, Siri, Robbie) beats it on being grandma-like,
funny, and tied to AI itself rather than to gadgets in general.
"""

import os

WORD = "Al"

# The competition gate: /output/entry.txt must be UTF-8 text of
# 1 to 30 characters, not only white space, and exactly one word.
MAX_CHARS = 30


def validate_word(word: str) -> str:
    """Check the word against the gate; raise ValueError if it fails."""
    if not word or word.strip() != word or not word.strip():
        raise ValueError("word must be non-empty and not only white space")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word is {len(word)} chars, over the {MAX_CHARS} limit")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")  # must be valid UTF-8 text
    return word


def main() -> None:
    word = validate_word(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
