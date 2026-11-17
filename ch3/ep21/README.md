# Episode 21 — Watchdog v3.0: one tool, two logs (chapter 3 finale)

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: https://youtu.be/DAo4qocinoc

## Also try

- `python watchdog.py practice_journal.json --json --web access.log` — the same table from the journal export
- `python watchdog.py practice_auth.log` — without `--web`, the WEB 404s column shows `-` (not checked)
- `python -m pytest` — episode 13's tests still pass

All three logs are **synthetic** (one made-up day; RFC 5737 documentation IPs).

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py practice_auth.log --web access.log`
- macOS / Linux: `python3 watchdog.py practice_auth.log --web access.log`

Expected output:

```
IP ADDRESS       FAILS  FIRST     LAST      WEB 404s
203.0.113.45       212  03:17:57  04:31:18        21
198.51.100.77       96  04:34:36  05:09:39         0
203.0.113.9         41  14:31:52  14:46:28         0
198.51.100.140      17  00:49:27  00:54:10         0

4 suspicious IPs (threshold 5)
```

## Files

- `watchdog.py`
- `test_watchdog.py`
- `practice_auth.log`
- `practice_journal.json`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add a WEB FIRST column: when did each IP first hit the website? Share yours in the comments.
