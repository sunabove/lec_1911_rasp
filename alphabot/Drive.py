#!/usr/bin/python
# -*- coding:utf-8 -*-
from AlphaBot import AlphaBot
import RPi.GPIO as GPIO 
from time import sleep

if __name__=='__main__':

    ab = AlphaBot()
    # 직진
    ab.forward()
    # 1초 기다림
    sleep( 1 )
    # 후진
    ab.backward()
    # 1초 기다림
    sleep( 1 )
    # 좌회전
    ab.left()
    # 1초 기다림
    sleep( 1 )
    # 우회전
    ab.right()
    # 1초 기다림
    sleep( 1 )
    # 멈춤
    ab.stop()

pass