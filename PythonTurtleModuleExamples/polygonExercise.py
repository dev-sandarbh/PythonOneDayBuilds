import turtle
import random

turtle.setup(800,600)
wn = turtle.Screen()
wn.title("Pentagon")
wn.colormode(255)

# let's make a function which takes two arguments one no of sides in polygon and second length of sides of the polygon; but remember that this function will draw a regular polygon

def regularPolygon(side,length):
    ''' this function draws a regular polygon of n sides and a fixed length'''
    total = (side-2)*180
    one_angle = 180 - (total/side)
    bob = turtle.Turtle()
    bob.shape("turtle")
    # bob.shapesize(2,2,5)
    bob.pensize(10)
    bob.pencolor("orange")
    bob.penup()
    bob.setpos(random.randint(-100,100),random.randint(-100,100))
    bob.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    bob.begin_fill()
    for i in range(side):
        bob.pendown()
        bob.fd(length)
        bob.left(one_angle)
    bob.end_fill()

regularPolygon(10,50)

# def drawOctagon():
# ''' this function draws a octagon'''
#     n=8
#     total = (n-2)*180
#     one_angle = 180 - (total/n)
#     bob = turtle.Turtle()
#     bob.shape("turtle")
#     # bob.shapesize(2,2,5)
#     bob.pensize(2)
#     bob.pencolor("orange")
#     bob.penup()
#     bob.setpos(random.randint(0,100),random.randint(0,100))
#     bob.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     bob.begin_fill()
#     for i in range(n):
#         bob.pendown()
#         bob.fd(75)
#         bob.left(one_angle)
#     bob.end_fill()

# def drawPentagon():
# ''' this function draws a pentagon'''
#     n=5
#     total = (n-2)*180
#     one_angle = 180 - (total/n)
#     bob = turtle.Turtle()
#     bob.shape("turtle")
#     # bob.shapesize(2,2,5)
#     bob.pensize(2)
#     bob.pencolor("orange")
#     bob.penup()
#     bob.setpos(random.randint(0,100),random.randint(0,100))
#     bob.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     bob.begin_fill()
#     for i in range(n):
#         bob.pendown()
#         bob.fd(50)
#         bob.left(one_angle)
#     bob.end_fill()

# drawPentagon()
# drawOctagon()
turtle.done()