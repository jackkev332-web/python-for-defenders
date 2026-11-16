# Watchdog v2.0 - Python for Defenders, chapter 2
import argparse
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
    args = parser.parse_args()

    failures = find_lines(read_log(args.logfile), "Failed password")
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
