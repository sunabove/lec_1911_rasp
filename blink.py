# coding: utf-8

import time
import RPi.GPIO as GPIO

# Pin definitions
led_pin = 17

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Blink forever
    while True:
        print("+", end = '', flush=True )
        GPIO.output(led_pin, GPIO.HIGH) # Turn LED on
        time.sleep(1)                   # Delay for 1 second
        print("\b", end = '', flush=True)
        print("-", end = '', flush=True)
        GPIO.output(led_pin, GPIO.LOW)  # Turn LED off
        time.sleep(1)                   # Delay for 1 second
        print("\b", end = '', flush=True)
    pass
# 예외 검출
except Exception :
    print( "\nExit program." )
pass