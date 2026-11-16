# Episode 17 — Web server logs: who is scanning your site?

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: coming soon

## Also try

- `python scanners.py access.log -t 2` — a threshold that's too low also flags the search crawler (two deleted posts)
- `access.log` is **synthetic**, in the "combined" format (nginx's default). The site is www.example.com; every client IP is from the RFC 5737 documentation ranges.

## Run it

Open a terminal **in this folder**, then:

- Windows: `python scanners.py access.log`
- macOS / Linux: `python3 scanners.py access.log`

Expected output:

```
IP ADDRESS        404s  PATHS TRIED
198.51.100.200      30  /.DS_Store, /.aws/credentials, [...]
203.0.113.45        21  /wp-admin/, /wp-login.php, /xmlrpc.php

2 scanners (threshold 10)
1 skipped (not a normal request)
```

## Files

- `scanners.py`
- `access.log`

## Challenge

Show when each scanner started and stopped. Hint: datetime.strptime(text, "%d/%b/%Y:%H:%M:%S %z"). Share yours in the comments.
