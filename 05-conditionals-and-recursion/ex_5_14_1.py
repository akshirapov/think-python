
"""This module contains a code for ex.1 related to ch.5.14.

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""

import time


if __name__ == '__main__':
    """Converts the current time to a time of days, hours, minutes and
    seconds from the epoch.
    """

    now = time.time()

    hours = int(now // (60*60))
    minutes = int(now // 60 - hours*60)
    seconds = int(now % 60)
    days = int(hours // 24)

    print(f'{days} days '
          f'{hours-24*days} hours '
          f'{minutes} minutes '
          f'{seconds} seconds '
          f'since the epoch.')
