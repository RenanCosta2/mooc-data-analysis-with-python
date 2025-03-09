#!/usr/bin/env python3

# Exercise 3.12 (radial fade)
# Make program that does fading of an image as earlier, except now not in horizontal direction but in radial direction. As we move away from the centre of the image, the pixels fade to black.

# Part 1:

# Write function center that returns coordinate pair (center_y, center_x) of the image center. Note that these coordinates might not be integers. Example of usage:


# print(center(np.zeros((10, 11, 3))))
# (4.5, 5)
# The function should work both for two and three dimensional images, that is grayscale and color images.

# Write also function radial_distance that returns for image with width w and height h an array with shape (h,w), where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image.

# Part 2:

# Create function scale(a, tmin=0.0, tmax=1.0) that returns a copy of the array a with its elements scaled to be in the range [tmin,tmax].

# Using the functions radial_distance and scale write function radial_mask that takes an image as a parameter and returns an array with same height and width filled with values between 0.0 and 1.0. Do this using the scale function. To make the resulting array values near the center of array to be close to 1 and closer to the edges of the array are values closer to be 0, subtract the previous array from 1.

# Write also function radial_fade that returns the image multiplied by its radial mask.

# Test your functions in the main function, which should create, using matplotlib, a figure that has three subfigures stacked vertically. On top the original painting.png, in the middle the mask, and on the bottom the faded image.

import numpy as np
import matplotlib.pyplot as plt

def center(a):

    return ((a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2) 

def radial_distance(a):

    height, width = a.shape[:2]

    y_center, x_center = center(a)

    y_indexes, x_indexes = np.meshgrid(np.arange(height), np.arange(width), indexing="ij")

    distance = np.sqrt((x_indexes - x_center) ** 2 + (y_indexes - y_center) ** 2)
    
    return distance

def scale(a, tmin=0.0, tmax=1.0):
    
    amin = np.min(a)
    amax = np.max(a)
    
    if amin == amax:
        return np.full_like(a, tmin)
    
    scaled = tmin + (a - amin) * (tmax - tmin) / (amax - amin)
    
    return scaled

def radial_mask(a):

    a = radial_distance(a)

    mask = 1 - scale(a)

    return mask

def radial_fade(a):

    height, width = a.shape[:2]

    mask = radial_mask(a)

    return a * mask[:, :, np.newaxis]

def main():
    painting = plt.imread("src/painting.png")

    fig, ax = plt.subplots(3, 1)

    a = np.random.rand(5, 5, 3)

    print(radial_mask(a))

    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(painting))
    ax[2].imshow(radial_fade(painting))

    plt.show()

if __name__ == "__main__":
    main()
