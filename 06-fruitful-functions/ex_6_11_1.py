# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.6.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def b(z):
    prod = a(z, z)
    print(z, prod)
    print(f'[b]: z->{z}')
    return prod


def a(x, y):
    x = x + 1
    print(f'[a]: x->{x}, y->{y}')
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    print(f'[c]: x->{x}, y->{y}, z->{z}')
    return square


if __name__ == '__main__':
    x = 1
    y = x + 1
    print(c(x, y+3, x+y))
