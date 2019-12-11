# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


from ex_13_1_2 import process_file


def word_frequency(words: dict):
    """""Makes a list of word-freq pairs in descending order of frequency."""

    f = []
    for k, v in words.items():
        f.append((v, k))
    f.sort(reverse=True)

    return f


if __name__ == '__main__':
    words = process_file('war_and_peace.txt')
    print('The most frequently used words:')
    for frequent, word in word_frequency(words)[:20]:
        print(word.ljust(10), frequent, sep='\t')
