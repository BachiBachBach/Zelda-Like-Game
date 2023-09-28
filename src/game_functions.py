# draw function

def draw(screen, *items):
    for item in items:
        screen.blit(item.image)