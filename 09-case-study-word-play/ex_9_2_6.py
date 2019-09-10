# -*- coding: utf-8 -*-

"""
This module contains a code for ex.6 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_abecedarian(word):
    """Returns True if the letters in a word appear in alphabetical order."""

    if len(word) <= 1:
        return True

    order = ord(word[0])
    for c in word:
        if ord(c) < order:
            return False
        order = ord(c)

    return True


if __name__ == '__main__':
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            count += 1

    print('*'*80)
    print(f'Words with letters in alphabetical order: {count}')
