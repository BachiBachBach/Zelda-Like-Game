from player import Player

# draw function



def draw(screen, *items: Player):
    for item in items:
        screen.blit(item.image)