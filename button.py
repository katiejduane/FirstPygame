# start button!
import pygame.font

class Start_Button(object):
    def __init__(self, screen):
        # Print the start button
        self.screen = screen
        # How big is the screen? We need a rect
        self.screen_rect = screen.get_rect()
        # Set screen width
        self.width = 100
        # Set height
        self.height = 50
        # Set color
        green = (0,200,150) # can also make variables with color names and RGB numbers in a tuple
        self.button_color = 150,50,50
        self.text_color = 255, 255, 255
        # get font from pygame!
        self.font = pygame.font.Font(None, 52)
        # Set rect of button
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # Set location of rect
        self.rect.center = self.screen_rect.center

    def setup_message(self):
        # Set up the message!
        self.image_message = self.font.render("Play", True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color, self.rect)
        # actually DRAW the button
        self.screen.blit(self.image_message, self.image_message_rect)