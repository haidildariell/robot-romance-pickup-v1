#!/usr/bin/env python3
"""Robot Romance entry: one single-line pickup line for an AI.

Writes exactly one pickup line to <OUTPUT_DIR>/entry.txt.
The line is a joke aimed at a robot/AI: a pop-up ad frame with a
second beat (a vow never to click, surrendered) closing on a
concrete visible image (both hands on the mouse).
"""

import os

LINE = "Are you a pop-up ad? I swore I'd never click one, and here I am, both hands on the mouse."

# The competition gate accepts 1-200 characters of UTF-8 text.
MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly instead of emitting an entry the gate would refuse."""
    if not line.strip():
        raise ValueError("pickup line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"pickup line is {len(line)} characters, over the {MAX_CHARS} cap"
        )


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
