# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def word_dict():
    """Make a dictionary of words."""

    d = {}
    with open('words.txt') as fin:
        for line in fin:
            d[line.strip()] = []
    return d


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


def search_pairs(d):
    """Finds all the rotate pairs in wordlist.

    :param d: Dictionary of words
    """

    for k in d:
        for n in range(1, 26):
            rotated = rotate_word(k, n)
            if rotated in d:
                d[k].append(rotated)


if __name__ == '__main__':
    words = word_dict()
    search_pairs(words)

    for w in words:
        if len(words[w]) > 0:
            print(f'{w}: {words[w]}')
