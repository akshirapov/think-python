# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.5.14 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def is_triangle(a, b, c):
    """Prints either “Yes” or “No”, depending on whether you can or
     cannot form a triangle from sticks with the given lengths.

    :param a: Length of stick.
    :param b: Length of stick.
    :param c: Length of stick.
    """

    if (a+b <= c) and (a+c <= b) and (b+c <= a):
        print('Yes')
    else:
        print('No')


def main():
    """Prompts the user to input values for sticks a, b and c and checks
    whether they form triangle.
    """

    print('Enter lengths of sticks to check')
    a = int(input('Enter a:\n'))
    b = int(input('Enter b:\n'))
    c = int(input('Enter c:\n'))

    is_triangle(a, b, c)


if __name__ == '__main__':
    main()
