# -*- coding: utf-8 -*-

"""
This module contains a code for ex.6 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_anagrams(first: str, second: str):
    """Checks if first and second strings are anagrams."""
    return list(first).sort() == list(second).sort()


if __name__ == '__main__':
    print(is_anagrams('cat', 'act'))
