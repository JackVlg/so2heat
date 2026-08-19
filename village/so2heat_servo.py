import logging
from time import sleep
import pigpio

MIN_PULSE = 500               # Pulse width for 0 degrees
MAX_PULSE = 2500              # Pulse width for 180 degrees

class SO2HeatServo :

    log = None
    pi = None

    def __init__(self):
        self.log = logging.getLogger("SO2HeatServo")
        self.pi = pigpio.pi()  # Connect to local pigpio daemon
        if not self.pi.connected:
            self.log.info("Failed to connect to pigpio daemon. Run 'sudo pigpiod' first.")
            exit(0)

    def set_servo_angle(self, gpio, angle):
        # Map angle (0-180) to pulse width (MIN_PULSE to MAX_PULSE)
        pulse_width = MIN_PULSE + (angle / 180.0) * (MAX_PULSE - MIN_PULSE)
        self.pi.set_servo_pulsewidth(gpio, pulse_width)

    def press_button(self, angle):
        self.log.info("Press button at angle {}".format(angle))
        self.set_servo_angle(4, angle)
        self.set_servo_angle(4, 0)

    def stop(self):
        self.pi.stop()
        self.log.info("Stopped servo.")