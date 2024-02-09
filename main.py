import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.penup()
tim.goto(-350, -310)

for column in range(10):
    for row in range (9):
        tim.dot(20, random_color())
        tim.forward(70)
    tim.dot(20, random_color())
    tim.setheading(90)
    tim.forward(70)
    if column % 2 == 0:
        tim.setheading(180)
    else:
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()