# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.15.9 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import math
import turtle

from ex_15_9_1 import Point, Circle, Rectangle


def polyline(t, n, length, angle):
    """Draws n line segments.

    :param t: turtle object
    :param n: number of line segments
    :param length: length of each segments
    :param angle: degrees between segments
    """

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    :param t: turtle object
    :param r: radius of the arc
    :param angle: angle subtended by the arc, in degrees
    """

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)


def draw_rect(t: turtle.Turtle, rect: Rectangle):
    """Draws  the rectangle.

    :param t: turtle object
    :param rect: rectangle object
    """

    w = rect.width
    h = rect.height

    t.ht()

    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.rt(90)
    t.fd(h)


def draw_circle(t: turtle.Turtle, circle: Circle):
    """Draws  the circle.

    :param t: turtle object
    :param circle: circle object
    """

    t.ht()
    arc(t, circle.radius, 360)


def main():
    bob = turtle.Turtle()

    box = Rectangle()
    box.width = 100
    box.height = 50
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0

    circle = Circle()
    circle.radius = 50
    circle.center = Point()
    circle.center.x = 0
    circle.center.y = 0

    draw_rect(bob, box)
    draw_circle(bob, circle)

    turtle.mainloop()


if __name__ == '__main__':
    main()
