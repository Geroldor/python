import pygame
from pygame.locals import *
import sys
import random

pygame.init()

# Set up the window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))

#game variables
current_fighter = 1
total_fighters = 2
action_cooldown = 0
action_wait_time = 30
attack = False
potion = False
clicked = False



pygame.display.set_caption('RPG')
fpd = pygame.time.Clock()
background = pygame.image.load("python/sprites/background.png").convert_alpha()
panel = pygame.image.load("python/sprites/panel.png").convert_alpha()
sword_icon = pygame.image.load("python/sprites/sword.png").convert_alpha()

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
        self.max_health = health
        self.health = health
        self.strength = strength
        self.defense = defense
        self.alive = True
        self.image_list = []
        self.image_idle_list = [pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_1.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_2.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_3.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_4.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_5.png"), pygame.image.load("python/sprites/Warrior/Individual/idle/Warrior_Idle_6.png")]
        for i in range(len(self.image_idle_list)):
            self.image_idle_list[i] = pygame.transform.scale(self.image_idle_list[i], ((self.image_idle_list[i].get_width() * 3), (self.image_idle_list[i].get_height() * 3)))
        self.image_attack_list = []
        for i in range(12):
            self.image_attack_list.append(pygame.image.load("python/sprites/Warrior/Individual/Attack/Warrior_Attack_" + str(i + 1) + ".png"))
        for i in range(len(self.image_attack_list)):
            self.image_attack_list[i] = pygame.transform.scale(self.image_attack_list[i], ((self.image_attack_list[i].get_width() * 3), (self.image_attack_list[i].get_height() * 3)))
        self.image_list = self.image_idle_list
        self.image = self.image_list[0]
        self.image_index = 0
        self.update_index = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 210
        font = pygame.font.SysFont("Arial", 20)
        self.text = font.render(self.name, True, WHITE)
        h = str(self.health) + "/" + str(self.max_health)
        self.health_text = font.render(h, True, WHITE)

    def Health_Bar(self):
        life_percentage = (self.health / self.max_health)
        healthbar_percentage = life_percentage * 100
        current_health = (280 / 100) * healthbar_percentage
        pygame.draw.rect(screen, red, (500, 435, 280, 20))
        pygame.draw.rect(screen, green, (500, 435, current_health, 20))
        pygame.draw.rect(screen, medium_green, (500, 435, current_health, 15))
        screen.blit(self.text, (425, 435))
        screen.blit(self.health_text, (705, 455))



    def attack(self, enemy):
        self.image_list = self.image_attack_list
        enemy.health -= self.strength + random.randint(0, 25) - enemy.defense
        if enemy.health <= 0:
            enemy.health = 0
            enemy.alive = False
        

    def update(self):
        self.Health_Bar()
        animation_cooldown = 100
        self.image = self.image_list[self.image_index]
        if self.image_list == self.image_attack_list:
            if self.image_index == 11:
                self.image_list = self.image_idle_list
        if pygame.time.get_ticks() - self.update_index > animation_cooldown:
            self.image_index += 1
            self.update_index = pygame.time.get_ticks()
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        screen.blit(self.image, self.rect)
        

class knight:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.max_health = health
        self.health = health
        self.strength = strength
        self.defense = defense
        self.alive = True
        self.update_index = pygame.time.get_ticks()
        # /home/geraldo/Documentos/faculdade/python/sprites/enemy/Bringer-Of-Death/Individual Sprite/Idle/Bringer-of-Death_Idle_8.png
        self.image_idle_list = [pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_1.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_2.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_3.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_4.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_5.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_6.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_7.png"), pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Idle/Bringer-of-Death_Idle_7.png")]
        
        for i in range(len(self.image_idle_list)):
            self.image_idle_list[i] = pygame.transform.scale(self.image_idle_list[i], ((self.image_idle_list[i].get_width() * 3), (self.image_idle_list[i].get_height() * 3)))
        self.image_attack_list = []
        for i in range(10):
            self.image_attack_list.append(pygame.image.load("python/sprites/enemy/Bringer-Of-Death/Attack/Bringer-of-Death_Attack_" + str(i + 1) + ".png"))
        for i in range(len(self.image_attack_list)):
            self.image_attack_list[i] = pygame.transform.scale(self.image_attack_list[i], ((self.image_attack_list[i].get_width() * 3), (self.image_attack_list[i].get_height() * 3)))
        self.image_list = self.image_idle_list
        self.image = self.image_idle_list[0]
        self.image_index = 0
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * 3), (self.image.get_height() * 3)))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 65
        font = pygame.font.SysFont("Arial", 20)
        self.text = font.render(self.name, True, WHITE)
        h = str(self.health) + "/" + str(self.max_health)
        self.health_text = font.render(h, True, WHITE)

    def Health_Bar(self):
        life_percentage = (self.health / self.max_health)
        healthbar_percentage = life_percentage * 100
        current_health = (280 / 100) * healthbar_percentage
        pygame.draw.rect(screen, red, (500, 495, 280, 20))
        pygame.draw.rect(screen, green, (500, 495, current_health, 20))
        pygame.draw.rect(screen, medium_green, (500, 495, current_health, 15))
        screen.blit(self.text, (425, 495))
        screen.blit(self.health_text, (705, 515))

    def attack(self, hero):
        self.image_list = self.image_attack_list
        hero.health -= self.strength + random.randint(5, 25) - hero.defense
        if hero.health <= 0:
            hero.health = 0
            hero.alive = False

    def update(self):
        animation_cooldown = 100
        self.image = self.image_list[self.image_index]
        if pygame.time.get_ticks() - self.update_index > animation_cooldown:
            self.image_index += 1
            self.update_index = pygame.time.get_ticks()
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        screen.blit(self.image, self.rect)
        self.Health_Bar()
        if self.image_list == self.image_attack_list:
            if self.image_index == 6:
                self.image_list = self.image_idle_list
                self.image_index = 0
        

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

    # reset the actions
    attack = False
    target = None
    pos = pygame.mouse.get_pos()
    if villain.rect.collidepoint(pos):
        if clicked:
            attack = True
            target = villain
    # player action
    
    if player.alive:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                # Look for player action
                if attack and target != None:
                    player.attack(villain)
                    current_fighter += 1
                    action_cooldown = 0
    
    # enemy action
    if villain.alive:
        if current_fighter == 2:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                # Look for enemy action
                villain.attack(player)
                current_fighter -= 1
                action_cooldown = 0
    
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    # Update the display
    pygame.display.update()
    fpd.tick(60)