# -*- coding: utf-8 -*-

"""
This module contains a code for ex.12 related to ch.10.15 of
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


def interlock(a, v):
    """Checks whether a word contains two interleaved words."""
    return in_bisect(a, v[::2]) and in_bisect(a, v[1::2])


def interlock_general(a, v, n):
    """Checks whether a word contains n interleaved words."""

    for i in range(n):
        if not in_bisect(a, v[i::n]):
            return False

    return True


if __name__ == '__main__':
    words = []
    with open('words.txt') as fin:
        for line in fin:
            words.append(line.strip())

    words.sort()

    print('Two interleaved words:')
    for word in words:
        if interlock(words, word):
            print(f'{word} = {word[::2]} + {word[1::2]}')

    print('Three interleaved words:')
    for word in words:
        if interlock_general(words, word, 3):
            print(f'{word} = {word[::3]} + {word[1::3]} + {word[2::3]}')
