import pygame
pygame.init()

fontlist = pygame.font.get_fonts()
for f in fontlist:
    print(f)

textoa = 35
textob = "B"
textoc = 35

texto_concatenado = str(textoa) + str(textob) + str(textoc)