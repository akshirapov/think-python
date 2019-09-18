# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def invert_dict(d):
    """Inverts dictionary.

    Each value will become a list of letters.
    """

    r = dict()
    for key in d:
        val = d[key]
        r.setdefault(val, []).append(key)
    return r


if __name__ == '__main__':
    f = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(f)

    for i in invert_dict(f):
        keys = inverse[i]
        print(f'{i}: {keys}')
