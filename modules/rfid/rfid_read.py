import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)
rfid = SimpleMFRC522()
GPIO.setwarnings(False)
print("kir")
while True:

    try:
        print("kiiiir")
        id, text = rfid.read()
        print(id)
        print("hi")
    #print(text)
    except Exception as e:
        print("error")
    finally:
        GPIO.cleanup()
