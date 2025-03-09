#!/usr/bin/python3

# Exercise 3.6 (meeting lines)
# Write function meeting_lines that gets the coefficients of two lines as parameters and returns the point where the two lines meet. The equations for the lines are y=a1x+b1 and y=a2x+b2​. Use the np.linalg.solve function. Create a main function to test your solution.

# Example of usage:

# x, y = meeting_lines(a1, b1, a2, b2)

import numpy as np

def meeting_lines(a1, b1, a2, b2):

    A = np.array([[a1, -1], [a2, -1]])
    B = np.array([-b1, -b2])

    return np.linalg.solve(A, B)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
