import pygame
from pygame.locals import *
import random
import math

# Initialize pygame
pygame.init()

# Set up the window
background_color = (250, 250, 250)
width = 800
height = 600
screen = pygame.display.set_mode((800, 600))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
class Player(pygame.sprite.Sprite):
    def __init__(self, speed, damage):
        
        self.x = width // 2
        self.y = height // 2
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.speed = speed
        self.damage = damage
        self.shoot_cooldown = 0
        self.shooting = False
        self.image = pygame.image.load("python/tps/sprites/seta-direita.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() // 2), (self.image.get_height() // 2)))
        self.rect = self.image.get_rect()
        self.base_image = self.image
        self.base_rect = self.base_image.get_rect(center = self.pos)
        
    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse = self.mouse_coords[0] - self.rect.centerx
        self.y_change_mouse = self.mouse_coords[1] - self.rect.centery
        self.angle = math.degrees(math.atan2(self.y_change_mouse, self.x_change_mouse))
        self.image = pygame.transform.rotate(self.base_image, -self.angle)
        self.rect = self.image.get_rect(center = self.base_rect.center)
        
    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            self.bullet = Bullet(self.x, self.y, self.angle)
            bullet_group.add(self.bullet)
            

    def user_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed
            
        if pygame.mouse.get_pressed() == (1, 0, 0) or key[pygame.K_SPACE]:
            self.shooting = True
            self.shoot()
        else:
            self.shooting = False
    
    
    def move(self):
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.base_rect.center = self.pos
        self.rect.center = self.base_rect.center
    
    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()
        screen.blit(self.image, self.rect)
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        
        self.image = pygame.image.load("python/tps/sprites/ponto-final.png")
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * 2), (self.image.get_height() * 2)))
        self.x = x
        self.y = y
        self.angle = angle
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * 10
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * 10

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def update(self):
        self.move()
        screen.blit(self.image, self.rect)
        if self.x < 0 or self.x > width:
            self.kill()
        
        if self.rect.collidelist(all_sprites) > -1:
            print("hit")
            meteorite = all_sprites[self.rect.collidelist(all_sprites)]
            meteorite.kill()
            all_sprites.remove(meteorite)
            bullet_group.remove(self)
            self.kill
            for i in range(random.randint(1, 3)):
                metorite = Meteor(random.randint(0, width), random.randint(0, height), random.randint(-3, 2))
                all_sprites.append(metorite)
            
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("python/tps/sprites/meteoro1.png")
        self.scale = random.randint(1, 3)
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * self.scale), (self.image.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.image_base = self.image
        self.rect_base = self.image_base.get_rect()
        self.x = x
        self.y = y
        self.speedx = speed
        self.speedy = speed
        
    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        
        if self.x < 0 or self.x > width:
            self.speedx *= -1
        if self.y < 0 or self.y > height:
            self.speedy *= -1
            
    def update(self):
        self.move()
        screen.blit(self.image, (self.x, self.y))
        
# Initialize game objects
player = Player(10, 1)
all_sprites = []
bullet_group = pygame.sprite.Group()
for i in range(random.randint(1, 10)):
    metorite = Meteor(random.randint(0, width), random.randint(0, height), random.randint(-3, 2))
    all_sprites.append(metorite)
    
# Set up the game loop
running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    if player.x < 0:
        player.x = width
    if player.x > width:    
        player.x = 0
    if player.y < 0:
        player.y = height
    if player.y > height:
        player.y = 0

    # Update game state
    screen.fill(background_color)
    bullet_group.update()
    for sprite in all_sprites:
        sprite.update()
    player.update()
    
    pygame.display.update()
    clock.tick(30)