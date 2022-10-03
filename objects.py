import pygame
from pygame.math import Vector2

#Variables here
gravity = Vector2(0,1.5)

#classes go here
class Player:
    def __init__(self,pos,speed,health,weapon):
        self.image_raw = pygame.image.load("Apprentice_Wizard.png")
        self.image = pygame.transform.scale(self.image_raw,[64,64])
        self.rect = self.image.get_bounding_rect()
        self.pos = Vector2(pos)
        self.velocity = Vector2(0)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        self.speed = speed
        self.health = health
        self.weapon = weapon
        self.grounded = False
        self.jump = False

    def collision_plat(self,platforms):
        for platform in platforms:
            if platform.rect.colliderect(self.rect):
                if self.jump == False:
                    self.grounded = True
                    self.pos[1]  = platform.pos[1] - self.rect.height
                if self.jump == True:
                    if self.pos[1] > platform.pos[1] - self.rect.height:
                        self.pos[1] = platform.pos[1] - self.rect.height

            else:
                self.grounded = False
    def render(self, screen):
        screen.blit(self.image, self.pos)
        self.rect.center = [self.pos[0] + 32, self.pos[1] + 32]
        #pygame.draw.rect(screen,(0,0,255),self.rect)

    def move(self,events,time):
        if self.grounded == False:
            self.velocity += gravity*time
            self.pos += self.velocity + (0.5)*gravity*time**2
        elif self.grounded == True:
            self.velocity[1] = 0
        if self.jump == True:
            self.velocity[1] = -3
            #self.jump = False
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
        self.rect = pygame.Rect(self.pos, [self.width, self.height])
        self.top_pos = [self.pos,[self.pos[0] + self.width,self.pos[1]],"top"]
        self.bottom_pos = [[self.pos[0],self.pos[1] + self.height],[self.pos[0] + self.width,self.pos[1] + self.height],"bottom"]
        self.left_pos = [self.pos,[self.pos[0],self.pos[1] + self.height],"left"]
        self.right_pos = [[self.pos[0] + self.width,self.pos[1]],[self.pos[0] + self.width,self.pos[1] + self.height],"right"]
        self.lines = [self.top_pos,self.bottom_pos,self.left_pos,self.right_pos]


    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for line in self.lines:
            pygame.draw.line(screen,(255,0,0),line[0],line[1])



#objects go here
player = Player([0,0],3,100,"wand")