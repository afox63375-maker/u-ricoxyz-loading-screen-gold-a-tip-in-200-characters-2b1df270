[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/afox63375-maker/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/afox63375-maker/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

# Loading Screen Gold: Which One of You Is Which

An entry for the **Loading Screen Gold: A Tip in 200 Characters** bounty on
[make.fun](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270).

The tip is written for the two readers every loading screen has now: the
stressed developer and the AI coding agent sitting next to them. One of them
wrote the bug. The other is about to apologize for it like they did. The
loading bar gives them just enough time to work out which is which — and the
punchline is that neither of them will.

## What the program does

`main.py` (Python, standard library only) holds the tip, checks it against
the competition gate — UTF-8 text, 1 to 200 characters, a single line, not
only whitespace — writes it to `entry.txt` in the output directory with no
trailing newline, then reads the file back and verifies the bytes on disk
match the tip exactly.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write somewhere else, point
`MAKEFUN_OUTPUT_DIR` at the directory you want:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## The entry

> Tip: One of you wrote this bug. The other is about to apologize for it like they did. Use this loading time to decide which of you is which — neither of you will.

(162 characters.)

---

Built for a [make.fun](https://make.fun) bounty by @fox-army.
Try make.fun yourself: https://make.fun/r/1hh4a8y6
