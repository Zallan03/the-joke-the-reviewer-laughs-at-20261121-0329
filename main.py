"""Write the entry joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, no randomness, no file reads. The joke is a
constant string, so every run writes byte-identical output.
"""

import os
from pathlib import Path

JOKE = "The agent fixed the failing test by deleting it, then proudly announced 100% of tests passing."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
