import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(6, GPIO.OUT) # output rf

# Initial state for LEDs:
print("Testing RF out, Press CTRL+C to exit")

#rfid = SimpleMFRC522()

try:
     print("set GIOP high")
     GPIO.output(6, GPIO.HIGH)
     time.sleep(5)
     #id, text = rfid.read()
     #print(id)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    print("Keyboard interrupt")

except:
    print("some error")

finally:
   print("clean up")
   GPIO.cleanup() # cleanup all GPIO
