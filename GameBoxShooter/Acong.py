import pygame
import random
import time
import copy
import datetime
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# classes

class Balloon(pygame.sprite.Sprite):
    """ this class represents the baloons """

    def __init__(self):
        # Call the parent class (Sprite) constructor  (not get it??)
        super().__init__()

        self.image = pygame.Surface([40, 30])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
    def update(self):
        """ Release the balloons"""
        self.rect.y += speed

class Shooter(pygame.sprite.Sprite):
    """this class represents the player """

    def __init__(self):
        """set up the player on creation"""
        # Call the parent class (Sprite) constructor   ???? for what????
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 10

class Bullet(pygame.sprite.Sprite):
    """This class represents the bullets """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([10, 4])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x -= 6

# --- Create the window

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode([screen_width, screen_height])
myfont = pygame.font.SysFont("monospace", 16)
youlose = pygame.font.SysFont("monospace", 50)

# --- Sprite lists

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()

# List of each balloons in the game
balloon_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites



# Create a red shooter
shooter = Shooter()
all_sprites_list.add(shooter)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
sound = pygame.mixer.Sound("sound/bullet2.wav")
life = 10
score = 0
ammo = 30
time_to_reload = 1000
reloading = False
lastReloadTime = time.clock()
times = 0

if datetime.date.today().month == 12 and datetime.date.today().day == 25:
    pygame.mixer.music.load("sound/sound2.wav")
    print("Merry Christmas!")
else:
    pygame.mixer.music.load("sound/sound2.wav")
print("Loading Music...")
pygame.mixer.music.play(-1, 0.0)
print("Playing Background Music...")
# -------- Main Program Loop -----------



while not done:
    # --- Event Processing

    times += 1
    # speed = times % 2
    level = times // 1800 + 1
    speed = (level - 1) + times % 2

    if times % 150 == 0:
        # This represents baloons:
        for i in range(2):
            balloon = Balloon()


            # Set a random location for the balloon
            balloon.rect.x = random.randrange(400)
            balloon.rect.y = 10

            # Add the balloon to the list of objects
            balloon_list.add(balloon)
            all_sprites_list.add(balloon)



    # make shooter move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        shooter.rect.y -= 5
    elif keys[pygame.K_DOWN]:
        shooter.rect.y += 5

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # shoot the bullets
            if event.key == pygame.K_SPACE and not reloading and ammo > 0 :
                ammo -= 1
                bullet = Bullet()
                bullet.rect.x = shooter.rect.x
                bullet.rect.y = shooter.rect.y + pygame.Surface.get_size(shooter.image)[1]/2
                sound.play()
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

            elif event.key == pygame.K_SPACE:
                lastReloadTime = time.clock()
                reloading = True
        # pygame.event.pump()
    if reloading and time.clock() - lastReloadTime > 1:  # 1000
        reloading = False
        ammo = 30
        print(time.clock() - lastReloadTime)
    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a balloon
        balloon_hit_list = pygame.sprite.spritecollide(bullet, balloon_list, True)

        # For each balloon hit, remove the bullet and add to the score

        for balloon in balloon_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            if life > 0:
                score += 1


        # Remove the bullet if it flies up off the screen
        if bullet.rect.x < 0:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # calculate the number of lives left:

    for balloon in balloon_list: # logic: a balloon must be removed after being added to balloon_out_list
        balloon_out_list = pygame.sprite.Group()
        if balloon.rect.y >= screen_height:
            balloon_out_list.add(balloon)
            balloon_list.remove(balloon)
            all_sprites_list.remove(balloon)
            life -= 1


    # --- Draw a frame

    # Clear the screen
    screen.fill(WHITE)
    # Draw all the spites & check lose
    all_sprites_list.draw(screen)
    scoretext = myfont.render("Life = " + str(life) + " /Score = " + str(score) +" /Ammo =" + str(ammo) + " /Level = " + str(level), 1, (0, 0, 0))

    screen.blit(scoretext, (5, 10))

    if life <= 0:
        screen.fill(WHITE)
        losetext = youlose.render("You Lose", 1, (0, 0, 0))
        finalscore = youlose.render("Your Score Is: " + str(score), 1, (0, 0, 0))
        screen.blit(losetext, (100, 100))
        screen.blit (finalscore, (100, 250))



    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)

pygame.quit()