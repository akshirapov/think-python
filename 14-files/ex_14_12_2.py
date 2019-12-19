# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.14.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import shelve


def word_list(filename):
    """Makes a dictionary where the key is the word.

    :param filename: file with words
    """

    d = {}
    with open(filename) as fin:
        for line in fin.readlines():
            word = line.strip().lower()
            d[word] = None
    return d


def anagrams(words):
    """Searches for anagrams."""

    d = {}
    for word in words:
        letters = ''.join(sorted(word))
        d[letters] = d.get(letters, []) + [word]
    return d


def read_anagrams(filename, word):
    """Looks up the word in shelf and returns a list of its anagrams.

    :param filename: file name of shelf
    :param word: word to look up
    """

    letters = ''.join(sorted(word))
    with shelve.open(filename) as db:
        try:
            return db[letters]
        except KeyError:
            return []


def store_anagrams(filename, a_map):
    """Stores the anagrams from a dictionary in a shelf.

    :param filename: file name of shelf
    :param a_map: dictionary that maps string to list of anagrams
    """

    with shelve.open(filename) as db:
        for letters, words in a_map.items():
            db[letters] = words


def main():
    wl = word_list('words.txt')
    ad = anagrams(wl)

    shelf = 'anagrams'
    store_anagrams(shelf, ad)
    print(read_anagrams(shelf, 'hello'))


if __name__ == '__main__':
    main()
