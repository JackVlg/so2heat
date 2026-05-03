import json

class SO2HeatResponse:
    def __init__(self):
        self.status = "test"
        self.commands = []
        self.nextTimeout = 5000
        self.photo = None

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def deserialize(self, s):
        data = json.loads(s, object_hook=response_decoder)
        return data

def response_decoder(dct):
    res = SO2HeatResponse()
    res.status = dct['status']
    res.nextTimeout = dct['nextTimeout']
    res.photo = dct['photo']
    return res

