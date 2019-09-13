# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def middle(numbers: list):
    """Returns list without first and last elements."""

    if len(numbers) <= 2:
        return []

    return numbers[1:-1]


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(middle(t))
