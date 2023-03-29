import pygame
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

class Game:


    def __init__(self):
        global lebronStats
        global lebronMoves
        global luffyStats
        global luffyMoves
        global bruceStats
        global bruceMoves
        global hero

        pygame.init()
        charSelected = characterSelection.charSelection()
        if (charSelected == 1):
            hero = battleCalcs.Fighter(lebronStats, lebronMoves, 5000)
        elif (charSelected == 2):
            hero = battleCalcs.Fighter(bruceStats, bruceMoves, 5000)
        elif (charSelected == 3):
            hero = battleCalcs.Fighter(luffyStats, luffyMoves, 5000)
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()
        self.level1 = Level1()

    def run(self):
        global hero

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
                battleLoopBool = True
                gameObjects.battleLoopGrunt = False

            if battleLoopBool:
                heroImg = pygame.image.load("sridhar_player_icon_back.png")
                heroImg_rect = heroImg.get_rect()
                gruntImg = pygame.image.load("grunt_battle.png")
                gruntImg_rect = heroImg.get_rect()
                battleBg = pygame.image.load("battleBgTemplate.jpg")
                battleBg_rect = battleBg.get_rect()
                battleScreen = pygame.display.set_mode((battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)

                optionsMenu = (1000, 600, 50, 50)

                attack1 = (100, 535, (battleScreen_rect.width - 300) / 2, 50)
                attack2 = ((battleScreen_rect.width / 2) + 50, 535,
                           (battleScreen_rect.width - 300) / 2, 50)
                attack3 = (100, 630, (battleScreen_rect.width - 300) / 2, 50)
                attack4 = ((battleScreen_rect.width / 2) + 50, 630,
                           (battleScreen_rect.width - 300) / 2, 50)

                while battleRunning:
                    playerAttack = ""
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
                                playerAttack = "attack3"
                            # if optionsMenu.rect.collidepoint(event.pos):
                            #     menuText = battleFont.render('Success!', True, (0, 0, 0))
                            #     menuText_rect = menuText.get_rect()
                            #     menuText_rect.centerx = battleScreen_rect.centerx
                            #     pygame.display.update()
                    
                    if (playerAttack != ""):
                        if (playerAttack == "attack1"):
                            print("attack1")

                    battleScreen.blit(battleBg, (0, 0))
                    battleScreen.blit(heroImg, ((battleScreen_rect.width / 2) - 335, 320))
                    battleScreen.blit(gruntImg, ((battleScreen_rect.width / 2) + 158, 88))

                    pygame.draw.rect(battleScreen, (240, 240, 240), attack1)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack2)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack3)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack4)
                    
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
