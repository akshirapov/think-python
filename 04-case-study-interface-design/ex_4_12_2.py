"""
This module contains a code for Exercise 2 related to ch.4.12 of

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
    print(f"polyline: [t -> '{t}'; n -> '{n}'; length -> '{length}'; angle -> '{angle}']")

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """
    Draws an arc with the given radius and angle

    :param t: Turtle object
    :param r: radius of the arc
    :param angle: angle subtended by the arc, in degrees
    """

    # stack diagram
    print(f"arc: [t -> '{t}'; r -> '{r}'; angle -> '{angle}']")

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)


def petal(t, r, angle):
    """
    Draw petal with length r

    :param t: Turtle object
    :param r: length of the petal
    :param angle: "width" of the petal
    """

    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r):
    """
    Draw a flower with n petals

    :param t: Turtle object
    :param n: number of petals
    :param r: radius of the flower
    """

    angle = 360 / n
    for i in range(n):
        petal(t, r, angle)
        t.lt(angle)


if __name__ == '__main__':
    bob = turtle.Turtle()
    flower(bob, 10, 100)

    turtle.mainloop()
