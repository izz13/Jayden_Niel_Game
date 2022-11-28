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
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    fps = 60
    DungeonImg1 = pygame.image.load("DungeonImages/DungeonScene1.png")
    DungeonImg2 = pygame.image.load("DungeonImages/DungeonScene2.png")
    DungeonImg3 = pygame.image.load("DungeonImages/DungeonScene3.png")
    DungeonImg4 = pygame.image.load("DungeonImages/DungeonScene4.png")
    scene = "dungeonScene2"
    dungeon1_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], [381, 420], 15, "spider", 2, [576, 420])]
    dungeon2_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75,75], [216, 215], 15, "spider", 2, [216, 215])]

    dungeon1_pos = [0,0]
    dungeon2_pos = [306,368]
    dungeon3_pos = [150, 10]
    dungeon4_pos = [0,0]
    if scene == "dungeonScene1":
        player.pos = dungeon1_pos
    if scene == "dungeonScene2":
        player.pos = dungeon2_pos
    if scene == "dungeonScene3":
        player.pos = dungeon3_pos
    if scene == "dungeonScene4":
        player.pos = dungeon4_pos


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
        dungeon2_platforms = [Platform([195, 465], 235, 465, black), Platform([0, 286], 52, 355, black), Platform([57, 400], 52, 400, black),
                              Platform([528, 393], 267, 207, black), Platform([0, 0], 612, 42, black), Platform([680, 0], 120, 85, black),
                              Platform([0, 40], 56, 156, black), Platform([484, 40], 60, 220, black), Platform([548, 40], 64, 42, black),
                              Platform([788, 85], 12, 309, black), Platform([114, 560], 82, 40, black), Platform([137, 240], 75, 10, black),
                              Platform([286, 256], 114, 209, black), Platform([464, 351], 200, 10, black), Platform([660, 281], 100, 10, black),
                              Platform([572, 215], 75, 10, black), Platform([690, 140], 75, 10, black)]
        screen.fill(gray)
        screen.blit(DungeonImg2, (0, 0))
        player.playerfunctions(screen, events, time, dungeon2_platforms)
        for platform in dungeon2_platforms:
            platform.render(screen)
        for e in dungeon2_enemies:
            e.update(screen)

    def dungeonScene3(events, time):
        dungeon3_platforms = [Platform([152, 158], 200, 10, black), Platform([585, 468], 210, 125, black), Platform([0, 520], 585, 75, black),
                              Platform([275, 412], 139, 110, black), Platform([652, 201], 142, 154, black), Platform([0, 415], 116, 105, black),
                              Platform([0, 235], 120, 80, black), Platform([0, 0], 116, 123, black), Platform([230, 0], 288, 59, black),
                              Platform([650, 0], 150, 83, black), Platform([786, 83], 10, 117, black), Platform([387, 230], 200, 10, black),
                              Platform([265, 300], 200, 10, black), Platform([487, 354], 100, 10, black), Platform([622, 423], 5, 5, green)]
        screen.fill(gray)
        screen.blit(DungeonImg3, (0, 0))
        player.playerfunctions(screen,events,time,dungeon3_platforms)
        for platform in dungeon3_platforms:
            platform.render(screen)


    def dungeonScene4(events, time):
        dungeon4_platforms = [Platform([0, 0], 117, 600, black), Platform([117, 0], 683, 81, black), Platform([710, 80], 90, 520, black),
                              Platform([121, 468], 589, 130, black), Platform([523, 302], 170, 10, black)]
        screen.fill(gray)
        screen.blit(DungeonImg4, (0, 0))
        player.render(screen)
        player.playerfunctions(screen, events, time, dungeon4_platforms)
        for platform in dungeon4_platforms:
            platform.render(screen)



    isRunning = True
    while isRunning:
        print(pygame.mouse.get_pos())
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
                player.pos = dungeon3_pos
            if player.pos[0] >= 780:
                scene = "dungeonScene2"
                player.pos = dungeon2_pos
        elif scene == "dungeonScene2":
            dungeonScene2(events, time)
            if player.pos[1] >= 600:
                scene = "dungeonScene4"
                player.pos = [396, 113]
        elif scene == "dungeonScene3":
            dungeonScene3(events, time)
            if player.pos[0] >= 800:
                scene = "dungeonScene4"
                player.pos = [131, 278]
        elif scene == "dungeonScene4":
            dungeonScene4(events, time)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    level2loop()
