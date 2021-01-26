import pygame
from Scripts.Split import *
pygame.init()




class Player:

    def __init__(self, name, image):
        self.name = name
        self.facing = "south"
        sprite = pygame.image.load(image)
        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]
        self.faces = get_faces(sprite)

    def render(self, surface,pos):
        surface.blit(self.faces[self.facing],pos)
    
    
    
        
            

    
