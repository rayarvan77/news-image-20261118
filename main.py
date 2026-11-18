"""Entry program for the news-image-20261118 bounty.

The image this repository holds is the entry: a front page summing up
Wednesday 18 November 2026 in six panels. This program copies it to the
output directory the grader provides, so the judge sees exactly the
bytes in entry.png.

Standard library only; no network, no arguments. Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    """Copy entry.png into the output directory, checking the copy."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    source = HERE / "entry.png"
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError("entry.png did not copy completely")


if __name__ == "__main__":
    main()
