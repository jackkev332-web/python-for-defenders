"""The watchdog as an MCP tool server: any MCP client, an AI app or our own script, can list and call its tools.

A client starts it and talks to it over stdin and stdout (JSON-RPC), so it never prints to stdout itself.
Usage (by a client, e.g. mcp_client.py): python watchdog_mcp.py [LOGFILE]
"""
import subprocess
import sys
from collections import Counter
from pathlib import Path

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

from watchdog import FAILED

LOG = sys.argv[1] if len(sys.argv) > 1 else "practice_auth.log"
mcp = MCPServer("watchdog")


def read_lines():
    """A server must answer, not exit: a missing log is an error for this call only."""
    if not Path(LOG).exists():
        raise ToolError("Can't find " + LOG + ". Check the file name.")
    return Path(LOG).read_text().splitlines()


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


if __name__ == "__main__":
    mcp.run()  # stdio: the client that started us is on the other end
