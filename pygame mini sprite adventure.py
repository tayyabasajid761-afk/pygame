import pygame
def main():
    pygame.init()
# PART 1: Create the game screen
screen_width, screen_height = 500, 400
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Mini Sprite Advanture")
# PART 2: Set sprite position and size
x, y = 50, 50
sprite_width, sprite_height = 60, 60
speed = 4
# PART 3: Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 125, 225)
RED   = (255, 0, 0)
GREEN =(0, 255 ,0)
YELLOW = (255, 255, 0)
current_color = WHITE
clock = pygame.time.Clock()
running = True
# PART 4 Game loop