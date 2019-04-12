#!/usr/bin/python3
# coding: utf-8

from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=17, trigger=4)

while 1 :
    print(ultrasonic.distance)

    