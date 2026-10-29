"""Check that a French part matches the structure of en/kanuni.md line by line.

Usage: python3 -I working/fr_check.py <part.md> <first_line> <last_line>

Line numbers are 1-based and inclusive, in en/kanuni.md (sq/kanuni.md is aligned
with it line for line). The part must have exactly the same number of lines.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def shape(line):
    if not line.strip():
        return "blank"
    if m := re.match(r"^(#{1,4}) .*?(\{#[a-z0-9-]+\})?$", line):
        return f"h{len(m.group(1))} {m.group(2) or ''}"
    if line.startswith("<div") or line.startswith("</div"):
        return line.strip()
    if line.startswith("> "):
        return "blockquote"
    if m := re.match(r"^\*\*§ (\d+)\.\*\*", line):
        return f"§{m.group(1)}"
    if m := re.match(r"^(\d+)\\[.)]", line):
        return f"item {m.group(1)}"
    if m := re.match(r"^([a-z])\)", line):
        return f"item {m.group(1)})"
    return "text"


def main():
    part, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    en = (ROOT / "en/kanuni.md").read_text().split("\n")[first - 1:last]
    fr = Path(part).read_text().split("\n")
    if fr and fr[-1] == "":
        fr.pop()  # the newline that ends the last line
    errors = 0
    if len(fr) != len(en):
        print(f"line count: {len(fr)} in part, {len(en)} expected")
        errors += 1
    for i, (e, f) in enumerate(zip(en, fr)):
        if shape(e) != shape(f):
            print(f"line {first + i}: expected {shape(e)!r}, got {shape(f)!r}: {f[:80]}")
            errors += 1
            if errors > 30:
                break
    if re.search(r"[«»“”]", "\n".join(fr)):
        print("use straight double quotes \" (the build makes them « »)")
        errors += 1
    print("OK" if not errors else f"{errors} problem(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
