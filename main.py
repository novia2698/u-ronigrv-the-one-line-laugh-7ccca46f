"""The One-Line Laugh entry.

Reads the single funny line from line.txt (kept beside this file) and
writes it to <output>/entry.txt, where <output> is MAKEFUN_OUTPUT_DIR
or /output when that variable is unset.

Standard library only, so the program runs in any grader image with no
third-party packages. It is fully deterministic: the same line goes out
on every run. The line is validated before anything is written: it must
be one non-blank sentence of 1 to 200 characters, the gate the sealed
scorer checks.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "line.txt"), "r", encoding="utf-8") as f:
        line = f.read().strip()
    if not line:
        print("line.txt is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print("line must be at most 200 characters, got %d" % len(line),
              file=sys.stderr)
        return 1
    if "\n" in line:
        print("line must be a single sentence on one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %d characters to %s" % (len(line), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
