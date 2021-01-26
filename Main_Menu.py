from appJar import gui
import sqlite3
conn = sqlite3.connect("GameDatabase.db")
c = conn.cursor()

win = gui("Login Window", "400x200")
win.setBg("Yellow")
win.setFont(18)
win.addLabel("lb1","Log in")
win.addLabelEntry("Username")
win.addLabelSecretEntry("Password")
win.setFocus("Username")

def press(button):
    if button == "Exit":
        win.stop()
    elif button == "Reset":
        win.clearEntry("Username")
        win.clearEntry("Password")
        win.setFocus("Username")
        
    elif button == "Submit":
        usr = win.getEntry("Username")
        pas = win.getEntry("Password")
        find_user = ('SELECT Password FROM Sensible_Dettails WHERE Username = ? AND Password = ?')
        c.execute(find_user,[(usr),(pas)])
        results = c.fetchall()
        c.close()
        if results:
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
            
    
    elif button == "Registration":
        win.stop()
        import Reg
        
win.addButtons(["Registration"],press)                         
win.addButtons(["Submit","Reset","Exit"],press)
win.go()
