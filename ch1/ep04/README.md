# Episode 4 — Errors and AI: read the red text, then check the AI

Python for Defenders · Chapter 1: Foundations (Novice)

Video: coming soon

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py`
- macOS / Linux: `python3 watchdog.py`

Expected output:

```
Watchdog starting
Lines in log: 1528
Failed logins: 369
Successful logins: 27
```

## Files

- `watchdog.py`
- `ask_ai.py`
- `error.txt`
- `typo.py`
- `indent.py`
- `challenge_ep03.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Print the IP address that line 186 came from. Hint: line.split(). Answer in episode 5.
