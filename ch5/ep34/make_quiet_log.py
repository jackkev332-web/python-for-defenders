"""Make quiet_auth.log: the practice day with every attacker removed. Only our own users are left (alice, bob and the
deploy server, with deploy's two typos). The right answer for this day: nobody attacked.
All addresses are documentation addresses (RFC 5737). Usage: python make_quiet_log.py [practice_auth.log] [quiet_auth.log]
"""
import sys

source = sys.argv[1] if len(sys.argv) > 1 else "practice_auth.log"
target = sys.argv[2] if len(sys.argv) > 2 else "quiet_auth.log"

ATTACKER_NETWORKS = ("203.0.113.", "198.51.100.")
lines = [line for line in open(source).read().splitlines()
         if not any(net in line for net in ATTACKER_NETWORKS)]
with open(target, "w") as out:
    out.write("\n".join(lines) + "\n")
print(target + ": " + str(len(lines)) + " lines")
