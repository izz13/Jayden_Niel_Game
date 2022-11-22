import pygame


def mainMenuloop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    fps = 60
    menubkgd = pygame.image.load("main_menu_pngs/menubackground.png")
    playbttn = pygame.image.load("main_menu_pngs/play_button.png")
    exitbttn = pygame.image.load("main_menu_pngs/exit_button.png")
    settingbttn = pygame.image.load("main_menu_pngs/settings.png")
    creditbttn = pygame.image.load("main_menu_pngs/credits.png")
    playbttn_rect = playbttn.get_bounding_rect()
    exitbttn_rect = exitbttn.get_bounding_rect()
    settingbttn_rect = settingbttn.get_bounding_rect()
    creditbttn_rect = creditbttn.get_bounding_rect()
    playbttn_rect.center = [180,250]
    exitbttn_rect.center = [650,450]
    settingbttn_rect.center = [650, 250]
    creditbttn_rect.center = [180, 450]


    isRunning = True
    while isRunning:
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbttn_rect.collidepoint(event.pos):
                    print("play button was pressed")

        screen.blit(menubkgd, [0, 0])
        screen.blit(playbttn, [80, 200])
        screen.blit(exitbttn, [500, 400])
        screen.blit(settingbttn, [500, 200])
        screen.blit(creditbttn, [80, 400])

        #pygame.draw.rect(screen,white,playbttn_rect)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    mainMenuloop()
