from os import kill
import pygame
from pygame import *
import math
import random

#inicia o jogo
pygame.init()

#tela
HEIGHT = 480
WIDTH = 720
DIMENSIONS = (WIDTH, HEIGHT)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("top-down shooter test")
pygame.display.set_allow_screensaver(True)
background =  pygame.image.load("python/ground.png")

#mouse
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

shots = ['•', '○', '°', '*', 'o', '.']

#classe da bala
class Ammo(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__() 
        font =  pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.image = font.render("•", True, (255, 255, 255)).convert_alpha()
        self.rect = self.image.get_rect()
        self.posicx = x
        self.posicy = y
        self.speed = 5
        self.angle = angle
        self.vel_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.vel_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

    def AmmoMove(self): #move a bala
        screen.blit(self.image, (self.posicx, self.posicy))
        self.posicx += self.vel_x
        self.posicy += self.vel_y
        self.rect.x = int(self.posicx)
        self.rect.y = int(self.posicy)

    def update(self):
        self.AmmoMove()

#classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posicx = WIDTH//2
        self.posicy = HEIGHT//2
        #font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        #self.image = font.render("<=>", True, (255, 255, 255)).convert_alpha()
        #self.image = pygame.transform.scale(self.image, (72, 72))
        self.image = pygame.transform.scale(pygame.image.load("Weapons/weaponR3.png"), (44, 44))
        self.image_base = self.image
        self.rect_base = self.image_base.get_rect()
        self.rect = self.rect_base.copy() 
        self.speed = 3
        self.shoot = False
        self.shoot_cooldown = 0
    
    def PlayerRotation(self):
        self.mouse_coord = pygame.mouse.get_pos() # pega as coordenadas do mouse
        self.x_change_player = (self.mouse_coord[0] - self.posicx) #calcula a diferença entre o X do player e o X do mouse
        self.y_change_player = (self.mouse_coord[1] - self.posicy) #calcula a diferença entre o Y do player e o Y do mouse
        self.angle = math.degrees(math.atan2(self.y_change_player, self.x_change_player)) #calcula a tangente pela equação abaixo e converte em graus
                                                                                          #(x_mouse - x_player)/(y_mouse - y_player)
        self.image = pygame.transform.rotate(self.image_base, -self.angle) #gira o player no grau obtido (a rotação no python é anti-horaria)
        self.rect = self.image.get_rect(center = self.rect_base.center) # atualiza o retangulo do player

    def move(self):
        key = pygame.key.get_pressed() 
        if key[pygame.K_w] and self.posicy > 0: #caso W seja pressionado, o objeto do player vai subir até o limite da tela
            self.posicy -= self.speed          #funciona igual pra todos os outros casos

        if key[pygame.K_s] and self.posicy < HEIGHT: 
            self.posicy += self.speed

        if key[pygame.K_a] and self.posicx > 0:
            self.posicx -= self.speed

        if key[pygame.K_d] and self.posicx < WIDTH:
            self.posicx += self.speed

        self.rect_base.center = (self.posicx, self.posicy)
        self.rect.center = self.rect_base.center

    def Shooting(self):
        #isso aqui cria e prepara um tiro qualquer na classe Ammo
        if self.shoot_cooldown == 0: #verifica o intervalo de tiro
            self.shoot_cooldown = 10 #reseta o intervalon(quanto menor, mais parece uma metralhadora)

            self.bullet = Ammo(self.rect.centerx, self.rect.centery, self.angle) #cria um projetil na coordenada do player
            bullet_group.add(self.bullet) #coloca o projetil na lista de balas
            all_sprites.add(self.bullet) #coloca o projetil na lista de objetos

    def update(self):
        #atualiza o personagem de acordo com as suas funções

        screen.blit(self.image, self.rect) #imprime o personagem na coordenada do retangulo que ele ta contido
        self.move() #função de mover o personagem
        self.PlayerRotation() #função de girar o personagem

        if self.shoot_cooldown > 0: #verifica o intervalo de tiro (talvez tenha algo em time pra melhorar isso)
            self.shoot_cooldown -= 1

#Jogo

player_character = Player() #criação base do personagem do jogador
game = True #variavel que determina se o jogo ta rodando
#random_circle = pygame.Rect(50, 50, WIDTH/2, HEIGHT/2)
all_sprites = pygame.sprite.Group() #lista infinita para colocar TODOS os objetos do jogo, independente da classe usada na criação
bullet_group = pygame.sprite.Group() #lista infinita para colocar os projeteis
enemy_list = pygame.sprite.Group()
all_sprites.add(player_character) #insere o player na lista dos objetos
while game:
    
    for event in pygame.event.get(): #para funcionar a saida do jogo
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            exit()

    if event.type == KEYDOWN: #igual o de cima
        if event.key == pygame.K_ESCAPE:
            game = False
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed() == (1, 0, 0): #detectar o click do mouse para atirar
        player_character.shoot = True
        player_character.Shooting()
    else:
        player_character.shoot = False

    screen.fill((0, 128, 0))
    all_sprites.update()

    pygame.display.update() #atualiza a tela
    clock.tick(60) #determina o fps
  