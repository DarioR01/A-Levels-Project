import sqlite3
from Scripts.NPCClass import*
from Scripts.Items import*
from appJar import gui


win = gui("Register", "800x600")
#win.setBg("SteelBlue")
win.setBg("Yellow")
win.setImageLocation("Graphics")
win.setFont(18)
TeacherCode="1234"
def start():
    win.removeAllWidgets()
    win.addLabel("lb1","Welcome")
    win.addButtons(["Login","Registration","Exit"],press)


##Registration
def Registration():
    win.removeAllWidgets()
    win.addLabel("lb2","Who are You?")
    win.addButtons(["Student","Teacher"],pressReg)
    win.addButtons(["Exit","Back"],pressReg)





def StudentLog():
    win.removeAllWidgets()
    win.addLabel("lb2","All Fields are compulsory")
    win.addLabelEntry("Username")
    win.addLabelEntry("Name")
    win.addLabelEntry("Surname")
    win.addLabelEntry("Email")
    win.addLabelEntry("Password")
    win.addLabelEntry("Repeat password")
    win.addLabelEntry("CharacterName")
    Classroom = win.addLabelEntry("Classroom")
    win.addButtons(["Submit","Back","Exit"],pressRegS)


    
def TeacherLog():
    win.removeAllWidgets()
    win.addLabel("lb2","All Fields are compulsory")
    win.addLabelEntry("Username")
    win.addLabelEntry("Name")
    win.addLabelEntry("Surname")
    win.addLabelEntry("Email")
    win.addLabelEntry("Password")
    win.addLabelEntry("Repeat password")
    win.addLabelEntry("Teacher Code")
    win.addButtons(["Submit","Back","Exit"],pressRegT)




def press(button):
    if button == "Exit":
        win.stop()
    elif button=="Login":
        Login()
    elif button=="Registration":
        Registration()

def pressReg(button):
    if button == "Exit":
        win.stop()
    elif button == "Back":
        start()
    elif button == "Student":
        StudentLog()
    elif button == "Teacher":
        TeacherLog()
    
def pressRegS(button):
    if button == "Exit":
        win.stop()
    elif button=="Back":
        Registration()
    elif button=="Submit":
        Username = win.getEntry("Username")
        Name = win.getEntry("Name")
        Surname = win.getEntry("Surname")
        Email = win.getEntry("Email")
        Password = win.getEntry("Password")
        Password1 = win.getEntry("Repeat password")
        Classroom = win.getEntry("Classroom")
        CharacterName= win.getEntry("CharacterName")
        Level=1
        Health = 100
        ATK = 20
        DEF = 5
        AttackPotion=0
        DefendPotion=0
        if Password == Password1:
            conn = sqlite3.connect("GameDatabase.db")
            c = conn.cursor()
            c.execute ('INSERT INTO Sensible_Dettails VALUES(?,?,?)',(Username,Password,Email))
            c.execute ('INSERT INTO Students VALUES(?,?,?,?)',(Name,Surname,Username,Classroom))
            c.execute ('INSERT INTO Character_Stats VALUES(?,?,?,?,?,?,?,?)',(Username,CharacterName,Level,Health,ATK,DEF,DefendPotion,AttackPotion))

            c.execute ('INSERT INTO Scores VALUES(?,0,0,0,0,0,0,0,0,0,0,0,0)',(Username,))
                        
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,CharacterName,"1","Prova.map"))
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,npcFight.name,npcFight.Alive,npcFight.mapping))
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,npcSpeech.name,npcSpeech.Alive,npcSpeech.mapping))
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,npcChallenge.name,npcChallenge.Alive,npcChallenge.mapping))

            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,ItemHealth.name,ItemHealth.Taken,ItemHealth.mapping))
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,ItemAttack.name,ItemAttack.Taken,ItemAttack.mapping))
            c.execute ('INSERT INTO Saves (Username,EntityName,Status,Map)VALUES(?,?,?,?)',(Username,Door1.name,Door1.Taken,Door1.mapping))
            
            conn.commit()
            c.close()
            conn.close()
            Login()
        else:
            win.infoBox("Error","Data Inputted invalid try again")
            return press
            
        
def pressRegT(button):
    if button == "Exit":
        win.stop()
    elif button=="Back":
        Registration()
    elif button=="Submit":
        Username = win.getEntry("Username")
        Name = win.getEntry("Name")
        Surname = win.getEntry("Surname")
        Email = win.getEntry("Email")
        Password = win.getEntry("Password")
        Password1 = win.getEntry("Repeat password")
        SubmittedCode = win.getEntry("Teacher Code")
        if Password == Password1 and TeacherCode==SubmittedCode:
            conn = sqlite3.connect("GameDatabase.db")
            c = conn.cursor()
            c.execute ('INSERT INTO Teachers VALUES(?,?,?)',(Username,Name,Surname))
            c.execute ('INSERT INTO Sensible_Dettails VALUES(?,?,?)',(Username,Password,Email))
            
            conn.commit()
            c.close()
            conn.close()
            Login()
        else:
            win.infoBox("Error","Data Inputted invalid try again")
            return press
        



##Login
def Login():
    win.removeAllWidgets()
    win.addLabel("lb1","Log in")
    win.addLabelEntry("Username")
    win.addLabelSecretEntry("Password")
    win.addButtons(["Registration","Submit","Exit"],pressLog)
    
def pressLog(button):
    if button == "Exit":
        win.stop()
    elif button =="Registration":
        Registration()
    elif button == "Submit":
        usr = win.getEntry("Username")
        pas = win.getEntry("Password")
        conn = sqlite3.connect("GameDatabase.db")
        c = conn.cursor()
        find_user = ('SELECT Password FROM Sensible_Dettails WHERE Username = ? AND Password = ?')
        c.execute(find_user,[(usr),(pas)])
        results = c.fetchall()
        find_role = ('SELECT Username FROM Teachers WHERE Username= ?')
        c.execute(find_role,[(usr)])
        Roleresults=c.fetchall()
        if len(Roleresults)==1:
             for i in results:
                win.stop()
                import TeacherChecking
        elif results:
            for i in results:
                win.stop()
                LogUser=usr
                file=open("LogUser.txt","w")
                file.write(LogUser)
                file.close()
                import RPGGame
                
            
        else:
            win.infoBox("Error","Invalid Username or Password")
            win.setFocus("Username")    
        
start()
win.go()
