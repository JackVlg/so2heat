import logging

from common import so2heat_response
from common.so2heat_types import CommandType, ParameterKeys
from village.so2heat_motor import SO2HeatMotor
from village.so2heat_servo import SO2HeatServo

class SO2HeatResponseProcessor:

    log = None
    motor : SO2HeatMotor
    servo : SO2HeatServo

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

        self.motor = SO2HeatMotor()
        self.servo = SO2HeatServo()

    def process(self, data : str):
        self.log.info("Processing response")

        result_hints = {}

        response = so2heat_response.from_json_str(data)

        if response.status == "Ok":
            commands = response.commands
            self.log.info(commands)

            for command in commands:
                self.log.info(command)
                if command.command_type == CommandType.ROTATE:
                    rotate_speed = command.parameters[ParameterKeys.ROTATE_SPEED]
                    rotate_duration = command.parameters[ParameterKeys.ROTATE_DURATION]
                    self.motor.rotate(rotate_speed, rotate_duration)
                if command.command_type == CommandType.PRESS_MAIN_BUTTON:
                    angle = command.parameters[ParameterKeys.ANGLE]
                    self.servo.press_button(angle)

            if response.nextTimeout is not None:
                result_hints["NEXT_TIMEOUT"] = response.nextTimeout

        return result_hints

    def stop(self):
        self.motor.stop()
        self.log.info("Stopped response processor.")