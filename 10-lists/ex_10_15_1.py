# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def nested_sum(numbers):
    """Adds up the elements from the nested lists."""

    if numbers is None:
        numbers = []

    total = 0
    for n in numbers:
        if isinstance(n, list):
            total += sum(n)

    return total


if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))
