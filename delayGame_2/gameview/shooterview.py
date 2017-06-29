class ShooterView:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def draw(self):
        self.counter += 1
        if self.counter >= self.time:
            self.current_img += 1
            if self.current_img >= len(self.images):
                self.current_img = 0
                self.active = False
            self.counter = 0

        if self.active:
            self.screen.blit(self.images[self.current_img], (50, 50))