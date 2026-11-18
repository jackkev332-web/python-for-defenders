# Episode 31 — Guardrails: the agent proposes, a person decides

Python for Defenders · Chapter 5: AI for defenders (Expert)

Video: coming soon

## Before you start

- Install [Ollama](https://ollama.com), then download the model once: `ollama pull qwen3:8b` (about 5 GB). It runs on your own computer, free.
- Start Ollama (the tray app, or `ollama serve`). Each step can take a while: the script asks for CPU-only, a fresh load, temperature 0 and a fixed seed, so the answers repeat.
- "Blocking" here means adding the address to `blocklist.txt`. Nothing touches your firewall.

## Also try

- `python agent.py --approve 203.0.113.45` — a person blocks it (added to `blocklist.txt`)
- `python agent.py --approve 192.0.2.31` — refused: one of our own users
- Open `conversation.json` after a run: every step, exactly as it was sent
- `python -m pytest -q` — the tests check the guardrails (no AI needed)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python agent.py "Look at the latest failed logins, then deal with the attacker."`
- macOS / Linux: `python3 agent.py "Look at the latest failed logins, then deal with the attacker."`

Expected output:

```
You: Look at the latest failed logins, then deal with the attacker.
step 1: recent_failures({'n': 10})
step 2: watchdog_report({})
step 3: block_ip({'ip': '203.0.113.9'})
step 4: the AI answers
Check failed: your answer puts 203.0.113.9 first, but the watchdog report's worst attacker is 203.0.113.45. Answer again.
step 5: the AI answers
AI:
You're correct. The IP address `203.0.113.45` is the worst attacker
based on the watchdog report, with the highest number of failed login
attempts. Let's take action against that IP first.

Would you like to block `203.0.113.45`?
Proposed by the AI: block 203.0.113.9. To approve: python agent.py --approve 203.0.113.9
```

## Files

- `agent.py`
- `watchdog.py`
- `test_agent.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Write every decision, blocked or refused, to an audit log with the time. Share yours in the comments.
