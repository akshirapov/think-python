# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.14.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


def sed(pattern, replace, file1, file2):
    """Reads a file1 and writes the destination file.

    In each line, replaces pattern with replace.

    :param pattern:
    :param replace:
    :param file1:
    :param file2:
    """

    try:
        fin = open(file1)
        fout = open(file2, 'w')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print('An error has occurred')
        return


def main():
    sed('Lorem', 'Cicero', 'file1.txt', 'file2.txt')


if __name__ == '__main__':
    main()
