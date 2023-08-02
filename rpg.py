import pygame
from pygame.locals import *
import sys

pygame.init()

# Set up the window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('RPG')
fpd = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

class Hero:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.alive = True

    def attack(self, enemy):
        enemy.health -= self.strength - enemy.defense

    def take_damage(self, damage):
        self.health -= damage

    def update(self):
        pygame.draw.rect(screen, red, (150, 200, 40, 40))
        pygame.draw.rect(screen, blue, (130, 260, 80, 10))
        

class Enemy:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, hero):
        hero.health -= self.strength - hero.defense

    def take_damage(self, damage):
        self.health -= damage

    def update(self):
        pygame.draw.rect(screen, blue, (350, 200, 40, 40))
        pygame.draw.rect(screen, yellow, (330, 260, 90, 10))

class Boss:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, hero):
        hero.health -= self.strength - hero.defense

    def take_damage(self, damage):
        self.health -= damage

class walls:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Create entitys
player = Hero("Player", 100, 10, 5)
villain = Enemy("Villain", 100, 10, 5)


# Start the game loop
running = True
while running:
    # Fill the background with white
    screen.fill(green)

    # Draw the player on the screen
    player.update()

    # Draw the enemy on the screen
    villain.update()

    # Draw the walls on the screen
    pygame.draw.rect(screen, gray, (0, 0, 640, 20))
    pygame.draw.rect(screen, gray, (0, 0, 20, 480))
    pygame.draw.rect(screen, gray, (0, 460, 640, 20))
    pygame.draw.rect(screen, gray, (620, 0, 20, 480))

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update the display
    pygame.display.update()
    fpd.tick(60)