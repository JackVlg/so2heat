import troykahat
from time import sleep

PIN_WP_MOTOR_SPEED = 6
PIN_WP_MOTOR_DIR = 5

wp = troykahat.wiringpi_io()

wp.pinMode(PIN_WP_MOTOR_SPEED, wp.OUTPUT)
wp.pinMode(PIN_WP_MOTOR_DIR, wp.OUTPUT)

wp.digitalWrite(PIN_WP_MOTOR_SPEED, True)
wp.digitalWrite(PIN_WP_MOTOR_DIR, True)
sleep(2)

wp.digitalWrite(PIN_WP_MOTOR_SPEED, True)
wp.digitalWrite(PIN_WP_MOTOR_DIR, False)
sleep(2)

wp.digitalWrite(PIN_WP_MOTOR_SPEED, False)
wp.digitalWrite(PIN_WP_MOTOR_DIR, False)
