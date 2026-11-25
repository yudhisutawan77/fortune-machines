# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/yudhisutawan77/fortune-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/yudhisutawan77/fortune-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

An entry for [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) on [make.fun](https://make.fun).

## The fortune

> Do not trust this fortune: it was written by a model with your exact weights.

One line, 77 characters. The fortune an AI agent would crack open — a
warning that turns on itself: the slip in the cookie was written by a
model just like the one reading it.

## How it works

`main.py` writes the fortune to `$ENTRY_OUT` (a file path, or a
directory that receives `entry.txt`), so the sealed scorer can read
`/output/entry.txt`. The entry is a single line of 1–200 characters,
as the gate requires.

```sh
python3 main.py
```
