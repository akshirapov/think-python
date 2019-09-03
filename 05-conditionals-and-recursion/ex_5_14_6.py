# -*- coding: utf-8 -*-

"""
This module contains a code for ex.6 related to ch.5.14 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import math
import turtle


def koch(t, x):
    """Draws a Koch curve with the given length.

    :param t: Turtle object
    :param x: Length of the curve
    """

    if x < 10:
        t.fd(x)
        return

    angle = 60
    d = x/3

    koch(t, d)

    t.lt(angle)
    koch(t, d)

    t.rt(2*angle)
    koch(t, d)

    t.lt(angle)
    koch(t, d)


def quadratic_koch(t, x, n):
    """Draws a nested quadratic Koch curve with the given length.

    :param t: Turtle object
    :param x: Length of the curve
    :param n: Nesting level
    """

    if x < 4:
        t.fd(x)
        return

    angle = 90
    d = x/4

    if n == 0:
        t.fd(d)

        t.lt(angle)
        t.fd(d)

        t.rt(angle)
        t.fd(d)

        t.rt(angle)
        t.fd(d)

        t.lt(angle)
        t.fd(d)
    else:
        quadratic_koch(t, d, n-1)

        t.lt(angle)
        quadratic_koch(t, d, n-1)

        t.rt(angle)
        quadratic_koch(t, d, n-1)

        t.rt(angle)
        quadratic_koch(t, d, n-1)

        t.lt(angle)
        quadratic_koch(t, d, n-1)


def snowflake(t, x):
    """Draws a snowflake by a Koch curve.

    :param t: Turtle object
    :param x: Length of side
    """

    angle = 60
    for i in range(3):
        koch(t, x)
        t.rt(2*angle)


if __name__ == '__main__':

    LENGTH = 300

    bob = turtle.Turtle()

    # move pen to the upper left corner of "triangle"
    ox = -LENGTH / 2
    oy = LENGTH * math.sqrt(3) / 4

    bob.pu()
    bob.goto(ox, oy)
    bob.pd()

    snowflake(bob, LENGTH)
    # quadratic_koch(bob, 4*LENGTH, 3)

    bob.hideturtle()
    turtle.mainloop()
