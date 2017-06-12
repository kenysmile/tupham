class GameView:
    def __init__(self, images, screen):
        self.image = images
        self.screen = screen

    def draw(self, gamemodel):
        self.screen.blit(self.image, (gamemodel.x, gamemodel.y))