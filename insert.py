import sqlite3
conn=sqlite3.connect('Mitmorning.db')
print("Open database Succesfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'HarlemSAiNt',19,'eMobilis','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'Oso Arrogant',22,'Strathmore','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3,'Harry Pac',26,'K.U','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'Millier Nila',28,'Loretto','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5,'Elmad Jerkins',34,'JKUAT','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'Spongebob Squarepants',12,'Krusty Crab','Male')")
#saving it
conn.commit()
print("Records added successfully")
conn.close()

