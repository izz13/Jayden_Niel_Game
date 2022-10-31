import pygame
import objects
from objects import player
from objects import Platform

pygame.init()

def leve1loop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    gray = (192, 192, 192)
    clock = pygame.time.Clock()
    fps = 60
    PlainsImg = pygame.image.load("plainsbackground.png")
    MtImg = pygame.image.load("Mountainbackground.png")
    player.pos = [0,0]
    plainsplatforms=[Platform([0, 480], 800, 120, green)]
    mountainplatforms=[Platform([0,540], 800, 60, gray),Platform([100,500], 600, 40, gray),Platform([140,460], 520, 40, gray),Platform([180,420], 440, 40, gray),Platform([220,380], 360, 40, gray),Platform([260,340], 280, 40, gray),Platform([300,300], 200, 40, gray),Platform([340,260], 120, 40, gray),Platform([380,220], 40, 40, gray)]


    def plainScene(events,time):
        screen.blit(PlainsImg,(0,0))
        player.render(screen)
        player.move(events,time)
        player.shoot(events,screen)
        player.collision_plat(plainsplatforms)
        for platform in plainsplatforms:
            platform.render(screen)
    def mountainScene(events,time):
        screen.blit(MtImg,(0,0))
        player.render(screen)
        player.move(events, time)
        player.shoot(events, screen)
        player.collision_plat(mountainplatforms)
        for platform in mountainplatforms:
            platform.render(screen)
        slvrImg_raw = pygame.image.load("themountainofsilver.png")
        slvrImg = pygame.transform.scale(slvrImg_raw,[640,450])
        screen.blit(slvrImg,(80,90))
    scene = "mountainScene"
    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        time = clock.get_time()/fps
        if scene == "plainScene":
            plainScene(events,time)
        if scene == "mountainScene":
            mountainScene(events,time)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    leve1loop()