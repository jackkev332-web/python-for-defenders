#!/usr/bin/env python3
"""Generate the SYNTHETIC practice log for the Python for Defenders series.

All IPs come from RFC 5737 documentation ranges (192.0.2.0/24,
198.51.100.0/24, 203.0.113.0/24), so no real host is referenced.
Deterministic: same seed -> same file, byte for byte (LF line endings on every OS).
Identical content to the trailer (video_001), so the series reaches the same numbers.
Usage: python make_practice_log.py practice_auth.log
"""
import random
import sys
from datetime import datetime, timedelta, timezone

rng = random.Random(1337)
HOST = "web01"
start = datetime(2026, 11, 9, 0, 0, 0, tzinfo=timezone.utc)

legit = {"192.0.2.10": "alice", "192.0.2.24": "bob", "192.0.2.31": "deploy"}
attackers = {
    "203.0.113.45": (212, ["root", "admin", "ubuntu", "test", "oracle", "postgres", "git", "user"]),
    "198.51.100.77": (96, ["root", "admin", "support", "pi", "guest"]),
    "203.0.113.9": (41, ["root"]),
    "198.51.100.140": (17, ["ftpuser", "test", "nagios"]),
}
real_users = {"root", "ubuntu", "alice", "bob", "deploy", "git"}

events = []  # (time, message)
for ip, user in legit.items():
    for _ in range(rng.randint(6, 12)):
        t = start + timedelta(seconds=rng.randint(0, 86399), microseconds=rng.randint(0, 999999))
        if rng.random() < 0.15:  # an honest typo before the right password
            events.append((t, f"Failed password for {user} from {ip} port {rng.randint(40000, 65000)} ssh2"))
            t += timedelta(seconds=rng.randint(3, 9))
        events.append((t, f"Accepted publickey for {user} from {ip} port {rng.randint(40000, 65000)} ssh2: ED25519 SHA256:{''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=43))}"))
for ip, (n, names) in attackers.items():
    t = start + timedelta(seconds=rng.randint(0, 60000))
    for _ in range(n):
        t += timedelta(seconds=rng.randint(1, 40), microseconds=rng.randint(0, 999999))
        user = rng.choice(names)
        port = rng.randint(30000, 65000)
        if user not in real_users:
            events.append((t, f"Invalid user {user} from {ip} port {port}"))
            events.append((t + timedelta(seconds=2), f"Failed password for invalid user {user} from {ip} port {port} ssh2"))
        else:
            events.append((t + timedelta(seconds=2), f"Failed password for {user} from {ip} port {port} ssh2"))
# background noise
for _ in range(900):
    t = start + timedelta(seconds=rng.randint(0, 86399), microseconds=rng.randint(0, 999999))
    events.append((t, rng.choice([
        "pam_unix(sshd:session): session closed for user deploy",
        "Received disconnect from 192.0.2.31 port 52210:11: disconnected by user",
        "Connection closed by 192.0.2.24 port 50122",
        "pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)",
    ])))

events.sort(key=lambda e: e[0])
out = open(sys.argv[1], "w", encoding="utf-8", newline="\n") if len(sys.argv) > 1 else sys.stdout
for t, msg in events:
    proc = "CRON" if "cron" in msg else "sshd"
    pid = rng.randint(1000, 39999)
    out.write(f"{t.isoformat(timespec='microseconds')} {HOST} {proc}[{pid}]: {msg}\n")
