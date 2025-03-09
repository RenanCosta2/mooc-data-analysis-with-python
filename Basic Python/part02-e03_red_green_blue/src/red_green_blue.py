#!/usr/bin/env python3

# Exercise 2.3 (red green blue)
# The file src/rgb.txt contains names of colors and their numerical representations in RGB format. The RGB format allows a color to be represented as a mixture of red, green, and blue components. Each component can have an integer value in the range [0,255]. Each line in the file contains four fields: red, green, blue, and colorname. Each field is separated by some amount of whitespace (tab or space in this case). The text file is formatted to make it print nicely, but that makes it harder to process by a computer. Note that some color names can also contain a space character.

# Write function red_green_blue that reads the file rgb.txt from the folder src. Remove the irrelevant first line of the file. The function should return a list of strings. Clean-up the file so that the strings in the returned list have four fields separated by a single tab character (\t). Use regular expressions to do this.

# The first string in the returned list should be:

# '255\t250\t250\tsnow'

import re
import os

def red_green_blue():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "rgb.txt")

    with open(filename, "r") as f:

        list = []

        for line in f:
            line_tab = re.search(r'(\d+\s*\d+\s*\d+)(\s*\w+\s*\w*)', line)
            rgb_code = re.sub(r'\s+', '\t', line_tab.group(1))
            rgb_name = re.sub(r'^\s+', '\t', line_tab.group(2))
            rgb_name = re.sub(r'\s+$', '', rgb_name)
            rgb = rgb_code + rgb_name
            list.append(rgb)

    return list


def main():
    list = red_green_blue()
    print(list)

if __name__ == "__main__":
    main()
