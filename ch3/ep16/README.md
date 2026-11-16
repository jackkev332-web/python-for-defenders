# Episode 16 — JSON logs: read the systemd journal

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: coming soon

## Also in this folder

- `python watchdog.py practice_auth.log` — the same table from the text log
- `python first_entry.py` — prints the first journal entry, field by field
- `practice_journal.json` — a **synthetic** `journalctl -o json` export of the practice log (5 fields per entry; a real export has more)
- `python -m pytest` — episode 13's tests still pass
- For the challenge: `timeline.py` is in [ch3/ep15](../ep15)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py practice_journal.json --json`
- macOS / Linux: `python3 watchdog.py practice_journal.json --json`

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
- `first_entry.py`
- `test_watchdog.py`
- `practice_journal.json`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Make timeline.py read the journal too. __REALTIME_TIMESTAMP is microseconds since 1970, UTC. Share yours in the comments.
