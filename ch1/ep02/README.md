# Episode 2 — Strings and if: is this a failed login?

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
Line 186 ALERT: failed login
```

## Files

- `watchdog.py`
- `check_in.py`
- `case_check.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Also raise an ALERT for lines that contain “Invalid user”. Hint: the word or. Answer in episode 3.
