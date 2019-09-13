# -*- coding: utf-8 -*-

"""
This module contains a code for ex.7 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def has_duplicates(seq: list):
    """Checks if sequence has duplicates."""

    for i in seq:
        if seq.count(i) > 1:
            return True

    return False


if __name__ == '__main__':
    t = [1, 2, 3, 3]
    print(has_duplicates(t))
