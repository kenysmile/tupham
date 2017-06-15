
import random


class GameModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.y >= 1000:

            self.y = 0

            self.x = random.randint(0, 320)

