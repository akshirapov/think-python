# -*- coding: utf-8 -*-

"""
This module contains a code for ex.9 related to ch.13.1 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import matplotlib.pyplot as plt

from ex_13_1_2 import process_file


def rank_freq(hist):
    """Returns a list of (rank, freq) tuples.

    :param: hist map from word to frequency
    """

    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1, f) for r, f in enumerate(freqs)]

    return rf


def plot_ranks(hist):
    """Plots frequency vs. rank.

    :param: hist: map from word to frequency
    """

    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.title("Zipf's law")

    plt.xlabel('Rank')
    plt.ylabel('Frequency')

    plt.xscale('log')
    plt.yscale('log')

    plt.plot(rs, fs)

    plt.show()


def main():
    h = process_file('war_and_peace.txt')
    plot_ranks(h)


if __name__ == '__main__':
    main()
