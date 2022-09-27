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
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    fps = 60
    PlainsImg = pygame.image.load("plainsbackground.png")
    MtImg = pygame.image.load("Mountainbackground.png")
    player.pos = [0,0]
    plainsplatforms=[Platform([0, 480], 800, 120, green)]

    def plainScene(events,time):
        screen.blit(PlainsImg,(0,0))
        player.render(screen)
        player.move(events,time)
        player.collision_plat(plainsplatforms)
        for platform in plainsplatforms:
            platform.render(screen)
    def mountainScene(events,time):
        screen.fill(white)
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