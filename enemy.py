import pygame
from pygame.math import Vector2

gravity = Vector2(0, 1)

#make an enemy class here
enemylist = ["vampire", "spider", "zombie", "lvl1boss"]



#parent Enemy class
class Enemy:
    def __init__(self, image,size,health, pos, damage, type, speed, defense = 0):
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
        self.defense = defense
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
                if self.defense != 0:
                    self.health -= projectile.total_damage*(1-self.defense)
                if self.defense == 0:
                    self.health-= projectile.total_damage
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
    def __init__(self,image,size,health, pos, damage, type, speed,defense,end_pos):
        super().__init__(image,size, health, pos, damage, type, speed,defense)
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
    def __init__(self,image,pos,size,health,damage,type,speed,defense,boss_right,boss_left,bossaxe_right,bossaxe_left):
        super().__init__(image,size, health, pos, damage,type, speed,defense)
        self.facing = "left"
        self.boss_right = pygame.image.load(boss_right)
        self.boss_left = pygame.image.load(boss_left)
        self.bossaxe_right = pygame.image.load(bossaxe_right)
        self.bossaxe_left = pygame.image.load(bossaxe_left)
        self.boss_health = pygame.Rect(50,500,self.health,50)
        self.damage_bar = pygame.Rect(50,500,self.health,50)

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
    def __init__(self, image, pos, size, health, damage, type, speed,defense, platforms):
        super().__init__(image, size, health, pos, damage, type,defense, speed)
        self.facing = "left"
        self.grounded = False
        self.platforms = platforms
        self.width = self.size[0]
        self.height = self.size[1]
        self.thickness = 2
        self.top_rect = pygame.Rect(self.pos, [self.width, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]

    def collision_plat(self):
        for platform in self.platforms:
            if self.bottom_rect.colliderect(platform.top_rect):
                self.grounded = True
                break
            else:
                self.grounded = False

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

        if self.grounded == False:
            self.velocity[1] = gravity[1]*3
            self.velocity[0] = 0
        if self.grounded == True:
            self.velocity[1] = 0
        #self.velocity[0] = 0
        self.collision_plat()
        self.pos += self.velocity

    def render(self,screen):
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.top_rect = pygame.Rect(self.pos, [self.width, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]
        # pygame.draw.rect(screen,(0,0,255),self.rect)
        draw = True
        if draw == True:
            for line in self.lines:
                pygame.draw.rect(screen, (255, 0, 0), line)
        screen.blit(self.image, self.pos)
        print(self.grounded)

    def update(self, screen, projectiles,player,platforms):
        self.platforms = platforms
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




