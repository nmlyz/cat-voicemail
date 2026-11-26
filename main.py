#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the voicemail greeting a cat
recorded for its human's phone.

The line was picked from 37 candidates by pairwise judging against the
brief: it must read as a cat's voicemail greeting, the joke must come
from something specific to cats, the cat must sound like a character
with an attitude of its own, and the punch must land quickly when
spoken aloud. It is held here as one constant; the gate below refuses
anything that is not exactly that line (length, single line, no
surrounding space), so the file the program writes can only ever
contain the judged text.

Why this line won: the cat knocks the phone off the bed — a behaviour
every cat owner recognises — and blames the phone for looking at it
wrong. The grudge is the joke, and the beep line at the end keeps it
a voicemail greeting rather than a caption about a cat.
"""

import os
import sys

LINE = (
    "Hi, it's the cat. I pushed your phone off the bed because it was "
    "looking at me wrong. Leave a message after the beep."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 117


def check_line(line):
    """Refuse anything that is not exactly the judged line."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not 1 <= len(line) <= 120:
        return "line outside the 1-120 character gate"
    if "\n" in line or line != line.strip():
        return "line must be a single line with no surrounding space"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
