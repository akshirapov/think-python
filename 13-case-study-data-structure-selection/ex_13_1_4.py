# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


from ex_13_1_2 import process_file


def word_to_dict(filename='words.txt'):
    """Reads file and returns dictionary of words."""

    d = {}
    with open(filename, encoding='utf8') as fin:
        for line in fin:
            word = line.strip()
            d[word] = None
    return d


if __name__ == '__main__':
    words_book = process_file('war_and_peace.txt')
    words_list = word_to_dict()
    for word_book in words_book:
        if word_book not in words_list:
            print(word_book)
