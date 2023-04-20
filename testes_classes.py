import pygame
from pygame import *
import math

#inicia o jogo
pygame.init()

#tela
HEIGHT = 720
WIDTH = 1280
DIMENSIONS = (WIDTH, HEIGHT)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(DIMENSIONS)

#classe player
class Player:
    def __init__(self, posicx, posicy, speed):
        self.posicx = posicx
        self.posicy = posicy
        font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.img = font.render(">---", True, (255, 255, 255))
        #self.img = pygame.image.load(img)
        self.img_base = self.img
        self.rect_base = self.img_base.get_rect()
        self.rect = self.rect_base.copy()
        self.speed = speed
    
    def PlayerRotation(self):
        self.mouse_coord = pygame.mouse.get_pos()
        self.x_change_player = (self.mouse_coord[0] - self.rect_base.centerx)
        self.y_change_player = (self.mouse_coord[1] - self.rect_base.centery)
        self.angle = math.degrees(math.atan2(self.y_change_player, self.x_change_player))
        self.img = pygame.transform.rotate(self.img_base, -self.angle)
        self.rect = self.img.get_rect(center = self.rect_base.center)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.posicy -= self.speed
        if key[pygame.K_s]:
            self.posicy += self.speed
        if key[pygame.K_a]:
            self.posicx -= self.speed
        if key[pygame.K_d]:
            self.posicx += self.speed
        if self.posicx > WIDTH:
            self.posicx = 0
        if self.posicx < 0:
            self.posicx = WIDTH
        if self.posicy > HEIGHT:
            self.posicy = 0
        if self.posicy < 0:
            self.posicy = HEIGHT
        self.rect_base.center = (self.posicx, self.posicy)
        self.rect.center = self.rect_base.center

    def PlayerUpdate(self):
        self.move()
        self.PlayerRotation()

#mouse
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

#Jogo
turtle = Player(WIDTH/2, HEIGHT/2, 8)
game = True
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((0,0,0))
    screen.blit(turtle.img, turtle.rect) 
    turtle.PlayerUpdate()
    pygame.display.update()
    clock.tick(30)    