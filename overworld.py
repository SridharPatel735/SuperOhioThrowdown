#overWorld file
import pygame, time, random
import gameObjects

pygame.init()

fps = 120
clock = pygame.time.Clock()
obamaFix = 1

pygame.mixer.music.load("menumusic.mp3")
obama = pygame.mixer.Sound("letmebeclear.mp3")

bg = pygame.image.load('bg2.jpg')
bg_rect = bg.get_rect()

screen = pygame.display.set_mode((bg_rect.width, bg_rect.height))
screen_rect = screen.get_rect()

# creating avatar to move in overworld   
heroImg = pygame.image.load('diamond.png')
hero_rect = heroImg.get_rect()
heroSpeed = 5

enemy = pygame.image.load('obamacube.png')
enemyImg = pygame.transform.scale(enemy, (100, 100))
enemy_rect = enemy.get_rect()
enemy_rect.x = 400
enemy_rect.y = 300

pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and (hero_rect.x + hero_rect.width) < screen_rect.width:
            hero_rect.x += heroSpeed
        if event.key == pygame.K_LEFT and hero_rect.x > 0:
            hero_rect.x -= heroSpeed
        if event.key == pygame.K_DOWN and (hero_rect.y + hero_rect.height) < screen_rect.height:
            hero_rect.y += heroSpeed
        if event.key == pygame.K_UP and hero_rect.y > 0:
            hero_rect.y -= heroSpeed
        

    if hero_rect.colliderect(enemy_rect):
        while obamaFix > 0:
            obamaFix -= 1
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(obama)
            time.sleep(2.50)
            enemyImg.set_alpha(0)
            pygame.mixer.music.unpause()


    screen.blit(bg, (0,0))
    screen.blit(enemyImg, enemy_rect)
    screen.blit(heroImg, hero_rect)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()