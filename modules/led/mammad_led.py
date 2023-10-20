from gpiozero import LED #imports the LED functions from gpiozero library

from time import sleep #imports the sleep function from time library

def turn_led_on(channel = 17):
    led = LED(channel)
    led.on()

def turn_led_off(channel = 17):
    led = LED(channel)
    led.off()

def led_func(channel = 17):
    led = LED(channel)
    led.on()
    sleep(3)
    led.off()