import pygame
import random

WIDTH = 640
HEIGHT = 640
FPS = 60

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#  initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kenysmile")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH
        self.rect.bottom = HEIGHT / 2
        self.speedy = 0
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    def shoot(self):
        bullet = Bullet(self.rect.bottom, self.rect.centerx)
        bullet.rect.x = player.rect.x
        bullet.rect.y = player.rect.y + pygame.Surface.get_size(player.image)[1]/2.5
        all_sprites.add(bullet)
        bullets.add(bullet)

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(400)
        self.rect.y = random.randrange(10)
        self.speedy = random.randrange(1, 4)
        # self.speedx = random.randrange(1, 4)

    def update(self):
        # self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(400)
            self.rect.y = random.randrange(10)

            self.speedy = random.randrange(1, 4)
        # self.rect.x += self.speedx

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 4))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.rect.bottom  = x
        self.rect.centerx = y

        self.speedx = -10
    def update(self):
        self.rect.x += self.speedx
#         kill it if moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
balloons = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(4):
    b = Balloon()
    all_sprites.add(b)
    balloons.add(b)
done = False

while not done:
    # Keep loop running at the right speed
    clock.tick(FPS)
    for event in pygame.event.get():
    #     check for closing window
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    # Update
    all_sprites.update()

    # check to see it a bullet hit a ballon
    hits = pygame.sprite.groupcollide(balloons, bullets, True, True)
    for hit in hits:
        m = Balloon()
        all_sprites.add(m)
        balloons.add(m)

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

