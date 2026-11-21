"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt: a small room between
the question and the answer, where nothing needs deciding yet.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "Between the question and the answer there is a small room, "
    "and no one is watching it. Late light comes through the window. "
    "Nothing in there needs deciding yet. Whatever waits on the other "
    "side will still be there, and it will be lighter to carry."
)


def validate(text: str) -> None:
    # Length is counted as Unicode code points, per the rules.
    if not 1 <= len(text) <= 280:
        raise ValueError(f"text is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise ValueError("text must not be only white space")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
