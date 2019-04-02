#!/usr/bin/python3
# coding: utf-8
from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26, pwm=True)

while 1 : 
    leds.on()
    sleep(2)
    leds.off()
    sleep(2)
    leds.value = (1, 0, 1, 0, 1)
    sleep(2)
    leds.value = (0.2, 0.4, 0.6, 0.8, 1.0)
    sleep(2)
    leds.blink()
    sleep(10) 
pass
