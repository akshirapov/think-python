# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.5.14 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import turtle


def draw(t, length, n):
    """Draws tree structure with two branches.

    :param t: Turtle object
    :param length: Length of branch
    :param n: Nesting
    """

    if n == 0:
        return

    angle = 45

    t.fd(length*n)
    t.lt(angle)

    # first branch
    draw(t, length, n-1)

    t.rt(2*angle)

    # second branch
    draw(t, length, n-1)

    t.lt(angle)
    t.bk(length*n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.lt(90)  # for clarity
    draw(bob, 20, 5)
    turtle.Screen().mainloop()
