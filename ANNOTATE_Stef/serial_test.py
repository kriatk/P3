import serial
import time
def receive_serial():
    read_serial = ser.readline()
    try:
        s[0] = str(int(ser.readline(), 16))
        print(s[0])


    # print read_serial
    except:
        s[0] = 0
        print("ERROR")
    return s[0]

ser = serial.Serial('/dev/ttyACM0',115200)
s = [0]
Flag = 0
speed=0
speed0=0
material=0

while Flag is 0:
	s[0]= receive_serial()
	speed = int(s[0]) & 65535
	time.sleep(0.05)
	s[0]=receive_serial()
	speed0=int(s[0]) & 65535
	if speed0 <= speed:
		Flag=1

while material is 0:
	s[0]= receive_serial()
	material = int(s[0]) >> 16
	print(s[0])

	print('in mat loop',material)
