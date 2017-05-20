from turtle import *
pensize(2)

def draw_star(x, y, length):
    penup()
    goto(x,y)
    pendown()

    for i in range(5):
        fd(50)
        right(144)
            
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
##from random import randrange, uniform
##
## randrange gives you an integral value
##irand = randrange(0, 10)
