from picamera2 import Picamera2, Preview
import time
import logging

picam2 = Picamera2()

print("started...")

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

picam2.start()

time.sleep(2)

print("middle...")
picam2.capture_file("image.jpg")
picam2.stop()
print("stopped")
