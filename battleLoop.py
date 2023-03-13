#overWorld file
import pygame, time, random
import gameObjects, math, battleCalcs, overworld

pygame.init()

fps = 120
clock = pygame.time.Clock()

#test grunt
grunt = battleCalcs.Fighter([1, 1, 1, 1], [{
    "Chasedown Block": battleCalcs.Move([0, 100, 10, 1, 1, 0]),
    "Yabadabadoo Old Navy": battleCalcs.Move([0, 50, 20, 2, 0, 0]),
    "Cleveland!! This is for You!": battleCalcs.Move([0, 100, 15, 3, 0, 0]),
    "Tomohawk Dunk": battleCalcs.Move([100, 90, 10, 4, 0, 0])
    }], 100)

#creating the miniboss and boss depending the level
if (overworld.level == 0):
    miniboss = battleCalcs.Fighter([1, 1, 1, 1], [{
    "Chasedown Block": battleCalcs.Move([0, 100, 10, 1, 1, 0]),
    "Yabadabadoo Old Navy": battleCalcs.Move([0, 50, 20, 2, 0, 0]),
    "Cleveland!! This is for You!": battleCalcs.Move([0, 100, 15, 3, 0, 0]),
    "Tomohawk Dunk": battleCalcs.Move([100, 90, 10, 4, 0, 0])
    }], 100)

    boss = battleCalcs.Fighter([1, 1, 1, 1], [{
    "Chasedown Block": battleCalcs.Move([0, 100, 10, 1, 1, 0]),
    "Yabadabadoo Old Navy": battleCalcs.Move([0, 50, 20, 2, 0, 0]),
    "Cleveland!! This is for You!": battleCalcs.Move([0, 100, 15, 3, 0, 0]),
    "Tomohawk Dunk": battleCalcs.Move([100, 90, 10, 4, 0, 0])
    }], 100)

running = True
while running:

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False