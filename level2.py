import pygame
from objects import player
from objects import Platform
import enemy
import tools

pygame.init()

def level2loop():

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (178, 190, 181)
    clock = pygame.time.Clock()
    fps = 60
    DungeonImg1 = pygame.image.load("DungeonImages/DungeonScene1.png")
    DungeonImg2 = pygame.image.load("DungeonImages/DungeonScene2.png")
    DungeonImg3 = pygame.image.load("DungeonImages/DungeonScene3.png")
    DungeonImg4 = pygame.image.load("DungeonImages/DungeonScene4.png")
    scene = "dungeonScene1"
    dungeon1_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], [381, 420], 15, "spider", 2, [576, 420])]



    def dungeonScene1(events, time):
        dungeon1_platforms = [Platform([0, 245], 91, 355, black), Platform([91, 481], 173, 119, black), Platform([164, 0],136, 140, black),
                              Platform([377, 531], 536, 69, black), Platform([300, 0], 138, 3, black), Platform([438, 0], 138, 140, black),
                              Platform([719, 216], 81, 84, black), Platform([685, 476], 115, 54, black), Platform([754, 375], 46, 100, black),
                              Platform([382, 477], 192, 53, black), Platform([715, 0], 85, 135, black), Platform([577, 0], 135, 3, black),
                              Platform([576, 512], 104, 18, black), Platform([720, 370], 80, 3, black), Platform([197, 245], 100, 3, black),
                              Platform([197, 402], 100, 3, black), Platform([391, 322], 140, 3, black), Platform([576, 365], 100, 3, black),
                              Platform([598, 250], 100, 3, black)]
        screen.fill(gray)
        screen.blit(DungeonImg1, (0, 0))
        player.playerfunctions(screen,events,time,dungeon1_platforms)
        for platform in dungeon1_platforms:
            platform.render(screen)
        for e in dungeon1_enemies:
            e.update(screen)


    def dungeonScene2(events, time):
        dungeon2_platforms = [Platform([0, 245], 91, 355, black)]
        screen.fill(gray)
        screen.blit(DungeonImg2, (0, 0))
        player.render(screen)
        player.playerfunctions(screen, events, time, dungeon2_platforms)
        for platform in dungeon2_platforms:
            platform.render(screen)

    def dungeonScene3(events, time):
        dungeon3_platforms = [Platform([0, 245], 91, 355, black)]
        screen.fill(gray)
        screen.blit(DungeonImg3, (0, 0))
        player.playerfunctions(screen,events,time,dungeon3_platforms)
        for platform in dungeon3_platforms:
            platform.render(screen)


    def dungeonScene4(events, time):
        dungeon4_platforms = [Platform([0, 245], 91, 355, black)]
        screen.fill(gray)
        screen.blit(DungeonImg4, (0, 0))
        player.render(screen)
        player.playerfunctions(screen, events, time, dungeon4_platforms)
        for platform in dungeon4_platforms:
            platform.render(screen)



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

        if scene == "dungeonScene1":
            dungeonScene1(events, time)
            if player.pos[1] >= 521:
                scene = "dungeonScene3"
                player.pos = [150, 10]
            if player.pos[0] >= 780:
                scene = "dungeonScene2"
        elif scene == "dungeonScene2":
            dungeonScene2(events, time)
            #if player.pos[]
        elif scene == "dungeonScene3":
            dungeonScene3(events, time)
        elif scene == "dungeonScene4":
            dungeonScene4(events, time)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    level2loop()
