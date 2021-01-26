import sqlite3
conn = sqlite3.connect("tutorial.db")
c = conn.cursor()
##Create Students table
##def create_table():
##    c.execute("CREATE TABLE IF NOT EXISTS Students(Name VARCHAR(20) NOT NULL,Surname VARCHAR(20) NOT NULL,Username VARCHAR(20) NOT NULL PRIMARY KEY UNIQUE, Classroom TEXT NOT NULL)")
##create_table()

##Create sensible dettail table
##def create_table1():
##    c.execute("CREATE TABLE `Registration Sensible_Dettails` (`Username`VARCHAR(20) NOT NULL UNIQUE,`Password` TEXT NOT NULL,`Email`TEXT NOT NULL UNIQUE,PRIMARY KEY(`Username`)FOREIGN KEY (Username) REFERENCES Students(Username)")
##create_table1()


##Create Character Stats Table
##def create_table():
##    c.execute("CREATE TABLE IF NOT EXISTS `Character_Stats`(`Username`VARCHAR(20) NOT NULL UNIQUE,`Health`INT NOT NULL,`ATK` INT NOT NULL,`DEF` INT NOT NULL,`AttackPotion` INT NOT NULL,`DefendPotion` INT NOT NULL, PRIMARY KEY(`Username`)FOREIGN KEY (Username) REFERENCES Students(Username))") 
##create_table()


##Insert into students table
##def data_entry():
##    c.execute("INSERT INTO Students VALUES('Simone','Apicella','xXOmegaXx','C35')")
##    conn.commit()
##    c.close()
##    conn.close()
##data_entry()

##Insert into sensible data table
##def data_entry1():
##    c.execute("INSERT INTO Sensible_Dettails VALUES('xxXOmegaXx','Omega3','Simon.Apicella@gmail.com')")
##    conn.commit()
##    c.close()
##    conn.close()
##data_entry1()

##Insert into Character Stats Table
##def data_entry():
##    c.execute("INSERT INTO Character_Stats VALUES(`xXOmegaXx`,`100`,`20`,`5`,`1000`,`1000`)")
##    conn.commit()
##    c.close()
##    conn.close()
##data_entry()







##Reading from Students table
c.execute('SELECT * FROM Students')
rows = c.fetchall()
for row in rows:
    print('{0},{1},{2}'.format(row[0],row[1],row[2]))
conn.commit()
conn.close()










##def login():
##    Username = input("Username:")
##    c.execute('SELECT * FROM Sensible_Dettails WHERE Username = (?)',[Username])
##    rows = c.fetchall()
##    for row in rows:
##        '{0},{1}'.format(row[0],row[1])
##    Password = input("Password:")
##    if Password == row[1]:
##        print("GG")
##    else:
##        print("Username or Password")
##
##def register():
##    Name = input("Name:")
##    Surname = input("Surname:")
##    Username = input("Username:")
##    Classroom = input("Classroom:")
##    Password = input("Password:")
##    Passwordc = input("Repeat you password:")
##    Email = input("Email:")
##    if Password == Password1:
##        c.execute ('INSERT INTO Sensible_Dettails VALUES(?,?,?)',(Username,Password,Email))
##        c.execute ('INSERT INTO Students VALUES(?,?,?,?)',(Name,Surname,Username,Classroom))
##        conn.commit()
##        c.close()
##        conn.close()
##    else:
##        print("Error")
##        return register









##register()

    
