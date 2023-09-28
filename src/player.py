import pygame
from src.settings import *

## Define player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 38))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()