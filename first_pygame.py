# Import pygame
import pygame

# Initialize pygame
pygame.init()

# Make a screen with a size. It must be a TUPLE.
screen_size = (512, 480) # that's how big background.png is!
pygame_screen = pygame.display.set_mode(screen_size) # pygame's syntax for setting screen

pygame.display.set_caption('Robin Hood') # set's caption on the top of the game window

# ======================VARIABLES FOR OUR GAME=============================== #
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')

# =======================Main Game Loop====================================== #
game_on = True
while game_on:
    #Listen for events and quit if the user clicks X (apple red dot at top L of window)
    for even in pygame.get():
 