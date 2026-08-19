import sys

import requests
import time
import logging
import base64
from requests.exceptions import ConnectTimeout, ConnectionError
from urllib3.exceptions import ReadTimeoutError

from common.so2heat_request import SO2HeatRequest
from village.so2heat_camera import SO2HeatCamera
from village.so2heat_response_processor import SO2HeatResponseProcessor

timeout = 0.5

camera : SO2HeatCamera
response_processor : SO2HeatResponseProcessor

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
response_processor = SO2HeatResponseProcessor()

try:
    while True:
        log.info("Next time")

        request = makeRequest()

        try:
            response = requests.post(home_url + '/api/v1/update-status', headers={'Content-Type': 'application/json'}, data=request, timeout=(4, 3), verify=False)
            response.raise_for_status()
            text_body = response.text
            response_hints : dict = response_processor.process(text_body)

            timeout = 1
        except ConnectTimeout as e:
            log.info("Connection timed out")
            timeout = 5
        except ConnectionError as e:
            log.info("Connection error")
            log.info(e)
            timeout = 5
        except ReadTimeoutError as e:
            log.info("Read timeout error")
            timeout = 5
        except requests.exceptions.ReadTimeout as e:
            log.info("Read timeout")
            timeout = 5

        log.info("Sleeping...")
        time.sleep(timeout)
finally:
    camera.stop()
