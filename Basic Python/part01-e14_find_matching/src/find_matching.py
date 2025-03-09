#!/usr/bin/env python3

# Exercise 1.14 (find matching)
# Write function find_matching that gets a list of strings and a search string as parameters. The function should return the indices to those elements in the input list that contain the search string. Use the function enumerate.

# An example: find_matching(["sensitive", "engine", "rubbish", "comment"], "en") should return the list [0, 1, 3].

def find_matching(L, pattern):

    indexes = []

    for i, value in enumerate(L):
        if pattern in value:
            indexes.append(i)

    return indexes

def main():
    indexes = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(indexes)

if __name__ == "__main__":
    main()
