from gamecontrollers.gamecontrollers import GameControllers
from gamemodel.gamemodel import GameModel
from gameview.zombieview import ZombieView
from gameview.gameview import GameView

import pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

bossmodel = GameModel(1, 1)
bossview = GameView(pygame.image.load("images/cs1.png"), screen)
boss = GameControllers(bossmodel, bossview)

counter = 0
creep_animations = [
    pygame.image.load("images/cs1.png"),
    pygame.image.load("images/cs2.png"),
    pygame.image.load("images/cs3.png"),
    pygame.image.load("images/cs4.png"),
    pygame.image.load("images/cs5.png"),
    pygame.image.load("images/cs6.png"),
    pygame.image.load("images/cs7.png"),
    pygame.image.load("images/cs8.png"),
    pygame.image.load("images/cs9.png"),
    pygame.image.load("images/cs10.png"),]

creep = ZombieView(creep_animations, screen)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    boss.counter += 1
    if boss.counter >= 10:
        boss.move(1, 0)
        boss.counter = 0


    creep.draw()
    boss.draw()
    pygame.display.flip()
