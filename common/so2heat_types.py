from enum import Enum

class ParameterKeys:
    ROTATE_SPEED = "rotateSpeed"
    ROTATE_DURATION = "rotateDuration"

class CommandType(Enum):
    ROTATE = "ROTATE"
    PRESS_MAIN_BUTTON = "PRESS_MAIN_BUTTON"


