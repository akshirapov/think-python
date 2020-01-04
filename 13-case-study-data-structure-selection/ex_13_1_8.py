# -*- coding: utf-8 -*-

"""
This module contains a code for ex.8 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import string
import random

from ex_13_1_2 import skip_header


def process_word(word: str):
    """Strips whitespace and punctuation from the word."""

    chars = string.whitespace + string.punctuation + string.digits + '”“‘’'
    return word.strip(chars)


def process_line(line: str, words: list):
    """Splits a line into words and counts the number of words."""

    line = line.replace('—', ' ')
    for word in line.split():
        pw = process_word(word)
        words.append(pw)


def word_list(filename):
    """Makes a list of the words from a file."""
    a = []
    with open(filename, encoding='utf-8') as fin:
        skip_header(fin)
        for line in fin:
            if line.startswith('End of the Project Gutenberg'):
                break
            process_line(line, a)
    return a


def markov_analysis(filename: str, n=2):
    """Performs Markov analysis.

    :param: n: number of words in the prefix
    """
    d = {}

    words = word_list(filename)
    total = len(words)
    for i in range(total):
        if total - i == n:
            break

        prefix = tuple(words[i:i+n])
        suffix = words[i+n]
        d[prefix] = d.get(prefix, []) + [suffix]

    return d


def random_text(suffix_map: dict, n=100):
    """Generates random words from the analyzed text.

    Starts with a random prefix from the dictionary.

    :param: n: number of words to generate
    """

    # Start prefix
    prefix = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map[prefix]

        word = random.choice(suffixes)
        print(word, end=' ')

        # Next prefix
        prefix = prefix[1:] + (word,)


def main():
    m = markov_analysis('war_and_peace.txt', 2)
    random_text(m, 20)


if __name__ == '__main__':
    main()
