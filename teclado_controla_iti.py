#controle o objeto pelo teclado

import pygame
import sys
from pygame.locals import *
#constantes do tamanho da tela
x = 1280
y = 720
xc = x/2
yc = y/2
angle = 0

#inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('keyboard test')
clock = pygame.time.Clock()  

    

#cria o objeto inicialmente
font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
img = font.render("I-T-I", True, (255, 255, 255))

#copia do objeto inicial para transformação
rect = img.get_rect()
rotated_img = img
rotated_rect = rect
img_pos = [xc, yc]
img_speed = [0, 0]
img_direction = pygame.math.Vector2(1, 0)
screen.blit(img, rect);

#jogo
while True:
    #limpa a tela
    screen.fill((0, 0, 0))
    screen.blit(rotated_img, (xc, yc))

    #botão de sair da janelaa
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #comandos de teclas
    key = pygame.key.get_focused()
    if key[pygame.K_RIGHT]:
        xc = xc+7
        if xc > x:
        xc = 0
        img_direction = pygame.math.Vector2(0, -1)

    if key[pygame.K_LEFT]:
        xc = xc-7
        if xc < 0:
            xc = x
        img_direction = pygame.math.Vector2(0, 1)
            
    if key[pygame.K_UP]:
        yc = yc-7
        if yc < 0:
        yc = y
        img_direction = pygame.math.Vector2(-1, 0)

    if key[pygame.K_DOWN]:
        yc = yc+7
        if yc > y:
        yc = 0
        img_direction = pygame.math.Vector2(1, 0)
        
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()

    # atualize a posição do objeto com base na direção e na velocidade
    img_pos[0] += img_direction.x * img_speed[0]
    img_pos[1] += img_direction.y * img_speed[1]

    # calcule o ângulo de rotação
    angle = img_direction.angle_to(pygame.math.Vector2(1, 0))

    # rotacione a imagem do objeto
    rotated_img = pygame.transform.rotate(img, angle)
    rotated_rect = rotated_img.get_rect(center=rect.center)
    screen.blit(rotated_img, (xc, yc))

    # atualize a tela
    clock.tick(60)  
    pygame.display.update()