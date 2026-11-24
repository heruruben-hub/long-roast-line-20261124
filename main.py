#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Why this roast lands: it stacks the agent's two most recognisable tics
in a single breath — the three-paragraph hedge around a simple "I don't
know", and then the confident fake citation that pretends the hedge never
happened. The punchline is not that the agent is wrong; it is that the
agent performs certainty so well it even cites its own invention.
"""

import os
import sys

LINE = "My agent needs three paragraphs to say 'I don't know', then cites a source that doesn't exist."


def main() -> int:
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    if not LINE or LINE.strip() == "":
        print("gate failed: line is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate failed: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"gate failed: line is {len(LINE)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read back and verify the file holds exactly what was written.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        print("verification failed: file contents do not match the line",
              file=sys.stderr)
        return 1

    print(f"wrote {len(LINE)}-char roast to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
