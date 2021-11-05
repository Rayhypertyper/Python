import turtle
from random import randint
 


# Set the background color
screen = turtle.Screen() 
screen.bgcolor('white')   # black


# Create a turle
t = turtle.Turtle()
t.width(1)
t.color('red')
#t.speed(100)

side_length = 100
t.penup()
t.goto(-375,300)
t.pendown()
t.goto(-382,300)
def draw_square():
    for i in range (4): 
        t.fd(side_length)
        t.rt(90) 
draw_square() 
for i in range 5
t.fd(side_length)   # Forward: pixels
t.rt(90)            # Right Turn: degree
t.fd(side_length)   # Forward: pixels
t.rt(90)            # Right Turn: degree
# t.fd(side_length)   # Forward: pixels
# t.rt(90)            # Right Turn: degree
# t.fd(side_length)   # Forward: pixels
# t.rt(90)            # Right Turn: degree
# 
turtle.done()

