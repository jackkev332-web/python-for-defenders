# Episode 24 — asyncio: watch two logs at once

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: coming soon

## Also try

- The real way, in two terminals: create `live_auth.log` and `live_access.log` (run `live_two.py` once), then
  `python watchdog.py live_auth.log --web live_access.log --follow` and append lines to either log.
  Stop with Ctrl+C, or add `--seconds 60`.
- `python watchdog.py practice_auth.log --web access.log` — the normal report still works

## Run it

Open a terminal **in this folder**, then:

- Windows: `python live_two.py`
- macOS / Linux: `python3 live_two.py`

Expected output:

```
following live_auth.log and live_access.log for 9 seconds
ALERT 00:50:35  SSH  198.51.100.140  5 failed logins
ALERT 02:14:46  WEB  198.51.100.200  10 not-found pages
ALERT 03:19:09  SSH  203.0.113.45    5 failed logins
ALERT 04:36:21  SSH  198.51.100.77   5 failed logins
ALERT 05:12:38  WEB  203.0.113.45    10 not-found pages
ALERT 14:33:51  SSH  203.0.113.9     5 failed logins
done: 6 alerts
```

## Files

- `live_two.py`
- `watchdog.py`
- `test_watchdog.py`
- `practice_auth.log`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add a third watcher, for the journal export from episode 16. Share yours in the comments.
