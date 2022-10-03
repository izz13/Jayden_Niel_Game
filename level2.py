import pygame
from objects import player
from objects import Platform

pygame.init()

def level2loop():

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    fps = 60
    DungeonImg1 = pygame.image.load("DungeonScene1.png")
    DungeonImg2 = pygame.image.load("DungeonScene2.png")
    DungeonImg3 = pygame.image.load("DungeonScene3.png")
    DungeonImg4 = pygame.image.load("DungeonScene4.png")

    dungeon1_platforms = [Platform([0, 480], 800, 120, black)]


    def dungeonScene1(events,time):
        screen.fill(white)
        screen.blit(DungeonImg1, (0, 0))
        player.render(screen)
        player.move(events, time)
        player.collision_plat(dungeon1_platforms)
        for platform in dungeon1_platforms:
            platform.render(screen)
    def dungeonScene2():
        screen.fill(white)
        screen.blit(DungeonImg2, (0, 0))
        player.render(screen)

    def dungeonScene3():
        screen.fill(white)
        screen.blit(DungeonImg3, (0, 0))
        player.render(screen)

    def dungeonScene4():
        screen.fill(white)
        screen.blit(DungeonImg4, (0, 0))
        player.render(screen)


    scene = "dungeonScene1"
    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
        time = clock.get_time() / fps
        if scene == "dungeonScene1":
            dungeonScene1(events,time)
        elif scene == "dungeonScene2":
            dungeonScene2()
        elif scene == "dungeonScene3":
            dungeonScene3()
        elif scene == "dungeonScene4":
            dungeonScene4()

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    level2loop()
