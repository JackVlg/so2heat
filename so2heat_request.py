import base64
import json
import os
from json import JSONEncoder

class SO2HeatRequest() :

    def __init__(self, photo):
        self.photo = photo

class RequestEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, SO2HeatRequest):
            result = {'photo' : o.photo}
            return result
        if isinstance(o, bytearray):
            r = base64.b64encode(o).decode('ascii')
            return r
        return None

