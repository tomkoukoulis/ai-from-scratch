from pprint import pprint
import anthropic, json

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

print("\nresponse.stop_reason:")
print(response.stop_reason)

# print("\nblock:")
# for block in response.content:
#     print(block)

print("\nprint(response.content.model_dump_json(indent=2)):")
print(response.content.model_dump_json(indent=2))

print("\nprint(response.model_dump_json(indent=2)):")
print(response.model_dump_json(indent=2))
