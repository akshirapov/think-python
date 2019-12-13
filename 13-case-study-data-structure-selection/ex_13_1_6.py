# -*- coding: utf-8 -*-

"""
This module contains a code for ex.6 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


from ex_13_1_2 import process_file
from ex_13_1_4 import word_to_dict


def subtract(wb, wl):
    """Returns a set of all keys that appear in wb but not wl."""
    return set(wb) - set(wl)


def main():
    words_book = process_file('war_and_peace.txt')
    words_list = word_to_dict()
    diff = subtract(words_book, words_list)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word)


if __name__ == '__main__':
    main()
