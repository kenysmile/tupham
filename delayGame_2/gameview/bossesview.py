import random
class BossView:
    def __init__(self, images, screen):
        self.images = images
        self.screen = screen
        self.current_img = 0
        self.counter = 0
        self.time = 100
        self.active = True
    def draw(self, model, active):

        self.counter += 1
        if self.counter >= self.time:
            model.y += 2
        if model.y >= 500:
            model.y = 0
            model.x = random.randint(255, 600)
            active = False
        # if active:
            self.screen.blit(self.images, model.x, model.y)



