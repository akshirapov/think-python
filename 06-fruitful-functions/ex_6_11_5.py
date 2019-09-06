# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.6.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def gcd(a, b):
    """Returns the greatest common divisor of a and b."""

    if b == 0:
        return a

    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(8, 12))
    print(gcd(50, 12))
