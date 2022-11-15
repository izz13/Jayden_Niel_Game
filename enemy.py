import pygame
from pygame.math import Vector2

gravity = Vector2(0, 1)

#make an enemy class here
enemylist = ["vampire", "spider", "zombie"]

#parent Enemy class
class Enemy:
    def __init__(self, image,size, pos, damage, type, speed):
        self.image_raw = pygame.image.load(image)
        self.size = size
        self.image = pygame.transform.scale(self.image_raw,self.size)
        self.pos = Vector2(pos)
        self.velocity = Vector2(0)
        self. damage = damage
        self.type = type
        self.speed = speed
        self.rect = self.image.get_bounding_rect()

    def move(self):
        pass

    def render(self,screen):
        self.rect.center = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2]
        screen.blit(self.image,self.pos)

    def update(self, screen):
        self.move()
        self.render(screen)


class Spider(Enemy):
    def __init__(self,image,size, pos, damage, type, speed,end_pos):
        super().__init__(image,size, pos, damage, type, speed)
        self.start_pos = pos
        self.end_pos = end_pos

    def move(self):
        if self.pos[0] <= self.start_pos[0]:
            self.velocity[0] = self.speed
        elif self.pos[0] >= self.end_pos[0] - self.size[1]:
            self.velocity[0] = -self.speed
        self.pos += self.velocity




