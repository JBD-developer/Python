###############################
# TITLE : Turple
# CREATE DATE : 2022-02-15
# CREATOR : J
# MODIFIER : J
# MODIFY DATE :
# VERSION : 1.0.0
###############################
import turtle
import random


def screenLeft_click(x, y):
    global r, g, b
    turtle.pencolor(r, g, b)
    turtle.pendown()
    turtle.goto(x, y)


def screenRight_click(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screenMid_click(X, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


myT = turtle.Turtle()
pSize = 10
r, g, b = 0.0, 0.0, 0.0
turtle.title("turtle")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeft_click, 1)
turtle.onscreenclick(screenMid_click, 2)
turtle.onscreenclick(screenRight_click, 3)

turtle.done()