# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.8.13 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def rotate_word(word, n):
    """Rotates each letter by a fixed number of places.

    It is the implementation of the Caesar cypher.
    https://en.wikipedia.org/wiki/Caesar_cipher

    :param word: String to rotate
    :param n: Number of places
    :return: Rotated string
    """

    cypher = ''
    for c in word:

        if not c.isalpha():
            cypher += c
            continue

        if c.isupper():
            border = 65
        else:
            border = 96

        code = border + (ord(c) + n - border) % 26
        cypher += chr(code)

    return cypher


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('ChE7Er', 7))
