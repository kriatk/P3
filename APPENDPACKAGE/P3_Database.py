import sqlite3
import time
import datetime
import random

i = 1

conn = sqlite3.connect('Final_Database_P3.db')
c = conn.cursor()

Type_Errors = ["Hole", "Scratch", "Bump"]

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Flaw("
          "Flaw_ID INT, "
          "Process_ID INT, "
          "Position_X INT, "
          "Position_Y INT, "
          "Type_Flaw TEXT, "
          "Size_Flaw REAL) ")

    c.execute("CREATE TABLE IF NOT EXISTS Process("
          "Process_ID INT, "
          "Belt_ID INT, "
          "Sheet_ID INT, "
          "Current_Speed REAL, "
          "Time_Date_Process TEXT, "
          "Employee_ID INT)")

    c.execute("CREATE TABLE IF NOT EXISTS Sheet("
          "Sheet_ID INT, "
          "Process_ID INT, "
          "Material TEXT, "
          "Length REAL, "
          "Width REAL, "
          "Depth REAL, "
          "Employee_ID INT)")

    c.execute("CREATE TABLE IF NOT EXISTS Belt("
          "Belt_ID INT, "
          "Max_Speed REAL, "
          "Min_Speed REAL, "
          "Width_Belt REAL, "
          "Employee_ID INT)")

    c.execute("CREATE TABLE IF NOT EXISTS Module("
          "Module_ID INT, "
          "Belt_ID, "
          "Position_On_Belt INT, "
          "Employee_ID INT)")

    c.execute("CREATE TABLE IF NOT EXISTS Markers("
          "Markers_ID INT, "
          "Module_ID INT, "
          "Date_Changed TEXT, "
          "Colour TEXT, "
          "Type_Marker TEXT, "
          "Employee_ID INT)")

    c.execute("CREATE TABLE IF NOT EXISTS Employee_Responsible("
          "Employee_ID INT, "
          "Name TEXT, "
          "Title TEXT, "
          "Phone_Number INT)")

def dynamic_data_entry():
    Flaw_ID = i
    Process_ID = 1
    Belt_ID = 1
    Employee_ID = 1
    Sheet_ID = 1
    Module_ID = 1
    Markers_ID = 1
    Position_X = random.randrange(0,10)
    Position_Y = i
    Type_Flaw = random.choice(Type_Errors)
    Size_Flaw = random.randrange(0,5)
    Current_Speed = 8
    time_stamp = time.time()
    Time_Date_Process = str(datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S'))
    Material = 'Aluminum'
    Length = 10
    Width = 10
    Depth = 0.5
    Max_Speed = 10
    Min_Speed = 6
    Width_Belt = 10
    Position_On_Belt = 1
    Date_Changed = str(datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S'))
    Colour = 'Blue'
    Type_Marker = 'Tusche'
    Name = 'Brian'
    Title = 'Ingineer'
    Phone_Number = 53808710

    c.execute("INSERT INTO Flaw (Flaw_ID,Process_ID,Position_X,Position_Y,Type_Flaw,Size_Flaw) VALUES (?, ?, ?, ?, ?, ?)",
              (Flaw_ID,Process_ID,Position_X,Position_Y,Type_Flaw,Size_Flaw))

    c.execute("INSERT INTO Process (Process_ID,Belt_ID,Sheet_ID,Current_Speed,Time_Date_Process,Employee_ID) VALUES (?, ?, ?, ?, ?, ?)",
              (Process_ID,Belt_ID,Sheet_ID,Current_Speed,Time_Date_Process,Employee_ID,))

    c.execute("INSERT INTO Sheet (Sheet_ID,Process_ID,Material,Length,Width,Depth,Employee_ID) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (Sheet_ID,Process_ID,Material,Length,Width,Depth,Employee_ID))

    c.execute("INSERT INTO Belt (Belt_ID,Max_Speed,Min_Speed,Width_Belt,Employee_ID) VALUES (?, ?, ?, ?, ?)",
              (Belt_ID,Max_Speed,Min_Speed,Width_Belt,Employee_ID))

    c.execute("INSERT INTO Module (Module_ID,Belt_ID,Position_On_Belt,Employee_ID) VALUES (?, ?, ?, ?)",
              (Module_ID,Belt_ID,Position_On_Belt,Employee_ID))

    c.execute("INSERT INTO Markers (Markers_ID,Module_ID,Date_Changed,Colour,Type_Marker,Employee_ID) VALUES (?, ?, ?, ?, ?, ?)",
              (Markers_ID,Module_ID,Date_Changed,Colour,Type_Marker,Employee_ID))

    c.execute("INSERT INTO Employee_Responsible (Employee_ID,Name,Title,Phone_Number) VALUES (?, ?, ?, ?)",
              (Employee_ID,Name,Title,Phone_Number))

    conn.commit()

create_table()

while i < 11:
    dynamic_data_entry()
    i += 1
    time.sleep(1)

c.close
conn.close()
