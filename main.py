import pygame
import sys
from levelSettings import *
from level1 import Level1
from level2 import Level2
import gameObjects
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


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()

    def run(self):
        global level1Trigger, level2Trigger, level1RunBool, level2RunBool
        mainLoop = True
        nextLevelButton = True
        runOnce = True

        pygame.mixer.music.load("menumusic.mp3")
        battleLoopBool = False

        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(-1)

        while (mainLoop):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and runOnce == True:
                    level1Trigger = False
                    level2Trigger = True
                    runOnce = False

            if gameObjects.endOfLevelOne == True:
                level2Trigger = True
                level1Trigger = False
                gameObjects.endOfLevelOne = False

            if level1Trigger == True:
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
                # TODO - Add text to black screen
                if nextLevelButton == True:
                    self.level2 = Level2()
                    level2Trigger = False
                    level2RunBool = True
                    level1RunBool = False

            if gameObjects.battleLoopGrunt == True:
                battleLoopBool = True
                gameObjects.battleLoopGrunt = False

            if gameObjects.battleLoopMiniBoss == True:
                battleLoopBool = True
                gameObjects.battleLoopMiniBoss = False

            if gameObjects.battleLoopBoss == True:
                battleLoopBool = True
                gameObjects.battleLoopBoss = False

            if battleLoopBool:
                heroImg = pygame.image.load("sridhar_player_icon_back.png")
                heroImg_rect = heroImg.get_rect()
                gruntImg = pygame.image.load("grunt_battle.png")
                gruntImg_rect = heroImg.get_rect()
                battleBg = pygame.image.load("battleBgTemplate.jpg")
                battleBg_rect = battleBg.get_rect()
                battleScreen = pygame.display.set_mode(
                    (battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)

                optionsMenu = (1000, 600, 50, 50)

                attack1 = (100, 535, (battleBg_rect.width - 300) / 2, 50)
                attack2 = ((battleBg_rect.width / 2) + 50, 535,
                           (battleBg_rect.width - 300) / 2, 50)
                attack3 = (100, 630, (battleBg_rect.width - 300) / 2, 50)
                attack4 = ((battleBg_rect.width / 2) + 50, 630,
                           (battleBg_rect.width - 300) / 2, 50)

                #opponent = ((battleBg_rect.width / 2) + 158, 88, 150, 250)
                #hero = ((battleBg_rect.width / 2) - 335, 250, 150, 250)
                while battleRunning:

                    # event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            battleRunning = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                battleRunning = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            (x, y) = pygame.mouse.get_pos()
                            if ((x >= 100) and (x <= ((battleBg_rect.width - 300) / 2) + 100) and (y >= 535) and (y <= 585)):
                                print("attack1")
                            elif ((x >= (battleBg_rect.width / 2) + 50) and (x <= ((battleBg_rect.width - 300) / 2) + (battleBg_rect.width / 2) + 50) and (y >= 535) and (y <= 585)):
                                print("attack2")
                            elif ((x >= 100) and (x <= ((battleBg_rect.width - 300) / 2) + 100) and (y >= 630) and (y <= 680)):
                                print("attack3")
                            elif ((x >= (battleBg_rect.width / 2) + 50) and (x <= ((battleBg_rect.width - 300) / 2) + (battleBg_rect.width / 2) + 50) and (y >= 630) and (y <= 680)):
                                print("attack4")
                            # if optionsMenu.rect.collidepoint(event.pos):
                            #     menuText = battleFont.render('Success!', True, (0, 0, 0))
                            #     menuText_rect = menuText.get_rect()
                            #     menuText_rect.centerx = battleScreen_rect.centerx
                            #     pygame.display.update()
                    battleScreen.blit(battleBg, (0, 0))
                    battleScreen.blit(
                        heroImg, ((battleBg_rect.width / 2) - 335, 320))
                    battleScreen.blit(
                        gruntImg, ((battleBg_rect.width / 2) + 158, 88))

                    pygame.draw.rect(battleScreen, (255, 0, 0), optionsMenu)

                    pygame.draw.rect(battleScreen, (240, 240, 240), attack1)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack2)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack3)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack4)

                    #pygame.draw.rect(battleScreen, (0, 0, 0), opponent)
                    #pygame.draw.rect(battleScreen, (0, 0, 0), hero)
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


if __name__ == '__main__':
    game = Game()
    game.run()
