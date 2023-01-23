import MainMenu, level1, level2, objects, tools, enemy


level = "level1"

if level == "mainmenu":
    level = MainMenu.mainMenuloop()
if level == "level1":
    level = level1.leve1loop()
if level == "level2":
    level = level2.level2loop()
