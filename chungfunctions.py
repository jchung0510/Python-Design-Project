#chungfunctions

import turtle
bob=turtle.Turtle()
alice=turtle.Turtle()


def polygon(sides,distance,color):
    bob.color(color)
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance):
    for times in range(5):
        bob.forward(distance)
        bob.right(144)

def explosion(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.right(135)
    bob.end_fill()

def portal():
    for times in range(60):
        c = (times*4,times*4,times*4)
        polygon(3,125-times*2,c)
        bob.right(100)

def circle():
    for times in range(100):
        bob.circle(10)





