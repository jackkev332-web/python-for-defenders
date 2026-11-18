"""Watchdog agent v0.1: a local AI answers your question by asking OUR code for the facts.

Needs Ollama (https://ollama.com) running, with the qwen3:8b model downloaded.
The AI can't read your server. It can only ask for a tool; this script decides what actually runs.
Temperature 0, a fixed seed and CPU-only make the answer repeatable.
The whole conversation is saved to conversation.json, so you can see exactly what was sent.
Usage: python agent.py
"""
import json
import subprocess
import sys
import textwrap
import urllib.request
from pathlib import Path

LOG = "practice_auth.log"
QUESTION = ("Which IP addresses attacked my server today, "
            "and how many failed logins did each one have?")
TOOLS = [{
    "type": "function",
    "function": {
        "name": "watchdog_report",
        "description": "Run the watchdog on today's SSH log. Returns a table "
                       "of suspicious IP addresses and their failed logins.",
        "parameters": {"type": "object",
                       "properties": {}, "required": []},
    },
}]


def watchdog_report():
    watchdog = Path(__file__).parent / "watchdog.py"
    return subprocess.run([sys.executable, str(watchdog), LOG],
                          capture_output=True, text=True).stdout


def chat(messages):
    body = {"model": "qwen3:8b", "messages": messages, "tools": TOOLS,
            "stream": False, "think": False, "keep_alive": 0,
            "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}
    request = urllib.request.Request(
        "http://localhost:11434/api/chat", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(request))["message"]


def main():
    print("You: " + QUESTION)
    messages = [{"role": "user", "content": QUESTION}]
    reply = chat(messages)
    messages.append(reply)
    calls = reply.get("tool_calls") or []
    for call in calls:
        name = call["function"]["name"]
        args = call["function"]["arguments"]
        print(f"AI asks to run: {name}({args})")
        if name == "watchdog_report":
            result = watchdog_report()
        else:
            result = "There is no tool called " + name
        print(f"Our code runs it and sends back {len(result.splitlines())} lines.")
        messages.append({"role": "tool", "content": result, "tool_name": name})
    if calls:
        reply = chat(messages)
        messages.append(reply)
    Path("conversation.json").write_text(json.dumps(messages, indent=2))
    print("AI:")
    for line in reply["content"].splitlines():
        print(textwrap.fill(line, 72) if line else "")


if __name__ == "__main__":
    main()
