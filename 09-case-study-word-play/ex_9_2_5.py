# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def uses_all(word, letters):
    """Returns True if the word uses all the required letters at least once."""

    for c in letters:
        if c not in word:
            return False
    return True


if __name__ == '__main__':
    c1 = 0
    c2 = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            c1 += 1
        if uses_all(word, 'aeiouy'):
            c2 += 1

    print(f'Words using "aeiou": {c1}')
    print(f'Words using "aeiouy": {c2}')
