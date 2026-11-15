# Watchdog v1.0 - Python for Defenders, chapter 1


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


def count_by_ip(failures):
    counts = {}
    for line in failures:
        ip = get_ip(line)
        counts[ip] = counts.get(ip, 0) + 1
    return counts


def count_users(failures):
    counts = {}
    for line in failures:
        words = line.split()
        user = words[words.index("from") - 1]
        counts[user] = counts.get(user, 0) + 1
    return counts


def top_attackers(counts, n):
    return sorted(counts, key=counts.get, reverse=True)[:n]


print("Watchdog starting")
lines = read_log("practice_auth.log")
print("Lines in log:", len(lines))

failures = find_lines(lines, "Failed password")
print("Failed logins:", len(failures))
successes = find_lines(lines, "Accepted")
print("Successful logins:", len(successes))

counts = count_by_ip(failures)
print(counts)
for ip in top_attackers(counts, 3):
    print(ip, counts[ip])

users = count_users(failures)
for user in top_attackers(users, 3):
    print(user, users[user])
