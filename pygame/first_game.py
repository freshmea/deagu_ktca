from typing import Any
import pygame
import sys
import random

vec = pygame.Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self, root, pos, size):
        self.groups = root
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.size = size
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, (random.randint(10,250),random.randint(10,250),random.randint(10,250)), (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.all_sprites = pygame.sprite.Group()
        self.a = random.randint(3, 10)
        self.y = random.randint(3, 10)
    
    def update(self):
        self.rect.center = self.pos
        if self.pos.x > 600 and self.a > 0:
            self.a *= -1
        elif self.pos.x < 0 and self.a < 0:
            self.a *= -1
            
        if self.pos.y > 300 and self.y > 0:
            self.y *= -1
        elif self.pos.y < 0 and self.y < 0:
            self.y *= -1
            
        self.pos.x = self.pos.x + self.a
        self.pos.y = self.pos.y + self.y
            

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for i in range(10):
    all_sprites.add(Ball(all_sprites, vec(random.randint(10,200),random.randint(10,200)), random.randint(10,20) ))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    color = (255,255,255)
    screen.fill(color)
    
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    