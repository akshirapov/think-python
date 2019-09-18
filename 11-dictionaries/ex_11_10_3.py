# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.11.10 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


memo = {}


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

    if (m, n) in memo:
        return memo[m, n]
    else:
        memo[m, n] = ack(m-1, ack(m, n-1))
        return memo[m, n]


if __name__ == '__main__':
    print(ack(3, 6))
