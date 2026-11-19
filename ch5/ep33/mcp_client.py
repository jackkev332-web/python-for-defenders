"""List and call the watchdog's tools over MCP, the way an AI app would.

Starts watchdog_mcp.py as a subprocess, asks it which tools it has, then calls two of them.
The server's own messages (its stderr) go to server.log.
Usage: python mcp_client.py [LOGFILE]
"""
import asyncio
import sys

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.exceptions import MCPError

LOG = sys.argv[1] if len(sys.argv) > 1 else "practice_auth.log"
SERVER = StdioServerParameters(command=sys.executable,
                               args=["watchdog_mcp.py", LOG])
CALLS = [("ip_details", {"ip": "203.0.113.45"}), ("watchdog_report", {})]


async def main():
    with open("server.log", "w") as server_log:
        transport = stdio_client(SERVER, errlog=server_log)
        async with Client(transport, read_timeout_seconds=10) as client:
            listing = await client.list_tools()
            for tool in listing.tools:
                params = ", ".join(tool.input_schema.get("properties", {}))
                print(f"tool: {tool.name}({params})")
            for name, arguments in CALLS:
                try:
                    result = await client.call_tool(name, arguments)
                except MCPError as error:
                    print(f"{name}: MCPError: {error}")
                    continue
                label = "error" if result.is_error else "result"
                print(f"{name} {label}: {result.content[0].text.rstrip()}")


asyncio.run(main())
