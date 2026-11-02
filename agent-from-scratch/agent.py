from pprint import pprint
import anthropic

client = anthropic.Anthropic()

TOOLS = [{
    "name": "read_file",
    "description": "Read a file, or list the names in a directory.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string"
            }
        },
        "required": ["path"],
    },
}]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16384,
    tools=TOOLS,
    messages=[{
        "role": "user",
        "content": "What's in sample_project/README.md?",
    }],
)

print(response.stop_reason)
for block in response.content:
    print(block)
pprint(response)