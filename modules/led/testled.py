from gpiozero import LED #imports the LED functions from gpiozero library

from time import sleep #imports the sleep function from time library

led = LED(17)
led.on()
sleep(4)
led.off()