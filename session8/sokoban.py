import pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

class Game:
    def __init__(self):
        print("pass")

    def console_draw(self):
        # draw os console
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x == self.dest.x:
                    print(" D ", end="")
                elif y == self.box.y and x ==self.box.x:
                    print(" B ", end="")
                elif y == self.pusher.y and x == self.pusher.x:
                    print(" P ", end="")
                else:
                    print(" - ", end="")
            print()

    def draw_image_center(self, object, screen):
        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height()) / 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self):
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))
        # screen.blit(pusher_image, (self.pusher.x * pixel, self.pusher.y * pixel))
        # screen.blit(box_image, (self.box.x * pixel, self.box.y * pixel))
        # screen.blit(dest_image, (self.dest.x * pixel, self.dest.y * pixel))
        self.draw_image_center(self.pusher, screen)
        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.dest, screen)

    def move(self, x, y):
        self.x = x
        self.y = y



class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h
class Pusher:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move_pusher(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.y += 1
        elif key[pygame.K_UP]:
            self.y -= 1
        elif key[pygame.K_RIGHT]:
            self.x += 1
        elif key[pygame.K_LEFT]:
            self.x -= 1
        return dx, dy
class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Dest:
    def __init__(self, x, y):
        self.x = x
        self.y = y



sokoban = Game()
sokoban.map = Map(5, 5)
sokoban.pusher = Pusher(1, 1)
sokoban.box = Box(2, 2)
sokoban.dest = Dest(3, 3)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
box_image = pygame.image.load("images/box.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
sokoban.box.image = box_image
sokoban.pusher.image = pusher_image
sokoban.dest.image = dest_image
pixel = 64

while not done:
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.pusher.move_pusher()

    sokoban.pusher.x += dx
    sokoban.pusher.y += dy

    sokoban.draw()
    pygame.display.flip()

