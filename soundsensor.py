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
GPIO.output(17,GPIO.HIGH), GPIO.output(22,GPIO.HIGH), GPIO.output(24,GPIO.HIGH)

# just turn white light on
os.system("")

## here starts the sound part
#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print "It's gettign to noisy!"
        # white light goes off
        GPIO.output(17,GPIO.LOW), GPIO.output(22,GPIO.LOW), GPIO.output(24,GPIO.LOW)
        #yellow light light up
        os.system("pigs p 17 255")
        os.system("pigs p 22 80")
        time.sleep(5)
        print("Way to loud!")
        # turn yellow light off
        os.system("pigs p 17 0")
        os.system("pigs p 22 0")
        for _ in range(5):
                GPIO.output(22,GPIO.HIGH)
                GPIO.output(22,GPIO.LOW)
                return


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100) # let us know when the pin goes High or LOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
	time.sleep(1)
