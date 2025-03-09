#!/usr/bin/env python3

# Exercise 3.1 (column comparison)
# Write function column_comparison that gets a two dimensional array as parameter. The function should return a new array containing those rows from the input that have the value in the second column larger than in the second last column. You may assume that the input contains at least two columns. Don't use loops, but instead vectorized operations. Try out your function in the main function.

# For array

#  [[8, 9, 3, 8, 8],
#  [0, 5, 3, 9, 9],
#  [5, 7, 6, 0, 4],
#  [7, 8, 1, 6, 2],
#  [2, 1, 3, 5, 8]]
# the result would be

#  [[8, 9, 3, 8, 8],
#  [5, 7, 6, 0, 4],
#  [7, 8, 1, 6, 2]]

import numpy as np

def column_comparison(a):

    new_array = a[a[:, 1] > a[:, -2]]
    
    return new_array
    
def main():
    np.random.seed(0)
    numbers = np.random.randint(1, 9, (5, 5))
    
    array = column_comparison(numbers)

    print(array)

if __name__ == "__main__":
    main()
