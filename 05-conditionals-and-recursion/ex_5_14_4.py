# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.5.14 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def recurse(n, s):
    """Adds s to the sum of numbers from 0 to n.

    :param n: Integer
    :param s: Integer
    """
    if n == 0:
        print(f'[recurse]: n->{n}, s->{s}')
        print(s)
    else:
        recurse(n-1, n+s)


if __name__ == '__main__':
    recurse(3, 0)
