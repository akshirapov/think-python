# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.18.12 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


class PingPongParent:
    pass


class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong


class Pong(PingPongParent):
    def __init__(self, pings=None):
        if pings in None:
            self.pings = []
        else:
            self.pings = pings

    def add_ping(self, ping):
        self.pings.append(ping)


def main():
    pong = Pong()
    ping = Ping(pong)
    pong.add_ping(ping)


if __name__ == '__main__':
    main()
