import pygame,sqlite3
from Scripts.Globals import*
from Scripts.Colors import *
from Scripts.Map_Loader import *

storemapp=Globals.mapp


class Items:

    def __init__(self,name,effect,health,attack,armor):
        self.name = name
        self.effect =effect
        self.health =health
        self.attack =attack
        self.armor = armor
Item_Health =Items("Potion of Health","heal you of 20 HP",20,0,0)
Item_Attack =Items("Potioin of Attack","Increase your attack of 10",0,10,0)


class InGame:
    
    def __init__(self,name,x,y,picture,detectx,detecty,Taken,mapping):
        self.name= name
        self.x=x
        self.y=y
        self.picture=pygame.image.load(picture)
        size=self.picture.get_size()
        self.width=size[0]*3
        self.height=size[1]*4
        self.detectx=detectx
        self.detecty=detecty
        self.Taken=Taken
        self.Trigger=False
        self.mapping=mapping

    def renderItem(self,surface,pos):
        if self.Taken==False and self.mapping==Globals.mapp:
            conn=sqlite3.connect("GameDatabase.db")
            c=conn.cursor()
            c.execute('SELECT * FROM Saves WHERE Username=(?) AND EntityName=(?)',(Globals.LogUser,self.name))
            rows=c.fetchall()
            self.Taken=rows[0][3]
            surface.blit(self.picture,pos)
            conn.close()  

    def collisionItem(self):
        if self.Taken==False and self.mapping==Globals.mapp:
            self.Trigger=False
            self.detectx=0
            self.detecty=0

            
            if Globals.player_x+Globals.player_w/4<self.x+self.width/2 and Globals.player_x+Globals.player_w/4>self.x+self.width/4 and Globals.player_y+Globals.player_h/4>self.y and Globals.player_y-Globals.player_h/4<self.y:
                self.detectx=1
            if Globals.player_x-Globals.player_w/4>self.x-self.width/2 and Globals.player_x-Globals.player_w/4<self.x-self.width/4 and Globals.player_y+Globals.player_h/4>self.y and Globals.player_y-Globals.player_h/4<self.y:
                self.detectx=2
            if self.detectx!=1 or self.detectx!=2:
                if Globals.player_y+Globals.player_h/4<self.y+self.height/2 and Globals.player_y+Globals.player_h/4>self.y+self.height/4 and Globals.player_x+Globals.player_w/4>self.x and Globals.player_x-Globals.player_w/4<self.x:
                    self.detecty=1            
                if Globals.player_y-Globals.player_h/4>self.y-self.height/2 and Globals.player_y-Globals.player_h/4<self.y-self.height/4 and Globals.player_x+Globals.player_w/4>self.x and Globals.player_x-Globals.player_w/4<self.x:
                    self.detecty=2

            if self.detectx==1 or self.detectx==2 or self.detecty==1 or self.detecty==2:
                self.Trigger=True

        if self.Taken==True:
            self.detectx=0
            self.detecty=0

    def eventPick(self,surface,width, height):
        if self.Taken==False and self.mapping==Globals.mapp:
            option_font= pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)
            option="Press E to take this Item"
            if self.Trigger==True:
                option_overlay=option_font.render(option,True,(Color.Goldenrod))
                surface.blit(option_overlay, (width*(11/32),height*(5/6)))
                key=pygame.key.get_pressed()
                if key[pygame.K_e]:
                    self.Taken=True
                    conn=sqlite3.connect("GameDatabase.db")
                    c=conn.cursor()
                    c.execute('SELECT HealthPotion, AttackPotion FROM Character_Stats WHERE Username=(?)',(Globals.LogUser,))
                    rows=c.fetchall()
                    HealthPot=rows[0][0]
                    AttackPot=rows[0][1]
                    if self.name == "HealthPotion":
                        HealthPot+=1
                    if self.name == "AttackPotion":
                        AttackPot+=1
                    c.execute('UPDATE Character_Stats SET HealthPotion=(?),AttackPotion=(?) WHERE Username=(?)',(HealthPot,AttackPot,Globals.LogUser))
                    c.execute('UPDATE Saves SET Status=1 WHERE EntityName=(?) AND Username=(?)',(self.name,Globals.LogUser))
                    conn.commit()
                    conn.close()
    def changeRoom(self,surface,mapp,width,height):
        global storemapp
        if self.Taken==False:
            option_font= pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf",20)
            option="Press E to change room"
            if self.Trigger==True:
                option_overlay=option_font.render(option,True,(Color.Goldenrod))
                surface.blit(option_overlay, (width*(11/32),height*(5/6)))
                key=pygame.key.get_pressed()
                if key[pygame.K_e] and Globals.mapp!=mapp:
                    Globals.mapp=mapp
                    storemapp=self.mapping
                    self.mapping=mapp
                    surface.fill(Color.Black)
                    Globals.terrain=Map_Engine.load_map(Globals.mapp)
                    conn=sqlite3.connect("GameDatabase.db")
                    c=conn.cursor()
                    c.execute("UPDATE Saves SET Map=(?) WHERE Username=(?) AND EntityName=(?) ",(Globals.mapp,Globals.LogUser,Globals.characterName))
                    c.execute("UPDATE Saves SET Map=(?) WHERE Username=(?) AND EntityName=(?) ",(Globals.mapp,Globals.LogUser,self.name))
                    conn.commit()
                    conn.close()
                    self.detectx=0
                    self.detecty=0
                elif key[pygame.K_e] and (Globals.mapp==mapp or Globals.mapp==self.mapping):
                    Globals.mapp=storemapp
                    self.mapping=storemapp
                    surface.fill(Color.Black)
                    Globals.terrain=Map_Engine.load_map(Globals.mapp)
                    conn=sqlite3.connect("GameDatabase.db")
                    c=conn.cursor()
                    c.execute("UPDATE Saves SET Map=(?) WHERE Username=(?) AND EntityName=(?) ",(Globals.mapp,Globals.LogUser,Globals.characterName))
                    c.execute("UPDATE Saves SET Map=(?) WHERE Username=(?) AND EntityName=(?) ",(Globals.mapp,Globals.LogUser,self.name))
                    conn.commit()
                    conn.close()
                    self.detectx=0
                    self.detecty=0
                    
        else:
            self.detectx=0
            self.detecty=0
    def getmap(self):
        conn=sqlite3.connect("GameDatabase.db")
        c=conn.cursor()
        c.execute('SELECT * FROM Saves WHERE Username=(?) AND EntityName=(?)',(Globals.LogUser,self.name))
        rows=c.fetchall()
        self.mapping=str(rows[0][4])             
                    
ItemHealth=InGame("HealthPotion",100,100,"Graphics\\HealthItem.jpg",0,0,False,"Prova.map")
ItemAttack=InGame("AttackPotion",600,1000,"Graphics\\AttackItem.jpg",0,0,False,"Prova.map")                
Door1=InGame("Door",500,500,"Graphics\\Door.png",0,0,False,"Prova.map")


                    
                    
            
        

        
        
        
