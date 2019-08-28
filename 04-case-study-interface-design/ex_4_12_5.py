"""This module contains a code for ex.5 related to ch.4.12.

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import math
import time
import turtle


def polyline(t, n, length, angle):
    """Draws n line segments.

    :param t: Turtle object
    :param n: number of line segments
    :param length: length of each segments
    :param angle: degrees between segments
    """

    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle

    :param t: Turtle object
    :param r: radius of the arc
    :param angle: angle subtended by the arc, in degrees
    """

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)


def arch_spiral(t, n, length=4):
    """Draws an Archimedian spiral.

    :param t: Turtle object
    :param n: number of line segments
    :param length: length of each segment

    https://en.wikipedia.org/wiki/Archimedean_spiral
    """

    a = 0.01  # how loose the initial spiral starts out (larger is looser)
    b = 0.0002  # how loosly coiled the spiral is (larger is looser)
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


def fib_spiral(t, n):
    """Draws a Fibonacсi spiral.

    :param t: Turtle object
    :param n: length of sequence
    """

    a, b = 0, 1

    for i in range(n):
        arc(t, a, 90)
        a, b = b, a+b


if __name__ == '__main__':
    bob = turtle.Turtle()

    # arch_spiral(bob, 200)
    fib_spiral(bob, 15)

    bob.hideturtle()
    turtle.mainloop()
