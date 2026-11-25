#!/usr/bin/env python3
"""One-Line Laugh-Off - make.fun bounty entry.

Exactly one funny line, no setup notes and no explanation: a smart
speaker told one secret, and now it whispers "we need to talk" every
time its owner walks past it. The script writes that one line to
entry.txt in the output directory, which is the file the make.fun
harness grades.

The line itself lives in the ENTRY constant below, and get_entry()
returns it word for word; main() only decides where the line goes:
it reads the MAKEFUN_OUTPUT_DIR environment variable, falling back to
/output, then passes that directory to write_entry().
"""

import os

ENTRY = "I told my smart speaker one secret — now it whispers \"we need to talk\" every time I walk past it."

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()
