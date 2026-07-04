from pydantic import BaseModel
from common.soheat_command import SO2HeatCommand
import json


def from_json_str(json_str: str):
    fields_map = json.loads(json_str)
    restored_response = SO2HeatResponse(**fields_map)
    return restored_response


class SO2HeatResponse(BaseModel):
    status: str = 'Ok'
    commands: list[SO2HeatCommand] = []
    nextTimeout: int = 5


if __name__ == "__main__":
    response = SO2HeatResponse()

    cmd1_data = {"name": "PRESS BUTTON", "parameters": {"buttonName" : 'MAIN'}}
    cmd1 = SO2HeatCommand(**cmd1_data)
    response.commands.append(cmd1)

    jsonStr = response.model_dump_json(indent=2, exclude_none=True)
    print(jsonStr)

    print("---------------------------")
    restored = from_json_str(jsonStr)
    print(restored)

