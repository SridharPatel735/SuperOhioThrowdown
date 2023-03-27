import pygame
#DONE- Character selection to be used during the tutorial of the game
#sprites here are temporary, not official
pygame.init()


WIDTH = 500
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Character Selection")
door=pygame.image.load('door.png')

doorImg= pygame.transform.scale(door,(50,100))

enemy = pygame.image.load('obamacube.png')
enemyImg = pygame.transform.scale(enemy, (100, 100))
images = [enemyImg, pygame.image.load("diamond.png"), doorImg]

pygame.font.init()
f= pygame.font.SysFont("Arial", 30)\

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

select_button = pygame.Rect(WIDTH//2-50,2.5*c_Height,100,c_Height-50)

index=0
running = True
character_1=False
character_2=False
character_3=False
selected_character=None


while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (num_C):
                rect=select[i]
                if rect.collidepoint(event.pos):
                    index=i    
                    
            if select_button.collidepoint(event.pos):
                    if index==0:
                        character_1=True
                        print(1)
                    elif index==1:
                        character_2=True
                        print(2)
                    elif index==2:
                        character_3=True
                        print(3)
                    break

    if character_1:
        selected_character = 1
    elif character_2:
        selected_character = 2
    elif character_3:
        selected_character = 3

    if selected_character is not None:
        print(f"Selected character: {selected_character}")
        break 

    screen.fill((255,255,255))
    for i in range(num_C):
        image=images[i]
        r=select[i]
        screen.blit(image,r)
        if index is not None and i == index:
            pygame.draw.rect(screen,(0,0,0), r,2)
        else:
            pygame.draw.rect(screen,(0,0,0), r, 1)
    t=f.render("Select character", True,(0,0,0))
    t_r = t.get_rect(center=(WIDTH//2, c_Height//2))  

    pygame.draw.rect(screen, (0,0,0), select_button,2)
    select_text=f.render("Select",True,(0,0,0))
    select_text_rect = select_text.get_rect(center=select_button.center)

    screen.blit(select_text,select_text_rect)
    screen.blit(t,t_r)
    pygame.display.flip()
pygame.quit()    