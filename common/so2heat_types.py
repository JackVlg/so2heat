from enum import Enum

class ParameterKeys:
    ROTATE_DIRECTION = "rotateDirection"
    ROTATE_SPEED = "rotateSpeed"

class RotateDirection(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class CommandType(Enum):
    ROTATE = "ROTATE"
    PRESS_MAIN_BUTTON = "PRESS_MAIN_BUTTON"


