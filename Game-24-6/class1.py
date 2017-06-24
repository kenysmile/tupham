import pygame
import random
class Game:
    def __init__(self):
        print("Initialine")

    def console_draw(self):
        for y in range(self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x == self.dest.x:
                    print(" D ", end = "")
                elif y == self.box.y  and x == self.box.x:
                    print(" B ", end = "")
                elif y == self.pusher.y and x == self.pusher.x:
                    print(" P ", end = "")
                elif y == self.pusher_1.y and x == self.pusher_1.x:
                    print(" P1 ", end ="")
                else:
                    print(" - ", end = "")
            print()

    def draw_image_center(self, object, screen):
        w = (pixel - object.image.get_width())/ 2 + object.x * pixel
        h = (pixel - object.image.get_height())/ 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self):
#         draw in pygame
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
        self.draw_image_center(self.pusher_1, screen)

    def handle_input(self, event):
        dx = 0
        dy = 0

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            # elif event.key == pygame.K_LEFT:
            #     self.dest.x = self.box.x
            #     self.dest.y = self.box.y

                # if self.dest.x <= -11:
            #         self.dest.x = self.box.x
            #         self.dest.y = self.box.y
            #     else:
            #         self.dest.move(-1, 0)
                # sokoban.dest.move(-1, 0)
        if self.in_map(self.box, dx, dy):
            self.box.move(dx, dy)
            self.dest.move(dx, dy)

    def in_map(self,object, dx, dy):
        if 0 <= object.x + dx < self.map.width and 0 <= object.y + dy < self.map.height:
            return True
        else:
            return False

class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h

class Pusher:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        # self.current_img = 0
        # self.counter = 0
        # self.time = 100
        # self.active = True
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def collide(self, object, dx, dy):
        if self.x + dx == object.x and self.y + dy == object.y:
            return True
        else:
            return False

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Dest:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

sokoban = Game()
sokoban.map = Map(10, 10)
sokoban.pusher = Pusher(1, 1)
sokoban.pusher_1 = Pusher(2, 1)
sokoban.box = Box(9, 5)
sokoban.dest = Dest(9,5)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done= False
box_image = pygame.image.load("image/box.png")
pusher_image = pygame.image.load("image/pusher.png")
pusher_1_image = pygame.image.load("image/pusher.png")
ground_image = pygame.image.load("image/ground.png")
dest_image = pygame.image.load("image/dest.png")
pixel = 64
sokoban.box.image = box_image
sokoban.pusher.image = pusher_image
sokoban.pusher_1.image = pusher_1_image
sokoban.dest.image = dest_image
x = random.randint(255 , 640)

while not done:
    dx = 0
    dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # if event.type == pygame.KEYDOWN:
        #
        #     if event.key == pygame.K_LEFT:

        # elif event.key == pygame.K_LEFT:
        #
            # sokoban.dest.move(1, 0)
        sokoban.handle_input(event)
    if sokoban.pusher.y > 11:
        sokoban.pusher.y = 0
        sokoban.pusher.x = random.randint(0, 8)
        sokoban.pusher_1.y = 0
        sokoban.pusher_1.x = random.randint(0,8)

    # sokoban.dest.move(-1/10, 0)

        sokoban.dest.x = sokoban.box.x
        sokoban.dest.y = sokoban.box.y


    if sokoban.dest.x < -1:
        sokoban.dest.x = sokoban.box.x


    sokoban.dest.move(-0.5 ,0)
    sokoban.pusher.move(0, 0.03)
    sokoban.pusher_1.move(0, 0.02)
    sokoban.draw()
    pygame.display.flip()


