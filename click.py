# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:22:29 2020

@author: fabia
Click
"""

# Code to check if left or right mouse buttons were pressed
import win32api
import time
from playsound import playsound
import random



state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
scroll_info = win32api.GetKeyState(0x09)
while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    print(scroll_info)

    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
            playsound('click0' + str(random.randint(1,9)) + '.mp3')
        else:
            print('Left Button Released')

    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')
    time.sleep(0.001)