"""This module contains a code for ex.3 related to ch.4.12.

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import math
import turtle


def forward_and_left(t, distance, angle):
    """Move forward by the distance and turn left by angle.

    :param t: Turtle object
    :param distance: number
    :param angle: degrees
    """

    t.fd(distance)
    t.lt(angle)


def isosceles_triangle(t, a, alpha):
    """Draws isosceles triangle.

    :param t: Turtle object
    :param a: length of two equal sides
    :param alpha: angle between equal sides in degrees
    """

    # base corners
    beta = (180-alpha) / 2

    # base side by the cosine theorem
    b = abs(2 * a * math.cos(math.radians(beta)))

    forward_and_left(t, a, 180-beta)
    forward_and_left(t, b, 180-beta)
    forward_and_left(t, a, 180-alpha)


def polygon(t, n, r):
    """Draws pie with n segments.

    :param t: Turtle object
    :param n: number of segments
    :param r: radius of polygon
    """

    angle = 360 / n
    for i in range(n):
        isosceles_triangle(t, r, angle)
        t.lt(angle)


if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.hideturtle()

    polygon(bob, 7, 100)

    turtle.Screen().mainloop()
