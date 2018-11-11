#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

def menu():
    answer = 0

    print "1. Sound-Sensor-Version"
    print "2. Szenario-Version"
    print "3. Random input-Version"
    print "4. Exit\n"

    options = [1,2,3,4]

    while answer not in options:
        answer = int(raw_input("Press 1, 2, 3 or 4 and hit ENTER: "))

    if answer == 1:
        os.system("coware.py")
        menu()
    elif answer == 2:
        os.system("coware.py")
        print "2"
        menu()
    elif answer == 3:
        os.system("fading.py")
        print "2"
        menu()

menu()
