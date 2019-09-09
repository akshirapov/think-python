# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def has_no_e(s: str):
    """Returns True if the given word doesn’t have the letter “e” in it."""
    return 'e' not in s.lower()


if __name__ == '__main__':
    total = 0
    e_count = 0

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
            e_count += 1
        total += 1

    percentage = round(e_count/total*100)
    print('-'*80)
    print(f'Words that have no "e": {percentage}%')
