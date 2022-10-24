import pygame
from pygame.math import Vector2

# Variables here
gravity = Vector2(0, 1)

# classes go here
class Player:
    def __init__(self, pos, speed, health, wand,spells):
        self.image_raw = pygame.image.load("Apprentice_Wizard.png")
        self.width, self.height = 64, 64
        self.image = pygame.transform.scale(self.image_raw, [64, 64])
        self.pos = Vector2(pos)
        self.rect = self.image.get_bounding_rect()
        self.thickness = 2
        self.top_rect = pygame.Rect(self.pos, [self.width, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]
        self.velocity = Vector2(0)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.speed = speed
        self.health = health
        self.wand = wand
        self.spells = spells
        self.spell = self.spells[0]
        self.grounded = False
        self.jump = True
        self.jump_height = -6.5
        self.cooldown = 30
        self.projectiles = []

    def collision_plat(self, platforms):
        buffer = 2
        for platform in platforms:
            if platform.top_rect.colliderect(self.bottom_rect):
                if self.jump == False:
                    self.grounded = True
                    self.jump = True
                    self.pos[1] = platform.pos[1] - self.rect.height
                    self.velocity[1] = 0
                if self.jump == True:
                    if self.pos[1] > platform.pos[1] - self.rect.height:
                        self.pos[1] = platform.pos[1] - self.rect.height
                        self.velocity[1] = 0
            if platform.left_rect.colliderect(self.right_rect):
                #self.pos[0] = platform.pos[0]-self.width-buffer
                if self.velocity[0] > 0:
                    self.velocity[0] = 0
            if platform.right_rect.colliderect(self.left_rect):
                #self.pos[0] = platform.pos[0] + platform.width + buffer
                if self.velocity[0] < 0:
                    self.velocity[0] = 0
            if platform.bottom_rect.colliderect(self.top_rect):
                self.velocity[1] = 0

            if platform.rect.collidepoint(self.rect.center):
                self.grounded = True
                self.pos[1] = platform.pos[1] - self.rect.height

            else:
                self.grounded = False

    def render(self, screen):
        #Rendering collsion and player image
        screen.blit(self.image, self.pos)
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
        #rendering wand and spells
        self.wand.pos[0] = self.pos[0] + self.width - 25
        self.wand.pos[1] = self.pos[1] + self.height/2 - 30
        self.wand.render(screen)



    def move(self, events, time):
        if self.grounded == False:
            self.velocity += gravity * time
        #if self.jump == True:
            #self.velocity[1] = -3
            #self.jump = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocity[0] = -self.speed
                if event.key == pygame.K_RIGHT:
                    self.velocity[0] = self.speed
                if event.key == pygame.K_UP and self.jump == True:
                    print("jump")
                    self.velocity[1] = self.jump_height
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.velocity[0] = 0
                if event.key == pygame.K_UP:
                    self.jump = False
        self.pos += self.velocity
        print(self.pos)

    def shoot(self,events,screen):
        starting_pos = self.pos
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x and self.cooldown >= 30:
                    if self.spell == "fire":
                        self.projectiles.append(Spell("fire","fire.png",[64,64],50,pos = starting_pos))
                    self.cooldown = 0
        if self.cooldown < 30:
            self.cooldown += 1
        if len(self.projectiles) > 0:
            for projectile in self.projectiles:
                projectile.render(screen,self.wand.speed)




class Platform:
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.thickness = 5
        self.spacing = 2
        self.rect = pygame.Rect(self.pos, [self.width, self.height-self.spacing])
        self.top_rect = pygame.Rect([self.pos[0], self.pos[1]], [self.width - self.spacing, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width-self.spacing, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height-self.spacing])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height-self.spacing])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_line = True
        if draw_line:
            for line in self.lines:
                pygame.draw.rect(screen, (255, 0, 0), line)

class Wand:
    def __init__(self,type,image,damage_mult,speed):
        self.type=type
        self.image_raw=pygame.image.load(image)
        self.image_scaled = pygame.transform.scale(self.image_raw,[30,50])
        self.image = pygame.transform.rotozoom(self.image_scaled,-45,1)
        self.damage_mult=damage_mult
        self.speed=speed
        self.pos=[0,0]
    def render(self,screen):
        screen.blit(self.image,self.pos)

class Spell:
    def __init__(self, type, image, size, damage,pos = [0,0]):
        self.type = type
        self.image_raw = pygame.image.load(image)
        self.size = size
        self.image = pygame.transform.scale(self.image_raw,self.size)
        self.rect = self.image.get_bounding_rect()
        self.damage = damage
        self.pos = Vector2(pos)
        self.velocity = Vector2(0)

    def render(self,screen,speed):
        self.rect.topleft = self.pos
        screen.blit(self.image,self.pos)
        self.shoot(speed)

    def shoot(self,speed):
        self.velocity[0] = speed
        self.pos += self.velocity


# objects go here
starter_wand = Wand("starter_wand","Starter_Wand.png",1.25,10)
#fire_spell = Spell("fire","fire.png",[64,64],50)


player = Player([0, 0], 3, 100, starter_wand,["fire"])




"""
Damage works:
Fire spell with a damage of 50, then we multiply the speed with the wand's damage_mult
e.g. starter wand has a damag_mult of 1.25
total damage would be 50*1.25 = 62.5
"""
