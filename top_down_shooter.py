import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Set up the window
background_color = (0, 0, 0)
width = 800
height = 600
screen = pygame.display.set_mode((800, 600))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
class Player:
    def __init__(self, speed, damage):
        self.x = width // 2
        self.y = height // 2
        self.speed = speed
        self.damage = damage
        self.image = pygame.image.load("python/tps/sprites/seta.png")
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() // 2), (self.image.get_height() // 2)))
    
    def update(self):
        screen.blit(self.image, (self.x, self.y))

# Initialize game objects
player = Player(5, 1)

# Set up the game loop
running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[K_w]:
        player.y -= player.speed
    if key[K_s]:
        player.y += player.speed
    if key[K_a]:
        player.x -= player.speed
    if key[K_d]:
        player.x += player.speed
    
    if player.x < 0:
        player.x = width
    if player.x > width:    
        player.x = 0
    if player.y < 0:
        player.y = height
    if player.y > height:
        player.y = 0

    # Update game state
    player.update()
    
    clock.tick(30)
    pygame.display.update()