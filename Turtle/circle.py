import turtle


screen = turtle.Screen()
screen.bgcolor('white')
t = turtle.Turtle()
t.width(2)
t.color('red')
t.shape('turtle')
t.speed(100)
for x in range(100):
    t.circle(100)
    t.right(11)
turtle.done() 