# Episode 8 — Counter: count anything in one line

Python for Defenders · Chapter 2: Real tools (Beginner)

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
Top attackers: [('203.0.113.45', 212), ('198.51.100.77', 96), ('203.0.113.9', 41)]
Top usernames: [('root', 81), ('admin', 67), ('user', 29)]
```

## Files

- `watchdog.py`
- `counter_trap.py`
- `challenge_ep07.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Count the successful logins per user with Counter. Answer in episode 9.
