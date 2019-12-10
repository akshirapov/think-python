# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import string


if __name__ == '__main__':
    intab = string.ascii_letters
    outtab = string.ascii_letters
    deltab = string.whitespace + string.punctuation

    transtab = str.maketrans(intab, outtab, deltab)

    with open('words.txt') as fin:
        for line in fin.readlines():
            word = line.lower().translate(transtab)
            print(word)
