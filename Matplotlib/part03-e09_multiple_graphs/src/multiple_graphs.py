#!/usr/bin/env python3

# Exercise 3.9 (multiple graphs)
# In the above plot the x coordinates were implicitly set to the indices of the array a, that is, arange(10). Find out from the documentation of plt.plot how to specify the x coordinates explicitly. Find out also how to draw multiple graphs in one axes.

# Make your main function plot the following two graphs in one axes. The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.

# Add also a title and some labels for x axis and y axis. Note that in the non-interactive mode you have to call plt.show() for the figure to show.

import matplotlib.pyplot as plt
import numpy as np

def main():
    
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])

    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title("My first figure")
    plt.xlabel("My x-axis")
    plt.ylabel("My y-axis")
    plt.show()


if __name__ == "__main__":
    main()
