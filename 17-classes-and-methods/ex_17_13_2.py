# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.17.13 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


class Kangaroo:
    """A Kangaroo is a marsupial."""

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if not contents:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representation of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


def main():
    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)


if __name__ == '__main__':
    main()
