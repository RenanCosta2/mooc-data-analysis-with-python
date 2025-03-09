#!/usr/bin/env python3

# Exercise 2.15 (vector angles)
# Let x and y be m-dimensional vectors. 

# Write function vector_angles that gets two arrays X and Y with same shape (n,m) as parameters. Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) with the corresponding angles between vectors of X and Y in degrees, not in radians. Again, don't use loops, but use vectorized operations.

# Note: function np.arccos is only defined on the domain [-1.0,1.0]. If you try to compute np.arccos(1.000000001), it will fail. These kind of errors can occur due to use of finite precision in numerical computations. Force the argument to be in the correct range (clip method).

# Test your solution in the main program.

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
 
    inner_product = np.sum(X * Y, axis=1)
    X_inner_sqrt = np.sqrt(np.sum(X**2, axis=1))
    Y_inner_sqrt = np.sqrt(np.sum(Y**2, axis=1))

    angles = inner_product/(X_inner_sqrt*Y_inner_sqrt)

    angles = np.clip(angles, -1, 1)

    angles = np.degrees(np.arccos(angles))

    return angles

def main():
    np.random.seed(0)
    X = np.random.randint(1, 3, (4,4))
    Y = np.random.randint(1, 3, (4,4))

    angles = vector_angles(X, Y)

    print(angles)

if __name__ == "__main__":
    main()
