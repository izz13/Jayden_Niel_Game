import pygame
import time
import objects
from objects import player
from objects import Platform
import enemy

pygame.init()

boomImg = pygame.image.load("lvl 4/volcano.png")
def level4loop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (178, 190, 181)
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    fps = 60
    #font = pygame.font.SysFont(None, 60)
    scene1_platforms = [Platform([0, 450], 600, 150, "gray"), Platform([700, 450], 100, 150, "gray")]

    player.pos = [0,0]
    scene = "scene1"

    def scene1(screen, events, time):
        screen.blit(boomImg, (0, 0))
        for platform in scene1_platforms:
            platform.render(screen)
        player.playerfunctions(screen, events, time, scene1_platforms)

    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        time = clock.get_time() / fps
        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > 745:
            player.pos[0] = 745
        if scene == "scene1":
            scene1(screen, events, time)

        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

if __name__ == "__main__":
    level4loop()
pygame.quit()
quit()