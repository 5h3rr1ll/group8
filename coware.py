 #!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
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

def lightCheck():
    print"GREEN Light"
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    print"RED Light"
    GPIO.output(22,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(22,GPIO.LOW)
    print"BLUE Light"
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(24,GPIO.LOW)

def menu():
    answer = 0

    print "1. Sound-Sensor-Version"
    print "2. Funny colores"
    print "3. Exit\n"

    options = [1,2,3,4]

    while answer not in options:
        answer = int(raw_input("Press 1, 2, 3 or 4 and hit ENTER: "))

    if answer == 1:
        os.system("python soundsensor.py")
        menu()
    elif answer == 2:
        os.system("python fading.py")
        menu()
    elif answer == 3:
        return


lightCheck()
menu()
