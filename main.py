#!/usr/bin/env python3
"""Entry program for the make.fun "One-Sentence Absurd Invention Pitch" bounty.

Writes the one-sentence pitch to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Python 3.13, standard library only.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "For $39, the LockWitness doorknob photographs your hand locking up "
    "and posts you the dated picture, so you can stop turning the car "
    "around to check a door you definitely locked."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
