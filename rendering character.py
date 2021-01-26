import pygame,sys,time
from Scripts.Colors import *
pygame.init()





def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800,600
    window_title = "RPG Game"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

create_window()


GameDisplay = pygame.display.set_mode((window_width,window_height))

x=int
y=int

player= pygame.image.load("Graphics\\Hulp2ij.png")
width,height = player.get_width()/3,player.get_height()/4
south = pygame.Rect((width,0),(width,height))
west = pygame.Rect((width,height),(width,height))
east = pygame.Rect((width,height*2),(width,height))
north = pygame.Rect((width,height*3),(width,height))
south1 = pygame.Rect((0,0),(width,height))
west1 = pygame.Rect((0,height),(width,height))
east1 = pygame.Rect((0,height*2),(width,height))
north1 = pygame.Rect((0,height*3),(width,height))
south2 = pygame.Rect((width*2,0),(width,height))
west2 = pygame.Rect((width*2,height),(width,height))
east2 = pygame.Rect((width*2,height*2),(width,height))
north2 = pygame.Rect((width*2,height*3),(width,height))

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
  

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),north1)
            pygame.display.flip()
            time.sleep(0.15)
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),north2)
            pygame.display.flip()
            time.sleep(0.15)
        elif event.key == pygame.K_s:
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),south1)
            pygame.display.flip()
            time.sleep(0.15)
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),south2)
            pygame.display.flip()
            time.sleep(0.15)
        elif event.key == pygame.K_a:
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),west1)
            pygame.display.flip()
            time.sleep(0.15)
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),west2)
            pygame.display.flip()
            time.sleep(0.15)
        elif event.key == pygame.K_d:
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),east1)
            pygame.display.flip()
            time.sleep(0.15)
            window.fill(Color.Black)
            GameDisplay.blit(player,(window_width/2,window_height/2),east2)
            pygame.display.flip()
            time.sleep(0.15)
    elif event.type == pygame.KEYUP:
        pass
        

    
            
        
    
    
#https://stackoverflow.com/questions/11420426/split-image-in-pygame
#https://stackoverflow.com/questions/11420426/split-image-in-pygame




   
    
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
sys.exit()


