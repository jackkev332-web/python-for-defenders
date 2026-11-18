# Episode 29 — Tool calling: let the AI ask your code

Python for Defenders · Chapter 5: AI for defenders (Expert)

Video: https://youtu.be/35qNkVisLCY

## Before you start

- Install [Ollama](https://ollama.com), then download the model once: `ollama pull qwen3:8b` (about 5 GB). It runs on your own computer, free.
- Start Ollama (the tray app, or `ollama serve`). The first answer can take a minute: the script asks for CPU-only, a fresh load, temperature 0 and a fixed seed, so the answer repeats.

## Also try

- Open `conversation.json` after a run: the whole round trip, exactly as it was sent
- `python -m pytest -q` — the tests check the tool itself (no AI needed)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python agent.py`
- macOS / Linux: `python3 agent.py`

Expected output:

```
You: Which IP addresses attacked my server today, and how many failed logins did each one have?
AI asks to run: watchdog_report({})
Our code runs it and sends back 7 lines.
AI:
The following IP addresses attacked your server today, along with the
number of failed logins each had:

- **203.0.113.45**: 212 failed logins
- **198.51.100.77**: 96 failed logins
- **203.0.113.9**: 41 failed logins
- **198.51.100.140**: 17 failed logins

Note: The threshold for suspicious activity is set at 5 failed logins.
The IPs listed above exceed this threshold.
```

## Files

- `agent.py`
- `watchdog.py`
- `test_agent.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add a second tool, ip_details(ip), that returns one address's failed logins. Share yours in the comments.
