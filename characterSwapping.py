import pygame
#DONE - player can swap their character with another after defeating a miniboss or boss(final boss not applicable)

WIDTH = 500
HEIGHT = 300

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Character Swap")


pygame.font.init()
f= pygame.font.SysFont("Arial", 30)


yes_button = pygame.Rect(WIDTH//2-50+100,2.5*50,100,100-50)
no_button = pygame.Rect(WIDTH//2-50-100,2.5*50,100,100-50)

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

    screen.fill((255,255,255))
   
    t=f.render("Swap character?", True,(0,0,0))
    t_r = t.get_rect(center=(WIDTH//2, 100//2))  

    pygame.draw.rect(screen, (0,0,0), yes_button,2)
    yes_text=f.render("Yes",True,(0,0,0))
    yes_text_rect = yes_text.get_rect(center=yes_button.center)
    
    pygame.draw.rect(screen, (0,0,0), no_button,2)
    no_text=f.render("No",True,(0,0,0))
    no_text_rect = no_text.get_rect(center=no_button.center)

    screen.blit(no_text,no_text_rect)
    screen.blit(yes_text,yes_text_rect)
    screen.blit(t,t_r)
    pygame.display.flip()
pygame.quit()    