#!/usr/bin/env python3

# Exercise 2.13 (diamond)
# Create a function diamond that returns a two dimensional integer array where the 1s form a diamond shape. Rest of the numbers are 0. The function should get a parameter that tells the length of a side of the diamond. Do this using the eye and concatenate functions of NumPy and array slicing.

# Example of usage:


# print(diamond(3))
# [[0 0 1 0 0]
#  [0 1 0 1 0]
#  [1 0 0 0 1]
#  [0 1 0 1 0]
#  [0 0 1 0 0]]

# print(diamond(1))
# [[1]]

import numpy as np

def diamond(n):
    
    identity = np.eye(n, dtype=int)
    reverse_identity = np.fliplr(np.eye(n, dtype=int))
    reverse_identity = np.delete(reverse_identity, n-1, axis=1)

    upper_diamond = np.concatenate((reverse_identity, identity), axis=1)


    lower_identity = np.delete(identity, 0, axis=0)
    lower_identity_flip = np.fliplr(lower_identity)
    lower_identity_flip = np.delete(lower_identity_flip, 0, axis=1)

    lower_diamond = np.concatenate((lower_identity, lower_identity_flip), axis=1)

    full_diamond = np.concatenate((upper_diamond, lower_diamond), axis=0)

    return np.array(full_diamond)

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
