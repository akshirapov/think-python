# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.7.9 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import math


def estimate_pi():
    """Estimates the pi with the algorithm of Srinivasa Ramanujan."""

    pi = 0
    k = 0
    while True:
        n = math.factorial(4*k) * (1103 + 26390*k)
        d = math.factorial(k)**4 * 396**(4*k)
        term = 2 * math.sqrt(2) / 9801 * n / d

        pi += term
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / pi


if __name__ == '__main__':
    print(estimate_pi())
    print(math.pi)
