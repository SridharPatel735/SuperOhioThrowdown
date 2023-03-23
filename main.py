import pygame
import sys
from level1Settings import *
from level1 import Level
from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()


        self.level = Level()


    def run(self):
        pygame.mixer.music.load("menumusic.mp3")
        battleLoopBool = False
        
        pygame.mixer.music.set_volume(0.5)
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
                battleBg = pygame.image.load("battleBgTemplate.jpg")
                battleBg_rect = battleBg.get_rect()
                battleScreen = pygame.display.set_mode((battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)

                optionsMenu = (1000, 600, 50, 50) 
                while battleRunning:

                    #event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            battleRunning = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                battleRunning = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if optionsMenu.rect.collidepoint(event.pos):
                                menuText = battleFont.render('Success!', True, (0, 0, 0))
                                menuText_rect = menuText.get_rect()
                                menuText_rect.centerx = battleScreen_rect.centerx
                                pygame.display.update()
                    battleScreen.blit(battleBg, (0,0))
                    pygame.draw.rect(battleScreen, (255, 0, 0), optionsMenu)
                    pygame.display.update()
                battleLoopBool = False

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == '__main__':
    game = Game()
    game.run()
