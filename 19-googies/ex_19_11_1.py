# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.19.11 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def binominal_coeff(n: int, k: int) -> int:
    """Computes binominal coefficient "n choose k".

    :param n: number of trials
    :param k: number of succeses
    """
    return 1 if k == 0 else 0 if n == 0 else binominal_coeff(n-1, k) + binominal_coeff(n-1, k-1)


def main():
    print(binominal_coeff(10, 3))


if __name__ == '__main__':
    main()
