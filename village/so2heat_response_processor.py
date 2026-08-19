import logging

from common import so2heat_response

class SO2HeatResponseProcessor:

    log = None;

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

    def process(self, data : str):
        self.log.info("Processing response")

        response = so2heat_response.from_json_str(data)
        print(response)