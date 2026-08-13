from pydantic import BaseModel

from common.so2heat_types import CommandType


class SO2HeatCommand(BaseModel):
    command_type : CommandType
    parameters : dict

    def __init__(self, command_type: CommandType, parameters: dict) -> None:
        super().__init__(**{"command_type": command_type, "parameters": parameters})
        self.command_type = command_type
        self.parameters = parameters

    def command_type(self) -> CommandType:
        return self.command_type

    def parameters(self) -> dict:
        return self.parameters