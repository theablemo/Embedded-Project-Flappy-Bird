#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def setup_sound(channel: int):
    #GPIO SETUP
    #channel = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)

#def callback(channel):
 #   if GPIO.input(channel):
  #      print ("Sound Detected!")
   # else:
    #    print ("Sound Detected!")
def detect_sound(callback, channel):
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

def cleanup_sound():
    pass
# infinite loop
#while True:
 #       time.sleep(1)
