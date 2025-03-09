#!/usr/bin/env python3

# Exercise 4.7 (subsetting with loc)
# Write function subsetting_with_loc that in one go takes the subset of municipalities from Akaa to Äänekoski and restricts it to columns: "Population", "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %". The function should return this content as a DataFrame. Use the attribute loc.

import pandas as pd

def subsetting_with_loc():

    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)

    df = df["Akaa":"Äänekoski"]

    df = df.loc[:, [
        'Population',
        'Share of Swedish-speakers of the population, %',
        'Share of foreign citizens of the population, %'
    ]]

    return df

def main():

    print(subsetting_with_loc())
    return

if __name__ == "__main__":
    main()
