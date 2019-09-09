# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def avoids(s: str, forbidden: str):
    """Returns True if the string doesn’t use any of the forbidden letters."""

    for c in forbidden:
        if c in s:
            return False
    return True


if __name__ == '__main__':
    uin = input('Enter forbidden letters:\n')
    count = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, uin):
            print(word)
            count += 1

    print(f"Words that don't contain any of forbidden letters: {count}")
