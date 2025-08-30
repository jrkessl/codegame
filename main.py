import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.surface import Surface

pygame.init()

# Load background image and create window
window = pygame.display.set_mode((1024, 768), HWSURFACE | DOUBLEBUF | RESIZABLE) # Creates game window with set size, and some options 
pygame.display.set_caption("Code Game (working title)") # set window title
background = pygame.image.load("grass2.png") # load background image
renderWidth = background.get_width() # capture dimensions of background image
renderHeight = background.get_height()

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

    # Create a surfate and blit the background image onto it
    renderSurface = Surface((renderWidth, renderHeight))
    renderSurface.blit(background, (0, 0))

    # Scale rendering to window size
    windowWidth, windowHeight = window.get_size()
    renderRatio = renderWidth / renderHeight
    windowRatio = windowWidth / windowHeight
    if windowRatio <= renderRatio:
        rescaledSurfaceWidth = windowWidth
        rescaledSurfaceHeight = int(windowWidth / renderRatio)
        rescaledSurfaceX = 0
        rescaledSurfaceY = (windowHeight - rescaledSurfaceHeight) // 2
    else:
        rescaledSurfaceWidth = int(windowHeight * renderRatio)
        rescaledSurfaceHeight = windowHeight
        rescaledSurfaceX = (windowWidth - rescaledSurfaceWidth) // 2
        rescaledSurfaceY = 0

    # Scale the rendering to the window/screen size
    rescaledSurface = pygame.transform.scale(
        renderSurface, (rescaledSurfaceWidth, rescaledSurfaceHeight)
    )
    window.blit(rescaledSurface, (rescaledSurfaceX, rescaledSurfaceY)) # render the scaled surface in the window
    pygame.display.update() # update the display

pygame.quit()

# parou em:
# https://www.patternsgameprog.com/strategy-game-1-start

# isso aqui parece interessante:
# https://github.com/Murasakiao/RTS_pygame