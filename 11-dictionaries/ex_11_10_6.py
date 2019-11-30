# -*- coding: utf-8 -*-

"""
This module contains a code for ex.6 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def word_dict():
    """Make a dictionary of words."""

    d = {}
    with open('words.txt') as fin:
        for line in fin:
            d[line.strip().lower()] = []
    return d


def pron_dict():
    """Make a dictionary of pronunciations of words."""

    d = {}
    with open('c06d') as fin:
        for line in fin:
            if line[0] == '#':
                continue
            word = line.split()[0]
            pron = ' '.join(line.split()[1:])
            d[word.lower()] = pron
    return d


def homophones(a: str, b: str, prons: dict):
    """Checks if two letters are pronounced the same way."""

    if a not in prons:
        return False
    if b not in prons:
        return False

    return prons[a] == prons[b]


def check(word: str, words: dict, prons: dict):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation."""

    word1 = word[1:]
    if word1 not in words:
        return False
    if not homophones(word, word1, prons):
        return False

    word2 = word[0] + word[2:]
    if word2 not in words:
        return False
    if not homophones(word, word2, prons):
        return False

    return True


if __name__ == '__main__':
    words = word_dict()
    prons = pron_dict()
    for wd in words:
        if check(wd, words, prons):
            print(f'{wd}: {wd[1:]}, {wd[0]+wd[2:]}')
