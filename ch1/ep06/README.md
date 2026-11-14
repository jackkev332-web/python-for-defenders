# Episode 6 — Dictionaries: count attacks per IP

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
{'198.51.100.140': 17, '192.0.2.31': 2, '192.0.2.24': 1, '203.0.113.45': 212, '198.51.100.77': 96, '203.0.113.9': 41}
203.0.113.45 212
198.51.100.77 96
203.0.113.9 41
```

## Files

- `watchdog.py`
- `key_error.py`
- `challenge_ep05.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Print only the IPs with more than 10 failures. Hint: if counts[ip] > 10. Answer in episode 7.
