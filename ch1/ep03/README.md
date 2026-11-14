# Episode 3 — Loops: check all 1,528 lines

Python for Defenders · Chapter 1: Foundations (Novice)

Video: https://youtu.be/z_LfXlipr4w

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py`
- macOS / Linux: `python3 watchdog.py`

Expected output:

```
Watchdog starting
Lines in log: 1528
Failed logins: 369
```

## Files

- `watchdog.py`
- `loop_gotcha.py`
- `challenge_ep02.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Also count the successful logins. They contain the word “Accepted”. Answer in episode 4.
