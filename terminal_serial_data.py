import serial

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
