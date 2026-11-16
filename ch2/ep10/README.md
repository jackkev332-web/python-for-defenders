# Episode 10 — Regex: match a log line by its shape

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

IP ADDRESS       FAILS  USERNAMES TRIED
203.0.113.45       212  admin, git, oracle, postgres, root, test, ubuntu, user
198.51.100.77       96  admin, guest, pi, root, support
203.0.113.9         41  root
198.51.100.140      17  ftpuser, nagios, test
192.0.2.31           2  deploy
192.0.2.24           1  bob
```

## Files

- `watchdog.py`
- `check_pattern.py`
- `check_naive.py`
- `challenge_ep09.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Write a regex for the Accepted lines that also captures the login method. Answer in episode 11.
