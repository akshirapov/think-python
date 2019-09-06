
"""
This module contains a code for Exercise 1 related to ch.4.12 of

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import math
import turtle


def polyline(t, n, length, angle):
    """
    Draws n line segments.

    :param t: Turtle object
    :param n: number of line segments
    :param length: length of each segments
    :param angle: degrees between segments
    """

    # stack diagram
    print(f'[polyline]: t->{t}, n->{n}, length->{length}, angle->{angle}')

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def square(t, length):
    """
    Draws a square with sides of the given length
    Returns the Turtle to the starting position and location.

    :param t: Turtle object
    :param length: length of each side
    """

    polyline(t, 4, length, 90)


def polygon(t, n, length):
    """
    Draws a polygon with n sides

    :param t: Turtle object
    :param length: length of each side
    :param n: number of sides
    """

    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """
    Draws an arc with the given radius and angle

    :param t: Turtle object
    :param r: radius of the arc
    :param angle: angle subtended by the arc, in degrees
    """

    # stack diagram
    print(f'[arc]: t->{t}, r->{r}, angle->{angle}')

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """
    Draws a circle with the given radius

    :param t: Turtle object
    :param r: radius of the circle
    """

    # stack diagram
    print(f'[circle]: t->{t}, r->{r}')

    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()

    # square(bob, 100)
    # polygon(bob, 10, 100)
    # arc(bob, 100, 30)
    circle(bob, 100)

    # wait for the user to close the window
    turtle.mainloop()
