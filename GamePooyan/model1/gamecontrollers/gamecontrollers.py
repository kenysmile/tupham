import pygame
class GameControllers:
    def __init__(self, gamemodel, gameview):
        self.gamemodel = gamemodel
        self.gameview = gameview
        self.counter = 0

    def draw(self):
        self.gameview.draw(self.gamemodel)

    def move(self, dx, dy):
        self.gamemodel.move(dx, dy)
