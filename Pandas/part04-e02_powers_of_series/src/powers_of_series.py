#!/usr/bin/env python3

# Exercise 4.2 (powers of series)
# Make function powers_of_series that takes a Series and a positive integer k as parameters and returns a DataFrame. The resulting DataFrame should have the same index as the input Series. The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two. The third column should contain the Series raised to the power of three, and so on until (and including) power of k. The columns should have indices from 1 to k.

# The values should be numbers, but the index can have any type. Test your function from the main function. Example of usage:


# s = pd.Series([1,2,3,4], index=list("abcd"))
# print(powers_of_series(s, 3))
# Should print:

#    1   2   3
# a  1   1   1
# b  2   4   8
# c  3   9  27
# d  4  16  64

import pandas as pd

def powers_of_series(s, k):

    return pd.DataFrame({i: s**i for i in range(1, k+1)})
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 5))
    return
    
if __name__ == "__main__":
    main()
