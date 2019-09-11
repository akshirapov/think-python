# -*- coding: utf-8 -*-

"""
This module contains a code for ex.8 related to ch.9.2 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_palindrome(string: str):
    """Checks the string if it is a palindrome.

    :returns Bool
    """
    return string.lower() == string[::-1].lower()


if __name__ == '__main__':
    for i in range(100000, 999996):
        if not (is_palindrome(str(i)[-4:]) and
                is_palindrome(str(i+1)[-5:]) and
                is_palindrome(str(i+2)[-5:-1]) and
                is_palindrome(str(i+3))):
            continue
        else:
            print(i)
