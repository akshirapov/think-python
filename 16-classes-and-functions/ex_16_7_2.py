# -*- coding: utf-8 -*-

"""
This module contains a code for ex.2 related to ch.16.7 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


from datetime import date, datetime


def main():
    print("\nToday's date:")
    today = datetime.today()
    print(today.strftime("%A, %B %d, %Y"))

    print("\nYour next birthday and how far away it is:")
    # s = input('Input your birthday mm/dd/yyyy format:\n')
    s = '10/11/1989'
    birthday = datetime.strptime(s, '%m/%d/%Y')
    delta_year = (today.month, today.day) > (birthday.month, birthday.day)
    next_birthday = birthday.replace(year=today.year + delta_year)
    until_next_birthday = next_birthday-today
    print(next_birthday.strftime('%B %d, %Y'))
    print(until_next_birthday)

    print("\nYour age:")
    last_birthday = birthday.replace(year=next_birthday.year-1)
    print(last_birthday.year-birthday.year)

    print("\nFor people born on these dates:")
    birthday1 = date(day=11, month=5, year=1967)
    birthday2 = date(day=11, month=10, year=2003)
    print(birthday1)
    print(birthday2)

    print("\nDouble Day is")
    d1 = min(birthday1, birthday2)
    d2 = max(birthday1, birthday2)
    dd = d2 + (d2 - d1)
    print(dd)


if __name__ == '__main__':
    main()
