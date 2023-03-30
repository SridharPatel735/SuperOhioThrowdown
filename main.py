import pygame
import random
import time
import sys
import pauseMenu
from levelSettings import *
from level1 import Level1
from level2 import Level2
import gameObjects
import battleCalcs
import characterSelection
from debug import debug
import time

level1Trigger = True
level2Trigger = False
level1RunBool = False
level2RunBool = False


def draw_text(screen, text, font_size, x, y):
    text_font = pygame.font.Font("kvn-pokemon-gen-5.ttf", font_size)
    text_color = (255, 255, 255)
    img = text_font.render(text, True, text_color)
    screen.blit(img, (x, y))


lebronStats = [85, 75, 60, 70]
lebronMoves = [[0, 100, 10, 1, 1, 0, "Chasedown Block"], [0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"], [0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"], [100, 90, 10, 4, 0, 0, "Tomohawk Dunk"]]

luffyStats = [50, 90, 90, 60]
luffyMoves = [[10, 100, 5, 9, 0, 0, "Gatling Punch"], [40, 100, 20, 0, 1, 0, "Jet Pistol"], [150, 100, 5, 5, 0, 0, "Giant Pistol"], [0, 100, 5, 10, 0, 0, "Gear Change"]]

bruceStats = [90, 45, 45, 110]
bruceMoves = [[30, 100, 10, 0, 0, 0, "Leg Sweep"], [10, 100, 3, 12, 0, 0, "One Inch Punch"], [15, 100, 10, 0, 1, 0, "Lop Sao Backfist"], [0, 100, 10, 1, 1, 0, "Block"], [7, 100, 5, 9, 0, 15, "Lightning Fast Punches"]]

gruntStats = [40, 40, 40, 40]
gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"], [50, 100, 10, 0, 0, 0, "Punch"], [0, 100, 3, 3, 0, 0, "Get Angry"], [0, 100, 5, 16, 0, 0, "Stop Right There"]]

obamaStats = [45, 120, 120, 25]
obamaMoves = [[0, 100, 3, 7, 0, 0, "Let Me Be Clear"], [20, 100, 5, 17, 0, 0, "Campaign Trail Stomp"], [0, 100, 5, 16, 0, 0, "Landslide Victory"], [30, 100, 10, 14, 0, 0, "Endorsement Enforcement"]]

ohmStats = [100, 100, 100, 100]
ohmMoves = [[150, 100, 1, 5, 0, 0, "Super Ohio Throwdown"], [20, 100, 10, 6, 0, 0, "AtOHMic BOHMb"], [0, 50, 5, 7, 0, 0, "Attack of the ClOHMs"], [0, 100, 3, 8, 0, 0, "OHMazing Grace"]]

emStats = [70, 100, 50, 20]
emMoves = [[140, 100, 1, 0, 0, 15, "Killshot"], [20, 100, 10, 11, 0, 0, "Rap God"], [0, 100, 1, 13, 0, 0, "Not Afraid"], [10, 100, 5, 9, 0, 0, "8 Mile Melee"], [0, 100, 1, 13, 0, 0, "Till I Collapse"], [0, 50, 20, 2, 0, 10, "Music to Be Murdered By"]]

jackStats = [110, 50, 40, 70]
jackMoves = [[0, 100, 5, 1, 0, 0, "Drunken Dodge"], [90, 100, 3, 18, 0, 0, "Crash the Boat"], [40, 100, 5, 11, 0, 0, "Slash and Dash"], [0, 100, 1, 19, 0, 0, "Pillage"]]

sharkStats = [100, 30, 60, 70]
sharkMoves = [[0, 100, 10, 11, 0, 0, "Tidal Wave"], [0, 90, 5, 8, 0, 0, "Fish Feast"], [60, 100, 10, 0, 0, 0, "Bite"], [20, 100, 10, 6, 0, 0, "Puncture Prey"]]

bearStats = [40, 140, 80, 40]
bearMoves = [[60, 100, 10, 0, 0, 0, "Bite"], [0, 100, 10, 12, 0, 0, "Shake the Tree"], [0, 100, 1, 13, 0, 0, "Bear Down"], [30, 100, 10, 14, 0, 0, "Berry Bush Beatdown"], [0, 100, 1, 15, 0, 15, "Unbearable Bunker"]]

hero = 0
heroLevel = 5000
grunt = 0
enemy = 0
miniBoss = 0
boss = 0
gruntLevel = heroLevel + 1000
miniBossLevel = heroLevel + 2000
bossLevel = heroLevel + 3000
charSelected = 0
healthLength = 215

heroHealthBlock = 0
enemyHealthBlock = 0
heroStartingHealth = 0
heroHealthRect = 0
enemyHealthRect = 0
enemyStartingHealth = 0


class Game:

    def __init__(self):
        global lebronStats
        global lebronMoves
        global luffyStats
        global luffyMoves
        global bruceStats
        global bruceMoves
        global hero
        global charSelected
        global heroLevel

        pygame.init()
        charSelected = characterSelection.charSelection()
        if (charSelected == 1):
            hero = battleCalcs.Fighter(
                lebronStats, lebronMoves, heroLevel, "lebron.png")
        elif (charSelected == 2):
            hero = battleCalcs.Fighter(
                bruceStats, bruceMoves, heroLevel, "bruce_lee.png")
        elif (charSelected == 3):
            hero = battleCalcs.Fighter(
                luffyStats, luffyMoves, heroLevel, "luffy.png")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()

    def run(self):
        global level1Trigger, level2Trigger, level1RunBool, level2RunBool
        nextLevelButton = True
        runOnce = True

        global lebronStats, lebronMoves
        global luffyStats, luffyMoves
        global bruceStats, bruceMoves
        global gruntStats, gruntMoves
        global obamaStats, obamaMoves
        global ohmStats, ohmMoves
        global emStats, emMoves
        global jackStats, jackMoves
        global sharkStats, sharkMoves
        global bearStats, bearMoves
        global hero, grunt, miniBoss, boss
        global enemy
        global heroLevel, miniBossLevel, bossLevel

        global heroHealthBlock, heroStartingHealth, heroHealthRect
        global enemyHealthBlock, enemyStartingHealth, enemyHealthRect
        

        pygame.mixer.music.load("menumusic.mp3")
        battleLoopBool = False
        endBattle = False

        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and runOnce == True:
                    level1Trigger = False
                    level2Trigger = True
                    runOnce = False
                if event.key == pygame.K_ESCAPE and battleLoopBool==False:
                    pauseMenu.p()

            if gameObjects.endOfLevelOne == True:
                level2Trigger = True
                level1Trigger = False
                gameObjects.endOfLevelOne = False

            if level1Trigger == True:
                heroLevel = 5000
                gruntLevel = heroLevel + 1000
                grunt = battleCalcs.Fighter(gruntStats, gruntMoves, gruntLevel, "grunt_battle.png")
                self.level1 = Level1()
                level1Trigger = False
                level1RunBool = True
                level2Trigger = False
                level2RunBool = False

            elif level2Trigger == True:
                nextLevelButton = False
                self.screen.fill('black')
                line1 = "Testing"
                line2 = "CONTINUE"

                draw_text(self.screen, line1, 30, 100, 100)
                draw_text(self.screen, line2, 30, 590, 600)

                continueRectangle = pygame.draw.rect(
                    self.screen, "red", pygame.Rect(550, 600, 200, 60), 2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if (x >= 550) and (x <= 750) and (y >= 600) and (y <= 660):
                        nextLevelButton = True

                pygame.display.update()
                if nextLevelButton == True:
                    heroLevel = hero.getLevel() * 1000
                    gruntLevel = heroLevel + 1000
                    miniBossLevel = heroLevel + 2000
                    bossLevel = heroLevel + 3000
                    print("-------------------------------------------------------------------------")
                    print(heroLevel)
                    print(gruntLevel)
                    print(miniBossLevel)
                    print(bossLevel)
                    print("-------------------------------------------------------------------------")
                    grunt = battleCalcs.Fighter(gruntStats, gruntMoves, gruntLevel, "grunt_battle.png")
                    miniBoss = battleCalcs.Fighter(sharkStats, sharkMoves, miniBossLevel, "shark.png")
                    boss = battleCalcs.Fighter(jackStats, jackMoves, bossLevel, "jackSparrow.png")
                    self.level2 = Level2()
                    level2Trigger = False
                    level2RunBool = True
                    level1RunBool = False

            if gameObjects.battleLoopGrunt == True:
                enemy = grunt
                healthLength = 215
                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp
                battleLoopBool = True
                gameObjects.battleLoopGrunt = False

            if gameObjects.battleLoopMiniBoss == True:
                gruntStats = [40, 40, 40, 40]
                gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"], [50, 100, 10, 0, 0, 0, "Punch"], [
                    0, 100, 3, 3, 0, 0, "Get Angry"], [0, 100, 5, 16, 0, 0, "Stop Right There"]]
                enemy = battleCalcs.Fighter(
                    gruntStats, gruntMoves, 5000, "grunt_battle.png")
                if (charSelected == 1):
                    hero = battleCalcs.Fighter(
                        lebronStats, lebronMoves, 5000, "lebron.png")
                elif (charSelected == 2):
                    hero = battleCalcs.Fighter(
                        bruceStats, bruceMoves, 5000, "bruce_lee.png")
                elif (charSelected == 3):
                    hero = battleCalcs.Fighter(
                        luffyStats, luffyMoves, 5000, "luffy.png")

                healthLength = 215

                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp
                battleLoopBool = True
                gameObjects.battleLoopMiniBoss = False

            if gameObjects.battleLoopBoss == True:
                gruntStats = [40, 40, 40, 40]
                gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"], [50, 100, 10, 0, 0, 0, "Punch"], [
                    0, 100, 3, 3, 0, 0, "Get Angry"], [0, 100, 5, 16, 0, 0, "Stop Right There"]]
                enemy = battleCalcs.Fighter(
                    gruntStats, gruntMoves, 5000, "grunt_battle.png")
                if (charSelected == 1):
                    hero = battleCalcs.Fighter(
                        lebronStats, lebronMoves, 5000, "lebron.png")
                elif (charSelected == 2):
                    hero = battleCalcs.Fighter(
                        bruceStats, bruceMoves, 5000, "bruce_lee.png")
                elif (charSelected == 3):
                    hero = battleCalcs.Fighter(
                        luffyStats, luffyMoves, 5000, "luffy.png")

                healthLength = 215

                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp
                battleLoopBool = True
                gameObjects.battleLoopBoss = False

            if battleLoopBool:
                heroHealthBar = 0
                enemyHealthBar = 0

                heroImg = pygame.image.load(hero.imageSource)
                heroImg = pygame.transform.flip(heroImg, True, False)
                heroImg_rect = heroImg.get_rect()
                gruntImg = pygame.image.load(enemy.imageSource)
                gruntImg_rect = heroImg.get_rect()
                battleBg = pygame.image.load("battleBgTemplate.jpg")
                battleBg_rect = battleBg.get_rect()
                battleBorder = pygame.image.load("battleBgBorder.png")
                battleScreen = pygame.display.set_mode(
                    (battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)
                endMessageFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 48)

                heroHealthRect = (884, 408, heroHealthBar, 10)
                enemyHealthRect = (335, 152, enemyHealthBar, 10)

                attack1 = (100, 535, (battleScreen_rect.width - 300) / 2, 50)
                attack2 = ((battleScreen_rect.width / 2) + 50, 535,
                           (battleScreen_rect.width - 300) / 2, 50)
                attack3 = (100, 630, (battleScreen_rect.width - 300) / 2, 50)
                attack4 = ((battleScreen_rect.width / 2) + 50, 630,
                           (battleScreen_rect.width - 300) / 2, 50)

                while battleRunning:
                    playerAttack = ""
                    playerEffect = 0
                    enemyAttack = ""
                    enemyEffect = 0

                    heroHealthRect = (884, 408, heroHealthBar, 10)
                    enemyHealthRect = (335, 152, enemyHealthBar, 10)
                    # event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            battleRunning = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                battleRunning = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            (x, y) = pygame.mouse.get_pos()
                            if ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 535) and (y <= 585)):
                                playerAttack = "attack1"
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 535) and (y <= 585)):
                                playerAttack = "attack2"
                            elif ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 630) and (y <= 680)):
                                playerAttack = "attack3"
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 630) and (y <= 680)):
                                playerAttack = "attack4"
                            # elif ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                            #     time.sleep(1)
                            #     endBattle = False
                            #     battleRunning = False

                            # if optionsMenu.rect.collidepoint(event.pos):
                            #     menuText = battleFont.render('Success!', True, (0, 0, 0))
                            #     menuText_rect = menuText.get_rect()
                            #     menuText_rect.centerx = battleScreen_rect.centerx
                            #     pygame.display.update()

                    if (playerAttack != ""):
                        enemyMove = random.randint(1, 4)
                        result = False
                        playerDmg = 0
                        enemyDmg = 0

                        if (playerAttack == "attack1"):
                            playerEffect == hero.move1effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                        elif (playerAttack == "attack2"):
                            playerEffect == hero.move2effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                        elif (playerAttack == "attack3"):
                            playerEffect == hero.move3effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                        elif (playerAttack == "attack4"):
                            playerEffect == hero.move4effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)

                        if (result):
                            if (playerAttack == "attack1"):
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move1bp, hero.level, enemy.tempDef)
                            elif (playerAttack == "attack2"):
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move2bp, hero.level, enemy.tempDef)
                            elif (playerAttack == "attack3"):
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move3bp, hero.level, enemy.tempDef)
                            elif (playerAttack == "attack4"):
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move4bp, hero.level, enemy.tempDef)

                            enemy.tempHp = enemy.tempHp - playerDmg
                            enemyHealthBar = (enemyStartingHealth - enemy.tempHp) * enemyHealthBlock
                                #If enemy HP is empty, end of battle process starts
                            if (enemy.tempHp < 0):
                                if (enemyHealthBar >= 215):
                                    enemyHealthBar = 215
                                heroHealthRect = (884, 408, heroHealthBar, 10)
                                enemyHealthRect = (335, 152, enemyHealthBar, 10)
                                pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                                pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)
                                battleScreen.blit(battleBorder, (0, 500))
                                battleText = pygame.font.Font.render(endMessageFont, "The enemy fainted!", True, (255, 255, 255))
                                battleScreen.blit(battleText, (50, 550))
                                endBattle = True
                                pygame.display.update()

                                while (endBattle == True):
                                    hero.afterWin(hero.getLevel() + 1000)
                                    hero.reset()
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            battleRunning = False
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            (x, y) = pygame.mouse.get_pos()
                                            if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                time.sleep(1)
                                                endBattle = False
                                                battleRunning = False
                                        
                            
                            else:
                                if (enemyMove == 1):
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.atk, enemy.move1bp, enemy.level, hero.dfs)
                                elif (enemyMove == 2):
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.atk, enemy.move2bp, enemy.level, hero.dfs)
                                elif (enemyMove == 3):
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.atk, enemy.move3bp, enemy.level, hero.dfs)
                                elif (enemyMove == 4):
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.atk, enemy.move4bp, enemy.level, hero.dfs)

                                hero.tempHp = hero.tempHp - enemyDmg
                                heroHealthBar = (heroStartingHealth - hero.tempHp) * heroHealthBlock
                                #If player HP is empty, end of battle process starts
                                if (hero.tempHp < 0):
                                    if (heroHealthBar >= 215):
                                        heroHealthBar = 215
                                    heroHealthRect = (884, 408, heroHealthBar, 10)
                                    enemyHealthRect = (335, 152, enemyHealthBar, 10)
                                    pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                                    pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)
                                    battleScreen.blit(battleBorder, (0, 500))
                                    battleText = pygame.font.Font.render(endMessageFont, "You fainted!", True, (255, 255, 255))
                                    battleScreen.blit(battleText, (50, 550))
                                    endBattle = True
                                    pygame.display.update()

                                    while (endBattle == True):
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                battleRunning = False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                (x, y) = pygame.mouse.get_pos()
                                                if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                    time.sleep(1)
                                                    endBattle = False
                                                    battleRunning = False
                                                    pygame.quit()
                                                    sys.exit()

                        elif (result == False):
                            if (enemyMove == 1):
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.atk, enemy.move1bp, enemy.level, hero.dfs)
                            elif (enemyMove == 2):
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.atk, enemy.move2bp, enemy.level, hero.dfs)
                            elif (enemyMove == 3):
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.atk, enemy.move3bp, enemy.level, hero.dfs)
                            elif (enemyMove == 4):
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.atk, enemy.move4bp, enemy.level, hero.dfs)

                            hero.tempHp = hero.tempHp - enemyDmg
                            heroHealthBar = (heroStartingHealth - hero.tempHp) * heroHealthBlock
                            #If player HP is empty, end of battle process starts
                            if (hero.tempHp < 0):
                                if (heroHealthBar >= 215):
                                    heroHealthBar = 215
                                heroHealthRect = (884, 408, heroHealthBar, 10)
                                enemyHealthRect = (335, 152, enemyHealthBar, 10)
                                pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                                pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)
                                battleScreen.blit(battleBorder, (0, 500))
                                battleText = pygame.font.Font.render(endMessageFont, "You fainted!", True, (255, 255, 255))
                                battleScreen.blit(battleText, (50, 550))
                                endBattle = True
                                pygame.display.update()

                                while (endBattle == True):
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                battleRunning = False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                (x, y) = pygame.mouse.get_pos()
                                                if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                    time.sleep(1)
                                                    endBattle = False
                                                    battleRunning = False
                                                    pygame.quit()
                                                    sys.exit()
                            
                            else:
                                if (playerAttack == "attack1"):
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.atk, hero.move1bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack2"):
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.atk, hero.move2bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack3"):
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.atk, hero.move3bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack4"):
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.atk, hero.move4bp, hero.level, enemy.dfs)

                                enemy.tempHp = enemy.tempHp - playerDmg    
                                enemyHealthBar = (enemyStartingHealth - enemy.tempHp) * enemyHealthBlock
                                #If enemy HP is empty, end of battle process starts
                                if (enemy.tempHp < 0):
                                    if (enemyHealthBar >= 215):
                                        enemyHealthBar = 215
                                    heroHealthRect = (884, 408, heroHealthBar, 10)
                                    enemyHealthRect = (335, 152, enemyHealthBar, 10)
                                    pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                                    pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)
                                    battleScreen.blit(battleBorder, (0, 500))
                                    battleText = pygame.font.Font.render(endMessageFont, "Enemy fainted!", True, (255, 255, 255))
                                    battleScreen.blit(battleText, (50, 550))
                                    endBattle = True
                                    pygame.display.update()

                                    while (endBattle == True):
                                        hero.afterWin(hero.getLevel() + 1000)
                                        hero.reset()
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                battleRunning = False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                (x, y) = pygame.mouse.get_pos()
                                                if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                    time.sleep(1)
                                                    endBattle = False
                                                    battleRunning = False
                                                

                    battleScreen.blit(battleBg, (0, 0))
                    battleScreen.blit(
                        heroImg, ((battleScreen_rect.width / 2) - 335, 320))
                    battleScreen.blit(battleBorder, (0, 500))
                    battleScreen.blit(
                        gruntImg, ((battleScreen_rect.width / 2) + 158, 88))

                    pygame.draw.rect(battleScreen, (240, 240, 240), attack1)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack2)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack3)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack4)

                    pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                    pygame.draw.rect(
                        battleScreen, (255, 0, 0), enemyHealthRect)

                    attack1Text = battleFont.render(
                        hero.move1name, True, (0, 0, 0))
                    attack1Text_rect = attack1Text.get_rect()
                    battleScreen.blit(attack1Text, (100 + ((((battleScreen_rect.width - 300) / 2) -
                                      attack1Text_rect.width) / 2), 535 + ((50 - attack1Text_rect.height) / 2)))

                    attack2Text = battleFont.render(
                        hero.move2name, True, (0, 0, 0))
                    attack2Text_rect = attack2Text.get_rect()
                    battleScreen.blit(attack2Text, (((battleScreen_rect.width / 2) + 50) + (
                        (((battleScreen_rect.width - 300) / 2) - attack2Text_rect.width) / 2), 535 + ((50 - attack2Text_rect.height) / 2)))

                    attack3Text = battleFont.render(
                        hero.move3name, True, (0, 0, 0))
                    attack3Text_rect = attack3Text.get_rect()
                    battleScreen.blit(attack3Text, (100 + ((((battleScreen_rect.width - 300) / 2) -
                                      attack3Text_rect.width) / 2), 630 + ((50 - attack3Text_rect.height) / 2)))

                    attack4Text = battleFont.render(
                        hero.move4name, True, (0, 0, 0))
                    attack4Text_rect = attack4Text.get_rect()
                    battleScreen.blit(attack4Text, (((battleScreen_rect.width / 2) + 50) + (
                        (((battleScreen_rect.width - 300) / 2) - attack4Text_rect.width) / 2), 630 + ((50 - attack4Text_rect.height) / 2)))
                    pygame.display.update()
                battleLoopBool = False

            self.screen.fill('black')

            if level1RunBool == True:
                self.level1.run()
            elif level2RunBool == True:
                self.level2.run()

            if nextLevelButton == True:
                pygame.display.update()
                self.clock.tick(FPS)

    def effectCheck():
        print("works")


if __name__ == '__main__':
    game = Game()
    game.run()
