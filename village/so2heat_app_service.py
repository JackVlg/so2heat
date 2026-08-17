import sys

import requests
import time
import logging
import base64
from requests.exceptions import ConnectTimeout, ConnectionError
from common.so2heat_request import SO2HeatRequest
from village.so2heat_camera import SO2HeatCamera

timeout = 5

camera : SO2HeatCamera

def makeRequest() :
    global camera
    photo = camera.capture()
    b64 = base64.b64encode(photo)
    req = SO2HeatRequest()
    req.photo = b64.decode()
    result = req.model_dump_json(indent=2, exclude_none=True)
    return result

# START

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger("main")

home_url = sys.argv[1]
log.info("Home url is {}".format(home_url))

camera = SO2HeatCamera()

try:
    while True:
        log.info("Next time")

        request = makeRequest()
        print(type(request))

        try:
            response = requests.post(home_url + '/api/v1/update-status', headers={'Content-Type': 'application/json'}, data=request, timeout=(4, 3))
        except ConnectTimeout as e:
            log.info("Connection timed out")
            timeout = 5
        except ConnectionError as e:
            log.info("Connection error")
            timeout = 5

        log.info("Sleeping...")
        time.sleep(timeout)
finally:
    camera.stop()
