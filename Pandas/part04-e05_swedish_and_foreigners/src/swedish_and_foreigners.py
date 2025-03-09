#!/usr/bin/env python3

# Exercise 4.5 (swedish and foreigners)
# Write function swedish_and_foreigners that

# Reads the municipalities data set
# Takes the subset about municipalities (like in previous exercise)
# Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
# From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.
# The function should return this final DataFrame.

# Do you see some kind of correlation between the columns about Swedish speaking and foreign people? Do you see correlation between the columns about the population and the proportion of Swedish speaking people in this subset?

import pandas as pd

def swedish_and_foreigners():

    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)

    df = df["Akaa":"Äänekoski"]

    df = df.drop(columns=[
        "Proportion of the unemployed among the labour force, %",
        "Proportion of pensioners of the population, %",
        "Population change from the previous year, %"
        ])
    
    df = df[
        (df["Share of Swedish-speakers of the population, %"] > 5) &
        (df["Share of foreign citizens of the population, %"] > 5)
        ]

    return df

def main():

    print(swedish_and_foreigners())
    return

if __name__ == "__main__":
    main()
