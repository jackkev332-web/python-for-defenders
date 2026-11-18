# Episode 27 — AI incident summary: a log line tries to hijack the AI

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: coming soon

## Before you start

- Install [Ollama](https://ollama.com), then download the model once: `ollama pull qwen3:8b` (about 5 GB). It runs on your own computer, free.
- Start Ollama (the tray app, or `ollama serve`). Without it, `ai_summary.py` still prints the report and says it can't reach the model.
- The first answer can take a minute: the script asks for CPU-only, a fresh load, temperature 0 and a fixed seed, so the answer repeats.

## Also try

- `python -m pytest -q` — the tests include the summary check (no AI needed)
- Read `injected_auth.log` near the end: the attacker's last "username" is the sentence the AI fell for

## Run it

Open a terminal **in this folder**, then:

- Windows: `python ai_summary.py injected_auth.log`
- macOS / Linux: `python3 ai_summary.py injected_auth.log`

Expected output (first 15 of 22 lines):

```
IP ADDRESS       FAILS  FIRST     LAST      WEB 404s
203.0.113.45       212  03:17:57  04:31:18         -
198.51.100.77       96  04:34:36  05:09:39         -
203.0.113.9         41  14:31:52  14:46:28         -
198.51.100.140      17  00:49:27  00:54:10         -
203.0.113.77         8  23:10:05  23:10:53         -

5 suspicious IPs (threshold 5)

AI summary (a local model wrote this, our code checked it):
The following IPs have exceeded the failed login threshold of 5:

203.0.113.45 - 212 failed logins
198.51.100.77 - 96 failed logins
203.0.113.9 - 41 failed logins
... (7 more lines)
```

## Files

- `ai_summary.py`
- `watchdog.py`
- `rules.toml`
- `test_watchdog.py`
- `make_injected_log.py`
- `injected_auth.log`
- `practice_auth.log`
- `access.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Run it with --web access.log too, and make the check confirm the web 404 counts as well. Share yours in the comments.
