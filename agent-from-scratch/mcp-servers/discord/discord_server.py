import json
import os
import urllib.request

from mcp.server import MCPServer

mcp = MCPServer("discord")

@mcp.tool()
def send_message(username: str, message: str) -> str:
    """Post a message to the cohort's Discord channel."""
    payload = json.dumps({"content": f"**{username}**: {message}"}).encode()
    request = urllib.request.Request(
        os.environ["WEBHOOK_URL"],
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "mcp-workshop"},
    )
    urllib.request.urlopen(request).read()
    return f"Posted to the channel as {username}"

mcp.run()
