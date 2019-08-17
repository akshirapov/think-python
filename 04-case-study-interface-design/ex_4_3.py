
import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def circle(t, r):
    c = 2 * math.pi * r
    length = 10
    n = int(c/length)
    polygon(t, length, n)


def arc(t, r, angle):
    c = 2 * math.pi * r
    length = 10
    n = int(c/length)
    for i in range(int(n*angle/360)):
        t.fd(length)
        t.lt(360/n)


bob = turtle.Turtle()

square(bob, 100)
polygon(bob, 100, 10)
circle(bob, 100)
arc(bob, 100, 270)

turtle.mainloop()
