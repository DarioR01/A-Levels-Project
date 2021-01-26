import pygame

pygame.init()

def get_faces(sprite):
    faces ={}

    size = sprite.get_size()
    tile_size =(int(size[0] / 3), int(size[1] / 4))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0, 0),(tile_size[1],0, tile_size[0], tile_size[1]))
    faces ["south"] = south 

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0, 0),(tile_size[0],tile_size[1]*3, tile_size[0], tile_size[1]))
    faces["north"] = north 

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0, 0),(tile_size[1], tile_size[1],tile_size[0], tile_size[1]))
    faces["west"] = west 

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0, 0),(tile_size[0] ,tile_size[1]*2,tile_size[0] ,tile_size[1]))
    faces["east"] = east

    south1 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south1.blit(sprite, (0, 0),(0,0, tile_size[0], tile_size[1]))
    faces ["south1"] = south1 

    north1 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north1.blit(sprite, (0, 0),(0, tile_size[1]*3, tile_size[0], tile_size[1]))
    faces["north1"] = north1 

    west1 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west1.blit(sprite, (0, 0),(0, tile_size[1],tile_size[0], tile_size[1]))
    faces["west1"] = west1 
 
    east1 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east1.blit(sprite, (0, 0),(0,tile_size[1]*2,tile_size[0] ,tile_size[1]))
    faces["east1"] = east1

    south2 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south2.blit(sprite, (0, 0),(tile_size[0]*2, 0, tile_size[0], tile_size[1]))
    faces ["south2"] = south2 

    north2 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north2.blit(sprite, (0, 0),(tile_size[0]*2, tile_size[1]*3, tile_size[0], tile_size[1]))
    faces["north2"] = north2 

    west2 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west2.blit(sprite, (0, 0),(tile_size[0]*2, tile_size[1],tile_size[0], tile_size[1]))
    faces["west2"] = west2 

    east2 = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east2.blit(sprite, (0, 0),(tile_size[0]*2 ,tile_size[1]*2 ,tile_size[0] ,tile_size[1]))
    faces["east2"] = east2 

    return faces
