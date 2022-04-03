#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) < 2:
	sys.exit("Usage:\n\t{} <GPIO pin number>\n\nE.G. {} 21".format(sys.argv[0], sys.argv[0]))
try:
	gpio_number = int(sys.argv[1])
	print("Blinking pin ", gpio_number)
except Exception as e:
	print("Wrong pin number: {}.".format(sys.argv[1]))

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio_number, GPIO.OUT)

for i in range(0, 5):
	GPIO.output(gpio_number, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(gpio_number, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
