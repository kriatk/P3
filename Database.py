import sqlite3
import random
import time

file_name='testdb.db'
loop=0
y=0
errorarray=[0,0,0]
ID=1

def writeDB(x,y,STATUS):
    db = sqlite3.connect(file_name) # either create or open database
    cursor = db.cursor()
    cursor.execute('''INSERT INTO errors(X, Y, status) VALUES(?,?,?)''', (x,y, STATUS))
    db.commit()
    print("X:",x,"Y:",y,"Status:",STATUS,"...written into data base")
    #get last row ID
    id = cursor.lastrowid
    print('Last row id: %d' % id)
    db.close()

def readDB(error_ID):
    db = sqlite3.connect(file_name) # either create or open database
    cursor = db.cursor()
    cursor.execute('''SELECT X, Y, status FROM errors WHERE id=?''', (error_ID,))
    error = cursor.fetchone()
    db.commit()
    print(error[0],error[1],error[2])
    #get values outside of function
    errorarray[0]=error[0]
    errorarray[1]=error[1]
    errorarray[2]=error[2]

    db.close()


def updateDB(value, error_ID):
    db = sqlite3.connect(file_name) # either create or open database
    cursor = db.cursor()
    cursor.execute('''UPDATE errors SET status = ? WHERE id = ? ''',(value, error_ID))
    db.commit()
    cursor.execute('''SELECT X, Y, status FROM errors WHERE id=?''', (error_ID,))
    error = cursor.fetchone()
    print(error[0],error[1],error[2])
    db.close()


#connect to or create Data base
db = sqlite3.connect(file_name)
# Get a cursor object
cursor = db.cursor()
#create table errors with input X, Y and Status
cursor.execute('''DROP TABLE IF EXISTS errors''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS errors(id INTEGER PRIMARY KEY, X REAL, Y REAL, status INTEGER) ''')
# update & close
db.commit()
db.close()

#generates list of 10 errors
while loop <100:
    x = random.randint(0, 9)
    y = y+1
    stat = 0 #random.randint(0, 1)
    writeDB(x,y,stat)
    readDB(loop+1)

    loop=loop+1
start = time.clock()
print(start)

speed = 1000/60 # conveyor speed cm/s
while ID<=loop:
    readDB(ID)
    while errorarray[1]-0.5 > (time.clock()-start)*speed:
        1+1
    #Wait and then ACTUATE
    updateDB(1,ID)
    ID=ID+1

