import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Set up the window
background_color = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
class Player:
    def __init__(self, x, y, speed, damage):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
    
    def update(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 20, 20))

# Initialize game objects
player = Player(400, 300, 5, 1)

# Set up the game loop
running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update game state
    player.update()
    
    # Draw screen
    screen.fill(background_color)
    clock.tick(30)
    pygame.display.update()