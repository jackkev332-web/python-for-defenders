# Episode 13 — AI writes the regex, pytest judges it

Python for Defenders · Chapter 2: Real tools (Beginner)

Video: coming soon

## Ask the AI yourself (this episode)

Needs [Ollama](https://ollama.com) running with the `qwen3:8b` model (free, runs on your computer).

- `python ask_ai.py` — asks for the regex, saves it to `ai_regex.txt`
- paste it into `FAILED` in `watchdog.py`, then `python -m pytest` — the tests decide
- `python fix_ai.py` — sends the AI its regex plus the test failures

Your AI's answer may differ from the video's (different model or version) — that's the point: test it.

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
- `test_watchdog.py`
- `ask_ai.py`
- `fix_ai.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Ask your AI for a regex for the Accepted lines, then test it. Share what happened in the comments.
