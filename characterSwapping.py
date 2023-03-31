import pygame
#DONE - player can swap their character with another after defeating a miniboss or boss(final boss not applicable)

WIDTH = 500
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Character Swap")


pygame.font.init()
f= pygame.font.SysFont("Arial", 30)

door=pygame.image.load('prisonDoor.png')
doorImg= pygame.transform.scale(door,(50,100))

enemy = pygame.image.load('obamacube.png')
enemyImg = pygame.transform.scale(enemy, (100, 100))

arrow=pygame.image.load("arrow.png")
arrowImg=pygame.transform.scale(arrow,(100,100))
arrow_rect = arrowImg.get_rect(center=(WIDTH // 2, HEIGHT // 2))

images = [enemyImg, doorImg]

num_C = len(images)
c_Width=enemyImg.get_width()
c_Height=enemyImg.get_height()
select = []
total_width = num_C * c_Width + (num_C - 1) * 20
x_start = (WIDTH - total_width) // 2

for i in range(num_C):
    x = i*(c_Width+20)+x_start
    y=c_Height
    r= pygame.Rect(x,y,c_Width,c_Height)
    select.append(r)


yes_button = pygame.Rect(WIDTH//2-50+100,2.5+220,100,100-50)
no_button = pygame.Rect(WIDTH//2-50-100,2.5+220,100,100-50)

index=0
running = True
no=False
yes=False


while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
                    
            if yes_button.collidepoint(event.pos):
                    yes=True
                    running=False
            if no_button.collidepoint(event.pos):
                    no=True
                    running=False



    if no:
        print(f"Selected character stays same")
        break
    elif yes:
         print(f"Swapped characters") 
    separate=0
    screen.fill((255,255,255))
    for i in range(num_C):
        image=images[i]
        r=select[i]
        r.x=c_Height+separate
        separate=200
        screen.blit(image,r)
        if index is not None and i == index:
            pygame.draw.rect(screen,(0,0,0), r,2)
        else:
            pygame.draw.rect(screen,(0,0,0), r, 2)
   
    t=f.render("Swap character?", True,(0,0,0))
    t_r = t.get_rect(center=(WIDTH//2, 100//2))  

    pygame.draw.rect(screen, (0,0,0), yes_button,2)
    yes_text=f.render("Yes",True,(0,0,0))
    yes_text_rect = yes_text.get_rect(center=yes_button.center)
    
    pygame.draw.rect(screen, (0,0,0), no_button,2)
    no_text=f.render("No",True,(0,0,0))
    no_text_rect = no_text.get_rect(center=no_button.center)

    screen.blit(arrowImg,arrow_rect)
    screen.blit(no_text,no_text_rect)
    screen.blit(yes_text,yes_text_rect)
    screen.blit(t,t_r)
    pygame.display.flip()
pygame.quit()    