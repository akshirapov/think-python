# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import string


def process_word(word: str):
    """Strips whitespace and punctuation from the word
    and converts it to lowercase.
    """

    chars = string.whitespace + string.punctuation + string.digits + '”“‘’'
    return word.strip(chars).lower()


def process_line(line: str, words: dict):
    """Splits a line into words and counts the number of words."""

    line = line.replace('—', ' ')
    exceptions = ['', 'abc'] + list('bcdefghjklmnopqrstuvxwyz')

    for word in line.split():
        pw = process_word(word)
        if pw not in exceptions:
            words[pw] = words.get(pw, 0) + 1


def process_file(filename: str):
    """Makes a histogram that contains the words from a file."""

    if not filename:
        return

    words = {}

    with open(filename, encoding='utf8') as fin:
        skip_header(fin)
        for line in fin:
            if line.startswith('End of the Project Gutenberg'):
                break
            process_line(line, words)

    return words


def skip_header(fin):
    """Reads from file until it finds the line that ends the header."""

    for line in fin:
        if line.startswith('*** START OF THIS PROJECT GUTENBERG'):
            break


def total_words(words: dict):
    """Counts the total number of words."""
    return sum(words.values())


def diff_words(words: dict):
    """Counts the different number of words."""
    return len(words)


if __name__ == '__main__':
    words = process_file('war_and_peace.txt')

    total = total_words(words)
    diff = diff_words(words)

    print(f'Total words: {total}')
    print(f'Different words: {diff}')
