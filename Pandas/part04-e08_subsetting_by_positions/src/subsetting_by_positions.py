#!/usr/bin/env python3

# Exercise 4.8 (subsetting by positions)
# Write function subsetting_by_positions that does the following.

# Read the data set of the top forty singles from the beginning of the year 1964 from the src folder. Return the top 10 entries and only the columns Title and Artist. Get these elements by their positions, that is, by using a single call to the iloc attribute. The function should return these as a DataFrame.

import pandas as pd

def subsetting_by_positions():

    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", index_col=0)

    df = df.iloc[0:10, [1, 2]]

    return df

def main():

    print(subsetting_by_positions())

    return

if __name__ == "__main__":
    main()
