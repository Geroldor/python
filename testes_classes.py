import pygame
from pygame import *
import math
import random


#inicia o jogo
pygame.init()

#tela
HEIGHT = 768
WIDTH = 1366
DIMENSIONS = (WIDTH, HEIGHT)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("top-down shooter test")

#random
words = ["porra", "caralho", "filho da puta", "arrombado", "pagão", "herege", "rato", "inseto", "cretino", "vagabunda", "puta", "fiat marea", "beta", "machista", "homofobico", "bicha", "gay", "nazista"]

#mouse
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

#classe da parede
class Wall:
    def __init__():

#classe da bala
class Ammo(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__() 
        font =  pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.image = font.render("°", True, (255, 255, 255)).convert()
        #self.image = font.render(random.choice(words), True, (255, 255, 255))
        #self.image = pygame.image.load("pygame/bullet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.posicx = x
        self.posicy = y
        self.speed = 15
        self.angle = angle
        self.vel_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.vel_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

    def AmmoMove(self):
        screen.blit(self.image, (self.posicx, self.posicy))
        self.posicx += self.vel_x
        self.posicy += self.vel_y
        self.rect.x = int(self.posicx)
        self.rect.y = int(self.posicy)

    def update(self):
        self.AmmoMove()

#classe player
class Player(pygame.sprite.Sprite):
    def __init__(self, posicx, posicy, speed):
        super().__init__()
        self.posicx = posicx
        self.posicy = posicy
        font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.image = font.render(">>>:", True, (255, 255, 255))
        #self.image = pygame.image.load("python/player_test.png")
        self.image_base = self.image
        self.rect_base = self.image_base.get_rect()
        self.rect = self.rect_base.copy()
        self.speed = speed
        self.shoot = False
        self.shoot_cooldown = 0
    
    def PlayerRotation(self):
        self.mouse_coord = pygame.mouse.get_pos()
        self.x_change_player = (self.mouse_coord[0] - self.rect_base.centerx)
        self.y_change_player = (self.mouse_coord[1] - self.rect_base.centery)
        self.angle = math.degrees(math.atan2(self.y_change_player, self.x_change_player))
        self.image = pygame.transform.rotate(self.image_base, -self.angle)
        self.rect = self.image.get_rect(center = self.rect_base.center)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.posicy > 0:
            self.posicy -= self.speed
        if key[pygame.K_s] and self.posicy < HEIGHT:
            self.posicy += self.speed
        if key[pygame.K_a] and self.posicx > 0:
            self.posicx -= self.speed
        if key[pygame.K_d] and self.posicx < WIDTH:
            self.posicx += self.speed
        if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
            self.speed = 3
        else:
            self.speed = 8
        #if self.posicx > WIDTH:
        #    self.posicx = 0
        #if self.posicx < 0:
        #    self.posicx = WIDTH
        #if self.posicy > HEIGHT:
        #    self.posicy = 0
        #if self.posicy < 0:
        #    self.posicy = HEIGHT

        self.rect_base.center = (self.posicx, self.posicy)
        self.rect.center = self.rect_base.center

    def Shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 5
            self.bullet = Ammo(self.posicx, self.posicy, self.angle)
            bullet_group.append(self.bullet)
            all_sprites.append(self.bullet)

    def update(self):
        screen.blit(self.image, self.rect)
        self.move()
        self.PlayerRotation()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    

#Jogo
turtle = Player(WIDTH/2, HEIGHT/2, 8)
game = True
all_sprites = []
bullet_group = []
all_sprites.append(turtle)
while game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            exit()

    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game = False
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed() == (1, 0, 0):
        turtle.shoot = True
        turtle.Shooting()
    else:
        turtle.shoot = False

    screen.fill((0,0,0))
    #screen.blit(turtle.image, turtle.rect)
    #turtle.update()
    for b in bullet_group:
        b.AmmoMove()
    
    for sprite in all_sprites:
        sprite.update()


    pygame.display.update()
    clock.tick(30)
  