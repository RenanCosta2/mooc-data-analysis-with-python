#!/usr/bin/env python3

# Exercise 4.6 (growing municipalities)
# Write function growing_municipalities that gets subset of municipalities (a DataFrame) as a parameter and returns the proportion of municipalities with increasing population in that subset.

# Test your function from the main function using some subset of the municipalities. Print the proportion as percentages using 1 decimal precision.

# Example output:

# Proportion of growing municipalities: 12.4%

import pandas as pd

def growing_municipalities(df):
    growing = df[df["Population change from the previous year, %"] > 0]

    return (growing["Population change from the previous year, %"].count()) / (df["Population change from the previous year, %"].count())

def main():

    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)

    df = df["Akaa":"Äänekoski"]

    proportion = growing_municipalities(df)

    print(f"Proportion of growing municipalities: {proportion*100:.1f}%")

    return

if __name__ == "__main__":
    main()
