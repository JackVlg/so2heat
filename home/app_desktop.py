from common.so2heat_command import SO2HeatCommand
from common.so2heat_types import CommandType, RotateDirection, ParameterKeys
from home import app_gui, http_server, command_buffer
import os

from home.command_buffer import CommandsBuffer
from home.update_request_processor import UpdateRequestProcessor

print("Working directory:", os.getcwd())
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))

commands_buffer : CommandsBuffer = command_buffer.CommandsBuffer()

httpServer : http_server.StoppableHTTPServer

def start_http_button_click():
    httpServer.start()
    gui.set_home_image()
    gui.set_label("Http server started!")

def stop_http_button_click():
    httpServer.stop()
    gui.set_work_image()
    gui.set_label("Http server stopped!")

def left_button_click():
    gui.set_label("Left pressed!")
    command = SO2HeatCommand(CommandType.ROTATE, {ParameterKeys.ROTATE_DIRECTION : RotateDirection.LEFT})
    global commands_buffer
    commands_buffer.addCommand(command)

def right_button_click():
    gui.set_label("Right pressed!")
    command = SO2HeatCommand(CommandType.ROTATE, {ParameterKeys.ROTATE_DIRECTION : RotateDirection.RIGHT})
    global commands_buffer
    commands_buffer.addCommand(command)

def central_button_click():
    gui.set_label("Apply pressed!")
    command = SO2HeatCommand(CommandType.PRESS_MAIN_BUTTON, {})
    global commands_buffer
    commands_buffer.addCommand(command)

gui = app_gui.SO2HeatGUI(left_button_click,
                         right_button_click,
                         start_http_button_click,
                         stop_http_button_click,
                         central_button_click)

update_request_processor = UpdateRequestProcessor(gui, commands_buffer)

httpServer = http_server.StoppableHTTPServer()
http_server.update_request_handler = update_request_processor.process_request

gui.start()