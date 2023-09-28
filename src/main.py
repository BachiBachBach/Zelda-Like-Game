## import pygame

import pygame

## import sys

import sys

## import settings

from settings import *


## initialize pygame

pygame.init()

## define screen

screen = pygame.display.set_mode((screen_width, screen_height))

## main function

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(WHITE)
        pygame.display.update()
    
    pygame.quit()
    sys.exit()
            


if __name__ == "__main__":
    main()

