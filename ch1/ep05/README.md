# Episode 5 — Split strings: who is attacking?

Python for Defenders · Chapter 1: Foundations (Novice)

Video: https://youtu.be/qRs0K45AMrY

## Run it

Open a terminal **in this folder**, then:

- Windows: `python watchdog.py`
- macOS / Linux: `python3 watchdog.py`

Expected output (first 15 of 373 lines):

```
Watchdog starting
Lines in log: 1528
Failed logins: 369
Successful logins: 27
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
198.51.100.140
... (358 more lines)
```

## Files

- `watchdog.py`
- `fixed_position.py`
- `challenge_ep04.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Print the username each attacker tried. Hint: it's the word right before “from”. Answer in episode 6.
