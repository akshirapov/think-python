# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def chop(numbers: list):
    """Returns list without first and last elements."""
    del numbers[0]
    del numbers[-1]


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    chop(t)
    print(t)
