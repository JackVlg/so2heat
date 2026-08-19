import logging

class SO2HeatResponseProcessor:

    log = None;

    def __init__(self):
        self.log = logging.getLogger("SO2HeatResponseProcessor")
        logging.info("SO2HeatResponseProcessor initialized")

    def process(self, data : str):
        self.log.info("Processing response")
