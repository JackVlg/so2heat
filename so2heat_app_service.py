import requests
import time
import json
import logging
from requests.exceptions import ConnectTimeout, ConnectionError

from so2heat_request import SO2HeatRequest, RequestEncoder

timeout = 5

def makeRequest() :
    test_binary_array = bytearray("Hello", "utf-8")
    result = json.dumps(SO2HeatRequest(test_binary_array), indent=4, cls=RequestEncoder)
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

