from gamecontrollers.gamecontrollers import GameControllers
from gamemodel.gamemodel import GameModel
from gameview.bossesview import BossView
from gameview.gameview import GameView
from gameview.creepview import CreepView

import random
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
x = random.randint(0, 500)
bonusmodel = GameModel(x, 1)
bonusview = GameView(pygame.image.load("images/pusher.png"), screen)
bonus = GameControllers(bonusmodel, bonusview)

shootermodel = GameModel(600, 1)
shooterview = GameView(pygame.image.load("images/pusher.png"), screen)
shooter = GameControllers(shootermodel, shooterview)

x = random.randint(0, 500)
bossmodel = GameModel(x, 1)
bossview = GameView(pygame.image.load("images/box.png"), screen)
boss = GameControllers(bossmodel, bossview)


x = random.randint(0, 500)
bossmodel_1 = GameModel(x, 1)
bossview_1 = GameView(pygame.image.load("images/box.png"), screen)
boss_1 = GameControllers(bossmodel_1, bossview_1)

x = random.randint(0,500)
y = random.randint(0, 500)
bossmodel_2 = GameModel(x, 1)
bossview_2 = GameView(pygame.image.load("images/box.png"), screen)
boss_2 = GameControllers(bossmodel_2, bossview_2)

x = random.randint(0,500)
y = random.randint(0, 500)
bossmodel_3 = GameModel(x, 1)
bossview_3 = GameView(pygame.image.load("images/box.png"), screen)
boss_3 = GameControllers(bossmodel_3, bossview_3)

# x = random.randint(0,500)
# y = random.randint(0, 500)    # pygame.image.load("images.cs2.png"),]
# screenmodel = GameModel(640,640)
# screenview = GameView(pygame.image.load("images/screen1.png"), screen)
# abc = GameControllers(screenmodel, screenview)
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

creep = CreepView(creep_animations, screen)
x = 0
y = 0
while not done:
    dx = 0

    dy = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    boss.counter += 1
    if boss.counter >= 5:
        # boss_3.move(0, 1)

        boss.move(0, 1)
        boss_1.move(0, 2)
        boss_2.move(0, 3)
        boss.counter = 0
    bonus.move(0, 0.04)
    # boss.move(0, 1)

    # boss_3.draw()
    shooter.draw()
    bonus.draw()
    boss_2.draw()
    boss_1.draw()
    boss.draw()
    # creep.draw()
    pygame.display.flip()
