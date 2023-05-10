from typing import Any
import pygame
import sys

vec = pygame.Vector2

class Ball(pygame.sprite.Sprite):
    def __init__(self, root, pos, size):
        self.groups = root
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.size = size
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, (1,0,0), (self.size, self.size), self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.all_sprites = pygame.sprite.Group()
        self.a = 1
    
    def update(self):
        self.rect.center = self.pos
        if self.pos.x > 600:
            self.a = -1
        elif self.pos.x < 0:
            self.a = 1
        self.pos.x = self.pos.x + self.a
            

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
ball = Ball(all_sprites, vec(200,100), 10 )
all_sprites.add(ball)

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
    