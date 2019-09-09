# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def uses_only(word, letters):
    """Returns True if the word contains only letters in the list."""

    for c in word:
        if c not in letters:
            return False
    return True


if __name__ == '__main__':
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if uses_only(word, 'acefhlo'):
            print(word)
