# -*- coding: utf-8 -*-

"""
This module contains a code for ex.7 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import random
import bisect

from ex_13_1_2 import process_file
from ex_10_15_2 import cumsum


def random_word(wb: dict):
    """Chooses a random word from a book.

    The probability of each word is proportional to its frequency.
    """

    words = []
    freqs = []
    total_freq = 0

    for word, freq in wb.items():
        words.append(word)
        freqs.append(freq)
        total_freq += freq

    # Make list of cumulative frequencies
    freqs = cumsum(freqs)

    rn = random.randint(0, total_freq-1)
    i = bisect.bisect(freqs, rn)

    return words[i]


def main():
    words_book = process_file('war_and_peace.txt')
    print("Some random words from the book:")
    for i in range(10):
        rw = random_word(words_book)
        print(rw)


if __name__ == '__main__':
    main()
