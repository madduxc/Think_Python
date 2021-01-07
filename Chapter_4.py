#Author: Charles D. Maddux
#Date: 12/25/2020
#Description: Think Python Chapter 4 exercises

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

def square(t, length=100):
    """
    draws a square
    :param t:
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)
        i += 1

def polygon(jojo, length=100, sides=4):
    """
    draws a polygon
    """
    angle = 360/sides
    polyline(jojo, sides, length, angle)

def circle(t, radius=100):
    """
    draws a circle
    """
    circumf = radius * 2 * math.pi
    if radius < 100:
        sides = int(radius)
    elif radius <1000:
        sides = int(radius/5)
    else:
        radius = int(radius/10)
    length = circumf/sides
    angle = 360/sides
    polyline(t, sides, length, angle)

def xy_plot(axis, t):
    """
    draws am xy plot
    :param t:
    """
    #draw axis
    axis.pu()
    axis.lt(90)
    axis.fd(100)
    axis.rt(180)
    axis.pd()
    axis.fd(100)
    axis.lt(90)
    axis.fd(100)
    #wip - set up method to draw plot
    for i in range(4):
        t.fd(50)
        t.lt(90)
        i += 1


def main():
    """
    sends parameters to functions to answer main questions in exercises
    :return:
    """
    dist = 150
    sides = 5
    radius = 200
    bobo = turtle.Turtle()
    mojo = turtle.Turtle()
    angle = 60
#    square(bobo, dist)
#    polygon(bobo, dist, sides)
#    circle(mojo, radius)
    mojo.lt(90 + angle/ 2)
    petals = 10
    for i in range(petals):
        arc(mojo, radius, angle)
        mojo.lt(180 - angle)
        arc(mojo, radius, angle)
        mojo.rt(180 + 360/ petals + angle)

#    arc(mojo, radius/2)
#    arc(mojo, radius / 2, 60, "right")
#    arc(mojo, radius * 2)
#    xy_plot(bobo, mojo)
    turtle.mainloop()

main()