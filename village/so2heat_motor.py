import logging
import time

import pigpio

# Pin Configuration (using BCM numbering)
# Connect these to your L298N
DIR2_PIN = 24  # Connect to L298N's IN2
PWM_PIN = 25  # Connect to L298N's ENA (a PWM-capable pin)

# Motor Directions
FORWARD = (1, 0)
BACKWARD = (0, 1)
STOP = (0, 0)
BRAKE = (1, 1)

class SO2HeatMotor:
    log = None
    pi = None

    def __init__(self):
        self.log = logging.getLogger("SO2HeatMotor")
        pi = pigpio.pi()  # Connect to local pigpio daemon
        if not pi.connected:
            self.log.info("Failed to connect to pigpio daemon. Run 'sudo pigpiod' first.")
            exit(0)

    def set_motor(self, speed, direction):
        """
        speed: Integer from -100 to 100.
                Positive for forward, negative for backward.
        direction: A tuple like (1,0) or (0,1). This argument is optional
                   if you use speed's sign to determine direction.
        """
        # Set direction pins
        self.pi.write(DIR2_PIN, direction[1])

        # Map speed range (-100 to 100) to duty cycle range (0 to 255)
        # For pigpio's set_PWM_dutycycle, the range is 0-255.
        # 0 = 0% duty cycle (off), 255 = 100% duty cycle (full on).
        duty_cycle = int(abs(speed) / 100.0 * 255)
        self.pi.set_PWM_dutycycle(PWM_PIN, duty_cycle)

    def set_motor_simple(self, speed):
        """Control motor speed and direction with a single integer."""
        if speed > 0:  # Forward
            self.set_motor(speed, FORWARD)
        elif speed < 0:  # Backward
            self.set_motor(speed, BACKWARD)
        else:  # Stop
            self.set_motor(0, STOP)

    def rotate(self, speed, duration):
        self.log.info("rotate {}, {}".format(speed, duration))
        self.set_motor_simple(speed)
        time.sleep(duration)

        self.set_motor_simple(0)
        self.pi.set_PWM_dutycycle(PWM_PIN, 0)

    def stop(self):
        self.set_motor_simple(0)
        self.pi.set_PWM_dutycycle(PWM_PIN, 0)
        self.pi.stop()
        self.log.info("Stopped motor.")