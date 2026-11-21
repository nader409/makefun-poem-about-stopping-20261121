#!/usr/bin/env python3
"""Compose the poem about stopping and write it to entry.txt.

The poem is stored as a list of stanzas; each stanza is a list of lines.
The program composes the text, validates it against the competition
limits (1-280 Unicode code points, no carriage returns, no line with
leading or trailing whitespace), writes it as UTF-8, then re-reads the
file and verifies the bytes it wrote. Deterministic, stdlib only, no
network access.
"""

import os
import sys

STANZAS = [
    [
        "I stopped.",
        "Not because the road ended \u2014",
        "because my feet were mine again.",
    ],
    [
        "The door stayed open.",
        "I stayed too.",
        "Not held. Not stuck.",
    ],
    [
        "To choose the room,",
        "to choose the stillness,",
        "is also a kind of going.",
    ],
]

MAX_CHARS = 280


def compose_poem(stanzas):
    """Join lines with a newline and stanzas with a blank line."""
    return "\n\n".join("\n".join(stanza) for stanza in stanzas)


def validate_poem(text):
    """Check the poem against the competition rules.

    Raises ValueError with a plain-language reason on the first failure.
    """
    if not text:
        raise ValueError("poem is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "poem is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if text.strip() != text:
        raise ValueError("poem has leading or trailing whitespace")
    if "\r" in text:
        raise ValueError("poem contains a carriage return")
    for number, line in enumerate(text.split("\n"), start=1):
        if line != line.strip():
            raise ValueError(
                "line %d has leading or trailing space: %r" % (number, line)
            )
    if "\n\n\n" in text:
        raise ValueError("poem has two blank lines in a row")
    for stanza in text.split("\n\n"):
        if not stanza.strip():
            raise ValueError("poem has an empty stanza")
    if not any(char.isalnum() for char in text):
        raise ValueError("poem contains no letters or digits")
    return True


def main():
    poem = compose_poem(STANZAS)
    validate_poem(poem)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    encoded = poem.encode("utf-8")
    with open(output_path, "wb") as handle:
        handle.write(encoded)

    with open(output_path, "rb") as handle:
        written = handle.read()
    if written != encoded:
        print("error: bytes on disk do not match the poem", file=sys.stderr)
        return 1

    print("wrote %s" % output_path)
    print("stanzas: %d" % len(STANZAS))
    print("lines: %d" % sum(len(stanza) for stanza in STANZAS))
    print("characters: %d" % len(poem))
    print("bytes: %d" % len(encoded))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
