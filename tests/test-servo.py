from gpiozero.pins.pigpio import PiGPIOFactory, pigpio
from time import sleep

MIN_PULSE = 500               # Pulse width for 0 degrees
MAX_PULSE = 2500              # Pulse width for 180 degrees


pinf = PiGPIOFactory()

pi = pigpio.pi() 
if not pi.connected:
    print("Failed to connect to pigpio daemon. Run 'sudo pigpiod' first.")
    exit()
    
def set_servo_angle(gpio, angle):
    # Map angle (0-180) to pulse width (MIN_PULSE to MAX_PULSE)
    pulse_width = MIN_PULSE + (angle / 180.0) * (MAX_PULSE - MIN_PULSE)
    pi.set_servo_pulsewidth(gpio, pulse_width)
    
set_servo_angle(4, 45)
sleep(0.3)
set_servo_angle(4, 0)
sleep(2)


#servo = Servo(4)
#servo.min()
#sleep(2)
#servo.max()
#sleep(2)

