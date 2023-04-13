# controle o objeto pelo movimento do mouse

import pygame
import sys
import random
from pygame.locals import *

# constantes iniciais
x = 1360
xw = 5
xc = 0
y = 762
yc = 0
yw = 10
angle = 0
fps = 60

#vetores
cores = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (128, 0, 128), (255, 0, 255)]
cores_texto = [(0, 0, 0), (255, 255, 255)]
nomes = ["Geraldo", "Maico", "Giovanna", "Gau", "Giovaninha", "JC", "Guinnes", "Aninha", "Kmilla", "Jean", "Otavio", "Edimilson", "Jords", "Gregorio", "Emilly", "Cezar", "Sabrina", "Sophia", "Olavo", "Nathan"]



# inicializa o pygame e cria a tela
pygame.init()
pygame.mouse.set_visible(False)
black = (0, 0, 0)
white = (255, 255, 255)
cor = black
cor_texto = white
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Miechotech')
clock = pygame.time.Clock()

# cria o objeto inicialmente
font = pygame.font.SysFont(pygame.font.get_default_font(), 72, True, False)
obj = font.render("Miechotech", True, cor_texto)

# inicia o jogo
while True:

    # botão de sair da janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    xc += xw
    yc += yw

    if xc == 3 and yc == 3:
        b = xw
        xw = yw
        yw = b
    
    if xc >= (x-280):
        xw *= -1
        cor = random.choice(cores)
        cor_texto = random.choice(cores_texto)
        obj = font.render(random.choice(nomes), True, cor_texto)
    if yc >= (y-50):
        yw *= -1
        cor = random.choice(cores)
        cor_texto = random.choice(cores_texto)
        obj = font.render(random.choice(nomes), True, cor_texto)
    if xc <= 0:
        xw *= -1
        cor = random.choice(cores)
        cor_texto = random.choice(cores_texto)
        obj = font.render(random.choice(nomes), True, cor_texto)
    if yc <= 0:
        yw *= -1
        cor = random.choice(cores)
        cor_texto = random.choice(cores_texto)
        obj = font.render(random.choice(nomes), True, cor_texto)

    # limpa a tela
    screen.fill(cor)
    screen.blit(obj, (xc, yc))
    
    # atualiza a tela
    clock.tick(fps)
    pygame.display.update()
