# Watchdog v1.3 - Python for Defenders, chapter 2
import re
from collections import Counter

FAILED = re.compile(
    r"for (invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)
ACCEPTED = re.compile(
    r"Accepted (?P<method>\S+) for (?P<user>\S+) from"
)


def read_log(path):
    try:
        with open(path) as log:
            text = log.read()
    except FileNotFoundError:
        raise SystemExit("Can't find " + path + ". Open your terminal in its folder.")
    return text.splitlines()


def find_lines(lines, text):
    found = []
    for line in lines:
        if text in line:
            found.append(line)
    return found


def get_ip(line):
    return FAILED.search(line)["ip"]


def get_user(line):
    return FAILED.search(line)["user"]


print("Watchdog starting")
lines = read_log("practice_auth.log")
print("Lines in log:", len(lines))

failures = find_lines(lines, "Failed password")
print("Failed logins:", len(failures))
successes = find_lines(lines, "Accepted")
print("Successful logins:", len(successes))

ips = []
tried = {}
for line in failures:
    ip = get_ip(line)
    ips.append(ip)
    if ip not in tried:
        tried[ip] = set()
    tried[ip].add(get_user(line))

print()
print("IP ADDRESS       FAILS  USERNAMES TRIED")
for ip, count in Counter(ips).most_common():
    names = ", ".join(sorted(tried[ip]))
    print(f"{ip:<16} {count:>5}  {names}")

methods = []
for line in successes:
    methods.append(ACCEPTED.search(line)["method"])
print("Login methods:", Counter(methods).most_common())
