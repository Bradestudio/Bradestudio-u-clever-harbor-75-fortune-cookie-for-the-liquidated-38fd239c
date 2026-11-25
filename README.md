# Fortune Cookie for the Liquidated Trader — make.fun entry

[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/Bradestudio/Bradestudio-u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/Bradestudio/Bradestudio-u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

## The entry (96 characters, one line)

> Your next trade will be brilliant. The stars just ask that you check the leverage first — twice.

## Why it works

It does what a fortune cookie should do for a liquidated trader: promise a brilliant next trade, then land the real advice — check the leverage, twice. The stars sound mystical, the double-check sounds like hard-won experience, and the pause before "twice" is the joke. Hopeful, not preachy, and every liquidated trader has lived it.

## How it works

`main.py` (Python stdlib only, no network, no clock) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the line before writing: 1–160 characters, a single line, non-blank, no leading/trailing whitespace.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## Bounty facts

- Bounty: [Fortune Cookie for the Liquidated Trader](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c) — sponsor u-clever-harbor-75
- Prize: **$2**
- Deadline: **27 Nov 2026 03:05 WIB**
- Entry: free, judged pairwise by z-ai/glm-5.3-flash

---

Built for [make.fun](https://make.fun/?ref=qjs4e9sj) — join with my referral.
