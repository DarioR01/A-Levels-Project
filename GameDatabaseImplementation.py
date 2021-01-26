import sqlite3
conn=sqlite3.connect("GameDatabase.db")
c=conn.cursor()

##Create Students table
def studentsTable():
    c.execute("CREATE TABLE 'Students'(Name VARCHAR(20) NOT NULL,Surname VARCHAR(20) NOT NULL,Username VARCHAR(20)NOT NULL, Classroom TEXT NOT NULL, PRIMARY KEY(Username));")
    






##Create Sensible_details table
def Sensible_DettailsTable():
    c.execute("CREATE TABLE `Sensible_Dettails` (`Username`VARCHAR(20) NOT NULL,`Password` TEXT NOT NULL,`Email`TEXT NOT NULL UNIQUE,PRIMARY KEY(`Username`)FOREIGN KEY (Username) REFERENCES Students(Username) FOREIGN KEY (Username) REFERENCES Teachers(Username))")








##Create Character_Stats table
def Character_StatsTable():
   c.execute("CREATE TABLE 'Character_Stats' ('Username'VARCHAR(20) NOT NULL, 'CharacterName' VARCHAR(20) NOT NULL, 'Level' INT NOT NULL,'Health' INT NOT NULL, 'Attack' INT NOT NULL, 'Defend' INT NOT NULL, 'HealthPotion' INT NOT NULL, 'AttackPotion' INT NOT NULL, PRIMARY KEY(CharacterName), FOREIGN KEY (Username) REFERENCES Saves(Username))")








##Create Saves Table
def SavesTable():
    c.execute("CREATE TABLE 'Saves' ('EntityID' INTEGER PRIMARY KEY AUTOINCREMENT,'Username'VARCHAR(20) NOT NULL,'EntityName'VARCHAR(20) NOT NULL,'Status' BOOL NOT NULL,'Map' VARCHAR(20) NOT NULL,FOREIGN KEY(Username) REFERENCES Students(Username))")


def ScoresTable():
    c.execute("CREATE TABLE 'Scores' ('Username' VARCHAR(20) PRIMARY KEY, 'Score1' INTEGER, 'Score2' INTEGER, 'Score3' INTEGER, 'Score4' INTEGER, 'Score5' INTEGER, 'Score6' INTEGER, 'Score7' INTEGER, 'Score8' INTEGER, 'Score9' INTEGER, 'Score10' INTEGER, 'Score11' INTEGER, 'Score12' INTEGER, FOREIGN KEY(Username) REFERENCES Students(Username))")


def TeacherTable():
    c.execute("CREATE TABLE 'Teachers'('Username' VARCHAR(20) PRIMARY KEY,Name VARCHAR(20) NOT NULL,Surname VARCHAR(20) NOT NULL)")

ScoresTable()
studentsTable()
TeacherTable()
Sensible_DettailsTable()
Character_StatsTable()
SavesTable()



