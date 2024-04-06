import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to present a single alien in fleet."""
    
    def __init__(self, ai_game):
        """Initialize the alien and set a starting position"""
    
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/enemy_ship.bmp')
        self.rect = self.image.get_rect()
        
        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the specified position"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    
    def check_edges(self):
        """Returns True if is at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False