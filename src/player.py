import pygame
from settings import *


## Define player class

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        # define health
        self.hp = 100
        
        # define damage
        self.damage = 10
        
        # define image
        self.image = pygame.Surface((width, height))
        
        # define fill color
        self.image.fill(color)
        
        # get the rect of the player
        self.rect = self.image.get_rect()