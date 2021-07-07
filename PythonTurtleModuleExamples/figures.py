import turtle
from turtle import *
from random import *

# creating a window to draw various shapes on
wn = turtle.Screen()
wn.title("Figures with turtle")
wn.colormode(255)

bob = Turtle()
bob.shape('turtle')
bob.pensize(2)
# let's draw a basic equilateral triangle
# bob.begin_fill()
# for i in range(1,4):
#     bob.forward(100)
#     bob.left(120)
# bob.end_fill()

# let's draw some equilateral triangles at some random positions
# for triangles in range(1,16):       #say we want to get 15 triangles on the screen 
#     set_x = randint(-250,250)
#     set_y = randint(-250,250)
#     bob.penup()
#     bob.setpos(set_x,set_y)
#     for i in range(1,4):
#         bob.pendown()
#         bob.pencolor(randint(0,255),randint(0,255),randint(0,255))
#         bob.fillcolor(randint(0,255),randint(0,255),randint(0,255))
#         bob.begin_fill()
#         bob.forward(50)
#         bob.left(120)
#         bob.end_fill()
#         bob.penup()


# let's draw a isosceles triangle
# bob.forward(100)
# bob.left(140)
# bob.forward(100)
# bob.left(80)
# bob.forward(100)
# bob.home()

# let's draw a basic circle
# bob.pencolor(randint(0,255),randint(0,255),randint(0,255))
# bob.fillcolor(randint(0,255),randint(0,255),randint(0,255))
# bob.begin_fill()
# bob.circle(100)
# bob.end_fill()

# this extra three lines places the turtle at the centre of the cirlce after gets completed
# bob.penup()
# bob.setpos(0,100)
# bob.fillcolor(randint(0,255),randint(0,255),randint(0,255))

# let's draw a circle-by-circle
# for angle in range(0,360,15):
#     bob.seth(angle)
#     bob.pencolor(randint(0,255),randint(0,255),randint(0,255))
#     # bob.fillcolor(randint(0,255),randint(0,255),randint(0,255))
#     # bob.begin_fill()
#     bob.circle(100)
#     # bob.end_fill()

turtle.done()