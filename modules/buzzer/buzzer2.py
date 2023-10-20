from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(24)

#while True:
#    print(buzzer)
#    buzzer.beep()

def buz(time: int):


    buzzer.on()
    sleep(time)
    buzzer.off()

