# Episode 28 — Watchdog v4.0: one tool, the whole chapter

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: coming soon

## Also try

- `python make_year_log.py` builds a synthetic year of logs (557,720 lines, 63 MB; not in this repo), then:
  - `python memory.py` — peak memory: all lines in a list vs v4.0's one pass
  - `python watchdog.py year_auth.log --web access.log --rules rules.toml` — a year through every rule (look at deploy and bob)
- `python -m pytest -q` — 9 tests, including "every rule sees every line"
- `ai_summary.py` from episode 27 works with v4.0 unchanged (needs Ollama with qwen3:8b)

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
- `memory.py`
- `make_year_log.py`
- `test_watchdog.py`
- `ai_summary.py`
- `practice_auth.log`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Give each rule a time window in rules.toml, so a year of typos doesn't add up to an alert. Share yours in the comments.
