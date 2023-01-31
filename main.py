import MainMenu, level1, level2, objects, tools, enemy, settings


level = "mainmenu"

if level == "mainmenu":
    level = MainMenu.mainMenuloop()
if level == "settings":
    level = settings.settings_loop()
if level == "level1":
    level = level1.leve1loop()
if level == "level2":
    level = level2.level2loop()
if level == "settings":
    level = settings.settings_loop()
