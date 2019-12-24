# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.17.13 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object."""
        minutes = hour*60 + minute
        seconds = minutes*60 + second
        self.second = seconds

    def __str__(self):
        """Returns a string representation of the time."""
        minutes, second = divmod(self.second, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.second

    def is_after(self, other):
        """Returns True if t1 is after t2; False otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Add two Time objects or a Time object and a number."""
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.second
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return 0 <= self.second < 24 * 60 * 60


def int_to_time(seconds):
    """Makes a new Time object."""
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    # end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
