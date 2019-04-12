#!/usr/bin/python3
# coding: utf-8

from gpiozero import DistanceSensor
from signal import pause

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)
ultrasonic.threshold_distance = 0.5

def hello():
    print("Hello")

def bye():
    print("Bye")
    
ultrasonic.when_in_range = hello

ultrasonic.when_out_of_range = bye

pause()
