import pygame
import math
#tamamnho da tela
HEIGHT = 1280
WIDTH = 720

#inicio do jogo
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Objeto gira com o mouse")

#cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)

#objeto
fonts = pygame.font.SysFont(pygame.font.get_default_font(), 32)
obj = fonts.render("I-T-I", True, white)

#localização e movimentação do objeto
x = HEIGHT/2
y = WIDTH/2
v = 10

#inicio do jogo
game = True
while game:
    pygame.time.delay(30)
    screen.fill(black)
    screen.blit(obj, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x -= v

    if key[pygame.K_RIGHT]:
        x += v
    
    if key[pygame.K_UP]:
        y -= v
    
    if key[pygame.K_DOWN]:
        y += v

    if x < 0:
        x = HEIGHT
    
    if x > HEIGHT:
        x = 0

    if y < 0:
        y = WIDTH
    
    if y > WIDTH:
        y = 0

#    pointer = pygame.mouse.get_pos()
#    xangle = x - pointer[0]
#    yangle = y - pointer[1]
#    angle = math.degrees(math.atan2(xangle, yangle))
#    newobj = pygame.transform.rotate(obj, angle)
#    obj = newobj    
    pygame.display.update()

pygame.quit()