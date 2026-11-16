# Episode 11 — Virtual environments: install tools safely

Python for Defenders · Chapter 2: Real tools (Beginner)

Video: coming soon

## Set up a virtual environment (this episode)

In this folder:

- Create it: `python -m venv .venv` (macOS / Linux: `python3 -m venv .venv`)
- Activate it — Windows: `.venv\Scripts\activate` · macOS / Linux: `source .venv/bin/activate`
- Install the exact versions from the video: `python -m pip install -r requirements.txt`
- Check: `python -m pytest --version`

`requirements.txt` is the `pip freeze` output from the episode (versions as of the recording).

## Run it

Open a terminal **in this folder**, then:

- Windows: `python challenge_ep10.py`
- macOS / Linux: `python3 challenge_ep10.py`

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
Login methods: [('publickey', 27)]
```

## Files

- `challenge_ep10.py`
- `requirements.txt`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Rebuild the venv in a new folder from requirements.txt. Answer in episode 12.
