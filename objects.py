import pygame
from pygame.math import Vector2

# Variables here
gravity = Vector2(0, 1)


# classes go here
class Player:
    def __init__(self, pos, speed, health, weapon):
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
        self.weapon = weapon
        self.grounded = False
        self.jump = False

    def collision_plat(self, platforms):
        buffer = 15
        for platform in platforms:
            if platform.top_rect.colliderect(self.bottom_rect):
                print("collided")
                if self.jump == False:
                    self.grounded = True
                    self.pos[1] = platform.pos[1] - self.rect.height
                if self.jump == True:
                    if self.pos[1] > platform.pos[1] - self.rect.height:
                        self.pos[1] = platform.pos[1] - self.rect.height
            if platform.left_rect.colliderect(self.right_rect):
                self.pos[0] = platform.pos[0]-self.width-buffer
            if platform.right_rect.colliderect(self.left_rect):
                self.pos[0] = platform.pos[0] + platform.width + buffer
            if platform.rect.collidepoint(self.rect.center):
                self.grounded = True
                self.pos[1] = platform.pos[1] - self.rect.height

            else:
                self.grounded = False

    def render(self, screen):
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.top_rect = pygame.Rect(self.pos, [self.width, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]
        # pygame.draw.rect(screen,(0,0,255),self.rect)
        for line in self.lines:
            pygame.draw.rect(screen, (255, 0, 0), line)

    def move(self, events, time):
        if self.grounded == False:
            self.velocity += gravity * time
            self.pos += self.velocity + (0.5) * gravity * time ** 2
        elif self.grounded == True:
            self.velocity[1] = 0
        if self.jump == True:
            self.velocity[1] = -3
            # self.jump = False
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.velocity[0] = -self.speed
                if event.key == pygame.K_RIGHT:
                    self.velocity[0] = self.speed
                if event.key == pygame.K_UP:
                    print("jump")
                    self.jump = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.velocity[0] = 0
                if event.key == pygame.K_UP:
                    self.jump = False
        self.pos += self.velocity


class Platform:
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.thickness = 20
        self.rect = pygame.Rect(self.pos, [self.width, self.height])
        self.top_rect = pygame.Rect(self.pos, [self.width, self.thickness])
        self.bottom_rect = pygame.Rect([self.pos[0], self.pos[1] + self.height], [self.width, self.thickness])
        self.left_rect = pygame.Rect(self.pos, [self.thickness, self.height])
        self.right_rect = pygame.Rect([self.pos[0] + self.width, self.pos[1]], [self.thickness, self.height])
        self.lines = [self.top_rect, self.bottom_rect, self.left_rect, self.right_rect]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_line = True
        if draw_line:
            for line in self.lines:
                pygame.draw.rect(screen, (255, 0, 0), line)


# objects go here
player = Player([0, 0], 3, 100, "wand")
