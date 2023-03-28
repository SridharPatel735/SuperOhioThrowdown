import pygame
import sys
import characterSelection, battleCalcs
from levelSettings import *
from level1 import Level1
from level2 import Level2
from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()
        lebronMoves = {
            battleCalcs.Move([0, 100, 10, 1, 1, 0, "Chasedown Block"]),
            battleCalcs.Move([0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"]),
            battleCalcs.Move([0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"]),
            battleCalcs.Move([100, 90, 10, 4, 0, 0, "Tomohawk Dunk"])
        }
        lebronStats = [85, 75, 60, 70]
        mainFighter = battleCalcs.Fighter(lebronStats, lebronMoves, 5000)
        #mainFighter = characterSelection.charSelection()
        print(mainFighter.atk)

        self.level1 = Level1()


        


    def run(self):
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
            
            if battleLoopBool:
                heroImg = pygame.image.load("lebron.png")
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
                attack2 = ((battleScreen_rect.width / 2) + 50, 535, (battleScreen_rect.width - 300) / 2, 50) 
                attack3 = (100, 630, (battleScreen_rect.width - 300) / 2, 50) 
                attack4 = ((battleScreen_rect.width / 2) + 50, 630, (battleScreen_rect.width - 300) / 2, 50) 
                menuText = battleFont.render('Success!', True, (255, 0, 0))
                menuText_rect = menuText.get_rect()
                menuText_rect.center = battleScreen_rect.center
                pygame.display.update()

                #opponent = ((battleScreen_rect.width / 2) + 158, 88, 150, 250)
                #hero = ((battleScreen_rect.width / 2) - 335, 250, 150, 250)
                while battleRunning:

                    #event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            battleRunning = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                battleRunning = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            (x, y) = pygame.mouse.get_pos()
                            if ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 535) and ( y <= 585)):
                                print("attack1")
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 535) and ( y <= 585)):
                                print("attack2")
                            elif ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 630) and ( y <= 680)):
                                print("attack3")
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 630) and ( y <= 680)):
                                print("attack4")
                            # if optionsMenu.rect.collidepoint(event.pos):
                            #     menuText = battleFont.render('Success!', True, (0, 0, 0))
                            #     menuText_rect = menuText.get_rect()
                            #     menuText_rect.centerx = battleScreen_rect.centerx
                            #     pygame.display.update()
                    battleScreen.blit(battleBg, (0,0))
                    battleScreen.blit(heroImg, ((battleScreen_rect.width / 2) - 335, 320))
                    battleScreen.blit(gruntImg, ((battleScreen_rect.width / 2) + 158, 88))
                    battleScreen.blit(menuText, battleScreen_rect.center)

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
            self.level1.run()
            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()
