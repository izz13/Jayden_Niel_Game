import pygame

pygame.init()
level = "mainmenu"

isrunning = True
while isrunning:
    if level == "mainmenu":
        import MainMenu
        print("running main menu")
        level = MainMenu.mainMenuloop()
    if level == "settings":
        import settings
        level = settings.settings_loop()
    if level == "level1":
        import level1
        level = level1.leve1loop()
    if level == "level2":
        import level2
        level = level2.level2loop()
    if level == "level3":
        import level3
        level = level3.level3loop()
    if level == "level4":
        import level4
        level = level4.level4loop()

