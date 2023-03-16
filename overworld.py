#overWorld file
import pygame, time, random
import gameObjects, math

pygame.init()

fps = 120
clock = pygame.time.Clock()
obamaFix = 1

pygame.mixer.music.load("menumusic.mp3")
obama = pygame.mixer.Sound("letmebeclear.mp3")
battleLoopBool = False
test = True

bg = pygame.image.load('bg2.jpg')
bg_rect = bg.get_rect()
keys = {'right':False, 'up':False, 'left':False, 'down':False}

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

# creating avatar to move in overworld   
heroImg = pygame.image.load('diamond.png')
hero_rect = heroImg.get_rect()
heroSpeed = 1
'''
hero = battleCalcs.Fighter([1, 1, 1, 1], [{
    "Chasedown Block": battleCalcs.Move([0, 100, 10, 1, 1, 0]),
    "Yabadabadoo Old Navy": battleCalcs.Move([0, 50, 20, 2, 0, 0]),
    "Cleveland!! This is for You!": battleCalcs.Move([0, 100, 15, 3, 0, 0]),
    "Tomohawk Dunk": battleCalcs.Move([100, 90, 10, 4, 0, 0])
    }], 100)'''

enemy = pygame.image.load('obamacube.png')
enemyImg = pygame.transform.scale(enemy, (100, 100))
enemy_rect = enemy.get_rect()
enemy_rect.x = 400
enemy_rect.y = 300

level = 0

pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)
running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_TAB:
            battleLoopBool = True
        if event.key == pygame.K_RIGHT:
            keys['right'] = True
        elif event.key == pygame.K_LEFT:
            keys['left'] = True
        if event.key == pygame.K_UP:
            keys['up'] = True
        elif event.key == pygame.K_DOWN:
            keys['down'] = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            keys['right'] = False
        elif event.key == pygame.K_LEFT:
            keys['left'] = False
        if event.key == pygame.K_UP:
            keys['up'] = False
        elif event.key == pygame.K_DOWN:
            keys['down'] = False

    x, y = 0, 0
    if keys['right'] == True and (hero_rect.x + hero_rect.width) < screen_rect.width:
        x += heroSpeed
    if keys['left'] == True and hero_rect.x > 0:
        x -= heroSpeed
    if keys['down'] == True and (hero_rect.y + hero_rect.height) < screen_rect.height:
        y += heroSpeed
    if keys['up'] == True and hero_rect.y > 0:
        y -= heroSpeed
    
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            x = math.sqrt(x)
            y = math.sqrt(y)
        elif x > 0 and y < 0:
            x = math.sqrt(x)
            y = -y
            y = math.sqrt(y)
            y = -y
        elif x < 0 and y > 0:
            x = -x
            x = math.sqrt(x)
            x = -x
            y = math.sqrt(y)
        else:
            x = -x
            x = math.sqrt(x)
            x = -x
            y = -y
            y = math.sqrt(y)
            y = -y

    hero_rect.x += x
    hero_rect.y += y

    '''if hero_rect.colliderect(enemy_rect):
        enemy_rect.x = 0
        #pygame.mixer.music.pause()
        #pygame.mixer.Sound.play(obama)
        #time.sleep(2.50)
        #enemyImg.set_alpha(0)
        #pygame.mixer.music.unpause()
        screen.fill((0, 0, 0))
        battleLoopBool = True'''

    #battle loop
    if battleLoopBool:
        print("placeholder")
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
                        print ("test")
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
        
        

    if (test):
        screen.blit(bg, (0,0))
        screen.blit(enemyImg, enemy_rect)
        screen.blit(heroImg, hero_rect)
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()