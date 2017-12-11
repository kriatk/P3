import sqlite3
import random
import time
import Database

loop=0
y=0
x=0
file_name='errors.db'

#create table errors with input X, Y and Status
db = sqlite3.connect(file_name)
cursor = db.cursor()
cursor.execute('''DROP TABLE IF EXISTS errors''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS errors(id INTEGER PRIMARY KEY, X REAL, Y REAL, status INTEGER) ''')
# update & close
db.commit()
db.close()

#for i in range(0):
loop=0
while loop is not 10:
    Database.writeDB(file_name,x,y,0)
    print(y,x)
    loop=loop+1
    y=y+1#random.uniform(0.0,2.0)
    #y=round(y,2)
    x=x+1#random.uniform(0.0,10.0)
    #x=round(x,2)

loop=0
while loop is not 10:
    Database.writeDB(file_name,x,y,0)
    print(y,x)
    loop=loop+1
    y=y+1#random.uniform(0.0,2.0)
    #y=round(y,2)
    x=x-1#random.uniform(0.0,10.0)
    #x=round(x,2)

#Database.get_posts('errors.db')
db = sqlite3.connect(file_name) # either create or open database
cursor = db.cursor()
cursor.execute("SELECT * FROM errors")
#print(cursor.fetchall())
c=cursor.fetchall()

print(c[0][0])

