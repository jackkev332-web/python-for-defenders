# Episode 23 — Follow a log live: alerts the moment they happen

Python for Defenders · Chapter 4: Hardening (Advanced)

Video: https://youtu.be/FDy-Ciuq7Gc

## Also try

- `python cpu.py` — a polling loop without `sleep` vs with it (your CPU numbers will differ a little)
- Two terminals, the real way: make sure `live_auth.log` exists first (run `live_demo.py` once). Then in one
  terminal, `python watchdog.py live_auth.log --follow`; in the other, append lines to `live_auth.log`.
  Stop the watchdog with Ctrl+C.
- `python watchdog.py practice_auth.log` — the normal report still works

## Run it

Open a terminal **in this folder**, then:

- Windows: `python live_demo.py`
- macOS / Linux: `python3 live_demo.py`

Expected output:

```
following live_auth.log (Ctrl+C to stop)
ALERT 00:50:35  198.51.100.140 reached 5 failures
ALERT 03:19:09  203.0.113.45 reached 5 failures
ALERT 04:36:21  198.51.100.77 reached 5 failures
ALERT 14:33:51  203.0.113.9 reached 5 failures
stopped: 4 alerts
```

## Files

- `live_demo.py`
- `cpu.py`
- `watchdog.py`
- `test_watchdog.py`
- `practice_auth.log`

`practice_auth.log` is **synthetic**: every IP address is from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, RFC 5737).

## Challenge

Servers rotate logs (the file is renamed and a new one starts). Make --follow notice and reopen it, like tail -F. Share yours in the comments.
