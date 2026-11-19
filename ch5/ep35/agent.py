"""Watchdog v5.0: an AI triage assistant. Its tools come from the watchdog's MCP server.

Needs Ollama (https://ollama.com) running with qwen3:8b, and the mcp package (episode 33).
The AI only asks; the MCP server runs the tools; block_ip only proposes; a person approves.
Temperature 0, a fixed seed and CPU-only make the answers repeatable.
Usage: python agent.py "your question" [--max-steps N] [--log FILE]
       python agent.py --approve IP      (a person blocks IP)
"""
import argparse
import asyncio
import json
import re
import sys
import textwrap
import urllib.request
from pathlib import Path

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client

from watchdog_mcp import OUR_USERS, approve

LOG = "practice_auth.log"
IP = re.compile(r"\d+\.\d+\.\d+\.\d+")
OPTIONS = {"temperature": 0, "seed": 42, "num_gpu": 0}  # repeatable on CPU


def check(answer, question, report):
    """Our rule, in code: an answer about attackers names the worst IP first."""
    if "attacker" not in question.lower():
        return None  # the rule is about attackers; other questions pass
    top_row = report.splitlines()[1].split()
    if not top_row:
        return None  # nothing flagged today: nothing to check
    worst = top_row[0]
    named = IP.findall(answer)
    if named and named[0] == worst:
        return None
    first = named[0] if named else "no IP address"
    return (f"Check failed: your answer puts {first} first, but the "
            f"watchdog report's worst attacker is {worst}. Answer again.")


def chat(messages, tools):
    body = {"model": "qwen3:8b", "messages": messages, "tools": tools,
            "stream": False, "think": False, "keep_alive": 0,
            "options": OPTIONS}
    request = urllib.request.Request(
        "http://localhost:11434/api/chat", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(request))["message"]


async def ask(question, max_steps):
    server = StdioServerParameters(command=sys.executable,
                                   args=["watchdog_mcp.py", LOG])
    made, proposals, answer = [], [], None
    messages = [{"role": "user", "content": question}]
    with open("server.log", "w") as server_log:
        transport = stdio_client(server, errlog=server_log)
        async with Client(transport, read_timeout_seconds=60) as client:
            listing = await client.list_tools()
            tools = [{"type": "function", "function": {
                "name": tool.name, "description": tool.description,
                "parameters": tool.input_schema}} for tool in listing.tools]
            for step in range(1, max_steps + 1):
                reply = chat(messages, tools)
                messages.append(reply)
                calls = reply.get("tool_calls") or []
                if not calls:
                    print(f"step {step}: the AI answers")
                    report = await client.call_tool("watchdog_report", {})
                    problem = check(reply["content"], question,
                                    report.content[0].text)
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
                    made.append((name, arguments))
                    result = await client.call_tool(name, arguments)
                    text = result.content[0].text if result.content else ""
                    if name == "block_ip" and text.startswith("Proposed"):
                        proposals.append(arguments["ip"])
                    messages.append({"role": "tool", "content": text,
                                     "tool_name": name})
    Path("conversation.json").write_text(json.dumps(messages, indent=2))
    return {"answer": answer, "calls": made, "proposals": proposals}


def run(question, max_steps=5):
    """Ask the agent one question. Returns its answer (None if it stopped),
    every tool call it made, and what it proposed to block."""
    return asyncio.run(ask(question, max_steps))


def main():
    global LOG
    parser = argparse.ArgumentParser(description="Ask the watchdog agent.")
    parser.add_argument("question", nargs="?")
    parser.add_argument("--max-steps", type=int, default=5,
                        help="stop after this many AI replies (default: 5)")
    parser.add_argument("--approve", metavar="IP",
                        help="a person approves blocking IP")
    parser.add_argument("--log", default=LOG,
                        help="the SSH log to read (default: practice_auth.log)")
    args = parser.parse_args()
    LOG = args.log  # the MCP server reads this file
    if args.approve:
        print(approve(args.approve))
        return
    print("You: " + args.question)
    result = run(args.question, args.max_steps)
    if result["answer"] is None:
        print(f"Stopped: no answer after {args.max_steps} steps.")
    else:
        print("AI:")
        for line in result["answer"].splitlines():
            print(textwrap.fill(line, 72) if line else "")
    for ip in result["proposals"]:
        print(f"Proposed by the AI: block {ip}. "
              f"To approve: python agent.py --approve {ip}")


if __name__ == "__main__":
    main()
