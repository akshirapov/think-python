# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def has_duplicates(seq: list):
    """Checks if sequence has duplicates."""
    d = {}
    for i in seq:
        if i in d:
            return True
        d[i] = None

    return False


if __name__ == '__main__':
    t = [1, 2, 3, 3]
    print(has_duplicates(t))
