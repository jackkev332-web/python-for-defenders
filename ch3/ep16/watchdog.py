# Watchdog v2.1 - Python for Defenders, chapter 3
import argparse
import json
import re
import textwrap
from collections import Counter

FAILED = re.compile(
    r"Failed password for (invalid user )?"
    r"(?P<user>\S+) from (?P<ip>\S+)"
)


def read_log(path):
    try:
        with open(path) as log:
            text = log.read()
    except FileNotFoundError:
        raise SystemExit("Can't find " + path + ". Check the file name.")
    return text.splitlines()


def read_journal(path):
    messages = []
    for line in read_log(path):
        entry = json.loads(line)
        messages.append(entry["MESSAGE"])
    return messages


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


def main():
    parser = argparse.ArgumentParser(
        description="Flag IP addresses with repeated failed SSH logins.")
    parser.add_argument("logfile", help="the auth log to check")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                        help="minimum failures to flag (default: 5)")
    parser.add_argument("--json", action="store_true",
                        help="the log is a journalctl -o json export")
    args = parser.parse_args()

    if args.json:
        lines = read_journal(args.logfile)
    else:
        lines = read_log(args.logfile)
    failures = find_lines(lines, "Failed password")
    ips = []
    tried = {}
    for line in failures:
        ip = get_ip(line)
        ips.append(ip)
        if ip not in tried:
            tried[ip] = set()
        tried[ip].add(get_user(line))

    print("IP ADDRESS       FAILS  USERNAMES TRIED")
    flagged = 0
    for ip, count in Counter(ips).most_common():
        if count >= args.threshold:
            names = ", ".join(sorted(tried[ip]))
            names = textwrap.shorten(names, 40)
            print(f"{ip:<16} {count:>5}  {names}")
            flagged = flagged + 1
    print()
    print(f"{flagged} suspicious IPs (threshold {args.threshold})")


if __name__ == "__main__":
    main()
