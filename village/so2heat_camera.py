import io
import logging
from picamera2 import Picamera2

class SO2HeatCamera():

    camera : Picamera2
    log = None

    def __init__(self):
        log = logging.getLogger("main")

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
    camera = SO2HeatCamera()
    try:
        photo = camera.capture()
        print(type(photo))
    finally:
        camera.stop()
    print("Module test finished")
