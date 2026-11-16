# Episode 18 — Alerts: let the watchdog call you

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: coming soon

## Also try

- `python alert.py practice_auth.log -t 500` — exit code 0: OK
- `python alert.py practice_auth.lgo` — exit code 2: the watchdog itself failed (an error, not an attack)
- `python -m pytest` — episode 13's tests still pass

## Run it every 15 minutes (on a machine you administer)

- Linux (`crontab -e`): `*/15 * * * * python3 /opt/watchdog/alert.py /path/to/auth.log`
- Windows: Task Scheduler (`schtasks /create /sc minute /mo 15 ...`)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python alert.py practice_auth.log`
- macOS / Linux: `python3 alert.py practice_auth.log`

Expected output:

```
watchdog exit code: 1
ALERT: suspicious IPs found
IP ADDRESS       FAILS  USERNAMES TRIED
203.0.113.45       212  admin, git, oracle, postgres, [...]
198.51.100.77       96  admin, guest, pi, root, support
203.0.113.9         41  root
198.51.100.140      17  ftpuser, nagios, test

4 suspicious IPs (threshold 5)
```

## Files

- `alert.py`
- `watchdog.py`
- `test_watchdog.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Make alert.py add each alert to alerts.txt, with the date and time. Share yours in the comments.
