from home import app_gui, http_server

global photoW, photoH, imageLabel

from PIL import ImageTk

httpServer = http_server.StoppableHTTPServer()

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
                         stop_http_button_click)
gui.start()

def image_handler(data):
    print("image comming")
    global photo3
    photo3 = ImageTk.PhotoImage(data)
    imageLabel.config(image=photo3)

