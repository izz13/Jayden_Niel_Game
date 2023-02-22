import pygame
from pygame.math import Vector2

# Variables here

deadImg = pygame.image.load("deathscreen/gameover.png")
exitImg = pygame.image.load("deathscreen/exitafterdeath.png")
reviveImg = pygame.image.load("deathscreen/respawn.png")
jumpyraw_Img = pygame.image.load("Spells/Jump_Boost.png")
jumpyImg = pygame.transform.scale(jumpyraw_Img, (75, 75))
fireImg = pygame.image.load("Spells/fire.png")
iceImg = pygame.image.load("Spells/ice.png")
poisonrawImg = pygame.image.load("Spells/Poison_Spell.png")
poisonImg = pygame.transform.scale(poisonrawImg, (75, 75))
gravity = Vector2(0, 1)
green = (0, 255, 0)


# classes go here
class Player:
    def __init__(self, pos, speed, health, wand, spells):
        self.image_raw = pygame.image.load("Mobs/Apprentice_Wizard.png")
        self.width, self.height = 64, 64
        self.image = pygame.transform.scale(self.image_raw, [64, 64])
        self.pos = Vector2(pos)
        self.center = [self.pos[0] + self.width / 2, self.pos[1] + self.height / 2]
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
        self.jump_boost = False
        self.jump_boost_cooldown = 420
        self.jump_height = -6.5
        self.cooldown = 30
        self.projectiles = []
        self.facing = "Right"
        self.health_bar = pygame.Rect(self.pos[0], self.pos[1] - 10, self.health / 10, 10)
        self.damage_bar = pygame.Rect(self.pos[0], self.pos[1] - 10, self.health / 10, 10)
        self.keys = []

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
                # self.pos[0] = platform.pos[0] - self.width - buffer
                if self.velocity[0] > 0:
                    self.velocity[0] = 0
            if platform.right_rect.colliderect(self.left_rect):
                # self.pos[0] = platform.pos[0] + platform.width + buffer
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
        # Rendering collsion and player image
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.center = [self.pos[0] + self.width / 2, self.pos[1] + self.height / 2]
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
        # rendering wand and spells
        if self.facing == "Right":
            self.wand.pos[0] = self.pos[0] + self.width - 25
            self.wand.pos[1] = self.pos[1] + self.height / 2 - 30
            self.wand.render(screen, self.facing)
        if self.facing == "Left":
            self.wand.pos[0] = self.pos[0] + self.width - 93
            self.wand.pos[1] = self.pos[1] + self.height / 2 - 20
            self.wand.render(screen, self.facing)

    def playerfunctions(self, screen, events, time, platforms):
        self.render(screen)
        self.move(events, time)
        self.shoot(events, screen)
        self.collision_plat(platforms)
        pygame.draw.rect(screen, (255, 0, 0), self.damage_bar)
        pygame.draw.rect(screen, (0, 255, 0), self.health_bar)
        self.health_bar = pygame.Rect(self.pos[0], self.pos[1] - 10, self.health / 10, 10)
        self.damage_bar = pygame.Rect(self.pos[0], self.pos[1] - 10, 1000 / 10, 10)
        if self.spell == "fire":
            screen.blit(fireImg, [15, 15])
        if self.spell == "ice":
            screen.blit(iceImg, [15, 15])
        if self.spell == "jump_boost":
            screen.blit(jumpyImg, [15, 15])
        if self.spell == "poison":
            screen.blit(poisonImg, [15, 15])


    def move(self, events, time):
        if self.grounded == False:
            self.velocity += gravity * time
        # if self.jump == True:
        # self.velocity[1] = -3
        # self.jump = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.velocity[0] = -self.speed
                    self.facing = "Left"
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.velocity[0] = self.speed
                    self.facing = "Right"
                if event.key == pygame.K_UP and self.jump == True:
                    self.velocity[1] = self.jump_height
                if event.key == pygame.K_w and self.jump == True:
                    self.velocity[1] = self.jump_height
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    self.velocity[0] = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.jump = False
        if self.jump_boost == True:
            self.jump_height = -10
            self.jump_boost_cooldown -= 1
        if self.jump_boost_cooldown <= 0:
            self.jump_height = -6.5
            self.jump_boost = False
            self.jump_boost_cooldown = 420
        self.pos += self.velocity


    def shoot(self, events, screen):
        if self.facing == "Right":
            starting_pos = [self.pos[0] + 60, self.pos[1] - 5]
        if self.facing == "Left":
            starting_pos = [self.pos[0] - 60, self.pos[1] - 5]
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.spell = self.spells[0]
                if event.key == pygame.K_2:
                    self.spell = self.spells[1]
                if event.key == pygame.K_3 and len(self.spells) >= 3:
                    self.spell = self.spells[2]
                if event.key == pygame.K_4 and len(self.spells) >= 4:
                    self.spell = self.spells[3]
                if event.key == pygame.K_x and self.cooldown >= 30:
                    if self.spell == "fire":
                        self.projectiles.append(
                            Spell("fire", "Spells/fire.png", [64, 64], 50, self.wand.damage_mult, self.facing,
                                  pos=starting_pos))
                    if self.spell == "ice":
                        self.projectiles.append(
                            Spell("ice", "Spells/ice.png", [64, 64], 10, self.wand.damage_mult, self.facing,
                                  pos=starting_pos))
                    if self.spell == "poison":
                        self.projectiles.append(
                            Spell("poison", "Spells/Poison_Spell.png", [64, 64], 100, self.wand.damage_mult,
                                  self.facing, pos=starting_pos))
                    if self.spell == "jump_boost":
                        self.jump_boost = True

                    self.cooldown = 0
        if self.cooldown < 30:
            self.cooldown += 1
        if len(self.projectiles) > 0:
            for projectile in self.projectiles:
                projectile.render(screen, self.wand.speed)
                if projectile.pos[0] > 800:
                    self.projectiles.remove(projectile)


class Platform:
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.thickness = 5
        self.spacing = 2
        self.rect = pygame.Rect(self.pos, [self.width, self.height - self.spacing])
        self.top_rect = pygame.Rect([self.pos[0], self.pos[1]], [self.width - self.spacing, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height],
                                       [self.width - self.spacing, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height - self.spacing])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]],
                                      [self.thickness, self.height - self.spacing])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_line = True
        if draw_line:
            for line in self.lines:
                pygame.draw.rect(screen, (255, 0, 0), line)


class Wand:
    def __init__(self, type, image, damage_mult, speed):
        self.type = type
        self.image_raw = pygame.image.load(image)
        self.image_scaled = pygame.transform.scale(self.image_raw, [30, 50])
        self.image_right = pygame.transform.rotozoom(self.image_scaled, -45, 1)
        self.image_left = pygame.transform.rotozoom(self.image_scaled, 90, 1)
        self.damage_mult = damage_mult
        self.speed = speed
        self.pos = [0, 0]

    def render(self, screen, facing):
        if facing == "Right":
            screen.blit(self.image_right, self.pos)
        if facing == "Left":
            screen.blit(self.image_left, self.pos)


class Spell:
    def __init__(self, type, image, size, damage, damage_mult, facing, pos=[0, 0]):
        self.type = type
        self.image_raw = pygame.image.load(image)
        self.size = size
        self.image = pygame.transform.scale(self.image_raw, self.size)
        self.damage = damage
        self.damage_mult = damage_mult
        self.pos = Vector2(pos)
        self.velocity = Vector2(0)
        self.facing = facing
        self.rect = self.image.get_bounding_rect()
        self.total_damage = self.damage * self.damage_mult

    def render(self, screen, speed):
        self.rect.center = [self.pos[0] + self.size[0] / 2, self.pos[1] + self.size[1] / 2]
        screen.blit(self.image, self.pos)
        self.shoot(speed)
        # pygame.draw.rect(screen,(255,255,0),self.rect)

    def shoot(self, speed):
        self.velocity[0] = speed
        if self.facing == "Right":
            self.pos += self.velocity
        if self.facing == "Left":
            self.pos -= self.velocity

class Key:
    def __init__(self, pos, image, type):
        self.pos = pos
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [25, 25])
        self.type = type
        self.rect = self.image.get_bounding_rect()

    def render(self, screen):
        screen.blit(self.image, self.pos)
        self.rect.topleft = self.pos






# objects go here


starter_wand = Wand("starter_wand", "Items/Starter_Wand.png", 1.25, 5)
# fire_spell = Spell("fire","fire.png",[64,64],50)


player = Player([0, 0], 3, 1000, starter_wand, ["fire", "ice"])

"""
Damage works:
Fire spell with a damage of 50, then we multiply the speed with the wand's damage_mult
e.g. starter wand has a damage_mult of 1.25
total damage would be 50*1.25 = 62.5
"""
