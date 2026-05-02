import requests
import time
from requests.exceptions import ConnectTimeout, ConnectionError

import so2heat_motor
from so2heat_request import SO2HeatRequest

timeout = 5

def makeRequest() :
    result = SO2HeatRequest()

while True:
    print("Next time")

    request = makeRequest();

    try:
        response = requests.post('https://jackvlg.ru:8878/api/v1/', json=request, timeout=(4, 3))
    except ConnectTimeout as e:
        print("Connection timed out")

    time.sleep(timeout)

