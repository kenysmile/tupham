import turtle
wn=turtle.Screen()
turtle.bgcolor("lightgreen")
t=turtle.Turtle()
t.pensize(4)
def draw_square(l,s):

    t.color("violet")
    for i in range(s):
        t.forward(l)
        t.left(360/s)
        
for i in range(5):
        draw_square(20,4)
        t.penup()
        t.forward(20*2)
        t.pendown()
