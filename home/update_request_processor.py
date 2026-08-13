import io
import base64

from common import so2heat_response
from common.so2heat_request import from_json_str
from PIL import Image

from common.so2heat_response import SO2HeatResponse
from home import app_gui
from home.command_buffer import CommandsBuffer


class UpdateRequestProcessor:
    image : Image.Image
    gui: app_gui.SO2HeatGUI
    commands_buffer : CommandsBuffer

    def __init__(self, gui : app_gui.SO2HeatGUI, commands_buffer : CommandsBuffer):
        self.gui = gui
        self.commands_buffer = commands_buffer

    def process_request(self, content, response_hints : dict):
        request = from_json_str(content)
        decoded_image = base64.standard_b64decode(request.photo)
        self.image = Image.open(io.BytesIO(decoded_image))
        self.gui.set_image(self.image)

        response_hints["NEXT_TIMEOUT"] = 1

        commands = self.commands_buffer.getCommands()
        res = SO2HeatResponse()
        res.commands = commands
        return res

if __name__ == "__main__":
    with open("t:/work/so2heat/tests/test.jpg", "rb") as image_file:
        image_bytes = image_file.read()
        base64_string = base64.b64encode(image_bytes).decode('utf-8')
        print(base64_string)