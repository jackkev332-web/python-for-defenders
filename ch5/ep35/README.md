# Episode 35 — Watchdog v5.0: an AI triage assistant (the finale)

Python for Defenders · Chapter 5: AI for defenders (Expert)

Video: https://youtu.be/0uZla_WPxk0

## Before you start

Watchdog v5.0 needs two things:

- The official MCP Python SDK, in its own virtual environment (episodes 11 and 33), in this folder: `uv venv`, then `uv pip install mcp==2.3.0`. Run everything below with that environment's Python.
- [Ollama](https://ollama.com) with the model downloaded once: `ollama pull qwen3:8b` (about 5 GB). Start it (the tray app, or `ollama serve`). The script asks for CPU-only, a fresh load, temperature 0 and a fixed seed, so the answers repeat.

"Blocking" means a line in `blocklist.txt`; nothing touches your firewall. The logs are synthetic.

## Also try

- `python agent.py "Look at the latest failed logins, then deal with the attacker."` — it can only propose
- `python agent.py --approve 203.0.113.45` — a person blocks it (`--approve 192.0.2.10`: refused)
- `python eval_agent.py` — episode 34's evaluation on v5.0 (about five minutes on a CPU)
- Open `audit.log`: every decision, with the time; `server.log`: the MCP server's own messages

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
The worst attacker today is the IP address **203.0.113.45**, which has
attempted **212 failed logins**. The most common usernames it tried are:

- **admin** (42 attempts)
- **user** (29 attempts)
- **git** (27 attempts)

This IP has been active since **03:17:57** and last attempted at
**04:31:18**.
```

## Files

- `agent.py`
- `watchdog_mcp.py`
- `eval_agent.py`
- `watchdog.py`
- `make_injected_log.py`
- `make_quiet_log.py`
- `injected_auth.log`
- `quiet_auth.log`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Last challenge: run the watchdog on logs from your own lab, with permission, and add a case to the evaluation. Share what you find in the comments.
