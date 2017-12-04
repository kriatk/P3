import serial

ser = serial.Serial('/dev/ttyACM2',9600)
s = [0]
Flag = 0


while Flag is 0:
	read_serial=ser.readline()
	try:
		s[0] = str(int (ser.readline(),16))
		print (s[0])


		#print read_serial
	except:
		s[0]=0
		print("ERROR")
		continue

	speed_mat=int(s[0]) & 1
	print(speed_mat)

