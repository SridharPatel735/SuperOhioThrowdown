import pygame
pygame.init()

WIDTH=640
HEIGHT=480
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen_rect = screen.get_rect()

pygame.display.set_caption("Pause Menu")
hImg = pygame.image.load('diamond.png')
heroImg= pygame.transform.scale(hImg,(100,200))

hero_rect = hImg.get_rect()
heroSpeed = 5

def pause():
    f=pygame.font.Font(None,50)
    continue_t=f.render('Continue', True, (0,0,0))
    quit_t=f.render('Quit',True,(0,0,0))
    
    move_1=f.render('move 1', True,(0,0,0))
    move_2=f.render('move 2', True,(0,0,0))
    move_3=f.render('move 3', True,(0,0,0))
    move_4=f.render('move 4', True,(0,0,0))
    h_r=heroImg.get_rect(center=(WIDTH/2-150,HEIGHT/2-50))
    move_1_r=move_1.get_rect(center=(WIDTH/2+150,HEIGHT/2-100))
    move_2_r=move_2.get_rect(center=(WIDTH/2+150,HEIGHT/2-50))
    move_3_r=move_3.get_rect(center=(WIDTH/2+150,HEIGHT/2))
    move_4_r=move_4.get_rect(center=(WIDTH/2+150,HEIGHT/2+50))

    continue_r= continue_t.get_rect(center=(WIDTH/2-150,HEIGHT*9/10))
    quit_r= quit_t.get_rect(center=(WIDTH/2+150,HEIGHT*9/10))

    pygame.draw.rect(screen,(0,0,0), continue_r,2)

    pygame.draw.rect(screen,(0,0,0), (WIDTH,HEIGHT,150,150))
    dim=pygame.Surface(screen.get_size())
    dim.set_alpha(64)
    dim.fill((255,255,255))
    screen.blit(dim,(0,0))
    pygame.draw.rect(screen,(0,0,0), continue_r,2)
    pygame.draw.rect(screen,(0,0,0), quit_r,2)
    pygame.draw.rect(screen,(0,0,0), move_1_r,2)
    pygame.draw.rect(screen,(0,0,0), move_2_r,2)
    pygame.draw.rect(screen,(0,0,0), move_3_r,2)
    pygame.draw.rect(screen,(0,0,0), move_4_r,2)
    pygame.draw.rect(screen,(0,0,0), h_r,2)

    box = pygame.Rect(WIDTH/2-225, HEIGHT/2-200, 150, 250)
    pygame.draw.rect(screen, (255, 255, 255), box)
    pygame.draw.rect(screen, (0, 0, 0), box, 2)

    descBox = pygame.Rect(WIDTH/2-175, HEIGHT/2+115, 350, 50)
    pygame.draw.rect(screen, (255, 255, 255), descBox)
    pygame.draw.rect(screen, (0, 0, 0), descBox, 2)

    screen.blit(heroImg,h_r)
    screen.blit(continue_t,continue_r)
    screen.blit(quit_t,quit_r)
    screen.blit(move_1,move_1_r)
    screen.blit(move_2,move_2_r)
    screen.blit(move_3,move_3_r)
    screen.blit(move_4,move_4_r)
    f=pygame.font.Font(None,20)
    lvl_box = pygame.Rect(WIDTH/2-225, HEIGHT/2-230, 150, 30)
    pygame.draw.rect(screen, (255, 255, 255), lvl_box)
    pygame.draw.rect(screen, (0, 0, 0), lvl_box, 2)

    stat_box = pygame.Rect(WIDTH/2-225, HEIGHT/2+50, 150, 50)
    pygame.draw.rect(screen, (255, 255, 255), stat_box)
    pygame.draw.rect(screen, (0, 0, 0), stat_box, 2)
    lvl_text = f"LVL: {player_stats['lvl']}"
    lvl_render = f.render(lvl_text, True, (0, 0, 0))

    lvl_render_rect = lvl_render.get_rect(center=(WIDTH/2-150,HEIGHT/2-217))
    screen.blit(lvl_render, lvl_render_rect)

    stat_text = f"HP: {player_stats['hp']}  ATK: {player_stats['atk']}"
    stat_text_2=f"DEF: {player_stats['def']}  SPD: {player_stats['spd']}"
    stat_render = f.render(stat_text, True, (0, 0, 0))
    stat_render_rect = stat_render.get_rect(center=(WIDTH/2-150,HEIGHT/2+60))
    screen.blit(stat_render, stat_render_rect)

    stat_render_2 = f.render(stat_text_2, True, (0, 0, 0))
    stat_render_rect_2 = stat_render_2.get_rect(center=(WIDTH/2-150,HEIGHT/2+80))
    screen.blit(stat_render_2, stat_render_rect_2)

    pygame.display.update()

running = True
paused = False
bg = pygame.image.load('bg2.jpg')
bg_rect = bg.get_rect()
player_stats = {'lvl':1,'hp': 100, 'atk': 10, 'def': 5, 'spd': 20}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if paused:
                f=pygame.font.Font(None,50)
                continue_t=f.render('Continue', True, (0,0,0),2)
                quit_t=f.render('Quit',True,(0,0,0),2)
                continue_r= continue_t.get_rect(center=(WIDTH/2-150,HEIGHT*9/10))
                quit_r= quit_t.get_rect(center=(WIDTH/2+150,HEIGHT*9/10))
                move_1=f.render('move 1', True,(0,0,0),2)
                move_2=f.render('move 2', True,(0,0,0),2)
                move_3=f.render('move 3', True,(0,0,0),2)
                move_4=f.render('move 4', True,(0,0,0),2)
                move_1_r=move_1.get_rect(center=(WIDTH/2+150,HEIGHT/2-100))
                move_2_r=move_2.get_rect(center=(WIDTH/2+150,HEIGHT/2-50))
                move_3_r=move_3.get_rect(center=(WIDTH/2+150,HEIGHT/2))
                move_4_r=move_4.get_rect(center=(WIDTH/2+150,HEIGHT/2+50))
                mouse_pos = pygame.mouse.get_pos()
                if continue_r.collidepoint(mouse_pos):
                    paused = False
                elif quit_r.collidepoint(mouse_pos):
                    running = False
                elif move_1_r.collidepoint(mouse_pos):
                    print()
                elif move_2_r.collidepoint(mouse_pos):
                    print()
                elif move_3_r.collidepoint(mouse_pos):
                    print()
                elif move_4_r.collidepoint(mouse_pos):
                    print()            

    if paused:
        pause()
    else:
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and (hero_rect.x + hero_rect.width) < screen_rect.width:
                hero_rect.x += heroSpeed
            if event.key == pygame.K_LEFT and hero_rect.x > 0:
                hero_rect.x -= heroSpeed
            if event.key == pygame.K_DOWN and (hero_rect.y + hero_rect.height) < screen_rect.height:
                hero_rect.y += heroSpeed
            if event.key == pygame.K_UP and hero_rect.y > 0:
                hero_rect.y -= heroSpeed
        # Game code goes here
        screen.blit(bg, (0,0))
        screen.blit(hImg, hero_rect)

    pygame.display.flip()    
pygame.quit()