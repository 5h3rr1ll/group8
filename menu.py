#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

def menu():
    answer = 0

    print "1. Sound-Senser-Version"
    print "2. Szenario-Version"
    print "3. Random input-Version\n"

    options = [1,2,3]

    while answer not in options:
        answer = int(raw_input("Press 1, 2 or 3 and hit ENTER: "))

    if answer == 1:
        os.system("python fading.py")
        menu()
    elif answer == 2:
        print "2"
        menu()

menu()
