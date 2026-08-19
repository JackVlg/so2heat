import logging

from common import so2heat_response

class SO2HeatResponseProcessor:

    log = None;

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

    def process(self, data : str):
        self.log.info("Processing response")

        result_hints = {}

        response = so2heat_response.from_json_str(data)

        if response.status == "Ok":
            commands = response.commands
            print(commands)

            if response.nextTimeout is not None:
                result_hints["NEXT_TIMEOUT"] = response.nextTimeout

        return result_hints