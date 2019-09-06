# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.7.9 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import math


def mysqrt(a):
    """Returns an estimate of the square root of a."""

    x = 1
    epsilon = 0.0000001

    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y

    return x


def test_square_root():
    """Prints a table."""

    f1 = '{:<2}'
    f2 = '{:<18}'

    print(f1.format('a'), f2.format('mysqrt(a)'),
          f2.format('math.sqrt(a)'), f2.format('diff'))

    print(f1.format('-'), f2.format('-'*9),
          f2.format('-'*12), f2.format('-'*4))

    for i in range(1, 10):
        x1 = mysqrt(i)
        x2 = math.sqrt(i)
        print(f1.format(float(i)), f2.format(x1),
              f2.format(x2), f2.format(abs(x1-x2)))


if __name__ == '__main__':
    test_square_root()
