# Watchdog v3.0 - Python for Defenders, chapter 3 finale
import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone

FAILED = re.compile(
    r"Failed password for (invalid user )?"
    r"(?P<user>\S+) from (?P<ip>\S+)"
)
WEB = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[[^\]]+\] '
    r'"[^"]*" (?P<status>\d{3}) '
)
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def read_log(path):
    try:
        with open(path) as log:
            text = log.read()
    except FileNotFoundError:
        print("Can't find " + path + ". Check the file name.",
              file=sys.stderr)
        sys.exit(2)
    return text.splitlines()


def read_journal(path):
    lines = []
    for line in read_log(path):
        entry = json.loads(line)
        usec = int(entry["__REALTIME_TIMESTAMP"])
        when = EPOCH + timedelta(microseconds=usec)
        lines.append(when.isoformat() + " " + entry["MESSAGE"])
    return lines


def find_lines(lines, text):
    found = []
    for line in lines:
        if text in line:
            found.append(line)
    return found


def get_ip(line):
    return FAILED.search(line)["ip"]


def get_time(line):
    return datetime.fromisoformat(line.split()[0])


def web_404s(path):
    counts = Counter()
    for line in read_log(path):
        m = WEB.match(line)
        if m and m["status"] == "404":
            counts[m["ip"]] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(
        description="Flag IP addresses with repeated failed SSH logins.")
    parser.add_argument("logfile", help="the auth log to check")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                        help="minimum failures to flag (default: 5)")
    parser.add_argument("--json", action="store_true",
                        help="the log is a journalctl -o json export")
    parser.add_argument("--web", help="a web access log to cross-check")
    args = parser.parse_args()

    if args.json:
        lines = read_journal(args.logfile)
    else:
        lines = read_log(args.logfile)
    ips = []
    times = {}
    for line in find_lines(lines, "Failed password"):
        ip = get_ip(line)
        ips.append(ip)
        if ip not in times:
            times[ip] = []
        times[ip].append(get_time(line))
    web = Counter()
    if args.web:
        web = web_404s(args.web)

    print("IP ADDRESS       FAILS  FIRST     LAST      WEB 404s")
    flagged = 0
    for ip, count in Counter(ips).most_common():
        if count >= args.threshold:
            first = min(times[ip])
            last = max(times[ip])
            on_web = "-"
            if args.web:
                on_web = web[ip]
            print(f"{ip:<16} {count:>5}  {first:%H:%M:%S}"
                  f"  {last:%H:%M:%S}  {on_web:>8}")
            flagged = flagged + 1
    print()
    print(f"{flagged} suspicious IPs (threshold {args.threshold})")
    if flagged > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
