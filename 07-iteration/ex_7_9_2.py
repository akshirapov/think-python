# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.7.9 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import math


def eval_loop():
    """ Evaluates the given expressions."""

    result = None
    while True:
        exp = input('Enter expression:\n')
        if exp == 'done':
            print(result)
            break
        result = eval(exp)
        print(result)


if __name__ == '__main__':
    eval_loop()
