import pygame
import time
import objects
from objects import player
from objects import Platform
import enemy

pygame.init()
Mountaindoorbutton = False


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
    PlainsImg = pygame.image.load("LVL1Images/plainsbackground.png")
    MtImg = pygame.image.load("LVL1Images/Mountainbackground.png")
    caveImg = pygame.image.load("lvl1Images/cave.png")
    firstpicImg = pygame.image.load("lvl1_cutscene/first_cutscene_pic.png")
    secondpicImg = pygame.image.load("lvl1_cutscene/second_cutscene_pic.png")
    nextImg = pygame.image.load("lvl1_cutscene/next_button.png")
    nextImg_rect = nextImg.get_bounding_rect()
    nextImg_rect.center = [589, 296]
    playImg = pygame.image.load("lvl1_cutscene/playbutton.png")
    playImg_rect = playImg.get_bounding_rect()
    playImg_rect.center = [580, 135]


    player.pos = [0,0]
    plainsplatforms=[Platform([0, 480], 800, 120, green)]
    mountainplatforms=[Platform([0,540], 800, 60, gray),Platform([100,500], 600, 40, gray),Platform([140,460], 520, 40, gray),Platform([180,420], 440, 40, gray),Platform([220,380], 360, 40, gray),Platform([260,340], 280, 40, gray),Platform([300,300], 200, 40, gray),Platform([340,260], 120, 40, gray),Platform([380,220], 40, 40, gray)]
    caveplatforms = [Platform([0,443], 800, 157, gray)]
    scene = "plainScene"
    buttonrect = pygame.Rect([0, 150], [50, 50])
    doorrect = pygame.Rect([380, 0], [40, 220])
    l1boss = enemy.Bosslvl1("Mobs/lvl1boss.png",[543,315],[100,134],100,10,"lvl1boss",0.5)



    def plainScene(events,time):
        screen.blit(PlainsImg,(0,0))
        player.playerfunctions(screen,events,time,plainsplatforms)
        for platform in plainsplatforms:
            platform.render(screen)
    def mountainScene(events,time):
        screen.blit(MtImg,(0,0))
        player.playerfunctions(screen,events,time,mountainplatforms)
        for projectile in player.projectiles:
            if buttonrect.colliderect(projectile.rect):
                doorrect.y += 10000
        for platform in mountainplatforms:
            platform.render(screen)
        slvrImg_raw = pygame.image.load("LVL1Images/themountainofsilver.png")
        slvrImg = pygame.transform.scale(slvrImg_raw,[640,450])
        pygame.draw.rect(screen,green,buttonrect)
        pygame.draw.rect(screen, green, doorrect)
        pygame.draw.rect(screen, black, doorrect)
        screen.blit(slvrImg, (80, 90))
        if doorrect.colliderect(player.rect):
            if player.velocity[0] > 0:
                player.velocity[0] = -10
                player.velocity[1] = 10

    def cutscene1(events):
        screen.blit(firstpicImg,[0,0])
        screen.blit(nextImg,[489,246])
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
    def cutscene2(events):
        screen.blit(secondpicImg,[0,0])
        screen.blit(playImg, [480, 35])
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
    def cave(events, time):
        #print(pygame.mouse.get_pos())
        screen.blit(caveImg, [0, 0])
        player.playerfunctions(screen, events, time, caveplatforms)
        l1boss.update(screen,player.projectiles,player)

    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        time = clock.get_time()/fps
        if player.pos[0] < 0:
            player.pos[0] = 0
        if player.pos[0] > 745 and scene == "plainScene":
            scene = "mountainScene"
            player.pos = [0, 478]
        if player.pos[0] > 745 and scene == "mountainScene":
            scene = "cutscene1"
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextImg_rect.collidepoint(event.pos) and scene == "cutscene1":
                    scene = "cutscene2"
                if playImg_rect.collidepoint(event.pos) and scene == "cutscene2":
                    scene = "cavescene"
                    player.pos = [0, 478]
        if player.pos[0] > 745:
            player.pos[0] = 745
        if scene == "plainScene":
            plainScene(events, time)
        if scene == "mountainScene":
            mountainScene(events, time)
        if scene == "cutscene1":
            cutscene1(events)
        if scene == "cutscene2":
            cutscene2(events)
        if scene == "cavescene":
            cave(events, time)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    leve1loop()