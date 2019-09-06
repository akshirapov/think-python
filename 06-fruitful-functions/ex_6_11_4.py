# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.6.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_power(a, b):
    """Checks if a is a power of b."""

    if a == 0 or a == 1:
        return True

    if a % b != 0:
        return False

    return is_power(a/b, b)


if __name__ == '__main__':
    print(is_power(8, 2))
    print(is_power(25, 2))
    print(is_power(81, 3))
