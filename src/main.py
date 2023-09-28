## imports

import pygame
import sys
from src.player import Player
from game_functions import *





from settings import *


## initialize pygame

pygame.init()

## define screen

screen = pygame.display.set_mode((screen_width, screen_height))

# define our player

player: Player = Player(GREEN, 50, 30)

## main function

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(WHITE)
        draw(screen, player.image)
        pygame.display.update()
    
    pygame.quit()
    sys.exit()
            


if __name__ == "__main__":
    main()

