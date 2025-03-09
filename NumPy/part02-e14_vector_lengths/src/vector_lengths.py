#!/usr/bin/env python3

# Exercise 2.14 (vector lengths)
# Write function vector_lengths that gets a two dimensional array of shape (n,m) as a parameter. Each row in this array corresponds to a vector. The function should return an array of shape (n,), that has the length of each vector in the input. The length is defined by the usual Euclidean norm (Wikipedia). Don't use loops at all in your solution. Instead use vectorized operations. You must use at least the np.sum and the np.sqrt functions. You can't use the function scipy.linalg.norm. Test your function in the main function.

import numpy as np
#import scipy.linalg

def vector_lengths(a):

    lenghts = a**2
    lenghts = np.sqrt(lenghts.sum(axis=1))

    return lenghts

def main():
    np.random.seed(0)
    vector = np.random.randint(1, 20, (5, 6))
    #print(vector)

    lenghts = vector_lengths(vector)
    print(lenghts)

if __name__ == "__main__":
    main()
