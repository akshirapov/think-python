# -*- coding: utf-8 -*-

"""
This module contains a code for ex.8 related to ch.10.15 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import random


def has_duplicates(seq: list):
    """Checks if sequence has duplicates."""

    for el in seq:
        if seq.count(el) > 1:
            return True

    return False


if __name__ == '__main__':
    count = 0
    for _ in range(100):  # for accuracy
        students = []
        for i in range(23):
            day = random.randint(1, 31)
            month = random.randint(1, 12)
            students.append([day, month])

        if has_duplicates(students):
            count += 1
    print(count)
