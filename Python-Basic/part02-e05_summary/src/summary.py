#!/usr/bin/env python3

# Exercise 2.5 (summary)
# This exercise can give two points at maximum!

# Part 1.

# Create a function called summary that gets a filename as a parameter. The input file should contain a floating point number on each line of the file. Make your function read these numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.

# The main function should call the function summary for each filename in the list sys.argv[1:] of command line parameters. (Skip sys.argv[0] since it contains the name of the current program.)

# Example of usage from the command line: python3 src/summary.py src/example.txt src/example2.txt

# Print floating point numbers using six decimals precision. The output should look like this:

# File: src/example.txt Sum: 51.400000 Average: 10.280000 Stddev: 8.904606
# File: src/example2.txt Sum: 5446.200000 Average: 1815.400000 Stddev: 3124.294045
# Part 2.

# If some line doesn’t represent a number, you can just ignore that line. You can achieve this with the try-except block. An example of recovering from an exceptional situation:


# try:
#     x = float(line)           # The float constructor raises ValueError exception if conversion is no possible
# except ValueError:
#     # Statements in here are executed when the above conversion fails
# We will cover more about exceptions later in the course.

import sys
import math

def calculate_standard_deviation(num_list, average):

    standard_deviation = 0
    standard_deviation = sum((num - average) ** 2 for num in num_list)

    standard_deviation = math.sqrt(standard_deviation/(len(num_list) - 1))

    return standard_deviation

def summary(filename):

    sum_nums = 0
    num_quant = 0
    num_list = []

    with open(filename, 'r') as f:
        for line in f:
            try:
                num_quant += 1
                num = float(line)
                sum_nums += num
                num_list.append(num)
            except:
                num = num

    average = sum_nums/num_quant
    standard_deviation = calculate_standard_deviation(num_list, average)

    return (round(sum_nums, 6), round(average, 6), round(standard_deviation, 6))

def main():
    for filename in sys.argv[1:]:
        triple = summary(filename)
        print(f"File: {filename} Sum: {triple[0]:.6f} Average: {triple[1]:.6f} Stddev: {triple[2]:.6f}")

if __name__ == "__main__":
    main()
