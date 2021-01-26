import pygame

pygame.init()

class Tiles:

    Size = 32
        
    def Load_Texture(file,Size):
        bitmap= pygame.image.load(file)
        bitmap= pygame.transform.scale(bitmap,(Size,Size))
        surface= pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface

    Wood = Load_Texture("Graphics\\wood.png", Size)

    Cobblestone = Load_Texture("Graphics\\cobblestone.png", Size)

    Stone = Load_Texture("Graphics\\Stone.png", Size)

    Stone1 = Load_Texture("Graphics\\Stone4.png", Size)

    Lava = Load_Texture("Graphics\\Lava.GIF", Size)

    Badrock = Load_Texture("Graphics\\badrock.png", Size)

    Brick = Load_Texture("Graphics\\Brick.png", Size)

    netherrock = Load_Texture("Graphics\\netherrock.png", Size)

    Black = Load_Texture("Graphics\\Black.png",Size)

    Texture_Tags = {"1" : Wood, "2" : Cobblestone, "3" : Stone, "4" : Stone1, "5" : Lava, "6" : Badrock, "7" : Brick, "8" : netherrock, "9" : Black}
  

    
