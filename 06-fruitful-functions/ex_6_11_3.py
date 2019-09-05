# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.6.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def first(word):
    """Returns the first letter of a word."""

    if len(word) == 0:
        return ''
    else:
        return word[0]


def last(word):
    """Returns the last letter of a word."""

    if len(word) == 0:
        return ''
    else:
        return word[-1]


def middle(word):
    """Returns letters without the first and last letters of a word."""
    return word[1:-1]


def is_palindrome(word):
    """Checks the word if he is a palindrome."""

    if len(word) <= 1:
        return True

    if first(word) != last(word):
        return False

    return is_palindrome(middle(word))


if __name__ == '__main__':
    print(is_palindrome('noon'))
    print(is_palindrome('redivider'))
    print(is_palindrome('cat'))
