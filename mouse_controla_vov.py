#controle o objeto pelo movimento do mouse

import pygame, sys
from pygame.locals import *

#constantes iniciais
x = 1280
xc = x/2
y = 720
yc = y/2
angle = 0
fps = 60

#inicializa o pygame e cria a tela
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Mouse test')
clock = pygame.time.Clock()

#cria o objeto inicialmente
font = pygame.font.SysFont(pygame.font.get_default_font(), 32, True, False)
obj = font.render("V_O_V", True, (255, 255, 255))
pos = (xc, yc)

#inicia o jogo
while True:
    
    #limpa a tela
    screen.fill((0, 0, 0))
    screen.blit(obj, pos)

    #botão de sair da janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #ponto do mouse
    if event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        if xc < pos[0]:
            xc = x+1
        if xc > pos[0]:
            xc = -1
        if yc < pos[1]:
            yc = y+1
        if yc > pos[1]:
            yc = -1

    #atualiza a tela
    clock.tick(fps)
    pygame.display.update()