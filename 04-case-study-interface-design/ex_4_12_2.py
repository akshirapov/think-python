"""
This module contains a code for Exercise 2 related to ch.4.12 of

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import turtle


"""
General Plan:
1. Draw n-cross
2. Draw arcs 
"""


def flower(t, n, r):
    """
    Draw flower
    """
    # Draw cross
    angle = 360 / n
    for i in range(n):
        t.fd(r)
        t.bk(r)
        t.lt(angle)


if __name__ == '__main__':
    bob = turtle.Turtle()
    flower(bob, 7, 100)

    turtle.mainloop()
