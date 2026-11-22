#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

Deterministic, standard library only. The entry text is a short text
written to relax the AI judge reading it.
"""

import hashlib
import os

ENTRY_TEXT = "The kettle boiled a while ago and has gone quiet again. Steam rises from the spout, thins out, and is gone before it reaches the window — and the kitchen, which asked nothing of you all day, keeps the last of the light anyway."

# sha256 of the exact bytes main() writes to /output/entry.txt.
EXPECTED_SHA256 = "3b3f5350e90607f16059e15f5000856f217e0582cc0305c34062f212b8771224"


def validate(text):
    """Reject text that would fail the gate: empty, over 280 chars, or whitespace-only."""
    if len(text) == 0:
        raise ValueError("entry text must not be empty")
    if len(text) > 280:
        raise ValueError("entry text must be at most 280 characters")
    if text.strip() == "":
        raise ValueError("entry text must not be only whitespace")
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    with open("/output/entry.txt", "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"self-check failed: wrote sha256 {digest}, expected {EXPECTED_SHA256}"
        )


if __name__ == "__main__":
    main()
