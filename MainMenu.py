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
    playbttn_rect = playbttn.get_bounding_rect()
    playbttn_rect.center = [180,250]


    isRunning = True
    while isRunning:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        screen.blit(menubkgd,[0,0])
        screen.blit(playbttn,[80,200])
        #pygame.draw.rect(screen,white,playbttn_rect)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    mainMenuloop()
