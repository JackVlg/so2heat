import requests
import time
import logging
import base64
from requests.exceptions import ConnectTimeout, ConnectionError

from common.so2heat_request import SO2HeatRequest

timeout = 5

def makeRequest() :
    test_binary_array = bytearray("Hello", "utf-8")
    b64 = base64.b64encode(test_binary_array)
    req = SO2HeatRequest(b64)
    result = req.model_dump_json(indent=2, exclude_none=True)
    print("result: ", result)
    return result


while True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = logging.getLogger("main")
    log.info("Next time")

    request = makeRequest()

    try:
        response = requests.post('https://127.0.0.2:8878/api/v1/what-we-will-', json=request, timeout=(4, 3))
    except ConnectTimeout as e:
        log.info("Connection timed out")
        timeout = 5
    except ConnectionError as e:
        log.info("Connection error")
        timeout = 5

    log.info("Sleeping...")
    time.sleep(timeout)

