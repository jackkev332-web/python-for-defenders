# Watchdog v1.1 - Python for Defenders, chapter 2
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
users = []
for line in failures:
    ips.append(get_ip(line))
    users.append(get_user(line))

print("Top attackers:", Counter(ips).most_common(3))
print("Top usernames:", Counter(users).most_common(3))
