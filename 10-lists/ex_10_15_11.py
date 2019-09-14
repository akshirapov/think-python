# -*- coding: utf-8 -*-

"""
This module contains a code for ex.11 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def in_bisect(a, v):
    """Searches the value in list.

    :param a: Sorted list
    :param v: Target value
    :return: Bool
    """

    if len(a) == 0:
        return False

    i = len(a) // 2
    if a[i] == v:
        return True

    if a[i] > v:
        return in_bisect(a[:i], v)
    else:
        return in_bisect(a[i+1:], v)


if __name__ == '__main__':
    words = []
    with open('words.txt') as fin:
        for line in fin:
            words.append(line.strip())

    words.sort()

    for word in words:
        reversed_word = word[::-1]
        if in_bisect(words, reversed_word):
            print(f'{word}: {reversed_word}')
