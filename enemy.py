import pygame
from pygame.math import Vector2

gravity = Vector2(0, 1)

#make an enemy class here
enemylist = ["vampire", "spider", "zombie", "lvl1boss"]



l2boss = pygame.image.load("Mobs/L2_Minotaur_Boss.png")

#parent Enemy class
class Enemy:
    def __init__(self, image,size,health, pos, damage, type, speed):
        self.image_raw = pygame.image.load(image)
        self.size = size
        self.health = health
        self.image = pygame.transform.scale(self.image_raw,self.size)
        self.pos = Vector2(pos)
        self.velocity = Vector2(0)
        self. damage = damage
        self.type = type
        self.true_speed = speed
        self.speed = speed
        self.frozen_speed = speed/4
        self.rect = self.image.get_bounding_rect()
        self.destroyed = "live"
        self.frozen = False
        self.frozen_timer = 0

    def move(self,player):
        pass

    def attack(self,player):
        pass


    def render(self,screen):
        self.rect.center = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2]
        screen.blit(self.image,self.pos)
        #pygame.draw.rect(screen,(255,0,0),self.rect)

    def damage_taken(self,projectiles):
        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                self.health -= projectile.total_damage
                if projectile.type == "ice":
                    self.frozen = True
                    self.frozen_timer = 180
                projectiles.remove(projectile)
    def destroy(self):
        if self.health <=0:
            return "destroy"
        else:
            return "live"

    def is_frozen(self):
        self.speed = self.frozen_speed
        self.frozen_timer -= 1
        print(self.frozen_timer)


    def update(self, screen, projectiles,player):
        self.move(player)
        self.attack(player)
        self.render(screen)
        self.damage_taken(projectiles)
        self.destroyed = self.destroy()
        if self.frozen == True:
            self.is_frozen()
        if self.frozen_timer <= 0:
            self.speed = self.true_speed
            self.frozen = False




class Spider(Enemy):
    def __init__(self,image,size,health, pos, damage, type, speed,end_pos):
        super().__init__(image,size, health, pos, damage, type, speed)
        self.start_pos = pos
        self.end_pos = end_pos
        self.facing = "right"

    def move(self,player):
        if self.pos[0] <= self.start_pos[0]:
            self.facing = "right"
        elif self.pos[0] >= self.end_pos[0] - self.size[1]:
            self.facing = "left"
        if self.facing == "right":
            self.velocity[0] = self.speed
        if self.facing == "left":
            self.velocity[0] = -self.speed
        self.pos += self.velocity


class Bosslvl1(Enemy):
    def __init__(self,image,pos,size,health,damage,type,speed):
        super().__init__(image,size, health, pos, damage,type, speed)
        self.facing = "left"

    def move(self,player):
        player_pos = player.pos
        if self.pos.x > player_pos.x:
            self.facing ="left"
        if self.pos.x < player_pos.x:
            self.facing = "right"
        if self.facing == "right":
            self.velocity[0] = self.speed
        if self.facing == "left":
            self.velocity[0] = -self.speed

        self.pos += self.velocity


class Minotaur_Boss(Enemy):
    def __init__(self, image, pos, size, health, damage, type, speed):
        super().__init__(image, size, health, pos, damage, type, speed)
        self.facing = "left"

    def move(self, player):
        player_pos = player.pos
        if self.pos.x > player_pos.x:
            self.facing = "left"
        if self.pos.x < player_pos.x:
            self.facing = "right"
        if self.facing == "right":
            self.velocity[0] = self.speed
        if self.facing == "left":
            self.velocity[0] = -self.speed

        self.pos += self.velocity




