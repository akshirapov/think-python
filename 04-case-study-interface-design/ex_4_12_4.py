"""This module contains a code for ex.4 related to ch.4.12.

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import math
import turtle


def lt_fd(t, angle, length):
    """Turn left by angle and move forward by the length.

    :param t: Turtle object
    :param angle: angle in degrees
    :param length: distance to move
    """

    t.lt(angle)
    t.fd(length)


def rt_fd(t, angle, length):
    """Turn right by angle and move forward by the length.

    :param t: Turtle object
    :param angle: angle in degrees
    :param length: distance to move
    """

    t.rt(angle)
    t.fd(length)


def draw_a(t, size):
    """Draw letter "A"

    :param t: Turtle object
    :param size: size of the letter
    """

    # right triangle
    angle = math.degrees(math.atan2(size, size/2))
    length = math.sqrt(size**2 + (size/2)**2)

    lt_fd(t, angle, length)
    rt_fd(t, 2*angle, length)

    t.pu()
    lt_fd(t, 90+angle, size/2)
    t.pd()

    lt_fd(t, 90, size)


if __name__ == '__main__':
    bob = turtle.Turtle()

    draw_a(bob, 20)

    bob.hideturtle()
    turtle.mainloop()
