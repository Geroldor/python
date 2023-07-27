import pygame
from pygame.locals import *
import sys
import random

pygame.init()

tela = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.x = 480/2
        self.y = 640/2
        self.width = 5
        self.height = 10
        
    def main(self, display):
        pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, self.width, self.height))


player = Player()

while True:
    tela.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    player.main(tela)       
