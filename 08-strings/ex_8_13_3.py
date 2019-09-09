# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.8.13 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_palindrome(word):
    """Checks the word if he is a palindrome."""
    return word == word[::-1]


if __name__ == '__main__':
    print(is_palindrome('noon'))
    print(is_palindrome('redivider'))
    print(is_palindrome('cat'))
