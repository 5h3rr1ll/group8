#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time
from coware import lightCheck
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# red light
GPIO.setup(17,GPIO.OUT)
# green light
GPIO.setup(22,GPIO.OUT)
# blue light
GPIO.setup(24,GPIO.OUT)

# define white light
whiteOn =     GPIO.output(17,GPIO.HIGH), GPIO.output(22,GPIO.HIGH), GPIO.output(24,GPIO.HIGH)
whiteOff = GPIO.output(17,GPIO.LOW), GPIO.output(22,GPIO.LOW), GPIO.output(24,GPIO.LOW)
# just turn white light on
os.system("")

## here starts the sound part
#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print chanell
		GPIO.output(17,GPIO.LOW)
		GPIO.output(22,GPIO.HIGH)
	else:
		print "medium Sound Detected!2"
		GPIO.output(22,GPIO.LOW)
		GPIO.output(17,GPIO.HIGH)


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100) # let us know when the pin goes High or LOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
	time.sleep(1)
