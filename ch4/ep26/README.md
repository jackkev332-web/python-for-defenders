# Episode 26 — Attacker-controlled input: don't let a log line frame an innocent IP

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: coming soon

## Also try

- `python -m pytest -q` — the tests now include hostile lines (a framed username, and one that must be skipped)
- `python watchdog.py practice_auth.log` — on the honest log the report is the same as episode 25's
- `python make_framed_log.py` rebuilds `framed_auth.log` (the practice day + one attacker); every line in it is synthetic

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py framed_auth.log`
- macOS / Linux: `python3 watchdog.py framed_auth.log`

Expected output:

```
IP ADDRESS       FAILS  FIRST     LAST      WEB 404s
203.0.113.45       212  03:17:57  04:31:18         -
198.51.100.77       96  04:34:36  05:09:39         -
203.0.113.9         41  14:31:52  14:46:28         -
198.51.100.140      17  00:49:27  00:54:10         -
198.51.100.66        6  09:14:05  09:14:51         -

5 suspicious IPs (threshold 5)
```

## Files

- `watchdog.py`
- `rules.toml`
- `test_watchdog.py`
- `make_framed_log.py`
- `framed_auth.log`
- `practice_auth.log`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

The web rule '.* 404 ' can also match text in the user agent, which the client writes. Make it match only the status code. Share yours in the comments.
