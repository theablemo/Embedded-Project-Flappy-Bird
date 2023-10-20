#!/usr/bin/python
# coding=utf-8

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
#ads = ADS.ADS1115(i2c)
ads = ADS.ADS1115(address=0x48, i2c=i2c)

# Create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

delayTime = 0.2
Digital_PIN = 24

GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

print("sag")


while True:
    analog = '%.10f' % chan0.voltage
 
    # output to console
    if GPIO.input(Digital_PIN) == False:
        print ("Analog voltage value:", analog, "V, ", "Limit: not yet reached")
    else:
        print ("Analog voltage value:", analog, "V, ", "Limit: reached")
    print ("---------------------------------------")
 
    # reset + delay
    button_pressed = False
    time.sleep(delayTime)
