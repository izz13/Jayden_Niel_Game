import pygame
import time
import objects
from objects import player
from objects import Platform
import enemy

pygame.init()

deadImg = pygame.image.load("deathscreen/gameover.png")
exitImg = pygame.image.load("deathscreen/exitafterdeath.png")
reviveImg = pygame.image.load("deathscreen/respawn.png")
reviveImg_rect = reviveImg.get_bounding_rect()
reviveImg_rect.center = [411,333.5]
exitImg_rect = exitImg.get_bounding_rect()
exitImg_rect.center = [411,429.5]
boomImg = pygame.image.load("lvl 4/volcano.png")
lava_raw1Img = pygame.image.load("lvl 4/lava.png")
lava1Img = pygame.transform.scale(lava_raw1Img, [100, 145])
lava2Img = pygame.transform.scale(lava_raw1Img, [800, 800])
lava3Img = pygame.transform.scale(lava_raw1Img, [100, 50])
xy = [0, -800]
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
    scene1_platforms = [Platform([0, 450], 600, 150, "gray"), Platform([700, 450], 100, 150, "gray"), Platform([600, 590], 100, 100, "gray")]
    scene2_platforms = [Platform([0, 450], 800, 150, "gray")]
    scene3_platforms = [Platform([0, 450], 800, 150, "gray"), Platform([100, 380], 150, 50, "gray"), Platform([250, 310], 150, 50, "gray"), Platform([400, 240], 100, 50, "gray"), Platform([500, 170], 100, 50, "gray"), Platform([700, 170], 100, 50, "gray"), Platform([600, 170], 2, 430, "gray"), Platform([700, 170], 2, 430, "gray")]
    scene4_platforms = [Platform([0, 500], 150, 50, "gray"), Platform([160, 400], 150, 50, "gray"), Platform([320, 300], 150, 50, "gray"), Platform([480, 200], 150, 50, "gray"), Platform([640, 100], 160, 50, "gray")]
    scene1_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [350, 400], 15, "spider", 2, 0,[550, 400])]
    scene2_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [350, 400], 15, "spider", 2, 0, [550, 400]), enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75],180, [550, 400], 15, "spider", 2, 0,[750, 400])]
    scene3_enemies = [enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75], 180, [100, 325], 15, "spider", 2, 0, [250, 325]), enemy.Spider("Mobs/Common_Spider_Enemy.png", [75, 75],180, [500, 120], 15, "spider", 2, 0,[600, 120])]
    player.pos = [0,0]
    scene = "scene1"

    def death_scene(events, time):
        screen.blit(deadImg, (0, 0))
        screen.blit(reviveImg, (222, 302))
        screen.blit(exitImg, (222, 398))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitImg_rect.collidepoint(event.pos) and scene == "deathscene":
                    pygame.quit()
                if reviveImg_rect.collidepoint(event.pos) and scene == "deathscene":
                    #print("hit revive button")
                    player.pos.x,player.pos.y = 50, 50
                    player.health = 1000

    def scene1(screen, events, time, player):
        screen.blit(boomImg, (0, 0))
        for platform in scene1_platforms:
            platform.render(screen)
        screen.blit(lava1Img, (600, 455))
        player.playerfunctions(screen, events, time, scene1_platforms)
        if len(scene1_enemies) > 0:
            for e in scene1_enemies:
                e.update(screen,player.projectiles,player)
                if e.destroyed == "destroy":
                    scene1_enemies.remove(e)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitImg_rect.collidepoint(event.pos) and scene == "deathscene":
                    pygame.quit()
                if reviveImg_rect.collidepoint(event.pos) and scene == "deathscene":
                    #print("hit revive button")
                    player.pos.x,player.pos.y = 50, 50
                    player.health = 1000
        if player.pos[0] >= 600 and player.pos[0] <= 636:
            if player.pos[1] >= 391:
                death_scene(events,time)

    def scene2(screen, events, time, player):
        screen.blit(boomImg, (0, 0))
        for platform in scene2_platforms:
            platform.render(screen)
        player.playerfunctions(screen, events, time, scene2_platforms)
        if len(scene2_enemies) > 0:
            for e in scene2_enemies:
                e.update(screen, player.projectiles, player)
                if e.destroyed == "destroy":
                    scene2_enemies.remove(e)
        if xy[1] + 600 < player.pos[1]:
            xy[1] += 1
            screen.blit(lava2Img, xy)
        else:
            death_scene(events, time)
    def scene3(screen, events, time, player):
        screen.blit(boomImg, (0, 0))
        for platform in scene3_platforms:
            platform.render(screen)
        screen.blit(lava3Img,[600, 170])
        player.playerfunctions(screen, events, time, scene3_platforms)
        if len(scene3_enemies) > 0:
            for e in scene3_enemies:
                e.update(screen,player.projectiles,player)
                if e.destroyed == "destroy":
                    scene3_enemies.remove(e)
        if player.pos[0] >= 600 and player.pos[0] <= 700:
            death_scene(events, time)
    def scene(screen, events, time, player):
        screen.blit(boomImg, (0, 0))
        for platform in scene4_platforms:
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
        if player.pos[0] > 745 and scene == "scene1":
            player.pos = [0, 0]
            scene = "scene2"
        if player.pos[0] > 745 and scene == "scene2":
            player.pos = [0, 0]
            scene = "scene3"
        if scene == "scene1":
            scene1(screen, events, time, player)
        if scene == "scene2":
            scene2(screen, events, time, player)
        if scene == "scene3":
            scene3(screen, events, time, player)
        if scene == "scene4":
            scene4(screen, events, time, player)
        pygame.display.flip()
        clock.tick(fps)


pygame.quit()

if __name__ == "__main__":
    level4loop()
pygame.quit()
quit()