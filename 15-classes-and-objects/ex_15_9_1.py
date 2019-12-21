# -*- coding: utf-8 -*-

"""
This module contains a code for ex.1 related to ch.15.9 of
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
"""


import math
import copy


class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


class Circle:
    """Represents a circle.

    attributes: center, radius
    """


class Rectangle:
    """Represents a circle.

    attributes: width, height, corner
    """


def distance_between_points(p1, p2):
    """Computes the distance between two points."""

    dx = p1.x - p2.x
    dy = p1.y - p2.y

    return math.sqrt(dx**2 + dy**2)


def point_in_circle(point, circle):
    """Check if the Point lies in or on the boundary of the Circle."""

    d = distance_between_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Check if the Point lies in or on the boundary of the Circle."""

    p = copy.copy(rect.corner)

    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks if any of the corners of the Rectangle fall inside the circle."""

    p = copy.copy(rect.corner)

    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False


def main():
    center = Point()
    center.x = 150
    center.y = 100

    circle = Circle()
    circle.center = center
    circle.radius = 75

    print("\nPOINT IN THE CIRCLE:")
    p = Point()
    p.x = 300
    p.y = 100
    print(point_in_circle(p, circle))

    print("\nRECTANGLE IN THE CIRCLE:")
    box = Rectangle()
    box.width = 100
    box.height = 200
    box.corner = Point()
    box.corner.x = 100
    box.corner.y = 200
    print(rect_in_circle(box, circle))

    print("\nRECTANGLE FALL INSIDE THE CIRCLE:")
    print(rect_in_circle(box, circle))


if __name__ == '__main__':
    main()
