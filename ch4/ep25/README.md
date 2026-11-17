# Episode 25 — Rules as data: change the rules, not the code

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: coming soon

## Also try

- Add your own `[[rule]]` to `rules.toml` (keep regexes in 'single quotes') and run again — no code change
- `python watchdog.py practice_auth.log --web access.log` — the normal report still works
- Needs Python 3.11 or newer (`tomllib` is in the standard library from 3.11)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py practice_auth.log --web access.log --rules rules.toml`
- macOS / Linux: `python3 watchdog.py practice_auth.log --web access.log --rules rules.toml`

Expected output:

```
RULE                    IP ADDRESS        HITS
ssh-password-guessing   203.0.113.45       212
ssh-password-guessing   198.51.100.77       96
ssh-password-guessing   203.0.113.9         41
ssh-password-guessing   198.51.100.140      17
web-scanner             198.51.100.200      30
web-scanner             203.0.113.45        21
ssh-root-guessing       203.0.113.9         41
ssh-root-guessing       203.0.113.45        23

8 hits from 3 rules
```

## Files

- `watchdog.py`
- `rules.toml`
- `test_watchdog.py`
- `practice_auth.log`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Give each rule a severity (low, high) in the TOML file, and print it in the report. Share yours in the comments.
