import pygame

#Variables here
gravity = 3

#classes go here
class Player:
    def __init__(self,pos,speed,health,weapon):
        self.image_raw = pygame.image.load("Apprentice_Wizard.png")
        self.image = pygame.transform.scale(self.image_raw,[64,64])
        self.rect = self.image.get_bounding_rect()
        self.pos = pos
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.speed = speed
        self.health = health
        self.weapon = weapon
    def render(self, screen):
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]

class Platform:
    def __init__(self, pos, width, height, color):
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.pos, [self.width, self.height])

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


#objects go here
player = Player([0,0],3,100,"wand")