#!/usr/bin/env python3

# Exercise 1.16 (transform)
# Write a function transform that gets two strings as parameters and returns a list of integers. The function should split the strings into words, and convert these words to integers. This should give two lists of integers. Then the function should return a list whose elements are multiplication of two integers in the respective positions in the lists. For example transform("1 5 3", "2 6 -1") should return the list of integers [2, 30, -3].

# You have to use split, map, and zip functions/methods. You may assume that the two input strings are in correct format.

def transform(s1, s2):
    s1_splited = s1.split()
    s2_splited = s2.split()

    s1_splited = list(map(int, s1_splited))
    s2_splited = list(map(int, s2_splited))

    s3 = []

    for s1_value, s2_value in zip(s1_splited, s2_splited):
        s3.append(s1_value*s2_value)


    return s3

def main():
    s = transform("1 5 3", "2 6 -1")
    print(s)

if __name__ == "__main__":
    main()
