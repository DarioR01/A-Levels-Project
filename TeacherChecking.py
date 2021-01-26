import sqlite3
from appJar import gui

win = gui("Register", "800x600")
win.setBg("Teal")
#win.setBg("Yellow")
win.setFont(18)

def start():
    win.removeAllWidgets()
    win.addLabel("lb1","Welcome")
    win.addButtons(["Students Search"],press)
    win.addButtons(["Scores Search"],press)
    win.addButtons(["Change A student Score"],press)
    win.addButtons(["Exit"],press)

def StudentsSearch():
    win.removeAllWidgets()
    win.addLabel("lb1","Add Informations")
    win.addLabelEntry("Username")
    win.addLabelEntry("Name")
    win.addLabelEntry("Surname")
    win.addLabelEntry("Class")
    win.addButtons(["Submit","Back","Exit"],pressStudentSearch)


    
def ScoresSearch():
    win.removeAllWidgets()
    win.addLabelEntry("Times Tables")
    win.addLabelEntry("Specific Score")
    win.addLabelEntry("Lower Than")
    win.addLabelEntry("More Than")
    win.addButtons(["Submit","Back","Exit"],pressScoreSearch)


    
def ChangeScore():
    win.removeAllWidgets()
    win.addLabelEntry("By Username")
    win.addLabelEntry("By Classroom")
    win.addLabelEntry("Times Tables")
    win.addLabelEntry("Score To Insert")
    win.addButtons(["Submit","Back","Exit"],pressChangeScore)


    
def press(button):
    if button=="Exit":
        win.stop()
    elif button=="Students Search":
        StudentsSearch()
    elif button=="Scores Search":
        ScoresSearch()
    elif button=="Change A student Score":
        ChangeScore()


def pressStudentSearch(button):
    if button=="Exit":
        win.stop()
    elif button=="Back":
        start()
    elif button=="Submit":
        Username=win.getEntry("Username")
        Name=win.getEntry("Name")
        Surname=win.getEntry("Surname")
        Class=win.getEntry("Class")
        Information=[["Username",Username],["Name",Name],["Surname",Surname],["Classroom",Class]]
        Code="SELECT * FROM Students WHERE"
        x=0
        if Username=="" and Class=="" and Surname=="" and Name=="":
            win.infoBox("Error","No constraints given")
        else:
            while True:
                if len(Information)-1<x:
                    break
                elif Information[x][1]=="":
                    del Information[x]
                    x-=1
                x+=1
            conn = sqlite3.connect("GameDatabase.db")
            t = conn.cursor()
            if len(Information)-1==0:
                z=Information[0][0]
                c=Information[0][1]
                Code='SELECT * FROM Students WHERE'+' '+z+'=="'+c+'"'
            else:
                for y in range(len(Information)):
                    if y<len(Information)-1:
                        z=Information[y][0]
                        c=Information[y][1]
                        Code=Code+' '+z+'=="'+c+'"'+' AND'
                    else:
                        z=Information[y][0]
                        c=Information[y][1]
                        Code=Code+' '+z+'=="'+c+'"'
            t.execute(Code)
            results=t.fetchall()
            t.close()
            conn.close()
            print(results)
            if len(results)==0:
                win.infoBox("Error","No User matches the constraints given")
        
        
def pressScoreSearch(button):
    if button=="Exit":
        win.stop()
    elif button=="Back":
        start()
    elif button=="Submit":
        Error=False
        conn = sqlite3.connect("GameDatabase.db")
        c = conn.cursor()
        TimesTables=win.getEntry("Times Tables")
        SpecificScore=win.getEntry("Specific Score")
        LowerScore=win.getEntry("Lower Than")
        UpperScore=win.getEntry("More Than")
        Column='Score'+TimesTables
        if TimesTables=="" or int(TimesTables)<1 or int(TimesTables)>12:
             win.infoBox("Error","This timetable does not exists")
             Error=True
        if SpecificScore=="" and LowerScore=="" and UpperScore=="" and Error!=True:
            win.infoBox("Error","At least 1 constrain has to be given")
        if SpecificScore!="" and Error!=True:
            c.execute('SELECT Username FROM Scores WHERE '+Column+'==?',(SpecificScore,))
            Username=c.fetchall()
            for x in range(len(Username)):
                c.execute('SELECT * FROM Students WHERE Username==?',(Username[x]))
                results=c.fetchall()
                print(results)
        if LowerScore!="" and Error!=True:
            c.execute('SELECT Username FROM Scores WHERE '+Column+'<?',(LowerScore,))
            Username=c.fetchall()
            for x in range(len(Username)):
                c.execute('SELECT * FROM Students WHERE Username==?',(Username[x]))
                results=c.fetchall()
                print(results)
        if UpperScore!="" and Error!=True:
            c.execute('SELECT Username FROM Scores WHERE '+Column+'>?',(UpperScore,))
            Username=c.fetchall()
            for x in range(len(Username)):
                c.execute('SELECT * FROM Students WHERE Username==?',(Username[x]))
                results=c.fetchall()
                print(results)
        c.close()
        conn.close()



def pressChangeScore(button):
    if button=="Exit":
        win.stop()
    elif button=="Back":
        start()
    elif button=="Submit":
        Error=False
        Username=win.getEntry("By Username")
        Classroom=win.getEntry("By Classroom")
        TimesTables=win.getEntry("Times Tables")
        Score=win.getEntry("Score To Insert")
        Column="Score"+TimesTables
        if Username=="" or TimesTables=="" or Score=="":
             win.infoBox("Error","Give all the input required")
        elif int(TimesTables)<1 or int(TimesTables)>12:
            win.infoBox("Error","No such TimesTable")
            Error=True
        if Username!="" and Error!=True:
            conn = sqlite3.connect("GameDatabase.db")
            c = conn.cursor()
            c.execute('SELECT Username FROM Students WHERE Username==?',(Username,))
            User=c.fetchall()
            if len(User)!=0:
                c.execute('UPDATE Scores SET '+Column+'==? WHERE Username==?',(Score,Username))
                conn.commit()
                c.close()
                conn.close()
                win.infoBox("Change","The change have been successfull")
            else:
                win.infoBox("Error","The Given Username was not found")
        if Classroom!="" and Error!=True:
            conn = sqlite3.connect("GameDatabase.db")
            c = conn.cursor()
            c.execute('SELECT Username FROM Students WHERE Classroom==?',(Classroom,))
            Username=c.fetchall()
            c.close()
            conn.close()
            if len(Username)!=0:  
                for x in range(len(Username)):
                    conn = sqlite3.connect("GameDatabase.db")
                    c = conn.cursor()
                    c.execute('UPDATE Scores SET '+Column+'=='+Score+' WHERE Username==?',(Username[x]))
                    conn.commit()
                    c.close()
                    conn.close()
                win.infoBox("Change","The change have been successfull")
            else:
                win.infoBox("Error","Class Not Found")




    
    
start()
win.go()
