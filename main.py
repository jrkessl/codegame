import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from pygame.surface import Surface
from pygame.locals import *

running = True
SQUARE_SIZE = 32

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("soldier1.png")
        self.rect = self.image.get_rect() # Creates a Rect to store the position of the player
        self.rect.topleft = (10*SQUARE_SIZE, 10*SQUARE_SIZE) # Sets the starting position of the player

        self.isMovingLenght = SQUARE_SIZE # SQUARE_SIZE is the size of one tile (in pixels)
        self.isMovingCount = 0
        self.movingDirection = ' ' # direction the player is facing. Can be: N (north), W (west), etc. Also NE (northeast), NW, SE, SW. Or space (" ") for being still. 
        self.facingDirection = 'E' # default to looking right (east)
    
    # This method activates when the key happens to be pressed down just now. 
    def update(self):
        if (self.movingDirection == ' '): # If player is still 
            keys = pygame.key.get_pressed() # Get the keys that are pressed down now 
            if keys[pygame.K_LEFT]: # If the left arrow is being held down
                # Is the player already moving?
                if (self.movingDirection == ' '): # If the player is still
                    self.movingDirection = 'W' # Set the moving direction to left (west)
                    self.rect.move_ip(-1, 0) # move 1 pixel to left
                    self.isMovingCount = self.isMovingCount + 1
                else: # If the player is already moving
                    if (self.isMovingCount < self.isMovingLenght): # If it has not yet moved a full square
                        self.rect.move_ip(-1, 0) # move 1 pixel to left
                        self.isMovingCount = self.isMovingCount + 1
                    else: # If it has already moved a full square
                        self.movingDirection = ' '
                        self.isMovingCount = 0  
            elif keys[pygame.K_RIGHT]: # If the right arrow is being held down
                # Is the player already moving?
                if (self.movingDirection == ' '): # If the player is still
                    self.movingDirection = 'E' # Set the moving direction to right (east)
                    self.rect.move_ip(1, 0) # move 1 pixel to right
                    self.isMovingCount = self.isMovingCount + 1
                else: # If the player is already moving
                    if (self.isMovingCount < self.isMovingLenght): # If it has not yet moved a full square
                        self.rect.move_ip(1, 0) # move 1 pixel to right
                        self.isMovingCount = self.isMovingCount + 1
                    else: # If it has already moved a full square
                        self.movingDirection = ' '
                        self.isMovingCount = 0  
            elif keys[pygame.K_UP]: # If the up arrow is being held down
                # Is the player already moving?
                if (self.movingDirection == ' '): # If the player is still
                    self.movingDirection = 'N' # Set the moving direction to up (north)
                    self.rect.move_ip(0, -1) # move 1 pixel up
                    self.isMovingCount = self.isMovingCount + 1
                else: # If the player is already moving
                    if (self.isMovingCount < self.isMovingLenght): # If it has not yet moved a full square
                        self.rect.move_ip(0, -1) # move 1 pixel up
                        self.isMovingCount = self.isMovingCount + 1
                    else: # If it has already moved a full square
                        self.movingDirection = ' '
                        self.isMovingCount = 0  
            elif keys[pygame.K_DOWN]: # If the down arrow is being held down
                # Is the player already moving?
                if (self.movingDirection == ' '): # If the player is still
                    self.movingDirection = 'S' # Set the moving direction to down (south)
                    self.rect.move_ip(0, 1) # move 1 pixel down
                    self.isMovingCount = self.isMovingCount + 1
                else: # If the player is already moving
                    if (self.isMovingCount < self.isMovingLenght): # If it has not yet moved a full square
                        self.rect.move_ip(0, 1) # move 1 pixel down
                        self.isMovingCount = self.isMovingCount + 1
                    else: # If it has already moved a full square
                        self.movingDirection = ' '
                        self.isMovingCount = 0
        else: # If the player is already moving
            if (self.isMovingCount < self.isMovingLenght): # If it has not yet moved a full square
                if (self.movingDirection == 'W'):
                    self.rect.move_ip(-1, 0) # move 1 pixel to left
                elif (self.movingDirection == 'E'):
                    self.rect.move_ip(1, 0) # move 1 pixel to right
                elif (self.movingDirection == 'N'):
                    self.rect.move_ip(0, -1) # move 1 pixel up
                elif (self.movingDirection == 'S'):
                    self.rect.move_ip(0, 1) # move 1 pixel down
                elif (self.movingDirection == 'NW'):
                    self.rect.move_ip(-1, -1) # move 1 pixel to left and 1 pixel up
                elif (self.movingDirection == 'NE'):
                    self.rect.move_ip(1, -1) # move 1 pixel to right and 1 pixel up
                elif (self.movingDirection == 'SW'):
                    self.rect.move_ip(-1, 1) # move 1 pixel to left and 1 pixel down
                elif (self.movingDirection == 'SE'):
                    self.rect.move_ip(1, 1) # move 1 pixel to right and 1 pixel down
                self.isMovingCount = self.isMovingCount + 1
                print("moving...")
            else: # If it has already moved a full square
                self.movingDirection = ' '
                self.isMovingCount = 0 
                print("stopped!")
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
        
pygame.init()

# Set game speed
FPS = 60
FramePerSec = pygame.time.Clock()

# Prepare game window
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

frames=0 # Frame counter, for debugging 

renderSurface = Surface((windowWidth, windowHeight)) # Create a surfate
renderSurface.blit(background, (0, 0)) # blit the static background image onto it 

while running:

    # Check if we are closing 
    if pygame.event.peek(pygame.QUIT): # User pressed the window close button
        running = False
        break

    # players play the game 
    all_sprites.update() # Calls update method of all players

    # players get drawn in the screen     
    all_sprites.draw(renderSurface) # Calls draw method of all players

    window.blit(renderSurface, (0, 0)) # render the scaled surface in the window
    pygame.display.update() # update the display
    FramePerSec.tick(FPS)

    print("frames = ", frames)
    frames += 1

    # Clear the background where the players were, so we don't have to re-draw the whole screen at every frame
    for entity in all_sprites:
        renderSurface.blit(background, entity.rect.copy(), entity.rect.copy()) # redraw the background where the player was

pygame.quit()

# parou em:
# https://www.patternsgameprog.com/strategy-game-1-start

# isso aqui parece interessante:
# https://github.com/Murasakiao/RTS_pygame