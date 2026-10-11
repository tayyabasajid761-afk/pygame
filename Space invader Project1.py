import math
import random
import pygame
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y =380
ENEMY_START_Y_MIN = 50
ENEMY_START_X_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
# Initialize Pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Background (Scaled to fit the screen window)
background = pygame.image.load('backg.jpg')
#====updated the background scaling to fit the screen dimension====
background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_WIDTH))
# caption and Icon
pygame.display.set_caption("Space Invander")
icon = pygame.image.load('ufo.png')
pygame.disply.set_icon(icon)
# Player (Scaled to 64*64)
playerImg = pygame.image.load('player.png')
playerImg = p