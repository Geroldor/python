from os import kill
import pygame
from pygame import *
import math
import random


#inicia o jogo
pygame.init()

#tela
HEIGHT = 480
WIDTH = 640
DIMENSIONS = (WIDTH, HEIGHT)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption("top-down shooter test")

#random
words = ["porra", "caralho", "filho da puta", "arrombado", "pagão", "herege", "rato", "inseto", "cretino", "vagabunda", "puta", "fiat marea", "beta", "machista", "homofobico", "bicha", "gay", "nazista"]

#mouse
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

#classe do meteoro fds
class Enemy(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.posicx = random.randint(0, WIDTH)
        self.posicy = random.randint(0, HEIGHT)
        font = pygame.font.SysFont(pygame.font.get_default_font(), size)
        self.image = font.render("EVANDRO", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(0, 7)
        self.speed_y = random.randint(0, 7)
        all_sprites.append(self)
        enemy_list.append(self)

    def move(self):
        self.posicx += self.speed_x
        self.posicy += self.speed_y

        if self.posicx >= WIDTH or self.posicx <= 0:
            self.speed_x *= -1
        if self.posicy >= HEIGHT or self.posicy <= 0:
            self.speed_y *= -1

    def update(self):
        screen.blit(self.image, (self.posicx, self.posicy))
        self.move()

#classe da bala
class Ammo(pygame.sprite.Sprite):
    def __init__(self, x, y, angle): #cria a bala
        super().__init__() 
        font =  pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.image = font.render("°", True, (255, 255, 255)).convert_alpha()
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

    def AmmoMove(self): #move a bala
        screen.blit(self.image, (self.posicx, self.posicy))
        self.posicx += self.vel_x
        self.posicy += self.vel_y
        self.rect.x = int(self.posicx)
        self.rect.y = int(self.posicy)

    def update(self):
        self.AmmoMove()

#classe player
class Player(pygame.sprite.Sprite):
    def __init__(self, posicx, posicy):
        #cria o player
        super().__init__()
        self.posicx = posicx
        self.posicy = posicy
        font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.image = font.render(">>>:", True, (255, 255, 255))
        #self.image = pygame.image.load("python/player_test.png") #ta de reserva caso eu queira testar com uma foto
        self.image_base = self.image
        self.rect_base = self.image_base.get_rect()
        self.rect = self.rect_base.copy() #sobre os retangulos: toda coisa que aparece na tela do pygame ta dentro de um retangulo,
                                          #isso ajuda a determinar seu eixo e seu limite, e portanto ajuda na hora de girar o objeto(evita distorção
                                          # ou que ele vá para a casa do caralho), e nas colisões (evita que os objetos passem entre si como se o outro não existisse)
        self.speed_x_r = 6
        self.speed_x_l = 6
        self.speed_y_u = 6
        self.speed_y_d = 6
        self.shoot = False
        self.shoot_cooldown = 0
    
    def PlayerRotation(self):
        #calcula e rotaciona o personagem em torno de seu próprio eixo
        #de acordo com uma reta tangente traçada entre a posição do mouse e a posição do player
        self.mouse_coord = pygame.mouse.get_pos() # pega as coordenadas do mouse
        self.x_change_player = (self.mouse_coord[0] - self.rect_base.centerx) #calcula a diferença entre o X do player e o X do mouse
        self.y_change_player = (self.mouse_coord[1] - self.rect_base.centery) #calcula a diferença entre o Y do player e o Y do mouse
        self.angle = math.degrees(math.atan2(self.y_change_player, self.x_change_player)) #calcula a tangente pela equação abaixo e converte em graus
                                                                                          #(x_mouse - x_player)/(y_mouse - y_player)
        self.image = pygame.transform.rotate(self.image_base, -self.angle) #gira o player no grau obtido (a rotação no python é anti-horaria)
        self.rect = self.image.get_rect(center = self.rect_base.center) # atualiza o retangulo do player

    def move(self):
        key = pygame.key.get_pressed() #detecta a tecla pressionada e insere em key, key é praticamente o teclado mapeado em um vetor
                                       #da para usar event também, mas com o event não da pra usar varias teclas simultaneamente, tipo não
                                       #da para andar na diagonal pressionando W e A ou W e S

        if key[pygame.K_w]: #caso W seja pressionado, o objeto do player vai subir até o limite da tela
            self.posicy -= self.speed_y_u           #funciona igual pra todos os outros casos

        if key[pygame.K_s]:
            self.posicy += self.speed_y_d

        if key[pygame.K_a]:
            self.posicx -= self.speed_x_l

        if key[pygame.K_d]:
            self.posicx += self.speed_x_r

        
        #caso isso vire um pewpew da vida, os IFs abaixo permitem fazer tipo uma tela fixa infinita
        if self.posicx > WIDTH:
            self.posicx = 0
        if self.posicx < 0:
            self.posicx = WIDTH
        if self.posicy > HEIGHT:
            self.posicy = 0
        if self.posicy < 0:
            self.posicy = HEIGHT

        #manuseio do retangulo do objeto,
        #todo objeto em pygame ta dentro de um retangulo (informação util para colisões e rotação)
        self.rect_base.center = (self.posicx, self.posicy)
        self.rect.center = self.rect_base.center

    def Shooting(self):
        #isso aqui cria e prepara um tiro qualquer na classe Ammo
        if self.shoot_cooldown == 0: #verifica o intervalo de tiro
            self.shoot_cooldown = 5 #reseta o intervalon(quanto menor, mais parece uma metralhadora)

            self.bullet = Ammo(self.posicx, self.posicy, self.angle) #cria um projetil na coordenada do player
            bullet_group.append(self.bullet) #coloca o projetil na lista de balas
            all_sprites.append(self.bullet) #coloca o projetil na lista de objetos

    def update(self):
        #atualiza o personagem de acordo com as suas funções

        screen.blit(self.image, self.rect) #imprime o personagem na coordenada do retangulo que ele ta contido
        self.move() #função de mover o personagem
        self.PlayerRotation() #função de girar o personagem

        if self.shoot_cooldown > 0: #verifica o intervalo de tiro (talvez tenha algo em time pra melhorar isso)
            self.shoot_cooldown -= 1
    

#Jogo
player_character = Player(WIDTH/2, HEIGHT/2) #criação base do personagem do jogador
game = True #variavel que determina se o jogo ta rodando
all_sprites = [] #lista infinita para colocar TODOS os objetos do jogo, independente da classe usada na criação
bullet_group = [] #lista infinita para colocar os projeteis
enemy_list = []
all_sprites.append(player_character) #insere o player na lista dos objetos
meteor = Enemy(44)
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

    screen.fill((0,0,0)) #preencher o fundo da tela com preto
   
    for b in bullet_group: #move as balas atiradas
        b.AmmoMove()
        for e in enemy_list:
            if b.rect.colliderect(e.rect):
                print('colidiu')
                if(e.size > 8):
                    new_enemy_one = Enemy(e.size/2)
                    new_enemy_two = Enemy(e.size/2)
                    e.kill()
    for sprite in all_sprites: #atualiza todos os sprites do jogo (talvez as balas estejam sendo atualizadas 2x)
        sprite.update()
    pygame.display.update() #atualiza a tela
    clock.tick(60) #determina o fps
  