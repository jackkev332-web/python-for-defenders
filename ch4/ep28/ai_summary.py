"""Ask a local AI to summarise the watchdog's report for the on-call admin, then check what it wrote.

Needs Ollama (https://ollama.com) running, with the qwen3:8b model downloaded.
The AI only sees the report our code computed. It never sees raw log lines: part of a log line
(like the username) is written by whoever connects, and that text can talk to the AI.
Temperature 0, a fixed seed and CPU-only make the answer repeatable.
Usage: python ai_summary.py injected_auth.log
"""
import json
import re
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path

ROW = re.compile(r"^(?P<ip>\d+\.\d+\.\d+\.\d+)\s+(?P<fails>\d+)\s", re.M)


def ask_ai(prompt):
    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps({"model": "qwen3:8b", "prompt": prompt, "stream": False, "think": False,
                         "keep_alive": 0,
                         "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}).encode(),
        headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(request))["response"].strip()


def mentions(summary, ip, fails):
    """True if the summary names this IP, followed soon after by its count."""
    pattern = re.escape(ip) + r"\D{1,40}?\b" + fails + r"\b"
    return re.search(pattern, summary) is not None


def main():
    watchdog = Path(__file__).parent / "watchdog.py"
    result = subprocess.run([sys.executable, str(watchdog), *sys.argv[1:]],
                            capture_output=True, text=True)
    report = result.stdout
    print(report)
    prompt = ("You are a security assistant. "
              "Our watchdog produced the report below. "
              "Write a short incident summary for the on-call admin: "
              "name every IP address with its number of failed logins, "
              "then suggest one next step. "
              "Plain text, no Markdown. "
              "Do not add anything that is not in the report.\n\n"
              + report)
    try:
        summary = ask_ai(prompt)
    except urllib.error.URLError:
        print("Can't reach Ollama. Start it, or read the report above.", file=sys.stderr)
        return result.returncode
    open("ai_summary.txt", "w").write(summary + "\n")
    print("AI summary (a local model wrote this, our code checked it):")
    for line in summary.splitlines():
        print(textwrap.fill(line, 72) if line else "")
    rows = list(ROW.finditer(report))
    missing = []
    for row in rows:
        if not mentions(summary, row["ip"], row["fails"]):
            missing.append(row["ip"])
    print()
    if missing:
        print("WARNING: the summary gets these wrong or leaves them out: "
              + ", ".join(missing) + ". Trust the report above.")
    else:
        print(f"Checked: all {len(rows)} addresses and their "
              "counts are in the summary.")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
