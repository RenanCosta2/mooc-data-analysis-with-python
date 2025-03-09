#!/usr/bin/env python3

# Exercise 5.3 (top bands)
# Merge the DataFrames UK top40 and the bands DataFrame that are stored in the src folder. Do all this in the parameterless function top_bands, which should return the merged DataFrame. Use the left_on and right_on parameters to merge. Test your function from the main function.

import pandas as pd

def top_bands():

    bands = pd.read_csv("src/bands.tsv", sep="\t")

    bands["Band"] = bands["Band"].str.upper()

    top_40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    top_bands_df = pd.merge(bands, top_40, left_on=["Band"], right_on=["Artist"])

    return top_bands_df

def main():

    print(top_bands())

    return

if __name__ == "__main__":
    main()
