#!/usr/bin/python
# -*- coding:utf-8 -*-
from AlphaBot import AlphaBot
import RPi.GPIO as GPIO
import time

if __name__=='__main__':

    ab = AlphaBot()
    ab.forward()
    ab.backward()
    ab.left()
    ab.right()
    #ab.stop()
    try:
        while True:
            time.sleep(1)
        pass
    except KeyboardInterrupt:
        GPIO.cleanup()
    pass
pass