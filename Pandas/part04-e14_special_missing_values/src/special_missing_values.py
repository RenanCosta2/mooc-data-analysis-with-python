#!/usr/bin/env python3

# Exercise 4.14 (special missing values)
# Write function special_missing_values that does the following.

# Read the data set of the top forty singles from the beginning of the year 1964 from the src folder. Return the rows whose singles' position dropped compared to last week's position (column LW=Last Week).

# To do this you first have to convert the special values "New" and "Re" (Re-entry) to missing values (None).

import pandas as pd
import numpy as np

def special_missing_values():

    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    print(df.shape)

    df.replace(["New", "Re"], np.nan, inplace=True)
    df = df.astype({"LW" : float})

    dropped = df.loc[df.LW < df.Pos]

    return dropped

def main():

    print(special_missing_values())

    return

if __name__ == "__main__":
    main()
