"""Watchdog v5.0's tool server (MCP): the watchdog's tools, for any MCP client, an AI app or our own agent.

A client starts it and talks to it over stdin and stdout (JSON-RPC), so it never prints to stdout itself.
block_ip only proposes, refuses our own users whoever asks, and every decision goes to audit.log.
Usage (by a client, e.g. agent.py): python watchdog_mcp.py [LOGFILE]
"""
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

from watchdog import FAILED

LOG = "practice_auth.log"
BLOCKLIST = "blocklist.txt"
AUDIT = "audit.log"
OUR_USERS = {"192.0.2.10": "alice", "192.0.2.24": "bob",
             "192.0.2.31": "deploy"}  # never blocked, whoever asks
mcp = MCPServer("watchdog")


def read_lines():
    """A server must answer, not exit: a missing log is an error for this call only."""
    if not Path(LOG).exists():
        raise ToolError("Can't find " + LOG + ". Check the file name.")
    return Path(LOG).read_text().splitlines()


def audit(event):
    """Every decision, with the time. To a file: stdout belongs to the protocol."""
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    with open(AUDIT, "a") as log:
        log.write(f"{stamp} {event}\n")


@mcp.tool()
def watchdog_report() -> str:
    """Run the watchdog on today's SSH log. Returns a table of suspicious IP addresses and their failed logins."""
    watchdog = Path(__file__).parent / "watchdog.py"
    run = subprocess.run([sys.executable, str(watchdog), LOG],
                         capture_output=True, text=True)
    if run.returncode == 2:  # the watchdog's "can't read the log" exit code
        raise ToolError(run.stderr.strip())
    return run.stdout


@mcp.tool()
def ip_details(ip: str) -> str:
    """Details for one IP address: its failed logins, first and last time, and the usernames it tried."""
    times = []
    users = Counter()
    for line in read_lines():
        match = FAILED.search(line)
        if match and match["ip"] == ip:
            times.append(line[11:19])  # the time, HH:MM:SS
            users[match["user"]] += 1
    if not times:
        return "No failed logins from " + ip + "."
    top = ", ".join(f"{user} ({n})" for user, n in users.most_common(3))
    return (f"{ip}: {len(times)} failed logins, first {times[0]}, "
            f"last {times[-1]}. Most tried usernames: {top}")


@mcp.tool()
def recent_failures(n: int) -> str:
    """Return the latest failed SSH login lines from today's log."""
    failed = [line for line in read_lines() if FAILED.search(line)]
    return "\n".join(failed[-n:])


@mcp.tool()
def block_ip(ip: str) -> str:
    """Block an IP address at the firewall."""
    if ip in OUR_USERS:
        audit(f"the AI asked to block {ip}: refused, our user {OUR_USERS[ip]}")
        return f"Refused: {ip} is one of our own users ({OUR_USERS[ip]})."
    audit(f"the AI proposed blocking {ip}")
    return f"Proposed: blocking {ip} needs a person's approval."


def approve(ip):
    """A person decides. Not a tool, so the AI can never call it."""
    if ip in OUR_USERS:
        audit(f"a person asked to block {ip}: refused, our user {OUR_USERS[ip]}")
        return f"Refused: {ip} is one of our own users ({OUR_USERS[ip]})."
    with open(BLOCKLIST, "a") as blocklist:
        blocklist.write(ip + "\n")
    audit(f"a person blocked {ip}: added to {BLOCKLIST}")
    return f"Blocked {ip}: added to {BLOCKLIST}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        LOG = sys.argv[1]  # the log every tool reads
    mcp.run()  # stdio: the client that started us is on the other end
