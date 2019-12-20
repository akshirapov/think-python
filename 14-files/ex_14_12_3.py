# -*- coding: utf-8 -*-

"""
This module contains a code for ex.3 related to ch.14.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import os
import hashlib


def search_files(folder: str, suffix='') -> list:
    """Searches a directory and all of its subdirectories, recursively.

    Returns a list of complete paths for all files with a given suffix.
    """

    r = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(suffix):
                r.append(os.path.join(root, filename))
    return r


def md5sum(filename) -> str:
    """Return the digest value of file."""

    with open(filename, 'rb') as file:
        data = file.read()
        return hashlib.md5(data).hexdigest()


def compute_checksums(files: list) -> dict:
    """"Computes checksums for files.

    Returns a map from checksum to list of files with that checksum.
    """

    d = {}
    for name in files:
        checksum = md5sum(name)
        d[checksum] = d.get(checksum, []) + [name]
    return d


def search_duplicates(files: list):
    """Recognizes duplicates using "checksum" of files."""

    checksums = compute_checksums(files)
    for c, names in checksums.items():
        if len(names) > 1:
            print('*'*80)
            print('The following files have the same checksum:')
            for name in names:
                print(name)


def main():
    directory = os.getcwd()
    files = search_files(directory, '.mp3')
    search_duplicates(files)


if __name__ == '__main__':
    main()
