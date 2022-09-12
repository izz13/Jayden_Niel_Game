import pygame


def mainMenuloop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    fps = 60

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        screen.fill(white)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    mainMenuloop()
