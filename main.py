import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.surface import Surface
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("soldier1.png")
        
        self.rect = self.image.get_rect() # Creates a Rect to store the position of the player
        self.rect.center = (10*32, 10*32) # Sets the starting position of the player
 
    def update(self):
        pressed_keys = pygame.key.get_pressed() # pega a tecla pressionada 
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < windowWidth:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        if pressed_keys[K_UP]:
            if self.rect.top > 0:
                self.rect.move_ip(0, -5)
        
        if pressed_keys[K_DOWN]: # se apertou pra baixo 
            if self.rect.bottom < windowHeight: # se ainda não está na borda inferior 
                self.rect.move_ip(0, 5) # move 5 pixels pra baixo 
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
        
pygame.init()

# Load background image and create window
background = pygame.image.load("grass2.png") # load background image
windowWidth = background.get_width() # capture dimensions of background image
windowHeight = background.get_height()

window = pygame.display.set_mode((windowWidth, windowHeight), HWSURFACE | DOUBLEBUF | RESIZABLE) # Creates game window with the size of the background image, and some options 
pygame.display.set_caption("Code Game (working title)") # set window title

# Creates players
P1 = Player()

# Creates a group to hold sprites of all players
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

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

    # Calls draw method of all players
    # for entity in all_sprites:
    #     entity.draw(renderSurface)
    
    all_sprites.draw(renderSurface) # Calls draw method of all players
    all_sprites.update() # Calls update method of all players


    window.blit(renderSurface, (0, 0)) # render the scaled surface in the window
    pygame.display.update() # update the display

    

pygame.quit()

# parou em:
# https://www.patternsgameprog.com/strategy-game-1-start

# isso aqui parece interessante:
# https://github.com/Murasakiao/RTS_pygame