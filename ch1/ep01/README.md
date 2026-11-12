# Episode 1 — Your first Python script: read a server log

Python for Defenders · Chapter 1: Foundations (Novice)

Video: https://youtu.be/7XWZmS8Xaio

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py`
- macOS / Linux: `python3 watchdog.py`

Expected output:

```
Watchdog starting
Lines in log: 1528
```

## Files

- `watchdog.py`
- `practice_auth.log`
- `make_practice_log.py`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Print the very first line of the log. Hint: lines[0]. Answer in episode 2.
