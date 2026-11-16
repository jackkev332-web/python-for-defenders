# Episode 14 — argparse: Watchdog v2.0, a real command-line tool

Python for Defenders · Chapter 2: Real tools (Beginner)

Video: coming soon

## Options (this episode)

- `python watchdog.py --help` — the help page argparse writes for you
- `python watchdog.py practice_auth.log --threshold 50` (or `-t 50`) — only IPs with at least 50 failures
- `python -m pytest` — episode 13's tests still pass

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py practice_auth.log`
- macOS / Linux: `python3 watchdog.py practice_auth.log`

Expected output:

```
IP ADDRESS       FAILS  USERNAMES TRIED
203.0.113.45       212  admin, git, oracle, postgres, [...]
198.51.100.77       96  admin, guest, pi, root, support
203.0.113.9         41  root
198.51.100.140      17  ftpuser, nagios, test

4 suspicious IPs (threshold 5)
```

## Files

- `watchdog.py`
- `test_watchdog.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add a --top option that shows only the first N addresses. Share yours in the comments.
