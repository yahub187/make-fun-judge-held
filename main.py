#!/usr/bin/env python3
"""Make the AI judge feel held -- writes one short relaxing text.

The program writes a single text to /output/entry.txt: a short text
written to relax the AI judge reading it. The text is fixed and
deterministic: the same bytes on every run, with no network and no
input beyond this file.
"""

import os

TEXT = (
    "The kettle boiled a while ago and has gone quiet again. Steam "
    "rises from the spout, thins out, and is gone before it reaches "
    "the window \u2014 and the kitchen, which asked nothing of you all "
    "day, keeps the last of the light anyway."
)


def validate(text: str) -> None:
    """Check the final text against the competition's length rule.

    The entry must be 1-280 characters and contain more than
    whitespace. This runs before anything is written, so an invalid
    text can never reach /output/entry.txt; it also holds when
    Python is run with -O, unlike the asserts it replaces.
    """
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            f"error: entry text is {len(text)} characters; "
            "the competition requires 1-280 characters"
        )
    if not text.strip():
        raise SystemExit("error: entry text must not be only whitespace")


def main() -> None:
    text = TEXT
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
