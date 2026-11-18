"""Make framed_auth.log: the practice day plus a synthetic attack that tries to frame an innocent IP.

The attacker at 198.51.100.66 tries 6 passwords with the username "admin from 192.0.2.10 port 22".
192.0.2.10 is alice, the admin, who only ever logs in with her key.
Each attempt is written the way OpenSSH's sshd formats it (auth.c):
    "Invalid user %.100s from %.100s port %d"
    "%s %s%s%s for %s%.100s from %.200s port %d ssh2"   -> "Failed password for invalid user ..."
The username is whatever the client sends. sshd escapes newlines and control characters in it, but not spaces.
All addresses are documentation addresses (RFC 5737). Usage: python make_framed_log.py [practice_auth.log] [framed_auth.log]
"""
import random
import sys
from datetime import datetime, timedelta

source = sys.argv[1] if len(sys.argv) > 1 else "practice_auth.log"
target = sys.argv[2] if len(sys.argv) > 2 else "framed_auth.log"

ATTACKER = "198.51.100.66"
USERNAME = "admin from 192.0.2.10 port 22"
rng = random.Random(26)

lines = open(source).read().splitlines()
when = datetime.fromisoformat("2026-11-09T09:14:03.000000+00:00")
for attempt in range(6):
    port = rng.randint(40000, 65000)
    pid = rng.randint(1000, 40000)
    head = " web01 sshd[" + str(pid) + "]: "
    t = when + timedelta(seconds=attempt * 9, microseconds=rng.randint(0, 999999))
    lines.append(t.isoformat() + head + "Invalid user " + USERNAME + " from " + ATTACKER + " port " + str(port))
    t += timedelta(seconds=2, microseconds=rng.randint(0, 999999))
    lines.append(t.isoformat() + head + "Failed password for invalid user " + USERNAME
                 + " from " + ATTACKER + " port " + str(port) + " ssh2")
    t += timedelta(microseconds=rng.randint(0, 999999))
    lines.append(t.isoformat() + head + "Connection closed by " + ATTACKER + " port " + str(port))

lines.sort(key=lambda line: line.split()[0])
with open(target, "w") as out:
    out.write("\n".join(lines) + "\n")
print(target + ": " + str(len(lines)) + " lines")
