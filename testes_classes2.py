from os import kill
import pygame
from pygame import *
import math
import random


width = 720
height = 480

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("top-down shooter test 2")
pygame.display.set_allow_screensaver(True)
clock = pygame.time.Clock()
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_move_r_list = [pygame.image.load("dungeonSprites/ghost/tile008.png").convert(), pygame.image.load("dungeonSprites/ghost/tile009.png"), pygame.image.load("dungeonSprites/ghost/tile010.png"), pygame.image.load("dungeonSprites/ghost/tile011.png")]
        self.sprite_move_l_list = [pygame.image.load("dungeonSprites/ghost/tile012.png"), pygame.image.load("dungeonSprites/ghost/tile013.png"), pygame.image.load("dungeonSprites/ghost/tile014.png"), pygame.image.load("dungeonSprites/ghost/tile015.png")]
        self.sprite_move_list = self.sprite_move_r_list
        self.current_sprite = 0
        #font = pygame.font.SysFont(font.get_default_font(), 32)
        #self.image = font.render("Evandro", True, (255, 255, 255)).convert_alpha()
        self.image = self.sprite_move_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.posicx = x
        self.posicy = y
        self.speed = 2

    def update(self):
        self.current_sprite += 0.17
        if self.current_sprite >= len(self.sprite_move_r_list):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprite_move_list[int(self.current_sprite)], (44, 44))
        self.rect = self.image.get_rect()
        self.rect.center = (self.posicx, self.posicy)
        screen.blit(self.image, self.rect)
        


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

#classe Gun
class Gun(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image_r = pygame.transform.scale(pygame.image.load("Weapons/weaponR3.png"), (1383/32, 615/32))
        self.image_l = pygame.transform.scale(pygame.image.load("Weapons/weaponR3_1.png"), (1383/32, 615/32))
        self.image = self.image_r
        self.image_base = self.image
        self.rect_base = self.image_base.get_rect()
        self.rect = self.rect_base.copy()
        self.rect.center = pos
        self.posicx = self.rect.center[0]
        self.posicy = self.rect.center[1]
        self.speed = 3
        self.shoot = False
        self.shoot_cooldown = 0
    
    def GunRotation(self):
        self.mouse_coord = pygame.mouse.get_pos() # pega as coordenadas do mouse
        if self.mouse_coord[0] < self.posicx:
            self.image = self.image_l
            self.image = pygame.transform.flip(self.image, True, True)
            self.image_base = self.image
            self.rect = self.image.get_rect(center = self.rect_base.center)
            self.rect_base = self.image_base.get_rect(center = self.rect.center)
        else:
            self.image = self.image_r
            self.image_base = self.image
            self.rect = self.image.get_rect(center = self.rect_base.center)

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

        if key[pygame.K_s] and self.posicy < height: 
            self.posicy += self.speed

        if key[pygame.K_a] and self.posicx > 0:
            self.posicx -= self.speed

        if key[pygame.K_d] and self.posicx < width:
            self.posicx += self.speed

        self.rect_base.center = (self.posicx, self.posicy)
        self.rect.center = self.rect_base.center

    def Shooting(self):
        #isso aqui cria e prepara um tiro qualquer na classe Ammo
        if self.shoot_cooldown == 0: #verifica o intervalo de tiro
            self.shoot_cooldown = 10 #reseta o intervalon(quanto menor, mais parece uma metralhadora)

            self.bullet = Ammo(player.rect.centerx+25, player.rect.centery+20, self.angle) #cria um projetil na coordenada do player
            bullet_group.add(self.bullet) #coloca o projetil na lista de balas
            all_sprites.add(self.bullet) #coloca o projetil na lista de objetos

    def update(self):
        #atualiza o personagem de acordo com as suas funções

        screen.blit(self.image, self.rect) #imprime o personagem na coordenada do retangulo que ele ta contido
        self.move() #função de mover o personagem
        self.GunRotation() #função de girar o personagem

        if self.shoot_cooldown > 0: #verifica o intervalo de tiro (talvez tenha algo em time pra melhorar isso)
            self.shoot_cooldown -= 1


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.posicx = width//2
        self.posicy = height//2
        self.sprite_move_r_list = [pygame.image.load("dungeonSprites/mHero/tile008.png"), pygame.image.load("dungeonSprites/mHero/tile009.png"), pygame.image.load('dungeonSprites/mHero/tile010.png'), pygame.image.load('dungeonSprites/mHero/tile011.png')]
        self.sprite_move_l_list = [pygame.image.load("dungeonSprites/mHero/tile012.png"), pygame.image.load("dungeonSprites/mHero/tile013.png"), pygame.image.load('dungeonSprites/mHero/tile014.png'), pygame.image.load('dungeonSprites/mHero/tile015.png')]
        self.sprite_move_list = self.sprite_move_r_list
        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprite_move_r_list[self.current_sprite], (44, 44))
        self.rect = self.image.get_rect()
        self.rect.center = (self.posicx, self.posicy)
        self.speed = 3
        self.animate_right = False
        self.animate_left = False
        self.animate_up = False
        self.animate_down = False
        self.animate = False

    def animatePlayer(self):

        
        if self.animate:
            self.image = pygame.transform.scale(self.sprite_move_list[int(self.current_sprite)], (44, 44))
            screen.blit(self.image, (self.posicx, self.posicy))
        else:
            self.image = pygame.transform.scale(self.sprite_move_list[0], (44, 44))
            screen.blit(self.image, (self.posicx, self.posicy))
        
        self.current_sprite += 0.17
        if self.current_sprite >= len(self.sprite_move_r_list):
            self.current_sprite = 0
        
        
        self.animate = False
        
    def LookPlayer(self):
        #faz o player virar para o mouse no eixo x
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < self.posicx:
            self.sprite_move_list = self.sprite_move_l_list
            self.image = pygame.transform.scale(self.sprite_move_list[0], (44, 44))

        if mouse_pos[0] > self.posicx:
            self.sprite_move_list = self.sprite_move_r_list
            self.image = pygame.transform.scale(self.sprite_move_list[0], (44, 44))

    def MovePlayer(self):
        #move o player e anime de acordo com os sprites de sprite_move_r_list
        #o player se vira para a esquerda e direita de acordo com a direção que ele está indo
        key = pygame.key.get_pressed()

        if key[pygame.K_w] and self.posicy > 0:
            self.animate = True
            self.posicy -= self.speed          

        if key[pygame.K_s] and self.posicy < height: 
            self.animate = True
            self.posicy += self.speed

        if key[pygame.K_a] and self.posicx > 0:
            self.animate = True
            self.posicx -= self.speed

        if key[pygame.K_d] and self.posicx < width: 
            self.animate = True
            self.posicx += self.speed

        if pygame.mouse.get_pressed() == (1, 0, 0): #detectar o click do mouse para atirar
            gun.shoot = True
            gun.Shooting()
        else:
            gun.shoot = False

    def death_animate(self):
        self.death_list = [pygame.image.load("dungeonSprites/mHero/tile040.png"), pygame.image.load("dungeonSprites/mHero/tile041.png"), pygame.image.load('dungeonSprites/mHero/tile042.png'), pygame.image.load('dungeonSprites/mHero/tile043.png')]
        current = 0
        while current < 4:
            self.image = pygame.transform.scale(self.death_list[int(current)], (44, 44))
            current += 0.17


    def death(self):
        for monster in monster_group:
            if pygame.sprite.collide_rect(self, monster):
                self.death_animate()
                self.kill()
                gun.kill()
                pygame.quit()
                exit()
        
    def update(self):
        self.MovePlayer()
        self.animatePlayer()
        self.LookPlayer()
        self.death()
        self.rect.center = (self.posicx, self.posicy)

player = Player()
gun = Gun((player.rect.centerx+25, player.rect.centery+30))
ghost = Ghost(random.randint(0, width), random.randint(0, height))
bullet_group = pygame.sprite.Group()
monster_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(ghost)
all_sprites.add(player)
all_sprites.add(gun)
monster_group.add(ghost)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 80, 0))

    for bullet in bullet_group:
        for monster in monster_group:
            if pygame.sprite.collide_rect_ratio(0.5)(bullet, monster) :
                monster.kill()
                bullet.kill()
                ghost = Ghost(random.randint(0, width), random.randint(0, height))
                monster_group.add(ghost)
                all_sprites.add(ghost)


    all_sprites.update()
    pygame.display.update()
    clock.tick(60)