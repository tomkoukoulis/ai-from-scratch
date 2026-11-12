
import json
import os
import urllib.request
import urllib.error
import certifi

os.environ.setdefault("SSL_CERT_FILE", certifi.where())

from mcp.server import MCPServer

mcp = MCPServer("discord")

@mcp.tool()
def send_message(username: str, message: str) -> str:
    """Post a message to the cohort's Discord channel."""

    webhook_url = os.environ.get("WEBHOOK_URL")
    if not webhook_url:
        return "Error: WEBHOOK_URL is not configured."

    payload = json.dumps({
        "content": f"**{username}**: {message}"
    }).encode()

    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "mcp-workshop",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            response.read()
            return f"Posted to the channel as {username}"

    except urllib.error.HTTPError as e:
        details = e.read().decode("utf-8", errors="replace")
        return f"Discord HTTP error {e.code}: {details}"

    except urllib.error.URLError as e:
        return f"Connection error: {e.reason}"

    except TimeoutError:
        return "Error: Discord webhook request timed out."

mcp.run()
