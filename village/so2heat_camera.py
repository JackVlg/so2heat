import io
import logging
from picamera2 import Picamera2

class SO2HeatCamera():

    camera : Picamera2
    log = None

    def __init__(self):
        #Picamera2.set_logging(level=Picamera2.INFO, msg='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.log = logging.getLogger("main")

        self.camera = Picamera2()
        self.log.info("Camera created")

        camera_config = self.camera.create_preview_configuration()
        self.camera.configure(camera_config)
        self.log.info("Camera configured")

        self.camera.start()
        self.log.info("Camera started")

    def capture(self):
        buffer = io.BytesIO()
        self.camera.capture_file(buffer, format='jpeg')
        return buffer.getvalue()

    def stop(self):
        self.camera.stop()
        self.log.info("Camera stopped")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = logging.getLogger("main")

    camera = SO2HeatCamera()
    try:
        photo = camera.capture()
        log.info(type(photo))
    finally:
        camera.stop()
    log.info("Module test finished")
