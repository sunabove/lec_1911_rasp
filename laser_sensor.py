#!/usr/bin/python3
# coding: utf-8

from gpiozero import *
from time import sleep

sensor = MotionSensor( 16 )

idx = 0 ; 
while 1 :
    idx += 1 
    print( "[%03d] : Waiting for motion ..." % idx )
    sensor.wait_for_motion()
    print( "[%03d] : It's light! :)" % idx  ) 
    sleep( 2 )
pass
