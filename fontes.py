import pygame
pygame.init()

fontlist = pygame.font.get_fonts()
for f in fontlist:
    print(f)
