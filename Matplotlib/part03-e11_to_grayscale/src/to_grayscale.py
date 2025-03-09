#!/usr/bin/env python3

# Exercise 3.11 (to grayscale)
# This exercise can give two points at maximum!

# Part 1:

# Write a function to_grayscale that takes an RGB image (three dimensional array) and returns a two-dimensional gray-scale image. The conversion to gray-scale should take a weighted sum of the red, green, and blue values, and use that as the value of gray. The first axis is the x, the second is y, and the third is the color components (red, green, blue). Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. These weights are so because the human eye is most sensitive to green color and least sensitive to blue color.

# In the main function you can, for example, use the provided image src/painting.png. Display the grayscale image with the plt.imshow function. You may have to call the function plt.gray to set the color palette (colormap) to gray. (See help(plt.colormaps) for more information about colormaps.)

# Part 2:

# Write functions to_red, to_green, and to_blue that get a three dimensional array as a parameter and return a three dimensional array. For instance, the function to_red should zero out the green and blue color components and return the result. In the main function, create a figure with three subfigures: the top one should be the red image, the middle one the green image, and the bottom one the blue image.

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(painting):

    gray_image = (0.2126 * painting[:, :, 0]) + (0.7152 * painting[:, :, 1]) + (0.0722 * painting[:, :, 2])

    return gray_image

def to_red(painting):

    red_image = painting.copy()

    red_image[:, :, 1] = 0.0
    red_image[:, :, 2] = 0.0

    return red_image

def to_green(painting):

    green_image = painting.copy()

    green_image[:, :, 0] = 0.0
    green_image[:, :, 2] = 0.0

    return green_image

def to_blue(painting):

    blue_image = painting.copy()

    blue_image[:, :, 0] = 0.0
    blue_image[:, :, 1] = 0.0

    return blue_image

def main():
    
    painting = plt.imread("src/painting.png")

    gray_image = to_grayscale(painting)
    plt.imshow(gray_image, cmap="gray")

    fix, ax = plt.subplots(1, 3)

    red_image = to_red(painting)
    ax[0].imshow(red_image)

    green_image = to_green(painting)
    ax[1].imshow(green_image)

    blue_image = to_blue(painting)
    ax[2].imshow(blue_image)

    plt.show()


if __name__ == "__main__":
    main()
