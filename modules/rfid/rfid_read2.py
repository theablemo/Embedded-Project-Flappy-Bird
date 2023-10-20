import serial

ser = serial.Serial("/dev/ttyS0", 9600)

while True:
    print("hi")
    data = ser.read(12)
    if data:
        print("Tag ID:", data.hex())
