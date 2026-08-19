import logging

from common import so2heat_response
from common.so2heat_types import CommandType, ParameterKeys
from village.so2heat_motor import SO2HeatMotor


class SO2HeatResponseProcessor:

    log = None
    motor : SO2HeatMotor

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

        self.motor = SO2HeatMotor()

    def process(self, data : str):
        self.log.info("Processing response")

        result_hints = {}

        response = so2heat_response.from_json_str(data)

        if response.status == "Ok":
            commands = response.commands
            self.log.info(commands)

            for command in commands:
                if command.name == CommandType.ROTATE:
                    rotate_speed = command.parameters[ParameterKeys.ROTATE_SPEED]
                    rotate_duration = command.parameters[ParameterKeys.ROTATE_DURATION]
                    self.motor.rotate(rotate_speed, rotate_duration)

            if response.nextTimeout is not None:
                result_hints["NEXT_TIMEOUT"] = response.nextTimeout

        return result_hints

    def stop(self):
        self.motor.stop()
        self.log.info("Stopped response processor.")