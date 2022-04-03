#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# LEDS
led1 = 2
led2 = 3
led3 = 4
led4 = 14
led5 = 15
led6 = 17
led7 = 18
led8 = 27
led9 = 22
led10 = 23
led11 = 24
led12 = 10

#PUSH BUTTONS
btn1 = 9
btn2 = 25
btn3 = 11
btn4 = 7
btn5 = 5
btn6 = 6
btn7 = 12
btn8 = 13
btn9 = 19
btn10 = 16
btn11 = 26
btn12 = 20


allLeds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10, led11, led12]
allPushBtns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12]
pressed = []


def init():
	for i in range(len(allLeds)):
		GPIO.setup(allLeds[i], GPIO.OUT)
		GPIO.setup(allPushBtns[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)


def switchOffAll():
	for i in allLeds:
		GPIO.output(i, GPIO.LOW)


def switchOnAll():
	for i in allLeds:
		GPIO.output(i, GPIO.HIGH)


def test_switches():
	global pressed

	print("Testing switches:")
	for i in range(len(allLeds)):
		if not GPIO.input(allPushBtns[i]):
			print("    Switch {} is pressed on pin {}.".format(i, allPushBtns[i]))
			pressed.append(i)


def blink_pressed():
	for i in pressed:
		GPIO.output(allLeds[i], GPIO.HIGH)


init()

switchOnAll()
time.sleep(1)
switchOffAll()
test_switches()
for t in range(0, 5):
	blink_pressed()
	time.sleep(1)
	switchOffAll()
	time.sleep(1)

GPIO.cleanup()
