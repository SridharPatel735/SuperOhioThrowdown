import pygame, random, time
import sys
from levelSettings import *
from level1 import Level1
from level2 import Level2
import gameObjects, battleCalcs, characterSelection
from debug import debug


lebronStats = [85, 75, 60, 70]
lebronMoves = [[0, 100, 10, 1, 1, 0, "Chasedown Block"], [0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"], [0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"], [100, 90, 10, 4, 0, 0, "Tomohawk Dunk"]]

luffyStats = [50, 90, 90, 60]
luffyMoves = [[10, 100, 5, 9, 0, 0, "Gatling Punch"], [40, 100, 20, 0, 1, 0, "Jet Pistol"], [150, 100, 5, 5, 0, 0, "Giant Pistol"], [0, 100, 5, 10, 0, 0, "Gear Change"]]

bruceStats = [90, 45, 45, 110]
bruceMoves = [[30, 100, 10, 0, 0, 0, "Leg Sweep"], [10, 100, 3, 12, 0, 0, "One Inch Punch"], [15, 100, 10, 0, 1, 0, "Lop Sao Backfist"], [0, 100, 10, 1, 1, 0, "Block"], [7, 100, 5, 9, 0, 15, "Lightning Fast Punches"]]

hero = 0
enemy = 0
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
        global enemy
        global charSelected

        pygame.init()
        charSelected = characterSelection.charSelection()
        if (charSelected == 1):
            hero = battleCalcs.Fighter(lebronStats, lebronMoves, 5000, "lebron.png")
        elif (charSelected == 2):
            hero = battleCalcs.Fighter(bruceStats, bruceMoves, 5000, "bruce_lee.png")
        elif (charSelected == 3):
            hero = battleCalcs.Fighter(luffyStats, luffyMoves, 5000, "luffy.png")
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()
        self.level1 = Level1()

    def run(self):
        global lebronStats
        global lebronMoves
        global luffyStats
        global luffyMoves
        global bruceStats
        global bruceMoves
        global hero
        global enemy
        global charSelected

        global heroHealthBlock
        global enemyHealthBlock
        global heroStartingHealth
        global enemyStartingHealth
        global heroHealthRect
        global enemyHealthRect

        pygame.mixer.music.load("menumusic.mp3")
        battleLoopBool = False

        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    battleLoopBool = True
                 

            if gameObjects.battleLoopGrunt == True:
                gruntStats = [40, 40, 40, 40]
                gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"], [50, 100, 10, 0, 0, 0, "Punch"], [0, 100, 3, 3, 0, 0, "Get Angry"], [0, 100, 5, 16, 0, 0, "Stop Right There"]]
                enemy = battleCalcs.Fighter(gruntStats, gruntMoves, 5000, "grunt_battle.png")
                if (charSelected == 1):
                    hero = battleCalcs.Fighter(lebronStats, lebronMoves, 5000, "lebron.png")
                elif (charSelected == 2):
                    hero = battleCalcs.Fighter(bruceStats, bruceMoves, 5000, "bruce_lee.png")
                elif (charSelected == 3):
                    hero = battleCalcs.Fighter(luffyStats, luffyMoves, 5000, "luffy.png")
                
                healthLength = 215

                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp

                battleLoopBool = True
                gameObjects.battleLoopGrunt = False

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
                battleScreen = pygame.display.set_mode((battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)

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
                    enemyAttack = ""

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
                            # if optionsMenu.rect.collidepoint(event.pos):
                            #     menuText = battleFont.render('Success!', True, (0, 0, 0))
                            #     menuText_rect = menuText.get_rect()
                            #     menuText_rect.centerx = battleScreen_rect.centerx
                            #     pygame.display.update()

                    if (playerAttack != ""):
                        enemyMove = random.randint(1,4)
                        result = False
                        playerDmg = 0
                        enemyDmg = 0
                        
                        if (playerAttack == "attack1"):
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(hero.move1priority, enemy.move1priority, hero.spd, enemy.spd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(hero.move1priority, enemy.move2priority, hero.spd, enemy.spd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(hero.move1priority, enemy.move3priority, hero.spd, enemy.spd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(hero.move1priority, enemy.move4priority, hero.spd, enemy.spd)
                        elif (playerAttack == "attack2"):
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(hero.move2priority, enemy.move1priority, hero.spd, enemy.spd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(hero.move2priority, enemy.move2priority, hero.spd, enemy.spd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(hero.move2priority, enemy.move3priority, hero.spd, enemy.spd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(hero.move2priority, enemy.move4priority, hero.spd, enemy.spd)
                        elif (playerAttack == "attack3"):
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(hero.move3priority, enemy.move1priority, hero.spd, enemy.spd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(hero.move3priority, enemy.move2priority, hero.spd, enemy.spd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(hero.move3priority, enemy.move3priority, hero.spd, enemy.spd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(hero.move3priority, enemy.move4priority, hero.spd, enemy.spd)
                        elif (playerAttack == "attack4"):
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(hero.move4priority, enemy.move1priority, hero.spd, enemy.spd)
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(hero.move4priority, enemy.move2priority, hero.spd, enemy.spd)
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(hero.move4priority, enemy.move3priority, hero.spd, enemy.spd)
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(hero.move4priority, enemy.move4priority, hero.spd, enemy.spd)
                        
                        if (result):
                            if (playerAttack == "attack1"):
                                playerDmg = battleCalcs.damageCalc(hero.atk, hero.move1bp, hero.level, enemy.dfs)
                            elif (playerAttack == "attack2"):
                                playerDmg = battleCalcs.damageCalc(hero.atk, hero.move2bp, hero.level, enemy.dfs)
                            elif (playerAttack == "attack3"):
                                playerDmg = battleCalcs.damageCalc(hero.atk, hero.move3bp, hero.level, enemy.dfs)
                            elif (playerAttack == "attack4"):
                                playerDmg = battleCalcs.damageCalc(hero.atk, hero.move4bp, hero.level, enemy.dfs)
                            
                            enemy.hp = enemy.hp - playerDmg
                            enemyHealthBar = (enemyStartingHealth - enemy.hp) * enemyHealthBlock
                            if (enemy.hp <= 0):
                                battleRunning = False
                            
                            else:
                                if (enemyMove == 1):
                                    enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move1bp, enemy.level, hero.dfs)
                                elif (enemyMove == 2):
                                    enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move2bp, enemy.level, hero.dfs)
                                elif (enemyMove == 3):
                                    enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move3bp, enemy.level, hero.dfs)
                                elif (enemyMove == 4):
                                    enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move4bp, enemy.level, hero.dfs)

                                hero.hp = hero.hp - enemyDmg
                                heroHealthBar = (heroStartingHealth - hero.hp) * heroHealthBlock
                                if (hero.hp <= 0):
                                    battleRunning = False

                        elif (result == False):
                            if (enemyMove == 1):
                                enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move1bp, enemy.level, hero.dfs)
                            elif (enemyMove == 2):
                                enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move2bp, enemy.level, hero.dfs)
                            elif (enemyMove == 3):
                                enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move3bp, enemy.level, hero.dfs)
                            elif (enemyMove == 4):
                                enemyDmg = battleCalcs.damageCalc(enemy.atk, enemy.move4bp, enemy.level, hero.dfs)

                            hero.hp = hero.hp - enemyDmg
                            heroHealthBar = (heroStartingHealth - hero.hp) * heroHealthBlock
                            if (hero.hp <= 0):
                                time.sleep(2)
                                battleRunning = False
                            
                            else:
                                if (playerAttack == "attack1"):
                                    playerDmg = battleCalcs.damageCalc(hero.atk, hero.move1bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack2"):
                                    playerDmg = battleCalcs.damageCalc(hero.atk, hero.move2bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack3"):
                                    playerDmg = battleCalcs.damageCalc(hero.atk, hero.move3bp, hero.level, enemy.dfs)
                                elif (playerAttack == "attack4"):
                                    playerDmg = battleCalcs.damageCalc(hero.atk, hero.move4bp, hero.level, enemy.dfs)

                                enemy.hp = enemy.hp - playerDmg    
                                enemyHealthBar = (enemyStartingHealth - enemy.hp) * enemyHealthBlock
                                if (enemy.hp <= 0):
                                    time.sleep(2)
                                    battleRunning = False
                                                

                    battleScreen.blit(battleBg, (0, 0))
                    battleScreen.blit(heroImg, ((battleScreen_rect.width / 2) - 335, 320))
                    battleScreen.blit(battleBorder, (0, 500))
                    battleScreen.blit(gruntImg, ((battleScreen_rect.width / 2) + 158, 88))

                    pygame.draw.rect(battleScreen, (240, 240, 240), attack1)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack2)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack3)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack4)

                    pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                    pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)
                    
                    attack1Text = battleFont.render(hero.move1name, True, (0, 0, 0))
                    attack1Text_rect = attack1Text.get_rect()
                    battleScreen.blit(attack1Text, (100 + ((((battleScreen_rect.width - 300) / 2) - attack1Text_rect.width) / 2), 535 + ((50 - attack1Text_rect.height) / 2)))

                    attack2Text = battleFont.render(hero.move2name, True, (0, 0, 0))
                    attack2Text_rect = attack2Text.get_rect()
                    battleScreen.blit(attack2Text, (((battleScreen_rect.width / 2) + 50) + ((((battleScreen_rect.width - 300) / 2) - attack2Text_rect.width) / 2), 535 + ((50 - attack2Text_rect.height) / 2)))

                    attack3Text = battleFont.render(hero.move3name, True, (0, 0, 0))
                    attack3Text_rect = attack3Text.get_rect()
                    battleScreen.blit(attack3Text, (100 + ((((battleScreen_rect.width - 300) / 2) - attack3Text_rect.width) / 2), 630 + ((50 - attack3Text_rect.height) / 2)))

                    attack4Text = battleFont.render(hero.move4name, True, (0, 0, 0))
                    attack4Text_rect = attack4Text.get_rect()
                    battleScreen.blit(attack4Text, (((battleScreen_rect.width / 2) + 50) + ((((battleScreen_rect.width - 300) / 2) - attack4Text_rect.width) / 2), 630 + ((50 - attack4Text_rect.height) / 2)))
                    pygame.display.update()
                battleLoopBool = False

            self.screen.fill('black')
            self.level1.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
