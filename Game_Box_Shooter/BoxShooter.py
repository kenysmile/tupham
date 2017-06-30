import pygame
import time
def main():
    pygame.init()
#   design physical surface size, in pixels
#     surface_sz = 640

#   create surface of(width, height)
    main_surface = pygame.display.set_mode((640, 640))
#   Set up some data to describe a small retangle and it color
    small_rect = (300, 200, 40, 30)
    some_color = (255, 0, 0)
    ball = pygame.image.load("images/ball.png")
    my_font = pygame.font.SysFont('Courier', 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()
    while True:
        ev=pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500/ (t1- t0)
            t0 = t1


        main_surface.fill((0, 200, 255))
        main_surface.fill(some_color, small_rect)
        main_surface.blit(ball, (100, 200))
        the_text = my_font.render('Hello World', True, (0, 0, 0))
        the_text = my_font.render("Frame = {0}, Rate = {1:2f} fps".format(frame_count, frame_rate), True, (0, 0, 0))
        main_surface.blit(the_text,(10, 10))

        pygame.display.flip()
    pygame.quit()
main()


















# import pygame
# class QueenSprite:
#     def __init__(self, img, target_posn):
#         self.imgae = img
#         self.target_posn = target_posn
#         self.posn = target_posn
#
#     def update(self):
#         return
#
#     def draw(self, target_surface):
#         target_surface.blit(self.image, self.posn)
#
#     # Keep a list of all sprites in the game
#     all_sprites = []
#
#     for(col, row) in enumerate(the_board):
#         a_queen = QueenSprite(ball, col * sq + ball_offset, row * sp + ball_offset))
#         all_sprites.append(a_queen)
#
# gravity = 0,0001
#
# class QueenSprite:
#     def __init__(self, img, target_posn):
#         self.img = img
#         self.target_posn = target_posn
#         (x, y) = target_posn
#         self.posn = (x, 0)
#         self.y_velcocity = 0
#     def update(self):
#         self.y_velcocity += gravity
#         (x, y) = self.posn
#         new_y_pos = y + self.y_velcocity
#         self.posn = (x, new_y_pos)
#
#     def draw(self, target_surface):
#         target_surface.blit(self.image, self.posn)
#
#
# while True:
#     ev = pygame.event.poll()
#     if ev.type == pygame.QUIT:
#         break;
#
#     for sprite in all_sprites:
#         sprite.update()
#     for sprite in all_sprites:
#         sprite.draw(surface)
#     pygame.display.flip()
#
#
