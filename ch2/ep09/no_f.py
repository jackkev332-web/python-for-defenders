# Watchdog v1.2 - Python for Defenders, chapter 2
from collections import Counter


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
    words = line.split()
    return words[words.index("from") + 1]


def get_user(line):
    words = line.split()
    return words[words.index("from") - 1]


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
    print("{ip:<16} {count:>5}  {names}")
