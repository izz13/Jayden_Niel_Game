import pygame
from pygame.math import Vector2
from math import sqrt

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
        self.center = [self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2]
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

    def get_distance_player(self,player):
        distance = sqrt((self.rect.center[0]-player.rect.center[0])**2 + (self.rect.center[1]-player.rect.center[1])**2)
        return distance


    def render(self,screen):
        self.rect.center = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2]
        self.center = [self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2]
        screen.blit(self.image,self.pos)
        #pygame.draw.rect(screen,(255,0,0),self.rect)

    def damage_taken(self,projectiles):
        for projectile in projectiles:
            if self.rect.colliderect(projectile.rect):
                if self.defense != 0:
                    self.health -= projectile.total_damage*(1-(self.defense/100))
                if self.defense == 0:
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
        #print(self.frozen_timer)


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
        self.attacked = False
        self.cooldown = 0

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

    def attack(self, player):
        if self.attacked == False:
            if self.rect.colliderect(player.rect):
                player.health -= self.damage
                #print('player was attacked')
                self.attacked = True
                self.cooldown = 30
        if self.cooldown > 0:
            self.cooldown -= 1
        elif self.cooldown <= 0:
            self.attacked = False


class Bosslvl1(Enemy):
    def __init__(self, image, pos, size, health, damage, type, speed, defense, boss_right, boss_left):
        super().__init__(image, size, health, pos, damage, type, speed, defense)
        self.facing = "left"
        self.boss_right = []
        self.boss_left = []
        for i in range(4):
            self.boss_left.append(pygame.image.load(boss_left + "/1boss-" + str(i) + ".png"))
        for i in range(4):
            self.boss_right.append(pygame.image.load(boss_right + "/1boss-" + str(i) + ".png"))
        self.boss_current_left = self.boss_left[0]
        self.boss_current_right = self.boss_right[0]
        self.boss_health = pygame.Rect(50, 500, self.health, 50)
        self.damage_bar = pygame.Rect(50, 500, self.health, 50)
        self.attacking = False
        self.frame = 0
        self.anitime = 5
        self.hit_player = False

    def move(self, player):
        dist_player = self.get_distance_player(player)
        player_pos = player.pos
        if dist_player >= 45:
            self.frame = 0
            self.attacking = False
            if self.pos.x > player_pos.x:
                self.facing ="left"
                self.boss_current_left = self.boss_left[self.frame]
            if self.pos.x < player_pos.x:
                self.facing = "right"
                self.boss_current_right = self.boss_right[self.frame]
            if self.facing == "right":
                self.velocity[0] = self.speed
            if self.facing == "left":
                self.velocity[0] = -self.speed
        else:
            self.attacking = True
            self.velocity = Vector2(0)



        self.pos += self.velocity

    def render(self,screen):
        self.rect.center = [self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2]
        if self.facing == "left":
            screen.blit(self.boss_current_left,self.pos)
        if self.facing == "right":
            screen.blit(self.boss_current_right,self.pos)
        #pygame.draw.rect(screen,(255,0,0),self.rect)

    def attack(self, screen, player):
        UP = Vector2(0,1)
        if self.facing == "left":
            if self.frame < 4:
                if self.anitime >= 5:
                    self.boss_current_left = self.boss_left[self.frame]
                    self.frame += 1
                    self.anitime = 0
                else:
                    self.anitime += 1
                if self.frame == 3 and self.hit_player == False:
                    player.health -= 100
                    self.hit_player = True
                if self.frame == 4 and self.hit_player == True:
                    self.hit_player = False
            else:
                self.frame = 0
        if self.facing == "right":
            if self.frame < 4:
                if self.anitime >= 5:
                    self.boss_current_right = self.boss_right[self.frame]
                    self.frame +=1
                    self.anitime = 0
                else:
                    self.anitime += 1
                if self.frame == 3 and self.hit_player == False:
                    player.health -= 100
                    self.hit_player = True
                if self.frame == 4 and self.hit_player == True:
                    self.hit_player = False
            else:
                self.frame = 0

    def update(self, screen, projectiles, player):
        self.move(player)
        if self.attacking == True:
            self.attack(screen,player)
        self.render(screen)
        self.damage_taken(projectiles)
        self.destroyed = self.destroy()
        if self.frozen == True:
            self.is_frozen()
        if self.frozen_timer <= 0:
            self.speed = self.true_speed
            self.frozen = False


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
        self.boss_health = pygame.Rect(116,500,self.health,50)
        self.damage_bar = pygame.Rect(116,500,self.health,50)
        self.attacked = False
        self.cooldown = 0

    def collision_plat(self):
        for platform in self.platforms:
            if self.bottom_rect.colliderect(platform.top_rect):
                self.grounded = True
                break
            else:
                self.grounded = False
        for platform in self.platforms:
            if self.left_rect.colliderect(platform.right_rect):
                self.facing = "right"
                break
            if self.right_rect.colliderect(platform.left_rect):
                self.facing = "left"
                break
        

    def move(self, player):
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

    def attack(self, player):
        if self.attacked == False:
            if self.rect.colliderect(player.rect):
                player.health -= self.damage
                self.attacked = True
                self.cooldown = 30
        if self.cooldown > 0:
            self.cooldown -= 1
        elif self.cooldown <= 0:
            self.attacked = False


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
        #print(self.grounded)

    def update(self, screen, projectiles, player, platforms):
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

#level3
#vampire boss
class Vampire_Boss(Enemy):
    def __init__(self, image, pos, size, health, damage, type, speed, defense, platforms):
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
        self.boss_health = pygame.Rect(116,500,self.health,50)
        self.damage_bar = pygame.Rect(116,500,self.health,50)
        self.attacked = False
        self.cooldown = 0

    def collision_plat(self):
        for platform in self.platforms:
            if self.bottom_rect.colliderect(platform.top_rect):
                self.grounded = True
                break
            else:
                self.grounded = False
        for platform in self.platforms:
            if self.left_rect.colliderect(platform.right_rect):
                self.facing = "right"
                break
            if self.right_rect.colliderect(platform.left_rect):
                self.facing = "left"
                break
        if self.left_rect.centerx < 0:
            self.facing = "right"
        if self.right_rect.centerx > 800:
            self.facing = "left"

    def move(self, player):
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

    def attack(self, player):
        if self.attacked == False:
            if self.rect.colliderect(player.rect):
                player.health -= self.damage
                self.attacked = True
                self.cooldown = 30
        if self.cooldown > 0:
            self.cooldown -= 1
        elif self.cooldown <= 0:
            self.attacked = False


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
        #print(self.grounded)

    def update(self, screen, projectiles, player, platforms):
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

#lvl3 enemies
class Zombie(Enemy):
    def __init__(self,image,size,health, pos, damage, type, speed,defense,end_pos):
        super().__init__(image,size, health, pos, damage, type, speed,defense)
        self.start_pos = pos
        self.end_pos = end_pos
        self.facing = "right"
        self.attacked = False
        self.cooldown = 0

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

    def attack(self, player):
        if self.attacked == False:
            if self.rect.colliderect(player.rect):
                player.health -= self.damage
                #print('player was attacked')
                self.attacked = True
                self.cooldown = 30
        if self.cooldown > 0:
            self.cooldown -= 1
        elif self.cooldown <= 0:
            self.attacked = False



class Spikky_Boss():
    def __init__(self,spikky_img,spikky_pos,spikky_health,press_img,press_dmg,press_speed):
        self.spikky_img = pygame.image.load(spikky_img)
        self.spikky_img = pygame.transform.scale(self.spikky_img,[64,64])
        self.spikky_pos = spikky_pos
        self.spikky_health = 1000
        self.press_w,self.press_h = 160,210
        self.press_img = pygame.image.load(press_img)
        self.press_img = pygame.transform.scale(self.press_img, [self.press_w, self.press_h])
        self.press_dmg = 250
        self.press_speed = press_speed
        self.pressL ={
            "pos" : [0,0],
            "center" : [self.press_w/2,self.press_h/2],
            "rect" : self.press_img.get_bounding_rect(),
            "following" : 1000,
            "crunched" : False,
            "type" : "left",
            "idle" : False,
            "idle_speed" : 5}
        self.pressL["center"] = [self.pressL["center"][0] + self.pressL["pos"][0],self.pressL["center"][1] + self.pressL["pos"][1]]
        self.pressM = {
            "pos": [365, 0],
            "center": [self.press_w / 2, self.press_h / 2],
            "rect": self.press_img.get_bounding_rect(),
            "following": 1000,
            "crunched": False,
            "type" : "middle",
            "idle" : True,
            "idle_speed" : 7}
        self.pressM["center"] = [self.pressM["center"][0] + self.pressM["pos"][0],
                                 self.pressM["center"][1] + self.pressM["pos"][1]]
        self.pressR = {
            "pos": [730, 0],
            "center": [self.press_w / 2, self.press_h / 2],
            "rect": self.press_img.get_bounding_rect(),
            "following": 1000,
            "crunched": False,
            "type" : "right",
            "idle" : True,
            "idle_speed" : 10}
        self.pressR["center"] = [self.pressR["center"][0] + self.pressR["pos"][0],
                                 self.pressR["center"][1] + self.pressR["pos"][1]]
        self.press_pos = [0,0]
        self.press_center = [self.press_pos[0] + self.press_w/2,self.press_pos[1] + self.press_h/2]
        self.spikky_rect = self.spikky_img.get_bounding_rect()
        self.press_rect = self.press_img.get_bounding_rect()
        self.health_bar = pygame.Rect(50, 500, self.spikky_health, 50)
        self.damage_bar = pygame.Rect(50, 500, self.spikky_health, 50)
        self.following = 1000
        self.crunched = False

    def render_press(self,screen,press):
        press["rect"].center = press["center"]
        screen.blit(self.press_img,[press["center"][0] - self.press_w/2,press["center"][1] - self.press_h/2])
    def render_spikky(self,screen):
        self.spikky_rect.center = [self.spikky_pos[0] + 32, self.spikky_pos[1] + 32]
        screen.blit(self.spikky_img, self.spikky_pos)

    def find_player(self,player,press):
        if press["idle"] == False:
            if press["following"] > 0:
                if press["center"][0] > player.center[0]:
                    press["center"][0] -= 5
                if press["center"][0] < player.center[0]:
                    press["center"][0] += 5
                press["following"] -= 10
                if press["crunched"] == True:
                    press["crunched"] = False

    def idle(self,press):
        if press["idle"] == True:
            if press["center"][0] < 0:
                press["idle_speed"] = -press["idle_speed"]
            if press["center"][0] > 800:
                press["idle_speed"] = -press["idle_speed"]
            press["center"][0] += press["idle_speed"]


    def fall_down(self,press):
        if press["following"] <= 0:
            press["center"][1] += self.press_speed

    def go_up(self, player,press):
        if press["following"] <= 0 and press["center"][1] > 700:
            if press["type"] == "left":
                press["following"] = 1000
                self.pressL["idle"] = True
                self.pressM["idle"] = False
            if press["type"] == "middle":
                press["following"] = 1000
                self.pressM["idle"] = True
                self.pressR["idle"] = False
            if press["type"] == "right":
                press["following"] = 1000
                self.pressR["idle"] = True
                self.pressL["idle"] = False
            press["center"][1] = press["pos"][1] + self.press_h/2
            press["center"][0] = player.center[0]



    def attack(self,player,press):
        self.idle(press)
        self.find_player(player,press)
        self.fall_down(press)
        self.go_up(player,press)
        if press["rect"].colliderect(player.rect):
            if press["crunched"] == False:
                player.health -= self.press_dmg
                press["crunched"] = True


    def damage_taken(self,projectiles):
        for projectile in projectiles:
            if self.spikky_rect.colliderect(projectile.rect):
                self.spikky_health -= projectile.total_damage
                projectiles.remove(projectile)

    def update(self,screen,player,projectiles):
        self.render_spikky(screen)
        self.render_press(screen,self.pressL)
        self.render_press(screen,self.pressM)
        self.render_press(screen,self.pressR)
        self.attack(player,self.pressL)
        self.attack(player,self.pressM)
        self.attack(player, self.pressR)
        self.damage_taken(projectiles)
