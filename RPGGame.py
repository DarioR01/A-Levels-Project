#libraries/ python files importation
import pygame, sys, time, random,sqlite3    
from Scripts.Colors import *        
from Scripts.textures import *      
from Scripts.Globals import *
from Scripts.Map_Loader import *
from Scripts.Split import *
from Scripts.Player import *
from Scripts.Buttons import *
from Scripts.Items import *
from Scripts.NPCClass import *

pygame.init()


#Fetching saves from previous section
file=open("LogUser.txt","r")
for word in file:
    Globals.LogUser=str(word)

conn=sqlite3.connect("GameDatabase.db")
c=conn.cursor()
c.execute('SELECT * FROM Saves WHERE Username=(?)',(Globals.LogUser,))
rows=c.fetchall()
Globals.characterName=rows[0][2]
Globals.mapp=rows[0][4]
conn.close()

Door1.getmap()

def Death():
    global ZedStatus,KindredStatus,ShacoStatus
    conn=sqlite3.connect("GameDatabase.db")
    c=conn.cursor()
    c.execute('SELECT * FROM Saves WHERE Username=(?)',(Globals.LogUser,))
    rows=c.fetchall()
    ZedStatus = rows[1][3]
    ShacoStatus = rows[2][3]
    KindredStatus = rows[3][3]
    conn.close()



#Creation of FPS display
FPS=1
fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)    
    
        
    
def show_FPS():
    fps_overlay = fps_font.render(str(FPS),True,Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))
                            
#Create windows and different structures.
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800,600
    window_title = "RPG Game"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

Exit=pygame.image.load("Graphics\\Exit1.png")
Exit=pygame.transform.scale(Exit,(1280,720))
def stop_menu():
    pygame.mixer.music.pause()
    window.fill((Color.Black))
    window.blit(Exit,(-window_width/2,0))
    BackButton.draw(window,(Color.White))
    ExitButton.draw(window,(Color.White))
                    
#initialize window.
create_window()


##Create Buttons
BackButton= button((Color.Cyan),window_width/2-100,100,200,100,"Back")
ExitButton=button ((Color.Cyan),window_width/2-100,250,200,100,"Exit")


#Create player character
player = Player("Character","Graphics\\MainCharacterNew.png")
Globals.player_w, Globals.player_h = player.width, player.height


#Initialise Music
#pygame.mixer.music.load("Sounds\\Inuyashas Lullaby (Full).mp3")
#pygame.mixer.music.play(-1)


#Position of the player character in in proportion to the window.
playerposition_x=window_width/2
playerposition_y=window_height/2





#Speeches array creation
speech=["Hello","my name is Bob","Nice to meet you","Now I have to go","Bye"]
speech1=["I challenge you!!!"]


#Terrain initialization
Globals.terrain=Map_Engine.load_map(Globals.mapp)

j=1 ########Attento
#Main Game Loop
isRunning = True
while isRunning:
    #Starting time for FPS calulation
    Starttime=time.time()

    #Checking dead NPC
    Death()
    npcFight.Alive=ZedStatus
    npcChallenge.Alive=KindredStatus
    npcSpeech.Alive=ShacoStatus

    #Linking object with movements and collision calculation functions.
    ItemHealth.collisionItem()
    ItemAttack.collisionItem()
    Door1.collisionItem()    
    npcFight.movement()
    npcSpeech.movement()
    npcChallenge.movement()
    #Movent controlled by the pygame library.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN: #Selection due to a button press 
            if event.key == pygame.K_w or event.key == pygame.K_UP :
                Globals.camera_move = 1
                player.facing="north"
                
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                Globals.camera_move = 2
                player.facing = "south"
               
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                Globals.camera_move = 3
                player.facing = "west"
               
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                Globals.camera_move = 4
                player.facing = "east"
            elif event.key == pygame.K_p: 
                j=0

            elif event.key == pygame.K_ESCAPE:
                Pause = True
                #Pause window loop
                while Pause == True:
                    Globals.camera_move = 0
                    stop_menu()
                    pygame.display.update()
                    for event in pygame.event.get():
                        pos=pygame.mouse.get_pos()
                        if event.type == pygame.MOUSEBUTTONDOWN: #Selection due to button pressed in the stop window.
                            if BackButton.isOver(pos):
                                pygame.mixer.music.unpause()
                                Pause = False


                            if ExitButton.isOver(pos):
                                pygame.quit()
                                sys.exit()
                    
               

        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0
            
            


    #Main character movement and collision LOGIC
    if npcFight.Trigger==True:
        Globals.camera_move=0
    if Globals.camera_move ==  1 and Globals.player_y>0 and npcFight.detecty!=1 and npcSpeech.detecty!=1 and npcChallenge.detecty!=1 and ItemHealth.detecty!=1 and ItemAttack.detecty!=1 and Door1.detecty!=1:
        Globals.camera_y += 1000 * Globals.deltatime
    elif Globals.camera_move ==  2 and Globals.player_y<3135 and npcFight.detecty!=2 and npcSpeech.detecty!=2 and npcChallenge.detecty!=2 and ItemHealth.detecty!=2 and ItemAttack.detecty!=2 and Door1.detecty!=2:
        Globals.camera_y -= 1000 * Globals.deltatime
    elif Globals.camera_move ==  3 and Globals.player_x>0 and npcFight.detectx!=1 and npcSpeech.detectx!=1 and npcChallenge.detectx!=1 and ItemHealth.detectx!=1 and ItemAttack.detectx!=1 and Door1.detectx!=1:
        Globals.camera_x += 1000 * Globals.deltatime
    elif Globals.camera_move ==  4 and Globals.player_x<3150 and npcFight.detectx!=2 and npcSpeech.detectx!=2 and npcChallenge.detectx!=2 and ItemHealth.detectx!=2 and ItemAttack.detectx!=2 and Door1.detectx!=2:
        Globals.camera_x -= 1000 * Globals.deltatime

    #Main character position (x,y) calculation
    Globals.player_x = int(playerposition_x - Globals.player_w /2 - Globals.camera_x)
    Globals.player_y = int(playerposition_y - Globals.player_h /2 - Globals.camera_y)


    #RENDER GRAPHICS
    window.fill(Color.Black)

    window.blit(Globals.terrain, (Globals.camera_x, Globals.camera_y))

    player.render(window,(playerposition_x-Globals.player_w/2,playerposition_y - Globals.player_h/2))

    ItemHealth.renderItem(window,(ItemHealth.x+Globals.camera_x,ItemHealth.y+Globals.camera_y))
    ItemAttack.renderItem(window,(ItemAttack.x+Globals.camera_x,ItemAttack.y+Globals.camera_y))
    Door1.renderItem(window,(Door1.x+Globals.camera_x,Door1.y+Globals.camera_y))

    npcFight.render(window,(npcFight.positionx-npcFight.width/2+Globals.camera_x,npcFight.positiony-npcFight.height/2+Globals.camera_y))
    npcSpeech.render(window,(npcSpeech.positionx-npcSpeech.width/2+Globals.camera_x,npcSpeech.positiony-npcSpeech.height/2+Globals.camera_y))
    npcChallenge.render(window,(npcChallenge.positionx-npcChallenge.width/2+Globals.camera_x,npcChallenge.positiony-npcChallenge.height/2+Globals.camera_y))

    #Final time for FPS calculation
    endtime=time.time()

    #Slow down the FPS calculation
    if count==15:
        FPS=int(1/(endtime-Starttime))
        count=0
    else:
        count+=1

    #Deltatime calculation
    Globals.deltatime = 1 / FPS
    if Globals.deltatime <0.0008:
        Globals.deltatime=0.0008

    #FPS initialization
    show_FPS()
    

    #Linking object in the code with respective function
    npcChallenge.eventChallenge(window,window_width,window_height)
    npcSpeech.eventTalk(window,speech,window_width,window_height,event)
    npcFight.eventFight(window,window_width,window_height,speech1)
    ItemHealth.eventPick(window,window_width,window_height)
    ItemAttack.eventPick(window,window_width,window_height)
    Door1.changeRoom(window,"FirstLaby.map",window_width,window_height)
    
    if j==0:
        print("Camera move is:",Globals.camera_move) ########Attento
        print("Detect x is:",npcSpeech.detectx)
        print("Detect y is:",npcSpeech.detecty)
        print("facing is:",player.facing)
        j+=1

    #Updating the window
    pygame.display.update()

    pygame.display.flip()                                   
    

#Quitting the opened libraries
pygame.quit()
sys.exit()
                                    
            
