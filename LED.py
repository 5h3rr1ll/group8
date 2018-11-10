#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

def turn_light_on(color):
    if color == "g":
        print "Green LED on"
        GPIO.output(17,GPIO.HIGH)

light_status = 0

def turn_light_off(color):
    if color == "g":
        print "Green LED off"
        GPIO.output(17,GPIO.LOW)

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
