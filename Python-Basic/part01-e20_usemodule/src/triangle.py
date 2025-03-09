"""
Module triangle.py 

Calculate hypotenuse and area of the right-angled triangle
"""

__author__ = "Renan Costa"
__version__ = "v1"

import math

def hypotenuse(c1, c2):
    """
    hypotenuse which returns the length of the hypotenuse when given the lengths of two other sides of a right-angled triangle
    """
    return math.sqrt((c1 ** 2) + (c2 ** 2))

def area(c1, c2):
    """
    area which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
    """
    return (c1 * c2) / 2