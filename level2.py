import pygame

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


    def dungeonScene1():
        screen.blit(DungeonImg1, (0, 0))

    def dungeonScene2():
        screen.blit(DungeonImg2, (0, 0))

    def dungeonScene3():
        screen.blit(DungeonImg3, (0, 0))

    def dungeonScene4():
        pass

    scene = "dungeonScene"
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        if scene == "dungeonScene":
            dungeonScene()


        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    level2loop()