# Episode 30 — An agent loop: many tools, one step limit

Python for Defenders · Chapter 5: AI for defenders (Expert)

Video: https://youtu.be/TQlc4yuOa2Y

## Before you start

- Install [Ollama](https://ollama.com), then download the model once: `ollama pull qwen3:8b` (about 5 GB). It runs on your own computer, free.
- Start Ollama (the tray app, or `ollama serve`). Each step can take a while: the script asks for CPU-only, a fresh load, temperature 0 and a fixed seed, so the answers repeat.

## Also try

- `python agent.py "Look at the latest failed logins, then tell me which attacker I should deal with first."` — the check rejects its first answer and sends it back
- `python agent.py "Give me the details for every attacking IP address in today's report." --max-steps 3` — the step limit stops it
- Open `conversation.json` after a run: every step, exactly as it was sent
- `python -m pytest -q` — the tests check the tools and the check (no AI needed)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python agent.py "Which IP address is the worst attacker today, and what did it try?"`
- macOS / Linux: `python3 agent.py "Which IP address is the worst attacker today, and what did it try?"`

Expected output:

```
You: Which IP address is the worst attacker today, and what did it try?
step 1: watchdog_report({})
step 2: ip_details({'ip': '203.0.113.45'})
step 3: the AI answers
AI:
The worst attacker today is the IP address **203.0.113.45**, which
attempted **212 failed logins**. The most common usernames it tried
were:

- **admin** (42 times)
- **user** (29 times)
- **git** (27 times)

This IP address is highly suspicious and should be investigated further.
```

## Files

- `agent.py`
- `watchdog.py`
- `test_agent.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

What happens if the AI sends an argument name ip_details doesn't have? Make the loop send the error back. Share yours in the comments.
