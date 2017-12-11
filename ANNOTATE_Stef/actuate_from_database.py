import sqlite3
import random
import time
import Database
import serial
import spidev
#import write_to_database

#initiate spi & serial
spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 10000000
ser = serial.Serial('/dev/ttyACM0',9600)

#definitions
file_name='errors.db'
db = sqlite3.connect(file_name, timeout=10) # either create or open database
cursor = db.cursor()
#Actuators     =[0x96, 0x5F,0xFF,0xFF, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00]
#ActuatorsOn   =[0x96, 0x5F,0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF]
#ActuatorsOff  =[0x96, 0x5F,0xFF,0xFF, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00]

ActuatorsOn  =[0x96, 0x5F,0xFF,0xFF, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00, 0x00,0x00]
Actuators    =[0x96, 0x5F,0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF]
ActuatorsOff =[0x96, 0x5F,0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF]

error_ID=1

#speed measurement
speed = 0 # conveyor speed cm/s
s = [0]
Flag=0
material=0
offset=0#3.275 #in cm

def receive_serial():
    read_serial = ser.readline()
    try:
        s[0] = str(int(ser.readline(), 16))
        print(s[0])# print read_serial
    except:
        s[0] = 0
        print("ERROR")
    return s[0]

def actuator(cm,state,Actuators) :
    byte1 = 27-2*(10-cm)
    byte2 = 26-2*(10-cm)
    if state is 1:
        Actuators[byte1] = 0x00
        Actuators[byte2] = 0x00
    elif state is 0:
        Actuators[byte1] = 0xFF
        Actuators[byte2] = 0xFF


#check for conveyor speed to be constant (manually by input in keyboard or digitally)

spi.writebytes(ActuatorsOff)

#input speed
while Flag is 0:
	s[0]= receive_serial()
	speed = int(s[0]) & 65535
	time.sleep(0.05)
	# s[0]=receive_serial()
	# speed0=int(s[0]) & 65535
	if speed >= 1000:
		Flag=1
speed=(speed/100)*(100/60) #speed from m/min to cm/s

#check for material
while material is 0:
	s[0]= receive_serial()
	material = int(s[0]) >> 16
	print(material,speed)

start = time.clock()
cursor.execute("SELECT * FROM errors")
c=cursor.fetchall()
db.close()
print(c)
while 1:
    db = sqlite3.connect(file_name, timeout=10) # either create or open database

    cursor = db.cursor()
    cursor.execute('''SELECT X, Y, status FROM errors WHERE id=?''', (error_ID,))
    e = cursor.fetchone()
    db.close()
    while e is None:
        db = sqlite3.connect(file_name, timeout=10) # either create or open database
        print("DB Open")
        cursor = db.cursor()
        cursor.execute('''SELECT X, Y, status FROM errors WHERE id=?''', (error_ID,))
        e = cursor.fetchone()
        #print("waiting fo data")
        db.close()
        print("DB Closed")
        time.sleep(1)

    errors, IDs, a=Database.sort(error_ID,file_name)
    print("actuate at:",a+0.5,"now at:",speed*(time.clock()-start))

    #write actuators into array
    for error in errors:
        actuator(error,1,Actuators)
        print("added error", error)
        print("ActuatorsIn", Actuators)
    print("ActuatorsOut", Actuators)

    #wait for position to actuate
    while speed*(time.clock()-start)+offset <= a+0.5: #+0.5 because we cut the position instead of rounding. when we mark at a and one error lies at a+ >0.5 we are too a away from it
        0
    print(a+0.5,speed*(time.clock()-start),"Print now")
    print(time.clock())
    spi.writebytes(Actuators)
    time.sleep(0.03)
    spi.writebytes(ActuatorsOff)
    print(time.clock())
    print(a+0.5,speed*(time.clock()-start),"marked")

    print(Actuators)

    #reset actuator array
    Actuators     = [0x96, 0x5F,0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF, 0xFF,0xFF]
    print("RESET",Actuators)

    #write status in database (later also time since start, time, date )
    for ID in IDs:
        db = sqlite3.connect(file_name, timeout=10) # either create or open database
        cursor = db.cursor()
        cursor.execute('''UPDATE errors SET status = ? WHERE id = ? ''',(1, ID))
        print("0 to 1 for ID", ID)
        try:
            db.commit()
        except:
            print("CHANGE WAS NOT COMMITTED")
            continue
        db.close()

    #set new ID to look at in database
    error_ID = IDs[-1]+1 #last elemt of array

    #db = sqlite3.connect(file_name) # either create or open database
    #cursor = db.cursor()
    #cursor.execute("SELECT * FROM errors")
    #c=cursor.fetchall()
    #print(c)
