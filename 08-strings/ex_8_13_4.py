# -*- coding: utf-8 -*-

"""
This module contains a code for ex.4 related to ch.8.13 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


"""
According to the exercise, for each function, it is necessary to describe 
what it actually does (assuming that the parameter is a string).
"""


def any_lowercase1(s):
    """Checks if the first letter is lowercase."""

    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Returns string "True"."""

    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Checks if the last letter is lowercase."""

    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Checks if any letter is lowercase."""

    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Checks if the all word is lowercase."""

    for c in s:
        if not c.islower():
            return False
    return True
