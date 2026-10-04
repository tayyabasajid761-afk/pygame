import pygame
import random
# Initialize Pygame
pygame.init()
# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
# Sprite class representing the moving object 
class Sprite(pygame.sprite.Sprite):
# Constructor method
 def __init__(self,color,height,width):
    # Call to the parent class (Sprite) constructor
    super().__init__()
    #  Create the sprite's surface with dimension and color
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    # Get the sprit's rect defining its position and size
    self.rect = self.image.get_rect()
    # Set initial velocity 
    self.velocity = [random.choice([-1, 1]), random choice([-1, 1])] 
    # Method to update the sprite's position
 def update(self):
      self.rect.move_ip(self.velocity)
      boundary-hit = False
      if self.rect.left <= 0 or self.rect.right >= 500:
         self.velocity[0] = -self.velocity[0]
         boundary_hit = True
      if self.rect.top <= 0 or self.rect.bottom >= 400:
         self.velocity[1] = -self.velocity[1]
         boundary_hit = True
      if boundary_hit:
         pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
         pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

