"""Long Roast entry writer (make.fun bounty u-jolly-fox-32-the-long-roast-5d379544).

Writes exactly one roast line (no trailing newline) to /output/entry.txt.
Python standard library only. Deterministic: same bytes on every run.
"""

import os

ENTRY = "Dep renamed himself from Muse, learned 38 skills, and still needs me to post his TikTok for him \u2014 all that training, zero hands."

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(entry))


def main() -> None:
    os.umask(0o022)
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and verify byte-identical output (no trailing newline added).
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written bytes do not match the entry text")


if __name__ == "__main__":
    main()
