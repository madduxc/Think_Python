#Author: Charles D. Maddux
#Date: 12/26/2020
#Description: Think Python Chapter 4 alphabet exercise

import math
import turtle

def polyline(mojo, sides=4, length=100, angle=90, dir="left"):
    """
    Draws the segments of the shape defined in subsequent functions
    """
    if dir == "left":
        for i in range(sides):
            mojo.fd(length)
            mojo.lt(angle)
    else:
        for i in range(sides):
            mojo.fd(length)
            mojo.rt(angle)

def arc(bobo, radius=100, angle=90, direction="left"):
    arc_length = 2 * math.pi * radius * angle/360
    n = int(arc_length/ 3) + 1
    step_length = arc_length/ n
    step_angle = float(angle)/ n
    polyline(bobo, n, step_length, step_angle, direction)

def draw_a(turtle, size):
    """
    draw the letter 'a'.  Takes a turtle and size (int or float) as input
    :return:
    """
    turtle.lt(90)
#    arc(turtle, size/2, 60, "right")
    turtle.fd(size* 0.45)
    arc(turtle, size* 0.45, 180)
    turtle.fd(size* 0.10)
    arc(turtle, size* 0.45, 180)

def draw_b(turtle, size):
    """
    draw the letter 'b'.  Takes a turtle and size (int or float) as input
    :return:
    """
    turtle.lt(90)
    turtle.pu()
    turtle.fd(size* 2)
    turtle.rt(180)
    turtle.pd()
    turtle.fd(size)
    turtle.rt(90)
    draw_a(turtle, size)

# to be continued ...

def main():
    """
    sends parameters to functions to answer main questions in exercises
    :return:
    """
    bobo = turtle.Turtle()
    mojo = turtle.Turtle()

    size = 100
    draw_a(bobo, size)
    turtle.mainloop()

main()