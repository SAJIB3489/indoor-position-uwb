import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
# ACM0 will depend on your USB/UART port port.

while True:
    line = ser.readline().decode('utf-8').strip()
    print(line)
