from pydantic import BaseModel
import base64
import json

def from_json_str(json_str: str):
    fields_map = json.loads(json_str)
    restored_request = SO2HeatRequest(**fields_map)
    return restored_request

class SO2HeatRequest(BaseModel) :
    photo: str = None

if __name__ == "__main__":
    request = SO2HeatRequest()

    test_binary_array = bytearray("Hello", "utf-8")
    b64_bytes = base64.b64encode(test_binary_array)
    b64_str = b64_bytes.decode()

    request.photo = b64_str;

    jsonStr = request.model_dump_json(indent=2, exclude_none=True)
    print(jsonStr)

    print('--------------------------------')

    restored = from_json_str(jsonStr)
    print(restored)

