# Watchdog v3.3 - Python for Defenders, chapter 4
import argparse
import asyncio
import json
import re
import sys
import time
from collections import Counter
from datetime import datetime, timedelta, timezone

FAILED = re.compile(
    r"Failed password for (invalid user )?"
    r"(?P<user>\S+) from (?P<ip>\S+)"
)
WEB = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] '
    r'"[^"]*" (?P<status>\d{3}) '
)
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def read_log(path):
    try:
        with open(path) as log:
            for line in log:
                yield line.rstrip("\n")
    except FileNotFoundError:
        print("Can't find " + path + ". Check the file name.",
              file=sys.stderr)
        sys.exit(2)


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


async def follow(path, seconds):
    stop = time.monotonic() + seconds
    with open(path) as log:
        log.seek(0, 2)
        while time.monotonic() < stop:
            line = log.readline()
            if line:
                yield line.rstrip("\n")
            else:
                await asyncio.sleep(0.1)


async def watch_ssh(path, threshold, seconds):
    counts = Counter()
    alerts = 0
    async for line in follow(path, seconds):
        if "Failed password" in line:
            ip = get_ip(line)
            counts[ip] += 1
            if counts[ip] == threshold:
                print(f"ALERT {get_time(line):%H:%M:%S}  SSH  "
                      f"{ip:<15} {threshold} failed logins")
                alerts = alerts + 1
    return alerts


async def watch_web(path, threshold, seconds):
    counts = Counter()
    alerts = 0
    async for line in follow(path, seconds):
        m = WEB.match(line)
        if m and m["status"] == "404":
            counts[m["ip"]] += 1
            if counts[m["ip"]] == threshold:
                when = datetime.strptime(m["time"],
                                         "%d/%b/%Y:%H:%M:%S %z")
                print(f"ALERT {when:%H:%M:%S}  WEB  "
                      f"{m['ip']:<15} {threshold} not-found pages")
                alerts = alerts + 1
    return alerts


async def watch_live(auth, web, threshold, seconds):
    watchers = [watch_ssh(auth, threshold, seconds)]
    if web:
        watchers.append(watch_web(web, 10, seconds))
    alerts = sum(await asyncio.gather(*watchers))
    print(f"done: {alerts} alerts")
    if alerts > 0:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Flag IP addresses with repeated failed SSH logins.")
    parser.add_argument("logfile", help="the auth log to check")
    parser.add_argument("-t", "--threshold", type=int, default=5,
                        help="minimum failures to flag (default: 5)")
    parser.add_argument("--json", action="store_true",
                        help="the log is a journalctl -o json export")
    parser.add_argument("--web", help="a web access log to cross-check")
    parser.add_argument("--follow", action="store_true",
                        help="keep watching the log(s) as they grow")
    parser.add_argument("--seconds", type=float, default=float("inf"),
                        help="with --follow: stop after this many seconds")
    args = parser.parse_args()

    if args.follow:
        try:
            return asyncio.run(watch_live(args.logfile, args.web,
                                          args.threshold, args.seconds))
        except KeyboardInterrupt:
            print("stopped")
            return 0
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
