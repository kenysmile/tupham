
from turtle import *

def draw_square(length,color):
    
    pencolor(color)
    for i in range(4):   
        fd(length)
        left(90)
                    

draw_square(100, "blue")


