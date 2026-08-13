from common.so2heat_command import SO2HeatCommand
from common.so2heat_types import CommandType


class CommandsBuffer:
    commands = []

    def addCommand(self, new_command : SO2HeatCommand):
        if new_command.command_type == CommandType.ROTATE:
            for old_command in self.commands:
                if old_command.command_type == CommandType.ROTATE:
                    self.commands.remove(old_command)

        if new_command.command_type == CommandType.PRESS_MAIN_BUTTON:
            for old_command in self.commands:
                if old_command.command_type == CommandType.PRESS_MAIN_BUTTON:
                    self.commands.remove(old_command)

        self.commands.append(new_command)

    def getCommands(self):
        ready_command: SO2HeatCommand
        result = []
        for ready_command in self.commands:
            result.append(ready_command)
        self.commands.clear()
        return result