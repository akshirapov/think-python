# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def cumsum(numbers: list):
    """Returns list where the ith element is the sum of the first i+1."""

    result = []

    for i in range(0, len(numbers)):
        result.append(sum(numbers[:i+1]))

    return result


if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))
