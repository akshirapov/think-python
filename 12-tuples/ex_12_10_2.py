# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.12.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def word_list():
    """Makes a dictionary where the key is the word.

    :return: Dictionary
    """

    d = {}
    with open('words.txt') as fin:
        for line in fin.readlines():
            word = line.strip().lower()
            d[word] = True
    return d


def anagrams(words):
    """Searches for anagrams."""

    d = {}
    for word in words:
        letters = ''.join(sorted(word))
        d[letters] = d.get(letters, []) + [word]
    return d


def scramble(a, n):
    """looking for letters with the most anagrams.

    :param: a: Dictionary with anagrams
    :param: n: Length of letter
    """

    t = []
    for k in a:
        if len(k) == n:
            t.append((len(a[k]), k))
    t.sort(reverse=True)

    return t[0][1]


if __name__ == '__main__':
    wl = word_list()
    ad = anagrams(wl)
    al = sorted(ad.values(), key=len, reverse=True)
    for v in al:
        if len(v) > 1:
            print(v)

    bingo = scramble(ad, 8)
    print(bingo)
