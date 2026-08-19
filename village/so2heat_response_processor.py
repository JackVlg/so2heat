import logging

from common.so2heat_response import SO2HeatResponse

class SO2HeatResponseProcessor:

    log = None;

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

    def process(self, data : str):
        self.log.info("Processing response")

        response = SO2HeatResponse.from_json_str(data)
        print(response)