# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.12.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def word_list() -> dict:
    """Makes a dictionary of words."""

    d = {}
    with open('words.txt') as fin:
        for line in fin.readlines():
            word = line.strip().lower()
            d[word] = True
    return d


def is_reducible(word, words) -> bool:
    """Checks the word can be reduced."""

    if word == 'a' or word == 'i' or word == '':
        return True

    if word not in words:
        return False

    for i in range(len(word)):
        if is_reducible(word[:i]+word[i+1:], wl):
            return True

    return False


def all_reducible(words) -> list:
    """Returns words that can be reduced."""

    r = []
    for word in words:
        if is_reducible(word, words):
            r.append((len(word), word))
    r.sort(reverse=True)

    return r


if __name__ == '__main__':
    wl = word_list()
    wr = all_reducible(wl)
    print(wr[0][1])
