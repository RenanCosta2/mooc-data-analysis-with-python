#!/usr/bin/env python3

# Exercise 3.13 (read series)
# Write function read_series that reads input lines from the user and return a Series. Each line should contain first the index and then the corresponding value, separated by whitespace. The index and values are strings (in this case dtype is object). An empty line signals the end of Series. Malformed input should cause an exception. An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.

# Test your function from the main function.

import pandas as pd

def read_series():

    keys = []
    values = []

    while(True):
        line = input("Write key and value separated by whitespace: ")

        if not line:
            break

        line_splited = line.split()

        if(len(line_splited) != 2):
            raise Exception("Invalid input")

        keys.append(line_splited[0])
        values.append(line_splited[1])

    return pd.Series(values, index=keys)

def main():
    
    series = read_series()

    print(series)

if __name__ == "__main__":
    main()
