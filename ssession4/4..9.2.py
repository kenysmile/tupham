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
l=20  
for i in range(5):
        draw_square(l,4)
        t.penup()
        t.right(135)
        t.forward(15)
        t.left(135)
        t.pendown()

        l+=20
        
       
