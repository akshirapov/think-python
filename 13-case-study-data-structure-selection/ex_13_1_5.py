# -*- coding: utf-8 -*-

"""
This module contains a code for ex.5 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


from ex_13_1_2 import process_file
from random import choices

if __name__ == '__main__':
    words = process_file('war_and_peace.txt')
    r = choices(list(words.keys()), words.values())
    print(f'{r}')
