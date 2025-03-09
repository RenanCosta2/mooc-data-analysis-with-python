#!/usr/bin/env python3

# Exercise 2.6 (file count)
# This exercise can give two points at maximum!

# Part 1.

# Create a function file_count that gets a filename as parameter and returns a triple of numbers. The function should read the file, count the number of lines, words, and characters in the file, and return a triple with these count in this order. You get division into words by splitting at whitespace. You don't have to remove punctuation.

# Part 2.

# Create a main function that in a loop calls file_count using each filename in the list of command line parameters sys.argv[1:] as a parameter, in turn. For call python3 src/file_count file1 file2 ... the output should be

# ?      ?       ?       file1
# ?      ?       ?       file2
# ...
# The fields are separated by tabs (\t). The fields are in order: linecount, wordcount, charactercount, filename.

import sys

def file_count(filename):

    lines = 0
    words = 0
    characters = 0

    with open(filename, 'r') as f:
        for line in f:
            line_split = line.split()

            characters += len(line)
            words += len(line_split)
            lines += 1

    return (lines, words, characters)

def main():
    for filename in sys.argv[1:]:
        count = file_count(filename)
        print(f'{count[0]}\t{count[1]}\t{count[2]}\t{filename}')

if __name__ == "__main__":
    main()
