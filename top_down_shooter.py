import pygame
from pygame.locals import *
import sys
import random

pygame.init()

tela = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.x = 480//2
        self.y = 640//2
        self.width = 32
        self.height = 32
        
    def main(self, display):
        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), self.width)

player = Player()

while True:
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (255, 255, 255), (player.x, player.y), player.width)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    player.main(tela)       
    clock.tick(30)