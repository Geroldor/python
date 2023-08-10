import pygame
from pygame.locals import *
import sys
import random

pygame.init()

tela = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
backgiund = pygame.image.load("python\sprites\\background.png")

class Player:
    def __init__(self):
        self.x = 640//2
        self.y = 480//2
        self.width = 32
        self.height = 32
        self.img = pygame.image.load("python\sprites\Warrior\Individual\idle\Warrior_Idle_1.png")        
        self.img = pygame.transform.scale(self.img, (self.width * 3, self.height * 3))
    
    def update(self):
        tela.blit(self.img, (self.x, self.y))
        
player = Player()

while True:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    player.update()
    clock.tick(30)