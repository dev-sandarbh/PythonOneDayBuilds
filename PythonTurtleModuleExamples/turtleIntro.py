import turtle

step = 5

#creating an object of turtle class
demo = turtle.Turtle()
# defining the color - it accepts common color names, rgb values and hex values
# first arg in color func is boundary color and second arg is fill color

# demo.color("red","cyan")
# demo.begin_fill()
# for i in range(0,49):
#     demo.forward(step)
#     demo.left(90)
#     demo.forward(step)
#     demo.left(90)
#     step+=1
#     demo.forward(step)
#     demo.left(90)
#     step+=1
#     demo.forward(step)
# demo.end_fill()

demo.color("red","cyan")
demo.begin_fill() 

print(demo.pos())
# creating a basic square 
for i in range(0,4):
    demo.forward(100)
    demo.left(90)
demo.end_fill()
print(demo.pos())
# commands to move our turtle to a new loaction
demo.penup()
demo.pensize(5)
demo.right(90)
demo.pencolor("grey")
demo.forward(10)
demo.pendown()

print(demo.pos())
# creating another square just below it
demo.begin_fill() 
for i in range(0,4):
    demo.forward(100)
    demo.left(90)
demo.end_fill()
print(demo.pos())

turtle.done()
