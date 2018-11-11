#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# red light
GPIO.setup(17,GPIO.OUT)
# green light
GPIO.setup(22,GPIO.OUT)
# blue light
GPIO.setup(24,GPIO.OUT)

# just turn white light on
GPIO.output(17,GPIO.HIGH), GPIO.output(22,GPIO.HIGH), GPIO.output(24,GPIO.HIGH)

## here starts the sound part !!

#GPIO SETUP, pin in the pin on th Raspberry Pi, in this case the GPIO 4
pin = 4
GPIO.setmode(GPIO.BCM)
# GPIO.IN means that the Raspberry Pi get's an input instead of giving somethign out
# on that pin
GPIO.setup(pin, GPIO.IN)

def callback(pin):
    if GPIO.input(pin):
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
        for _ in range(10):
                GPIO.output(17,GPIO.HIGH)
                time.sleep(.5)
                GPIO.output(17,GPIO.LOW)
                time.sleep(.5)
                continue

print "second white light"
# just turn white light on
GPIO.output(17,GPIO.HIGH), GPIO.output(22,GPIO.HIGH), GPIO.output(24,GPIO.HIGH)

GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime=100) # let us know when the pin goes High or LOW
GPIO.add_event_callback(pin, callback) # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
	time.sleep(1)
