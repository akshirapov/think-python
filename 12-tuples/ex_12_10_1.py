# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.12.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def count_letters(s):
    """Counts the number of letters in a string.

    :param s: String.
    :return: Dictionary with letter-number pairs.
    """

    d = {}
    for x in s:
        d[x] = d.get(x, 0) + 1
    return d


def most_frequent(s):
    """Sorts the letters in a string in decreasing order of frequency.

    :param s: String
    :return: Ordered list
    """

    h = count_letters(s)
    t = []
    for letter, frequency in h.items():
        t.append((frequency, letter))

    r = []
    for f, c in sorted(t):
        r.append(c)

    return r


if __name__ == '__main__':
    with open('romeo_and_juliet.txt') as fin:
        text = fin.read()
    seq = most_frequent(text)
    for i in seq:
        print(i)
