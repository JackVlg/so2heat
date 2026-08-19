from typing import List

from pydantic import BaseModel
import json

from common.so2heat_command import SO2HeatCommand


def from_json_str(json_str: str):
    fields_map = json.loads(json_str)
    restored_response = SO2HeatResponse(**fields_map)
    new_list = []
    for item in restored_response.commands:
        new_list.append(SO2HeatCommand(**item))
    restored_response.commands = new_list
    return restored_response


class SO2HeatResponse(BaseModel):
    status: str = 'Ok'
    commands : List = []
    nextTimeout: int = 5

if __name__ == "__main__":
    response = SO2HeatResponse()

    rs1 = '{"status": "Ok","commands": [{"command_type": "PRESS_MAIN_BUTTON","parameters": {}},{"command_type": "ROTATE","parameters": {"rotateDirection": "RIGHT"}}],"nextTimeout": 1}'
    restored = from_json_str(rs1)
    print(restored)

    js = restored.model_dump_json(indent=2, exclude_none=True)
    print(js)

