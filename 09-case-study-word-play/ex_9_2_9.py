# -*- coding: utf-8 -*-

"""
This module contains a code for ex.9 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def are_reversed(first: str, second: str):
    """Checks if the first and second strings are the reverse of each other.

    :rtype: bool
    """
    return first.zfill(2) == second.zfill(2)[::-1]


def count_matches(diff: int, display=False):
    """Counts the number of palindromic ages.

    :param diff: Difference in ages
    :param display: (optional) Print pairs
    :return Number
    :rtype: int
    """

    count = 0

    child = 0
    while True:
        parent = child + diff
        if are_reversed(str(parent), str(child)):
            count += 1
            if display:
                print(f'{parent}, {child}')
        if parent > 120:
            break
        child += 1

    return count


if __name__ == '__main__':
    for i in range(10, 70):
        if count_matches(i) >= 8:
            count_matches(i, True)
            break
