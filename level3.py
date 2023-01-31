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

    scene = "escape_room"

    def escape_room(events,time):
        screen.fill(gray)

    isRunning = True
    while isRunning:
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

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    level3loop()