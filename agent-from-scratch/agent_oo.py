import json
from pprint import pprint

import anthropic
from anthropic.types import Message


class Agent:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.tools = [{
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

    def run(self):
        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=16384,
            tools=self.tools,
            messages=[{
                "role": "user",
                "content": "What's in sample_project/README.md?",
            }],
        )

        # json_string = """
        # {
        #     "id": "msg_011CgdwtVsmHRzVsp6bnuHws",
        #     "container": null,
        #     "content": [
        #         {
        #             "id": "toolu_015Z2xfSz835mWZGg6SUiPM5",
        #             "caller": {
        #                 "type": "direct"
        #             },
        #             "input": {
        #                 "path": "sample_project/README.md"
        #             },
        #             "name": "read_file",
        #             "type": "tool_use",
        #             "toolset_name": null
        #         }
        #     ],
        #     "diagnostics": null,
        #     "model": "claude-sonnet-4-6",
        #     "role": "assistant",
        #     "stop_details": null,
        #     "stop_reason": "tool_use",
        #     "stop_sequence": null,
        #     "type": "message",
        #     "usage": {
        #         "cache_creation": {
        #             "ephemeral_1h_input_tokens": 0,
        #             "ephemeral_5m_input_tokens": 0
        #         },
        #         "cache_creation_input_tokens": 0,
        #         "cache_read_input_tokens": 0,
        #         "inference_geo": "global",
        #         "input_tokens": 574,
        #         "output_tokens": 60,
        #         "output_tokens_details": null,
        #         "server_tool_use": null,
        #         "service_tier": "standard",
        #         "speed": "standard"
        #     }
        # }
        # """

        # response = Message.model_validate_json(json_string)

        print("\nresponse.stop_reason:")
        print(response.stop_reason)
        # print("\nblock:")
        # for block in response.content:
        #     print(block)
        print("\nprint(response.content.model_dump_json(indent=2)):")
        print(response.content.model_dump_json(indent=2)) # WINNER!
        # print("\npprint(response.model_dump()):")
        # pprint(response.model_dump()) # orders alphabetically
        # print("\npprint(response.model_dump_json(indent=2)):")
        # pprint(response.model_dump_json(indent=2)) # prints \n
        # print("\nprint(response.model_dump()):")
        # print(response.model_dump())
        print("\nprint(response.model_dump_json(indent=2)):")
        print(response.model_dump_json(indent=2)) # WINNER!
        # print("\nprint(json.dumps(response.model_dump(), indent=2, default=str)):")
        # print(json.dumps(response.model_dump(), indent=2, default=str)) # long syntax


if __name__ == "__main__":
    Agent().run()