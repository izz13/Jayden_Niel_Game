import pygame

pygame.init()
def settings_loop():
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
    settImg = pygame.image.load("main_menu_pngs/settings_page.png")
    backImg = pygame.image.load("main_menu_pngs/back.png")
    backImg_rect = backImg.get_bounding_rect()
    backImg_rect.topleft = [0, 0]

    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backImg_rect.collidepoint(event.pos):
                    return "mainmenu"
        screen.blit(settImg, [0, 0])
        screen.blit(backImg, (0, 0))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
    quit()

if __name__ == "__main__":
    settings_loop()