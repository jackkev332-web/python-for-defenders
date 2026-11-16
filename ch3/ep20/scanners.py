# Scanner finder - Python for Defenders, chapter 3 (episode 17)
import argparse
import re
import textwrap
from collections import Counter

LINE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[[^\]]+\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]*" '
    r'(?P<status>\d{3}) '
)


def main():
    parser = argparse.ArgumentParser(
        description="Flag IP addresses that ask for many missing pages.")
    parser.add_argument("logfile", help="the web server's access log")
    parser.add_argument("-t", "--threshold", type=int, default=10,
                        help="minimum 404s to flag (default: 10)")
    args = parser.parse_args()

    ips = []
    paths = {}
    skipped = 0
    with open(args.logfile) as log:
        for line in log:
            m = LINE.match(line)
            if m is None:
                skipped = skipped + 1
                continue
            if m["status"] == "404":
                ips.append(m["ip"])
                if m["ip"] not in paths:
                    paths[m["ip"]] = set()
                paths[m["ip"]].add(m["path"])

    print("IP ADDRESS        404s  PATHS TRIED")
    flagged = 0
    for ip, count in Counter(ips).most_common():
        if count >= args.threshold:
            tried = ", ".join(sorted(paths[ip]))
            tried = textwrap.shorten(tried, 40)
            print(f"{ip:<16} {count:>5}  {tried}")
            flagged = flagged + 1
    print()
    print(f"{flagged} scanners (threshold {args.threshold})")
    print(f"{skipped} skipped (not a normal request)")


if __name__ == "__main__":
    main()
