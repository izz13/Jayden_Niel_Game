import pygame
from objects import player
from objects import Platform
import enemy
import tools

pygame.init()

def level3loop():
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
    zombie_img = "Mobs/zombie.png"

    scene = "escape_room"
    escape_room_pos = [200, 300]
    if scene == "escape_room":
        player.pos = escape_room_pos

    escaperoom_enemies = [enemy.Zombie(zombie_img, [75, 75],250, [381, 420], 30, "zombie", 5, 10,[576, 420])]

    def escape_room(events,time):
        escape_room_platforms = [Platform([0, 500], 800, 105, black)]
        screen.fill(gray)
        player.playerfunctions(screen, events, time, escape_room_platforms)
        for platform in escape_room_platforms:
            platform.render(screen)
        if len(escaperoom_enemies) > 0:
            for e in escaperoom_enemies:
                e.update(screen,player.projectiles,player)
                print(e.health)
                if e.destroyed == "destroy":
                    escaperoom_enemies.remove(e)

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