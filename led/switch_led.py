#!/usr/bin/python3
# coding: utf-8

from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

while True:
    print( "Press the switch button, please!" )
    button.wait_for_press()
    print( "You have pushed me" )
    led.toggle()
    sleep(0.5)
pass
