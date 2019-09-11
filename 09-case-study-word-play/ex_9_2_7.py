# -*- coding: utf-8 -*-

"""
This module contains a code for ex.7 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def has_three_consecutive_double_letters(string: str):
    """Returns a word with three consecutive double letters."""

    if len(string) < 6:
        return False

    index = 0
    for char in string:
        # looking for the first pair
        index = string.find(2*char)
        if index != -1:
            break

    # no double letters
    if index == -1:
        return False

    if len(string[index:]) < 6:
        return False

    if string[index+2] != string[index+3]:
        return False

    if string[index+4] != string[index+5]:
        return False

    return True


if __name__ == '__main__':
    with open('words.txt') as fin:
        for line in fin:
            word = line.strip()
            if has_three_consecutive_double_letters(word):
                print(word)
