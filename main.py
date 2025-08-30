import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.surface import Surface

pygame.init()

# Load background image and create window
background = pygame.image.load("grass2.png") # load background image
windowWidth = background.get_width() # capture dimensions of background image
windowHeight = background.get_height()

window = pygame.display.set_mode((windowWidth, windowHeight), HWSURFACE | DOUBLEBUF | RESIZABLE) # Creates game window with the size of the background image, and some options 
pygame.display.set_caption("Code Game (working title)") # set window title

running = True
while running:

    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    renderSurface = Surface((windowWidth, windowHeight)) # Create a surfate
    renderSurface.blit(background, (0, 0)) # blit the background image onto it 

    window.blit(renderSurface, (0, 0)) # render the scaled surface in the window
    pygame.display.update() # update the display

pygame.quit()

# parou em:
# https://www.patternsgameprog.com/strategy-game-1-start

# isso aqui parece interessante:
# https://github.com/Murasakiao/RTS_pygame