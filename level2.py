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
    font = pygame.font.SysFont(None, 60)
    DungeonImg1 = pygame.image.load("DungeonImages/DungeonScene1.png")
    DungeonImg2 = pygame.image.load("DungeonImages/DungeonScene2.png")
    DungeonImg3 = pygame.image.load("DungeonImages/DungeonScene3.png")
    dungeontunnelimg = pygame.image.load("DungeonImages/Boss_Tunnel.png")
    DungeonImg4 = pygame.image.load("DungeonImages/DungeonScene4.png")
    pedestal = pygame.transform.scale(pygame.image.load("Items/Scroll_Pedestal.png"), [175, 175])
    scroll = pygame.transform.scale(pygame.image.load("Items/Scroll_Item.png"), [100, 100])
    scroll_rect = scroll.get_bounding_rect()
    picked_scroll = False

    dungeon4_platforms = [Platform([0, 0], 117, 600, black), Platform([117, 0], 683, 81, black),
                          Platform([710, 80], 90, 520, black),
                          Platform([121, 468], 589, 130, black), Platform([523, 302], 170, 10, black)]
    scene = "dungeonScene1"
    dungeon1_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75],180, [381, 420], 15, "spider", 2, 0,[576, 420]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75],180, [95, 425], 15, "spider", 2, 0,[270, 425]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75],180, [390, 270], 15, "spider", 2, 0,[530, 270])]

    dungeon2_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75,75],180, [127, 188], 15, "spider", 1.5, 0,[225, 188]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [279, 204], 15, "spider", 2.1, 0, [412, 204]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [459, 298], 15, "spider", 2.1, 0, [672, 298]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [562, 163], 15, "spider", 2.1, 0, [662, 163])]

    dungeon3_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [383, 175], 15, "spider", 2.5, 0, [597, 175]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [256, 247], 15, "spider", 2.5, 0, [478, 247]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [624, 412], 15, "spider", 2, 0, [790, 412])]

    dungeonT_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [376, 317], 15, "spider", 1.5, 0, [461, 317]),
                        enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [275, 374], 15, "spider", 1.5, 0, [365, 374])]

    minotaur_boss = enemy.Minotaur_Boss("Mobs/L2_Minotaur_Boss.png",[609, 180],[100, 100],600,15,"minotaur_boss",.8, 2.9, dungeon4_platforms)

    dungeon1_pos = [0,0]
    dungeon2_pos = [0, 200]
    dungeon3_pos = [150, 10]
    dungeon4_pos = [0,0]
    dungeon_tunnel_pos = [0, 0]
    if scene == "dungeonScene1":
        player.pos = dungeon1_pos
    if scene == "dungeonScene2":
        player.pos = dungeon2_pos
    if scene == "dungeonScene3":
        player.pos = dungeon3_pos
    if scene == "dungeonScene4":
        player.pos = dungeon4_pos
    if scene == "dungeonScene_tunnel":
        player.pos = dungeon_tunnel_pos

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
        if len(dungeon1_enemies) > 0:
            for e in dungeon1_enemies:
                e.update(screen,player.projectiles,player)
                if e.destroyed == "destroy":
                    dungeon1_enemies.remove(e)


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
        if len(dungeon2_enemies) > 0:
            for e in dungeon2_enemies:
                e.update(screen,player.projectiles,player)
                if e.destroyed == "destroy":
                    dungeon2_enemies.remove(e)

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
        if len(dungeon3_enemies) > 0:
            for e in dungeon3_enemies:
                e.update(screen,player.projectiles,player)
                if e.destroyed == "destroy":
                    dungeon3_enemies.remove(e)

    def dungeonScene_tunnel(events, time):
        dungeon_tunnel_platforms = [Platform([0, 500], 800, 20, black), Platform([275, 425], 87.5, 10, black), Platform([377, 372], 87.5, 10, black)]
        screen.fill(gray)
        screen.blit(dungeontunnelimg, (0, 0))
        screen.blit(pedestal, [420, 330])
        if picked_scroll == False:
            screen.blit(scroll, [455, 255])
            scroll_rect.center = [505,305]
        player.playerfunctions(screen, events, time, dungeon_tunnel_platforms)
        for platform in dungeon_tunnel_platforms:
            platform.render(screen)
        if len(dungeonT_enemies) > 0:
            for e in dungeonT_enemies:
                e.update(screen, player.projectiles, player)


    def dungeonScene4(events, time):
        screen.fill(gray)
        screen.blit(DungeonImg4, (0, 0))
        #dungeon4_platforms
        #player.jump_height = -10
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    player.spell = player.spells[2]
                if player.spell == "jump_boost" and event.key == pygame.K_x:
                    player.jump_boost = True
        """
        player.render(screen)
        player.playerfunctions(screen, events, time, dungeon4_platforms)
        for platform in dungeon4_platforms:
            platform.render(screen)
        minotaur_boss.update(screen,player.projectiles,player,dungeon4_platforms)
        health_outline1 = pygame.Rect((112, 496), (610, 60))
        pygame.draw.rect(screen, gray, health_outline1)
        pygame.draw.rect(screen,(255,0,0),minotaur_boss.damage_bar)
        pygame.draw.rect(screen, (0, 255, 0), minotaur_boss.boss_health)
        minotaur_boss.boss_health.width = minotaur_boss.health
        health_msg = font.render("HEALTH", 0, (255, 0, 0))
        screen.blit(health_msg, [300, 510])
        if len(dungeon4_platforms) == 5:
            if minotaur_boss.pos[1] > dungeon4_platforms[4].pos[1]:
                dungeon4_platforms.remove(dungeon4_platforms[4])



    isRunning = True
    while isRunning:
        #print(player.pos)
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
                scene = "dungeonScene_tunnel"
                player.pos = [0, 0]
        elif scene == "dungeonScene3":
            dungeonScene3(events, time)
            if player.pos[0] >= 800:
                scene = "dungeonScene_tunnel"
                player.pos = [20, 255]
        elif scene == "dungeonScene_tunnel":
            dungeonScene_tunnel(events, time)
            if player.pos[0] >= 800:
                scene = "dungeonScene4"
                player.pos = [400, 255]
            if player.rect.colliderect(scroll_rect):
                picked_scroll = True
                #print("picked up")
                player.spells.append("jump_boost")
        elif scene == "dungeonScene4":
            dungeonScene4(events, time)
       # if scene == "dungeonScene3":
           # print('test')


        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    level2loop()
