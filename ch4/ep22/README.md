# Episode 22 — Generators: a year of logs, almost no memory

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: https://youtu.be/6c8KSDC0AT4

## First: make a year of logs

- `python make_year_log.py` writes `year_auth.log`: the synthetic practice day for every day of 2026
  (557,720 lines, 63.4 MB — not stored in this repository).

## Also try

- `python once.py` — 369 failed, 27 accepted (it makes a list once; try removing `list(...)`)
- `python -m pytest` — episode 13's tests, fixed to make a list once
- `python watchdog.py practice_auth.log` — Watchdog v3.1: `read_log` now streams

Your memory numbers will differ a little from the ones below (machine and Python version).

## Run it

Open a terminal **in this folder**, then:

- Windows: `python memory.py`
- macOS / Linux: `python3 memory.py`

Expected output:

```
load_all   153.87 MB  134,685 failures
stream       0.03 MB  134,685 failures
```

## Files

- `memory.py`
- `once.py`
- `watchdog.py`
- `test_watchdog.py`
- `make_year_log.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Count the failures per month, with a chain of generators. Share yours in the comments.
