# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


if __name__ == '__main__':
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
