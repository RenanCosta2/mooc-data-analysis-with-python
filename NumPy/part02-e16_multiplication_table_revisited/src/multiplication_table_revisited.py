#!/usr/bin/env python3

# Exercise 2.16 (multiplication table revisited)
# Write function multiplication_table that gets a positive integer n as parameter. The function should return an array with shape (n,n). The element at index (i,j) should be i*j. Don't use for loops! In your solution, rely on broadcasting, the np.arange function, reshaping and vectorized operators. Example of usage:


# print(multiplication_table(4))
# [[0 0 0 0]
# [0 1 2 3]
# [0 2 4 6]
# [0 3 6 9]]

import numpy as np

def multiplication_table(n):

    array_row = np.arange(n)
    array_column = np.arange(n).reshape((n, 1))

    table = array_row*array_column

    return table

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
