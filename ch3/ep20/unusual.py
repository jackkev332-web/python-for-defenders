# Unusual visitors - Python for Defenders, chapter 3 (episode 20)
import argparse
import re

from sklearn.ensemble import IsolationForest

LINE = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[[^\]]+\] '
    r'"(?P<method>\S+) (?P<path>\S+) [^"]*" '
    r'(?P<status>\d{3}) '
)


def features(path):
    stats = {}
    with open(path) as log:
        for line in log:
            m = LINE.match(line)
            if m is None:
                continue
            ip = m["ip"]
            if ip not in stats:
                stats[ip] = {"requests": 0, "missing": 0,
                             "paths": set()}
            s = stats[ip]
            s["requests"] += 1
            if m["status"] == "404":
                s["missing"] += 1
            s["paths"].add(m["path"])
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Score how unusual each IP address looks.")
    parser.add_argument("logfile", help="the web server's access log")
    args = parser.parse_args()

    stats = features(args.logfile)
    ips = sorted(stats)
    rows = []
    for ip in ips:
        s = stats[ip]
        rows.append([s["requests"], s["missing"], len(s["paths"])])

    model = IsolationForest(random_state=0)
    model.fit(rows)
    scores = model.score_samples(rows)
    labels = model.predict(rows)

    print("IP ADDRESS       REQS  404s  PATHS   SCORE")
    ranked = sorted(zip(scores, ips, rows, labels))
    for score, ip, row, label in ranked[:6]:
        note = ""
        if label == -1:
            note = "unusual"
        print(f"{ip:<16} {row[0]:>4}  {row[1]:>4}  {row[2]:>5}"
              f"  {score:6.3f}  {note}")
    print()
    print(f"{list(labels).count(-1)} of {len(ips)} IPs look unusual")


if __name__ == "__main__":
    main()
