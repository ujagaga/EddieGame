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
btn1 = 8
btn2 = 25
btn3 = 11
btn4 = 7
btn5 = 5
btn6 = 6
btn7 = 12
btn8 = 13
btn9 = 19
btn10 = 21
btn11 = 26
btn12 = 20


allLeds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10, led11, led12]
allPushBtns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12]
pinMap = [27, 1, 3, 5, 7, 29, 31, 7, 24, 21, 19, 23, 32, 33, 8, 10, 36, 11, 12, 35, 38, 40, 15, 16, 18, 22, 37, 13]


def init():
	for i in range(len(allLeds)):
		GPIO.setup(allLeds[i], GPIO.OUT)
		GPIO.setup(allPushBtns[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)


def test_switches():
	for i in range(len(allPushBtns)):
		if not GPIO.input(allPushBtns[i]):
			print("\tSwitch {} is pressed on GPIO {} (Board pin {}).".format(i + 1, allPushBtns[i], pinMap[allPushBtns[i]]))
			return i
	return -1


init()
print("Will now light up one LED at a time. Press the button which lights up.")
for i in range(len(allLeds)):
	print("LED {} on GPIO {} (Board pin {})".format(i + 1, allLeds[i], pinMap[allLeds[i]]))
	GPIO.output(allLeds[i], GPIO.HIGH)
	while test_switches() < 0:
		time.sleep(0.1)

	GPIO.output(allLeds[i], GPIO.LOW)

	time.sleep(1)
	while test_switches() >= 0:
		time.sleep(0.3)

GPIO.cleanup()
