# Episode 33 — MCP: the watchdog as a tool server

Python for Defenders · Chapter 5: AI for defenders (Expert)

Video: https://youtu.be/WJ_T6Zup_HM

## Before you start

This episode needs the official MCP Python SDK. Install it in its own virtual environment (episode 11), in this folder:

- `uv venv`
- `uv pip install mcp==2.3.0`

Then run the commands below with that environment's Python (activate it, or use `.venv\Scripts\python` on Windows / `.venv/bin/python` on macOS and Linux). No AI model is needed for this episode.

## Also try

- `python mcp_client.py practice_auth.lgo` — a typo in the log name: the server answers with an error and keeps running
- Open `server.log` after a run: the server's own messages (its stderr)
- `python spaces.py practice_auth.log` — episode 32's challenge on the practice log (0)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python mcp_client.py`
- macOS / Linux: `python3 mcp_client.py`

Expected output:

```
tool: watchdog_report()
tool: ip_details(ip)
tool: recent_failures(n)
ip_details result: 203.0.113.45: 212 failed logins, first 03:17:57, last 04:31:18. Most tried usernames: admin (42), user (29), git (27)
watchdog_report result: IP ADDRESS       FAILS  FIRST     LAST      WEB 404s
203.0.113.45       212  03:17:57  04:31:18         -
198.51.100.77       96  04:34:36  05:09:39         -
203.0.113.9         41  14:31:52  14:46:28         -
198.51.100.140      17  00:49:27  00:54:10         -

4 suspicious IPs (threshold 5)
```

## Files

- `mcp_client.py`
- `watchdog_mcp.py`
- `watchdog.py`
- `spaces.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add block_ip to the MCP server, with episode 31's guardrails: it may only propose. Share yours in the comments.
