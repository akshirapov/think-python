# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def words_to_dict():
    """Stores words from txt file as keys in dictionary."""

    d = dict()

    with open('words.txt') as fin:
        for line in fin:
            d[line.strip()] = ''

    return d


if __name__ == '__main__':
    words = words_to_dict()
    print(f'{"hello" in words}')
