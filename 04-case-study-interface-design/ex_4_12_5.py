"""This module contains a code for ex.5 related to ch.4.12.

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import turtle


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


if __name__ == '__main__':
    bob = turtle.Turtle()

    arch_spiral(bob, 200)

    bob.hideturtle()
    turtle.mainloop()
