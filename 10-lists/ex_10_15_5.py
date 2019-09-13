# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_sorted(sequence: list):
    """Checks a sequence if it is ordered in ascending order."""
    return sequence == sorted(sequence)


if __name__ == '__main__':
    t = [1, 2, 2]
    print(is_sorted(t))
    t = ['b', 'a']
    print(is_sorted(t))
