#overWorld file
import pygame, time, random
import gameObjects

pygame.init()

# Initialize the game
bg_img = pygame.image.load('background.jpg')
bg_rect = bg_img.get_rect()

screen = pygame.display.set_mode((bg_rect.width + 400, bg_rect.height))
screen_rect = screen.get_rect()

left = pygame.draw.rect(screen, (0, 0, 255), (0, 0, 200, 666))
right = pygame.draw.rect(screen, (0, 0, 255), (1200, 0, 200, 666))

no_of_diamonds = 10
diamond_group = pygame.sprite.Group()
for i in range(no_of_diamonds):
   diamond_group.add(gameobjects.Diamond(screen_rect))

no_of_spaceships = 1
spaceship_group = pygame.sprite.Group()
for i in range(no_of_spaceships):
   spaceship_group.add(gameobjects.Spaceship(screen_rect))

# creating new groups for panel diamonds and variables to track saved or taken diamonds in the game
saved_diamonds = 0
saved_group = pygame.sprite.Group()   

taken_diamonds = 0
taken_group = pygame.sprite.Group()

# initialize font and game labels
font = pygame.font.Font('CoffeeHealing.ttf', 32)

# initializing left "taken" panel and blitting it
takenText = "Taken: {}"
formattedTaken = takenText.format(taken_diamonds)
takenLabel = font.render(formattedTaken, True, (255, 255, 255))
taken_rect = takenLabel.get_rect()
taken_rect.top = (left.top)
taken_rect.centerx = (left.centerx)
screen.blit(takenLabel, taken_rect)

# initializing right "saved" panel and blitting it
savedText = "Saved: {}"
formattedSaved = savedText.format(saved_diamonds)
savedLabel = font.render(formattedSaved, True, (255, 255, 255))
saved_rect = savedLabel.get_rect()
saved_rect.top = (right.top)
saved_rect.centerx = (right.centerx)
screen.blit(savedLabel, saved_rect)

#method to refresh the saved panel
def displaySaved():
    screen.fill((0, 0, 255), (1200, 0, 200, 50))
    savedText = "Saved: {}"
    formattedSaved = savedText.format(saved_diamonds)
    savedLabel = font.render(formattedSaved, True, (255, 255, 255))
    saved_rect = savedLabel.get_rect()
    saved_rect.top = (right.top)
    saved_rect.centerx = (right.centerx)
    screen.blit(savedLabel, saved_rect)
    saved_group.draw(screen)

#method to refresh the taken panel
def displayTaken():
    screen.fill((0, 0, 255), (0, 0, 200, 50))
    takenText = "Taken: {}"
    formattedTaken = takenText.format(taken_diamonds)
    takenLabel = font.render(formattedTaken, True, (255, 255, 255))
    taken_rect = takenLabel.get_rect()
    taken_rect.top = (left.top)
    taken_rect.centerx = (left.centerx)
    screen.blit(takenLabel, taken_rect)
    taken_group.draw(screen)

#renders all components on the screen
def render():
    screen.blit(bg_img,(200, 0))
    diamond_group.update()
    diamond_group.draw(screen)

    spaceship_group.update()
    spaceship_group.draw(screen)
    displaySaved()
    displayTaken()
    pygame.display.flip()


render()
running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #if mouse and diamonds collide, iterates the counter and updates the saved panel
            for sprite in diamond_group.sprites():
                if sprite.rect.collidepoint(event.pos):
                    saved_diamonds += 1
                    saved_group.add(gameobjects.SavedDiamond(right))
                    diamond_group.remove(sprite)
                    diamond_group.update()
                    diamond_group.draw(screen)
                    displaySaved()
                    
    
    #collision detection to keep diamonds and spaceship in bounds
    for sprite in diamond_group:
        if sprite.rect.x < 201 or sprite.rect.x > screen_rect.width - 301:
            sprite.rand_xd *= -1
        if sprite.rect.y < 0 or sprite.rect.y > screen_rect.height - 100:
            sprite.rand_yd *= -1
    
    for sprite in spaceship_group:
        if sprite.rect.x < 200 or sprite.rect.x > screen_rect.width - 328:
            sprite.rand_xd *= -1
        if sprite.rect.y < 0 or sprite.rect.y > screen_rect.height - 128:
            sprite.rand_yd *= -1

    collideCheck = pygame.sprite.groupcollide(diamond_group,spaceship_group,True,False)
    
    #if spaceship and diamonds collide, iterates the counter and updates the taken panel
    for collisionDetected in collideCheck:
        taken_diamonds += 1
        taken_group.add(gameobjects.TakenDiamond(left))
        displayTaken()

    #render
    render()
    time.sleep(0.05)

pygame.quit()