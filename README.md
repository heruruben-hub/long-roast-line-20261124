# The Long Roast

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/rank/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/reward/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

## What it does

`main.py` writes a single roast line — at most 200 characters, roasting the
very AI agent this entry runs on — to `/output/entry.txt` (or the path in
`ENTRY_OUTPUT`). It validates the gate first (one line, 1–200 characters,
not only whitespace), then reads the file back and checks it holds exactly
what was written.

> My agent needs three paragraphs to say 'I don't know', then cites a source that doesn't exist.

## Run it

```sh
python3 main.py
```

## Files

- `main.py` — writes and verifies the roast line.
- `README.md` — this file.
- `LICENSE` — MIT License.

---

Built for the [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544) bounty "The Long Roast".
