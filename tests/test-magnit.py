import troykahat
from time import sleep

PIN_WP_RELAY = 7

wp = troykahat.wiringpi_io()

wp.pinMode(PIN_WP_RELAY, wp.OUTPUT)

while True:
	wp.digitalWrite(PIN_WP_RELAY, True)
	sleep(2)
	wp.digitalWrite(PIN_WP_RELAY, False)
	sleep(2)
