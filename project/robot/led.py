# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO

LED1 = 16
LED2 = 20

class LED:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED1, GPIO.OUT)
        GPIO.setup(LED2, GPIO.OUT)
    def lighting(self, n, t):     # n:何回 t:何秒 点灯
        for i in range(n):
            GPIO.output(LED1, GPIO.HIGH)
            GPIO.output(LED2, GPIO.HIGH)
            time.sleep(t)
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW)
            time.sleep(t)
