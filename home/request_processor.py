import io

from common.so2heat_request import from_json_str
import base64
from PIL import Image, ImageTk

from home import app_gui


class RequestProcessor:
    image : Image.Image
    gui: app_gui.SO2HeatGUI

    def __init__(self, gui : app_gui.SO2HeatGUI):
        self.gui = gui

    def process_request(self, content):
        request = from_json_str(content)
        decoded_image = base64.standard_b64decode(request.photo)
        self.image = Image.open(io.BytesIO(decoded_image))
        self.gui.set_image(self.image)

if __name__ == "__main__":
    with open("t:/work/so2heat/tests/test.jpg", "rb") as image_file:
        image_bytes = image_file.read()
        base64_string = base64.b64encode(image_bytes).decode('utf-8')
        print(base64_string)