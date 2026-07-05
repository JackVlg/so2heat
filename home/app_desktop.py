from home import app_gui, http_server, request_processor
import os
from home.request_processor import RequestProcessor

imgSize = (800, 600)

print("Working directory:", os.getcwd())
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))

httpServer : http_server.StoppableHTTPServer

def left_button_click():
    gui.set_label("Left pressed!")

def right_button_click():
    gui.set_label("Right pressed!")

def start_http_button_click():
    httpServer.start()
    gui.set_home_image()
    gui.set_label("Http server started!")

def stop_http_button_click():
    httpServer.stop()
    gui.set_work_image()
    gui.set_label("Http server stopped!")

gui = app_gui.SO2HeatGUI(left_button_click,
                         right_button_click,
                         start_http_button_click,
                         stop_http_button_click,
                         imgSize)

request_processor = RequestProcessor(gui)

httpServer = http_server.StoppableHTTPServer()
http_server.update_request_handler = request_processor.process_request

gui.start()