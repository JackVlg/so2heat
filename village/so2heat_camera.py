import io

from picamera2 import Picamera2

class SO2HeatCamera():

    camera : Picamera2

    def __init__(self):
        self.camera = Picamera2()
        print("Camera created")

        camera_config = self.camera.create_preview_configuration()
        self.camera.configure(camera_config)
        print("Camera configured")

        self.camera.start()
        print("Camera started")

    def capture(self):
        buffer = io.BytesIO()
        self.camera.capture_buffer(buffer, format='jpeg')
        return buffer.getvalue()

    def stop(self):
        self.camera.stop()
        print("Camera stopped")

if __name__ == "__main__":
    camera = SO2HeatCamera()
    try:
        photo = camera.capture()
        print(type(photo))
    finally:
        camera.stop()
    print("Module test finished")
