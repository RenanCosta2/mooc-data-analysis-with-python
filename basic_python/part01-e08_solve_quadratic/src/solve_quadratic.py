#!/usr/bin/env python3

# Exercise 1.8 (solve quadratic)
 
# Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:

# print(solve_quadratic(1,-3,2))
# (2.0,1.0)
# print(solve_quadratic(1,2,1))
# (-1.0,-1.0)
# You may want to use the math.sqrt function from the math module in your solution. Test that your function works in the main function!

import math
import numpy as np

def solve_quadratic(a, b, c):
    x1 = ((-b) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = ((-b) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

    return (x1, x2)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
