#!/usr/bin/env python3

# Exercise 3.10 (subfigures)
# Write function subfigures that creates a figure that has two subfigures (two axes in matplotlib parlance). The function gets a two dimensional array a as a parameter. In the left subfigure draw using the plot method a graph, whose x coordinates are in the first column of a and the y coordinates are in the second column of a. In the right subfigure draw using the scatter method a set of points whose x coords are again in the first column of a and whose y coordinates are in the second column of a. Additionally, the points should get their color from the third column of a, and size of the point from the fourth column of a. For this, use the c and s named parameters of scatter, respectively

# Test your function subfigure from the main function.

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1, 2)

    first_column = a[:, 0]
    second_column = a[:, 1]
    third_column = a[:, 2]
    fourth_column = a[:, 3]

    ax[0].plot(first_column, second_column) 
    ax[1].scatter(first_column, second_column, c=third_column, s=fourth_column)

    plt.show()

def main():
    np.random.seed(0)
    array = np.random.randint(1, 100, (4, 4))

    print(array)

    subfigures(array)

if __name__ == "__main__":
    main()
