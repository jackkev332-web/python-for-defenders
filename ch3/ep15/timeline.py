# Timeline - Python for Defenders, chapter 3 (episode 15)
import argparse
from datetime import datetime, timedelta

from watchdog import find_lines, get_ip, read_log

WINDOW = timedelta(seconds=60)


def get_time(line):
    return datetime.fromisoformat(line.split()[0])


def most_in_window(times):
    best = 0
    for start in times:
        count = 0
        for t in times:
            if start <= t < start + WINDOW:
                count = count + 1
        if count > best:
            best = count
    return best


def main():
    parser = argparse.ArgumentParser(
        description="When did each IP fail to log in?")
    parser.add_argument("logfile", help="the auth log to check")
    args = parser.parse_args()

    failures = find_lines(read_log(args.logfile), "Failed password")
    times = {}
    for line in failures:
        ip = get_ip(line)
        if ip not in times:
            times[ip] = []
        times[ip].append(get_time(line))

    print("IP ADDRESS       FAILS  FIRST     MINUTES  BURST")
    bursts = 0
    for ip, seen in times.items():
        first = min(seen)
        lasted = max(seen) - first
        minutes = round(lasted.total_seconds() / 60)
        burst = most_in_window(seen)
        print(f"{ip:<16} {len(seen):>5}  {first:%H:%M:%S}"
              f"  {minutes:>7}  {burst:>5}")
        if burst >= 5:
            bursts = bursts + 1
    print()
    print(f"{bursts} IPs with a burst: 5+ failures within 60 seconds")


if __name__ == "__main__":
    main()
