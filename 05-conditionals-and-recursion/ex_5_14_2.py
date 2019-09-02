# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.5.14 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def check_fermat(a, b, c, n):
    """Checks to see if Fermat's theorem holds.

    :param a: positive int
    :param b: positive int
    :param c: positive int
    :param n: natural number
    """

    if (n > 2) and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def main():
    """Prompts the user to input values for a, b, c and n and check
    whether they violate Fermat’s theorem.
    """

    a = int(input('Enter a:\n'))
    b = int(input('Enter b:\n'))
    c = int(input('Enter c:\n'))
    n = int(input('Enter n:\n'))

    check_fermat(a, b, c, n)


if __name__ == '__main__':
    main()
