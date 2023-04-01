import pygame, main
pygame.init()
def p():
    WIDTH=1280
    HEIGHT=720
    screen=pygame.display.set_mode((WIDTH,HEIGHT))

    pygame.display.set_caption("Pause Menu")
    print(type(main.hero.imageSource))
    hImg = pygame.image.load(main.hero.imageSource)
<<<<<<< HEAD
    player_stats = {'lvl':main.hero.level,'hp': main.hero.hp, 'atk': main.hero.atk, 'def': main.hero.dfs, 'spd': main.hero.spd}
    move_stats_1= {'bp':main.hero.move1bp,'acc': main.hero.move1acc, 'pp': main.hero.move1pp, 'efc': main.hero.move1effect, 'pri': main.hero.move1priority}
    move_stats_2= {'bp':main.hero.move2bp,'acc': main.hero.move2acc, 'pp': main.hero.move2pp, 'efc': main.hero.move2effect, 'pri': main.hero.move2priority}
    move_stats_3= {'bp':main.hero.move3bp,'acc': main.hero.move3acc, 'pp': main.hero.move3pp, 'efc': main.hero.move3effect, 'pri': main.hero.move3priority}
    move_stats_4= {'bp':main.hero.move3bp,'acc': main.hero.move4acc, 'pp': main.hero.move4pp, 'efc': main.hero.move4effect, 'pri': main.hero.move4priority}

=======
    player_stats = {'lvl':main.hero.level,'hp': main.hero.hp, 'atk': main.hero.atk, 'dfs': main.hero.dfs, 'spd': main.hero.spd}
>>>>>>> 4134549c301942e75bea83dd6940368ba88dd6f9
    heroImg = pygame.transform.scale(hImg,(320, 440))
    

    def pause():
        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',30)
        continue_t=f.render('Continue', True, (0,0,0))
        quit_t=f.render('Quit',True,(0,0,0))
        
        move_1=f.render(main.hero.move1name, True,(0,0,0))
        move_2=f.render(main.hero.move2name, True,(0,0,0))
        move_3=f.render(main.hero.move3name, True,(0,0,0))
        move_4=f.render(main.hero.move4name, True,(0,0,0))
        h_r=heroImg.get_rect(center=(WIDTH/2-300,HEIGHT/2-100))
        move_1_r=move_1.get_rect(center=(WIDTH/2+300,HEIGHT/2-200))
        move_2_r=move_2.get_rect(center=(WIDTH/2+300,HEIGHT/2-150))
        move_3_r=move_3.get_rect(center=(WIDTH/2+300,HEIGHT/2-100))
        move_4_r=move_4.get_rect(center=(WIDTH/2+300,HEIGHT/2-50))

        continue_r= continue_t.get_rect(center=(WIDTH/2-300,HEIGHT*9/10))
        quit_r= quit_t.get_rect(center=(WIDTH/2+300,HEIGHT*9/10))

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
        pygame.draw.rect(screen,(0,0,0), h_r)

        

        descBox = pygame.Rect(WIDTH/2-175, HEIGHT/2+200, 350, 60)
        pygame.draw.rect(screen, (255, 255, 255), descBox)
        pygame.draw.rect(screen, (0, 0, 0), descBox, 2)

        screen.blit(heroImg,h_r)
        screen.blit(continue_t,continue_r)
        screen.blit(quit_t,quit_r)
        screen.blit(move_1,move_1_r)
        screen.blit(move_2,move_2_r)
        screen.blit(move_3,move_3_r)
        screen.blit(move_4,move_4_r)
        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',20)
        lvl_box = pygame.Rect(WIDTH/2-460, HEIGHT/2-350, 320, 30)
        pygame.draw.rect(screen, (255, 255, 255), lvl_box)
        pygame.draw.rect(screen, (0, 0, 0), lvl_box, 2)

        stat_box = pygame.Rect(WIDTH/2-460, HEIGHT/2+100, 320, 50)
        pygame.draw.rect(screen, (255, 255, 255), stat_box)
        pygame.draw.rect(screen, (0, 0, 0), stat_box, 2)
        lvl_text = f"LVL: {player_stats['lvl']}"
        lvl_render = f.render(lvl_text, True, (0, 0, 0))

        lvl_render_rect = lvl_render.get_rect(center=(WIDTH/2-380,HEIGHT/2-335))
        screen.blit(lvl_render, lvl_render_rect)
        f=pygame.font.Font('kvn-pokemon-gen-5.ttf',20)

        stat_text = f"HP: {player_stats['hp']}  ATK: {player_stats['atk']}"
        stat_text_2=f"DEF: {player_stats['def']}  SPD: {player_stats['spd']}"
        stat_render = f.render(stat_text, True, (0, 0, 0))
        stat_render_rect = stat_render.get_rect(center=(WIDTH/2-350,HEIGHT/2+120))
        screen.blit(stat_render, stat_render_rect)

        stat_render_2 = f.render(stat_text_2, True, (0, 0, 0))
        stat_render_rect_2 = stat_render_2.get_rect(center=(WIDTH/2-350,HEIGHT/2+140))
        screen.blit(stat_render_2, stat_render_rect_2)

        pygame.display.update()

    running = True
    paused = False


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if paused:
                        f=pygame.font.Font(None,50)
                        continue_t=f.render('Continue', True, (0,0,0),2)
                        quit_t=f.render('Quit',True,(0,0,0),2)
                        continue_r= continue_t.get_rect(center=(WIDTH/2-300,HEIGHT*9/10))
                        quit_r= quit_t.get_rect(center=(WIDTH/2+300,HEIGHT*9/10))
                        move_1=f.render(main.hero.move1name, True,(0,0,0))
                        move_2=f.render(main.hero.move2name, True,(0,0,0))
                        move_3=f.render(main.hero.move3name, True,(0,0,0))
                        move_4=f.render(main.hero.move4name, True,(0,0,0))
                        move_1_r=move_1.get_rect(center=(WIDTH/2+150,HEIGHT/2-200))
                        move_2_r=move_2.get_rect(center=(WIDTH/2+150,HEIGHT/2-150))
                        move_3_r=move_3.get_rect(center=(WIDTH/2+150,HEIGHT/2-100))
                        move_4_r=move_4.get_rect(center=(WIDTH/2+150,HEIGHT/2-50))
                        mouse_pos = pygame.mouse.get_pos()
                        if continue_r.collidepoint(mouse_pos):
                            paused = False
                            return 1
                        elif quit_r.collidepoint(mouse_pos):
                            running = False
                            return 2
                        elif move_1_r.collidepoint(mouse_pos):
                            m_stats_1 = f"Base Power: {move_stats_1['bp']}  Accuracy: {move_stats_1['acc']} Power Points:{move_stats_1['pp']}"
                            m_render_1 = f.render(m_stats_1, True, (0, 0, 0))
                            m_render_rect_1 = m_render_1.get_rect(center=(WIDTH/2-350,HEIGHT/2+120))
                            screen.blit(stat_render, stat_render_rect)
                        elif move_2_r.collidepoint(mouse_pos):
                            print()
                        elif move_3_r.collidepoint(mouse_pos):
                            print()
                        elif move_4_r.collidepoint(mouse_pos):
                            print()            


        if paused:
            pause()

            
            
        pygame.display.flip()    
    pygame.quit()