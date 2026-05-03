import requests
import time
import random
import json
import base64
import os
from requests.exceptions import ConnectTimeout, ConnectionError

import so2heat_motor
from so2heat_request import SO2HeatRequest, RequestEncoder

timeout = 5

def makeRequest() :
    test_binary_array = bytearray("Hello", "utf-8")
    result = json.dumps(SO2HeatRequest(test_binary_array), indent=4, cls=RequestEncoder)
    print("result: ", result)
    return result


while True:
    print("Next time")

    request = makeRequest()

    try:
        response = requests.post('https://127.0.0.2:8878/api/v1/what-we-will-', json=request, timeout=(4, 3))
    except ConnectTimeout as e:
        print("Connection timed out")

    time.sleep(timeout)

