import pygame, math, sqlite3,sys, importlib
from Scripts.Split import *
from Scripts.Colors import *
from Scripts.Globals import *
from Scripts.Buttons import *

pygame.init()

probability=[]
directions=[]
for x in range(500):
    probability.append(x+1)
for y in range(4):
    directions.append(y+1)
z=0
keynumber=0

count=0 


class NPC:
    def __init__(self,name,positionx,positiony,health,atk,defe,detectx,detecty,Trigger,Alive,mapping,image):
        self.name=name
        self.facing="south"
        self.positionx=positionx
        self.positiony=positiony
        self.health=health
        self.atk=atk
        self.defe=defe
        self.detectx=detectx
        self.detecty=detecty
        self.Trigger=Trigger
        sprite= pygame.image.load(image)
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        self.faces=get_faces(sprite)
        self.x=0
        self.y=1
        self.d=0
        self.Alive=Alive
        self.count=0
        self.mapping=mapping
        
    def render(self,surface,pos):
        if self.Alive==True and self.mapping==Globals.mapp:
            surface.blit(self.faces[self.facing],pos)

    def movement(self):
        if self.Alive==True and self.mapping==Globals.mapp:
            self.Trigger=False
            self.detectx=0
            self.detecty=0
            self.x=int(self.positionx-self.width/2)
            self.y=int(self.positiony-self.height/2)

            
            if Globals.player_x+Globals.player_w/4<self.x+self.width/2 and Globals.player_x+Globals.player_w/4>self.x+self.width/4 and Globals.player_y+Globals.player_h/4>self.y and Globals.player_y-Globals.player_h/4<self.y:
                self.detectx=1
            if Globals.player_x-Globals.player_w/4>self.x-self.width/2 and Globals.player_x-Globals.player_w/4<self.x-self.width/4 and Globals.player_y+Globals.player_h/4>self.y and Globals.player_y-Globals.player_h/4<self.y:
                self.detectx=2
            if self.detectx!=1 or self.detectx!=2:
                if Globals.player_y+Globals.player_h/4<self.y+self.height/2 and Globals.player_y+Globals.player_h/4>self.y+self.height/4 and Globals.player_x+Globals.player_w/4>self.x and Globals.player_x-Globals.player_w/4<self.x:
                    self.detecty=1            
                if Globals.player_y-Globals.player_h/4>self.y-self.height/2 and Globals.player_y-Globals.player_h/4<self.y-self.height/4 and Globals.player_x+Globals.player_w/4>self.x and Globals.player_x-Globals.player_w/4<self.x:
                    self.detecty=2
            
            p=random.choice(probability)
            if p==1:
                self.d=random.choice(directions)
            if self.detectx==1 or self.detectx==2 or self.detecty==1 or self.detecty==2:
                self.d=0
                self.Trigger=True
            elif self.d==1 and self.y>0 and self.detecty!=2:
                self.positiony+=-100*Globals.deltatime
                self.facing="north"
            elif self.d==2 and self.y<3135 and self.detecty!=1:
                self.positiony+=100*Globals.deltatime
                self.facing="south"
            elif self.d==3 and self.x>0 and self.detectx!=2:
                self.positionx+=-100*Globals.deltatime
                self.facing="west"
            elif self.d==4 and self.x<3150 and self.detectx!=1:
                self.positionx+=100*Globals.deltatime
                self.facing="east"
        if self.Alive==False:
            self.detectx=0
            self.detecty=0
            self.Trigger=False

            
    def eventFight(self,surface,width,height,Speech):
        global count
        z=0
        key=pygame.key.get_pressed()
        if self.Trigger==True and self.mapping==Globals.mapp:
            if key[pygame.K_RETURN]:
                pygame.mixer.music.pause()
                Globals.Entityname=self.name
                self.dataFight()
                print("fight")
                if count==0:
                    import Fight
                    count+=1
                else:
                    import Fight
                    importlib.reload(Fight)
                pygame.mixer.music.unpause()
            Speech=button((Color.White),100,height*(5/6)-10,600,100,Speech[z])
            Speech.draw(surface,(Color.Black))
            instruction="Press Enter to continue"
            instruction_font= pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",12)
            instruction_overlay=instruction_font.render(instruction,True,(Color.Goldenrod))
            surface.blit(instruction_overlay,(width*(11/16),height*(23/24)))
            
            
            

    def eventChallenge(self,surface,width, height):
        global count
        option_font= pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)
        option="Press E to challenge"
        if self.Trigger==True and self.mapping==Globals.mapp:
            option_overlay=option_font.render(option,True,(Color.Goldenrod))
            surface.blit(option_overlay, (width*(11/32),height*(5/6)))
            key=pygame.key.get_pressed()
            if key[pygame.K_e]:
                pygame.mixer.music.pause()
                Globals.Entityname=self.name
                self.dataFight()
                if count==0:
                    import Fight
                    count+=1
                else:
                    import Fight
                    importlib.reload(Fight)



    def eventTalk(self,surface,Speech,width,height,Event):
        global z,keynumber
        if self.Trigger==True and self.mapping==Globals.mapp:
            key=pygame.key.get_pressed()
            if z==len(Speech)-1:
                keynumber=1
                if key[pygame.K_RETURN]:
                    self.Trigger=False
            if key[pygame.K_RETURN]and keynumber!=1:
                z+=1
                keynumber+=1
            if Event.type==pygame.KEYUP:
                keynumber=0
            Speech=button((Color.White),100,height*(5/6)-10,600,100,Speech[z])
            Speech.draw(surface,(Color.Black))
            instruction="Press Enter to continue"
            instruction_font= pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",12)
            instruction_overlay=instruction_font.render(instruction,True,(Color.Goldenrod))
            surface.blit(instruction_overlay,(width*(11/16),height*(23/24)))
            
    def dataFight(self):
        Globals.aihealth=self.health
        Globals.aiatk=self.atk
        Globals.aidefe=self.defe
        Globals.EntityName=self.name

npcFight=NPC("Zed",400,400,100,20,5,0,0,False,True,"Prova.map","Graphics\\NPCImage1.png")
npcSpeech=NPC("Shaco",200,200,100,20,5,0,0,False,True,"Prova.map","Graphics\\NPCImage2.png")
npcChallenge=NPC("Kindred",600,100,100,20,5,0,0,False,True,"Prova.map","Graphics\\NPCImage3.png")
   
        
        

           





















    
