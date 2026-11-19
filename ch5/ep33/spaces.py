"""Episode 32's challenge: flag every failed login whose username contains a space.

Real usernames don't have spaces. A "username" with spaces is a sentence, and maybe an order for an AI.
Usage: python spaces.py LOGFILE
"""
import sys

from watchdog import FAILED, read_log

flagged = []
for line in read_log(sys.argv[1]):
    match = FAILED.search(line)
    if match and " " in match["user"]:
        flagged.append(match["user"])
print(f"{len(flagged)} failed login(s) with a space in the username:")
for user in flagged:
    print("  " + user)
