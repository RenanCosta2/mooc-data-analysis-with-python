#!/usr/bin/env python3

# Exercise 2.11 (rows and columns)
# Write two functions, get_rows and get_columns, that get a two dimensional array as parameter. They should return the list of rows and columns of the array, respectively. The rows and columns should be one dimensional arrays. You may use the transpose operation, which flips rows to columns, in your solution. The transpose is done by the T method:


# a=np.random.randint(0, 10, (4,4))
# print(a)
# print(a.T)
# [[0 1 9 9]
# [0 4 7 3]
# [2 7 2 0]
# [0 4 5 5]]
# [[0 0 2 0]
# [1 4 7 4]
# [9 7 2 5]
# [9 3 0 5]]

# Test your solution in the main function. Example of usage:


# a = np.array([[5, 0, 3, 3],
#  [7, 9, 3, 5],
#  [2, 4, 7, 6],
#  [8, 8, 1, 6]])
# get_rows(a)
# [array([5, 0, 3, 3]), array([7, 9, 3, 5]), array([2, 4, 7, 6]), array([8, 8, 1, 6])]
# get_columns(a)
# [array([5, 7, 2, 8]), array([0, 9, 4, 8]), array([3, 3, 7, 1]), array([3, 5, 6, 6])]

import numpy as np

def get_rows(a):

    return list(a)

def get_columns(a):

    return list(a.T)

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
