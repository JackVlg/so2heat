from enum import StrEnum


class ParameterKeys:
    ROTATE_SPEED = "rotateSpeed"
    ROTATE_DURATION = "rotateDuration"
    ANGLE = "angle"

class CommandType(StrEnum):
    ROTATE = "ROTATE"
    PRESS_MAIN_BUTTON = "PRESS_MAIN_BUTTON"


