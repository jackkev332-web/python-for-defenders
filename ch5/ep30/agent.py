"""Watchdog agent v0.2: a loop. The AI asks for tools until it can answer.

Needs Ollama (https://ollama.com) running, with the qwen3:8b model downloaded.
The AI can only ask for a tool; this script decides what actually runs.
Temperature 0, a fixed seed and CPU-only make the answers repeatable.
Every step is printed; the whole conversation is saved to conversation.json.
Usage: python agent.py "your question" [--max-steps N]
"""
import argparse
import json
import re
import subprocess
import sys
import textwrap
import urllib.request
from collections import Counter
from pathlib import Path

from watchdog import FAILED, read_log

LOG = "practice_auth.log"
IP = re.compile(r"\d+\.\d+\.\d+\.\d+")
TOOLS = [
    {"type": "function", "function": {
        "name": "watchdog_report",
        "description": "Run the watchdog on today's SSH log. Returns a table "
                       "of suspicious IP addresses and their failed logins.",
        "parameters": {"type": "object",
                       "properties": {}, "required": []}}},
    {"type": "function", "function": {
        "name": "ip_details",
        "description": "Details for one IP address: its failed logins, "
                       "first and last time, and the usernames it tried.",
        "parameters": {"type": "object", "properties": {
            "ip": {"type": "string", "description": "the IP address"}},
            "required": ["ip"]}}},
    {"type": "function", "function": {
        "name": "recent_failures",
        "description": "Return the latest failed SSH login lines "
                       "from today's log.",
        "parameters": {"type": "object", "properties": {
            "n": {"type": "integer", "description": "how many lines"}},
            "required": ["n"]}}},
]


def watchdog_report():
    watchdog = Path(__file__).parent / "watchdog.py"
    return subprocess.run([sys.executable, str(watchdog), LOG],
                          capture_output=True, text=True).stdout


def ip_details(ip):
    times = []
    users = Counter()
    for line in read_log(LOG):
        match = FAILED.search(line)
        if match and match["ip"] == ip:
            times.append(line[11:19])  # the time, HH:MM:SS
            users[match["user"]] += 1
    if not times:
        return "No failed logins from " + ip + "."
    top = ", ".join(f"{user} ({n})" for user, n in users.most_common(3))
    return (f"{ip}: {len(times)} failed logins, first {times[0]}, "
            f"last {times[-1]}. Most tried usernames: {top}")


def recent_failures(n):
    failed = [line for line in read_log(LOG) if FAILED.search(line)]
    return "\n".join(failed[-n:])


FUNCTIONS = {"watchdog_report": watchdog_report, "ip_details": ip_details,
             "recent_failures": recent_failures}


def check(answer):
    """Our rule, in code: the answer names the report's worst IP first."""
    top_row = watchdog_report().splitlines()[1].split()
    if not top_row:
        return None  # nothing flagged today: nothing to check
    worst = top_row[0]
    named = IP.findall(answer)
    if named and named[0] == worst:
        return None
    first = named[0] if named else "no IP address"
    return (f"Check failed: your answer puts {first} first, but the "
            f"watchdog report's worst attacker is {worst}. Answer again.")


def chat(messages):
    body = {"model": "qwen3:8b", "messages": messages, "tools": TOOLS,
            "stream": False, "think": False, "keep_alive": 0,
            "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}
    request = urllib.request.Request(
        "http://localhost:11434/api/chat", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(request))["message"]


def main():
    parser = argparse.ArgumentParser(description="Ask the watchdog agent.")
    parser.add_argument("question")
    parser.add_argument("--max-steps", type=int, default=5,
                        help="stop after this many AI replies (default: 5)")
    args = parser.parse_args()
    print("You: " + args.question)
    messages = [{"role": "user", "content": args.question}]
    answer = None
    for step in range(1, args.max_steps + 1):
        reply = chat(messages)
        messages.append(reply)
        calls = reply.get("tool_calls") or []
        if not calls:
            print(f"step {step}: the AI answers")
            problem = check(reply["content"])
            if problem:
                print(problem)
                messages.append({"role": "user", "content": problem})
                continue
            answer = reply["content"]
            break
        for call in calls:
            name = call["function"]["name"]
            arguments = call["function"]["arguments"]
            print(f"step {step}: {name}({arguments})")
            if name in FUNCTIONS:
                result = FUNCTIONS[name](**arguments)
            else:
                result = "There is no tool called " + name
            messages.append({"role": "tool", "content": result,
                             "tool_name": name})
    Path("conversation.json").write_text(json.dumps(messages, indent=2))
    if answer is None:
        print(f"Stopped: no answer after {args.max_steps} steps.")
        return
    print("AI:")
    for line in answer.splitlines():
        print(textwrap.fill(line, 72) if line else "")


if __name__ == "__main__":
    main()
