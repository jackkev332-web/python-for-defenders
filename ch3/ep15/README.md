# Episode 15 — datetime: when did each attack happen?

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: https://youtu.be/5YK0hZ5g8n0

## Also in this folder

- `python after_four.py` — counts the failed logins after 04:00 UTC (a time with a time zone, so Python can compare it)
- `watchdog.py` — Watchdog v2.0 from episode 14; `timeline.py` imports its functions, so keep both in the same folder

## Run it

Open a terminal **in this folder**, then:

- Windows: `python timeline.py practice_auth.log`
- macOS / Linux: `python3 timeline.py practice_auth.log`

Expected output:

```
IP ADDRESS       FAILS  FIRST     MINUTES  BURST
198.51.100.140      17  00:49:27        5      5
192.0.2.31           2  01:02:11     1286      1
192.0.2.24           1  01:22:46        0      1
203.0.113.45       212  03:17:57       73      7
198.51.100.77       96  04:34:36       35      5
203.0.113.9         41  14:31:52       15      6

4 IPs with a burst: 5+ failures within 60 seconds
```

## Files

- `timeline.py`
- `after_four.py`
- `watchdog.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Add a --since option to timeline.py that skips failures before a time you give. Remember the time zone! Share yours in the comments.
