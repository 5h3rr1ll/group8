#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# red light
GPIO.setup(17,GPIO.OUT)
# green light
GPIO.setup(22,GPIO.OUT)
# blue light
GPIO.setup(24,GPIO.OUT)

def turn_light_on(color):
    if color == "g":
        print "Green LED on"
        GPIO.output(22,GPIO.HIGH)

light_status = 0

def turn_light_off(color):
    if color == "g":
        print "Green LED off"
        GPIO.output(22,GPIO.LOW)

def start(light_status):
    if light_status == 0:
        a = raw_input("Do yu want to turn ligh on? y/n: ")
        if a == "y":
            turn_light_on()
            # return 1
            light_status = 1

        if light_status == 1:
            a = raw_input("Do you want to turn light off? y/n: ")
            if a == "y":
                turn_light_off()
                # return 0
                light_status = 0
                
               
               
# start(light_status)
#
# while True:
#     db = 0

turn_light_on("g")
time.sleep(3)
turn_light_off("g")

# here starts the sound part
#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print "loud Sound Detected!"
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



