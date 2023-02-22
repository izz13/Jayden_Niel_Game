import pygame
import objects
from objects import player
from objects import Platform
import enemy
import tools

pygame.init()

def level3loop():
    #basic variables go here
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

    #images go here
    zombie_img = "Mobs/zombie.png"
    BDB = pygame.image.load("Level3Images/Blocked_Door-Barrier.png")
    Button = pygame.image.load("Level3Images/LVL3Button.png")
    S1Lever = pygame.image.load("Level3Images/Standing_Lever.png")
    S2Lever= pygame.image.load("Level3Images/Pushed_Lever.png")
    Vault1 = pygame.image.load("Level3Images/Basic_Vault.png")
    Vault2 = pygame.image.load("Level3Images/Advanced_Vault.png")
    Vault_key1= pygame.image.load("Level3Images/Vault1Key.png")
    Vault_key2= pygame.image.load("Level3Images/Vault2Key.png")

    #scene and pos go here
    scene = "escape_room"
    escape_room_pos = [0, 320]
    if scene == "escape_room":
        player.pos = escape_room_pos

    #enemies go here
    escaperoom_enemies = [enemy.Zombie(zombie_img, [75, 75],1, [140, 430], 30, "zombie", 5, 10,[300, 430]),
                          enemy.Zombie(zombie_img, [75, 75],1, [365, 430], 30, "zombie", 5, 10,[525, 430]),
                          enemy.Zombie(zombie_img, [75, 75],1, [590, 430], 30, "zombie", 5, 10,[750, 430])]
    basicvaultkey = objects.Key([590, 430], "Level3Images/Vault1Key.png", "basic_key")


    #main scene function goes here
    def escape_room(events,time):
        escape_room_platforms = [Platform([0, 500], 800, 105, black)]
        screen.fill(gray)
        player.playerfunctions(screen, events, time, escape_room_platforms)
        for platform in escape_room_platforms:
            platform.render(screen)
        if len(escaperoom_enemies) > 0:
            for e in escaperoom_enemies:
                e.update(screen,player.projectiles,player)
                #print(e.health)
                if e.destroyed == "destroy":
                    escaperoom_enemies.remove(e)
        if len(escaperoom_enemies) == 0 and len(player.keys) == 0:
            basicvaultkey.render(screen)
            if player.rect.colliderect(basicvaultkey.rect):
                print("picked up basic vault key")
                player.keys.append(basicvaultkey)



    #game-loop goes here
    isRunning = True
    while isRunning:
        #print(pygame.mouse.get_pos())
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
                print("If you see this on your console, you have exited Wizard Dungeon Game. Our team here at ACF thanks you for playing! Have a good day.")
        time = clock.get_time() / fps
        if player.pos[0] < 0:
            player.pos[0] = 0
        if scene == "escape_room":
            escape_room(events, time)
            player.spells.append("poison")
            player.spells.append("jump_boost")

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    level3loop()