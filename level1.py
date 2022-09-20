import pygame
import objects
from objects import player
from objects import Platform

def leve1loop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    fps = 60
    PlainsImg = pygame.image.load("plainsbackground.png")
    MtImg = pygame.image.load("Mountainbackground.png")
    player.pos = [0,300]
    plainsplatforms=[Platform([0,500],800,100,white)]

    def plainScene():
        screen.blit(PlainsImg,(0,0))
        player.render(screen)
        for platform in plainsplatforms:
            platform.render(screen)
    def mountainScene():
        screen.fill(white)
    scene = "plainScene"
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
        if scene == "plainScene":
            plainScene()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    leve1loop()