# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.16.7 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """


def print_time(t):
    """Prints a string representation of the time.

    t: time object
    """

    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def int_to_time(seconds: int):
    """Makes a new Time object from seconds.

    :param seconds: seconds from midnight
    """

    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time: Time):
    """Computes the number of seconds since midnight.

    :param time: time object
    """

    return time.hour*60*60 + time.minute*60 + time.second


def mul_time(time: Time, n: int):
    """Multiplies a time n times.

    :param time: time object
    :param n: number of multiplications
    """

    seconds = time_to_int(time) * n

    return int_to_time(seconds)


def main():
    original_time = Time()
    original_time.hour = 11
    original_time.minute = 59
    original_time.second = 30

    print('\nMultiplication:')
    print('*'*40)
    factor = 5
    new_time = mul_time(original_time, factor)
    print(f'Factor: {factor}')
    print_time(original_time)
    print_time(new_time)

    print('\nMarathon:')
    print('*'*40)
    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5
    print('The finishing time:')
    print_time(race_time)

    distance = 13.1
    pace = mul_time(race_time, 1/distance)
    print(f'Time per mile:')
    print_time(pace)


if __name__ == '__main__':
    main()
