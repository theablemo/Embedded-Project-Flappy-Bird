import time
import Adafruit_ADS1x15

# Create an instance of the ADS1115 ADC
ads = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
GAIN = 4

# Set the channel you want to use
channel = 0

while True:
    # Read the voltage level from the channel
    while True:
        try:
            voltage = ads.read_adc(channel, gain=GAIN)
        except Exception:
            continue
        break
    # Convert the ADC value to a voltage level
    voltage = voltage * 1.024 / 32767

    # Convert the voltage to sound intensity
    intensity = (voltage/3.3)*100 # 2.0 is a sample value for max_sound_level_in_volts. Replace with the actual maximum sound level in volts.
    intensity = round(intensity, 2)

    print("Intensity: {}%".format(intensity))
    time.sleep(0.5)
