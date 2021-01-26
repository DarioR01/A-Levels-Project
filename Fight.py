import pygame, random, math, time,sqlite3
from Scripts.Globals import *
from Scripts.Items import*
from Scripts.Buttons import *
from Scripts.Colors import *
from Scripts.NPCClass import *


conn=sqlite3.connect("GameDatabase.db")
c=conn.cursor()
DataUser=c.execute('SELECT * FROM Character_Stats WHERE Username=(?)',(Globals.LogUser,))
rows=c.fetchall()
pygame.init()

myhealth= int(rows[0][3])
myatk=int(rows[0][4])
mydefe=int(rows[0][5])
AttackPotionNumber=int(rows[0][6])
DefendPotionNumber=int(rows[0][7])

##Get from database
ScoreUser=c.execute('SELECT * FROM Scores WHERE Username=(?)',(Globals.LogUser,))
AllScore=c.fetchall()
print(AllScore)
Score1=int(AllScore[0][2])
Score2=int(AllScore[0][2])
Score3=int(AllScore[0][3])
Score4=int(AllScore[0][4])
Score5=int(AllScore[0][5])
Score6=int(AllScore[0][6])
Score7=int(AllScore[0][7])
Score8=int(AllScore[0][8])
Score9=int(AllScore[0][9])
Score10=int(AllScore[0][10])
Score11=int(AllScore[0][11])
Score12=int(AllScore[0][12])

aihealth=Globals.aihealth
aiatk=Globals.aiatk
aidefe=Globals.aidefe


font=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
Bigfont=pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",40)
Plus=font.render("+",True,Color.Green)
Minus=font.render("-", True, Color.Red)
RunnedOutPot=font.render("Runned Out",True,Color.Red)


#Musics and Sounds
#pygame.mixer.music.load("Sounds\\MarchOfTheMoa.mp3")
#pygame.mixer.music.play(-1)

def Punch():
    Punch= pygame.mixer.Sound("Sounds//Punch.wav")
    pygame.mixer.Sound.play(Punch)





#Main Loop Inplementation
def showHP():
    displayDefend=font.render(("Heal: "+str(mydefe)),True,Color.Green)
    displayAttack=font.render(("Attack: "+str(myatk)),True,Color.Red)
    Hp=font.render("HP: ",True,Color.Goldenrod)
    HealthDisplay=font.render(str(aihealth),True,Color.Goldenrod)
    MyHealthDisplay=font.render(str(myhealth),True,Color.Goldenrod)
    win.blit(Hp,(window_width/8-50,window_height/12))
    win.blit(Hp,(window_width*7/8-50,window_height*1/3))
    win.blit(HealthDisplay,(window_width/8,window_height/12))
    win.blit(MyHealthDisplay,(window_width*7/8,window_height*1/3))
    win.blit(displayAttack,(window_width*23/32,0))
    win.blit(displayDefend,(window_width*7/8,0))
    
    
def showquestion():
    factor1=Bigfont.render(str(Number1),True,Color.Goldenrod)
    factor2=Bigfont.render(str(Number2),True,Color.Goldenrod)
    Times=Bigfont.render(" X ",True,Color.Goldenrod)
    win.blit(factor1,(window_width/2-50,window_height/2))
    win.blit(Times,(window_width/2,window_height/2))
    win.blit(factor2,(window_width/2+50,window_height/2))
    
def DamageHPMe():
    DamageHPMe= font.render(str(aiatk),True,Color.Red)
    win.blit(DamageHPMe,(window_width*7/8+50,window_height*1/3))
    win.blit(Minus,(window_width*7/8+40,window_height*1/3))
def DamageHPAI():
    DamageHPAI= font.render(str(myatk),True,Color.Red)
    win.blit(Minus,(window_width/8+40,window_height/12))
    win.blit(DamageHPAI,(window_width/8+50,window_height/12))

    
def HealHPMe():
    HealME=font.render(str(mydefe),True,Color.Green)
    win.blit(HealME,(window_width*7/8+60,window_height*1/3))
    win.blit(Plus,(window_width*7/8+40,window_height*1/3))    
def HealHPAI():
    HealAI= font.render(str(aidefe),True,Color.Green)
    win.blit(HealAI,(window_width/8+60,window_height/12))
    win.blit(Plus,(window_width/8+40,window_height/12))
    
def OutOfPotion():
    if AttackPotionNumber==0:
        win.blit(RunnedOutPot,(window_width*3/80,window_height*3/4))
    if DefendPotionNumber==0:
        win.blit(RunnedOutPot,(window_width*33/80,window_height*3/4))



    

def ExitOption():
    ExitOption=True
    while ExitOption==True:
        ExitMenu()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitOption=False
                PotionSelect=False
                fight=False
                isRunning=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if ExitButton.isOver(pos):
                    pygame.quit()
                if ResumeButton.isOver(pos):
                    ExitOption=False

                                        
                        
                
    
                                 

#Loading Graphics
BackGround=pygame.image.load("Graphics\\FB.png")
Character= pygame.image.load("Graphics\\Me.png")
Enemy=pygame.image.load("Graphics\\FightEnemy.png")
Victory=pygame.image.load("Graphics\\Victory.jpg")
Defeat=pygame.image.load("Graphics\\Defeat.jpg")

InputColor=(Color.LightBlue)

#Create windows
def create_window():
    global win, window_height, window_width, window_title
    window_width, window_height = 800,600
    window_title = "RPG Game"
    pygame.display.set_caption(window_title)
    win = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)



create_window()


m=window_width*3/4
n=window_height*5/12

x=window_width/8
y=window_height/6


    
def MainWindow():
    win.fill((Color.Black))
    win.blit(BackGround,(0,0))
    win.blit(Enemy,(x,y))
    win.blit(Character,(m,n))
    showHP()
    
    AttackButton.draw(win,(Color.White))
    DefendButton.draw(win,(Color.White))
    UseItemButton.draw(win,(Color.White))
    if MeDamage == True:
        DamageHPAI()
    elif MeDefend == True:
        HealHPMe()
    elif AIDamage == True:
        DamageHPMe()
    elif AIDefend == True:
        HealHPAI()

    

       
def PickItem():
    win.fill((Color.Black))
    win.blit(BackGround,(0,0))
    win.blit(Enemy,(x,y))
    win.blit(Character,(m,n))
    showHP()
    
    AttPotionButton.draw(win,(Color.White))
    HealthPotionButton.draw(win,(Color.White))
    BackButton.draw(win,(Color.White))
    OutOfPotion()
    
def questionWindow():
    win.fill((Color.Black))
    win.blit(BackGround,(0,0))
    win.blit(Enemy,(x,y))
    win.blit(Character,(m,n))
    showHP()
    showquestion()
    TryInput.draw(win,(InputColor))
    
    
  
def VictoryWindow():
    V=True
    win.fill((Color.Black))
    win.blit(Victory,(-window_width/10,0))
    ContinueButton.draw(win,(Color.White))
    pygame.display.update()
    while V==True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if ContinueButton.isOver(pos):
                    V=False
                    c.execute('UPDATE Character_Stats SET HealthPotion=(?),AttackPotion=(?) WHERE Username=(?)',(DefendPotionNumber,AttackPotionNumber,Globals.LogUser))
                    c.execute('UPDATE Saves SET Status=0 WHERE EntityName=(?) AND Username=(?)',(Globals.EntityName,Globals.LogUser))
                    c.execute('UPDATE Scores SET Score1=(?),Score2=(?),Score3=(?),Score4=(?),Score5=(?),Score6=(?),Score7=(?),Score8=(?),Score9=(?),Score10=(?),Score11=(?),Score12=(?)',(Score1,Score2,Score3,Score4,Score5,Score6,Score7,Score8,Score9,Score10,Score11,Score12))                    
                    conn.commit()
                   
def DefeatWindow():
    D=True
    win.fill((Color.Black))
    win.blit(Defeat,(-window_width/5,0))
    RetryButton.draw(win,(Color.White))
    pygame.display.update()
    while D==True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if RetryButton.isOver(pos):
                    D=False
                    c.execute('UPDATE Character_Stats SET HealthPotion=(?),AttackPotion=(?) WHERE Username=(?)',(DefendPotionNumber,AttackPotionNumber,Globals.LogUser))
                    c.execute('UPDATE Saves SET Status=1 WHERE EntityName=(?) AND Username=(?)',(Globals.EntityName,Globals.LogUser))
                    c.execute('UPDATE Scores SET Score1=(?),Score2=(?),Score3=(?),Score4=(?),Score5=(?),Score6=(?),Score7=(?),Score8=(?),Score9=(?),Score10=(?),Score11=(?),Score12=(?)',(Score1,Score2,Score3,Score4,Score5,Score6,Score7,Score8,Score9,Score10,Score11,Score12))
                    conn.commit()


Exit=pygame.image.load("Graphics\\Exit1.png")
Exit=pygame.transform.scale(Exit,(1280,720))
def ExitMenu():
    win.fill((Color.Black))
    win.blit(Exit,(-window_width/2,0))
    ExitButton.draw(win,(Color.White))
    ResumeButton.draw(win,(Color.White))



#AI technology baby
def AiTurn():
    global myhealth,myatk,mydefe,aihealth,aiatk,aidefe,isRunning,AIDefend
    count=0
    if aihealth <= 0:
        VictoryWindow()
        isRunning=False
    if aihealth >= 50 and aihealth > 0 and count==0:
        count+=1
        EnemyAttack()
        myhealth = myhealth - aiatk
    if aihealth < 50 and aihealth > 0 and myhealth!= aiatk:
        aihealth = aihealth+aidefe
        AIDefend=True
        MainWindow()
        pygame.display.flip()
        time.sleep(0.5)
        AIDefend=False
    if myhealth== aiatk and count==0:
        count+=1
        EnemyAttack()
        myhealth=myhealth-aiatk
    if myhealth <= 0:
        DefeatWindow()
        isRunning=False
    count=0

#Animations
def MeAttack():
    global m,n, MeDamage
    while m >=x and n>=y:
        m-=48/5
        n-=3
        MainWindow()
        pygame.display.flip()
    Punch()
    MeDamage = True
    while m <=window_width*3/4 and n<=window_height*5/12:
        m+=48/5
        n+=3
        MainWindow()
        pygame.display.flip()
    MeDamage = False
    pygame.display.flip()
        
def EnemyAttack():
    global x,y,AIDamage
    while x<=m and y<=n:
        x+=48/5
        y+=3
        MainWindow()
        pygame.display.flip()
    Punch()
    AIDamage=True
    while x>=window_width/8 and y>=window_height/6:
        x-=48/5
        y-=3
        MainWindow()
        pygame.display.flip()
    time.sleep(0.5)
    AIDamage=False
    pygame.display.flip()
        
    


#Buttons Creation
AttackButton= button((Color.Firebrick), 2,window_height-102 , 200, 100, 'Attack')
DefendButton=button((Color.LightBlue),window_width/2-100,window_height-102,200,100,"Defend")
UseItemButton=button((Color.Ivory),window_width-202,window_height-102,200,100,"Use An Item")



AttPotionButton=button((Color.Firebrick),2,window_height-102,200,100,"Potion of Attack")
HealthPotionButton=button((Color.Ivory),window_width/2-100,window_height-102,200,100,"Potion of Health")
BackButton=button((Color.White),window_width-202,window_height-102,200,100,"Back")



ExitButton=button((Color.Cyan),window_width/2-100,window_height/2-102,200,100,"Exit")
ResumeButton=button((Color.Cyan),window_width/2-100,window_height/2+50,200,100,"Back To Game")

ContinueButton=button((Color.Gray),window_width-250,window_height-150,200,100,"Continue")
RetryButton=button((Color.Gray),window_width-250,window_height-150,200,100,"Retry")




TryInput=button((Color.White),window_width/5,window_height-150,500,30,"")




NumberPick=[]
for z in range(12):
    NumberPick.append(z+1)
#use tuple for questionaire
def GetQuestion():
    global Question,Number1,Number2,Score1,Score2,Score3,Score4,Score5,Score6,Score7,Score8,Score9,Score10,Score11,Score12
    if Score1<-100:
        Number1=1
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score2<-100:
        Number1=2
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score3<-100:
        Number1=3
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score4<-100:
        Number1=4
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score5<-100:
        Number1=5
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score6<-100:
        Number1=6
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score7<-100:
        Number1=7
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score8<-100:
        Number1=8
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score9<-100:
        Number1=9
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score10<-100:
        Number1=10
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score11<-100:
        Number1=11
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    if Score12<-100:
        Number1=12
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
    else:
        Number1=random.choice(NumberPick)
        Number2=random.choice(NumberPick)
        Questionlvl1=Number1*Number2
        Question=str(Questionlvl1)
def getRight():
    global Number1,Number2,Score1,Score2,Score3,Score4,Score5,Score6,Score7,Score8,Score9,Score10,Score11,Score12
    if Number1==1 or Number2==1:
        Score1+=10
    if Number1==2 or Number2==2:
        Score2+=10
    if Number1==3 or Number2==3:
        Score3+=10
    if Number1==4 or Number2==4:
        Score4+=10
    if Number1==5 or Number2==5:
        Score5+=10
    if Number1==6 or Number2==6:
        Score6+=10
    if Number1==7 or Number2==7:
        Score7+=10
    if Number1==8 or Number2==8:
        Score8+=10
    if Number1==9 or Number2==9:
        Score9+=10
    if Number1==10 or Number2==10:
        Score10+=10
    if Number1==11 or Number2==11:
        Score11+=10
    if Number1==12 or Number2==12:
        Score12+=10
    
def getWrong():
    global Number1,Number2,Score1,Score2,Score3,Score4,Score5,Score6,Score7,Score8,Score9,Score10,Score11,Score12
    if Number1==1 or Number2==1:
        Score1-=10
    if Number1==2 or Number2==2:
        Score2-=10
    if Number1==3 or Number2==3:
        Score3-=10
    if Number1==4 or Number2==4:
        Score4-=10
    if Number1==5 or Number2==5:
        Score5-=10
    if Number1==6 or Number2==6:
        Score6-=10
    if Number1==7 or Number2==7:
        Score7-=10
    if Number1==8 or Number2==8:
        Score8-=10
    if Number1==9 or Number2==9:
        Score9-=10
    if Number1==10 or Number2==10:
        Score10-=10
    if Number1==11 or Number2==11:
        Score11-=10
    if Number1==12 or Number2==12:
        Score12-=10


MeDamage = False
AIDamage = False
MeDefend=False
AIDefend=False


GetQuestion()
isRunning = True
while isRunning == True:
    questionWindow()
    pygame.display.update()
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            isRunning = False

        #Question and Answare display
        if event.type==pygame.MOUSEBUTTONDOWN:
            if TryInput.isOver(pos):
                TryInput.active = not TryInput.active
                InputColor=(Color.Blue)
            else:
                TryInput.active=False
                InputColor=(Color.Cyan)
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ExitOption()
            if TryInput.active:
                if event.key== pygame.K_RETURN:
                    if TryInput.text==Question:
                        print("Right Answer Detected")
                        getRight()
                        RightAns = True        
                    else:
                        print("Wrong Answer Detected")
                        getWrong()
                        RightAns = False
                    TryInput.text=""


                    
                    #Main Fight Menu display
                    fight=True
                    while fight == True:
                        MainWindow()
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type== pygame.QUIT:
                                fight=False
                                isRunning=False
                            if event.type==pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    ExitOption()

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos=pygame.mouse.get_pos()
                                if AttackButton.isOver(pos):
                                    if RightAns==True:
                                        aihealth=aihealth-myatk
                                        MeAttack()
                                        time.sleep(0.5)
                                        MeDamage = False
                                        AiTurn()
                                        fight=False
                                        GetQuestion()
                                    else:
                                        storeatk=myatk
                                        myatk=int(myatk/2)
                                        aihealth=int(aihealth-myatk)
                                        MeAttack()
                                        time.sleep(0.5)
                                        MeDamage = False
                                        myatk=storeatk
                                        AiTurn()
                                        fight=False
                                        GetQuestion()
                                        
                                if DefendButton.isOver(pos):
                                    if RightAns==True:
                                        myhealth = myhealth+mydefe
                                        MeDefend=True
                                        MainWindow()
                                        pygame.display.flip()
                                        time.sleep(0.5)
                                        MeDefend=False
                                        AiTurn()
                                        fight=False
                                        GetQuestion()
                                    if RightAns==False:
                                        AiTurn()
                                        fight=False
                                        GetQuestion()
                                if UseItemButton.isOver(pos):
                                    PotionSelect = True
                            
                            

                                


                                    #Use Item Window
                                    while PotionSelect == True:
                                        PickItem()
                                        pygame.display.update()
                                        for event in pygame.event.get():
                                            pos = pygame.mouse.get_pos()
                                            if event.type == pygame.QUIT:
                                                PotionSelect=False
                                                fight=False
                                                isRunning=False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if AttPotionButton.isOver(pos):
                                                    if AttackPotionNumber <= 0:
                                                        pass
                                                    else:
                                                        myatk = myatk+Item_Attack.attack
                                                        pygame.display.update()
                                                        AttackPotionNumber-=1
                                                if HealthPotionButton.isOver(pos):
                                                    if DefendPotionNumber<=0:
                                                        pass
                                                    else:
                                                        myhealth= myhealth+Item_Health.health
                                                        DefendPotionNumber-=1
                                                if BackButton.isOver(pos):
                                                    PotionSelect = False
                                            if event.type==pygame.KEYDOWN:
                                                ExitOption()
                                

                elif event.key == pygame.K_BACKSPACE:
                    TryInput.text=TryInput.text[:-1]
                else:
                    TryInput.text += event.unicode
                TryInput.txt_surface=FONT.render(TryInput.text,True,TryInput.color)



pygame.mixer.music.pause()

       
        
               
        
