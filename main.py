import pygame

pygame.init()

# Load image and create window
image = pygame.image.load("grass2.png") # load image 
window = pygame.display.set_mode(image.get_size()) # create window the size of the image
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

    # Render
    window.blit(image, (0, 0))
    pygame.display.update()

pygame.quit()

# parou em:
# https://www.patternsgameprog.com/strategy-game-1-start

# isso aqui parece interessante:
# https://github.com/Murasakiao/RTS_pygame