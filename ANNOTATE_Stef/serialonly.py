import serial
import time

speed = 0 # conveyor speed cm/s
s = [0]
lspeed=[]
Flag=0
material=0
offset=0#3.275 #in cm

ser = serial.Serial('/dev/ttyACM0',115200)


def receive_serial():
    read_serial = ser.readline()
    try:
    	s[0] = str(int(ser.readline(), 32))
    	print(s[0])# print read_serial
        print(read_serial)
    except:
        s[0] = 0
        print("ERROR")
    return s[0]

while 1:
	lspeed=receive_serial()
	time.sleep(0.5)
	#print(lspeed)
    #print(receive_serial())
