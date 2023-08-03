import pygame
from pygame.locals import *
import sys

pygame.init()

# Set up the window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('RPG')
fpd = pygame.time.Clock()
background = pygame.image.load("python/sprites/background.png").convert_alpha()
panel = pygame.image.load("python/sprites/panel.png").convert_alpha()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)
green = (0, 155, 0)
medium_green = (0, 100, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

class Hero:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.alive = True
        self.image_list = [pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_1.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_2.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_3.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_4.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_5.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_6.png")]
        for i in range(len(self.image_list)):
            self.image_list[i] = pygame.transform.scale(self.image_list[i], ((self.image_list[i].get_width() * 3), (self.image_list[i].get_height() * 3)))
        self.image = self.image_list[0]
        self.image_index = 0
        self.update_index = pygame.time.get_ticks()
        #self.image = pygame.transform.scale(self.image, ((self.image.get_width() * 3), (self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 210
        font = pygame.font.SysFont("Arial", 20)
        self.text = font.render(self.name, True, WHITE)


    def attack(self, enemy):
        enemy.health -= self.strength - enemy.defense
        pygame.time.wait(120)
        enemy.health -= self.strength - enemy.defense

    def update(self):
        animation_cooldown = 100
        self.image = self.image_list[self.image_index]
        pygame.time.wait(120)
        if pygame.time.get_ticks() - self.update_index > animation_cooldown:
            self.image_index += 1
            self.update_index = pygame.time.get_ticks()
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, red, (500, 435, 280 - ((280 / 100) * (100 - self.health)), 20))
        pygame.draw.rect(screen, green, (500, 435, 280, 20))
        pygame.draw.rect(screen, medium_green, (500, 435, 280, 15))
        screen.blit(self.text, (423, 435))
        

class knight:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.alive = True
        self.update_index = pygame.time.get_ticks()
        self.image_list = [pygame.image.load("python/sprites/Boss/idle/tile000.png"), pygame.image.load("python/sprites/Boss/idle/tile001.png"), pygame.image.load("python/sprites/Boss/idle/tile002.png"), pygame.image.load("python/sprites/Boss/idle/tile003.png")]
        for i in range(len(self.image_list)):
            self.image_list[i] = pygame.transform.scale(self.image_list[i], ((self.image_list[i].get_width() * 3), (self.image_list[i].get_height() * 3)))
        self.image = self.image_list[0]
        self.image_index = 0
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * 3), (self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 155
        font = pygame.font.SysFont("Arial", 20)
        self.text = font.render(self.name, True, WHITE)

    def attack(self, hero):
        hero.health -= self.strength - hero.defense

    def update(self):
        animation_cooldown = 100
        self.image = self.image_list[self.image_index]
        if pygame.time.get_ticks() - self.update_index > animation_cooldown:
            self.image_index += 1
            self.update_index = pygame.time.get_ticks()
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, red, (500, 495, 280 - ((280 / 100) * (100 - self.health)), 20))
        pygame.draw.rect(screen, green, (500, 495, 280, 20))
        pygame.draw.rect(screen, medium_green, (500, 495, 280, 15))
        screen.blit(self.text, (425, 495))



# Create entitys
player = Hero("Player", 100, 10, 5)
villain = knight("Villain", 100, 10, 5)


# Start the game loop
running = True
while running:
    # Fill the background with white
    screen.blit(background, (0, 0))
    screen.blit(panel, (0, screen_height - bottom_panel))

    # Draw the player on the screen
    player.update()

    # Draw the enemy on the screen
    villain.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update the display
    pygame.display.update()
    fpd.tick(60)