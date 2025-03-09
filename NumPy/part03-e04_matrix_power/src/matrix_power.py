#!/usr/bin/env python3

# Exercise 3.4 (matrix power)
# Repeat the functionality of the NumPy function numpy.linalg.matrix_power, which raises a square matrix of shape (m,m) to the nth power. Here the multiplication is the matrix multiplication. Square matrix a raised to power n is therefore a @ a @ ... @ a where a is repeated n times. When n is zero then 
# a
# 0
# a 
# 0
#   is equal to np.eye(m).

# Write function matrix_power that gets as first argument a square matrix a and as second argument a non-negative integer n. The function should return the matrix a multiplied by itself n-1 times. Use Python's reduce function and a generator expression.

# Extend the matrix_power function. For negative powers, we define a^-1 to be equal to the multiplicative inverse of a. You can use NumPy's function numpy.linalg.inv for this. And you may assume that the input matrix is invertible.

from functools import reduce
import numpy as np

def matrix_power(a, n):

    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    elif n < 0:
        inv_matrix = np.linalg.inv(a)
        return reduce(lambda x, _: x @ inv_matrix, range(abs(n) - 1), inv_matrix)
        
    matrix = reduce(lambda x, _ : x @ a, range(n-1), a)

    return matrix

def main():

    np.random.seed(0)
    matrix = np.random.randint(1, 3, (2, 2))

    print(matrix_power(matrix, 2))


if __name__ == "__main__":
    main()
