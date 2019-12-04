# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.12.10 of
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


def anagrams(words: dict):
    """Searches for anagrams."""

    d = {}
    for word in words:
        letters = ''.join(sorted(word))
        d[letters] = d.get(letters, []) + [word]
    return d


def difference(word1: str, word2: str):
    """Counts the number of differences between two words."""

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count


def metathesis_pair(d: dict):
    """Print all pairs of words that differ by swapping two letters.

    :param d: map from word to list of anagrams
    """

    for a_list in d.values():
        for word1 in a_list:
            for word2 in a_list:
                if word1 < word2 and difference(word1, word2) == 2:
                    print(word1, word2)


if __name__ == '__main__':
    wl = word_list()
    anms = anagrams(wl)
    metathesis_pair(anms)
