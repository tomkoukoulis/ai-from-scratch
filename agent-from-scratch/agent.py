from pprint import pprint
from pathlib import Path
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

def read_file(path: str) -> str:
    target = Path(path)
    if target.is_dir():
        return "\n".join(path_of_item.name for path_of_item in target.iterdir())
    
    return target.read_text()

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

tool_use = next(block for block in response.content if block.type == "tool_use")
result = read_file(tool_use.input["path"])

response2 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16384,
    tools=TOOLS,
    messages=[
        {"role": "user", "content": "What's in sample_project/README.md?"},
        {"role": "assistant", "content": response.content},
        {"role": "user", "content": [{
            "type": "tool_result",
            "tool_use_id": tool_use.id,
            "content": result,
        }]},
    ],
)

print(response2.stop_reason)
# for block in response2.content:
#     if block.type == "text":
#         print(block.text)
print("\nprint(response2.content.model_dump_json(indent=2)):")
print(response2.content.model_dump_json(indent=2))