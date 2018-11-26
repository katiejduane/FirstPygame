# Import pygame
import pygame

# Import my own classes
from Hero import Hero

# Import badguy!
from BadGuy import BadGuy

# Import Arrowwww
from Arrow import Arrow

#Get group and groupcollide from the Sprite Module
from pygame.sprite import Group, groupcollide

# Initialize pygame
pygame.init()

# Make a screen with a size. It must be a TUPLE.
screen_size = (512, 480) # that's how big background.png is!
pygame_screen = pygame.display.set_mode(screen_size) # pygame's syntax for setting screen

pygame.display.set_caption('Robin Hood') # set's caption on the top of the game window

theHero = Hero()

bad_boy = BadGuy()
bad_boys = Group()
bad_boys.add(bad_boy)

# arrows = []
arrows = Group()

# ======================VARIABLES FOR OUR GAME=============================== #
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
# heroLoc = {
#     'x':0,
#     'y':0
# }

bg_music = pygame.mixer.Sound('bg.wav')
bg_music.play()

# =======================Main Game Loop====================================== #
game_on = True
while game_on:
    # Listen for events and quit if the user clicks X (apple red dot at top L of window)
    # ======= Event Checker ======== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user clicked the red dot X
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 275: # right arrow key number
                theHero.should_move("right")
            elif event.key == 276:
                theHero.should_move("left")
            elif event.key == 273:
                theHero.should_move("up")
            elif event.key == 274:
                theHero.should_move("down")
            elif event.key == 32:
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)
            else:
                print (event.key)
        elif event.type == pygame.KEYUP: #the user released a key
            if event.key == 275: 
                theHero.should_move("right", False)
            elif event.key == 276:
                theHero.should_move("left", False)
            elif event.key == 273:
                theHero.should_move("up", False)
            elif event.key == 274:
                theHero.should_move("down", False)
            else:
                print (event.key)

    # ======= Draw Stuff! ========= #
    # We use blit to draw on the screen. blit = block image transfer
    # blit is a method that takes two args: what to draw and where to draw it!
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    # Draw the hero
    theHero.draw_me()
    # Draw the arrows
    for arrow in arrows:
        arrow.update_me()
        pygame_screen.blit(arrow_image, [arrow.x, arrow.y])

    arrow_hit = groupcollide(arrows, bad_boys, True, True)  

    # Draw the bad guys
    for bad_boy in bad_boys:
        bad_boy.update_me(theHero)
        pygame_screen.blit(monster_image, [bad_boy.x, bad_boy.y])
    
    pygame_screen.blit(hero_image, [theHero.x, theHero.y])
    pygame.display.flip()



 