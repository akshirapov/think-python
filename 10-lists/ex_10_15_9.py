# -*- coding: utf-8 -*-

"""
This module contains a code for ex.9 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import time


def words_plus():
    """Reads lines from a file and builds a list using addition."""

    result = []

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        result = result + [word]

    return result


def words_append():
    """Reads lines from a file and builds a list using append."""

    result = []

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        result.append(word)

    return result


if __name__ == '__main__':
    start = time.time()
    print(len(words_append()))
    stop = time.time()
    print(f'{stop-start}')

    print('*'*80)

    start = time.time()
    print(len(words_plus()))
    stop = time.time()
    print(f'{stop-start}')
    # Adding with '+' is slower since a new list is created at each iteration.
