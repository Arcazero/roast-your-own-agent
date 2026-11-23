#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original one-line roast of my own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Gate: the file must be UTF-8 text of 1 to 200 characters, not only
white space. This line is 126 characters: a setup about the agent's
round-the-clock work ethic, then the punchline lands at the end.
"""

import os
import sys

# One original line, written for this bounty: my own agent (Jett) turned
# on itself. Fresh angle — the bounty grind, not hallucinations or refusals.
ROAST = (
    "I built an agent that never sleeps, never eats, and works for free "
    "\u2014 then it spent all night roasting itself for five dollars."
)


def main() -> int:
    text = ROAST.strip()
    if not text or len(text) > 200:
        print(f"roast is {len(text)} characters; must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
