# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.6.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def ack(m, n):
    """Evaluates the Ackermann function A(m, n).
    https://en.wikipedia.org/wiki/Ackermann_function

    :param m: Positive integer
    :param n: Positive integer
    :return: Natural number
    """

    if m < 0 or n < 0:
        print('Arguments must be greater than or equal zero.')
        return

    if m == 0:
        return n + 1

    if n == 0:
        return ack(m-1, 1)

    return ack(m-1, ack(m, n-1))


if __name__ == '__main__':
    print(ack(3, 4))
