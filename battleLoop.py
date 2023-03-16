#overWorld file
import pygame, time, random

pygame.init()

fps = 120
clock = pygame.time.Clock()


def battleLoop():
    print("test")

    battleBg = pygame.image.load("battleBgTemplate.jpg")
    battleBg_rect = battleBg.get_rect()
    battleScreen = pygame.display.set_mode((battleBg_rect.width, battleBg_rect.height))
    battleScreen_rect = battleScreen.get_rect()
    running = True
    while running:

        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    battleScreen.blit(battleBg, (0,0))
    pygame.display.update()
    #clock.tick(fps)

    
pygame.quit()